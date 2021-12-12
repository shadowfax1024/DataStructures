class BSTNode:
    def __init__(self,data):
        self.data = data
        self.right =None
        self.left  = None

    def add_child(self,data):
        if(self.data==data):
            print("Node Already Exists!")
            return
        if(self.data > data):
            if(self.left):
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if(self.right):
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)
    def inorder(self):
        items = []
        if(self.left):
            items += self.left.inorder()
        items.append(self.data)
        if(self.right):
            items += self.right.inorder()
        return items
    def preorder(self):
        items =[]
        items.append(self.data)
        if(self.left):
            items +=self.left.preorder()
        if(self.right):
            items +=self.right.preorder()
        return items

    def find_min(self):
        if(self.left):
            return self.left.find_min()
        else:
            return self.data
    def find_max(self):
        if(self.right):
            return self.right.find_max()
        else:
            return self.data

    def search(self,data):
        if(self.data== data):
            return True
        elif(self.data > data):
            if(self.left):
                return self.left.search(data)
            else:
                return False
        elif(self.data < data):
            if(self.right):
                return self.right.search(data)
            else:
                return False
    def delete(self,val):
        if( val< self.data):
            if(self.left):
                self.left = self.left.delete(val)
        elif(val > self.data):
            if(self.right):
                self.right = self.right.delete(val)
        else:
            if(self.right==None and self.left==None):  # this is for the leaf node
                return None
            elif(self.right==None):  # the node has 1 children
                return self.left
            elif(self.left==None):  # the node has 1 children
                return self.right
            else:  # the node to be deleted has 2 children   # implemented both methods!!! for deletion in  a node with 2 childrens!!
                min_val = self.right.find_min()
                print("minval on the right: ",min_val)
                #max_val = self.left.find_max()
                self.data = min_val # max_val
                self.right = self.right.delete(min_val)#self.right.delete(min_val)
        return self




if __name__ == "__main__":
    root = BSTNode(5)
    for i in range(10):
        root.add_child(i)
    #print(root,root.data,root.left,root.right)
    print(root.inorder())
    print(root.search(100),root.search(-100),root.search(8))
    print(root.find_min(),root.find_max())
    print(root.preorder())
    print(root.inorder())
    print("deleting 5")
    root.delete(5)
    print(root.inorder())
