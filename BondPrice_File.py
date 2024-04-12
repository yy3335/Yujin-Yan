
def getBondDuration(y, face, couponRate, m, ppy = 1):
    pmt = face * couponRate / ppy
    duration = 0
    pvsum = 0  
    for t in range(1, m*ppy  + 1):
        pv = pmt / ((1 + y/ppy) ** t)
        if t == m * ppy:
            pv += face / ((1 + y/ppy) ** t) 
        duration += t * pv
        pvsum += pv

    duration /= pvsum  
    duration /= ppy     
    return duration