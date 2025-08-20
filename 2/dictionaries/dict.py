def main():
    grades = {"tebello": "B", "thabiso": "C", "luke": "A", "seth": "A"}

    print(grades)
    print(grades["thabiso"])
    # use grades.get("boemo") to avoid KeyError
    print(grades["boemo"])


if __name__ == "__main__":
    main()
