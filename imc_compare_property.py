class IMC:
    __pHeight = 0   #classe privada
    __pWeight = 0

    def __getHeight(self):  #encapsulamento
        return self.__pHeight
    def __setHeight(self, inValue):
        self.__pHeight = inValue
    height = property(__getHeight, __setHeight)

    def __getWeight(self):  #encapsulamento
        return self.__pWeight
    def __setWeight(self, inValue):
        self.__pWeight = inValue
    weight = property(__getWeight, __setWeight)

    def __eq__(self,other):
        return self.height == other.height and self.weight == other.weight