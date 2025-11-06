class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        count = 0
        print("Im here")
        if count >= n:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                print("Found flower")
                prev = 1
            elif i == len(flowerbed)-1:
                print("Reached end")
                if prev ==0 and count+1 >=n:
                    return True
                return False
            elif flowerbed[i+1]==0:
                if flowerbed[i] == 0 and prev == 0:        
                    prev = 1
                    count +=1
                    print("Found space count =",count)
                    if count >= n:
                        return True
                else:
                    prev = 0
        return False 
        