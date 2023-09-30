



"""List of prime numbers generator."""

"""ENTER YOUR SOLUTION HERE!"""



def primes(number_of_primes):

    if number_of_primes < 1:

        raise ValueError("the number of primes must be greater than 0")

    list = []

    candidate = 1

    while len(list) < number_of_primes:

        prime = True

        i = 2

        while prime == True and i <= candidate/2:

            if candidate%i == 0:

                prime = False

            else:

                i += 1

        if prime == True:

            list.append(candidate)

        candidate += 1

        

    return list

