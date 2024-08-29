calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    global calls
    lens = len(string)
    stringUp = string.upper()
    stringLow = string.lower()
    count_calls()
    return lens,stringUp,stringLow


def is_contains(string, list_to_search):
    global calls
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
