def join(*lists, sep='-'):
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)  # add every list
        if i < len(lists) - 1:
            result.append(sep)  # add the sep char
    return result if result else None
