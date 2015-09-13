from collatz import memoize


@memoize
def square_digit_chain(num):
    chain = [num]
    next_num = sum(int(i)**2 for i in str(num))
    if next_num in (1, 89):
        chain.append(next_num)
    else:
        chain.extend(square_digit_chain(next_num))
    return chain


def main():
    total = 0
    for i in range(1, 10000000):
        if square_digit_chain(i)[-1] == 89:
            total += 1
    print total


if __name__ == "__main__":
    main()
