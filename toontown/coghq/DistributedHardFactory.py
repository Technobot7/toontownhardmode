from direct.directnotify import DirectNotifyGlobal
import DistributedFactory

class DistributedHardFactory(DistributedFactory.DistributedFactory):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedHardFactory')

    def __init__(self, cr):
        DistributedFactory.DistributedFactory.__init__(self, cr)

    def getFloorOuchLevel(self):
        return 8
