#
# PySNMP MIB module ADTRAN-ATLAS-UNIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS-UNIT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
frCircuitDlci, frCircuitIfIndex = mibBuilder.importSymbols("RFC1315-MIB", "frCircuitDlci", "frCircuitIfIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, IpAddress, Integer32, Counter64, ModuleIdentity, ObjectIdentity, iso, Unsigned32, Counter32, MibIdentifier, NotificationType, NotificationType, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "IpAddress", "Integer32", "Counter64", "ModuleIdentity", "ObjectIdentity", "iso", "Unsigned32", "Counter32", "MibIdentifier", "NotificationType", "NotificationType", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154))
adGenATLASmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1))
adATLASUnitmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5))
adATLASUnitInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1))
adATLASUnitUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3))
adATLASUnitStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 4))
adATLASUpdateFw = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1))
adATLASConfigXfer = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2))
class AdTftpConfigXferStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("idle", 1), ("tftpFilenotFound", 2), ("tftpServerTimeout", 3), ("errorNotEnoughMmemory", 4), ("tftpDownloadInProgress", 5), ("tftpUploadInProgress", 6), ("tftpDownloadFailed", 7), ("tftpUploadFailed", 8), ("tftpDownloadComplete", 9), ("tftpUploadComplete", 10), ("tftpBadConfigFile", 11), ("tftpBadFilesize", 12), ("tftpNVRAMcfgCopyFailed", 13), ("downloadCopyingInternalConfig", 14), ("tftpFiletypeNotBinary", 15), ("tftpFileRevisionTooOld", 16), ("tftpRemoteDiskFull", 17), ("tftpFileAlreadyExists", 18), ("tftpFileAccessViolation", 19), ("tftpBadFileChecksum", 20), ("tftpReadNVRAMparseFailed", 21), ("downoadWaitingOnNVRAMsave", 22), ("uploadWritingInternalConfig", 23))

adATLASUnitIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUnitIfNumber.setStatus('mandatory')
adATLASUnitPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2), )
if mibBuilder.loadTexts: adATLASUnitPortInfoTable.setStatus('mandatory')
adATLASUnitPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2, 1), ).setIndexNames((0, "ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"), (0, "ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"))
if mibBuilder.loadTexts: adATLASUnitPortInfoEntry.setStatus('mandatory')
adATLASUnitPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("inTest", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUnitPortStatus.setStatus('mandatory')
adATLASUnitPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUnitPortIfIndex.setStatus('mandatory')
adATLASUnitPortDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUnitPortDescription.setStatus('mandatory')
adATLASUnitPortSlotMapTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 3), )
if mibBuilder.loadTexts: adATLASUnitPortSlotMapTable.setStatus('mandatory')
adATLASUnitPortSlotMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adATLASUnitPortSlotMapEntry.setStatus('mandatory')
adATLASUnitSlotAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUnitSlotAddress.setStatus('mandatory')
adATLASUnitPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUnitPortAddress.setStatus('mandatory')
adATLASUpdateFwModuleNum = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASUpdateFwModuleNum.setStatus('mandatory')
adATLASUpdateFwTFTPSrvAddr = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASUpdateFwTFTPSrvAddr.setStatus('mandatory')
adATLASUpdateFwTFTPSrvFileName = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASUpdateFwTFTPSrvFileName.setStatus('mandatory')
adATLASUpdateFwCurrStatus = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUpdateFwCurrStatus.setStatus('mandatory')
adATLASUpdateFwPrevStatus = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUpdateFwPrevStatus.setStatus('mandatory')
adATLASUpdateFwControl = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASUpdateFwControl.setStatus('mandatory')
adATLASConfigXferTFTPSrvAddr = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASConfigXferTFTPSrvAddr.setStatus('mandatory')
adATLASConfigXferTFTPSrvFileName = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASConfigXferTFTPSrvFileName.setStatus('mandatory')
adATLASConfigXferCurrStatus = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 3), AdTftpConfigXferStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASConfigXferCurrStatus.setStatus('mandatory')
adATLASConfigXferPrevStatus = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 4), AdTftpConfigXferStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASConfigXferPrevStatus.setStatus('mandatory')
adATLASConfigXferDwnldControl = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("loadAndUseCfg", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASConfigXferDwnldControl.setStatus('mandatory')
adATLASConfigXferUpldControl = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 3, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("saveCfg", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adATLASConfigXferUpldControl.setStatus('mandatory')
adATLASUnitFPStatus = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 5, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLASUnitFPStatus.setStatus('mandatory')
adATLASFrSwToBkup = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400500)).setObjects(("RFC1315-MIB", "frCircuitIfIndex"), ("RFC1315-MIB", "frCircuitDlci"))
adATLASFrSwToPrimary = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 154) + (0,15400501)).setObjects(("RFC1315-MIB", "frCircuitIfIndex"), ("RFC1315-MIB", "frCircuitDlci"))
mibBuilder.exportSymbols("ADTRAN-ATLAS-UNIT-MIB", adATLASUnitPortSlotMapTable=adATLASUnitPortSlotMapTable, adATLASUpdateFwPrevStatus=adATLASUpdateFwPrevStatus, adATLASmg=adATLASmg, adATLASConfigXferUpldControl=adATLASConfigXferUpldControl, adATLASUpdateFwTFTPSrvAddr=adATLASUpdateFwTFTPSrvAddr, adATLASUnitStatus=adATLASUnitStatus, adATLASUnitPortDescription=adATLASUnitPortDescription, adATLASConfigXfer=adATLASConfigXfer, adATLASUpdateFwModuleNum=adATLASUpdateFwModuleNum, adATLASUnitIfNumber=adATLASUnitIfNumber, adGenATLASmg=adGenATLASmg, adATLASConfigXferTFTPSrvFileName=adATLASConfigXferTFTPSrvFileName, adATLASUnitInfo=adATLASUnitInfo, adATLASUnitmg=adATLASUnitmg, adATLASFrSwToBkup=adATLASFrSwToBkup, adATLASUnitSlotAddress=adATLASUnitSlotAddress, adATLASUpdateFwTFTPSrvFileName=adATLASUpdateFwTFTPSrvFileName, adATLASUnitPortIfIndex=adATLASUnitPortIfIndex, adATLASConfigXferCurrStatus=adATLASConfigXferCurrStatus, adATLASUpdateFwControl=adATLASUpdateFwControl, adATLASUnitFPStatus=adATLASUnitFPStatus, adATLASFrSwToPrimary=adATLASFrSwToPrimary, adATLASUnitPortSlotMapEntry=adATLASUnitPortSlotMapEntry, adATLASUnitUtil=adATLASUnitUtil, adATLASUnitPortAddress=adATLASUnitPortAddress, adATLASUpdateFwCurrStatus=adATLASUpdateFwCurrStatus, AdTftpConfigXferStatus=AdTftpConfigXferStatus, adtran=adtran, adATLASConfigXferTFTPSrvAddr=adATLASConfigXferTFTPSrvAddr, adMgmt=adMgmt, adATLASConfigXferDwnldControl=adATLASConfigXferDwnldControl, adATLASUnitPortInfoTable=adATLASUnitPortInfoTable, adATLASUnitPortStatus=adATLASUnitPortStatus, adATLASUnitPortInfoEntry=adATLASUnitPortInfoEntry, adATLASConfigXferPrevStatus=adATLASConfigXferPrevStatus, adATLASUpdateFw=adATLASUpdateFw)
