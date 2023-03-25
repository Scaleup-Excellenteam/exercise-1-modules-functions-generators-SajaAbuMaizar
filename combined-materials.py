def interleave(*iterables):
    iterators = [iter(it) for it in iterables]  # get the parameters
    result = []
    while iterators:  # until we're done
        for it in iterators:
            try:
                result.append(next(it))  # add the wanted element
            except StopIteration:
                iterators.remove(it)
    return result
