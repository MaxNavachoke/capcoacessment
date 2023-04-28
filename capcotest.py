
def solution(nums,target):  
        length = len(nums)  
        tar = target  
        for i in range(length-1):  
            for j in range(i+1, length):  
                if nums[i]+nums[j] == tar:  
                    new_list = i, j  
                    return new_list[0]+new_list[1]  
        return 1  
  
nums = [1, 2, 4, 5, 11]  
target = 6
solution(nums,target)