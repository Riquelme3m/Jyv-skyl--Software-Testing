def number_of_vowels(s:str)->int:
    '''Return the number of vowels in a string.

    >>> number_of_vowels('riquelme')
    4
    >>> number_of_vowels('monkey')
    2
    >>> number_of_vowels('tangerine')
    4
    '''
    vowels='aeiou'
    return sum(1 for char in s if char in vowels)