inv = 100
K = 0.055

returns = [130]


def NPV(investment, inflation, returns_list):

    out = -investment
    t = 0
    for r in returns_list:
        t += 1
        out += r/((1+inflation)**t)
    
    return out

NPV(inv,K,returns)
