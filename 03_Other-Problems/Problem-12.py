class TwoStacks:
    def __init__(self):
        # Initialize two stacks as empty lists
        self.stack1 = []
        self.stack2 = []
        self.arr = [None] * 5
        self.p = 0
        self.n = len(self.arr) - 1
        

    # Function to push an integer into stack 1
    def push1(self, x):
        if self.p == self.n - 1:
            self.arr[self.p] == -1
        self.stack1.append(x)


    # Function to push an integer into stack 2
    def push2(self, x):
        pass

    # Function to remove an element from top of stack 1
    def pop1(self):
        pass

    # Function to remove an element from top of stack 2
    def pop2(self):
        pass