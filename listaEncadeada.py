class Node:

    def __init__(self, label) -> None:
        self.label = label
        self.next = None
        
    def getLabel(self):
        return self.label
    
    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next


class LinkedList:

    def __init__(self) -> None:
        self.first: Node = None
        self.last: Node = None
        self.len: int = 0

    def isEmpty(self):
        if self.len > 0:
            return False
        return True

    def push(self, label, index = 'end'):
        if not index == 'end':
            if index < 0:
                raise ValueError('Index must be positive')

        #Criando node
        node = Node(label)

        #Verifica se está vazia
        if self.isEmpty():
            self.first = node
            self.last = node

        elif index == 0:
            #inseção no inicio
            node.setNext(self.first)
            self.first(node)


        elif index == 'end':
            #inserção no fim
            self.last.setNext(node)
            self.last = node

        elif index >= self.len:
            #inserção no fim
            self.last.setNext(node)
            self.last = node

        else:
            #insersão no meio
            prev_node: Node = self.first
            curr_node: Node = self.first.getNext()
            curr_index: int = 1

            while curr_index != None:

                if curr_index == index:
                    #setar curr_node como próximo do nó
                    node.setNext(curr_node)
                    prev_node.setNext(node)
                    break
                
                prev_node = curr_node
                curr_node = curr_node.getNext()
                curr_index += 1
        self.len += 1
                
    def pop(self, index = 'end'):

        if self.isEmpty():
            #Gera erro se a lista estiver vazia
            raise IndexError('Linked List is empty')
        
        if not index == 'end':
            if index < 0:
                raise IndexError('Index must be positive')
            
        if not index == 'end':
            if index >= self.len:
                raise IndexError("Index must be smaller than the Linked List's length")
            
        flag_remove = False

        if index == 'end':
            self.pop(index = self.len -1)
            flag_remove = True
            return

        if self.first.getNext() == None:
            #possui apenas um elemento
            self.first = None
            self.last = None
            flag_remove = True

        elif index == 0:
            #remove do inicio
            self.first = self.first.getNext()
            flag_remove = True

        else:
            #A lista possui mais de um elemento e não foi removido do inicio
            prev_node: Node = self.first
            curr_node: Node = self.first.getNext()
            curr_index = 1

            while curr_node != None:
                
                if index == curr_index:
                    #O proximo do anterior deve apontar para o proximo do curr
                    prev_node.setNext(curr_node.getNext())
                    curr_node.setNext(None)
                    flag_remove = True
                    break
            
                prev_node = curr_node
                curr_node = curr_node.getNext()
                curr_index += 1
            
        if flag_remove:
            self.len -= 1
    
    def length(self):
        return self.len
    
    def show(self):
        curr_node = self.first

        while curr_node != None:
            print(curr_node.getLabel(), end = ' ')
            curr_node = curr_node.getNext()
        print('')

if __name__ == '__main__':
    lista = LinkedList()

    print(lista.isEmpty())

    lista.push('marcos')
    lista.push('andré')
    lista.push('wanderley', 1)

    lista.show()
    print(lista.length())

    print(lista.isEmpty())

    lista.pop(1)
    lista.show()
    lista.pop()
    lista.show()