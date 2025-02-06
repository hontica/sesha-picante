
def generate_random_number():
    return random.randint(1, 20)

def main():
    print("Random Number Generator (1-20)")
    while True:
        input("Press Enter to generate a random number...")
        print(f"Generated Number: {generate_random_number()}")
        again = input("Do you want to generate another number? (y/n): ")
        if again.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
