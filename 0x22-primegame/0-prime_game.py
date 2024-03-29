#!/usr/bin/python3
""" prime game """


def isPrime(x):
    """ checks if a number is prime """
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ prime game """
    if x < 1 or not nums or nums == []:
        return None
    p = min(x, len(nums))
    Maria = 0
    Ben = 0
    player = 0
    for i in range(p):
        if nums[i] < 2:
            Ben += 1
        elif nums[i] == 2:
            Maria += 1
        else:
            player = True
            prime_exist = 1
            n = list(range(2, nums[i] + 1))
            while (prime_exist):
                prime_exist = 0
                for j in n:
                    if (isPrime(j)):
                        prime_exist = 1
                        player = not player
                        n = list(filter(lambda x: x % j != 0, n))
            if (player):
                Ben += 1
            else:
                Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None