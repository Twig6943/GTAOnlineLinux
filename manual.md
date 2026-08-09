## enhanced

open `/etc/hosts` and add this to the file
```
0.0.0.0 test-s1.battleye.com
0.0.0.0 paradiseenhanced-s1.battleye.com
```
##

add the proton battleye runtime path to the launch options, it should look something like this
`PROTON_BATTLEYE_RUNTIME=/path/to/SteamLibrary/steamapps/common/Proton\ BattlEye\ Runtime/ %command%`

##

open the game files and go to x64/data  
create a new file called `startup.meta` and paste this into it
```xml
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
```

## legacy

open `/etc/hosts` and add this to the file
```
0.0.0.0 test-s1.battleye.com
0.0.0.0 paradise-s1.battleye.com

```
##

add the proton battleye runtime path to the launch options, it should look something like this
`PROTON_BATTLEYE_RUNTIME=/path/to/SteamLibrary/steamapps/common/Proton\ BattlEye\ Runtime/ %command%`

##

open the game files and go to x64/data  
create a new file called `startup.meta` and paste this into it
```xml
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
	  </Item>
	  <Item>
	   <filename>platform:/data/cdimages/scaleform_frontend.rpf</filename>
	   <fileType>RPF_FILE_PRE_INSTALL</fileType>
	  </Item>
	 </dataFiles>
	<contentChangeSets itemType="CDataFileMgr__ContentChangeSet" />
	<dataFiles itemType="CDataFileMgr__DataFile" />
	<patchFiles />
</CDataFileMgr__ContentsOfDataFileXml>                     
<!--GTAOnlineLinux-->
```
