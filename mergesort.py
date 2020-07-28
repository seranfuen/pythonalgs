class MergeSort():
    
    def _merge(self, leftSide, rightSide):
        i = 0
        j = 0
        leftSideLength = len(leftSide)
        rightSideLength = len(rightSide)
        result = []
        for _ in range(0, leftSideLength + rightSideLength):
            if i < leftSideLength and (j >= rightSideLength or
            leftSide[i] < rightSide[j]):
                result.append(leftSide[i])
                i += 1
            elif j < rightSideLength:
                result.append(rightSide[j])
                j += 1
        return result
    
    
    def sort(self, toSort):
        if len(toSort) <= 1:
            return toSort
        leftSide = self.sort(toSort[len(toSort)//2:])
        rightSide = self.sort(toSort[:len(toSort)//2])
        return self._merge(leftSide, rightSide)