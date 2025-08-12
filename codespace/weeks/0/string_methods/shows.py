# defines a function to clean up and format SHOW list into a concantenated string

# a list of cartoon shows with inconsistent spacing or capitalization
SHOWS = [
    "Avatar: The last airbender",
    "Ben 10",
    "Arthur  ",
    "Spongebob squarepants",
    "Phineas And ferb",
    "Kim possible",
    " Jimmy Neutron",
    "the Proud family ",
]

# defines a function to clean up and format SHOWS list into a concantenated string
def get_shows():
    # create empty list to store formatted show names
    shows = []

    for show in SHOWS:
        # remove leading spaces and format to title case
        shows.append(show.strip().title())

    #joins the formatted show names into a string separated by commas
    print(', '.join(shows))


if __name__ == "__main__":
    get_shows()
