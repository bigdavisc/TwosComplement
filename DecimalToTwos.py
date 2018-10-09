decimal = int(input("Number Please: "))
bitsNeeded = 1
raisedBase = 1
twosComp = []

if decimal < 0:

    decimal = decimal * -1
    while raisedBase-1 < decimal:

        raisedBase = raisedBase*2
        bitsNeeded += 1

    dividend = decimal
    for i in range(bitsNeeded):

        remainder = dividend % 2
        dividend = dividend // 2
        if remainder == 1:
            x = 0
        else:
            x = 1
        twosComp.insert(0, x)

    for i in range(bitsNeeded-1, -1, -1):

            if twosComp[i] == 1:
                twosComp[i] -= 1
            else:
                twosComp[i] += 1
                break
else:

    while raisedBase-1 < decimal:

        raisedBase = raisedBase*2
        bitsNeeded += 1
    dividend = decimal

    for i in range(bitsNeeded):

        remainder = dividend % 2
        dividend = dividend // 2
        twosComp.insert(0, remainder)

print("".join(map(str, twosComp)))