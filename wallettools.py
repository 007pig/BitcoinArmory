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

        newWallet.labelName = (shortLabel + ' (Part 2)')[:32]
        newWallet.labelDescr = (longLabel + ' (Part 2)')[:256]

        newWallet.commentsMap = self.commentsMap
        newWallet.opevalMap = self.opevalMap

        # newWallet.uniqueIDBin = self.uniqueIDBin
        newWallet.highestUsedChainIndex = self.highestUsedChainIndex
        newWallet.lastComputedChainAddr160 = self.lastComputedChainAddr160
        newWallet.lastComputedChainIndex = self.lastComputedChainIndex

        a1 = dict(self.addrMap.items()[0:5000])
        a2 = dict(self.addrMap.items()[5000:10000])
        a3 = dict(self.addrMap.items()[10000:15000])

        newWallet.addrMap = a2
        newWallet.addrMap['ROOT'] = self.addrMap['ROOT']

        firstAddr = a2[a2.keys()[0]]

        self.uniqueIDBin = (ADDRBYTE + firstAddr.getAddr160()[:5])[::-1]
        self.uniqueIDB58 = binary_to_base58(self.uniqueIDBin)


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

        newWallet.writeFreshWalletFile(newWalletFile, shortLabel, longLabel)
        return newWallet




wltLoad = WalletTools().readWalletFile('/Users/xiaoyu/Desktop/p1_armory_JQ3HSakw_.watchonly.wallet')
wltID = wltLoad.uniqueIDB58

wltLoad.forkWatchonlyWallet('/Users/xiaoyu/Library/Application Support/Armory/p1_armory_JQ3HSakw_.watchonly.part2.wallet')

pprint.pprint(wltID)
