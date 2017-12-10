def highest_affinity(site_list, user_list, time_list):
    work = dict()
    table = dict()
    array = list()

    for i in range(len(site_list)):
        user = user_list[i]
        site = site_list[i]
        if user not in work:
            work[user] = list()
        work[user].append(site)
        l = work[user]
        if len(l) >= 2:
            for j in range(len(l)):
                if l[j] != site:
                    if (l[j], site) in table:
                        table[(l[j], site)] += 1
                    else:
                        table[(l[j], site)] = 1

    m = 0
    result = ("a", "b")
    for key in table:
        if table[key] > m:
            m = table[key]
            result = key

    a, b = result
    c = [a, b]
    a = min(c)
    b = max(c)

    return (a, b)
