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
    elif (a>b) and (c>a):
        return c
print(main(5,7,4))