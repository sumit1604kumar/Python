def add(*arg):
    global total

    total =0
    for x in arg:
        total += x
    # print(f"{total}: Minutes")
    return total
add(123,41,11,3,41,69,44,48,31,35,19,64)

def second(*pa):
    global result
    count  = 0
    for y in pa:
        count += y
    result = round(count/60)
    # print(result)
    return result
second(0)

last = total + result
print(last)

#-----------------------------------------------------------------------------------------------------------------------------


