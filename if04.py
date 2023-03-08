def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    answer = 0

    if a > b:
        answer += a

    elif b > a:
        answer += b

    elif a == b:
        answer += 0


    return answer

print(main(17,17))