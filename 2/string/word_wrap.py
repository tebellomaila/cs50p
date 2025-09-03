def word_wrap(text, width, punct=" "):
    """ Wrap the text to a specified width by breaking at a certain punctuation when possible """
    words = []  # List to store the wrapped lines
    start = 0

    # Loop until the entire text is processed
    while start < len(text):
        # Calculate the end index for the current line
        end = start + width
        
        # Check if the end index has processed the entire text and then add the rest of the text
        if end >= len(text):
            word = text[start:]
            words.append(word)
            break

        # Extract the current part of the text
        parts = text[start:end]

        # Find the last given punctuation or space in the text to wrap at this position 
        pos = parts.rfind(punct)

        if pos > 0:
            line = parts[:pos]
            words.append(line)
            start += pos + 1      # Move start position after the given punctuation or space
            
        elif pos == 0:
            start += 1      # Skip the given punctuation or space and move to the next character
        else:   
            # No punctuation mark or space found, break at exact width
            words.append(parts)
            start = end
    
    return words

def main():
    """ Main function to test the word wrap """
    sentence = input("Type your message: ")

    wrapped_lines = word_wrap(sentence, 21)

    for i,line in enumerate(wrapped_lines, 1):
        print(f"Line {i}: {line}")


if __name__ == "__main__":
    main()
