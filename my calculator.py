class Calculator():
    def sum(self, a, b):
        c = print(a+b)
        return c

    def substraction(self, a, b):
        c = print(a-b)
        return c

    def multiply(self, a, b):
        c= print(a*b)
        return c

    def divide(self, a, b):
        c = print(a/b)
        return c

if __name__ == '__main__':
    sum = Calculator().sum
    sum(5, 2)

    sub = Calculator().substraction
    sub(5, 2)

    mult = Calculator().multiply
    mult(5,2)

    div = Calculator().divide
    div(5, 2)



