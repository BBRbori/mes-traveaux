def main():
    age = int(input("Quel est ton age ?\n"))

    if age < 18:
        total_price = 7
    else:
        total_price = 12
    pop = str(input("souhaitez-vous du pop corn\n"))
    if pop == "oui":
        total_price += 5
    print(total_price)

if __name__ == "__main__":
    main()
