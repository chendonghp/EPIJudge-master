from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    # return []
    # #brute-force
    # import math
    # primes=[]
    # def is_prime(a):
    #     if a==2:
    #         return True
    #     for i in range(2,math.ceil(a**0.5)+1):
    #         if a % i ==0:
    #             return False
    #     return True
    #
    # for i in range(2,n+1):
    #     if is_prime(i):
    #         primes.append(i)
    # return primes
    is_prime=[False]*2+[True]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)
            j=i
            while i*j<=n:
                is_prime[i*j]=False
                j+=1
    return primes



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
