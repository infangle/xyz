class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Use a separate stack to keep track of minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Example usage:
# obj = MinStack()
# obj.push(3)
# obj.push(5)
# obj.push(2)
# obj.pop()
# print(obj.top())  # Output: 5
# print(obj.getMin())  # Output: 3
