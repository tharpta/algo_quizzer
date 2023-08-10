import random

sorting_algos = []
graph_algos = []
linked_lists=[]




all_algorithms = sorting_algos + graph_algos + linked_lists

def algo_selector(remaining_algorithms):
    """
    algo_selector function

    Parameters:
    - remaining_algorithms (list): The list of algorithm names that have not yet been studied. 

    Functionality:
    - Prints a message and restarts the list when all algorithms have been studied.
    - Randomly selects an algorithm from the remaining list to print.
    - Removes the selected algorithm from the remaining list.
    - Prompts the user to continue or quit.
    - Breaks the loop if user enters 'n' to quit.
    - Continues looping and selecting algorithms until user quits.

    The all_algorithms list contains all algorithm names.
    The algo_selector function takes the full list as a parameter initially.
    It removes algorithms as they are selected to print.
    When the remaining list is empty, it resets it back to the full list.
    """
    while True:
        if len(remaining_algorithms) == 0:
            print("All algorithms have been studied! Starting list over")
            remaining_algorithms = all_algorithms[:]
            print(f"The len of all algorithms is {len(all_algorithms)}")

        random_num = random.randint(0, len(remaining_algorithms) - 1)
        print(remaining_algorithms[random_num])
        remaining_algorithms.pop(random_num)
        
        nextAlgo = input("Continue? (y/n): ")
        while nextAlgo != 'y' and nextAlgo != 'n':
            nextAlgo = input("Continue? (y/n): ")
        
        if nextAlgo == 'n':
            break


algo_selector(all_algorithms[:])