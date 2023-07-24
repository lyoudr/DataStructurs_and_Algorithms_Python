### Program Verification
# 1. the correct answer is obtained if the program terminates
# 2. the program always terminates.

# initial assertion : p => gives the properties that the input values must have
# final assertion : q => gives the properties that the output of the program should have

"""
Definition 1
A prgram, or program segment, S is said to be partially correct with respect to the 
initial assertion p and the final assertion q if whenever p is true for the input values
of S and S terminates, then q is true for the ouput values of S
The notion p{S}q indeicates that the program, or program segment, S is partially correct to the initial assertion p and final assertion q
"""


### Rules of Inference
# Suppose that the program S is split into subprograms S1 and S2
# Write S = S1;S2
# S1 
    # initial assertion, p
    # final assertion, q
# S2
    # initial assertion, q
    # final assertion, r
# Below is the rule of composition
"""
    p{S1}q
    q{S2}r
    ----------
    p{S1;S2}r
"""

### Condition Statements
# Two things must be done to verify that this program is correct
# 1. when p is true and condition is also true, then q is true after S terminates
# 2. when p is true and condition is false, then q is true
"""
    if condition then
        S
"""
"""
    (p ∧ condition){S}q 
    (p ∧ ¬condition) → q
    -------------------------
    ∴ p{if condition then S}q.
"""


### Loop Invariants

# Example 1
# An assertion that remains true each time S is executed must be chosen.
# Such an assertion is called a "loop invariant"
# p is a loop invariant if (p ∧ condition){S}p is true.
"""
    while condition
        S
"""
"""
    (p ∧ condition){S}p
    ---------------------------------
    p{while condition S}(-condition ∧ p)
"""

# Example 2
"""
    i := 1
    factorial := 1
    while i < n
        i := i + 1
        factorial := factorial * i
"""
# initial assertion : factorial = i! and i <= n


# Example 3
"""
 
"""
# initail assertion (p): m and n are integers
    # p{S1}q is true
# q : p ∧ (a = |n|)
# r : q ∧ (k = 0) ∧ (x = 0)
    # q{S2}r is true
# r -> x = m * 0 and 0 <= a (before loop)
# s : x = ma and a = |n| (after loop)
    # r{S3}s is true
# t : product = mn
    # s{S4}t