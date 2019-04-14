def binaryCheck(checknum):
    for val in str(checknum):
        if int(val) > 1:
            raise TypeError(f' Input "{checknum}" not in binary')
def booltobin(boolval):
    if type(boolval) != bool:
        raise TypeError(f'Input "{boolval}" is not a boolean')
    if boolval == True:
        return(1)
    elif boolval == False:
        return(0)
def convertDeci(inputbin):
    global gatesstr, gatesopen, twocheck
    binaryCheck(inputbin)
    #variable asignment
    innum = 0
    gatesopen = 0
    gatesstr = '0'
    twocheck = True
    output = 1
    decimal = 0

    #input
    listnorm = []
    for num in str(inputbin):
        listnorm.append(int(num))
    listnorm = tuple(listnorm)
    numin = len(listnorm)
    listnot = []
    for val in listnorm:
        listnot.append(booltobin(not(val)))
    listnot = tuple(listnot)

    #check gates
    def gatecheck():
        global gatesstr, gatesopen, twocheck
        gatesstr = str(gatesopen)
        while len(gatesstr) < numin:
            gatesstr= '0'+gatesstr
        gateslist = list(gatesstr)
        while twocheck:
            try:
                twoind= gateslist.index('2')
                gateslist[twoind] = '0'
                gateslist[twoind-1] = str(int(gateslist[twoind-1])+1)
            except ValueError:
                twocheck=False
        twocheck = True
        gatesstr = ''.join(gateslist)
        gatesopen = int(gatesstr)

    #initializing gates
    gatecheck()

    #main
    while len(gatesstr) <= numin:
        output = 1
        for innum in range(numin):
            if int(gatesstr[innum]):
                listused = listnorm[innum]
            else:
                listused = listnot[innum]
            output = output and listused
        if output == 1:
            del gatesstr, gatesopen, twocheck
            return(decimal)
        decimal += 1
        gatesopen += 1
        gatecheck()

def add(binaddend1, binaddend2, carryin = 0):
    binaryCheck(binaddend1)
    binaryCheck(binaddend2)
    output = []
    cout = 0
    binlist = [int(binaddend1),int(binaddend2)]
    binlist.sort(reverse = True)
    binlist = tuple(binlist)
    while len(str(binaddend1)) <= len(str(binlist[0])):
        binaddend1 = "0" + str(binaddend1)
    while len(str(binaddend2)) <= len(str(binlist[0])):
        binaddend2 = "0" + str(binaddend2)
    for num in range(1,len(binaddend1)+1):
        if num == 1:
            c = carryin
        else:
            c = cout
        a = int(binaddend1[-num])
        b = int(binaddend2[-num])
        output.append(booltobin(((a != b) != c)))
        cout = (a and b) or (c and (a != b))
    output = ''.join(output[::-1])
    while (output[0] == '0') and (len(output) != 1):
        output = output[1:]
    return(output)
def subtract(minuend, subtrahend, borrowin=0):
    binaryCheck(minuend)
    binaryCheck(subtrahend)
    output = []
    bout = 0
    binlist = [int(minuend),int(subtrahend)]
    binlist.sort(reverse = True)
    binlist = tuple(binlist)
    while len(str(minuend)) <= len(str(binlist[0])):
        minuend = "0" + str(minuend)
    while len(str(subtrahend)) <= len(str(binlist[0])):
        subtrahend = "0" + str(subtrahend)
    for num in range(1,len(minuend)+1):
        if num == 1:
            borrow  = borrowin
        else:
            borrow = bout
        a = int(minuend[-num])
        b = int(subtrahend[-num])
        output.append(booltobin(((a != b) != borrow)))
        bout = (not(a) and b) or (borrow and not(a != b))
    output = ''.join(output[::-1])
    while (output[0] == '0') and (len(output) != 1):
        output = output[1:]
    return(output)
def divide(dividend, divisor):
    binaryCheck(dividend)
    binaryCheck(divisor)
    quotient = 0
    while int(dividend) >= int(divisor):
        dividend = subtract(dividend, divisor)
        quotient = add(quotient, 1)
    else:
        return((quotient, dividend))
def multiply(factor1, factor2):
    binaryCheck(factor1)
    binaryCheck(factor2)
    out = []
    check = 0
    while check != factor2:
        out.append(factor1)
    while len(out) != 1:
        out[0] = add(out[0],out[1])
        del out[1]
    return(out[0])
def convertBin(decinum):
    output = []
    try:
        int(decinum)
    except ValueError:
        raise TypeError(f'Input "{decinum}" is not a number')
    while decinum != 0:
        output.append(str(decinum % 2))
        decinum= decinum // 2
    output = ''.join(output[::-1])
    return(output)