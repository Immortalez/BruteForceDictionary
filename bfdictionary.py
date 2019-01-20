

def combinations_amount(ch_set, min_len, max_len):
    """
    :param ch_set: string/list/set of characters to be used in generation
    :param min_len: minimal length of the combinations
    :param max_len: maximal length of the combinations
    :return: amount of all combinations that will be generated
    """
    # Eliminating duplicates using the unique elements property of sets
    if isinstance(ch_set, str) or isinstance(ch_set, list) or isinstance(ch_set, set):
        ch_set = sorted(set(ch_set))
    else:
        print("Invalid character set was provided.")
        return

    ch_set_len = len(ch_set)
    total = 0
    for i in range(min_len, max_len+1):
        total += ch_set_len ** i
    return total


def generate_combinations(ch_set, comb_length, current_comb=""):
    """
    :param ch_set: string/list/set of characters to be used in generation
    :param comb_length: length of the generated combinations
    :param current_comb: character(s) that every combination starts with
    :return: None
    """
    # Eliminating duplicates using the unique elements property of sets
    if isinstance(ch_set, str) or isinstance(ch_set, list) or isinstance(ch_set, set):
        ch_set = sorted(set(ch_set))
    else:
        print("Invalid character set was provided.")
        return

    if comb_length == 0:
        # Current combination reached its target length, print the combination
        print(current_comb)
        return

    ch_set_len = len(ch_set)
    for i in range(ch_set_len):
        # Generating next combination
        # Calling the function recursively with decremented length
        # as we go one character by one
        # Therefore we end up with 'comb_length' amount of nested loops
        new_comb = current_comb + chset[i]
        generate_combinations(ch_set, comb_length-1, new_comb)


def generate_var_length_combinations(ch_set, min_len, max_len):
    """
    :param ch_set: string/list/set of characters to be used in generation
    :param min_len: minimal length of the combinations
    :param max_len: maximal length of the combinations
    :return: None
    """
    for i in range(min_len, max_len+1):
        generate_combinations(ch_set, i)


chset = "abcdefghijklmnopqrstuwxyz"
generate_var_length_combinations(chset, 3, 5)


# Saving the combinations to a file




