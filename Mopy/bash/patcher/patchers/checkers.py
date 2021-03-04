# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#  This file is part of Wrye Bash.
#
#  Wrye Bash is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
#
#  Wrye Bash is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Wrye Bash.  If not, see <https://www.gnu.org/licenses/>.
#
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2021 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================
"""This module houses checkers. A checker is a patcher that verifies certain
properties about records and either notifies the user or attempts a fix when it
notices a problem."""

import re
from collections import defaultdict
from itertools import chain
# Internal
from ..base import Patcher
from ... import bush
from ...bolt import GPath, deprint
from ...brec import strFid

class ContentsCheckerPatcher(Patcher):
    """Checks contents of leveled lists, inventories and containers for
    correct content types."""
    patcher_group = u'Special'
    patcher_order = 50
    contType_entryTypes = bush.game.cc_valid_types
    contTypes = set(contType_entryTypes)
    entryTypes = set(chain.from_iterable(contType_entryTypes.itervalues()))
    _read_sigs = tuple(contTypes | entryTypes)

    def __init__(self, p_name, p_file):
        super(ContentsCheckerPatcher, self).__init__(p_name, p_file)
        self.fid_to_type = {}
        self.id_eid = {}

    @property
    def active_write_sigs(self):
        return tuple(self.contTypes) if self.isActive else ()

    def scanModFile(self, modFile, progress):
        """Scan modFile."""
        # First, map fids to record type for all records for the valid record
        # types. We need to know if a given fid belongs to one of the valid
        # types, otherwise we want to remove it.
        id_type = self.fid_to_type
        for entry_type in self.entryTypes:
            if entry_type not in modFile.tops: continue
            for record in modFile.tops[entry_type].getActiveRecords():
                fid = record.fid
                if fid not in id_type:
                    id_type[fid] = entry_type
        # Second, make sure the Bashed Patch contains all records for all the
        # types we may end up patching
        for cont_type in self.contTypes:
            if cont_type not in modFile.tops: continue
            patchBlock = self.patchFile.tops[cont_type]
            pb_add_record = patchBlock.setRecord
            id_records = patchBlock.id_records
            for record in modFile.tops[cont_type].getActiveRecords():
                if record.fid not in id_records:
                    pb_add_record(record.getTypeCopy())

    def buildPatch(self,log,progress):
        """Make changes to patchfile."""
        if not self.isActive: return
        modFile = self.patchFile
        keep = self.patchFile.getKeeper()
        fid_to_type = self.fid_to_type
        id_eid = self.id_eid
        log.setHeader(u'= ' + self._patcher_name)
        # Execute each pass - one pass is needed for every distinct record
        # class layout, e.g. leveled list classes generally share the same
        # layout (LVLI.entries[i].listId, LVLN.entries[i].listId, etc.)
        # whereas CONT, NPC_, etc. have a different layout (CONT.items[i].item,
        # NPC_.items[i].item)
        for cc_pass in bush.game.cc_passes:
            # Validate our pass syntax first
            if len(cc_pass) not in (2, 3):
                raise RuntimeError(u'Unknown Contents Checker pass type %r' %
                                   cc_pass)
            # See explanation below (entry_fid definition)
            needs_entry_attr = len(cc_pass) == 3
            # First entry in the pass is always the record types this pass
            # applies to
            for rec_type in cc_pass[0]:
                if rec_type not in modFile.tops: continue
                # Set up a dict to track which entries we have removed per fid
                id_removed = defaultdict(list)
                # Grab the types that are actually valid for our current record
                # types
                valid_types = set(self.contType_entryTypes[rec_type])
                for record in modFile.tops[rec_type].records:
                    group_attr = cc_pass[1]
                    # Set up two lists, one containing the current record
                    # contents, and a second one that we will be filling with
                    # only valid entries.
                    new_entries = []
                    current_entries = getattr(record, group_attr)
                    for entry in current_entries:
                        # If len(cc_pass) == 3, then this is a list of
                        # MelObject instances, so we have to take an additional
                        # step to retrieve the fids (e.g. for MelGroups or
                        # MelStructs)
                        entry_fid = getattr(entry, cc_pass[2]) \
                            if needs_entry_attr else entry
                        # Actually check if the fid has the correct type. If
                        # it's not valid, then this will return None, which is
                        # obviously not in the valid_types.
                        if fid_to_type.get(entry_fid, None) in valid_types:
                            # The type is valid, so grow our new list
                            new_entries.append(entry)
                        else:
                            # The type is wrong, so discard the entry. At this
                            # point, we know that the lists have diverged - but
                            # we need to keep going, there may be more invalid
                            # entries for this record.
                            id_removed[record.fid].append(entry_fid)
                            id_eid[record.fid] = record.eid
                    # Check if after filtering using the code above, our two
                    # lists have diverged and, if so, keep the changed record
                    if len(new_entries) != len(current_entries):
                        setattr(record, group_attr, new_entries)
                        keep(record.fid)
                # Log the result if we removed at least one entry
                if id_removed:
                    log(u'\n=== ' + rec_type)
                    for contId in sorted(id_removed):
                        log(u'* ' + id_eid[contId])
                        for removedId in sorted(id_removed[contId]):
                            log(u'  . %s: %06X' % (removedId[0],
                                                   removedId[1]))

#------------------------------------------------------------------------------
_main_master = GPath(bush.game.master_file)
class EyeCheckerPatcher(Patcher):
    patcher_group = u'Special'
    patcher_order = 29 # Run before Tweak Races
    _read_sigs = (b'EYES', b'RACE')

    def __init__(self, p_name, p_file):
        super(EyeCheckerPatcher, self).__init__(p_name, p_file)
        self.isActive = True ##: Always enabled to support eye filtering?
        self.eye_mesh = {}

    @property
    def active_write_sigs(self):
        return (b'RACE',) if self.isActive else ()

    def scanModFile(self, modFile, progress):
        if b'RACE' not in modFile.tops: return
        eye_mesh = self.eye_mesh
        patchBlock = self.patchFile.tops[b'RACE']
        id_records = patchBlock.id_records
        srcEyes = {record.fid for record in
                   modFile.tops[b'EYES'].getActiveRecords()}
        for record in modFile.tops[b'RACE'].getActiveRecords():
            if record.fid not in id_records:
                patchBlock.setRecord(record.getTypeCopy())
            if not record.rightEye or not record.leftEye:
                # Don't complain if the FULL is missing, that probably means
                # it's an internal or unused RACE
                if record.full:
                    deprint(u'No right and/or no left eye recorded in race '
                        u'%s, from mod %s' % (record.full, modFile.fileInfo))
                continue
            for eye in record.eyes:
                if eye in srcEyes:
                    eye_mesh[eye] = (record.rightEye.modPath.lower(),
                                     record.leftEye.modPath.lower())

    def buildPatch(self, log, progress):
        if not self.isActive: return
        patchFile = self.patchFile
        if b'RACE' not in patchFile.tops: return
        racesFiltered = []
        keep = patchFile.getKeeper()
        #--Eye Mesh filtering
        eye_mesh = self.eye_mesh
        try:
            blueEyeMesh = eye_mesh[(_main_master, 0x27308)]
        except KeyError:
            print(u'error getting blue eye mesh:')
            print(u'eye meshes:', eye_mesh)
            raise
        argonianEyeMesh = eye_mesh[(_main_master, 0x3e91e)]
        for eye in (
            (_main_master, 0x1a), #--Reanimate
            (_main_master, 0x54bb9), #--Dark Seducer
            (_main_master, 0x54bba), #--Golden Saint
            (_main_master, 0x5fa43), #--Ordered
            ):
            eye_mesh.setdefault(eye,blueEyeMesh)
        def setRaceEyeMesh(race,rightPath,leftPath):
            race.rightEye.modPath = rightPath
            race.leftEye.modPath = leftPath
        for race in patchFile.tops[b'RACE'].records:
            if not race.eyes: continue  #--Sheogorath. Assume is handled
            # correctly.
            if not race.rightEye or not race.leftEye: continue #--WIPZ race?
            if re.match(u'^117[a-zA-Z]', race.eid, flags=re.U): continue  #--
            #  x117 race?
            raceChanged = False
            mesh_eye = {}
            for eye in race.eyes:
                if eye not in eye_mesh:
                    deprint(
                        _(u'Mesh undefined for eye %s in race %s, eye removed '
                          u'from race list.') % (
                            strFid(eye), race.eid,))
                    continue
                mesh = eye_mesh[eye]
                if mesh not in mesh_eye:
                    mesh_eye[mesh] = []
                mesh_eye[mesh].append(eye)
            currentMesh = (
                race.rightEye.modPath.lower(), race.leftEye.modPath.lower())
            try:
                maxEyesMesh = sorted(mesh_eye, key=lambda a: len(mesh_eye[a]),
                                     reverse=True)[0]
            except IndexError:
                maxEyesMesh = blueEyeMesh
            #--Single eye mesh, but doesn't match current mesh?
            if len(mesh_eye) == 1 and currentMesh != maxEyesMesh:
                setRaceEyeMesh(race,*maxEyesMesh)
                raceChanged = True
            #--Multiple eye meshes (and playable)?
            if len(mesh_eye) > 1 and (race.flags.playable or race.fid == (
                    _main_master, 0x038010)):
                #--If blueEyeMesh (mesh used for vanilla eyes) is present,
                # use that.
                if blueEyeMesh in mesh_eye and currentMesh != argonianEyeMesh:
                    setRaceEyeMesh(race,*blueEyeMesh)
                    race.eyes = mesh_eye[blueEyeMesh]
                    raceChanged = True
                elif argonianEyeMesh in mesh_eye:
                    setRaceEyeMesh(race,*argonianEyeMesh)
                    race.eyes = mesh_eye[argonianEyeMesh]
                    raceChanged = True
                #--Else figure that current eye mesh is the correct one
                elif currentMesh in mesh_eye:
                    race.eyes = mesh_eye[currentMesh]
                    raceChanged = True
                #--Else use most popular eye mesh
                else:
                    setRaceEyeMesh(race,*maxEyesMesh)
                    race.eyes = mesh_eye[maxEyesMesh]
                    raceChanged = True
            if raceChanged:
                racesFiltered.append(race.eid)
                keep(race.fid)
        log.setHeader(u'= ' + self._patcher_name)
        log(u'\n=== ' + _(u'Eye Meshes Filtered'))
        if not racesFiltered:
            log(u'. ~~%s~~' % _(u'None'))
        else:
            log(_(u"In order to prevent 'googly eyes', incompatible eyes have "
                  u'been removed from the following races.'))
            for eid in sorted(racesFiltered):
                log(u'* ' + eid)

#------------------------------------------------------------------------------
class RaceCheckerPatcher(Patcher):
    patcher_group = u'Special'
    patcher_order = 40 # Run after Tweak Races
    _read_sigs = (b'EYES', b'HAIR', b'RACE')

    @property
    def active_write_sigs(self):
        return (b'RACE',) if self.isActive else ()

    def scanModFile(self, modFile, progress):
        if not (set(modFile.tops) & set(self._read_sigs)): return
        for pb_sig in self._read_sigs:
            patchBlock = self.patchFile.tops[pb_sig]
            id_records = patchBlock.id_records
            for record in modFile.tops[pb_sig].getActiveRecords():
                if record.fid not in id_records:
                    patchBlock.setRecord(record.getTypeCopy())

    def buildPatch(self, log, progress):
        if not self.isActive: return
        patchFile = self.patchFile
        if b'RACE' not in patchFile.tops: return
        keep = patchFile.getKeeper()
        racesSorted = []
        eyeNames = {x.fid: x.full for x in patchFile.tops[b'EYES'].records}
        hairNames = {x.fid: x.full for x in patchFile.tops[b'HAIR'].records}
        for race in patchFile.tops[b'RACE'].records:
            if (race.flags.playable or race.fid == (
                    _main_master, 0x038010)) and race.eyes:
                prev_hairs = race.hairs[:]
                race.hairs.sort(key=lambda x: hairNames.get(x))
                prev_eyes = race.eyes[:]
                race.eyes.sort(key=lambda x: eyeNames.get(x))
                if race.hairs != prev_hairs or race.eyes != prev_eyes:
                    racesSorted.append(race.eid)
                    keep(race.fid)
        log.setHeader(u'= ' + self._patcher_name)
        log(u'\n=== ' + _(u'Eyes/Hair Sorted'))
        if not racesSorted:
            log(u'. ~~%s~~' % _(u'None'))
        else:
            for eid in sorted(racesSorted):
                log(u'* ' + eid)
