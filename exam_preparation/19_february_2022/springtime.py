from collections import Counter


def start_spring(**kwargs):
    spring = kwargs
    c = Counter(spring.values())

    sorted_dict = sorted(spring.items(), key= lambda x: (-c[x[1]], x[1], x[0]))

    result = {}
    final_result = ''
    for k, v in sorted_dict:
        if v not in result:
            result[v] = []
        result[v].append(k)

    for k, v in result.items():
        final_result += f'{k}:\n'
        joined = "\n-".join(v)
        final_result += f'-{joined}\n'

    return final_result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

print('-------------------------------------------------')

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

print('-------------------------------------------------')

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
