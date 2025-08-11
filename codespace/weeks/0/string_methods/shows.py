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

def get_shows():
    shows = []

    for show in SHOWS:
        shows.append(show.strip().title())
    print(', '.join(shows))

if __name__ == "__main__":
    get_shows()
