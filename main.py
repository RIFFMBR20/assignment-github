from addition import add
from subtraction import subtract

def main():
    print("Kalkulator Sederhana")
    a = 10
    b = 5

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")

if __name__ == "__main__":
    main()