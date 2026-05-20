# Tower of Hanoi
import time


class Tower:
    def __init__(self):
        print("Welcome to Tower of hanoi")
        print()
        print("given position A=[3,2,1]      B=[]      C=[]    ")
        print()
        print("Expected output  A=[]         B=[]       C=[3,2,1]  ")
        self.A = []
        self.B = []
        self.C = []

    def tower(self, item):
        self.A.append(item)
        time.sleep(3)
        print("A=", self.A)
        print("items in tower A \n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A, "    ",     "B=", self.B, "     ", "C=", self.C)
        print("Pass One Completed\n")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A", self.A, "   ",    "B=", self.B, "   ", "C=", self.C)
        print("pass two completed=========\n")

    def pass3(self):
        self.temp = self.A.pop(0)
        self.A.append(self.temp)
        time.sleep(3)
        print("A", self.A, "   ",    "B=", self.B, "   ", "C=", self.C)
        print("pass three completed=========\n")

    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A, "    ",     "B=", self.B, "      ", "C=", self.C)
        print("Pass four Completed==========================================\n")

    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=", self.A, "    ",     "B=", self.B, "      ", "C=", self.C)
        print("Pass five Completed==========================================\n")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A, "    ",     "B=", self.B, "      ", "C=", self.C)
        print("Pass six Completed==========================================\n")

    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A, "    ",     "B=", self.B, "      ", "C=", self.C)
        print("Pass seven Completed==========================================\n")


obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()
