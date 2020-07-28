from random import seed
from random import randint

class QuickSort():
    def sort(self, arr):
        seed(1)
        self._sort(arr, 0, len(arr))
        return arr
    
    def _sort(self, arr, start, end):
        if end - start <= 1:
            return
        
        # Put pivot at the beginning of (sub)array
        pivot = randint(start, end - 1)
        pivotValue = arr[pivot]
        arr[pivot] = arr[start]
        arr[start] = pivotValue
        
        nextPositionLargerPivot = start + 1
        # after pivot, analyze every single element
        # if it's smaller or equal to pivot value, put 
        # it at nextPositionLargerPivot and increase it
        # otherwise do nothing
        for i in range(start + 1, end):
            if arr[i] <= pivotValue:
                aux = arr[nextPositionLargerPivot]
                arr[nextPositionLargerPivot] = arr[i]
                arr[i] = aux
                nextPositionLargerPivot += 1
        
        # Place pivot in correct position
        aux = arr[nextPositionLargerPivot-1]
        arr[nextPositionLargerPivot-1] = pivotValue                
        arr[start] = aux
        
        # Recurse by sorting both halves
        self._sort(arr, start, nextPositionLargerPivot - 1)
        self._sort(arr, nextPositionLargerPivot, end) 