def main():
    userinput = input()
    convert(userinput)

def convert(to):
    #replace :(
    to = to.replace(":(","🙁")

    #replace :)
    to = to.replace(":)","🙂")

    print(to)

main()