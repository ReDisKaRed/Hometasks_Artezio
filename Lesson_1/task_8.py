def highest_values(dictionary):
    list_values = []
    for value in dictionary.values():
        list_values.append(value)
    if len(list_values) != 3:
        list_values.pop(min(list_values))
    return list_values


print(highest_values({"Roma's age": 10, "Nikita's age": 5, "Max's age": 22, "Vlad's age": 3}))





