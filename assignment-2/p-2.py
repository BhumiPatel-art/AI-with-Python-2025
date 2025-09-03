def main():
    shopping_list = []

    while True:
        choice = input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: ")

        if choice == "1":
            item = input("What will be added?: ")
            shopping_list.append(item)

        elif choice == "2":
            if len(shopping_list) == 0:
                print("The list is empty, nothing to remove.")
                continue

            print(f"There are {len(shopping_list)} items in the list.")
            try:
                index = int(input("Which item is deleted?: "))
                if 0 <= index < len(shopping_list):
                    shopping_list.pop(index)
                else:
                    print("Incorrect selection.")
            except ValueError:
                print("Incorrect selection.")

        elif choice == "3":
            print("The following items remain in the list:")
            for item in shopping_list:
                print(item)
            break

        else:
            print("Incorrect selection.")

if __name__ == "__main__":
    main()
