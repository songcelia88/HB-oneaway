"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""
    if abs(len(w1) - len(w2)) > 1:
    	return False

    error = 0
    if len(w1) > len(w2):
    	shorter_word = w2
    	longer_word = w1
    else:
    	shorter_word = w1
    	longer_word = w2

    for i, letter in enumerate(shorter_word):
    	if letter != longer_word[i]:
    		if len(w1) != len(w2) and letter !=longer_word[i+1]:
    			error +=1
    		elif len(w1) == len(w2):
    			error +=1

    if error <= 1:
    	return True
    else:
    	return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
