def binaryCheck(checknum):    # all done
    for val in str(checknum):
        if val != '-':
            val = int(val) > 1
            neg = False
        else:
            val = True
            neg = True
        if not(val) and neg:
            raise TypeError(f' Input "{checknum}" not in binary')

def booltobin(boolval):    #all done
    if type(boolval) != bool:
        raise TypeError(f'Input "{boolval}" is not a boolean')
    if boolval == True:
        return('1')
    elif boolval == False:
        return('0')

def convertDeci(inputbin, input_type = 'bin'):       #all done
    global gatesstr, gatesopen, twocheck
    binaryCheck(inputbin)
    #variable asignment
    if input_type in ['bin','binary']:
        inputbin = inputbin
    elif input_type in ['bcd','bcd']:
        inputbin = convertBin(inputbin, 'bcd')
    else:
        ValueError('Invalid input type')
    innum = 0
    gatesopen = 0
    gatesstr = '0'
    twocheck = True
    output = 1
    decimal = 0
    if int(inputbin) < 0:
        neg = '-'
        inputbin = str(abs(int(inputbin)))
    else:
        neg = ''

    #input
    listnorm = []
    for num in str(inputbin):
        listnorm.append(int(num))
    listnorm = tuple(listnorm)
    numin = len(listnorm)
    listnot = []
    for val in listnorm:
        listnot.append(int(booltobin(not(val))))
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
            return(neg + str(decimal))
        decimal += 1
        gatesopen += 1
        gatecheck()

def add(binaddend1, binaddend2, carryin = 0):     #all done
    binaryCheck(binaddend1)
    binaryCheck(binaddend2)

    if (int(binaddend1) >= 0) and (int(binaddend2) < 0):
        return(subtract(binaddend1, abs(int(binaddend2))))
    elif (int(binaddend1) < 0) and (int(binaddend2) < 0):
        return('-' + add(abs(binaddend1), abs(binaddend2)))
    elif (int(binaddend1) < 0) and (int(binaddend2) >= 0):
        return('-' + subtract(abs(binaddend1), binaddend2))

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

    return(str(output))

def subtract(minuend, subtrahend, borrowin=0):  #all done
    binaryCheck(minuend)
    binaryCheck(subtrahend)

    if (int(minuend) >= 0) and (int(subtrahend) < 0):
        return(add(minuend, abs(int(subtrahend))))
    elif (int(minuend) < 0) and (int(subtrahend) < 0):
        return('-' + subtract(abs(minuend), abs(subtrahend)))
    elif (int(minuend) < 0) and (int(subtrahend) >= 0):
        return('-' + add(abs(minuend), subtrahend))

    if int(minuend) < int(subtrahend):
        subtrahend1 = minuend
        minuend1 = subtrahend
        subtrahend = subtrahend1
        minuend = minuend1
        neg = '-'
    else:
        neg = ''
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
    return(neg + str(output))

def divide(dividend, divisor):                                   #all done
    binaryCheck(dividend)
    binaryCheck(divisor)
    if (int(dividend) < 0) and (int(divisor) < 0):
        neg = ''
        rneg = '-'
        divisor = abs(divisor)
        dividend = abs(dividend)
    elif (int(dividend) >= 0) and (int(divisor) < 0):
        neg = '-'
        rneg = ''
        divisor = abs(divisor)
        dividend = abs(dividend)
    elif (int(dividend) < 0) and (int(divisor) >= 0):
        neg = '-'
        rneg = '-'
        divisor = abs(divisor)
        dividend = abs(dividend)
    else:
        neg = ''
        rneg = ''
    if int(divisor) == 0:
        raise ZeroDivisionError('division by zero')
    quotient = 0
    while int(dividend) >= int(divisor):
        dividend = subtract(dividend, divisor)
        quotient = add(quotient, 1)
    else:
        return((str(int(neg + str(quotient))), str(int(rneg + str(dividend)))))

def multiply(factor1, factor2):             #all done
    binaryCheck(factor1)
    binaryCheck(factor2)
    if (int(factor1) < 0) and (int(factor2) < 0):
        neg = ''
        factor1 = abs(factor1)
        factor2 = abs(factor2)
    elif (int(factor1) >= 0) and (int(factor2) < 0):
        neg = '-'
        factor1 = abs(factor1)
        factor2 = abs(factor2)
    elif (int(factor1) < 0) and (int(factor2) >= 0):
        neg = '-'
        factor1 = abs(factor1)
        factor2 = abs(factor2)
    else:
        neg = ''
    out = []
    check = 0
    while int(check) != int(factor2):
        out.append(factor1)
        check = add(check, 1)
    while len(out) != 1:
        out[0] = add(out[0],out[1])
        del out[1]
    return(str(int(neg + str(out[0]))))

def convertBcd(num, input_type = 'decimal'):      #all done
    binnums = ('0000','0001','0010','0011','0100','0101','0110','0111','1000','1001')
    out = []
    if int(num) < 0:
        neg = '-'
    else:
        neg = ''
    if input_type.lower() in ['dec','decimal']:
        for digit in str(num):
            out.append(binnums[int(digit)])
        out[0] = neg + out[0]
        return(tuple(out))
    elif input_type.lower() in ['bin', 'binary']:
        while int(num) > 1010:
            num, rem = divide(num, 1010)
            while len(rem) != 4:
                rem = '0'+rem
            out.append(rem)
            if int(num) != 0 and int(num) < 1010:
                while len(num) != 4:
                    num = '0'+num
                out.append(num)
        out = out[::-1]
        out[0] = neg + out[0]
        return(tuple(out))
    else:
        raise ValueError('Invalid input type')

def convertBin(num, input_type = 'decimal'):  #needs neg and bcd implementation
    output = []
    if input_type.lower() in ['dec','decimal']:
        bcd = list(convertBcd(num))
    elif input_type.lower() == 'bcd':
        bcd = num
    else:
        raise ValueError('Invalid input type')
    while len(bcd) != 1:
        bcd[1]= add(multiply(bcd[0],1010), bcd[1])
        del bcd[0]
    output = ''.join(bcd)
    output = str(int(output))
    return(output)
