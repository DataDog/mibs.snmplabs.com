#
# PySNMP MIB module H3C-EFM-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-EFM-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
h3cEpon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cEpon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, TimeTicks, Gauge32, Counter32, Unsigned32, ObjectIdentity, NotificationType, MibIdentifier, Integer32, mib_2, Counter64, IpAddress, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "Counter32", "Unsigned32", "ObjectIdentity", "NotificationType", "MibIdentifier", "Integer32", "mib-2", "Counter64", "IpAddress", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, DateAndTime, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "MacAddress")
h3cEfmOamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3))
h3cEfmOamMIB.setRevisions(('2004-10-24 00:00',))
if mibBuilder.loadTexts: h3cEfmOamMIB.setLastUpdated('200410240000Z')
if mibBuilder.loadTexts: h3cEfmOamMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
h3cDot3OamMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1))
h3cDot3OamConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2))
class Dot3Oui(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

h3cDot3OamTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 1), )
if mibBuilder.loadTexts: h3cDot3OamTable.setStatus('current')
h3cDot3OamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDot3OamEntry.setStatus('current')
h3cDot3OamAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamAdminState.setStatus('current')
h3cDot3OamOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("linkfault", 2), ("passiveWait", 3), ("activeSendLocal", 4), ("sendLocalAndRemote", 5), ("sendLocalAndRemoteOk", 6), ("oamPeeringLocallyRejected", 7), ("oamPeeringRemotelyRejected", 8), ("operational", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamOperStatus.setStatus('current')
h3cDot3OamMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("passive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamMode.setStatus('current')
h3cDot3OamMaxOamPduSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 1522))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamMaxOamPduSize.setStatus('current')
h3cDot3OamConfigRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamConfigRevision.setStatus('current')
h3cDot3OamFunctionsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 1, 1, 6), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamFunctionsSupported.setStatus('current')
h3cDot3OamPeerTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2), )
if mibBuilder.loadTexts: h3cDot3OamPeerTable.setStatus('current')
h3cDot3OamPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDot3OamPeerEntry.setStatus('current')
h3cDot3OamPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamPeerStatus.setStatus('current')
h3cDot3OamPeerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamPeerMacAddress.setStatus('current')
h3cDot3OamPeerVendorOui = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1, 3), Dot3Oui()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamPeerVendorOui.setStatus('current')
h3cDot3OamPeerVendorInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamPeerVendorInfo.setStatus('current')
h3cDot3OamPeerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("passive", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamPeerMode.setStatus('current')
h3cDot3OamPeerMaxOamPduSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 1522))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamPeerMaxOamPduSize.setStatus('current')
h3cDot3OamPeerConfigRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamPeerConfigRevision.setStatus('current')
h3cDot3OamPeerFunctionsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 2, 1, 8), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamPeerFunctionsSupported.setStatus('current')
h3cDot3OamLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 3), )
if mibBuilder.loadTexts: h3cDot3OamLoopbackTable.setStatus('current')
h3cDot3OamLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDot3OamLoopbackEntry.setStatus('current')
h3cDot3OamLoopbackCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noLoopback", 1), ("startRemoteLoopback", 2), ("stopRemoteLoopback", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamLoopbackCommand.setStatus('current')
h3cDot3OamLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noLoopback", 1), ("initiatingLoopback", 2), ("remoteLoopback", 3), ("terminatingLoopback", 4), ("localLoopback", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamLoopbackStatus.setStatus('current')
h3cDot3OamLoopbackIgnoreRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("process", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamLoopbackIgnoreRx.setStatus('current')
h3cDot3OamStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4), )
if mibBuilder.loadTexts: h3cDot3OamStatsTable.setStatus('current')
h3cDot3OamStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDot3OamStatsEntry.setStatus('current')
h3cDot3OamInformationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamInformationTx.setStatus('current')
h3cDot3OamInformationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamInformationRx.setStatus('current')
h3cDot3OamUniqueEventNotificationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamUniqueEventNotificationTx.setStatus('current')
h3cDot3OamUniqueEventNotificationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamUniqueEventNotificationRx.setStatus('current')
h3cDot3OamDuplicateEventNotificationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamDuplicateEventNotificationTx.setStatus('current')
h3cDot3OamDuplicateEventNotificationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamDuplicateEventNotificationRx.setStatus('current')
h3cDot3OamLoopbackControlTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamLoopbackControlTx.setStatus('current')
h3cDot3OamLoopbackControlRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamLoopbackControlRx.setStatus('current')
h3cDot3OamVariableRequestTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamVariableRequestTx.setStatus('current')
h3cDot3OamVariableRequestRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamVariableRequestRx.setStatus('current')
h3cDot3OamVariableResponseTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamVariableResponseTx.setStatus('current')
h3cDot3OamVariableResponseRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamVariableResponseRx.setStatus('current')
h3cDot3OamOrgSpecificTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamOrgSpecificTx.setStatus('current')
h3cDot3OamOrgSpecificRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamOrgSpecificRx.setStatus('current')
h3cDot3OamUnsupportedCodesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamUnsupportedCodesTx.setStatus('current')
h3cDot3OamUnsupportedCodesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamUnsupportedCodesRx.setStatus('current')
h3cDot3OamFramesLostDueToOam = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 4, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamFramesLostDueToOam.setStatus('current')
h3cDot3OamEventConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5), )
if mibBuilder.loadTexts: h3cDot3OamEventConfigTable.setStatus('current')
h3cDot3OamEventConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cDot3OamEventConfigEntry.setStatus('current')
h3cDot3OamErrSymPeriodWindowHi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrSymPeriodWindowHi.setStatus('current')
h3cDot3OamErrSymPeriodWindowLo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrSymPeriodWindowLo.setStatus('current')
h3cDot3OamErrSymPeriodThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrSymPeriodThresholdHi.setStatus('current')
h3cDot3OamErrSymPeriodThresholdLo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrSymPeriodThresholdLo.setStatus('current')
h3cDot3OamErrSymPeriodEvNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrSymPeriodEvNotifEnable.setStatus('current')
h3cDot3OamErrFramePeriodWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFramePeriodWindow.setStatus('current')
h3cDot3OamErrFramePeriodThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFramePeriodThreshold.setStatus('current')
h3cDot3OamErrFramePeriodEvNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFramePeriodEvNotifEnable.setStatus('current')
h3cDot3OamErrFrameWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFrameWindow.setStatus('current')
h3cDot3OamErrFrameThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFrameThreshold.setStatus('current')
h3cDot3OamErrFrameEvNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFrameEvNotifEnable.setStatus('current')
h3cDot3OamErrFrameSecsSummaryWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 9000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFrameSecsSummaryWindow.setStatus('current')
h3cDot3OamErrFrameSecsSummaryThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 900))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFrameSecsSummaryThreshold.setStatus('current')
h3cDot3OamErrFrameSecsEvNotifEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 5, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot3OamErrFrameSecsEvNotifEnable.setStatus('current')
h3cDot3OamEventLogTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6), )
if mibBuilder.loadTexts: h3cDot3OamEventLogTable.setStatus('current')
h3cDot3OamEventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogIndex"))
if mibBuilder.loadTexts: h3cDot3OamEventLogEntry.setStatus('current')
h3cDot3OamEventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cDot3OamEventLogIndex.setStatus('current')
h3cDot3OamEventLogTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogTimestamp.setStatus('current')
h3cDot3OamEventLogOui = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 3), Dot3Oui()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogOui.setStatus('current')
h3cDot3OamEventLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogType.setStatus('current')
h3cDot3OamEventLogLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogLocation.setStatus('current')
h3cDot3OamEventLogWindowHi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogWindowHi.setStatus('current')
h3cDot3OamEventLogWindowLo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogWindowLo.setStatus('current')
h3cDot3OamEventLogThresholdHi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogThresholdHi.setStatus('current')
h3cDot3OamEventLogThresholdLo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogThresholdLo.setStatus('current')
h3cDot3OamEventLogValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 10), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogValue.setStatus('current')
h3cDot3OamEventLogRunningTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 11), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogRunningTotal.setStatus('current')
h3cDot3OamEventLogEventTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 6, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot3OamEventLogEventTotal.setStatus('current')
h3cDot3OamTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 7))
h3cDot3OamTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 7, 0))
h3cDot3OamThresholdEvent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 7, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogTimestamp"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogOui"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogType"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogLocation"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogWindowHi"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogWindowLo"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogThresholdHi"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogThresholdLo"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogValue"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogRunningTotal"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogEventTotal"))
if mibBuilder.loadTexts: h3cDot3OamThresholdEvent.setStatus('current')
h3cDot3OamNonThresholdEvent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 1, 7, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogTimestamp"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogOui"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogType"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogLocation"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogEventTotal"))
if mibBuilder.loadTexts: h3cDot3OamNonThresholdEvent.setStatus('current')
h3cDot3OamGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1))
h3cDot3OamCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 2))
h3cDot3OamCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 2, 1)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamControlGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamStatsBaseGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamLoopbackGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrSymbolPeriodEventGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFramePeriodEventGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFrameEventGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFrameSecsSummaryEventGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogGroup"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamCompliance = h3cDot3OamCompliance.setStatus('current')
h3cDot3OamControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 1)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamAdminState"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamOperStatus"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamMode"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamMaxOamPduSize"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamConfigRevision"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamFunctionsSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamControlGroup = h3cDot3OamControlGroup.setStatus('current')
h3cDot3OamPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 2)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerStatus"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerMacAddress"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerVendorOui"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerVendorInfo"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerMode"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerFunctionsSupported"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerMaxOamPduSize"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamPeerConfigRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamPeerGroup = h3cDot3OamPeerGroup.setStatus('current')
h3cDot3OamStatsBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 3)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamInformationTx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamInformationRx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamUniqueEventNotificationTx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamUniqueEventNotificationRx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamDuplicateEventNotificationTx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamDuplicateEventNotificationRx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamLoopbackControlTx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamLoopbackControlRx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamVariableRequestTx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamVariableRequestRx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamVariableResponseTx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamVariableResponseRx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamOrgSpecificTx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamOrgSpecificRx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamUnsupportedCodesTx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamUnsupportedCodesRx"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamFramesLostDueToOam"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamStatsBaseGroup = h3cDot3OamStatsBaseGroup.setStatus('current')
h3cDot3OamLoopbackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 4)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamLoopbackCommand"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamLoopbackStatus"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamLoopbackIgnoreRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamLoopbackGroup = h3cDot3OamLoopbackGroup.setStatus('current')
h3cDot3OamErrSymbolPeriodEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 5)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodWindowHi"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodWindowLo"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodThresholdHi"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodThresholdLo"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrSymPeriodEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamErrSymbolPeriodEventGroup = h3cDot3OamErrSymbolPeriodEventGroup.setStatus('current')
h3cDot3OamErrFramePeriodEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 6)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFramePeriodWindow"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFramePeriodThreshold"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFramePeriodEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamErrFramePeriodEventGroup = h3cDot3OamErrFramePeriodEventGroup.setStatus('current')
h3cDot3OamErrFrameEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 7)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFrameWindow"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFrameThreshold"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFrameEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamErrFrameEventGroup = h3cDot3OamErrFrameEventGroup.setStatus('current')
h3cDot3OamErrFrameSecsSummaryEventGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 8)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFrameSecsSummaryWindow"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFrameSecsSummaryThreshold"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamErrFrameSecsEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamErrFrameSecsSummaryEventGroup = h3cDot3OamErrFrameSecsSummaryEventGroup.setStatus('current')
h3cDot3OamEventLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 9)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogTimestamp"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogOui"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogType"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogLocation"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogWindowHi"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogWindowLo"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogThresholdHi"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogThresholdLo"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogValue"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogRunningTotal"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamEventLogEventTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamEventLogGroup = h3cDot3OamEventLogGroup.setStatus('current')
h3cDot3OamNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 3, 2, 1, 10)).setObjects(("H3C-EFM-COMMON-MIB", "h3cDot3OamThresholdEvent"), ("H3C-EFM-COMMON-MIB", "h3cDot3OamNonThresholdEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cDot3OamNotificationGroup = h3cDot3OamNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("H3C-EFM-COMMON-MIB", h3cDot3OamFunctionsSupported=h3cDot3OamFunctionsSupported, h3cDot3OamPeerFunctionsSupported=h3cDot3OamPeerFunctionsSupported, h3cDot3OamUniqueEventNotificationRx=h3cDot3OamUniqueEventNotificationRx, h3cDot3OamTrapsPrefix=h3cDot3OamTrapsPrefix, h3cDot3OamEventLogRunningTotal=h3cDot3OamEventLogRunningTotal, h3cDot3OamPeerVendorOui=h3cDot3OamPeerVendorOui, h3cDot3OamErrFramePeriodEvNotifEnable=h3cDot3OamErrFramePeriodEvNotifEnable, h3cDot3OamNotificationGroup=h3cDot3OamNotificationGroup, h3cDot3OamErrFrameWindow=h3cDot3OamErrFrameWindow, h3cEfmOamMIB=h3cEfmOamMIB, h3cDot3OamEventLogWindowHi=h3cDot3OamEventLogWindowHi, h3cDot3OamVariableRequestTx=h3cDot3OamVariableRequestTx, h3cDot3OamLoopbackStatus=h3cDot3OamLoopbackStatus, h3cDot3OamPeerTable=h3cDot3OamPeerTable, h3cDot3OamStatsTable=h3cDot3OamStatsTable, h3cDot3OamUniqueEventNotificationTx=h3cDot3OamUniqueEventNotificationTx, h3cDot3OamUnsupportedCodesRx=h3cDot3OamUnsupportedCodesRx, h3cDot3OamPeerConfigRevision=h3cDot3OamPeerConfigRevision, h3cDot3OamErrSymPeriodThresholdLo=h3cDot3OamErrSymPeriodThresholdLo, h3cDot3OamEventConfigEntry=h3cDot3OamEventConfigEntry, h3cDot3OamEventLogType=h3cDot3OamEventLogType, h3cDot3OamErrFrameEventGroup=h3cDot3OamErrFrameEventGroup, h3cDot3OamEventLogValue=h3cDot3OamEventLogValue, h3cDot3OamErrFramePeriodWindow=h3cDot3OamErrFramePeriodWindow, h3cDot3OamNonThresholdEvent=h3cDot3OamNonThresholdEvent, h3cDot3OamErrFrameSecsEvNotifEnable=h3cDot3OamErrFrameSecsEvNotifEnable, h3cDot3OamInformationRx=h3cDot3OamInformationRx, h3cDot3OamEventLogOui=h3cDot3OamEventLogOui, h3cDot3OamOperStatus=h3cDot3OamOperStatus, h3cDot3OamTraps=h3cDot3OamTraps, h3cDot3OamEventLogThresholdHi=h3cDot3OamEventLogThresholdHi, h3cDot3OamEventLogWindowLo=h3cDot3OamEventLogWindowLo, h3cDot3OamErrFrameSecsSummaryEventGroup=h3cDot3OamErrFrameSecsSummaryEventGroup, h3cDot3OamCompliances=h3cDot3OamCompliances, h3cDot3OamMode=h3cDot3OamMode, PYSNMP_MODULE_ID=h3cEfmOamMIB, h3cDot3OamConformance=h3cDot3OamConformance, h3cDot3OamPeerMode=h3cDot3OamPeerMode, h3cDot3OamPeerEntry=h3cDot3OamPeerEntry, h3cDot3OamEventLogEventTotal=h3cDot3OamEventLogEventTotal, h3cDot3OamEventLogIndex=h3cDot3OamEventLogIndex, h3cDot3OamPeerMaxOamPduSize=h3cDot3OamPeerMaxOamPduSize, h3cDot3OamEventLogLocation=h3cDot3OamEventLogLocation, h3cDot3OamStatsBaseGroup=h3cDot3OamStatsBaseGroup, h3cDot3OamErrFrameEvNotifEnable=h3cDot3OamErrFrameEvNotifEnable, h3cDot3OamStatsEntry=h3cDot3OamStatsEntry, h3cDot3OamOrgSpecificTx=h3cDot3OamOrgSpecificTx, h3cDot3OamDuplicateEventNotificationRx=h3cDot3OamDuplicateEventNotificationRx, h3cDot3OamFramesLostDueToOam=h3cDot3OamFramesLostDueToOam, h3cDot3OamEventLogTimestamp=h3cDot3OamEventLogTimestamp, h3cDot3OamThresholdEvent=h3cDot3OamThresholdEvent, h3cDot3OamVariableRequestRx=h3cDot3OamVariableRequestRx, h3cDot3OamAdminState=h3cDot3OamAdminState, h3cDot3OamPeerVendorInfo=h3cDot3OamPeerVendorInfo, h3cDot3OamErrSymPeriodThresholdHi=h3cDot3OamErrSymPeriodThresholdHi, h3cDot3OamErrSymPeriodWindowHi=h3cDot3OamErrSymPeriodWindowHi, h3cDot3OamTable=h3cDot3OamTable, h3cDot3OamVariableResponseRx=h3cDot3OamVariableResponseRx, h3cDot3OamErrFrameThreshold=h3cDot3OamErrFrameThreshold, h3cDot3OamLoopbackGroup=h3cDot3OamLoopbackGroup, h3cDot3OamLoopbackEntry=h3cDot3OamLoopbackEntry, h3cDot3OamLoopbackControlTx=h3cDot3OamLoopbackControlTx, h3cDot3OamEventLogTable=h3cDot3OamEventLogTable, h3cDot3OamErrSymPeriodWindowLo=h3cDot3OamErrSymPeriodWindowLo, h3cDot3OamEventConfigTable=h3cDot3OamEventConfigTable, h3cDot3OamMIB=h3cDot3OamMIB, h3cDot3OamLoopbackIgnoreRx=h3cDot3OamLoopbackIgnoreRx, h3cDot3OamEventLogThresholdLo=h3cDot3OamEventLogThresholdLo, h3cDot3OamInformationTx=h3cDot3OamInformationTx, h3cDot3OamConfigRevision=h3cDot3OamConfigRevision, h3cDot3OamEventLogGroup=h3cDot3OamEventLogGroup, h3cDot3OamPeerStatus=h3cDot3OamPeerStatus, h3cDot3OamErrSymbolPeriodEventGroup=h3cDot3OamErrSymbolPeriodEventGroup, h3cDot3OamEntry=h3cDot3OamEntry, h3cDot3OamLoopbackTable=h3cDot3OamLoopbackTable, h3cDot3OamMaxOamPduSize=h3cDot3OamMaxOamPduSize, Dot3Oui=Dot3Oui, h3cDot3OamErrFrameSecsSummaryWindow=h3cDot3OamErrFrameSecsSummaryWindow, h3cDot3OamPeerGroup=h3cDot3OamPeerGroup, h3cDot3OamErrFramePeriodEventGroup=h3cDot3OamErrFramePeriodEventGroup, h3cDot3OamLoopbackCommand=h3cDot3OamLoopbackCommand, h3cDot3OamVariableResponseTx=h3cDot3OamVariableResponseTx, h3cDot3OamErrFrameSecsSummaryThreshold=h3cDot3OamErrFrameSecsSummaryThreshold, h3cDot3OamGroups=h3cDot3OamGroups, h3cDot3OamOrgSpecificRx=h3cDot3OamOrgSpecificRx, h3cDot3OamDuplicateEventNotificationTx=h3cDot3OamDuplicateEventNotificationTx, h3cDot3OamErrFramePeriodThreshold=h3cDot3OamErrFramePeriodThreshold, h3cDot3OamLoopbackControlRx=h3cDot3OamLoopbackControlRx, h3cDot3OamPeerMacAddress=h3cDot3OamPeerMacAddress, h3cDot3OamControlGroup=h3cDot3OamControlGroup, h3cDot3OamUnsupportedCodesTx=h3cDot3OamUnsupportedCodesTx, h3cDot3OamCompliance=h3cDot3OamCompliance, h3cDot3OamErrSymPeriodEvNotifEnable=h3cDot3OamErrSymPeriodEvNotifEnable, h3cDot3OamEventLogEntry=h3cDot3OamEventLogEntry)
