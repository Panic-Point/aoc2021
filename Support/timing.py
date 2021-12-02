def timing(start, end):
    t = (end - start)
    unit = 's'
    if t < 1:
        t *= 1000
        unit = 'ms'
        if t < 100:
            t *= 1000
            unit = 'μs'
    print('Time taken {}{}'.format(round(t, 3), unit))
