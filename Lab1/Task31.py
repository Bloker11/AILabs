def max_sum(a, b, c):
    if (a > b) and (a > c) and (b > c):
        return a + b
    elif (b > a) and (b > c) and (a > c):
        return b + a
    elif (b > a) and (b > c) and (c > a):
        return b + c
    elif (c > a) and (c > b) and (b > a):
        return b + c
    elif (a > b) and (a > c) and (c > b):
        return a + c
    elif (c > a) and (c > b) and (a > b):
        return a + c
    else:
        return "there are no greatest values"


print(max_sum(80, 40, 70))

list = [2, 5, 8, 6, 11, 10, 15]



def return_even(x):
    list2 = []
    for i in x:
        if i % 2 == 0:
            list2.append(i)
    return list2


print(return_even(list))

def trapezoid_area(a, b, h):
    return ((a+b)*h)/2

print(trapezoid_area(5,10,2))


def christmass(deco):
    print("     ^")
    print("    ^^^")
    print("   ^^^^"+deco+"^")
    print("  ^^^^^^^")
    print("   ^^^" + deco + "^^")
    print("  ^^^^^^^")
    print(" ^^^^"+ deco + "^^^^")
    print("    ###")

christmass("*")
christmass("o")
