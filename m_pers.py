
# get a number. multiply each digit together. repeat with the product.

# counter = 1


def m_pers(n, step):
    x = 1
    for i in range(len(str(n))):
        x *= int(str(n)[i-1])
    print(str(step) + ": " + str(x))
    s = step
    if len(str(x)) > 1:
        # counter += 1
        s = m_pers(x, step + 1)
    else:
        print("Total Steps = " + str(step))
    return s


'''
# try a single number
val = 1
while int(val)>0:
    val = input("enter number")
    print("starting conprutations")
    print("0: " + str(val))
    m_pers(val, 1)
    val = input("1 to continue, 0 to quit")
'''


# try a range of numbers
max = input("upper bound?: ")
min = input("lower bound?: ")
max_steps = 1
max_val = 1

for i in range(int(min), int(max) + 1):
    print("0: " + str(i))
    n = m_pers(i, 1)
    if n > max_steps:
        max_steps = n
        max_val = i

print("max steps = " + str(max_steps))
print("number = " + str(max_val))
