def is_prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def get_primes(n):
  primes = []
  for i in range(2, n+1):
    if is_prime(i):
      primes.append(i)
  return primes

num = int(input("Enter a number: "))

primes = get_primes(num)
print(primes)