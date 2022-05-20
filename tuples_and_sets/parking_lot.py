
def parking_lot(iters):

    lot = set()

    for _ in range(iters):
        command, car_plate = input().split(', ')

        if command == 'IN':
            lot.add(car_plate)
        elif command == 'OUT' and car_plate in lot:
            lot.remove(car_plate)

    if len(lot) != 0:
        [print(i) for i in lot]
    else:
        print('Parking Lot is Empty')


iterations = int(input())
parking_lot(iterations)
