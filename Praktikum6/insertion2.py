# Insertion Sort Descending

def insertionSort(data):
    for index in range(1, len(data)):
        currentvalue = data[index]
        position = index
        while position > 0 and data[position - 1] < currentvalue: # gunakan "<" diantara  'data[position - 1]' dan 'currentvalue' jika ingin mengurutkan dari yang paling besar ke kecil (descending)
            data[position] = data[position - 1]
            position = position - 1
        data[position] = currentvalue

data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)