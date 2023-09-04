
def permCheck(code,panel):
    posInCode = panel
    posInCode2 = panel + 8
    bitmask = 1 << posInCode
    bitmask2 = 1 << posInCode2
    result = int(code) & bitmask
    result2 = int(code) & bitmask2
    if result == bitmask and result2 == bitmask2:
        print("Granted acces panel "+str(panel))
        return True
    else:
        return False