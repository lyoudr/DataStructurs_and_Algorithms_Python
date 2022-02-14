from string import ascii_uppercase
import math

### Cryptology
# Alphabet table
def alp_num():
    al_num = dict()
    num_al = dict()
    k = 0
    for c in ascii_uppercase:
        al_num[c] = k
        num_al[str(k)] = c
        k += 1
    return al_num, num_al

# encryption
def encrypt(n):
    return (n + 3) % 26

# Caesar encryption
def caesar_encrypt(in_str: str) -> str:
    al_num, num_al = alp_num()
    out_str = ''
    for c in in_str:
        num = al_num.get(c)
        en_num = encrypt(num)
        out_str += num_al.get(str(en_num))
    return out_str

# Base b expansion
def base_b_expansion(n: int, b: int):
    ans = ''
    q = n
    while q != 0:
        a = q % b                    # a is reminder
        ans += str(a)
        q = math.floor(q/b)          # q is quotient
    return ans[::-1]


# from binary expansion to ten expansion
def binary_to_ten_expansion(n: int):
    """
        Ex:
            input:  101011111
            output: 351
    """
    ans = 0
    for index, i in enumerate(str(n)[::-1]):
        ans += int(i) * math.pow(2, index)
    return ans

# binary integer addition
def add(a: int, b: int) -> int:
    a = str(a)[::-1]
    b = str(b)[::-1]
    c = 0
    sum = ''
    for i in range(0, max(len(a), len(b))):
        bi_a = int(a[i]) if i <= len(str(a))-1 else 0
        bi_b = int(b[i]) if i <= len(str(b))-1 else 0

        d = math.floor((bi_a + bi_b + c)/2)
        s = bi_a + bi_b + c - 2*d
        sum += str(s)
        c = d
    sum += str(c)
    return int(sum[::-1])

# binary integer multiple
def multiple(a: int, b: int) -> int:
    a = str(a)
    b = str(b)[::-1]
    c_list = []
    for i in range(0, len(b)):
        if int(b[i]) == 1:
            c_list.append(a + '0'*i)
        else:
            c_list.append('0'* (len(a)+i))
    print('c_list is =>', c_list)
    p = 0
    for c in c_list:
        p = add(p, c)
        print('p is =>', p)
    return p


def division(a: int, d: int):
    q = 0
    r = abs(a)
    while r >= d:
        r -= d
        q += 1
    if a < 0 and r > 0:
        r = d - r
        q = -(q+1)
    return (q, r)


def euclid(a: int, b: int):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x



## Matrix
class Matrix:
    def __init__(self, a, b) -> None:
        self._A = a
        self._B = b
        self._m = len(a)
        self._n = len(b[0])
        self._k = len(b)
    
    def make_matrix(self, action):
        matrix = []
        c_ij = []
        for i in range(0, self._m):
            for j in range(0, self._n):
                c = 0
                for q in range(0, self._k):
                    if action == 'multiple':
                        c = self._multiple(c, i, q, j)
                    if action == 'boolean':
                        c = self._boolean(c, i, q, j)
                c_ij.append(c)
            matrix.append(c_ij)
            c_ij = []
        return matrix
    
    def join(self):
        matrix = []
        c_ij = []
        for i in range(0, self._m):
            for j in range(0, self._n):
                c = self._A[i][j] or self._B[i][j] 
                c_ij.append(c)
            matrix.append(c_ij)
            c_ij = []
        return matrix

    def meet(self):
        matrix = []
        c_ij = []
        for i in range(0, self._m):
            for j in range(0, self._n):
                c = self._A[i][j] and self._B[i][j] 
                c_ij.append(c)
            matrix.append(c_ij)
            c_ij = []
        return matrix

    # two matrix A, B multiple, time complexity is n3
    def _multiple(self, c, i, q, j):
        return c + (self._A[i][q] * self._B[q][j])

    # two matrix A, B multiple, time complexity is n3
    def _boolean(self, c, i, q, j):
        return c or (self._A[i][q] and self._B[q][j])
