from os import walk

result = {}

for _, _, files in walk('..'):
    for file in files:
        ext = file.split('.')[-1]
        if ext not in result:
            result[ext] = []
        result[ext].append(file)

sorted_dict = sorted(result.items(), key= lambda x: (x[0], x[1]))

for k, v in sorted_dict:
    print(k, ' '.join(v))




# using recursion
# from os import listdir
# from os.path import isdir, join
#
#
# def directory_traversal(path, files_by_ext):
#     for element in listdir(path):
#         if isdir(join(path, element)):
#             directory_traversal(join(path, element), files_by_ext)
#         else:
#             extension = element.split('.')[-1]
#             if extension not in files_by_ext:
#                 files_by_ext[extension] = []
#             files_by_ext[extension].append(element)
#
#
# result = {}
# directory_traversal('./', result)
#
# for key, value in result.items():
#     print(key, value)
