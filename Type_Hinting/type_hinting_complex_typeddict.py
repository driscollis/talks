from enum import IntEnum
from typing import TypedDict

class FordModel(IntEnum):
    F150 = 1
    Bronco = 2
    Mustang = 3

class FordModelType(TypedDict):
    name: str
    retail: float
    inventory: str

f150: FordModelType = {
            "name": "F-150",
            "retail": 38.6,
            'inventory': "trucks_2025.log",
        }

bronco: FordModelType =  {
            "name": "Bronco",
            "retail": 40.4,
            'inventory': "suvs_2025.log",
        }

mustang: FordModelType =  {
            "name": "Mustang",
            "retail": 32.5,
            'inventory': "cars_2025.log",
        }

CAR_INFO: dict[FordModel, FordModelType] = {
        FordModel.F150: f150,
        FordModel.Bronco: bronco,
        FordModel.Mustang: mustang
}

print(CAR_INFO[FordModel.Mustang]["inventory"])
print(CAR_INFO[FordModel.Mustang]["retail"]+10)