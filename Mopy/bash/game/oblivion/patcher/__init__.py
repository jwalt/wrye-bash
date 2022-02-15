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
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2022 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================

"""This package contains the Oblivion specific patchers. This module
contains the data structures that are dynamically set on a per game basis in
bush."""
# ***no imports!***

# Function Info ---------------------------------------------------------------
# 0: no param; 1: int param; 2: formid param; 3: float param
condition_function_data = {
    1:    (u'GetDistance', 2, 0),
    5:    (u'GetLocked', 0, 0),
    6:    (u'GetPos', 1, 0),
    8:    (u'GetAngle', 1, 0),
    10:   (u'GetStartingPos', 1, 0),
    11:   (u'GetStartingAngle', 1, 0),
    12:   (u'GetSecondsPassed', 0, 0),
    14:   (u'GetActorValue', 1, 0),
    18:   (u'GetCurrentTime', 0, 0),
    24:   (u'GetScale', 0, 0),
    27:   (u'GetLineOfSight', 2, 0),
    32:   (u'GetInSameCell', 2, 0),
    35:   (u'GetDisabled', 0, 0),
    36:   (u'MenuMode', 1, 0),
    39:   (u'GetDisease', 0, 0),
    40:   (u'GetVampire', 0, 0),
    41:   (u'GetClothingValue', 0, 0),
    42:   (u'SameFaction', 2, 0),
    43:   (u'SameRace', 2, 0),
    44:   (u'SameSex', 2, 0),
    45:   (u'GetDetected', 2, 0),
    46:   (u'GetDead', 0, 0),
    47:   (u'GetItemCount', 2, 0),
    48:   (u'GetGold', 0, 0),
    49:   (u'GetSleeping', 0, 0),
    50:   (u'GetTalkedToPC', 0, 0),
    53:   (u'GetScriptVariable', 2, 1),
    56:   (u'GetQuestRunning', 2, 0),
    58:   (u'GetStage', 2, 0),
    59:   (u'GetStageDone', 2, 1),
    60:   (u'GetFactionRankDifference', 2, 2),
    61:   (u'GetAlarmed', 0, 0),
    62:   (u'IsRaining', 0, 0),
    63:   (u'GetAttacked', 0, 0),
    64:   (u'GetIsCreature', 0, 0),
    65:   (u'GetLockLevel', 0, 0),
    66:   (u'GetShouldAttack', 2, 0),
    67:   (u'GetInCell', 2, 0),
    68:   (u'GetIsClass', 2, 0),
    69:   (u'GetIsRace', 2, 0),
    70:   (u'GetIsSex', 1, 0),
    71:   (u'GetInFaction', 2, 0),
    72:   (u'GetIsID', 2, 0),
    73:   (u'GetFactionRank', 2, 0),
    74:   (u'GetGlobalValue', 2, 0),
    75:   (u'IsSnowing', 0, 0),
    76:   (u'GetDisposition', 2, 0),
    77:   (u'GetRandomPercent', 0, 0),
    79:   (u'GetQuestVariable', 2, 1),
    80:   (u'GetLevel', 0, 0),
    81:   (u'GetArmorRating', 0, 0),
    84:   (u'GetDeadCount', 2, 0),
    91:   (u'GetIsAlerted', 0, 0),
    98:   (u'GetPlayerControlsDisabled', 0, 0),
    99:   (u'GetHeadingAngle', 2, 0),
    101:  (u'IsWeaponOut', 0, 0),
    102:  (u'IsTorchOut', 0, 0),
    103:  (u'IsShieldOut', 0, 0),
    104:  (u'IsYielding', 0, 0),
    106:  (u'IsFacingUp', 0, 0),
    107:  (u'GetKnockedState', 0, 0),
    108:  (u'GetWeaponAnimType', 0, 0),
    109:  (u'GetWeaponSkillType', 0, 0),
    110:  (u'GetCurrentAIPackage', 0, 0),
    111:  (u'IsWaiting', 0, 0),
    112:  (u'IsIdlePlaying', 0, 0),
    116:  (u'GetCrimeGold', 0, 0),
    122:  (u'GetCrime', 2, 1),
    125:  (u'IsGuard', 0, 0),
    127:  (u'CanPayCrimeGold', 0, 0),
    128:  (u'GetFatiguePercentage', 0, 0),
    129:  (u'GetPCIsClass', 2, 0),
    130:  (u'GetPCIsRace', 2, 0),
    131:  (u'GetPCIsSex', 1, 0),
    132:  (u'GetPCInFaction', 2, 0),
    133:  (u'SameFactionAsPC', 0, 0),
    134:  (u'SameRaceAsPC', 0, 0),
    135:  (u'SameSexAsPC', 0, 0),
    136:  (u'GetIsReference', 2, 0),
    141:  (u'IsTalking', 0, 0),
    142:  (u'GetWalkSpeed', 0, 0),
    143:  (u'GetCurrentAIProcedure', 0, 0),
    144:  (u'GetTrespassWarningLevel', 0, 0),
    145:  (u'IsTrespassing', 0, 0),
    146:  (u'IsInMyOwnedCell', 0, 0),
    147:  (u'GetWindSpeed', 0, 0),
    148:  (u'GetCurrentWeatherPercent', 0, 0),
    149:  (u'GetIsCurrentWeather', 2, 0),
    150:  (u'IsContinuingPackagePCNear', 0, 0),
    153:  (u'CanHaveFlames', 0, 0),
    154:  (u'HasFlames', 0, 0),
    157:  (u'GetOpenState', 0, 0),
    159:  (u'GetSitting', 0, 0),
    160:  (u'GetFurnitureMarkerID', 0, 0),
    161:  (u'GetIsCurrentPackage', 2, 0),
    162:  (u'IsCurrentFurnitureRef', 2, 0),
    163:  (u'IsCurrentFurnitureObj', 2, 0),
    170:  (u'GetDayOfWeek', 0, 0),
    171:  (u'IsPlayerInJail', 0, 0),
    172:  (u'GetTalkedToPCParam', 2, 0),
    175:  (u'IsPCSleeping', 0, 0),
    176:  (u'IsPCAMurderer', 0, 0),
    180:  (u'GetDetectionLevel', 2, 0),
    182:  (u'GetEquipped', 2, 0),
    185:  (u'IsSwimming', 0, 0),
    190:  (u'GetAmountSoldStolen', 0, 0),
    193:  (u'GetPCExpelled', 2, 0),
    195:  (u'GetPCFactionMurder', 2, 0),
    197:  (u'GetPCFactionSteal', 2, 0),
    199:  (u'GetPCFactionAttack', 2, 0),
    201:  (u'GetPCFactionSubmitAuthority', 2, 0),
    203:  (u'GetDestroyed', 0, 0),
    214:  (u'HasMagicEffect', 2, 0),
    215:  (u'GetDoorDefaultOpen', 0, 0),
    223:  (u'IsSpellTarget', 2, 0),
    224:  (u'GetIsPlayerBirthsign', 2, 0),
    225:  (u'GetPersuasionNumber', 0, 0),
    227:  (u'HasVampireFed', 0, 0),
    228:  (u'GetIsClassDefault', 2, 0),
    229:  (u'GetClassDefaultMatch', 0, 0),
    230:  (u'GetInCellParam', 2, 2),
    237:  (u'GetIsGhost', 0, 0),
    242:  (u'GetUnconscious', 0, 0),
    244:  (u'GetRestrained', 0, 0),
    246:  (u'GetIsUsedItem', 2, 0),
    247:  (u'GetIsUsedItemType', 1, 0),
    249:  (u'GetPCFame', 0, 0),
    251:  (u'GetPCInfamy', 0, 0),
    254:  (u'GetIsPlayableRace', 0, 0),
    255:  (u'GetOffersServicesNow', 0, 0),
    258:  (u'GetUsedItemLevel', 0, 0),
    259:  (u'GetUsedItemActivate', 0, 0),
    264:  (u'GetBarterGold', 0, 0),
    265:  (u'IsTimePassing', 0, 0),
    266:  (u'IsPleasant', 0, 0),
    267:  (u'IsCloudy', 0, 0),
    274:  (u'GetArmorRatingUpperBody', 0, 0),
    277:  (u'GetBaseActorValue', 1, 0),
    278:  (u'IsOwner', 2, 0),
    280:  (u'IsCellOwner', 2, 2),
    282:  (u'IsHorseStolen', 0, 0),
    285:  (u'IsLeftUp', 0, 0),
    286:  (u'IsSneaking', 0, 0),
    287:  (u'IsRunning', 0, 0),
    288:  (u'GetFriendHit', 2, 0),
    289:  (u'IsInCombat', 0, 0),
    300:  (u'IsInInterior', 0, 0),
    305:  (u'GetInvestmentGold', 0, 0),
    306:  (u'IsActorUsingATorch', 0, 0),
    309:  (u'IsXBox', 0, 0),
    310:  (u'GetInWorldspace', 2, 0),
    312:  (u'GetPCMiscStat', 1, 0),
    313:  (u'IsActorEvil', 0, 0),
    314:  (u'IsActorAVictim', 0, 0),
    315:  (u'GetTotalPersuasionNumber', 0, 0),
    318:  (u'GetIdleDoneOnce', 0, 0),
    320:  (u'GetNoRumors', 0, 0),
    323:  (u'WhichServiceMenu', 0, 0),
    327:  (u'IsRidingHorse', 0, 0),
    329:  (u'IsTurnArrest', 0, 0),
    332:  (u'IsInDangerousWater', 0, 0),
    338:  (u'GetIgnoreFriendlyHits', 0, 0),
    339:  (u'IsPlayersLastRiddenHorse', 0, 0),
    353:  (u'IsActor', 0, 0),
    354:  (u'IsEssential', 0, 0),
    358:  (u'IsPlayerMovingIntoNewSpace', 0, 0),
    361:  (u'GetTimeDead', 0, 0),
    362:  (u'GetPlayerHasLastRiddenHorse', 0, 0),
    365:  (u'GetPlayerInSEWorld', 0, 0),

    # extended by OBSE
    1107: (u'IsAmmo', 1, 0),
    1884: (u'GetPCTrainingSessionsUsed', 2, 0),
    2213: (u'GetPackageOffersServices', 2, 0),
    2214: (u'GetPackageMustReachLocation', 2, 0),
    2215: (u'GetPackageMustComplete', 2, 0),
    2216: (u'GetPackageLockDoorsAtStart', 2, 0),
    2217: (u'GetPackageLockDoorsAtEnd', 2, 0),
    2218: (u'GetPackageLockDoorsAtLocation', 2, 0),
    2219: (u'GetPackageUnlockDoorsAtStart', 2, 0),
    2220: (u'GetPackageUnlockDoorsAtEnd', 2, 0),
    2221: (u'GetPackageUnlockDoorsAtLocation', 2, 0),
    2222: (u'GetPackageContinueIfPCNear', 2, 0),
    2223: (u'GetPackageOncePerDay', 2, 0),
    2224: (u'GetPackageSkipFalloutBehavior', 2, 0),
    2225: (u'GetPackageAlwaysRun', 2, 0),
    2226: (u'GetPackageAlwaysSneak', 2, 0),
    2227: (u'GetPackageAllowSwimming', 2, 0),
    2228: (u'GetPackageAllowFalls', 2, 0),
    2229: (u'GetPackageArmorUnequipped', 2, 0),
    2230: (u'GetPackageWeaponsUnequipped', 2, 0),
    2231: (u'GetPackageDefensiveCombat', 2, 0),
    2232: (u'GetPackageUseHorse', 2, 0),
    2233: (u'GetPackageNoIdleAnims', 2, 0),
}

# Known record types
save_rec_types = {
    6 : _(u'Faction'),
    19: _(u'Apparatus'),
    20: _(u'Armor'),
    21: _(u'Book'),
    22: _(u'Clothing'),
    25: _(u'Ingredient'),
    26: _(u'Light'),
    27: _(u'Misc. Item'),
    33: _(u'Weapon'),
    35: _(u'NPC'),
    36: _(u'Creature'),
    39: _(u'Key'),
    40: _(u'Potion'),
    48: _(u'Cell'),
    49: _(u'Object Ref'),
    50: _(u'NPC Ref'),
    51: _(u'Creature Ref'),
    58: _(u'Dialog Entry'),
    59: _(u'Quest'),
    61: _(u'AI Package'),
}

#------------------------------------------------------------------------------
# Leveled Lists
#------------------------------------------------------------------------------
listTypes = (b'LVLC',b'LVLI',b'LVSP',)

#------------------------------------------------------------------------------
# Import Prices
#------------------------------------------------------------------------------
namesTypes = {b'ALCH', b'AMMO', b'APPA', b'ARMO', b'BOOK', b'BSGN', b'CLAS',
              b'CLOT', b'CONT', b'CREA', b'DOOR', b'ENCH', b'EYES', b'FACT',
              b'FLOR', b'HAIR', b'INGR', b'KEYM', b'LIGH', b'MGEF', b'MISC',
              b'NPC_', b'RACE', b'SGST', b'SLGM', b'SPEL', b'WEAP'}

#------------------------------------------------------------------------------
# Import Prices
#------------------------------------------------------------------------------
pricesTypes = {b'ALCH', b'AMMO', b'APPA', b'ARMO', b'BOOK', b'CLOT', b'INGR',
               b'KEYM', b'LIGH', b'MISC', b'SGST', b'SLGM', b'WEAP'}

#------------------------------------------------------------------------------
# Import Stats
#------------------------------------------------------------------------------
# The contents of these tuples has to stay fixed because of CSV parsers
statsTypes = {
    b'ALCH': ('eid', 'weight', 'value'),
    b'AMMO': ('eid', 'weight', 'value', 'damage', 'speed', 'enchantPoints'),
    b'APPA': ('eid', 'weight', 'value', 'quality'),
    b'ARMO': ('eid', 'weight', 'value', 'health', 'strength'),
    b'BOOK': ('eid', 'weight', 'value', 'enchantPoints'),
    b'CLOT': ('eid', 'weight', 'value', 'enchantPoints'),
    b'INGR': ('eid', 'weight', 'value'),
    b'KEYM': ('eid', 'weight', 'value'),
    b'LIGH': ('eid', 'weight', 'value', 'duration'),
    b'MISC': ('eid', 'weight', 'value'),
    b'SGST': ('eid', 'weight', 'value', 'uses'),
    b'SLGM': ('eid', 'weight', 'value'),
    b'WEAP': ('eid', 'weight', 'value', 'health', 'damage', 'speed', 'reach',
              'enchantPoints'),
}

#------------------------------------------------------------------------------
# Import Sounds
#------------------------------------------------------------------------------
soundsTypes = {
    b'ACTI': (u'sound',),
    b'CONT': (u'soundOpen', u'soundClose'),
    b'CREA': (u'footWeight', u'inheritsSoundsFrom', u'sounds'),
    b'DOOR': (u'soundOpen', u'soundClose', u'soundLoop'),
    b'LIGH': (u'sound',),
    b'MGEF': (u'castingSound', u'boltSound', u'hitSound', u'areaSound'),
#    b'REGN': ('entries.sounds',),
    b'SOUN': (u'soundFile', u'minDistance', u'maxDistance', u'freqAdjustment',
              u'staticAtten', u'stopTime', u'startTime'),
    b'WATR': (u'sound',),
    b'WTHR': (u'sounds',),
}

#------------------------------------------------------------------------------
# Import Cells
#------------------------------------------------------------------------------
cellRecAttrs = {
    u'C.Climate': (u'climate', u'flags.behaveLikeExterior'),
    ##: Patches unuseds?
    u'C.Light': (u'ambientRed', u'ambientGreen', u'ambientBlue', u'unused1',
                 u'directionalRed', u'directionalGreen', u'directionalBlue',
                 u'unused2', u'fogRed', u'fogGreen', u'fogBlue', u'unused3',
                 u'fogNear', u'fogFar', u'directionalXY', u'directionalZ',
                 u'directionalFade', u'fogClip'),
    u'C.MiscFlags': (u'flags.isInterior', u'flags.invertFastTravel',
                     u'flags.forceHideLand', u'flags.handChanged'),
    u'C.Music': (u'music',),
    u'C.Name': (u'full',),
    u'C.Owner': (u'ownership', u'flags.publicPlace'),
    u'C.RecordFlags': (u'flags1',), # Yes seems funky but thats the way it is
    u'C.Regions': (u'regions',),
    u'C.Water': (u'water', u'waterHeight', u'flags.hasWater'),
}

#------------------------------------------------------------------------------
# Import Graphics
#------------------------------------------------------------------------------
graphicsTypes = {
    b'ACTI': (u'model',),
    b'ALCH': (u'iconPath', u'model'),
    b'AMMO': (u'iconPath', u'model'),
    b'APPA': (u'iconPath', u'model'),
    b'ARMO': (u'maleBody', u'maleWorld', u'maleIconPath', u'femaleBody',
              u'femaleWorld', u'femaleIconPath', u'biped_flags'),
    b'BOOK': (u'iconPath', u'model'),
    b'BSGN': (u'iconPath',),
    b'CLAS': (u'iconPath',),
    b'CLOT': (u'maleBody', u'maleWorld', u'maleIconPath', u'femaleBody',
              u'femaleWorld', u'femaleIconPath', u'biped_flags'),
    b'CONT': (u'model',),
    b'CREA': (u'bodyParts', u'nift_p'),
    b'DOOR': (u'model',),
    b'EFSH': (u'particleTexture', u'fillTexture', u'flags', u'unused1',
              u'memSBlend', u'memBlendOp', u'memZFunc', u'fillRed',
              u'fillGreen', u'fillBlue', u'unused2', u'fillAIn', u'fillAFull',
              u'fillAOut', u'fillAPRatio', u'fillAAmp', u'fillAFreq',
              u'fillAnimSpdU', u'fillAnimSpdV', u'edgeOff', u'edgeRed',
              u'edgeGreen', u'edgeBlue', u'unused3', u'edgeAIn', u'edgeAFull',
              u'edgeAOut', u'edgeAPRatio', u'edgeAAmp', u'edgeAFreq',
              u'fillAFRatio', u'edgeAFRatio', u'memDBlend', u'partSBlend',
              u'partBlendOp', u'partZFunc', u'partDBlend', u'partBUp',
              u'partBFull', u'partBDown', u'partBFRatio', u'partBPRatio',
              u'partLTime', u'partLDelta', u'partNSpd', u'partNAcc',
              u'partVel1', u'partVel2', u'partVel3', u'partAcc1', u'partAcc2',
              u'partAcc3', u'partKey1', u'partKey2', u'partKey1Time',
              u'partKey2Time', u'key1Red', u'key1Green', u'key1Blue',
              u'unused4', u'key2Red', u'key2Green', u'key2Blue', u'unused5',
              u'key3Red', u'key3Green', u'key3Blue', u'unused6', u'key1A',
              u'key2A', u'key3A', u'key1Time', u'key2Time', u'key3Time'),
    b'EYES': (u'iconPath',),
    b'FLOR': (u'model',),
    b'FURN': (u'model',),
    b'GRAS': (u'model',),
    b'HAIR': (u'iconPath', u'model'),
    b'INGR': (u'iconPath', u'model'),
    b'KEYM': (u'iconPath', u'model'),
    b'LIGH': (u'iconPath', u'model'),
    b'LSCR': (u'iconPath',),
    b'LTEX': (u'iconPath',),
    b'MGEF': (u'iconPath', u'model'),
    b'MISC': (u'iconPath', u'model'),
    b'QUST': (u'iconPath',),
    b'REGN': (u'iconPath',),
    b'SGST': (u'iconPath', u'model'),
    b'SKIL': (u'iconPath',),
    b'SLGM': (u'iconPath', u'model'),
    b'STAT': (u'model',),
    b'TREE': (u'iconPath', u'model'),
    b'WEAP': (u'iconPath', u'model'),
}
graphicsFidTypes = {
    b'MGEF': (u'light', u'effectShader', u'enchantEffect')
}
graphicsModelAttrs = (u'model', u'maleBody', u'maleWorld', u'femaleBody', u'femaleWorld')
#------------------------------------------------------------------------------
# Import Inventory
#------------------------------------------------------------------------------
inventoryTypes = (b'CREA',b'NPC_',b'CONT',)

#------------------------------------------------------------------------------
# NPC Checker
#------------------------------------------------------------------------------
# Note that we use _x to avoid exposing these to the dynamic importer
def _fid(_x): return None, _x # None <=> game master
def _cobl(_x): return u'Cobl Main.esm', _x
_standard_eyes = [_fid(_x) for _x in (0x27306, 0x27308, 0x27309)] + \
                 [_cobl(_x) for _x in (0x000821, 0x000823, 0x000825, 0x000828,
                                       0x000834, 0x000837, 0x000839, 0x00084F)]
default_eyes = {
    #--Oblivion.esm
    # Argonian
    _fid(0x23FE9): [_fid(0x3E91E)] +
                   [_cobl(_x) for _x in (0x01F407, 0x01F408, 0x01F40B,
                                         0x01F40C, 0x01F410, 0x01F411,
                                         0x01F414, 0x01F416, 0x01F417,
                                         0x01F41A, 0x01F41B, 0x01F41E,
                                         0x01F41F, 0x01F422, 0x01F424)],
    # Breton
    _fid(0x0224FC): _standard_eyes,
    # Dark Elf
    _fid(0x0191C1): [_fid(0x27307)] +
                    [_cobl(_x) for _x in (0x000861, 0x000864, 0x000851)],
    # High Elf
    _fid(0x019204): _standard_eyes,
    # Imperial
    _fid(0x000907): _standard_eyes,
    # Khajiit
    _fid(0x022C37): [_fid(0x375c8)] +
                    [_cobl(_x) for _x in (0x00083B, 0x00083E, 0x000843,
                                          0x000846, 0x000849, 0x00084C)],
    # Nord
    _fid(0x0224FD): _standard_eyes,
    # Orc
    _fid(0x0191C0): [_fid(0x2730A)] +
                    [_cobl(_x) for _x in (0x000853, 0x000855, 0x000858,
                                          0x00085A, 0x00085C, 0x00085E)],
    # Redguard
    _fid(0x000D43): _standard_eyes,
    # Wood Elf
    _fid(0x0223C8): _standard_eyes,
    #--Cobl Main.esm
    # cobRaceAureal
    _cobl(0x07948): [_fid(0x54BBA)],
    # cobRaceHidden
    _cobl(0x02B60): [_cobl(_x) for _x in (0x01F43A, 0x01F438, 0x01F439,
                                          0x0015A7, 0x01792C, 0x0015AC,
                                          0x0015A8, 0x0015AB, 0x0015AA)],
    # cobRaceMazken
    _cobl(0x07947): [_fid(0x54BB9)],
    # cobRaceOhmes
    _cobl(0x1791B): [_cobl(_x) for _x in (0x017901, 0x017902, 0x017903,
                                          0x017904, 0x017905, 0x017906,
                                          0x017907, 0x017908, 0x017909,
                                          0x01790A, 0x01790B, 0x01790C,
                                          0x01790D, 0x01790E, 0x01790F,
                                          0x017910, 0x017911, 0x017912,
                                          0x017913, 0x017914, 0x017915,
                                          0x017916, 0x017917, 0x017918,
                                          0x017919, 0x01791A, 0x017900)],
    # cobRaceXivilai
    _cobl(0x1F43C): [_cobl(_x) for _x in (0x01F437, 0x00531B, 0x00531C,
                                          0x00531D, 0x00531E, 0x00531F,
                                          0x005320, 0x005321, 0x01F43B,
                                          0x00DBE1)],
}
# Clean these up, no need to keep them around now
del _cobl, _fid

#------------------------------------------------------------------------------
# Import Text
#------------------------------------------------------------------------------
text_types = {
    b'BOOK': (u'book_text',),
    b'BSGN': (u'description',),
    b'CLAS': (u'description',),
    b'LSCR': (u'description',),
    b'MGEF': (u'description',),
    # omit RACE - covered by R.Description
    b'SKIL': (u'description',),
}

#------------------------------------------------------------------------------
# Contents Checker
#------------------------------------------------------------------------------
# Entry types used for CONT, CREA, LVLI and NPC_
_common_entry_types = {b'ALCH', b'AMMO', b'APPA', b'ARMO', b'BOOK', b'CLOT', b'INGR',
                       b'KEYM', b'LIGH', b'LVLI', b'MISC', b'SGST', b'SLGM', b'WEAP'}
cc_valid_types = {
    b'CONT': _common_entry_types,
    b'CREA': _common_entry_types,
    b'LVLC': {b'CREA', b'LVLC', b'NPC_'},
    b'LVLI': _common_entry_types,
    b'LVSP': {b'LVSP', b'SPEL'},
    b'NPC_': _common_entry_types,
}
cc_passes = (
    ((b'LVLC', b'LVLI', b'LVSP'), 'entries', 'listId'),
    ((b'CONT', b'CREA', b'NPC_'), 'items', 'item'),
)

#------------------------------------------------------------------------------
# Import Scripts
#------------------------------------------------------------------------------
scripts_types = {b'ACTI', b'ALCH', b'APPA', b'ARMO', b'BOOK', b'CLOT', b'CONT',
                 b'CREA', b'DOOR', b'FLOR', b'FURN', b'INGR', b'KEYM', b'LIGH',
                 b'MISC', b'NPC_', b'QUST', b'SGST', b'SLGM', b'WEAP'}

#------------------------------------------------------------------------------
# Import Actors
#------------------------------------------------------------------------------
actor_importer_attrs = {
    b'CREA': {
        u'Actors.ACBS': (u'barterGold', u'baseSpell', u'calcMax', u'calcMin',
                         u'fatigue', u'flags.biped', u'flags.essential',
                         u'flags.flies', u'flags.noBloodDecal',
                         u'flags.noBloodSpray', u'flags.noCombatInWater',
                         u'flags.noCorpseCheck', u'flags.noHead',
                         u'flags.noLeftArm', u'flags.noLowLevel',
                         u'flags.noRightArm', u'flags.noShadow',
                         u'flags.pcLevelOffset', u'flags.respawn',
                         u'flags.swims', u'flags.walks',
                         u'flags.weaponAndShield', u'level_offset'),
        u'Actors.AIData': (u'aggression', u'confidence', u'energyLevel',
                           u'responsibility', u'services', u'trainLevel',
                           u'trainSkill'),
        u'Actors.CombatStyle': (u'combatStyle',),
        u'Actors.RecordFlags': (u'flags1',),
        u'Actors.Skeleton': (u'model',),
        u'Actors.Stats': (u'agility', u'attackDamage', u'combatSkill',
                          u'endurance', u'health', u'intelligence', u'luck',
                          u'magic', u'personality', u'soul', u'stealth',
                          u'speed', u'strength', u'willpower'),
        u'Creatures.Blood': (u'bloodDecalPath', u'bloodSprayPath'),
        u'Creatures.Type': (u'creatureType',),
        u'NPC.Class': (),
        u'NPC.Race': (),
    },
    b'NPC_': {
        u'Actors.ACBS': (u'barterGold', u'baseSpell', u'calcMax', u'calcMin',
                         u'fatigue', u'flags.autoCalc',
                         u'flags.canCorpseCheck', u'flags.essential',
                         u'flags.female', u'flags.noLowLevel',
                         u'flags.noPersuasion', u'flags.noRumors',
                         u'flags.pcLevelOffset', u'flags.respawn',
                         u'flags.summonable', u'level_offset',),
        u'Actors.AIData': (u'aggression', u'confidence', u'energyLevel',
                           u'responsibility', u'services', u'trainSkill',
                           u'trainLevel'),
        u'Actors.CombatStyle': (u'combatStyle',),
        u'Actors.RecordFlags': (u'flags1',),
        u'Actors.Skeleton': (u'model',),
        u'Actors.Stats': (u'attributes', u'health', u'skills',),
        u'Creatures.Blood': (),
        u'Creatures.Type': (),
        u'NPC.Class': (u'iclass',),
        u'NPC.Race': (u'race',),
    },
}
actor_types = (b'CREA', b'NPC_')
spell_types = (b'LVSP', b'SPEL')

#------------------------------------------------------------------------------
# Import Spell Stats
#------------------------------------------------------------------------------
spell_stats_attrs = (u'eid', u'cost', u'level', u'spellType', u'flags')

#------------------------------------------------------------------------------
# Tweak Actors
#------------------------------------------------------------------------------
actor_tweaks = {
    u'VORB_NPCSkeletonPatcher',
    u'MAONPCSkeletonPatcher',
    u'VanillaNPCSkeletonPatcher',
    u'RedguardNPCPatcher',
    u'NoBloodCreaturesPatcher',
    u'AsIntendedImpsPatcher',
    u'AsIntendedBoarsPatcher',
    u'QuietFeetPatcher',
    u'IrresponsibleCreaturesPatcher',
    u'RWALKNPCAnimationPatcher',
    u'SWALKNPCAnimationPatcher',
}

#------------------------------------------------------------------------------
# Tweak Names
#------------------------------------------------------------------------------
names_tweaks = {
    'NamesTweak_BodyPartCodes',
    'NamesTweak_Body_Armor_Tes4',
    'NamesTweak_Body_Clothes',
    'NamesTweak_Ingestibles_Tes4',
    'NamesTweak_NotesScrolls',
    'NamesTweak_Spells',
    'NamesTweak_Weapons_Tes4',
    'NamesTweak_DwarvenToDwemer',
    'NamesTweak_DwarfsToDwarves',
    'NamesTweak_StaffsToStaves',
    'NamesTweak_FatigueToStamina',
    'NamesTweak_MarksmanToArchery',
    'NamesTweak_SecurityToLockpicking',
    'NamesTweak_AmmoWeight',
    'NamesTweak_RenameGold',
}
body_part_codes = (u'ARGHTCCPBS', u'ABGHINOPSL')
text_replacer_rpaths = {
    b'ALCH': ('full', 'effects[i].scriptEffect?.full'),
    b'AMMO': ('full',),
    b'APPA': ('full',),
    b'ARMO': ('full',),
    b'BOOK': ('full', 'book_text'),
    b'BSGN': ('full', 'description'),
    b'CLAS': ('full', 'description'),
    b'CLOT': ('full',),
    b'CONT': ('full',),
    b'CREA': ('full',),
    b'DOOR': ('full',),
    b'ENCH': ('full', 'effects[i].scriptEffect?.full',),
    b'EYES': ('full',),
    b'FACT': ('full',), ##: maybe add male_title/female_title?
    b'FLOR': ('full',),
    b'FURN': ('full',),
    b'GMST': ('value',),
    b'HAIR': ('full',),
    b'INGR': ('full', 'effects[i].scriptEffect?.full'),
    b'KEYM': ('full',),
    b'LIGH': ('full',),
    b'LSCR': ('full', 'description'),
    b'MGEF': ('full', 'description'),
    b'MISC': ('full',),
    b'NPC_': ('full',),
    b'QUST': ('full', 'stages[i].entries[i].text'),
    b'RACE': ('full', 'description'),
    b'SGST': ('full', 'effects[i].scriptEffect?.full'),
    b'SKIL': ('description', 'apprentice', 'journeyman', 'expert', 'master'),
    b'SLGM': ('full',),
    b'SPEL': ('full', 'effects[i].scriptEffect?.full'),
    b'WEAP': ('full',),
}
gold_attrs = lambda _self_ignore, _gm_master: {
    'eid': 'Gold001',
    'model.modPath': r'Clutter\goldCoin01.NIF',
    'model.modb': 1.0,
    'model.modt_p': None,
    'iconPath': r'Clutter\IconGold.dds',
    'value': 1,
    'weight': 0.0,
}

#------------------------------------------------------------------------------
# Tweak Settings
#------------------------------------------------------------------------------
settings_tweaks = {
    u'GlobalsTweak_Timescale',
    u'GlobalsTweak_ThievesGuild_QuestStealingPenalty',
    u'GlobalsTweak_ThievesGuild_QuestKillingPenalty',
    u'GlobalsTweak_ThievesGuild_QuestAttackingPenalty',
    u'GlobalsTweak_Crime_ForceJail',
    u'GmstTweak_Arrow_LitterCount',
    u'GmstTweak_Arrow_LitterTime',
    u'GmstTweak_Arrow_RecoveryFromActor',
    u'GmstTweak_Arrow_Speed',
    u'GmstTweak_Camera_ChaseTightness',
    u'GmstTweak_Camera_ChaseDistance',
    u'GmstTweak_Magic_ChameleonRefraction',
    u'GmstTweak_Compass_Disable',
    u'GmstTweak_Compass_RecognitionDistance',
    u'GmstTweak_Actor_UnconsciousnessDuration',
    u'GmstTweak_Movement_FatigueFromRunningEncumbrance',
    u'GmstTweak_Player_HorseTurningSpeed',
    u'GmstTweak_Camera_PCDeathTime',
    u'GmstTweak_World_CellRespawnTime',
    u'GmstTweak_Combat_RechargeWeapons',
    u'GmstTweak_Magic_BoltSpeed',
    u'GmstTweak_Msg_EquipMiscItem',
    u'GmstTweak_Msg_AutoSaving',
    u'GmstTweak_Msg_HarvestFailure',
    u'GmstTweak_Msg_HarvestSuccess',
    u'GmstTweak_Msg_QuickSave',
    u'GmstTweak_Msg_HorseStabled',
    u'GmstTweak_Msg_NoFastTravel',
    u'GmstTweak_Msg_LoadingArea',
    u'GmstTweak_Msg_QuickLoad',
    u'GmstTweak_Msg_NotEnoughCharge',
    u'GmstTweak_CostMultiplier_Repair',
    u'GmstTweak_Actor_GreetingDistance',
    u'GmstTweak_CostMultiplier_Recharge',
    u'GmstTweak_MasterOfMercantileExtraGoldAmount',
    u'GmstTweak_Combat_MaxActors',
    u'GmstTweak_Crime_AlarmDistance',
    u'GmstTweak_Crime_PrisonDurationModifier',
    u'GmstTweak_CostMultiplier_Enchantment',
    u'GmstTweak_CostMultiplier_SpellMaking',
    u'GmstTweak_AI_MaxActiveActors',
    u'GmstTweak_Magic_MaxPlayerSummons',
    u'GmstTweak_Combat_MaxAllyHitsInCombat_Tes4',
    u'GmstTweak_Magic_MaxNPCSummons',
    u'GmstTweak_Bounty_Assault',
    u'GmstTweak_Bounty_HorseTheft',
    u'GmstTweak_Bounty_Theft',
    u'GmstTweak_Combat_Alchemy',
    u'GmstTweak_Combat_Repair',
    u'GmstTweak_Actor_MaxCompanions',
    u'GmstTweak_Actor_TrainingLimit',
    u'GmstTweak_Combat_MaximumArmorRating',
    u'GmstTweak_Warning_InteriorDistanceToHostiles',
    u'GmstTweak_Warning_ExteriorDistanceToHostiles',
    u'GmstTweak_UOPVampireAgingAndFaceFix',
    u'GmstTweak_AI_MaxDeadActors',
    u'GmstTweak_Player_InventoryQuantityPrompt_Tes4',
    u'GmstTweak_Bounty_Trespassing',
    u'GmstTweak_Bounty_Pickpocketing',
    u'GmstTweak_LevelDifference_CreatureMax',
    u'GmstTweak_LevelDifference_ItemMax',
    u'GmstTweak_Actor_StrengthEncumbranceMultiplier',
    u'GmstTweak_Visuals_NPCBlood',
    u'GmstTweak_AI_MaxSmileDistance',
    u'GmstTweak_Player_MaxDraggableWeight',
    u'GmstTweak_AI_ConversationChance',
    u'GmstTweak_AI_ConversationChance_Interior',
    u'GmstTweak_Crime_PickpocketingChance',
    u'GmstTweak_Actor_MaxJumpHeight_Tes4',
    u'GmstTweak_Bounty_Murder',
    u'GmstTweak_Bounty_Jailbreak',
    u'GmstTweak_Prompt_Activate_Tes4',
    u'GmstTweak_Prompt_Open_Tes4',
    u'GmstTweak_Prompt_Read_Tes4',
    u'GmstTweak_Prompt_Sit_Tes4',
    u'GmstTweak_Prompt_Take_Tes4',
    u'GmstTweak_Prompt_Talk_Tes4',
    u'GmstTweak_Msg_NoSoulGemLargeEnough',
    u'GmstTweak_Combat_SpeakOnAttackChance',
    u'GmstTweak_Combat_SpeakOnHitChance_Tes4',
    u'GmstTweak_Combat_SpeakOnHitThreshold_Tes4',
    u'GmstTweak_Combat_SpeakOnPowerAttackChance_Tes4',
    u'GmstTweak_Combat_RandomTauntChance',
    u'GmstTweak_LevelUp_SkillCount',
    u'GmstTweak_Combat_MaxFriendHitsInCombat_Tes4',
}

#------------------------------------------------------------------------------
# Import Relations
#------------------------------------------------------------------------------
relations_attrs = (u'faction', u'mod') ##: mod?

#------------------------------------------------------------------------------
# Import Enchantment Stats
#------------------------------------------------------------------------------
ench_stats_attrs = (u'itemType', u'chargeAmount', u'enchantCost', u'flags')

#------------------------------------------------------------------------------
# Import Effect Stats
#------------------------------------------------------------------------------
mgef_stats_attrs = (u'flags', u'base_cost', u'associated_item', u'school',
                    u'resist_value', u'projectileSpeed', u'cef_enchantment',
                    u'cef_barter')

#------------------------------------------------------------------------------
# Tweak Assorted
#------------------------------------------------------------------------------
assorted_tweaks = {
    u'AssortedTweak_ArmorShows_Amulets',
    u'AssortedTweak_ArmorShows_Rings',
    u'AssortedTweak_ClothingShows_Amulets',
    u'AssortedTweak_ClothingShows_Rings',
    u'AssortedTweak_ArmorPlayable',
    u'AssortedTweak_ClothingPlayable',
    u'AssortedTweak_BowReach',
    u'AssortedTweak_ConsistentRings',
    u'AssortedTweak_DarnBooks',
    u'AssortedTweak_FogFix',
    u'AssortedTweak_NoLightFlicker',
    u'AssortedTweak_PotionWeight',
    u'AssortedTweak_PotionWeightMinimum',
    u'AssortedTweak_StaffWeight',
    u'AssortedTweak_SetCastWhenUsedEnchantmentCosts',
    u'AssortedTweak_WindSpeed',
    u'AssortedTweak_UniformGroundcover',
    u'AssortedTweak_HarvestChance',
    u'AssortedTweak_IngredientWeight',
    u'AssortedTweak_ArrowWeight',
    u'AssortedTweak_ScriptEffectSilencer',
    u'AssortedTweak_DefaultIcons',
    u'AssortedTweak_SetSoundAttenuationLevels',
    u'AssortedTweak_SetSoundAttenuationLevels_NirnrootOnly',
    u'AssortedTweak_FactioncrimeGoldMultiplier',
    u'AssortedTweak_LightFadeValueFix',
    u'AssortedTweak_SkyrimStyleWeapons',
    u'AssortedTweak_TextlessLSCRs',
    u'AssortedTweak_SEFFIcon',
    u'AssortedTweak_BookWeight',
}
nonplayable_biped_flags = {u'backWeapon', u'quiver', u'weapon', u'torch',
                           u'rightRing', u'sideWeapon'}
not_playable_flag = (u'biped_flags', u'notPlayable')
staff_condition = (u'weaponType', 4)
static_attenuation_rec_type = b'SOUN'

#------------------------------------------------------------------------------
# Import Races
#------------------------------------------------------------------------------
import_races_attrs = {
    b'RACE': {
        u'R.Attributes-F': (u'femaleStrength', u'femaleIntelligence',
                            u'femaleWillpower', u'femaleAgility',
                            u'femaleSpeed', u'femaleEndurance',
                            u'femalePersonality', u'femaleLuck'),
        u'R.Attributes-M': (u'maleStrength', u'maleIntelligence',
                            u'maleWillpower', u'maleAgility', u'maleSpeed',
                            u'maleEndurance', u'malePersonality',
                            u'maleLuck'),
        u'R.Body-F': (u'femaleTailModel', u'femaleUpperBodyPath',
                      u'femaleLowerBodyPath', u'femaleHandPath',
                      u'femaleFootPath', u'femaleTailPath'),
        u'R.Body-M': (u'maleTailModel', u'maleUpperBodyPath',
                      u'maleLowerBodyPath', u'maleHandPath', u'maleFootPath',
                      u'maleTailPath'),
        u'R.Body-Size-F': (u'femaleHeight', u'femaleWeight'),
        u'R.Body-Size-M': (u'maleHeight', u'maleWeight'),
        u'R.Description': (u'description',),
        u'R.Ears': (u'maleEars', u'femaleEars'),
        u'R.Eyes': (u'eyes', u'leftEye', u'rightEye'),
        u'R.Hair': (u'hairs',),
        u'R.Head': (u'head',),
        u'R.Mouth': (u'mouth', u'tongue'),
        u'R.Skills': (u'skills',),
        u'R.Teeth': (u'teethLower', u'teethUpper'),
        u'R.Voice-F': (u'femaleVoice',),
        u'R.Voice-M': (u'maleVoice',),
    },
}

#------------------------------------------------------------------------------
# Import Enchantments
#------------------------------------------------------------------------------
enchantment_types = {b'AMMO', b'ARMO', b'BOOK', b'CLOT', b'WEAP'}

#------------------------------------------------------------------------------
# Tweak Races
#------------------------------------------------------------------------------
race_tweaks = {
    u'RaceTweak_BiggerOrcsAndNords',
    u'RaceTweak_MergeSimilarRaceHairs',
    u'RaceTweak_MergeSimilarRaceEyes',
    u'RaceTweak_PlayableEyes',
    u'RaceTweak_PlayableHairs',
    u'RaceTweak_GenderlessHairs',
    u'RaceTweak_AllEyes',
    u'RaceTweak_AllHairs',
}
race_tweaks_need_collection = True

#------------------------------------------------------------------------------
# Timescale Checker
#------------------------------------------------------------------------------
# Nehrim has a timescale of 10, but the Nehrim devs forgot to change the wave
# periods for their grass to match, hence we keep default_wp_timescale at 30
# for Nehrim too
default_wp_timescale = 30
