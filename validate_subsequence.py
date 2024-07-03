def isValidSubsequence(array, sequence):
    while len(sequence) != 0 and len(array) != 0:
        if array[0] == sequence[0]:
            array.pop(0)
            sequence.pop(0)
        else:
            array.pop(0)
    if len(sequence) == 0:
        return True
    else:
        return False

#wersja_druga
def isValidSubsequence2(array, sequence):
    j = 0
    for i in range(len(array)):
        if array[i] == sequence[j]:
            j += 1
        if j == len(sequence):
            return True
    return False
