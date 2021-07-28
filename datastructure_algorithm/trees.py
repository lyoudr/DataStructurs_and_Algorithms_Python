# It is not always clear what productivity experts mean by "nonlinear" thinking.
# But when we say that trees are "nonlinear", we are refereing to an organizational relationship that is richer than the simple
# "before" and "after" relationship between objects in sequence

# The relationship in a tree are "hierarchical", with some objects being "above" and some "below" others
# Actually, the main terminology for tree data structures comes from family trees 
# In Figure 8.3, we revisit an earlier example.
# We see that the internal nodes of the tree are associated with directories and the leaves are associated with regular files.

# In the UNIX and Linux operating system, the root of the tree is appropriately called the "root directory", and is represented by the symbol "/."

# Example 8.2 : The inheritance relation between classes in a Python program forms a tree when 

# 8.1.2 The Tree Abstract Data Type

# position
# p.element(): Return the element stored at position "p"

# The tree ADT then supports the following "accessor methods", allowing a user to navigate the various positions of a tree.

# T.root(): Return the position of the root of tree T, or None if T is empty.
# T.is_root(p): Return True if position "p" is the root of Tree T.
# T.parent(p): Return the position of the parent of position p, or None if p is the root of T.
# T.num_children(p): Return the number of children of position "p".
# T.children(p): Generate an iteration of the children of position p.
# T.is_leaf(p): Return True if position p does not have any children.
# len(T): Return the nummber of positions (and hence elements) that are contained in tree T.
# T.is_empty(): Return True if tree T does not contain any positions.
# T.positions(): Generate an iteration of all positions of tree T.
# iter(T): Generate an iteration of all elements stored within tree T.


# from linked_list import LinkedQueue

# abstract base class
class Tree:
    '''Abstract base class representing a tree structure.'''
    
    # -------------------------------- nested Position class ----------------------------------
    class Position:
        '''An abstraction representing the location of a single element'''
        def element(self):
            '''Return the element stored at this Position.'''
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            '''Return True if other Position represents the same location'''
            raise NotImplementedError('must be implemented by subclass')
        
        def __ne__(self, other):
            '''Return True if other does not represent the same location.'''
            return not(self == other)      # opposite of __eq__

    # ------------- abstract methods that concrete subclass must support ----------------------
    def root(self):
        '''Return Position representing the tree's root (or None if empty).'''
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        '''Return Position representing p's parent (or None if p is root).'''
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        '''Return the number of children that Position p has.'''
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self, p):
        '''Generate an iteration of Positions representing p's children'''
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        '''Return the total number of elements in the tree.'''
        raise NotImplementedError('must be implemented by subclass')
    
    # ------------- concrete methods implemented in this class -----------------------------------
    def is_root(self, p):
        '''Return True if Position p represents the root of the tree.'''
        return self.root() == p
    
    def is_leaf(self, p):
        '''Return True if Position p does not have any children'''
        return self.num_children(p) == 0
    
    def is_empty(self):
        '''Return True if the tree is empty'''
        return len(self) == 0
    
    def depth(self, p): # The "depth" of p is the number of ancestors of p, excluding p itself.
        '''Return the number of levels separating Position p from the root.'''
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    

    def _height1(self): # O(n2) worst-case time
        '''Return the height of the tree'''
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    

    def _height2(self, p): # O(n) worst-case time
        '''Return the height of the subtree rooted at Position p.'''
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        '''Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree.
        '''
        if p is None:
            p = self.root()
        return self._height2(p)        # start _height2 recursion

    def __iter__(self):
        '''Generate an iteration of the tree's elements.'''
        for p in self.positions():     # use same order as positions()
            yield p.element()          # but yield each element

    # Preorder 前序遍歷
    def preorder(self): # 根節點 => 左子節點 => 右子節點
        '''Generate a preorder iteration of positions in the tree.'''
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):     # start recursion
                yield p


    def _subtree_preorder(self, p):
        '''Generate a preorder iteration of positons in subtree rooted at p.'''
        yield p                                         # visit p before its subtrees
        for c in self.children(p):                      # for each child c
            for other in self._subtree_preorder(c):     # do preorder of c's subtree
                yield other


    # Postorder 後序遍歷
    def postorder(self): # 左子節點 => 右子節點 => 根節點
        '''Generate a postorder iteration of positions in the tree.'''
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p

    def _subtree_postorder(self, p):
        '''Generate a postorder iteration of positions in subtree rooted at p'''
        for c in self.children(p):                     # for each child c
            for other in self._subtree_postorder(c):   # do postorder of c's subtree
                yield other
        yield p                                        # visit p after its subtrees


    def positions(self , type):
        '''Generate an iteration of the tree's positions.'''
        if type == 'preorder':
            return self.preorder()
        
        if type == 'postorder':
            return self.postorder()
        
        if type == 'inorder':
            return self.inorder()


# Such binary trees are known as "decision trees" 決策樹
# Recursive Binary Tree Definition
# 8.2.1 The Binary Tree Abstract Data Type
# As an abstract data type, a binary tree is a specialization of a tree that supports three additional accessor methods

# T.left(p) : Return the position that represents the left child of p, or None if p has no left child.
# T.right(p) : Return the position that represents the right child of p, or None if p has no right child.
# T.sibling(p) : Return the position that represents the sibling of p, ro None if p has no sibling.

class BinaryTree(Tree):
    '''Abstract base class representing a binary tree structure.'''

    # -------------------------- additional abstract methods -----------------------------
    def left(self, p):
        '''Return a Position representing p's left child.
        Return None if p does not have a left child.
        '''
        raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
        '''Return a Position representing p's right child.
        Return None if p does not have a right child.
        '''
        raise NotImplementedError('must be implemented by subclass')
    
    # --------------------------- concrete methods implemented in this class -----------------
    def sibling(self, p):
        '''Return a Position representing p's sibling (or None if no sibling).'''
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)             # possibly None
            else:
                return self.left(parent)              # possibly None
    
    def children(self, p):
        '''Generate an iteration of Positions representing p's children.'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # Inorder 中序遍歷
    def inorder(self):
        '''Generate an inorder iteration of positions in the tree.'''
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p


    def _subtree_inorder(self, p):
        '''Generate an inorder iteration of positions in subtree rooted at p.'''
        if self.left(p) is not None:                   # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                                        # visit p between its subtrees
        if self.right(p) is not None:                  # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

# 8.3 Implementing Trees
# LinkedBinaryTree
# T.add_root(e) : Create a root for an empty tree, storing e as the element, and return the position of that root; an error occurs if the tree is not empty
# T.add_left(p, e) : Create
class LinkedBinaryTree(BinaryTree):
    '''Linked representation of a binary tree structure.'''

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    class Position(BinaryTree.Position):
        '''An abstraction representing the location of a single element.'''

        def __init__(self, container, node):
            '''Constructure should not be invoked by user.'''
            self._container = container
            self._node = node
        
        def element(self):
            '''Return the element stored at this Position.'''
            return self._node._element
        

        def __eq__(self, other):
            '''Return True if other is a Position representing the same location.'''
            return type(other) is type(self) and other._node is self._node
        

    def _validate(self, p):
        '''Return associated node, if postion is valid.'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')

        return p._node
    

    def _make_position(self, node):
        '''Return Position instance for given node (or None if node).'''
        return self.Position(self, node) if node is not None else None
    
    # -------------------------- binary tree constructor ---------------
    def __init__(self):
        '''Create an initially empmty binary tree'''
        self._root = None
        self._size = 0
    
    # -------------------------- public accessors -----------------------
    def __len__(self):
        '''Return the total number of elements in the tree.'''
        return self._size
    
    def root(self):
        '''Return the root Position of the tree (or None if tree is empty).'''
        return self._make_position(self._root)

    def parent(self, p):
        '''Return the Position of p's parent (or None if p is root).'''
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        '''Return the Position of p's left child (or None if no left child).'''
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        '''Return the Position of p's right child (or None if no right child).'''
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        '''Return the number of children of Position p'''
        node = self._validate(p)
        count = 0
        if node._left is not None:   # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count


    def _add_root(self, e):
        '''
            Place element at the root of an empty tree and return new Postion.
            Raise ValueError if tree noneempty
        '''
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        '''
            Create a new left child for Position p, storing element e.
            Return the Position of new node.
            Raise ValueError if Position p is invalid or p already has a left child.
        '''
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
    

    def _add_right(self, p, e):
        '''
            Create a new right child for Position p, storing element e.
            Return the Position of new node.
            Raise ValueError if Position p is invalid or p already has a right child.
        '''
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        '''Replace the element at position p with e, and return old element.'''
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    
    def _delete(self, p): # O(1) time
        '''Delete the node at Position p, and replace it with its child, if any.
        
        Return the element that had been stored at Position p
        Raise ValueError if Position p is invalid or p has two children
        '''
        node = self._validate(p)
        if self.num_children(p) == 2: 
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node                 # convention for decprecated node
        return node._element
    
    def _attach(self, p, t1, t2):
        '''Attach trees t1 and t2 as left and right subtrees of external p'''
        node = self._validate(p)

        if not self.is_leaf(p): 
            raise ValueError('position must be leaf.')
        if not type(self) is type(t1) is type(t2): # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None                   # set t1 instance to empty
            t1._size = 0
        
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None                   # set t2 instance to empty
            t2._size = 0
    

# 8.3.3 Linked Structure for General Trees
# When representing a binary tree 
# For a general tree, there is no a priori limit on the number of children that a node may have.

# 8.4 Tree Traversal Algorithms
# A traversal of a tree "T" is a systematic way of accessng, or "visiting"
# In this section, we describe several common traversal schemes, implement them in the context of our various tree classes, and discuss several common applications of
# then the subtrees are traversed according to the order of the 
# The pseudo-code for the preorder traversal of the subtree rooted 

# 8.4.1
# 1. Preorder Traversal
# Algorithm preorder(T, p):
    # perform the "visit" action for position p
    # for each child c in T.children(p) do
        # preorder(T, c)


# 2. Postorder Traversal => it recursively traverses the subtrees rooted at the children of the root first, and then visit the root (hence, the name "postorder")
# Algorithm postorder(T, p):
    # for each child c in T.children(p) do
        # postorder(T, c)
    # perform the "visit" action for position p

# 8.4.2 Breadth-First Tree Traversal 
# another common approach is to traverse a tree so that we visit all the positions at depth d before we visit the positions at depth d + 1.
# Such an algorithm is known as a "breadth-first traversal."
# The process is not recursive, since we are not traversing entire subtrees at once.
# We use a queue to produce a FIFO (i.e., first-in first-out) semantics for the order in which we visit nodes.


# Algorithm inorder(p):
    # if p has a left child lc then
        # inorder(lc)                {recursively traverse the left subtree of p}
    # perform the "visit" action for position p
    # if p has a right child rc then
        # inorder(rc)                {recursively traverse the right subtree of p}


# Binary Search Trees
# An important application of the inorder traversal algorithm arises when we store an ordered sequence of elements in a binary tree, defining the structure we call a binary search tree.
# Let S be a set whose unique elements have an order relation.
# We can use a binary search tree T for set S to find whether a given search value v is in S, 
# Note that the running time of searching in a binary search tree T is propotional to the height of T. 

# Recall from Proposition 8.8 that the height of a binary tree 
# T.positions(): Generate an iteration of all positions of tree T.
# iter(T): Generate an iteration of all elemenets stored within tree T.


### 8.4.5 Applications of Tree Traversals
# We would like to have a mechanism for children to return information to the parent as part of the traversal process.
# A custom solution to the disk space problem, with each level of recustion providing 


### 8.4.6 Euler Tours and the Template Method Pattern *
# The various applications described 
# Furthermore, in some contexts it was important to know the depth of a position, or the complete path from the root to that position, or to return information from one level of the recursion to another.
# For each of the previous 

# adaptability
# reusablility
# In this section, we develop a more general framework for implementing tree traversals based on a concept known as "Euler tour traversal"
# The Euler tour traversal of a general tree T can be informally defined as a "walk" around T, where we start by going from the root toward its leftmost child, viewing the edges of T as being "walls"
# A "pre visit" occurs when first reaching the position, that is, when the walk passes immediately left of the node in our visualization.
# A "post visit" occurs when the walk later proceeds upward from that position, that is, when the walk passes to the right of the node in our visualization.
# The process of an Euler tour can easily be viewed recursively.

# Algorithm eulertour(T, p):
    # perform the "pre visit" action for position p
    # for each child c in T.children(p) do
        # eulertour(T, c)                                   {recursively tour the subtree rooted at c}
    # perform the "post visit" action for position p

# To allow customization, the primary algorithmm calls auxiliary functions

class EulerTour:
    '''Abstract base class for performing Euler tour of a tree.
    
    _hook_previsit and _hook_postvisit may be overridden by subclasses.
    '''

    def __init__(self, tree):
        '''Prepare an Euler tour template for given tree.'''
        self._tree = tree
    

    def tree(self):
        '''Return reference to the tree being traversed.'''
        return self._tree
    

    def execute(self):
        '''Perform the tour and return any result from post visit of root.'''
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])  # start the recursion
    

    def _tour(self, p, d, path):
        '''Perform tour of subtree rooted at Position p
        p       Position of current node being visited
        d       depth of p in the tree
        path    list of indices of children on path from root to p
        '''
        self._hook_previsit(p, d, path)                     # "pre visit" p
        results = []
        path.append(0)                                      # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))        # recur on child's subtree
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)  # "post visit" p
        return answer
    
    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d path, results):
        pass