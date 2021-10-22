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
        # visit left node
        if self.left:
            elements+=self.left.in_order_traversal()

        # visit base node 
        elements+= self.data
        # visit right tree
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

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




def build_tree(elements):

    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root 


if __name__ =="__main__":
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(17))
