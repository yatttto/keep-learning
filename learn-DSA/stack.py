class Stack(object):
    ```
    模拟一个栈
    ```

    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.size = self.top + 1

    def push(self, element):
        if self.is_full():
            raise exception('StackOverFlow!')
        else:
            self.stack.append(element)
            self.top += 1

    def pop(self):
        if self.is_empty():
            raise exception('StackIsEmpty!')
        else:
            self.stack.pop()
            self.top -= 1
