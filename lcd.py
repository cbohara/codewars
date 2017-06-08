import sys


def main():
    # [[num1, denom1], [num2, denom2], ... [num n, denom n]]
    input_matrix = [[1, 2], [1, 3], [1, 4]]

    # create list of denominators
    denoms = sorted([x[1] for x in input_matrix])
    matrix = denoms[:]

    # create matrix of multiples
    for index, value in enumerate(denoms):
        matrix[index] = [value * x for x in range(1, 20)]

    # match multiples of largest denominator to other lists
    master = matrix[-1]
    common = 0
    for current in master:
            count = 0
            for multiples in matrix:
                if current in multiples:
                    count += 1
            if count == len(denoms):
                common = current
                break

    # common denominator is now stored in common > use to determine final output
    for index, value in enumerate(denoms):
        denoms[index] = [int(common/value), common]

    return denoms

if __name__ == "__main__":
    sys.exit(main())
