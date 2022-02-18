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
"""Functions for initializing Bash data structures on boot. For now exports
functions to initialize bass.dirs that need be initialized high up into the
boot sequence to be able to backup/restore settings."""
import io
from configparser import ConfigParser, MissingSectionHeaderError

# Local - make sure that all imports here are carefully done in bash.py first
from .bass import dirs, get_ini_option
from .bolt import GPath, Path, decoder, deprint, os_name, top_level_dirs
from .env import get_personal_path, get_local_app_data_path, \
    get_win_store_game_info, shellMakeDirs
from .exception import BoltError, NonExistentDriveError

mopy_dirs_initialized = bash_dirs_initialized = False

def get_path_from_ini(bash_ini_, option_key, section_key=u'General'):
    get_value = get_ini_option(bash_ini_, option_key, section_key)
    get_value = (get_value and get_value.strip()) or u'.'
    return GPath(get_value) if get_value != u'.' else None

def getPersonalPath(bash_ini_, my_docs_path):
    #--Determine User folders from Personal and Local Application Data directories
    #  Attempt to pull from, in order: Command Line, Ini, win32com, Registry
    if my_docs_path:
        my_docs_path = GPath(my_docs_path)
        sErrorInfo = _(u'Folder path specified on command line (-p)')
    else:
        my_docs_path = get_path_from_ini(bash_ini_, u'sPersonalPath')
        if my_docs_path:
            sErrorInfo = _(
                u'Folder path specified in bash.ini (%s)') % u'sPersonalPath'
        else:
            my_docs_path, sErrorInfo = get_personal_path()
    #  If path is relative, make absolute
    if not my_docs_path.is_absolute():
        my_docs_path = dirs[u'app'].join(my_docs_path)
    #  Error check
    if not my_docs_path.exists():
        raise BoltError(f'Personal folder does not exist.\nPersonal folder: '
                        f'{my_docs_path}\nAdditional info:\n{sErrorInfo}')
    return my_docs_path

def getLocalAppDataPath(bash_ini_, app_data_local_path):
    #--Determine User folders from Personal and Local Application Data directories
    #  Attempt to pull from, in order: Command Line, Ini, win32com, Registry
    if app_data_local_path:
        app_data_local_path = GPath(app_data_local_path)
        sErrorInfo = _(u'Folder path specified on command line (-l)')
    else:
        app_data_local_path = get_path_from_ini(bash_ini_,
                                                u'sLocalAppDataPath')
        if app_data_local_path:
            sErrorInfo = _(u'Folder path specified in bash.ini (%s)') % u'sLocalAppDataPath'
        else:
            app_data_local_path, sErrorInfo = get_local_app_data_path()
    #  If path is relative, make absolute
    if not app_data_local_path.is_absolute():
        app_data_local_path = dirs[u'app'].join(app_data_local_path)
    #  Error check
    if not app_data_local_path.exists():
        raise BoltError(f'Local AppData folder does not exist.\nLocal AppData '
            f'folder: {app_data_local_path}\nAdditional info:\n{sErrorInfo}')
    return app_data_local_path

def getOblivionModsPath(bash_ini_, game_info):
    ob_mods_path = get_path_from_ini(bash_ini_, u'sOblivionMods')
    ws_info = get_win_store_game_info(game_info)
    if ob_mods_path:
        src = [u'[General]', u'sOblivionMods']
    elif not ws_info.installed:
        # Currently the standard location, next to the game install
        ob_mods_path = GPath(GPath(u'..').join(
            f'{game_info.bash_root_prefix} Mods'))
        src = u'Relative Path'
    else:
        # New location for Windows Store games,
        # Documents\Wrye Bash\{game} Mods
        ob_mods_path = dirs[u'personal'].join(
            u'Wrye Bash', f'{game_info.bash_root_prefix} Mods')
        src = u'My Documents'
    if not ob_mods_path.is_absolute(): ob_mods_path = dirs[u'app'].join(ob_mods_path)
    return ob_mods_path, src

def getBainDataPath(bash_ini_):
    idata_path = get_path_from_ini(bash_ini_, u'sInstallersData')
    if idata_path:
        src = [u'[General]', u'sInstallersData']
        if not idata_path.is_absolute(): idata_path = dirs[u'app'].join(idata_path)
    else:
        idata_path = dirs[u'installers'].join(u'Bash')
        src = u'Relative Path'
    return idata_path, src

def getBashModDataPath(bash_ini_):
    mod_data_path = get_path_from_ini(bash_ini_, u'sBashModData')
    if mod_data_path:
        if not mod_data_path.is_absolute():
            mod_data_path = dirs[u'app'].join(mod_data_path)
        src = [u'[General]', u'sBashModData']
    else:
        mod_data_path = dirs[u'bash_root'].join(u'Bash Mod Data')
        src = u'Relative Path'
    return mod_data_path, src

def getLegacyPath(newPath, oldPath):
    return (oldPath,newPath)[newPath.is_dir() or not oldPath.is_dir()]

def getLegacyPathWithSource(newPath, oldPath, newSrc, oldSrc=None):
    if newPath.is_dir() or not oldPath.is_dir():
        return newPath, newSrc
    else:
        return oldPath, oldSrc

def init_dirs(bashIni_, personal, localAppData, game_info):
    """Initialize bass.dirs dictionary. We need the bash.ini and the game
    being set, so this is called upon setting the game. Global structures
    that need info on Bash / Game dirs should be initialized here and set
    as globals in module scope. It may be called two times if restoring
    settings fails."""
    if not mopy_dirs_initialized:
        raise BoltError(u'init_dirs: Mopy dirs uninitialized')
    # Any warnings found during this stage can be added here as strings
    init_warnings = []
    #--Oblivion (Application) Directories
    dirs[u'app'] = game_info.gamePath
    dirs[u'defaultPatches'] = (
        dirs[u'mopy'].join(u'Bash Patches', game_info.bash_patches_dir)
        if game_info.bash_patches_dir else u'')
    dirs[u'taglists'] = dirs[u'mopy'].join(u'taglists', game_info.taglist_dir)
    #  Personal
    dirs[u'personal'] = personal = getPersonalPath(bashIni_, personal)
    if game_info.uses_personal_folders:
        dirs[u'saveBase'] = personal.join(u'My Games', game_info.my_games_name)
    else:
        dirs[u'saveBase'] = dirs[u'app']
    deprint(f'My Games location set to {dirs[u"saveBase"]}')
    #  Local Application Data
    dirs[u'local_appdata'] = localAppData = getLocalAppDataPath(bashIni_,
                                                                localAppData)
    # AppData for the game, depends on if it's a WS game or not.
    ws_info = get_win_store_game_info(game_info)
    if ws_info.installed:
        version_info = ws_info.get_installed_version()
        dirs[u'userApp'] = localAppData.join(
            u'Packages', version_info.full_name, u'LocalCache', u'Local',
            game_info.appdata_name)
    else:
        dirs[u'userApp'] = localAppData.join(game_info.appdata_name)
    deprint(f'LocalAppData location set to {dirs[u"userApp"]}')
    # Use local copy of the oblivion.ini if present
    # see: http://en.uesp.net/wiki/Oblivion:Ini_Settings
    # Oblivion reads the Oblivion.ini in the directory where it exists
    # first, and only if bUseMyGamesDirectory is non-existent or set to 1 does
    # it then look for My Documents\My Games\Oblivion.ini. In other words,
    # both can exist simultaneously, and only the value of bUseMyGamesDirectory
    # in the Oblivion.ini directory where Oblivion.exe is run from will
    # actually matter.
    # Utumno: not sure how/if this applies to other games
    first_ini_name = game_info.Ini.dropdown_inis[0]
    data_oblivion_ini = dirs[u'app'].join(first_ini_name)
    game_ini_path = dirs[u'saveBase'].join(first_ini_name)
    dirs[u'mods'] = dirs[u'app'].join(game_info.mods_dir)
    if data_oblivion_ini.is_file():
        oblivionIni = ConfigParser(allow_no_value=True) ##: use GameIni here
        try:
            try:
                # Try UTF-8 first, will also work for ASCII-encoded files
                oblivionIni.read(data_oblivion_ini, encoding='utf8')
            except UnicodeDecodeError:
                # No good, this is a nonstandard encoding
                with data_oblivion_ini.open(u'rb') as ins:
                    ini_contents = ins.read()
                oblivionIni.read_file(io.StringIO(decoder(ini_contents)))
        except MissingSectionHeaderError:
            # Probably not actually a game INI - might be reshade
            init_warnings.append(
                _(u'The global INI file in your game directory (%s) does not '
                  u'appear to be a valid game INI. It might come from an '
                  u'incorrectly installed third party tool. Consider '
                  u'deleting it and validating your game files.') %
                data_oblivion_ini)
        # is bUseMyGamesDirectory set to 0?
        if get_ini_option(oblivionIni, u'bUseMyGamesDirectory') == u'0':
            game_ini_path = data_oblivion_ini
            # Set the save game folder to the Oblivion directory
            dirs[u'saveBase'] = dirs[u'app']
            # Set the data folder to sLocalMasterPath
            dirs[u'mods'] = dirs[u'app'].join(get_ini_option(oblivionIni,
                u'SLocalMasterPath') or game_info.mods_dir)
    # these are relative to the mods path so they must be set here
    dirs[u'patches'] = dirs[u'mods'].join(u'Bash Patches')
    dirs[u'tag_files'] = dirs[u'mods'].join(u'BashTags')
    dirs[u'ini_tweaks'] = dirs[u'mods'].join(u'INI Tweaks')
    #--Mod Data, Installers
    oblivionMods, oblivionModsSrc = getOblivionModsPath(bashIni_, game_info)
    dirs[u'bash_root'] = oblivionMods
    deprint(f'Game Mods location set to {oblivionMods}')
    dirs[u'modsBash'], modsBashSrc = getBashModDataPath(bashIni_)
    dirs[u'modsBash'], modsBashSrc = getLegacyPathWithSource(
        dirs[u'modsBash'], dirs[u'app'].join(game_info.mods_dir, u'Bash'),
        modsBashSrc, u'Relative Path')
    deprint(f'Bash Mod Data location set to {dirs[u"modsBash"]}')
    dirs[u'installers'] = oblivionMods.join(u'Bash Installers')
    dirs[u'installers'] = getLegacyPath(dirs[u'installers'],
                                        dirs[u'app'].join(u'Installers'))
    deprint(f'Installers location set to {dirs[u"installers"]}')
    dirs[u'bainData'], bainDataSrc = getBainDataPath(bashIni_)
    deprint(f'Installers bash data location set to {dirs[u"bainData"]}')
    dirs[u'bsaCache'] = dirs[u'bainData'].join(u'BSA Cache')
    dirs[u'converters'] = dirs[u'installers'].join(u'Bain Converters')
    dirs[u'dupeBCFs'] = dirs[u'converters'].join(u'--Duplicates')
    dirs[u'corruptBCFs'] = dirs[u'converters'].join(u'--Corrupt')
    # create bash user folders, keep these in order
    dir_keys = (u'modsBash', u'installers', u'converters', u'dupeBCFs',
                u'corruptBCFs', u'bainData', u'bsaCache')
    deprint(u'Checking if WB directories exist and creating them if needed:')
    try:
        for dir_key in dir_keys:
            wanted_dir = dirs[dir_key]
            deprint(f' - {wanted_dir}')
            shellMakeDirs([wanted_dir])
    except NonExistentDriveError as e:
        # NonExistentDriveError is thrown by shellMakeDirs if any of the
        # directories cannot be created due to residing on a non-existing
        # drive (in posix if permission is denied). Find which keys are
        # causing the errors
        msg = _dirs_err_msg(e, dir_keys, bainDataSrc, modsBashSrc,
                            oblivionMods, oblivionModsSrc)
        raise BoltError(msg)
    global bash_dirs_initialized
    bash_dirs_initialized = True
    return game_ini_path, init_warnings

def _dirs_err_msg(e, dir_keys, bainDataSrc, modsBashSrc, oblivionMods,
                  oblivionModsSrc):
    badKeys = set()  # List of dirs[key] items that are invalid
    # First, determine which dirs[key] items are causing it
    for dir_key in dir_keys:
        if dirs[dir_key] in e.failed_paths:
            badKeys.add(dir_key)
    # Now, work back from those to determine which setting created those
    if os_name == 'posix':
        m = _("Please check the settings for the following paths in your "
              "bash.ini, the drive does not exist or you don't have write "
              "permissions")
    else:
        m = _(u'Please check the settings for the following paths in your '
              u'bash.ini, the drive does not exist')
    msg = _(u'Error creating required Wrye Bash directories.') + f'  {m}:\n\n'
    relativePathError = []
    if u'modsBash' in badKeys:
        if isinstance(modsBashSrc, list):
            msg += (' '.join(modsBashSrc) + f'\n    {dirs[u"modsBash"]}\n')
        else:
            relativePathError.append(dirs[u'modsBash'])
    if {u'installers', u'converters', u'dupeBCFs', u'corruptBCFs'} & badKeys:
        # All derived from oblivionMods -> getOblivionModsPath
        if isinstance(oblivionModsSrc, list):
            msg += (u' '.join(oblivionModsSrc) + f'\n    {oblivionMods}\n')
        else:
            relativePathError.append(oblivionMods)
    if {u'bainData', u'bsaCache'} & badKeys:
        # Both derived from 'bainData' -> getBainDataPath
        # Sometimes however, getBainDataPath falls back to oblivionMods,
        # So check to be sure we haven't already added a message about that
        if bainDataSrc != oblivionModsSrc:
            if isinstance(bainDataSrc, list):
                msg += u' '.join(bainDataSrc) + f'\n    {dirs[u"bainData"]}\n'
            else:
                relativePathError.append(dirs[u'bainData'])
    if relativePathError:
        msg += u'\n' + _(u'A path error was the result of relative paths.')
        msg += u'  ' + _(u'The following paths are causing the errors, '
                         u'however usually a relative path should be fine.')
        msg += u'  ' + _(u'Check your setup to see if you are using '
                         u'symbolic links or NTFS Junctions') + u':\n\n'
        msg += u'\n'.join([f'{x}' for x in relativePathError])
    return msg

def init_dirs_mopy():
    dirs[u'mopy'] = Path.getcwd()
    dirs[u'bash'] = dirs[u'mopy'].join(u'bash')
    dirs[u'compiled'] = dirs[u'bash'].join(u'compiled')
    dirs[u'l10n'] = dirs[u'bash'].join(u'l10n')
    dirs[u'db'] = dirs[u'bash'].join(u'db')
    dirs[u'templates'] = dirs[u'mopy'].join(u'templates')
    dirs[u'images'] = dirs[u'bash'].join(u'images')
    from . import archives
    if os_name == u'nt': # don't add local directory to binaries on linux
        archives.exe7z = dirs[u'compiled'].join(archives.exe7z).s
    global mopy_dirs_initialized
    mopy_dirs_initialized = True

def getLocalSaveDirs():
    """Return a list of possible local save directories, NOT including the
    base directory."""
    baseSaves = dirs[u'saveBase'].join(u'Saves')
    # Path.list returns [] for non existent dirs
    localSaveDirs = [x for x in top_level_dirs(baseSaves) if
                     x not in (u'Bash', u'Mash')]
    # Filter out non-encodable names
    bad = set()
    for folder in localSaveDirs:
        try:
            folder.encode(u'cp1252')
        except UnicodeEncodeError:
            bad.add(folder)
    localSaveDirs = sorted(x for x in localSaveDirs if x not in bad)
    return localSaveDirs
