#!/usr/bin/env python3

# GTAOnlineEnhancedLinux
# Copyright (C) 2026  WerIstLuka <weristluka@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import subprocess
import time

protonBattleyeRuntimeSteamID = 1161040
gtaEnhancedSteamID = 3240220
steamTimeout = 5

metaContent = '''\
<?xml version="1.0" encoding="UTF-8"?>
<!--GTAOnlineLinux-->
<CDataFileMgr__ContentsOfDataFileXml>
 <disabledFiles />
 <includedXmlFiles itemType="CDataFileMgr__DataFileArray" />
 <includedDataFiles />
 <dataFiles itemType="CDataFileMgr__DataFile">
  <Item>
   <filename>platform:/data/cdimages/scaleform_platform_pc.rpf</filename>
   <fileType>RPF_FILE</fileType>
   <registerAs />
   <locked value="false" />
   <loadCompletely value="false" />
   <overlay value="false" />
   <patchFile value="false" />
   <disabled value="false" />
   <persistent value="false" />
   <enforceLsnSorting value="true" />
   <contents />
   <installPartition>PARTITION_NONE</installPartition>
  </Item>
  <Item>
   <filename>platform:/data/cdimages/scaleform_frontend.rpf</filename>
   <fileType>RPF_FILE_PRE_INSTALL</fileType>
   <registerAs />
   <locked value="false" />
   <loadCompletely value="false" />
   <overlay value="false" />
   <patchFile value="false" />
   <disabled value="false" />
   <persistent value="false" />
   <enforceLsnSorting value="true" />
   <contents />
   <installPartition>PARTITION_NONE</installPartition>
  </Item>
  <Item>
   <filename>platform:/data/cdimages/scaleform_frontend_gen9.rpf</filename>
   <fileType>RPF_FILE_PRE_INSTALL</fileType>
   <registerAs />
   <locked value="false" />
   <loadCompletely value="false" />
   <overlay value="false" />
   <patchFile value="false" />
   <disabled value="false" />
   <persistent value="false" />
   <enforceLsnSorting value="true" />
   <contents />
   <installPartition>PARTITION_NONE</installPartition>
  </Item>
  <Item>
   <filename>platform:/levels/gta5/script/script.rpf</filename>
   <fileType>RPF_FILE_PRE_INSTALL</fileType>
   <registerAs />
   <locked value="false" />
   <loadCompletely value="false" />
   <overlay value="false" />
   <patchFile value="false" />
   <disabled value="false" />
   <persistent value="false" />
   <enforceLsnSorting value="true" />
   <contents />
   <installPartition>PARTITION_NONE</installPartition>
  </Item>
 </dataFiles>
 <contentChangeSets itemType="CDataFileMgr__ContentChangeSet" />
 <patchFiles />
 <allowedFolders />
</CDataFileMgr__ContentsOfDataFileXml>
<!--GTAOnlineLinux-->
'''

def closeSteam() -> None:
	try:
		steamPID = subprocess.check_output(['pidof', 'steam'])
		os.kill(int(steamPID), 15)
	except subprocess.CalledProcessError:
		return
	while True:
		try:
			with open('/proc/{steamPID}/comm') as PIDcomm:
				if PIDcomm.read() == "steam":
					time.sleep(1)
		except FileNotFoundError:
			break

def getSteamGamePath(steamID:int, name:str) -> str:
	with open(os.path.expanduser('~/.steam/root/config/libraryfolders.vdf'), 'r') as steamFolders:
		lines = steamFolders.readlines()
		path = ''
		for line in lines:
			if line.lstrip().startswith('\"path'):
				path = line.split()[1][1:-1]
				continue
			if line.lstrip().startswith(f'\"{steamID}'):
				return path
		print(f'couldn\'t find {name}')
		exit(1)

def writeLaunchOptions() -> None:
	battleyePath = getSteamGamePath(protonBattleyeRuntimeSteamID, 'proton battleye runtime')
	launchOption = rf'PROTON_BATTLEYE_RUNTIME={battleyePath}/steamapps/common/Proton\\ BattlEye\\ Runtime/ %command%'
	userIDs = os.listdir(os.path.expanduser('~/.steam/root/userdata/'))
	for userID in userIDs:
		if not os.path.isfile(os.path.expanduser(f'~/.steam/root/userdata/{userID}/config/localconfig.vdf')):
			continue
		if userID == 'anonymous':
			continue
		with open(os.path.expanduser(f'~/.steam/root/userdata/{userID}/config/localconfig.vdf'), 'r') as steamConfig:
			lines = steamConfig.readlines()
			outputFile = ''
			inGTA = False
			gotGTA = False
			for index, line in enumerate(lines):
				if line.strip() == f'\"{gtaEnhancedSteamID}\"' and lines[index+1].strip() == '{':
					inGTA = True
					gotGTA = True
				if inGTA:
					if line.lstrip().startswith('\"LaunchOptions'):
						continue
					if line.strip() == '}':
						inGTA = False
						outputFile += f'\t\t\t\t\t\t\"LaunchOptions\"\t\t\"{launchOption}\"\n'
				outputFile += line
			steamConfig.close()
		with open(os.path.expanduser(f'~/.steam/root/userdata/{userID}/config/localconfig.vdf'), 'w') as steamConfig:
			steamConfig.writelines(outputFile)
			steamConfig.close()
		if not gotGTA:
			print('couldn\'t set launch options')
			exit(1)
		return

def writeHosts() -> None:
	with open('/etc/hosts', 'r') as hostsFile:
		lines = hostsFile.readlines()
		toAppend = ''
		if '0.0.0.0 test-s1.battleye.com\n' not in lines:
			toAppend += '0.0.0.0 test-s1.battleye.com\n'
		if '0.0.0.0 paradiseenhanced-s1.battleye.com\n' not in lines:
			toAppend += '0.0.0.0 paradiseenhanced-s1.battleye.com\n'
		hostsFile.close()
	if toAppend == '':
		return
	print('need root access to write to /etc/hosts')
	subprocess.call(['sudo', 'bash', '-c', f'echo -n \"{toAppend}\" >> /etc/hosts'])

def createStartupMeta() -> None:
	path = getSteamGamePath(gtaEnhancedSteamID, 'gta enhanced')
	path += '/steamapps/common/Grand Theft Auto V Enhanced/x64/data/startup.meta'
	with open(path, 'w') as metaFile:
		metaFile.write(metaContent)
		metaFile.close()

print("""\
GTAOnlineEnhancedLinux Copyright (C) 2026  WerIstLuka <weristluka@gmail.com>
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it under certain conditions;""")

closeSteam()
time.sleep(steamTimeout)
writeLaunchOptions()
createStartupMeta()
writeHosts()