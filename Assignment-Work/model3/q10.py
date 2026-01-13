#  Write a Python function that takes two lists and returns true if
# they haveat least one common member.

def comn_mem(list1,list2):
    for i in list1:
       if i in list2:
           return True
    return False
l1=[1,2,3]
l2=[4,5,6]
print(comn_mem(l1,l2))

