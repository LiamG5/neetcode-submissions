# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        
        # An empty list or a single-element list requires no sorting iterations
        if not pairs:
            return ans

        # Insertion Sort Algorithm
        for i in range(len(pairs)):
            j = i
            # Move the element backwards until it finds its correct sorted position
            # Using '>' ensures stable sorting (equal keys maintain original order)
            while j > 0 and pairs[j - 1].key > pairs[j].key:
                # Swap elements
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1
            
            # Append a copy of the current state of the array
            ans.append(list(pairs))
            
        return ans

            

        
            
                    

            






        