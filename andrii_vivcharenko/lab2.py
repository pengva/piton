def is_prime(num):
    for i in range(2,(num // 2) + 1):
        if num % i == 0:
            return False
    return True

def prime_num_generator(n):
    for i in range(2, n):
        if is_prime(i):
            yield i

if __name__ == '__main__':
    a = prime_num_generator(100)
    for i in range(0, 50):
        print(next(a))