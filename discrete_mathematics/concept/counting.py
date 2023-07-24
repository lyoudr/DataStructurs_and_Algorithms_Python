### Permutations

# ALGORITHM 1 Generating the Next Permutation 排列 in Lexicographic Order.
"""
    1. Find the integers aj and aj+1 with aj < aj+1, and aj+1 > aj+2 > ... an, that is, the last pair of adjacent integers in the permutation where the first integer in the pair is smaller than the second 
"""
def next_permutation(set_a: list):
    j = len(set_a) - 2
    
    # find the last pair where aj < aj+1
    while set_a[j] > set_a[j+1]:
        j -= 1
    
    # find the least integer among aj+1,aj+2,..., and an that is greater than aj
    k = len(set_a) - 1
    while set_a[j] > set_a[k]:
        k -= 1   # ak is the smallest integer greater than aj to the right of aj
    
    # interchange aj and ak
    set_a[j], set_a[k] = set_a[k], set_a[j]

    # arrange the rest element to the right of aj in increasing order
    r = len(set_a) - 1
    s = j+1
    while r > s:
        # interchange as and ar
        set_a[s], set_a[r] = set_a[r], set_a[s]
        r -= 1
        s += 1
    
    return set_a
    
# ALGORITHM 2 Generating the Next Larger Bit String
def next_bit_string(bit_str: str):
    bit_str = list(bit_str)
    i = len(bit_str)-1
    while bit_str[i] == '1' and i >= 0:
        bit_str[i] = '0'
        i -= 1
    bit_str[i] = '1'
    return ''.join(bit_str)


# ALGORITHM 3 Generating the Next r-Combination in Lexicographic Order
"""
    1.locate the last element ai in the sequence such that ai != n - r + i.
    2. replace ai with ai + 1
    3. replace aj with ai + j - i + 1, for j = i+1, i+2, ..., r
""" 
# C(6, 4): 
    # n = 6, {1, 2, 3, 4, 5, 6}
    # r = 4, set_a = {1, 3, 4, 5}
def next_r_combination(n: int, set_a: set) -> set: # set_a = {a1, a2, ..., ar}: proper subset of {1, 2, ..., n} not equal {n-r+1, ..., n} with a1 < a2 < ... < ar
    set_a = list(set_a)
    r = len(set_a) - 1
    i = r
    while set_a[i] == n - r + i:
        i = i - 1
    set_a[i] += 1
    for j in range(i+1, r+1):
        set_a[j] = set_a[i] + j - i
    return set(set_a)

