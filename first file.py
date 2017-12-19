rounds = [1, 2, 3, 4, 5, 6, 7, 8]


def cross(change):
    crossed_change = [
        change[1], change[0],
        change[3], change[2],
        change[5], change[4],
        change[7], change[6]]
    return crossed_change


def do_18(change):
    crossed_change = [
        change[0], change[2],
        change[1], change[4],
        change[3], change[6],
        change[5], change[7]]
    return crossed_change


c_change = rounds
for i in range(10):
    print(c_change)
    c_change = cross(c_change)
    print(c_change)
    c_change = do_18(c_change)




exit()
for x in range(10):
    for y in range(1, 10):
        print(x, y, x + y)







exit()
total = 0
for x in range(10):
    if x % 2 == 1:
        total = total + x
    print(x, total)







exit()
for number in range(10):
    if number % 2 == 1:
        print(number)
    else:
        print(number, "was even")
print("it finished")
