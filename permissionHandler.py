

def addingPermCheck(code): 
    posInCode = 7   #7 bit, last in second byte
    posInCode2 = 3
    bitmask = 1 << posInCode
    bitmask2 = 1 << posInCode2
    result = int(code) & bitmask
    result2 = int(code) & bitmask2
    if result == bitmask and result2 == bitmask2:
        return True
    else:
        return False