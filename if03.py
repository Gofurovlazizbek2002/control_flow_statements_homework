def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a>0:
      return a+1
    if a<0:
        return a-2
    if a==0:
        return 10

print(main(0))