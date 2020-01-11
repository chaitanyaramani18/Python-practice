"""
* Creator : Chaitanya Ramani
* Email : chaitanyalramani@gmail.com

TODO : bubble sort algorithm example. 

In bubble sort algorithm each elemt of list is 
compare with right next element if it is smaller then swap and it continue till the length of list.
"""
import time 

 
def bubble_sort(unordered_list):
    start =  time.time()
    sorted_list = False
    print(len(unordered_list))

    while not sorted_list:
        sorted_list = True

        for i in range(0, (len(unordered_list)-1)):
            if unordered_list[i] > unordered_list[i+1]:
                sorted_list =False
                unordered_list[i] , unordered_list[i+1] = unordered_list[i+1],unordered_list[i]
    end = time.time()
    print("TIme taken by Bubble sort algorithm",(end-start))
    return unordered_list
    


print(bubble_sort([2,5,3,4,5,56,72,2,8,5,6,34,23,2]))
