class Solution:
    def maxArea(height):
        best_area = 0            
        begin = 0
        end = len(height) - 1
            
        while end > begin:
            breadth = end - begin
            length = min(height[begin],height[end])
            area = length * breadth
            if area > best_area:
                best_area = area
            if height[end] > height[begin]:
                begin+=1
            else:
                end-=1
        return best_area

sol = Solution
print("Container with most water = {}" .format(sol.maxArea([1,1])))