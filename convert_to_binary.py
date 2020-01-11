"""
* Creator : Chaitanya Ramani
* Email : chaitanyalramani@gmail.com
TODO : using the task data to convert interger to binary

Example : 
60/2 = 30 -> 0(reminder)
30/2 = 15 -> 0(reminder)
15/2 = 7 -> 1(reminder)
7/2 = 3 -> 1(reminder)
3/2 = 1 -> 1
1/2 = 0 -> 1

to varify the number use 
int('111100',2) will return 60 

"""


from stack import Stack

def div_by_two(dec_num):
    s = Stack()

    while dec_num > 0:
        reminder  = dec_num % 2
        s.push(reminder)
        dec_num = dec_num // 2 

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(div_by_two(60))