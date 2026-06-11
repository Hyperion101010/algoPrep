class MinStack:

    def __init__(self):
        self.sz = 0
        self.sp = 0

        """
            The trick is to have a stack made of two elements per stack node.
            So the stack node will be consisting of value and min_value till now.
            On every push we check its top and compare if value is less and insert it.
            On ever getMin we just check the top and return the value.
        """
        self.lst = [(1, 1e9) for i in range(int(1e5))]


    def push(self, value: int) -> None:
        (top_val, top_min) = self.lst[self.sp]
        if self.sz == 0:
            top_min = value

        min_val = 1e9

        if top_min > value:
            min_val = value
        else:
            min_val = top_min
        
        self.sz +=1
        self.sp = (self.sp + 1) % self.sz
        self.lst[self.sp] = (value, min_val)


    def pop(self) -> None:
        (val, min_element) = self.lst[self.sp]
        self.sz-=1

        if self.sz == 0:
            self.sp == 0
        else:
            self.sp = (self.sp - 1) % self.sz


    def top(self) -> int:
        (top_val, top_min) = self.lst[self.sp]
        return top_val

    def getMin(self) -> int:
        (top_val, top_min) = self.lst[self.sp]
        return top_min 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
