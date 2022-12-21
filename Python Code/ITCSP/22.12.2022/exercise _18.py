## Write a program which will prin out the prime numbers up to the number provided by the user through input73

def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def print_primes(n):
  for i in range(2, n+1):
    if is_prime(i):
      print(i)

num = int(input("Enter a number: "))

print_primes(num)