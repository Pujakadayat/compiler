import re

n = 1
y = []

ops = ["+", "-", "*", "/"]

expr = input("Enter an expression: ")

# split value
m = re.split("([+-/*])", expr)


def addressCode(m, n):
    """Takes the first two terms, which get assigned to a variable "t1"
     This creates a reusable expression, but will not change the original assignment"""
    for word in m:
        if word in ops:
            # essentially works as a stack
            y.append("".join(m[0:3]))
            m.pop(0)
            m.pop(0)
            m[0] = "t" + str(n)
            n += 1
    return m, n


# if there is more than one term
while len(m) > 1:
    # pass in m: the split value
    # pass in n: which starts at 1
    m, n = addressCode(m, n)
k = len(y)
# reverse so we can see how operation was built up to tn from t1
y.reverse()

for i in range(0, len(y)):
    print("t" + str(k) + "=" + y[i])
    k -= 1
