'''
Creator : Chaitanya Ramani
Email : chaitanyalramani@gmail.com
'''

class Stack():
    '''
    this is basically use of inbuilt method of list.
    ''' 
    def  __init__(self):
        self.item = []    
        
    def push(self,item):
         self.item.append(item)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def get_stack(self):
        return self.item

if __name__ == '__main__':
    s = Stack()
    s.push('A')
    print(s.get_stack())

