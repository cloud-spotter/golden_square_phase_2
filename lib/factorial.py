# File: lib/factorial.py
# Trying out the Python interactive Debugger in VS Code!

def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
        # Code railing with lines this way round:
        # n -= 1
        # product *= n
    return product

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 24