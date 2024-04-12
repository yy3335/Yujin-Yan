def getBondPrice_E(face, couponRate, m, yc):
    pmt = face * couponRate
    bondPrice = 0
    for t, ytm in enumerate(yc, start=1):
        pv = pmt / ((1 + ytm) ** t)
        bondPrice += pv
        if t == m:
            pvcf = face / ((1 + ytm) ** t)
            bondPrice += pvcf
    return bondPrice