class Solution:
    def compute(self, a, b, operator):
        if operator == '+':
            return int(a + b)
        elif operator == "-":
            return int(a - b)
        elif operator == "*":
            return a * b
        return int(a / b)

    def is_operator(self, char):
        if char in ["+", "-", "*", "/"]:
            return True
        return False

    def perform_operation(self):
        """
            The trick of the question is we will recursively resolve the operators and then compute the operation result.
        """
        operation = self.stack.pop()
        b_val = 0
        a_val = 0

        if not self.is_operator(operation):
            return int(operation)

        if self.is_operator(self.stack[-1]):
            b_val = self.perform_operation()
        else:
            b = self.stack.pop()
            b_val = int(b)
        
        if self.is_operator(self.stack[-1]):
            a_val = self.perform_operation()
        else:
            a = self.stack.pop()
            a_val = int(a)
        
        return int(self.compute(a_val, b_val, operation))

    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = deque([])

        for i in tokens:
            self.stack.append(i)

        return self.perform_operation()
