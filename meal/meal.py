def main():
    t = convert(input("What time is it? "))

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    #convert 12-hour format
    if time.endswith("a.m."):
        x, y = time.rstrip("am.").split(":")
        if x == "12":
            return round(0 + (float(y)/60), 2)
        else:
            return round(float(x) + (float(y)/60), 2)
    elif time.endswith("p.m."):
        x, y = time.rstrip("pm.").split(":")
        if x == "12":
            return round(float(x) + (float(y)/60), 2)
        else:
            return round(float(x) + (float(y)/60) + 12, 2)
   #convert 24-hour format
    else:
        x, y = time.split(":")
        return round(float(x) + (float(y)/60), 2)


if __name__ == "__main__":
    main()