def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a>b) or (a>c):
        return a
    elif (a>b) and (c>a) :
        return b
    elif (a<b) and (c<a):
        return b
print(main(6,7,3))
