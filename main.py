def print_hi(name):
    print(f"Hi, {name}")

if __name__ == "__main__":
    # name input
    name = input("Enter your name : ")
    age = int(input("Enter your age"))
    # added feature for feature-1 branch
    print_hi(name, age)