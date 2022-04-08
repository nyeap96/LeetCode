#Problem # 703

#Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
#Implement KthLargest class:
#
#KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
#int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
# 
#
#Example 1:
#
#Input
#["KthLargest", "add", "add", "add", "add", "add"]
#[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
#Output
#[null, 4, 5, 5, 8, 8]
#
#Explanation
#KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
#kthLargest.add(3);   // return 4
#kthLargest.add(5);   // return 5
#kthLargest.add(10);  // return 5
#kthLargest.add(9);   // return 8
#kthLargest.add(4);   // return 8
# 
#
#Constraints:
#
#1 <= k <= 104
#0 <= nums.length <= 104
#-104 <= nums[i] <= 104
#-104 <= val <= 104
#At most 104 calls will be made to add.
#It is guaranteed that there will be at least k elements in the array when you search for the kth element.


# code start
class KthLargest:
    #so one interesting thing here is that it is kth largest element in sorted order, not kth distinct element. This indicates that duplicates count towards kth largest element so in [1,2,2] and k=1 or 2 the answer would both be 2 because the value 2 is both the largest and second largest elements.
    
    # so when doing add you want to return the kth element from the back when sorted. You could sort everytime it is called and make the coding much easier but it becomes much slower since it will cost nlog(n) everytime kthLargest is called 
    
    def __init__(self, k: int, nums: List[int]):
        # member initialization
        self.numArr = sorted(nums)      # technically this returns a copy of nums that is sorted, does not actually sort nums
        self.k = k
        if not self.numArr:
            self.kLargeVal = None
        else:
            self.kLargeVal = self.numArr[len(self.numArr) - self.k]
        
    
    def add(self, val: int) -> int:
        
        # now we need to insert into the array. I would probably just do a form of insertion sort which is O(n)
        
        for i in range(0,len(self.numArr)):
            if val <= self.numArr[i]:
                self.numArr.insert(i,val)
                self.kLargeVal = self.numArr[len(self.numArr) - self.k]
                return self.kLargeVal
        
        # if goes through whole loop then append to end
        self.numArr.append(val)
        self.kLargeVal = self.numArr[len(self.numArr) - self.k]
        return self.kLargeVal

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)