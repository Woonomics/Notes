inv = 100
K = 0.055

returns = [130]


def NPV(investment, inflation, returns+):

    out = -inv
    t = 0
    for r in returns:
        t += 1
        out += r/((1+K)**t)
    
    return out

NPV()
