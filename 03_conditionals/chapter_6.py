seat_type = input("Enter seat type (sleeper/AC/genral/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper")
    case "ac":
        print("AC")
    case "general":
        print("General")
    case "luxury":
        print("Luxury")
    case _:
        print("No Match")
        