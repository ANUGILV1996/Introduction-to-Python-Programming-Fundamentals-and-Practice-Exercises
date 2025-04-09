# Lambda Function.

# Problem 1: Using Normal Function.
def addition(a):
    return a + 10
print(addition(5))

# Problem 2: Using Lambda Function.
q = lambda a: a + 10
print(q(5))

# Problem 3.
r = lambda a, b, c, d: a + b + c * d + a
print(r(2, 8, 9, 6))


# Problem 4.
def sample(x):
    return lambda a: a + x
ans = sample(2)
print(ans(5))
ans_1 = sample(7)
print(ans_1(7))

# End of Code.