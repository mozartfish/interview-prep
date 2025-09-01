class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, left, mid, right):
            L = [0 for i in range(mid - left + 1)]
            R = [0 for i in range(right - mid)]

            for i in range(len(L)):
                L[i] = arr[left + i]
            for j in range(len(R)):
                R[j] = arr[mid + 1 + j]

            i = 0
            j = 0
            k = left

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

            return arr

        def mergeSort(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                mergeSort(arr, left, mid)
                mergeSort(arr, mid + 1, right)
                merge(arr, left, mid, right)

            return arr

        n = len(nums)
        return mergeSort(nums, 0, n - 1)
