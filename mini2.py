
from collections import deque

def palindrome_checker():
    text = input("Enter a word or sentence: ")

    # Keep letters and digits; ignore spaces and punctuation
    text = ''.join(
        ch.lower() for ch in text if ch.isalnum()
    )

    if not text:
        print("Please enter at least one letter or digit.")
        return

    stack = []
    queue = deque()

    # Insert characters into stack and queue
    for ch in text:
        stack.append(ch)
        queue.append(ch)

    # Compare reversed and original order
    palindrome = True

    while queue:
        stack_char = stack.pop()
        queue_char = queue.popleft()

        if stack_char != queue_char:
            palindrome = False
            break

    if palindrome:
        print("The given input is a palindrome.")
    else:
        print("The given input is not a palindrome.")

palindrome_checker()
