import sys
import time
from trees.bst import Tree

def main():
    try:
        f = open("text/" + sys.argv[1])
    except OSError as e:
        print("OS error({0}): {1}".format(e.errno, e.strerror))
        sys.exit()
    except:
        print("Usage: 'python tree_runner.py [name_of_text_file]'")
        sys.exit()

    data = f.read().strip()
    nums = str.split(data, "\n")
    nums = [int(num) for num in nums]

    k_sum, runtime = k_median_sum(nums) 
    print("k median sum is: " + str(k_sum) + " and it took: " + str(runtime) + " s")
    f.close()

def k_median_sum(nums):
    start_time = time.process_time()
    
    root = Tree(nums[0])
    sum = root.val 

    for num in nums[1:]:
        root.insert(num)
        if root.size % 2 == 0:
            mid = root.size//2
        else:
            mid = (root.size+1)//2
        mid_val = root.select(mid) 
        sum += mid_val
    
    end_time = time.process_time()
    length_time = end_time - start_time
    
    return sum, length_time

main()
