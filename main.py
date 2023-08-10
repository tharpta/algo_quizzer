import random

sorting_algos = []
graph_algos = []
linked_lists=[]




all_algorithms = sorting_algos + graph_algos + linked_lists

def algo_selector(remaining_algorithms):
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