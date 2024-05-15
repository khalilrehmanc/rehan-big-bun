class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


# Example usage:
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(10)

# Pop elements from the stack
print("Popped item:", stack.pop())  # Output: Popped item: 30
print("Popped item:", stack.pop())  # Output: Popped item: 20

# Check size and emptiness of the stack
print("Size of stack:", stack.size())  # Output: Size of stack: 1
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

# Pop remaining item
print("Popped item:", stack.pop())  # Output: Popped item: 10

# Trying to pop from an empty stack
print("Popped item:", stack.pop())  # Output: Stack is empty, Popped item: None
