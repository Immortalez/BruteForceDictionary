import sys  # sys.exit()

#  Stores the direction for saving the combinations
savingDir = "dictionary.txt"


def cls(n=60):
    for i in range(60):
        print()


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
    for i in range(min_len, max_len + 1):
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
        generate_combinations(ch_set, comb_length - 1, new_comb)


def generate_var_length_combinations(ch_set, min_len, max_len):
    """
    :param ch_set: string/list/set of characters to be used in generation
    :param min_len: minimal length of the combinations
    :param max_len: maximal length of the combinations
    :return: None
    """
    for i in range(min_len, max_len + 1):
        generate_combinations(ch_set, i)


def menu():
    choice = "-1"
    while not ("0" <= choice <= "2"):
        cls()
        print("""                                                                      
            ,-----.                   ,--.             ,------.                           
            |  |) /_ ,--.--.,--.,--.,-'  '-. ,---.     |  .---',---. ,--.--. ,---. ,---.  
            |  .-.  \|  .--'|  ||  |'-.  .-'| .-. :    |  `--,| .-. ||  .--'| .--'| .-. : 
            |  '--' /|  |   '  ''  '  |  |  \   --.    |  |`  ' '-' '|  |   \ `--.\   --. 
            `------' `--'    `----'   `--'   `----'    `--'    `---' `--'    `---' `----' 
                ,------.  ,--.        ,--.  ,--.                                          
                |  .-.  \ `--' ,---.,-'  '-.`--' ,---. ,--,--,  ,--,--.,--.--.,--. ,--.   
                |  |  \  :,--.| .--''-.  .-',--.| .-. ||      \\' ,-.  ||  .--' \  '  /    
                |  '--'  /|  |\ `--.  |  |  |  |' '-' '|  ||  |\ '-'  ||  |     \   '     
                `-------' `--' `---'  `--'  `--' `---' `--''--' `--`--'`--'   .-'  /      
                                                                              `---'
                                                                              
                    [ 1 ]   Generate the dictionary
                    [ 2 ]   Change saving direction ({})
                        
                    [ 0 ]   Exit 
            """.format(savingDir))
        # TODO: Include the whole printout in the loop
        choice = input("\t\t\tYour choice:  ")
    return choice


def menu_generate_dictionary():
    print("menu_generate_dictionary")


def menu_change_directory():
    print("menu_change_directory")


def my_switch(c):
    # Implementation of switch-case statement
    # Not very efficient, but it will do for the purpose
    if c == "0":
        sys.exit(0)
    elif c == "1":
        menu_generate_dictionary()
    elif c == "2":
        menu_change_directory()


ch = ""
while ch != "0":
    my_switch(menu())


#  TODO: Finish the menu
#  TODO: Saving the combinations to file
