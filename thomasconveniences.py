def integerchecker(integer):
    try:
        integer = int(integer)
        # Returns True as there was no error
        return True
    except ValueError:
        # Returns False as there was an error
        return False


def reversenumbers(finish_, start_):
    reverse_ = []
    for i in range(finish_, start_ - 1, -1):
        reverse_.append(i)
    return reverse_


def removeduplicates(list)

reversenumbers(20, 0)