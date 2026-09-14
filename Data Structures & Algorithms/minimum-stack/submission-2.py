class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        self.curr_min = float('infinity')

    def push(self, val: int) -> None:
        self.curr_min = min(self.curr_min, val)
        self.stack.append(val)
        self.mins.append(self.curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        self.curr_min = self.mins[-1] if self.mins else float('infinity')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
