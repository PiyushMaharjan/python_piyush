import numpy as np

'''#one dimensional array
arr1 = np.array([1, 2, 3, 4, 5])

print(arr1.ndim)#output: 1'''

"""#two dimensional array
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])        

print(arr2.ndim)#output: 2"""

'''#three dimensional array
arr3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
                 [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])

print(arr3.shape)#output: 3
'''
'''#shape of array
arr4 = np.array([[['a', 'b','c'],['d','e','f'],['g','h','i']],
                 [['j','k','l'],['m','n','o'],['p','q','r']],
                 [['s','t','u'],['v','w','x'],['y','z',' ']]])
print (arr4.shape)#output: 3 '''                

'''#chain indexing
arr5 = np.array([[['a', 'b','c'],['d','e','f'],['g','h','i']],
                 [['j','k','l'],['m','n','o'],['p','q','r']],
                 [['s','t','u'],['v','w','x'],['y','z',' ']]])
print (arr5[0][0][0])

#multi-dimensional indexing
arr6 = np.array([[['a', 'b','c'],['d','e','f'],['g','h','i']],
                 [['j','k','l'],['m','n','o'],['p','q','r']],
                 [['s','t','u'],['v','w','x'],['y','z',' ']]])
print (arr6[1, 1, 1])'''

'''arr7 = np.array([[['a', 'b','c'],['d','e','f'],['g','h','i']],
                 [['j','k','l'],['m','n','o'],['p','q','r']],
                 [['s','t','u'],['v','w','x'],['y','z',' ']]])
word = arr7[2,0,0]+arr7[0,0,0]+arr7[0,1,2]+arr7[0,0,0]+arr7[1,0,2]

print(word)'''

