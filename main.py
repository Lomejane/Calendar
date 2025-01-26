def calendar(days_per_month, starting_date):
    # the header
    print("Sun Mon Tue Wed Thu Fri Sat")

    print("    " * starting_date, end="")


    for day in range(1, days_per_month + 1):
        print(f"{day:2} ", end=" ") 
        # 
        if (starting_date + day) % 7 == 0:
            print() # to next line
    print()
def main():
    # User Input (# of days adn starting date)
    try:
        days_per_month = int(input("How many days in this month (28-31): "))
        starting_date = int(input("What is the starting day(1 = Sun, 6 = Sat): "))
    # Check user inputs
        if 28 <= days_per_month <= 31 and 0 <= starting_date <= 6:
            calendar(days_per_month, starting_date)
        else:
            print("Enter numbers only!")
    except ValueError:
        print("Invalid keyword!")

if __name__ == "__main__":
    main()