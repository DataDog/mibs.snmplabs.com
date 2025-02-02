#
# PySNMP MIB module CISCO-LWAPP-MESH-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-MESH-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:48:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cLApSysMacAddress, cLApName = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress", "cLApName")
clMeshNeighborMacAddress, clMeshNodeBackhaul = mibBuilder.importSymbols("CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress", "clMeshNodeBackhaul")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Counter64, MibIdentifier, TimeTicks, ModuleIdentity, Gauge32, IpAddress, Unsigned32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Gauge32", "IpAddress", "Unsigned32", "iso", "Counter32")
TruthValue, TimeInterval, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeInterval", "TimeStamp", "DisplayString", "TextualConvention")
ciscoLwappMeshStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 617))
ciscoLwappMeshStatsMIB.setRevisions(('2010-09-01 00:00', '2007-03-12 00:00',))
if mibBuilder.loadTexts: ciscoLwappMeshStatsMIB.setLastUpdated('201009010000Z')
if mibBuilder.loadTexts: ciscoLwappMeshStatsMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappMeshStatsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 0))
ciscoLwappMeshStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 1))
ciscoLwappMeshStatsMIBConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 2))
ciscoLwappMeshStatsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 3))
ciscoLwappMeshNodeStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1))
ciscoLwappMeshNeighStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2))
ciscoLwappMeshStatsMIBNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 3))
ciscoLwappMeshAccessClass = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4))
ciscoLwappMeshDataRateStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5))
clMeshNodeStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1), )
if mibBuilder.loadTexts: clMeshNodeStatsTable.setStatus('current')
clMeshNodeStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"))
if mibBuilder.loadTexts: clMeshNodeStatsEntry.setStatus('current')
clMeshNodeMalformedNeighPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeMalformedNeighPkts.setStatus('current')
clMeshNodePoorNeighSnrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodePoorNeighSnrPkts.setStatus('current')
clMeshNodeExcludedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeExcludedPkts.setStatus('current')
clMeshNodeRxNeighReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeRxNeighReq.setStatus('current')
clMeshNodeRxNeighRsp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeRxNeighRsp.setStatus('current')
clMeshNodeTxNeighReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeTxNeighReq.setStatus('current')
clMeshNodeTxNeighRsp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeTxNeighRsp.setStatus('current')
clMeshNodeParentChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 8), Counter32()).setUnits('parent-switches').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeParentChanges.setStatus('current')
clMeshNodeSecBackhaulCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeSecBackhaulCount.setStatus('current')
clMeshNodeAssociationCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeAssociationCount.setStatus('current')
clMeshNodePktQueueStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2), )
if mibBuilder.loadTexts: clMeshNodePktQueueStatsTable.setStatus('current')
clMeshNodePktQueueStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueueIndex"))
if mibBuilder.loadTexts: clMeshNodePktQueueStatsEntry.setStatus('current')
clMeshNodePktQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("silver", 1), ("gold", 2), ("platinum", 3), ("bronze", 4), ("management", 5))))
if mibBuilder.loadTexts: clMeshNodePktQueueIndex.setStatus('current')
clMeshNodePktQueueAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 2), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodePktQueueAvg.setStatus('current')
clMeshNodePktQueuePeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 3), Gauge32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodePktQueuePeak.setStatus('current')
clMeshNodePktQueuePktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodePktQueuePktsDropped.setStatus('current')
clMeshNodePktQueueTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 5), TimeStamp()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodePktQueueTimeStamp.setStatus('current')
clMeshNodePktQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 2, 1, 6), Unsigned32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodePktQueueSize.setStatus('current')
clMeshNodeSecStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3), )
if mibBuilder.loadTexts: clMeshNodeSecStatsTable.setStatus('current')
clMeshNodeSecStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"))
if mibBuilder.loadTexts: clMeshNodeSecStatsEntry.setStatus('current')
clMeshNodeSecTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeSecTxPkts.setStatus('current')
clMeshNodeSecRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeSecRxPkts.setStatus('current')
clMeshNodeAssocReqFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeAssocReqFailures.setStatus('current')
clMeshNodeAssocReqTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeAssocReqTimeouts.setStatus('current')
clMeshNodeAssocReqSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeAssocReqSuccess.setStatus('current')
clMeshNodeAuthReqFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeAuthReqFailures.setStatus('current')
clMeshNodeAuthReqTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeAuthReqTimeouts.setStatus('current')
clMeshNodeAuthReqSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeAuthReqSuccess.setStatus('current')
clMeshNodeReassocReqFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeReassocReqFailures.setStatus('current')
clMeshNodeReassocReqTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 10), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeReassocReqTimeouts.setStatus('current')
clMeshNodeReassocReqSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 11), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeReassocReqSuccess.setStatus('current')
clMeshNodeReauthReqFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 12), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeReauthReqFailures.setStatus('current')
clMeshNodeReauthReqTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 13), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeReauthReqTimeouts.setStatus('current')
clMeshNodeReauthReqSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 14), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeReauthReqSuccess.setStatus('current')
clMeshNodeUnknownAssocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 15), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeUnknownAssocReq.setStatus('current')
clMeshNodeInvalidAssocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 16), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeInvalidAssocReq.setStatus('current')
clMeshNodeUnknownReauthReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 17), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeUnknownReauthReq.setStatus('current')
clMeshNodeInvalidReauthReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 18), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeInvalidReauthReq.setStatus('current')
clMeshNodeUnknownReassocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 19), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeUnknownReassocReq.setStatus('current')
clMeshNodeInvalidReassocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 1, 3, 1, 20), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNodeInvalidReassocReq.setStatus('current')
clMeshNeighStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1), )
if mibBuilder.loadTexts: clMeshNeighStatsTable.setStatus('current')
clMeshNeighStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"))
if mibBuilder.loadTexts: clMeshNeighStatsEntry.setStatus('current')
clMeshNeighAsParentTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighAsParentTxPkts.setStatus('current')
clMeshNeighAsParentRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighAsParentRxPkts.setStatus('current')
clMeshNeighTotalTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighTotalTxPkts.setStatus('current')
clMeshNeighSuccessTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighSuccessTxPkts.setStatus('current')
clMeshNeighRetriesTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighRetriesTxPkts.setStatus('current')
clMeshNeighPoorSnrRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 2, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshNeighPoorSnrRxPkts.setStatus('current')
clMeshAccessClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1), )
if mibBuilder.loadTexts: clMeshAccessClassTable.setStatus('current')
clMeshAccessClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"))
if mibBuilder.loadTexts: clMeshAccessClassEntry.setStatus('current')
clMeshAccessClassTotalTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshAccessClassTotalTxPkts.setStatus('current')
clMeshAccessClassSuccTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshAccessClassSuccTxPkts.setStatus('current')
clMeshAccessClassRetryPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshAccessClassRetryPkts.setStatus('current')
clMeshAccessClassRTSAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshAccessClassRTSAttempts.setStatus('current')
clMeshAccessClassRTSSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 4, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshAccessClassRTSSuccess.setStatus('current')
clMeshDataRateStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1), )
if mibBuilder.loadTexts: clMeshDataRateStatsTable.setStatus('current')
clMeshDataRateStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"), (0, "CISCO-LWAPP-MESH-STATS-MIB", "cLMeshDataRateIndex"))
if mibBuilder.loadTexts: clMeshDataRateStatsEntry.setStatus('current')
cLMeshDataRateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1, 1, 1), Unsigned32()).setUnits('Mbps')
if mibBuilder.loadTexts: cLMeshDataRateIndex.setStatus('current')
clMeshDataRateSuccTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshDataRateSuccTxPkts.setStatus('current')
clMeshDataRateTxAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clMeshDataRateTxAttempts.setStatus('current')
clMeshNodeQueueOverflowNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeQueueOverflowNotifEnabled.setStatus('current')
clMeshNodeStatsTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 2), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(18000, 90000)).clone(18000)).setUnits('hundredths-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeStatsTimeInterval.setStatus('current')
clMeshNodeSecBackhaulChangeNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeSecBackhaulChangeNotifEnabled.setStatus('current')
clMeshNodeExcessiveAssociationNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeExcessiveAssociationNotifEnabled.setStatus('current')
clMeshNodeExcessiveAssociationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 617, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(25)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clMeshNodeExcessiveAssociationThreshold.setStatus('current')
clMeshInitiatingApName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 617, 1, 3, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clMeshInitiatingApName.setStatus('current')
ciscoLwappMeshQueueOverflow = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 617, 0, 1)).setObjects(("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueuePeak"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueuePktsDropped"))
if mibBuilder.loadTexts: ciscoLwappMeshQueueOverflow.setStatus('current')
ciscoLwappMeshExcessiveAssociation = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 617, 0, 2)).setObjects(("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssociationCount"))
if mibBuilder.loadTexts: ciscoLwappMeshExcessiveAssociation.setStatus('current')
ciscoLwappMeshSecBackhaulChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 617, 0, 3)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshInitiatingApName"), ("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecBackhaulCount"))
if mibBuilder.loadTexts: ciscoLwappMeshSecBackhaulChange.setStatus('current')
ciscoLwappMeshStatsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 1))
ciscoLwappMeshStatsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2))
ciscoLwappMeshStatsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 1, 1)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshNodeStatsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshNodePktQueueStatsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshNodeSecStatsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshStatsConfigObjsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshStatsNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshStatsMIBCompliance = ciscoLwappMeshStatsMIBCompliance.setStatus('deprecated')
ciscoLwappMeshStatsMIBComplianceR01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 1, 2)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshNodeStatsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshNodePktQueueStatsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshNodeSecStatsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshStatsConfigObjsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshStatsNotifsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshNeighStatsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshStatsNotifObjsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshAccessClassGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshDataRateStatsGroup"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshNodeStatsGroupSup1"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshStatsConfigObjsGroupSup1"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshStatsNotifsGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshStatsMIBComplianceR01 = ciscoLwappMeshStatsMIBComplianceR01.setStatus('current')
ciscoLwappMeshNodeStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 1)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeMalformedNeighPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePoorNeighSnrPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeExcludedPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeRxNeighReq"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeRxNeighRsp"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeTxNeighReq"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeTxNeighRsp"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeParentChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNodeStatsGroup = ciscoLwappMeshNodeStatsGroup.setStatus('current')
ciscoLwappMeshNodePktQueueStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 2)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueueAvg"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueuePeak"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueuePktsDropped"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueueTimeStamp"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodePktQueueSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNodePktQueueStatsGroup = ciscoLwappMeshNodePktQueueStatsGroup.setStatus('current')
ciscoLwappMeshNodeSecStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 3)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecTxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecRxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssocReqFailures"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssocReqTimeouts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssocReqSuccess"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAuthReqFailures"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAuthReqTimeouts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAuthReqSuccess"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReassocReqFailures"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReassocReqTimeouts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReassocReqSuccess"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReauthReqFailures"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReauthReqTimeouts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeReauthReqSuccess"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeUnknownAssocReq"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeInvalidAssocReq"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeUnknownReauthReq"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeInvalidReauthReq"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeUnknownReassocReq"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeInvalidReassocReq"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNodeSecStatsGroup = ciscoLwappMeshNodeSecStatsGroup.setStatus('current')
ciscoLwappMeshStatsConfigObjsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 4)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeQueueOverflowNotifEnabled"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeStatsTimeInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshStatsConfigObjsGroup = ciscoLwappMeshStatsConfigObjsGroup.setStatus('current')
ciscoLwappMeshStatsNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 5)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshQueueOverflow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshStatsNotifsGroup = ciscoLwappMeshStatsNotifsGroup.setStatus('current')
ciscoLwappMeshNeighStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 6)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighAsParentTxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighAsParentRxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighTotalTxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighSuccessTxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighRetriesTxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNeighPoorSnrRxPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNeighStatsGroup = ciscoLwappMeshNeighStatsGroup.setStatus('current')
ciscoLwappMeshStatsNotifObjsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 7)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshInitiatingApName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshStatsNotifObjsGroup = ciscoLwappMeshStatsNotifObjsGroup.setStatus('current')
ciscoLwappMeshAccessClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 8)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassTotalTxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassSuccTxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassRetryPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassRTSAttempts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshAccessClassRTSSuccess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshAccessClassGroup = ciscoLwappMeshAccessClassGroup.setStatus('current')
ciscoLwappMeshDataRateStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 9)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshDataRateSuccTxPkts"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshDataRateTxAttempts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshDataRateStatsGroup = ciscoLwappMeshDataRateStatsGroup.setStatus('current')
ciscoLwappMeshNodeStatsGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 10)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecBackhaulCount"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeAssociationCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshNodeStatsGroupSup1 = ciscoLwappMeshNodeStatsGroupSup1.setStatus('current')
ciscoLwappMeshStatsConfigObjsGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 11)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeSecBackhaulChangeNotifEnabled"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeExcessiveAssociationNotifEnabled"), ("CISCO-LWAPP-MESH-STATS-MIB", "clMeshNodeExcessiveAssociationThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshStatsConfigObjsGroupSup1 = ciscoLwappMeshStatsConfigObjsGroupSup1.setStatus('current')
ciscoLwappMeshStatsNotifsGroupSup1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 617, 3, 2, 12)).setObjects(("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshExcessiveAssociation"), ("CISCO-LWAPP-MESH-STATS-MIB", "ciscoLwappMeshSecBackhaulChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappMeshStatsNotifsGroupSup1 = ciscoLwappMeshStatsNotifsGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-MESH-STATS-MIB", ciscoLwappMeshStatsMIBNotifs=ciscoLwappMeshStatsMIBNotifs, ciscoLwappMeshNodeSecStatsGroup=ciscoLwappMeshNodeSecStatsGroup, clMeshNodeReauthReqFailures=clMeshNodeReauthReqFailures, clMeshNeighAsParentRxPkts=clMeshNeighAsParentRxPkts, ciscoLwappMeshStatsMIB=ciscoLwappMeshStatsMIB, ciscoLwappMeshStatsNotifsGroup=ciscoLwappMeshStatsNotifsGroup, ciscoLwappMeshStatsMIBComplianceR01=ciscoLwappMeshStatsMIBComplianceR01, clMeshNodeTxNeighReq=clMeshNodeTxNeighReq, clMeshNeighAsParentTxPkts=clMeshNeighAsParentTxPkts, clMeshNodeReauthReqTimeouts=clMeshNodeReauthReqTimeouts, ciscoLwappMeshStatsConfigObjsGroup=ciscoLwappMeshStatsConfigObjsGroup, clMeshAccessClassTable=clMeshAccessClassTable, clMeshNodeSecRxPkts=clMeshNodeSecRxPkts, ciscoLwappMeshDataRateStats=ciscoLwappMeshDataRateStats, clMeshAccessClassEntry=clMeshAccessClassEntry, clMeshNodeSecBackhaulCount=clMeshNodeSecBackhaulCount, clMeshNodeTxNeighRsp=clMeshNodeTxNeighRsp, clMeshNodeAssocReqFailures=clMeshNodeAssocReqFailures, clMeshNodeReassocReqTimeouts=clMeshNodeReassocReqTimeouts, ciscoLwappMeshStatsConfigObjsGroupSup1=ciscoLwappMeshStatsConfigObjsGroupSup1, clMeshNodeAuthReqFailures=clMeshNodeAuthReqFailures, clMeshNodeRxNeighRsp=clMeshNodeRxNeighRsp, clMeshNodeExcessiveAssociationNotifEnabled=clMeshNodeExcessiveAssociationNotifEnabled, clMeshInitiatingApName=clMeshInitiatingApName, clMeshNodePktQueueIndex=clMeshNodePktQueueIndex, clMeshNodeExcessiveAssociationThreshold=clMeshNodeExcessiveAssociationThreshold, clMeshDataRateSuccTxPkts=clMeshDataRateSuccTxPkts, ciscoLwappMeshAccessClass=ciscoLwappMeshAccessClass, PYSNMP_MODULE_ID=ciscoLwappMeshStatsMIB, clMeshNeighTotalTxPkts=clMeshNeighTotalTxPkts, clMeshNeighStatsTable=clMeshNeighStatsTable, clMeshAccessClassRTSSuccess=clMeshAccessClassRTSSuccess, clMeshNodeStatsEntry=clMeshNodeStatsEntry, clMeshNodeStatsTimeInterval=clMeshNodeStatsTimeInterval, ciscoLwappMeshQueueOverflow=ciscoLwappMeshQueueOverflow, ciscoLwappMeshSecBackhaulChange=ciscoLwappMeshSecBackhaulChange, clMeshDataRateStatsTable=clMeshDataRateStatsTable, clMeshNodeParentChanges=clMeshNodeParentChanges, clMeshNodeSecBackhaulChangeNotifEnabled=clMeshNodeSecBackhaulChangeNotifEnabled, clMeshAccessClassSuccTxPkts=clMeshAccessClassSuccTxPkts, clMeshNeighSuccessTxPkts=clMeshNeighSuccessTxPkts, clMeshNodeExcludedPkts=clMeshNodeExcludedPkts, clMeshNeighPoorSnrRxPkts=clMeshNeighPoorSnrRxPkts, ciscoLwappMeshNodePktQueueStatsGroup=ciscoLwappMeshNodePktQueueStatsGroup, clMeshNodePktQueueTimeStamp=clMeshNodePktQueueTimeStamp, clMeshNodeMalformedNeighPkts=clMeshNodeMalformedNeighPkts, ciscoLwappMeshStatsMIBCompliance=ciscoLwappMeshStatsMIBCompliance, clMeshNodeUnknownReassocReq=clMeshNodeUnknownReassocReq, clMeshNodePktQueueSize=clMeshNodePktQueueSize, clMeshNodePktQueueAvg=clMeshNodePktQueueAvg, clMeshAccessClassRetryPkts=clMeshAccessClassRetryPkts, ciscoLwappMeshStatsMIBCompliances=ciscoLwappMeshStatsMIBCompliances, clMeshNodeQueueOverflowNotifEnabled=clMeshNodeQueueOverflowNotifEnabled, clMeshNodeUnknownAssocReq=clMeshNodeUnknownAssocReq, clMeshNodeAuthReqTimeouts=clMeshNodeAuthReqTimeouts, clMeshNodeStatsTable=clMeshNodeStatsTable, ciscoLwappMeshAccessClassGroup=ciscoLwappMeshAccessClassGroup, clMeshNodeAssocReqTimeouts=clMeshNodeAssocReqTimeouts, cLMeshDataRateIndex=cLMeshDataRateIndex, clMeshNodeInvalidAssocReq=clMeshNodeInvalidAssocReq, clMeshNodePktQueueStatsEntry=clMeshNodePktQueueStatsEntry, clMeshNodeSecStatsEntry=clMeshNodeSecStatsEntry, ciscoLwappMeshNodeStatsGroup=ciscoLwappMeshNodeStatsGroup, clMeshAccessClassRTSAttempts=clMeshAccessClassRTSAttempts, ciscoLwappMeshStatsMIBConfigObjects=ciscoLwappMeshStatsMIBConfigObjects, clMeshNodePktQueuePeak=clMeshNodePktQueuePeak, clMeshAccessClassTotalTxPkts=clMeshAccessClassTotalTxPkts, clMeshNodePoorNeighSnrPkts=clMeshNodePoorNeighSnrPkts, ciscoLwappMeshStatsMIBGroups=ciscoLwappMeshStatsMIBGroups, clMeshNodeSecStatsTable=clMeshNodeSecStatsTable, ciscoLwappMeshDataRateStatsGroup=ciscoLwappMeshDataRateStatsGroup, ciscoLwappMeshStatsNotifsGroupSup1=ciscoLwappMeshStatsNotifsGroupSup1, clMeshNodeInvalidReauthReq=clMeshNodeInvalidReauthReq, clMeshNodeAssocReqSuccess=clMeshNodeAssocReqSuccess, clMeshNodeSecTxPkts=clMeshNodeSecTxPkts, clMeshNodeReassocReqSuccess=clMeshNodeReassocReqSuccess, clMeshNeighStatsEntry=clMeshNeighStatsEntry, clMeshNodeRxNeighReq=clMeshNodeRxNeighReq, clMeshNodeReauthReqSuccess=clMeshNodeReauthReqSuccess, clMeshDataRateTxAttempts=clMeshDataRateTxAttempts, ciscoLwappMeshExcessiveAssociation=ciscoLwappMeshExcessiveAssociation, clMeshNodeReassocReqFailures=clMeshNodeReassocReqFailures, clMeshNeighRetriesTxPkts=clMeshNeighRetriesTxPkts, clMeshNodePktQueuePktsDropped=clMeshNodePktQueuePktsDropped, ciscoLwappMeshNeighStatsGroup=ciscoLwappMeshNeighStatsGroup, ciscoLwappMeshStatsMIBNotifObjects=ciscoLwappMeshStatsMIBNotifObjects, clMeshNodeUnknownReauthReq=clMeshNodeUnknownReauthReq, ciscoLwappMeshStatsMIBObjects=ciscoLwappMeshStatsMIBObjects, clMeshDataRateStatsEntry=clMeshDataRateStatsEntry, ciscoLwappMeshStatsNotifObjsGroup=ciscoLwappMeshStatsNotifObjsGroup, ciscoLwappMeshNodeStatsGroupSup1=ciscoLwappMeshNodeStatsGroupSup1, ciscoLwappMeshStatsMIBConform=ciscoLwappMeshStatsMIBConform, clMeshNodeAuthReqSuccess=clMeshNodeAuthReqSuccess, clMeshNodeInvalidReassocReq=clMeshNodeInvalidReassocReq, clMeshNodePktQueueStatsTable=clMeshNodePktQueueStatsTable, ciscoLwappMeshNodeStats=ciscoLwappMeshNodeStats, ciscoLwappMeshNeighStats=ciscoLwappMeshNeighStats, clMeshNodeAssociationCount=clMeshNodeAssociationCount)
