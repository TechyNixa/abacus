class Compute:
    def __init__(self, operator, operands):
        self.operator=operator
        self.operands=operands

    def add(self):
        pass

    def substract(self):
        difference=0
        for item in self.operands:
            difference-=item
        print(difference)    

    def divise(self):
        pass

    def multiply(self):
       sum=1
       for item in self.operands:
           sum*=item
        print(sum)   