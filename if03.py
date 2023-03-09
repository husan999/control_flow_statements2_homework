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
        answer=a
    elif (a>b) and (c>a) or (c>b):
        answer=b
    elif (a<b) and (c<a) or (c<b):
        answer=b
    elif a<b or a<c:
        answer=a
    elif a>c and c>b or a<b:
        answer=c
    elif a<c and c<b or a>b:
        answer=c
    return answer
print(main(5,7,3))
