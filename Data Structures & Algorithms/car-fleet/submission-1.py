class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(position)

        for i in range(n):
            stack.append((position[i], speed[i]))

        stack.sort()
        car, spd = stack.pop() 
        remaining_miles_of_leading_car = (target - car) / spd
        count = 1
        print(stack)
        while stack:
            car, spd = stack.pop() 
            remaining_miles_of_following_cars = (target - car) / spd
            if remaining_miles_of_leading_car < remaining_miles_of_following_cars:
                count += 1
                remaining_miles_of_leading_car = remaining_miles_of_following_cars
        return count
            
        
            
