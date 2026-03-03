
#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
print(f'EXPECTED_BAKE_TIME = {EXPECTED_BAKE_TIME} minut.')
PREPARATION_TIME = 2
#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
an argument and returns how many minutes the lasagna still needs to bake
based on the `EXPECTED_BAKE_TIME`.
    """
    return (EXPECTED_BAKE_TIME - elapsed_bake_time)

print(f'Remaining bake time is {bake_time_remaining(30)} minut.')

def preparation_time_in_minutes(layers):
    """Calculate the preparation time in minutes.
    :param layers: int - represents the number of layers used.
    :return: int - calculation of preparation time (in minutes) derived from 'PREPARATION_TIME'.
    Function that takes time for preparing with all layers as an argument and returns how many minutes it takes`.
    """
    return PREPARATION_TIME * layers

print(f'Preparation time is {preparation_time_in_minutes(10)} minut.')

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total elapsed time in mites.
    :param layers: int - represents the number of layers used.
    :param elapsed_bake_time : int - represents the actual minutes the lasagna has been in the oven.
    :return: int - calculation of total time (in minutes) spending on preparing and baking the lasagna.
    Function that takes time for preparing with all layers as an argument and returns how many minutes it takes`.
    """
    prep_time = preparation_time_in_minutes(layers)
    return elapsed_bake_time + prep_time
print(f'Elapsed time is {elapsed_time_in_minutes(3, 20)} minits.')



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
