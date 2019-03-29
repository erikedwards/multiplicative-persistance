
# get a number. multiply each digit together. repeat with the product.

# counter = 1


def m_pers(n, step):
    x = 1
    for i in range(len(str(n))):
        x *= int(str(n)[i-1])
    print(str(step) + ": " + str(x))
    if len(str(x)) > 1:
        # counter += 1
        m_pers(x, step + 1)
    else:
        print("Total Steps = " + str(step))


val = 1
while int(val)>0:
    val = input("enter number")
    print("starting conprutations")
    print("0: " + str(val))
    m_pers(val, 1)
    val = input("1 to continue, 0 to quit")


