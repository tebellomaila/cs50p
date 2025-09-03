## My Coding Journey: CS50P Problem Set 2

`Projects: Coke Machine, camelCase, Just setting up my Twttr, Nutrition Facts, Vanity Plate Validator`

The past few weeks has been all about string manipulation, input validation, use of dictionaries and lists in Python. I worked through five different projects from CS50P's Problem Set 2, each with their own unique challenges. At first, I felt overwhelmed looking at all the requirements, but breaking them down into smaller problems helped tremendously.

I started with the `coke machine simulator`. The goal was prompt users for coins until they've paid at least 50 cents, then calculate change. But my initial implementation had issues with input validation.My Mistake was I created the `get_valid_coin function` that would return 0 for invalid coins but didn't properly handle reprompting. The while loop was pointless since I returned immediately. What I learned from this input validation requires careful looping and functions should have clear and modular task. Sometines it's better to handle validation in the main loop rather than using helper functions that prompts until getting valid input which felt much cleaner

The `camelCase` problem set. This one seemed straightforward until I considered edge cases, say if the input started with uppercase or numbers. I realized I could process each character individually, adding underscores before uppercase letters (except the first character). The solution was more efficient with list comprehensions. I initially used the same variable name for the function and a list inside it. Renaming the inner variable to `snake_chars` made it much clearer. And then the `Twttr` problem set, the goal was simple to remove all vowels from text input.I used a string of vowels and built a new string by iterating through each character. The Nutrion Fact problem set taught me about dictionaries and case-insentive matching.The FDA provides specific calorie counts for fruits, and I needed to create a dictionary for this. I used built-in lower() function on the input to handle case insensitivity and learned to work with dictionary lookups. I also added try-except blocks to improve the program, even though the problem didn't strictly require it.

The `Vanity Plate Validator` problem set was the most challenging project! So many rules to validate: 
Start with at least two letters
Length between 2-6 characters
Numbers only at the end
First number can't be zero
No special characters

I kept getting `"TypeError: 'bool'` object is not subscriptable" errors. It took me forever to realize I was accidentally passing boolean values between functions instead of strings! I restructured my code to use early returns and a flag system for tracking number placement. Instead of trying to find numbers by index positions, I used boolean flag (`is_number`) to track whether I'd encountered any digits yet. So I learned that early returns make code cleaner and easier to debug and order of validation matters and testing edge cases is important. This problem set pushed me to think more carefully about code structure and validation. I'm getting better at breaking complex problems into smaller, manageable functions. My debugging skills have improved - I'm learning to read error messages more carefully and trace through execution flow. 
I still need to work on writing test cases before implementing solutions. Considering all edge cases upfront and using more descriptive variable names. But overall, I'm proud of my progress. Each project felt like a puzzle, and there's something interesting about seeing all the test cases pass after hours of debugging. I want to learn more about regular expressions for pattern matching and explore unit testing frameworks in Python
