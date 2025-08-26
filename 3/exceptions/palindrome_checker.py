def is_pal(word):
    """ Returns True if string is palindrome otherwise False """
    try:
        # Validate input type
        if not isinstance(word, list):
            raise TypeError("Input must be a list")

        # Create a copy to avoid modifying the original list
        r_word = word.copy()

        # Reverse the copy
        r_word.reverse()

        # Compare the reversed copy with the original list
        return r_word == word
    
    except TypeError as e:
        print(f"TypeError: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def main():
    """ Main function to test palindrome """
    
    # Test cases
    test_cases = [
            list("abcba"),
            list("rose"),
            "mom",
            [1,2,3,2,1],
            []
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"Test case {i}: {test_case}")
        print(f"Output: {is_pal(test_case)}\n")


if __name__ == "__main__":
    main()
