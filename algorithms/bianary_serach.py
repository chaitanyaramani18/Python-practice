"""
* Creator : Chaitanya Ramani
* Email : chaitanyalramani@gmail.com

TODO : bianary serach algorithm example. 

This is search algorithms to serach element from list. 
=> array must be shorted.
=> mark oth index as lower and last index as upper bound.
=> take a mid of this two index.
=> check if mid is lower then given serach then move your lower bound to mid 
=>if not move your upper bound to list.
"""

def bianary_search(list_a,search_element):
    list_a = sorted(list_a)
    lower_bound  = 0
    upper_bound = len(list_a)-1

    while lower_bound <= upper_bound:
        mid_point  = (lower_bound + upper_bound) // 2
        if list_a[mid_point] == search_element:
            return mid_point
        else:
            if list_a[mid_point] < search_element:
                lower_bound = mid_point + 1
            else:
                upper_bound = mid_point - 1
         
    
print(bianary_search([2,3,50,54,75,99,100,120,3,5,56,43,2345,46,346,6,32,2,5,7,78,8],2))
