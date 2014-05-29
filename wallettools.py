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

        newWallet.labelName = (shortLabel + ' (Part)')[:32]
        newWallet.labelDescr = (longLabel + ' (Part copy)')[:256]

        newWallet.addrMap['ROOT'] = self.addrMap['ROOT']

        newWallet.commentsMap = self.commentsMap
        newWallet.opevalMap = self.opevalMap

        newWallet.uniqueIDBin = self.uniqueIDBin
        newWallet.highestUsedChainIndex = self.highestUsedChainIndex
        newWallet.lastComputedChainAddr160 = self.lastComputedChainAddr160
        newWallet.lastComputedChainIndex = self.lastComputedChainIndex

        addcount = 0
        for addr160, addrObj in self.addrMap.iteritems():
            addcount += 1
            if (addcount >= 1000):
                break

            newWallet.addrMap[addr160] = addrObj.copy()
            # newWallet.addrMap[addr160].binPrivKey32_Encr = SecureBinaryData()
            # newWallet.addrMap[addr160].binPrivKey32_Plain = SecureBinaryData()
            # newWallet.addrMap[addr160].binInitVector16 = SecureBinaryData()
            # newWallet.addrMap[addr160].useEncryption = False
            # newWallet.addrMap[addr160].createPrivKeyNextUnlock = False

        newWallet.writeFreshWalletFile(newWalletFile, shortLabel, longLabel)
        return newWallet




wltLoad = WalletTools().readWalletFile('/Users/xiaoyu/Desktop/p1_armory_JQ3HSakw_.watchonly.wallet');
wltID = wltLoad.uniqueIDB58

wltLoad.forkWatchonlyWallet('/Users/xiaoyu/Library/Application Support/Armory/p1_armory_JQ3HSakw_.watchonly.part1.wallet')

pprint.pprint(wltID)
