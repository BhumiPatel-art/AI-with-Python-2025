def main():
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]  # 10 products
    total_sum = 0

    print("Supermarket")

    while True:
        try:
            choice = int(input("Please select product (1-10) 0 to Quit: "))
        except ValueError:
            print("Invalid input, try again.")
            continue

        if choice == 0:
            break
        elif 1 <= choice <= 10:
            price = prices[choice - 1]
            total_sum += price
            print(f"Product: {choice} Price: {price}")
        else:
            print("Invalid product number, try again.")

    print(f"Total: {total_sum}")

    while True:
        try:
            payment = int(input("Payment: "))
            if payment < total_sum:
                print("Not enough payment, try again.")
                continue
            break
        except ValueError:
            print("Invalid input, enter a number.")

    change = payment - total_sum
    print(f"Change: {change}")


if __name__ == "__main__":
    main()
