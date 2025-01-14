from SpecImports import *
LobbyParent = 10014
BoilerParent = 10030
PipeLeftParent = 10023
PipeRightParent = 10032
OilParent = 10034
ControlParent = 10037
DuctParent = 10036
PaintMixerStorageParent = 10660
CenterSiloOutsideBattleCellParent = 10663
LavaRoomFoyerParent = 10664
LavaRoomStorageParent = 10665
LookoutBattleCellParent = 10666
CenterSiloBattleCellParent = 10064
CenterSiloParent = 20095
SigRoomParent = 20058
WestSiloParent = 20094
WestSiloBattleCellParent = 10047
EastSiloParent = 20096
EastSiloBattleCellParent = 10068
LobbyCell = 0
BoilerCell = 1
PipeLeftCell = 2
PipeRightCell = 3
OilCell = 4
ControlCell = 5
DuctCell = 6
CenterSiloCell = 7
SigRoomCell = 8
WestSiloCell = 9
EastSiloCell = 10
CenterSiloOutsideCell = 11
PaintMixerStorageCell = 12
LavaRoomFoyerCell = 13
LavaRoomStorageCell = 14
LookoutCell = 15
BattleCells = {LobbyCell: {'parentEntId': LobbyParent,
             'pos': Point3(0, 0, 0)},
 BoilerCell: {'parentEntId': BoilerParent,
              'pos': Point3(0, 0, 0)},
 OilCell: {'parentEntId': OilParent,
           'pos': Point3(0, 0, 0)},
 ControlCell: {'parentEntId': ControlParent,
               'pos': Point3(0, 0, 0)},
 CenterSiloCell: {'parentEntId': CenterSiloBattleCellParent,
                  'pos': Point3(0, 0, 0)},
 PipeLeftCell: {'parentEntId': PipeLeftParent,
                'pos': Point3(0, 0, 0)},
 PipeRightCell: {'parentEntId': PipeRightParent,
                 'pos': Point3(0, 0, 0)},
 DuctCell: {'parentEntId': DuctParent,
            'pos': Point3(0, 0, 0)},
 SigRoomCell: {'parentEntId': SigRoomParent,
               'pos': Point3(0, 0, 0)},
 WestSiloCell: {'parentEntId': WestSiloBattleCellParent,
                'pos': Point3(0, 0, 0)},
 EastSiloCell: {'parentEntId': EastSiloBattleCellParent,
                'pos': Point3(-20, -10, 0)},
 CenterSiloOutsideCell: {'parentEntId': CenterSiloOutsideBattleCellParent,
                'pos': Point3(0, 0, 0)},
 PaintMixerStorageCell: {'parentEntId': PaintMixerStorageParent,
                'pos': Point3(0, 0, 0)},
 LavaRoomFoyerCell: {'parentEntId': LavaRoomFoyerParent,
                'pos': Point3(0, 0, 0)},
 LavaRoomStorageCell: {'parentEntId': LavaRoomStorageParent,
                'pos': Point3(0, 0, 0)},
 LookoutCell: {'parentEntId': LookoutBattleCellParent,
               'pos': Point3(0, 0, 0)}}
CogData = [{'type': 'tm',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 7,
  'battleCell': LobbyCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20078,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 8,
  'battleCell': LobbyCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20009,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 9,
  'battleCell': LobbyCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20079,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 8,
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20076,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 9,
  'battleCell': BoilerCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20077,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 9,
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 8,
  'battleCell': OilCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60133,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 9,
  'battleCell': OilCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60134,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 9,
  'battleCell': OilCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60135,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 8,
  'battleCell': ControlCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20039,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 9,
  'battleCell': ControlCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20049,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 9,
  'battleCell': ControlCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20075,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20103,
  'skeleton': 0,
  'revives': 2},
 {'type': 'mh',
  'parentEntId': CenterSiloParent,
  'boss': 1,
  'level': 12,
  'battleCell': CenterSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 4},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20104,
  'skeleton': 0,
  'revives': 2},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20105,
  'skeleton': 0,
  'revives': 2},
 {'type': 'tm',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 9,
  'battleCell': WestSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20097,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 10,
  'battleCell': WestSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20098,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': WestSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20099,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 9,
  'battleCell': EastSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20100,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 10,
  'battleCell': EastSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20101,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': 11,
  'battleCell': EastSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20102,
  'skeleton': 0},
 {'type': 'tf',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 9,
  'battleCell': PipeLeftCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20109,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 9,
  'battleCell': PipeLeftCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20110,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeLeftCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20111,
  'skeleton': 1},
 {'type': 'tf',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 9,
  'battleCell': PipeRightCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20106,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 9,
  'battleCell': PipeRightCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20107,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 10,
  'battleCell': PipeRightCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20108,
  'skeleton': 1},
 {'type': 'ms',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 7,
  'battleCell': DuctCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20038,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 8,
  'battleCell': DuctCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20067,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 9,
  'battleCell': DuctCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20068,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 9,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 9,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 10,
  'battleCell': SigRoomCell,
  'pos': Point3(5, 3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 10,
  'battleCell': SigRoomCell,
  'pos': Point3(5, 10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'ms',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 10,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(-6, 30, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 1},
 {'type': 'ms',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 10,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(-2, 30, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 1},
 {'type': 'm',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(2, 30, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 1},
 {'type': 'm',
  'parentEntId': CenterSiloOutsideBattleCellParent,
  'boss': 0,
  'level': 11,
  'battleCell': CenterSiloOutsideCell,
  'pos': Point3(6, 30, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 1},
 {'type': 'm',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 10,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(-2, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 1},
 {'type': 'm',
  'parentEntId': PaintMixerStorageParent,
  'boss': 0,
  'level': 10,
  'battleCell': PaintMixerStorageCell,
  'pos': Point3(2, 0, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 1},
 {'type': 'm',
  'parentEntId': LavaRoomFoyerParent,
  'boss': 0,
  'level': 9,
  'battleCell': LavaRoomFoyerCell,
  'pos': Point3(0, -5, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'm',
  'parentEntId': LavaRoomFoyerParent,
  'boss': 0,
  'level': 9,
  'battleCell': LavaRoomFoyerCell,
  'pos': Point3(-5, 0, 0),
  'h': 90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'tf',
  'parentEntId': LavaRoomFoyerParent,
  'boss': 0,
  'level': 9,
  'battleCell': LavaRoomFoyerCell,
  'pos': Point3(0, 5, 0),
  'h': 0,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'tf',
  'parentEntId': LavaRoomFoyerParent,
  'boss': 0,
  'level': 9,
  'battleCell': LavaRoomFoyerCell,
  'pos': Point3(5, 0, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'm',
  'parentEntId': LavaRoomStorageParent,
  'boss': 0,
  'level': 10,
  'battleCell': LavaRoomStorageCell,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 1},
 {'type': 'm',
  'parentEntId': LavaRoomStorageParent,
  'boss': 0,
  'level': 10,
  'battleCell': LavaRoomStorageCell,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1,
  'revives': 1},
 {'type': 'm',
  'parentEntId': LookoutBattleCellParent,
  'boss': 0,
  'level': 8,
  'battleCell': LookoutCell,
  'pos': Point3(2, -6, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'mh',
  'parentEntId': LookoutBattleCellParent,
  'boss': 0,
  'level': 8,
  'battleCell': LookoutCell,
  'pos': Point3(-2, -6, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1},
 {'type': 'm',
  'parentEntId': LookoutBattleCellParent,
  'boss': 0,
  'level': 9,
  'battleCell': LookoutCell,
  'pos': Point3(22, 1.5, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'mh',
  'parentEntId': LookoutBattleCellParent,
  'boss': 0,
  'level': 9,
  'battleCell': LookoutCell,
  'pos': Point3(18, 5, 0),
  'h': 90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 1}]
ReserveCogData = [{'type': 'cc',
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': 2,
  'battleCell': LobbyCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20009,
  'skeleton': 0,
  'joinParent': 20018},
 {'type': 'cc',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 2,
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20076,
  'skeleton': 0,
  'joinParent': 20019},
 {'type': 'tm',
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': 2,
  'battleCell': BoilerCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20077,
  'skeleton': 0,
  'joinParent': 20019},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 3,
  'battleCell': OilCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60133,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': OilParent,
  'boss': 0,
  'level': 4,
  'battleCell': OilCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60135,
  'skeleton': 0},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 2,
  'battleCell': ControlCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20039,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 2,
  'battleCell': ControlCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20049,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': ControlParent,
  'boss': 0,
  'level': 2,
  'battleCell': ControlCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20075,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 3,
  'battleCell': CenterSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20103,
  'skeleton': 0},
 {'type': 'gh',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 5,
  'battleCell': CenterSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 3,
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20104,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': 3,
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20105,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 3,
  'battleCell': PipeLeftCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': 4,
  'battleCell': PipeLeftCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 3,
  'battleCell': PipeRightCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'tm',
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': 4,
  'battleCell': PipeRightCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': 1},
 {'type': 'cc',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 2,
  'battleCell': DuctCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20038,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': DuctParent,
  'boss': 0,
  'level': 2,
  'battleCell': DuctCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20067,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 3,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'type': 'tm',
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': 4,
  'battleCell': SigRoomCell,
  'pos': Point3(5, -3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
