def get_average():
    with open("files11/data.txt", "r") as file:
        data = file.readlines()
    values = [float(i) for i in data[1:]]
    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)
