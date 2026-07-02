class MinStack:

    def __init__(self):
        self.ls = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        if not self.min_val or self.min_val[-1] >= val:
            self.min_val.append(val)

        self.ls.append(val)
        return None


        

    def pop(self) -> None:
        if self.ls[-1] == self.min_val[-1]:
            self.min_val.pop()
        self.ls.pop()
        return None
        

    def top(self) -> int:
        if self.ls:
            return self.ls[-1]
        return None
        

    def getMin(self) -> int:
        print(self.ls)
        print(self.min_val)
        if self.ls:
            return self.min_val[-1]
        return None

        
