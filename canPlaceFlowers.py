class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
         
        
        for i in range(len(flowerbed)):
            count=0
            if flowerbed[i-1] == 0 and flowerbed[i+1]==0:
                flowerbed[I] = 1
                count +=1
                if count >= n:
                    return True
        return False 
        