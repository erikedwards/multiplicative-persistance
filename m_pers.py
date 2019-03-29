
# get a number. multiply each digit together. repeat with the product.

# counter = 1


def m_pers(n):
    x = 1
    for i in range(len(str(n))):
        x *= int(str(n)[i-1])
    print(str(x))
    if len(str(x)) > 1:
        # counter += 1
        m_pers(x)


val = 1

while int(val)>0:
    val = input("enter number")
    print("starting conprutations")
    print(str(val))
    steps = 1
    m_pers(val)
    # print(str(counter) + " steps")
    val = input("1 to continue, 0 to quit")
