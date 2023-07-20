# Computing the successor of a position in a binary search tree.
"""
Algorithm after(p):
    if right(p) is not None then 
        walk = right(p)
        while left(walk) is not None do
            walk = left(walk)
        return walk
    else
        walk = p
        ancestor = parent(walk)
        while ancestor is not None and walk == right(ancestor) do
            walk = ancestor
            ancestor = parent(walk)
        return ancestor
"""

# Recursive search in a binary search tree.
"""
Algorithm TreeSearch(T, p, k):
    if k == p.key() then
        return p                                            {successful search}
    else if k < p.key() and T.left(p) is not None then
        return TreeSearch(T, T.left(p), k)                  {recur on left subtree}
    else if k > p.key() and T.right(p) is not None then
        return TreeSearch(T, T.right(p), k)                 {recur on right subtree}
    return p                                                {unsuccessful search}
"""
# we spend O(1) time per position encountered in the search,
# the overall search runs in O(h)


# Algorithm for inserting a key-value pair into a map that is represented as a binary search tree
"""
Algorithm TreeInsert(T, k, v):
    Input: A search key k to be associated with value v
    p = TreeSearch(T, T.root(), k)
    if k == p.key() then
        Set p's value to v
    else if k < p.key() then
        add node with item (k, v) as left child of p
    else
        add node with item (k, v) as right child of p
"""


from map_dictionary import MapBase
from trees import LinkedBinaryTree

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""
    # ------------------------- override Position class -----------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map's key-value pair"""
            return self.element()._key
        
        def value(self):
            """Return value of map's key-value pair."""
            return self.element()._value
    
    # ------------------------ nonpublic utilities -------------------------
    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():                                                 # found match
            return p
        elif k < p.key():                                                # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:                                                            # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p
    
    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk
    
    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self._subtree_first_position(self.root() if len(self) > 0 else None)
    
    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self._subtree_last_position(self.root() if len(self) > 0 else None)
    
    def before(self, p):
        """Return the Position just before p in the natural order.
        
        Return None if p is the first position.
        """
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above
    
    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)                              # hook for balanced tree subclasses
            return p
        
    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())
    
    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k.
        
        Return None if there does not exist such a key
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
    
    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)
    
    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError('Key Error:' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()
    
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)
    
    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    
    def delete(self, p):
        """Remove the item at given Position."""
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))        # find the left subtree of p, and find the largest node in this left subtree, that way, this node's value will be greater than any left subtree and smaller than any right subtree
            self._replace(p, replacement.element())
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)
    
    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError('Key Error ' + repr(k))
    
    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_access(self, p):
        pass

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)."""
        if make_left_child:                    # make it a left child
            parent._left = child
        else:                                  # make it a right child
            parent._right = child 
        if child is not None:                  # make child point to parent
            child._parent = parent 
    
    def _rotate(self, p):
        """Rotate Position p above its parent."""
        x = p._node
        y = x._parent                          # we assume this exists
        z = y._parent                          # grandparent (possibly None)
        if z is None:
            self._root = x                     # x becomes root
            x._parent = None
        else:
            self._relink(z, x, y == z._left)   # x becomes a direct child of z
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True)    # x._right becomes left child of y
            self._relink(x, y, False)          # y becomes right child of x
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)
    
    def _restructure(self, x):
        """Perfoem trinode restructure of Position x with parent/grandparent."""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):          # matching alignments
            self._rotate(y)                                       # single rotation (of y)
            return y                                              # y is new subtree root
        else:                                                     # opposite alignments
            self._rotate(x)                                       # double rotation (of x)      
            self._rotate(x)
            return x                                              # x is new subtree root