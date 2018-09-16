class Stack:
    """
                                                         _________________________   
                    /\\\\      _____          _____       |   |     |     |    | |  \\  
     ,-----,       /  \\\\____/__|__\_    ___/__|__\___   |___|_____|_____|____|_|___\\ 
  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    \\
 ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  
`````````````````````````````````````````````````````````````````````````````````````    
    """

    def __init__(self,i = None):
        self.items = [] if i == None else i

    def __str__(self):
        return 'stack: size= '+ str(self.size()) + ' =>> '+ str(self.items)

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

    def push(self,data):
        self.items.append(data)

    def peek(self):
        return self.items[-1]

s = Stack([i for i in range(10)])
print(s)
print(s.peek())
print(s.pop())
print(s)
s.push('Toyota Vios haha+')
print(s)