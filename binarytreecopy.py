class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

    
    def add_child(self,data):
        if data == self.data:
            return 
        
        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data) 
            else:
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            #add data in right subtree 
            if self.right:
                self.right.add_child(data) 
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

        # def in_order_traversal(self):

        #     elements = []
        #     # visit left node
        #     if self.left:
        #         elements+=self.left.in_order_traversal()

        #     # visit base node 
        #     elementsappend(self.data) 
        #     # visit right tree
        #     if self.right:
        #         elements+=self.right.in_order_traversal()

        #     return elements

    

    def pre_order_traversal(self):
        elements=[]
        #visit base node
        elements.append(self.data) 
        # visit left node 
        if self.left:
            elements+= self.left.pre_order_traversal()
        if self.right:
            elements+= self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements=[]

        # visit left node 
        if self.left:
            elements+= self.left.pre_order_traversal()
        if self.right:
            elements+= self.right.pre_order_traversal()
        #visit base node
        elements.append(self.data)

        return elements

    def sum_all_nodes(self):
        a=0
        if self.left:
            a = a+self.left.sum_all_nodes()
        if self.right:
            a = a+self.right.sum_all_nodes()
        a = a+self.data

        return a 



    def search(self,val):
        if self.data==val:
            return True

        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False


            #val might be in left sub tree 
        
        if val > self.data:
        
            if self.right:
                self.right.search(val)
            else:
                return False
            # val might be in right sub tree
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data
        
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.data 
    
    

    


def build_tree(elements):

    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root 


if __name__ =="__main__":
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.sum_all_nodes())