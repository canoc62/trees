import sys
import time
from trees.bst import Tree

def main():
    f = open("text/" + sys.argv[1])
    data = f.read()
    nums = str.split(data, "\n")
    nums = nums[0:len(nums)-1]

    k_sum, runtime = k_median_sum(nums) 
    print("k median sum is: " + str(k_sum) + " and it took: " + str(runtime) + " s")
    f.close()

def k_median_sum(nums):
    start_time = time.clock()
    
    root = Tree(int(nums[0]))
    sum = root.val 

    for num in nums[1:]:
        root.insert(int(num))
        if root.size % 2 == 0:
            mid = root.size//2
        else:
            mid = (root.size+1)//2
        mid_val = root.select(mid) 
        sum += mid_val
    
    end_time = time.clock()
    length_time = end_time - start_time
    
    return sum, length_time

main()
