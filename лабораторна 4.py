from dataclasses import dataclass


@dataclass
class TypeOfMainAssets:
    code: int
    type: str

@dataclass
class MoveOfMainAssets:
    name: str
    code: int
    remainder: float
    received: float
    output: float

type_array =[]
type_array.append(TypeOfMainAssets(100,"Бесарабський"))
type_array.append(TypeOfMainAssets(200,"Житній"))
type_array.append(TypeOfMainAssets(300,"Володимирський"))

move_array =[]
move_array.append(MoveOfMainAssets("02.11.2016",100,45,50,70))
move_array.append(MoveOfMainAssets("02.11.2016",200,35,30,50))
move_array.append(MoveOfMainAssets("02.11.16",300,35,30,45))
move_array.append(MoveOfMainAssets("14.11.2016",100,45,45,60))
move_array.append(MoveOfMainAssets("14.11.2016",200,40,40,50))
move_array.append(MoveOfMainAssets("14.11.2016",300,35,35,40))
move_array.append(MoveOfMainAssets("22.11.2016",10,40,40,60))
move_array.append(MoveOfMainAssets("22.11.2016",200,40,40,50))
move_array.append(MoveOfMainAssets("22.11.2016",300,40,40,60))

def printMoveOfMainAssets(moveofMainAssets):
    print("Дата: {name}, Код ринку: {code}, Картопля: {remainder}, Капуста: {received}, Цибуля: {output}")
          .format(name=MoveOfMainAssets.name, code=MoveOfMainAssets.code, remainder=MoveOfMainAssets.remainder,
               received=MoveOfMainAssets.received, output=MoveOfMainAssets.output))

for data in move_array:
    printMoveOfMainAssets

def printTypeOfMainAssets(typeofMainAssets):
       print("Код ринку: {code}, Найменування ринку: {type}")
           .format(code=typeOfMainAssets.code, type=typeOfMainAssets.type))

for data in type_array:
    printTypeOfMainAssets(data)

