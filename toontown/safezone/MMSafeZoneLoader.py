from toontown.safezone import MMPlayground
from toontown.safezone import SafeZoneLoader
import random


class MMSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = MMPlayground.MMPlayground
        self.musicFile = random.choice(['phase_6/audio/bgm/MM_nbrhood1.ogg', 'phase_6/audio/bgm/MM_nbrhood2.ogg', 'phase_6/audio/bgm/MM_nbrhood3.ogg'])                         
        self.activityMusicFile = 'phase_6/audio/bgm/MM_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/minnies_melody_land_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_MM_sz.pdna'
