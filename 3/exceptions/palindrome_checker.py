def is_pal(word):
    """ Returns True if list is palindrome otherwise False """
    try:
        # Validate input type
        if not isinstance(word, list):
            raise TypeError("Input must be a list")

        # Create a copy to avoid modifying the original list
        r_word = word.copy()
        print(r_word, word)

        # Reverse the copy
        r_word.reverse()
        print(r_word, word)

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
    try:
        # Test cases
        print(is_pal(list("abcba"))) # Should return True
        print(is_pal(list("rose"))) # Should return False
        print(is_pal("mom")) # Should raise TypeError

        # Test with non list input
        print(is_pal("not a list")) # Should raise TypeError
    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()
