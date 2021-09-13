import random
import numpy

array_length = 10
array = []
for i in range(array_length):
    array.append(random.random())



print ('Максимальное значение ', max(array))
print ('Минимальное значение ', min(array))
print ('Среднее значение ', numpy.mean(array))
