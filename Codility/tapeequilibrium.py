def solution(A):
    """
    Minimize the value |(A[0] + ... + A[P-1]) = (A[P] + ... + A[N-1])|.
    :param A: non-empty list of integers
    :return: an integer - the index value where the smallest difference occurs
    """
    # array must be more than 2 elements
    assert len(A) > 1

    # establish the tallys
    best = None
    before = 0
    after = sum(A)

    # adjust and test at every split
    for P in range(0, len(A) - 1):
        before += A[P]
        after -= A[P]
        difference = abs(before - after)
        if best is None or difference < best:
            best = difference

    return best

print(solution([-100,30,500]))