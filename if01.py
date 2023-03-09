def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """ 
    if a>b and a>c:
        return a
    elif a<b and b>c:
        return b
    elif a<c and c>b:
        return c
print(main(2,3,5))