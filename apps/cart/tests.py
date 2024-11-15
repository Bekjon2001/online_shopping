# ["a","a","b","b","c","c","c"]
def compress(chars: list[str]) -> int:
    dct = {}
    for j in chars:
        if j in dct:
            dct[j] += 1
        else:
            dct[j] = 1

    my_list = list(filter(lambda x: x != 1, list(dct.values()))) + list(dct.keys())
    return len(''.join(map(str, my_list)))


print(compress(["a","a","b","b","c","c","c"]))
