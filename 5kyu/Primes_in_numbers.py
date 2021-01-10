def prime_factors(n):
    n_temp = n
    list_of_factors = []
    while n_temp != 1:
        return_list = factor_search(n_temp)
        list_of_factors.append(return_list[0])
        n_temp = return_list[1]
    output_string = ""
    for i in range(2, list_of_factors[-1] + 1):
        counter = list_of_factors.count(i)
        if counter == 1:
            output_string += f"({i})"
        elif counter > 1:
            output_string += f"({i}**{counter})"
    return output_string


def factor_search(n):
    for factor in range(2, n + 1):
        if not n % factor:
            return factor, int(n/factor)
    return 1

