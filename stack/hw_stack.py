from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def isEmpty(self):
        return not self.stack

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return None
        item = self.stack.pop()
        return item

    def peek(self):
        if not self.stack:
            return None
        item = self.stack[-1]
        return item


def pairs(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


def is_brackets_balanced(brackets_string):
    my_stack = Stack()
    balanced = True
    i = 0
    while i < len(brackets_string) and balanced:
        symbol = brackets_string[i]
        if symbol in '([{':
            my_stack.push(symbol)
        else:
            if my_stack.isEmpty():
                balanced = False
            else:
                top = my_stack.pop()
                if not pairs(top, symbol):
                    balanced = False
        i += 1
    if balanced and my_stack.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    '''
    my_stack = Stack()
    print('пустой', my_stack.isEmpty())
    print('размер', my_stack.size())
    print('верхний', my_stack.peek())
    my_stack.push('a')
    my_stack.push('b')
    my_stack.push('c')
    print(my_stack.stack)
    print('пустой', my_stack.isEmpty())
    print('размер', my_stack.size())
    print('верхний', my_stack.peek())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print('верхний', my_stack.peek())
    '''

    print(is_brackets_balanced('(((([{}]))))'))
    print(is_brackets_balanced('}{}'))
