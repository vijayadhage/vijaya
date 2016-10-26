import math

def main():
    print("Triangle Area Program")
    print()
    a, b, c = map(float, raw_input("Enter three lengths separated by   commas: ").split(','))

    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2.0
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print()
        return round(area, 4)


    else:
         print()
         print("A triangle cannot be formed.")

if __name__ == '__main__':
    print("Area of the triangle =", main(), "square units.")
