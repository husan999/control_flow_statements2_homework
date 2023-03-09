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
        answer=a
    elif (a>b) and (c>a) and (c>b):
        answer=c
    elif (a<b) and (c<a) and (c<b):
        answer=c
    elif a>b and a>c:
        answer=a
    elif a>c and c>b and a>b:
        answer=b
    elif a<c and c<b and a>b:
        answer=b
    return answer
print(main(5,7,3))