#
# PySNMP MIB module HH3C-8021PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-8021PAE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hh3cRhw, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cRhw")
dot1xPaePortNumber, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, Bits, Integer32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, iso, NotificationType, Counter32, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "Bits", "Integer32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "iso", "NotificationType", "Counter32", "IpAddress", "Unsigned32")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
hh3cpaeExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 6))
hh3cpaeExtMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cpaeExtMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hh3cpaeExtMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cpaeExtMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cpaeExtMib.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cpaeExtMib.setDescription('this file extends IEEE8021-PAE-MIB(802.1x)')
hh3cpaeExtMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1))
hh3cdot1xPaeSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1))
hh3cdot1xPaeAuthenticator = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2))
hh3cdot1xAuthQuietPeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 1), Unsigned32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xAuthQuietPeriod.setReference(' 9.4.1, quietPeriod')
if mibBuilder.loadTexts: hh3cdot1xAuthQuietPeriod.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthQuietPeriod.setDescription('The value, in seconds, of the quietPeriod constant currently in use by the Authenticator PAE state machine.')
hh3cdot1xAuthTxPeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 2), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xAuthTxPeriod.setReference(' 9.4.1, txPeriod')
if mibBuilder.loadTexts: hh3cdot1xAuthTxPeriod.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthTxPeriod.setDescription('The value, in seconds, of the txPeriod constant currently in use by the Authenticator PAE state machine.')
hh3cdot1xAuthSuppTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 3), Unsigned32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xAuthSuppTimeout.setReference(' 9.4.1, suppTimeout')
if mibBuilder.loadTexts: hh3cdot1xAuthSuppTimeout.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthSuppTimeout.setDescription('The value, in seconds, of the suppTimeout constant currently in use by the Backend Authentication state machine.')
hh3cdot1xAuthServerTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 4), Unsigned32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xAuthServerTimeout.setReference(' 9.4.1, serverTimeout')
if mibBuilder.loadTexts: hh3cdot1xAuthServerTimeout.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthServerTimeout.setDescription('The value, in seconds, of the serverTimeout constant currently in use by the Backend Authentication state machine.')
hh3cdot1xAuthMaxReq = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 5), Unsigned32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xAuthMaxReq.setReference(' 9.4.1, maxReq')
if mibBuilder.loadTexts: hh3cdot1xAuthMaxReq.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthMaxReq.setDescription('The value of the maxReq constant currently in use by the Backend Authentication state machine.')
hh3cdot1xAuthReAuthPeriod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 6), Unsigned32().clone(3600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xAuthReAuthPeriod.setReference(' 9.4.1, reAuthPeriod')
if mibBuilder.loadTexts: hh3cdot1xAuthReAuthPeriod.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthReAuthPeriod.setDescription('The value, in seconds, of the reAuthPeriod constant currently in use by the Reauthentication Timer state machine.')
hh3cdot1xAuthMethod = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("chap", 1), ("pap", 2), ("eap", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xAuthMethod.setReference('')
if mibBuilder.loadTexts: hh3cdot1xAuthMethod.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthMethod.setDescription('The value defines the 802.1X authenticatin method.')
hh3cdot1xAuthConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cdot1xAuthConfigExtTable.setReference(' 9.4.1 Authenticator Configuration')
if mibBuilder.loadTexts: hh3cdot1xAuthConfigExtTable.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthConfigExtTable.setDescription(' table extends dot1xAuthConfigTable')
hh3cdot1xAuthConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: hh3cdot1xAuthConfigExtEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xAuthConfigExtEntry.setDescription(' The configuration information for an Authenticator PAE.')
hh3cdot1xpaeportAuthAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xpaeportAuthAdminStatus.setReference('')
if mibBuilder.loadTexts: hh3cdot1xpaeportAuthAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xpaeportAuthAdminStatus.setDescription('The administrative enable/disable state for Port Access Control in a port.')
hh3cdot1xpaeportControlledType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("port", 1), ("mac", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xpaeportControlledType.setReference('')
if mibBuilder.loadTexts: hh3cdot1xpaeportControlledType.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xpaeportControlledType.setDescription('Port Access Control type , base port access control or base MAC access control')
hh3cdot1xpaeportMaxUserNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 3), Integer32().clone(256)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xpaeportMaxUserNum.setReference('')
if mibBuilder.loadTexts: hh3cdot1xpaeportMaxUserNum.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xpaeportMaxUserNum.setDescription('the max num of online user in a port')
hh3cdot1xpaeportUserNumNow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1xpaeportUserNumNow.setReference('')
if mibBuilder.loadTexts: hh3cdot1xpaeportUserNumNow.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xpaeportUserNumNow.setDescription('the num of online user in a port now ')
hh3cdot1xpaeportClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xpaeportClearStatistics.setReference('')
if mibBuilder.loadTexts: hh3cdot1xpaeportClearStatistics.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xpaeportClearStatistics.setDescription('Clear various Statistics viz. ')
hh3cdot1xpaeportMcastTrigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xpaeportMcastTrigStatus.setReference('')
if mibBuilder.loadTexts: hh3cdot1xpaeportMcastTrigStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xpaeportMcastTrigStatus.setDescription('The administrative enable/disable state for sending muticast EAP_REQ/ID packet.')
hh3cdot1xpaeportHandshakeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1xpaeportHandshakeStatus.setReference('')
if mibBuilder.loadTexts: hh3cdot1xpaeportHandshakeStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1xpaeportHandshakeStatus.setDescription('The administrative enable/disable state for sending handshake EAP_REQ/ID packet.')
hh3cdot1xPaeTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0))
hh3csupplicantproxycheck = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 1)).setObjects(("HH3C-8021PAE-MIB", "hh3cproxycheckVlanId"), ("HH3C-8021PAE-MIB", "hh3cproxycheckPortName"), ("HH3C-8021PAE-MIB", "hh3cproxycheckMacAddr"), ("HH3C-8021PAE-MIB", "hh3cproxycheckIpaddr"), ("HH3C-8021PAE-MIB", "hh3cproxycheckUsrName"))
if mibBuilder.loadTexts: hh3csupplicantproxycheck.setStatus('current')
if mibBuilder.loadTexts: hh3csupplicantproxycheck.setDescription('')
hh3cproxycheckVlanId = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cproxycheckVlanId.setStatus('current')
if mibBuilder.loadTexts: hh3cproxycheckVlanId.setDescription('.')
hh3cproxycheckPortName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 3), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cproxycheckPortName.setStatus('current')
if mibBuilder.loadTexts: hh3cproxycheckPortName.setDescription('.')
hh3cproxycheckMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 4), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cproxycheckMacAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cproxycheckMacAddr.setDescription('.')
hh3cproxycheckIpaddr = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 5), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cproxycheckIpaddr.setStatus('current')
if mibBuilder.loadTexts: hh3cproxycheckIpaddr.setDescription('.')
hh3cproxycheckUsrName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 6, 1, 0, 6), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cproxycheckUsrName.setStatus('current')
if mibBuilder.loadTexts: hh3cproxycheckUsrName.setDescription('.')
mibBuilder.exportSymbols("HH3C-8021PAE-MIB", hh3cdot1xPaeSystem=hh3cdot1xPaeSystem, hh3cproxycheckUsrName=hh3cproxycheckUsrName, hh3cdot1xAuthConfigExtEntry=hh3cdot1xAuthConfigExtEntry, hh3cproxycheckMacAddr=hh3cproxycheckMacAddr, hh3cpaeExtMibObjects=hh3cpaeExtMibObjects, hh3cdot1xpaeportClearStatistics=hh3cdot1xpaeportClearStatistics, hh3csupplicantproxycheck=hh3csupplicantproxycheck, hh3cdot1xAuthQuietPeriod=hh3cdot1xAuthQuietPeriod, hh3cdot1xpaeportControlledType=hh3cdot1xpaeportControlledType, hh3cpaeExtMib=hh3cpaeExtMib, hh3cdot1xAuthMaxReq=hh3cdot1xAuthMaxReq, hh3cproxycheckIpaddr=hh3cproxycheckIpaddr, hh3cdot1xAuthTxPeriod=hh3cdot1xAuthTxPeriod, hh3cproxycheckPortName=hh3cproxycheckPortName, hh3cdot1xAuthConfigExtTable=hh3cdot1xAuthConfigExtTable, hh3cdot1xpaeportAuthAdminStatus=hh3cdot1xpaeportAuthAdminStatus, hh3cdot1xAuthServerTimeout=hh3cdot1xAuthServerTimeout, hh3cdot1xpaeportUserNumNow=hh3cdot1xpaeportUserNumNow, hh3cdot1xAuthSuppTimeout=hh3cdot1xAuthSuppTimeout, hh3cdot1xAuthReAuthPeriod=hh3cdot1xAuthReAuthPeriod, PYSNMP_MODULE_ID=hh3cpaeExtMib, hh3cdot1xAuthMethod=hh3cdot1xAuthMethod, hh3cdot1xpaeportMaxUserNum=hh3cdot1xpaeportMaxUserNum, hh3cdot1xPaeTraps=hh3cdot1xPaeTraps, hh3cproxycheckVlanId=hh3cproxycheckVlanId, hh3cdot1xpaeportHandshakeStatus=hh3cdot1xpaeportHandshakeStatus, hh3cdot1xpaeportMcastTrigStatus=hh3cdot1xpaeportMcastTrigStatus, hh3cdot1xPaeAuthenticator=hh3cdot1xPaeAuthenticator)
