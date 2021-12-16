class packet:
    def __init__(self, version, operator, subPacket=False):
        self.version=version
        self.operator=operator
        if subPacket:
            self.subPacket=[]
        else:
            self.value=None

    def __repr__(self):
        if self.operator==4:
            return f"Packet(Version: {self.version}, Operator: {self.operator}), Value: {self.value}"
        else:
            return f"Packet(Version: {self.version}, Operator: {self.operator}), SubPacket: {self.subPacket}"
    
    def getVersionTotal(self):
        if self.operator==4:
            return self.version
        else:
            return self.version+sum(x.getVersionTotal() for x in self.subPacket)
        
    def setValue(self, value):
        self.value=value

    def addSubpacket(self, packet):
        self.subPacket.append(packet)

    def calculate(self):
        if self.operator==4:
            return self.value
        if self.operator==0:
            return sum(i.calculate() for i in self.subPacket)
        if self.operator==1:
            i=1
            for j in self.subPacket:
                i*=j.calculate()
            return i
        if self.operator==2:
            return min(i.calculate() for i in self.subPacket)
        if self.operator==3:
            return max(i.calculate() for i in self.subPacket)
        if self.operator==5:
            return 1 if self.subPacket[0].calculate()>self.subPacket[1].calculate() else 0
        if self.operator==6:
            return 1 if self.subPacket[0].calculate()<self.subPacket[1].calculate() else 0
        if self.operator==7:
            return 1 if self.subPacket[0].calculate()==self.subPacket[1].calculate() else 0
        

def parsePackets(obj, mainPacket=True):
    newObject=packet(int(obj[0:3],2), int(obj[3:6],2), False if int(obj[3:6],2)==4 else True)
    packetContent=obj[6:]
    if newObject.operator==4:
        flag = 1
        content=""
        while flag:
            flag=int(packetContent[0])
            content+=packetContent[1:5]
            packetContent=packetContent[5:]
        newObject.setValue(int(content,2))
        return (newObject, packetContent)
    else:
        type = int(packetContent[0])
        packetContent=packetContent[1:]
        if type:
            subPackets=int(packetContent[0:11],2)
            packetContent=packetContent[11:]
            for i in range(subPackets):
                subObject, packetContent=parsePackets(packetContent)
                newObject.addSubpacket(subObject)
            return (newObject, packetContent)
        else:
            length=int(packetContent[0:15],2)
            currentPacketContent=packetContent[15:15+length]
            restPacketContent=packetContent[15+length:]
            while currentPacketContent:
                subObject, currentPacketContent=parsePackets(currentPacketContent)
                newObject.addSubpacket(subObject)
            return (newObject, restPacketContent)

import aoc_common
puzzles=aoc_common.fileToArray("test16.txt")
binaryPuzzles=[]
packets=[]
for i in puzzles:
    decimalPuzzle=int(i,16)
    binPuzzle=bin(decimalPuzzle)[2:]
    if len(binPuzzle)%4!=0:
        for _ in range(4-len(binPuzzle)%4):
            binPuzzle="0"+binPuzzle
    if i[0]=="0":
        binPuzzle="0000"+binPuzzle
    newObject, _ = parsePackets(binPuzzle)
    print(newObject)
    print(newObject.getVersionTotal())
    print(newObject.calculate())