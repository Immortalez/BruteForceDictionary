import sys  # sys.exit()
import time  # time.sleep()
import threading
#from threading import Thread  # checking if function is alive

#  Stores the direction for saving the combinations
saving_dir = "dictionary.txt"

# Predefined charsets
charset1 = "abcdefghijklmnopqrstuvwxyz"
charset2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
charset3 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
custom_charset = ""
amount_to_be_generated = 1
starting_with = ""  # String that every combination starts with


def cls(n=60):
    # Utility function to enhance visual experience
    for i in range(n):
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


def generate_combinations(ch_set, comb_length, current_comb=starting_with, dir=saving_dir):
    """
    :param ch_set: string/list/set of characters to be used in generation
    :param comb_length: length of the generated combinations
    :param current_comb: character(s) that every combination starts with
    :param dir: location of saving the dictionary
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
        print(current_comb)  # TODO: Comment out when done
        return

    ch_set_len = len(ch_set)
    for i in range(ch_set_len):
        # Generating next combination
        # Calling the function recursively with decremented length
        # as we go one character by one
        # Therefore we end up with 'comb_length' amount of nested loops
        new_comb = current_comb + ch_set[i]
        generate_combinations(ch_set, comb_length - 1, new_comb)


def generate_var_length_combinations(ch_set, min_len, max_len, dir=saving_dir):
    """
    :param ch_set: string/list/set of characters to be used in generation
    :param min_len: minimal length of the combinations
    :param max_len: maximal length of the combinations
    :param dir: location of saving the dictionary
    :return: None
    """

    # # Requires multithreading to work asynchronously
    # # Printing the progress
    # counter = 0
    # dic = {0: "\r\t\tGenerating dictionary    [{:.0f}%]  /".format((100*already_generated/amount_to_be_generated)),
    #        1: "\r\t\tGenerating dictionary.   [{:.0f}%]  -".format((100*already_generated/amount_to_be_generated)),
    #        2: "\r\t\tGenerating dictionary..  [{:.0f}%]  \\".format((100*already_generated/amount_to_be_generated))}
    # while generation_thread.isAlive():
    #     print(dic.get(counter % 3), end="")
    #     counter += 1
    #     time.sleep(0.05)

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
            """.format(saving_dir))
        # TODO: Include the whole printout in the loop
        choice = input("\t\t\tYour choice:  ")
    return choice


def menu_generate_dictionary():
    cls()
    print(
        """
         __   ___       ___  __       ___  __   __  
        / _` |__  |\ | |__  |__)  /\   |  /  \ |__) 
        \__> |___ | \| |___ |  \ /~~\  |  \__/ |  \ 
        """)
    cls(3)
    print('     \tPredefined charsets (type "[ 1 ]" to use the [ 1 ] etc.')
    print("     \t\t[ 1 ]\t" + charset1)
    print("     \t\t[ 2 ]\t" + charset2)
    print("     \t\t[ 3 ]\t" + charset3)

    global custom_charset
    custom_charset = input("\n     \tEnter the charset:  ")
    if len(custom_charset) > 0:
        if custom_charset == "[ 1 ]":
            custom_charset = charset1
        elif custom_charset == "[ 2 ]":
            custom_charset = charset2
        elif custom_charset == "[ 3 ]":
            custom_charset = charset3
    else:
        custom_charset = charset1
    time.sleep(1)

    minlen = int(input("     \tMinimal length: "))
    maxlen = int(input("     \tMaximal length: "))
    cls(2)

    global amount_to_be_generated
    amount_to_be_generated = combinations_amount(custom_charset, minlen, maxlen)
    print("     \tTotal amount of combinations: {}".format(amount_to_be_generated))
    print("\n     \tProgram will go back to the menu when finished.")
    time.sleep(0.5)
    print("     \tGenerating the dictionary...")

    generate_var_length_combinations(custom_charset, minlen, maxlen, saving_dir)
    input("Press ENTER to continue.")


def menu_change_directory():
    cls()
    print(
        """
         __     __   ___  __  ___  __   __      
        |  \ | |__) |__  /  `  |  /  \ |__) \ / 
        |__/ | |  \ |___ \__,  |  \__/ |  \  |  
        """)
    cls(3)
    new_dir = input("\t\t\tEnter new directory (with extension):  ")
    cls(4)
    global saving_dir
    saving_dir = new_dir
    time.sleep(0.3)


def menu_exit():
    cls()
    print(
        """
         .88888.                          dP dP                         
        d8'   `88                         88 88                         
        88        .d8888b. .d8888b. .d888b88 88d888b. dP    dP .d8888b. 
        88   YP88 88'  `88 88'  `88 88'  `88 88'  `88 88    88 88ooood8 
        Y8.   .88 88.  .88 88.  .88 88.  .88 88.  .88 88.  .88 88.  ... 
         `88888'  `88888P' `88888P' `88888P8 88Y8888' `8888P88 `88888P' 
                                                           .88          
                                                       d8888P           
        """
    )
    cls(4)
    time.sleep(0.5)
    sys.exit(0)


def my_switch_menu(c):
    # Implementation of switch-case statement
    # Not very efficient, but it will do for the purpose
    if c == "0":
        menu_exit()
    elif c == "1":
        menu_generate_dictionary()
    elif c == "2":
        menu_change_directory()


ch = ""
while ch != "0":
    my_switch_menu(menu())


#  TODO: Saving the combinations to file
