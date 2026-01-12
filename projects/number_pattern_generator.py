def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        string = ''
        for num in range(1, n+1):
            string = f'{string}{str(num)} '
        return string.strip()


number_pattern(12)
