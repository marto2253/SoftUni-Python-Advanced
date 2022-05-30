def sorting_cheeses(**kwargs):

    items = sorted(kwargs.items(), key= lambda x: (-len(x[1]), x[0]))

    result = []

    for name, count in items:
        result.append(name)
        result.extend(sorted(count, reverse=True))

    return '\n'.join([str(i)for i in result])
print(

    sorting_cheeses(

        Parmigiano=[165, 215],

        Feta=[150, 515],

        Brie=[150, 125]

    )

)

print(

    sorting_cheeses(

        Parmesan=[102, 120, 135],
        Pbrmesan=[102, 120, 135],

        Camembert=[100, 100, 105, 500, 430],

        Mozzarella=[50, 125],

    )

)
