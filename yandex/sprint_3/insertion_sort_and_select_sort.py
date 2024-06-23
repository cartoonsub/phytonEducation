def insertion_sort(array):
  for i in range(1, len(array)):
    item_to_insert = array[i]
    j = i

    print(item_to_insert, array[j-1], 'j:', j)
    while j > 0 and item_to_insert < array[j-1]:
      array[j] = array[j-1]
      j -= 1
    array[j] = item_to_insert
    print('step {}, sorted {} elements: {}'.format(i, i+1, array))

  print(array)
insertion_sort([11, 2, 0, 9, 7, 1])
# step 1, sorted 2 elements: [2, 11, 9, 7, 1]
# step 2, sorted 3 elements: [2, 9, 11, 7, 1]
# step 3, sorted 4 elements: [2, 7, 9, 11, 1]
# step 4, sorted 5 elements: [1, 2, 7, 9, 11]


print('---')
def select_sort(array):
    lenght = len(array)
    for i in range(lenght - 1):
        print('step:', i, array)
        min_index = i
        for k in range(i + 1, lenght):
            if array[k] < array[min_index]:
                min_index = k
        array[i], array[min_index] = array[min_index], array[i]
    return array

print(select_sort([11, 2, 9, 7, 1]))
