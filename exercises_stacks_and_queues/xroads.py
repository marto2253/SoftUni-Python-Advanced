from collections import deque


def xroads(green_secs, free_w_secs):
    cars = deque()
    command = input()
    cars_passed = 0
    crash = False
    while command != 'END':
        if command == 'green':
            green = True
            current_g_secs = green_secs
            while cars:
                if green:
                    car = cars.popleft()
                    current_length_of_car = len(car)
                    if current_g_secs < len(car):
                        green = False
                        time_to_exit = current_g_secs + free_w_secs
                        if abs(current_length_of_car - current_g_secs) > time_to_exit:
                            print('A crash happened!')
                            print(f'{car} was hit at {car[-(current_length_of_car-time_to_exit)]}.')
                            crash = True
                            break
                        else:
                            cars_passed += 1
                    else:
                        current_g_secs -= len(car)
                        cars_passed += 1
                else:
                    break
        if crash:
            break
        else:
            cars.append(command)
        command = input()

    if not crash:
        print('Everyone is safe.')
        print(f'{cars_passed} total cars passed the crossroads.')


green_seconds = int(input())
free_window_seconds = int(input())
xroads(green_seconds, free_window_seconds)