
def NaiveMatch(T, P):
    n = len(T)
    m = len(P)

    if n < m : return False

    for i in range(n - m):
        if T[i:i + m] == P:
            return True

    return False

text = "vahe is coming yeeee"
pat = "vag"
print(NaiveMatch(text, pat))
