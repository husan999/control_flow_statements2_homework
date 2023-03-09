def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a>b) and (a>c):
        return a
    elif (a>b) and (c>a) and (c>b):
        return c
    elif (a<b) and (c<a) and (c<b):
        return c
    elif a>b and a>c:
        return a
    elif a>c and c>b and a>b:
        return b
    elif a<c and c<b and a>b:
        return b
print(main(5,7,3))