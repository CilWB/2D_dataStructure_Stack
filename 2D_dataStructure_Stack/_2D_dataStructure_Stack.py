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

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop() if self.size()!=0 else None

    def push(self,data):
        self.items.append(data)
        
    def peek(self):
        return self.items[-1] if not self.isEmpty() else None

class park:

    def __init__(self,k=None):
        self.ASoi = Stack([] if k==None else k)
        self.BSoi = Stack([])

    def arrive(self,data):
            if self.ASoi.size() >= 4 :
                print('car : '+str(data)+' cannot arrive: SOI FULL' )
            else:
                self.ASoi.push(data)
                print('car : '+str(data)+' arrived\t\tspace left '+str(4-self.ASoi.size()))
    def depart(self,data):
        if self.ASoi.isEmpty() :
            return 'car '+str(data)+' cannot depart: soi empty' 
        found = False
        s = 'car '+str(data)+' depart :\n\t'
        while not self.ASoi.isEmpty() :
            top = self.ASoi.pop()
            s += 'pop '+ str(top) + ', '
            if  top == data :
                found = True
                break
            self.BSoi.push(top)
        while not self.BSoi.isEmpty() :
            top = self.BSoi.pop()
            #if top != data :
            self.ASoi.push(top)
            s += 'push '+ str(top) + ('' if self.BSoi.isEmpty() else ', ')
        
        s+= '\n\tspace left '+str(4-self.ASoi.size())
        return s if found else ('car '+str(data)+' cannot depart : No car '+ str(data) ) 
            
    def __str__(self):
        return 'print soi = '+ str( self.ASoi.items )

if __name__ == "__main__":
    #######testing stack class
    #s = Stack([i for i in range(10)])
    #print(s)
    #print(s.peek())
    #print(s.pop())
    #print(s)
    #s.push('Toyota Vios haha+')
    #print(s)

    p = park()
    print(p.depart(6))
    for i in range(1,6):
        p.arrive(i)
    print(p)
    print(p.depart(7))
    print(p.depart(2))
    print(p)

    #### only 4 car can park in the narrow Road
    #print(Stack.__doc__)
 

