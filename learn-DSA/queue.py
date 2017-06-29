class Queue(object):
    ```
    列表list的队列实现
    ```

    def __init__(self, size):
        self.queue = []
        self.front = -1
        self.end = -1
        self.size = size

    def is_empty(self):
        return self.end == self.front

    def is_full(self):
        return self.end - self.front + 1 == self.size

    def push(self, element):
        if self.is_full():
            raise exception('QueueIsFull！')
        else:
            self.queue.append(element)
            self.end += 1

    def pop(self):
        if self.is_empty():
            raise exception('QueueIsEmpty！')
        else:
            self.queue.pop(0)
            self.front = self.front + 1
