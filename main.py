import random

def run_single_trial(switch_doors, total_num_of_doors=3):
    """
    A trial is run where door 1 is assumed to be the winning door. The host
    will choose one of the remaining two doors to reveal an incorrect choice.

    """

    chosen_door = random.randint(1, total_num_of_doors)
    if switch_doors:
        # The host reveals an incorrect choice
        revealed_door = 3 if chosen_door == 2 else 2

        # Make the switch by choosing any other door than the initially-selected
        # one and the one just opened to reveal a goat.
        available_doors = [door_number for door_number in range(1, total_num_of_doors + 1)
                                if door_number not in (chosen_door, revealed_door)]

        chosen_door = random.choice(available_doors)

    # You win if you picked door number 1
    return chosen_door == 1

def run_all_trials(total_num_of_trials, switch_doors, total_num_of_doors=3):
    """
    Run x number of trials with y number of doors, with and without switching
    to see success percentage. Returns the number of trials which resulted in
    winning the car by picking door number 1.

    """

    number_of_wins = 0

    # Run all single trials and return number of wins
    for i in range(total_num_of_trials):
        if run_single_trial(switch_doors, total_num_of_doors):
            number_of_wins += 1

    return number_of_wins

num_of_doors, num_of_trials = 100, 1000000
num_of_wins_without_switching = run_all_trials(num_of_trials, False, num_of_doors)
num_of_wins_with_switching = run_all_trials(num_of_trials, True, num_of_doors)

print('Monty Hall Problem with {} doors'.format(num_of_doors))
print('Proportion of wins without switching: {:.4f}'
      .format(num_of_wins_without_switching / num_of_trials))
print('Proportion of wins with switching: {:.4f}'
      .format(num_of_wins_with_switching / num_of_trials))