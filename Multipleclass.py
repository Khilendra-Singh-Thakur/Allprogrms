class Cars:
    def __init__(self,CarName,CarModel):
        self.name=CarName
        self.model=CarModel
        
    def show(self):
        print(self.name)
        print(self.model)


class Ids:
    def __init__(self,CarId):
        self.ids=CarId

    def getId(self):
        print(self.ids)

class Main(Cars,Ids):
    def __init__(self,name,model,ids):
        Cars.__init__(self,name,model)
        Ids.__init__(self,ids)


Main1=Main('swift',500,1)
Main1.show()
Main1.getId()
