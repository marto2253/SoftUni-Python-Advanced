
def longest_intersection(iters):

    first_range = set()
    second_range = set()

    intersections = []

    for _ in range(iters):
        ranges = input().split('-')
        left_ranges = ranges[0].split(',')
        right_ranges = ranges[1].split(',')

        for num in range(int(left_ranges[0]), int(left_ranges[1]) + 1):
            first_range.add(int(num))

        for num in range(int(right_ranges[0]), int(right_ranges[1]) + 1):
            second_range.add(int(num))

        sets_intersection = first_range.intersection(second_range)

        if len(sets_intersection) > len(intersections):
            intersections.clear()
            intersections.append(first_range.intersection(second_range))

        first_range.clear()
        second_range.clear()

    print(f'Longest intersection is {[i for i in intersections[0]]} with length {len(intersections[0])}')


iterations = int(input())
longest_intersection(iterations)
