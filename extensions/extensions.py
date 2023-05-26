type = input("File name: ").strip().lower().split(".")[-1]

match type:
    case "gif" | "png":
        print(f"image/{type}")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf" | "zip":
        print(f"application/{type}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")