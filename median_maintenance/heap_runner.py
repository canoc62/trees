import sys
import time
from heaps.heaps import Heap, MinHeap

HEAP_LENGTH_DIFF_THRESH = 2

def main():
    try:
        f = open("text/" + sys.argv[1])
    except OSError as e:
        print("OS error({0}): {1}".format(e.errno, e.strerror))
        sys.exit()
    except:
        print("Usage: 'python heap_runner.py [name_of_text_file]'")
        sys.exit()

    data = f.read().strip()
    nums = str.split(data, "\n")
    nums = [int(num) for num in nums]
    k_sum, runtime = k_median_sum(nums)
    print("k median sum is: " + str(k_sum) + " and it took: " + str(runtime) + " s")
    f.close()

def k_median_sum(nums):
    if len(nums) == 0:
        return 0, time.process_time()
    elif len(nums) == 1:
        return nums[0], time.process_time()
    else:
        start_time = time.process_time()

        max_heap = Heap()
        min_heap = MinHeap()
        
        first_val = nums[0]
        max_heap.insert(first_val)
        k_sum = first_val

        for num in nums[1:]:
            if len(max_heap) == 0 or num <= max_heap.peek():
                max_heap.insert(num)
                if len(max_heap) - len(min_heap) == HEAP_LENGTH_DIFF_THRESH:
                    min_heap.insert(max_heap.extract())
            else:
                min_heap.insert(num)
                if len(min_heap) - len(max_heap) == HEAP_LENGTH_DIFF_THRESH:
                    max_heap.insert(min_heap.extract())
            if len(max_heap) >= len(min_heap):
                k_sum += max_heap.peek()
            else:
                k_sum += min_heap.peek()

        end_time = time.process_time()
        length_time = end_time - start_time

        return k_sum, length_time

if __name__ == '__main__':
    main()
