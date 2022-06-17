
def flights(*args):
    destinations = {}

    current_destination = ''

    for flight in args:
        flight = str(flight)
        if flight == 'Finish':
            break
        elif not flight.isdigit():
            current_destination += flight
            if flight not in destinations:
                destinations[flight] = 0
        elif flight.isdigit():
            destinations[current_destination] += int(flight)
            current_destination = ''

    return destinations


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print('-----------------------')

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print('-----------------------')

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))