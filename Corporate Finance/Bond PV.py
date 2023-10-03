coupon = 115
maturity = 1000
YTM = 0.1
time = 5

def PV(c, m, ytm, t):

    out = 0
    for r in range(t+1):
        if r == t+1:
            out += m/((1+ytm)**r)
        else:
            out += r/((1+ytm)**r)
    
    return out

PV(coupon, maturity, YTM, time)
