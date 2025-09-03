import spacy    # Import spaCy library for natural language processing

# Loads the English tokenizer, tagger, parser, NER, and POS tagger
nlp = spacy.load("en_core_web_sm")

def is_boolean_statement(text):
    """ Determines if a given text is a boolean statement not a question or command """

    # Processes the text with spaCy
    doc = nlp(text.strip()) 

    # Checks if the text ends with a question mark
    if doc[-1].text == "?":
        return False
    
    # Checks if the first token is a question word or auxiliary verb
    # WP = pronoun (who, what), WRB = adverb (when, where), MD = verb (can, could, may)
    if any(token.tag_ in ["WP", "WRB", "MD"] for token in doc[:1]):
        return False
    
    # Checks for polite requests or commands by analysing the sentence and find the root verb of the sentence
    root = [token for token in doc if token.dep_ == "ROOT"]
    if root and root[0].pos_ in ["VERB", "AUX"]:
        # Check if the sentence has a subject
        has_subj =  any(token.dep_ in {"nsubj", "nsubjpass"} for token in doc)
        if not has_subj:
            return False
    
    # If none of the above conditions are met, assume it's a boolean statement
    return True

def main():
    """ Main function to test the boolean statement with given examples """

    # Test cases to check the function works
    statements = ["The Earth revolves around the Sun.", # Declarative statement - Expected: Yes,
                  "Is the Earth flat?",     # Question - Expected: No
                  "Please close the door.", # Polite command - Expected: Yes
                  "I am going to school tomorrow.",  # Declarative statement - Expected: Yes
                  "What time is it?",   # Question - Expected: No
                  "Is it spring season in September.",    # Declarative statement - Expected: Yes
                  "Help!"   # Command - Expected: No
                  ]
    for i, statement in enumerate(statements, 1):
        result = "Yes" if is_boolean_statement(statement) else "No"
        print(f"{statement} This is {'a boolean statement' if result == 'Yes' else 'not a boolean statemnt'}")


if __name__ == "__main__":
    main()
