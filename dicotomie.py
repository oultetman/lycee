xmini = -10
xmaxi = 10
m_d_g = "7*x + 2"
m_d_d =" 6*x - 5"
difference=10
while abs(difference) > 0.00001:
    x0 = (xmaxi+xmini)/2
    x=x0
    d = eval(m_d_g) - eval(m_d_d)
    x = xmini
    d0 = eval(m_d_g) - eval(m_d_d)
    x=xmaxi
    d1 = eval(m_d_g) - eval(m_d_d)
    if d*d1<0:
        xmini = x0
        difference = (d+d1)/2
        print((x0+xmaxi)/2, difference)
    else:
        xmaxi = x0
        difference = (d+d0)/2
        print((x0+xmini)/2, difference)
