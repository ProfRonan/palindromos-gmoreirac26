"""Main functions"""


def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string
   