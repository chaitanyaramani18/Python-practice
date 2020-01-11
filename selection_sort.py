"""
* Creator : Chaitanya Ramani
* Email : chaitanyalramani@gmail.com

TODO : Selection sort algorithm example. 

The Selection Sort Algorithm starts by setting the first item in an unsorted list as 
the position with the lowest (minimum) value. We then use this to compare each of the items to the right.
Whenever we find a new item with a lower value, that becomes our new minimum value and we continue on.

After one iteration of the selection sort algorithm, we create two sublists. 
One will be for unsorted items and the other will be for sorted ones.
We move the minimum item from the unsorted sublist into the last position of our sorted sublist.

After we finish all the iterations,
we should be left with only the largest number in our unsorted sublist (which is now sorted to the highest position as it is the highest value.)

The selection sort algorithm has a complexity of O(n^2) still but nearly always outperforms the bubble sort algorithm in situations where writing is important (fewer switches, more efficient per iteration).

"""

def selection_sort(unordered_list):
    pass