while True:
    try:
        value = input()
        if value == "":
            raise Exception
        else:
            print(value)
    except:
        break;
