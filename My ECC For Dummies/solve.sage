#!/usr/bin/env sage

from Crypto.Util.number import long_to_bytes as lb

p = 6277101735386680763835789423207666416083908700390324961279
ID = 3243154082094975110425161650374039692150707098951074985457
c1 = 273313854985749705692360311202040937037213239294441646642
c2 = 6076257418068540152032600239285650920642292327792130060609
a = 6277101735386680763835789423207666416083908700390324961276
b = 2455155546008943817740293915197451784769108058161191238065

m2 = None

def legendre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def square_root(a, p):
    #Tonelli–Shanks algorithm
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

def solve (ID, e):
    global m2
    if e == 1:
        if lb(ID)[-1:] == b"}":
            m2 = ID

    else:
        r1 = square_root(ID, p)
        solve(r1, e // 2)
        r2 = p - r1
        solve(r2, e // 2)

    return m2

def flag():
    for i in range(1,65):
        print(f"[{i}] Processing..")
        plain2_long = solve(ID, 2**i)
        if plain2_long:
            print(f"-> Recovered second part of the Flag")
            R.<x> = IntegerModRing (p)[]
            roots = (c1^3*m2^2+a*c1*x^2*m2^2+b*x^3*m2^2 - (c2^2*x^3)).roots()
            print(f"-> Found roots for the polynomial")
            for root,_ in roots:
                try:
                    print(f"FLAG: {lb(root).decode()}_{lb(plain2_long).decode()}")
                    return
                except:
                    pass

if __name__ == '__main__':
    flag()

"""
[1] Processing..
[2] Processing..
[3] Processing..
[4] Processing..
[5] Processing..
[6] Processing..
[7] Processing..
[8] Processing..
[9] Processing..
[10] Processing..
[11] Processing..
[12] Processing..
[13] Processing..
[14] Processing..
[15] Processing..
[16] Processing..
[17] Processing..
[18] Processing..
[19] Processing..
[20] Processing..
-> Recovered second part of the Flag
-> Found roots for the polynomial
FLAG: HZiXCTF{Mv3lg4m4!_3CC_cRypT0Sy5t3m_H4cK}
"""
