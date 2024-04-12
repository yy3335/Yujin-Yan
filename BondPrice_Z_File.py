def getBondPrice_Z(face, couponRate, times, yc):
    pmt = face * couponRate
    bondPrice = 0
    for t, ytm in zip(times, yc):
        pv = pmt / ((1 + ytm) ** t)
        bondPrice += pv
    pvcf = face / ((1 + yc[-1]) ** times[-1])
    bondPrice += pvcf
    
    return bondPrice