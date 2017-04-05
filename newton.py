def factorial(number):
    result = 1
    if number == 0: return 1
    if number >= 1:
        for each in range(1, number+1):
            result *= each
        return int(result)


def newton_binomial(top_coeff, btm_coeff):
    if btm_coeff > top_coeff: return None
    numerator = factorial(top_coeff)
    denominator = factorial(top_coeff - btm_coeff) * factorial(btm_coeff)
    result = int(numerator / denominator)
    return result


# Pascal triangle
for top in range(10):
    for btm in range(10):
        print(newton_binomial(top, btm), end="\t")
    print("\n")


def sum_of_binomials(number, include_zero=False):
    result = 0
    for each in range(1, number+1, 1):
        result += newton_binomial(number, each)
    if include_zero: return int(result+1)
    else: return int(result)

print(sum_of_binomials(5))
