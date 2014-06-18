import pprint
from armoryengine.ALL import *

class WalletTools(PyBtcWallet):
    def forkWatchonlyWallet(self, newWalletFile):

        newWallet = WalletTools()
        newWallet.fileTypeStr = self.fileTypeStr
        newWallet.version = self.version
        newWallet.magicBytes = self.magicBytes
        newWallet.wltCreateDate = self.wltCreateDate
        newWallet.useEncryption = False
        newWallet.watchingOnly = True

        shortLabel = self.labelName
        longLabel = self.labelDescr

        startindex = 0

        while True:
            addresses = dict(self.addrMap.items()[startindex:startindex+2000])
            pprint.pprint(addresses)
            break
            if not addresses:
                break

            startindex += 2000

            newWallet.labelName = (shortLabel + ' (' + str(startindex) + ')')[:32]
            newWallet.labelDescr = (longLabel + ' (' + str(startindex) + ')')[:256]

            newWallet.commentsMap = self.commentsMap
            newWallet.opevalMap = self.opevalMap

            # newWallet.uniqueIDBin = self.uniqueIDBin
            newWallet.highestUsedChainIndex = self.highestUsedChainIndex
            newWallet.lastComputedChainAddr160 = self.lastComputedChainAddr160
            newWallet.lastComputedChainIndex = self.lastComputedChainIndex

            newWallet.addrMap = addresses
            newWallet.addrMap['ROOT'] = self.addrMap['ROOT']

            firstAddr = addresses[addresses.keys()[0]]

            newWallet.uniqueIDBin = (ADDRBYTE + firstAddr.getAddr160()[:5])[::-1]
            newWallet.uniqueIDB58 = binary_to_base58(newWallet.uniqueIDBin)


        # pprint.pprint(a1)
        # pprint.pprint(a2)
        # pprint.pprint(a3)

        # addcount = 0
        # for addr160, addrObj in self.addrMap.iteritems():
        #     addcount += 1
        #     if (addcount >= 10000):
        #         break
        #
        #     newWallet.addrMap[addr160] = addrObj.copy()
            # newWallet.addrMap[addr160].binPrivKey32_Encr = SecureBinaryData()
            # newWallet.addrMap[addr160].binPrivKey32_Plain = SecureBinaryData()
            # newWallet.addrMap[addr160].binInitVector16 = SecureBinaryData()
            # newWallet.addrMap[addr160].useEncryption = False
            # newWallet.addrMap[addr160].createPrivKeyNextUnlock = False

            newWallet.writeFreshWalletFile(newWalletFile + str(startindex) + '.wallet', shortLabel, longLabel)

        return newWallet




wltLoad = WalletTools().readWalletFile('/Users/xiaoyu/Desktop/p1_armory_JQ3HSakw_.watchonly.wallet')
# wltLoad = WalletTools().readWalletFile('/Users/xiaoyu/Library/Application Support/Armory/p1_armory_JQ3HSakw_.watchonly.part100000.wallet')
wltID = wltLoad.uniqueIDB58

wltLoad.forkWatchonlyWallet('/Users/xiaoyu/Library/Application Support/Armory/p1_armory_JQ3HSakw_.watchonly.part')

pprint.pprint(wltID)
