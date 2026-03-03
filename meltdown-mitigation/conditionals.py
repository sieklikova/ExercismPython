"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be balanced in criticality if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    else :
        return False

print(is_criticality_balanced(750, 650))
print(is_criticality_balanced(799, 501))
print(is_criticality_balanced(500, 600))
print(is_criticality_balanced(1000, 800))
print(is_criticality_balanced(800, 500))
print(is_criticality_balanced(800, 500.01))
print(is_criticality_balanced(799.99,500 ))
print(is_criticality_balanced( 500.01, 999.99))
print(is_criticality_balanced(625, 800 ))
print(is_criticality_balanced(625.99, 800 ))
print(is_criticality_balanced(625.01, 799.99 ))
print(is_criticality_balanced(799.99, 500.01 ))
print(is_criticality_balanced(624.99, 799.99 ))
print(is_criticality_balanced(500, 1000 ))
print(is_criticality_balanced(500.01, 1000 ))
print(is_criticality_balanced( 499.99, 1000))

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    percentage_value = (voltage * current) / theoretical_max_power * 100

    if percentage_value >= 80:
        return 'green'
    elif percentage_value >= 60 and percentage_value < 80:
        return 'orange'
    elif percentage_value >= 30 and percentage_value < 60:
        return 'red'
    else:
        return 'black'

print(reactor_efficiency(10, 1000, 10000))
print(reactor_efficiency(10, 999, 10000))
print(reactor_efficiency(10, 800, 10000))
print(reactor_efficiency(10, 799, 10000))
print(reactor_efficiency(10, 700, 10000))
print(reactor_efficiency(10, 600, 10000))
print(reactor_efficiency(10, 599, 10000))
print(reactor_efficiency(10, 560, 10000))
print(reactor_efficiency(10, 400, 10000))
print(reactor_efficiency(10, 300, 10000))
print(reactor_efficiency(10, 299, 10000))
print(reactor_efficiency(10, 200, 10000))
print(reactor_efficiency(10, 0, 10000))

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    calculation_danger_level = ((temperature * neutrons_produced_per_second)/threshold)*100
    if calculation_danger_level < 90:
        return 'LOW'
    elif calculation_danger_level >= 90 and calculation_danger_level <= 110:
        return 'NORMAL'
    else:
        return 'DANGER'

print(f'The danger level of the reactor is {fail_safe(10, 399, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 300, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 1, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10,0 , 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 901, 10000)}.')
print(f'The danger level of the reactor is {fail_safe(10, 1000, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 1099, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 899, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 700, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 400, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 1101, 10000)}')
print(f'The danger level of the reactor is {fail_safe(10, 1200, 10000)}')

