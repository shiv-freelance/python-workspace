
fruits = ['apple', 'banana', 'strawberry', 'mango', 'orange']

# fruits.sort(reverse=True) # reverse the list
# fruits.sort() # by default it sorts based on first character of the word.

fruits.sort(key=lambda x: x[1]) #it got sorted based on 2nd index position.
print(fruits)


result = (1, 2, 't', True, 3.4)
# result.sort() # sorting is possible when a list contains only homogenous elements.
print(result)

nums = {1,2,3,4,5,1,2,3}
