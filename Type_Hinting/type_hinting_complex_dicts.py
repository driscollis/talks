from enum import IntEnum

class FordModel(IntEnum):
    F150 = 1
    Bronco = 2
    Mustang = 3

CAR_INFO = {
        FordModel.F150: {
            "name": "F-150",
            "retail": 38.6,
            'inventory': "trucks_2025.log",
        },
        FordModel.Bronco: {
            "name": "Bronco",
            "retail": 40.4,
            'inventory': "suvs_2025.log",
        },
        FordModel.Mustang: {
            "name": "Mustang",
            "retail": 32.5,
            'inventory': "cars_2025.log",
        }
}

print(CAR_INFO[FordModel.Mustang]["inventory"])
print(CAR_INFO[FordModel.Mustang]["retail"]+10)