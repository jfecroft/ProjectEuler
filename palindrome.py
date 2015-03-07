from collections import deque


def is_palindrome(string):
    """ Return if a string is a palindrome."""

    character_deque = deque()
    # Put all chracters in deque.
    for i in string:
        character_deque.appendleft(i)

    # Check if characters in deque are symmetric.
    equal = True
    while equal and len(character_deque) > 1:
        rightcharacter = character_deque.pop()
        leftcharacter = character_deque.popleft()
        if rightcharacter != leftcharacter:
            equal = False  # Not a palidrome
    return equal
