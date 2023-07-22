### ALGORITHM 4 The bubble sort
"""
procedure bubblesort(a1, ..., an: real numbers with n >= 2)
for i := 1 to n-1
    for j := 1 to n-i
        if aj > aj+1 then interchange aj and aj+1
"""

def bubblesort(S):
    for i in range(len(S)):
        for j in range(i, len(S)-i):
            if S[j] > S[j+1]:
                temp = S[j]
                S[j] = S[j+1]
                S[j+1] = temp 

