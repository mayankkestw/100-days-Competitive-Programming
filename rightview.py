# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def showRight(root, level, res):
    if(root==None):
        return
    
    
    res[level] = root.data
    
    showRight(root.left, level+1, res)
    showRight(root.right, level+1, res)

def rightView(root):
    '''
    :param root: root of given tree.
    :return: the right view of tree,
    '''
    # code here
    level = 1
    
    res = {}
    
    showRight(root, level, res)
    
    return list(res.values())

