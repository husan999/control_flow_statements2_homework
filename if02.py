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

    answer = 0
    if (a < b) or (a < c):
        answer += a

    elif ((a < b) or (c < a)) and (c < b):
        answer += c

    elif ((b < a) or (a < c)) and (b < c):
        answer += b

    elif (b < a) or (b < c):
        answer += b

    elif ((b < a) or (c < b)) and (c < a):
        answer += c

    elif ((a < b) or (b < c)) and (a < c):
        answer += a

    elif (c < a) or (c < b):
        answer += c

    elif ((c < a) or (b < c)) and (b < a):
        answer += b

    elif ((a < c) or (c < b)) and (a < b):
        answer += a

    return answer

print(main(9,8,1))