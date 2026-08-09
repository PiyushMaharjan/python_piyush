import numpy as np

ages = np.array([[22, 25, 30, 35, 40, 45, 50],
                [39, 42, 47, 52, 57, 62, 67]])

'''teenagers = ages[ages < 30]
adults = ages[(ages >= 30) & (ages < 60)]
seniors = ages[ages >= 60]
evens = ages[ages % 2 == 0]
odd = ages[ages % 2 != 0]   


print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odd)'''

adults = np.where(ages >= 30, ages, 0)


print(adults)