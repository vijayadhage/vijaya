def summation_of_primes_below_n(n):
    list = []
    sum = 0
    for i in range(2, n):
        if checks_if_prime(i) == True:
            list.append(i)
    for j in list:
        sum+=j
    return sum

def checks_if_prime(n):
    if n == 2:
        return True
    import math
    upperlimit=math.ceil(math.sqrt(n))+1
    for i in range(2, upperlimit):
        if n%i == 0:
            return False
        elif i == math.ceil(math.sqrt(n)):
            return True

print(summation_of_primes_below_n(2000000))

'''There are a couple of hacks that I can tell right away. 

In the following piece of code, one modification is here.

    def checks_if_prime(n):
        if n == 2:
            return True
        import math
        upperlimit=math.ceil(math.sqrt(n))+1
        for i in range(2, upperlimit):
            if n%i == 0:
                return False
            elif i == :
                return True

I will still try to optimize `math.ceil(math.sqrt(n))` somehow, if I can save that for every calculation, that should be great.'''
