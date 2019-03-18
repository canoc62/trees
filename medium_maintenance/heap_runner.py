import sys
import time
from ..heaps import Heap, MinHeap

def main():
    f = open("text/" + sys.argv[1])
    data f.read()
    nums = str.split(data, "/n")
    nums = nums[0:len(nums) - 1]

    k_sum, runtime = k_median_sum(nums)
    print("k median sum is: " + str(k_sum) + " and it took: " + str(runtime) + " s")
    f.close()

def k_median_sum(nums):
    start_time = time.clock()

    end_time = time.clock()
    length_time = end_time - start_time

    for num in nums[1:]

    return sum, length_time

main()
