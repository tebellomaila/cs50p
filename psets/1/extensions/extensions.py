def get_file_extension(filename):
    index = filename.rfind(".")

    ext = slice(index, None)
    file_extension = filename[ext]

    match file_extension:
        case ".gif":
            media_type = "image/gif"
        case ".jpg" | ".jpeg":
            media_type = "image/jpeg"
        case ".png":
            media_type = "image/png"
        case ".pdf":
            media_type = "application/pdf"
        case ".txt":
            media_type = "text/plain"
        case ".zip":
            media_type = "application/zip"
        case _:
            media_type = "application/octet-stream"
    return media_type

def main():
    file = input("File name: ").strip().lower()
    extension = get_file_extension(file)
    print(extension)

if __name__ == "main"
    main()
