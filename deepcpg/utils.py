def ranges_to_list(x, start=0, stop=None):
    s = set()
    for xi in x:
        xi = str(xi)
        if xi.find('-') >= 0:
            t = xi.split('-')
            if len(t) != 2:
                raise ValueError('Invalid range!')
            if len(t[0]) == 0:
                t[0] = start
            if len(t[1]) == 0:
                t[1] = stop
            s |= set(range(int(t[0]), int(t[1]) + 1))
        else:
            s.add(int(xi))
    s = sorted(list(s))
    return s


def filter_regex(x, regexs):
    if not isinstance(x, list):
        x = [x]
    if not isinstance(regexs, list):
        regexs = [regexs]
    xf = set()
    for xi in x:
        for regex in regexs:
            if re.search(regex, xi):
                xf.add(xi)
    return sorted(list(xf))
