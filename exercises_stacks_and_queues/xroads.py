from collections import deque


def xroads(green_secs, free_w_secs):

    queue_of_cars = deque()
    passed_cars = 0
    green = True
    free = True
    crash = False
    command = input()
    last_char = ''
    car_hit = ''

    while command != 'END':
        if command == 'green':
            current_green_secs = green_secs
            seconds_to_exit = free_w_secs
            while queue_of_cars:
                if crash:
                    break
                car = queue_of_cars.popleft()
                if green:
                    for ch in range(len(car)):
                        if green:
                            current_green_secs -= 1
                        if current_green_secs == 0 and free:
                            green = False
                            seconds_to_exit -= 1
                            if seconds_to_exit < 0:
                                last_char += car[ch + 1]
                                car_hit += car
                                crash = True
                                break
                    else:
                        passed_cars += 1
        elif crash:
            break
        else:
            queue_of_cars.append(command)
        command = input()

    if crash:
        print('A crash happened!')
        print(f'{car_hit} was hit at {last_char}.')
    else:
        print('Everyone is safe.')
        print(f'{passed_cars} total cars passed the crossroads.')


green_seconds = int(input())
free_window_seconds = int(input())
xroads(green_seconds, free_window_seconds)