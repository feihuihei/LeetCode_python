import math
class PaiXu:
    #快速排序
    def quick_sort(self, arr, left, right):
        if left < right:
            q = self.partition(arr, left, right)
            self.quick_sort(arr, left, q)
            self.quick_sort(arr, q+1, right)
        else:
            return

    def partition(self, arr, left, right):
        i = left - 1
        for j in range(left, right):
            if arr[j] <= arr[right]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i

    def QuickSort(self,arr, firstIndex, lastIndex):
        if firstIndex < lastIndex:
            divIndex = self.Partition(arr, firstIndex, lastIndex)

            self.QuickSort(arr, firstIndex, divIndex)
            self.QuickSort(arr, divIndex + 1, lastIndex)
        else:
            return

    def Partition(self,arr, firstIndex, lastIndex):
        i = firstIndex - 1
        for j in range(firstIndex, lastIndex):
            if arr[j] <= arr[lastIndex]:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[lastIndex] = arr[lastIndex], arr[i + 1]
        return i

    #前K个高频元素
    def topKFrequent(self, nums, k):
        pass
    #颜色分类
    def sortColors(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        



obj = PaiXu()
array = [1,4,5,2,3,8,6,7,9]
obj.quick_sort(array,0,len(array) - 1)
# obj.QuickSort(array,0,len(array)-1)
print(array)
