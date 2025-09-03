import random


# This ensures the sequence of random numbers will be the same every time the program runs for reproducible results
random.seed(30)
for _ in range(6):
    print(f"With seed: {random.random()}")
print()

# This makes subsequent random numbers unpredictable and different each run using the system's current time
random.seed()   # Reset seed to use system time
saved_state =  random.getstate()    # Save state before generating random float numbers
for _ in range(6):
    print(f"Without seed: {random.random()}")
print()

# Restore the previous state
random.setstate(saved_state)

# This will regenerate the same 6 numbers as above
for _ in range(9):
    print(f"Saved state without seed: {random.random()}")
print()

# Generate additional random values
for _ in range(3):
    print(f"3 random bits: {random.getrandbits(3)}")
print()

# randrange is equivalent to randit
for _ in range(3):
    print(f"Random range (3-9): {random.randrange(3,10)}")
print()
for _ in range(3):
    print(f"Random integer (3-9): {random.randint(3,9)}")
