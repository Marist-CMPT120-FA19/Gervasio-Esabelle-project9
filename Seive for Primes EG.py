#Esabelle Gervasio
#Project 8
#primes sieve

def primes(n):
    limit=n+1
    prime=dict()
    for i in range(2, limit): prime[i]=True

    for i in prime:
        factors=range(i, limit, i)
        for f in factors[1:]:
            prime[f]=False
    return [i for i in prime if prime[i]==True]
    

def main():
    print("This program shows you all the prime numbers up to the number n")
    n=int(input("Please enter n: "))
    print(primes(n))
main()
    
        

