# Look out for intersections
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create position and speed pair arrays
        pair = [[p,s] for p, s in zip(position, speed)]

        stack = []
        # In reverse sorted order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            
            # Stack needs at least two cars to guarantee collision
            # and the top of the stack (that we just appended) will
            # reach the target position in equal or less time than the 
            # car that came before it means collision
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)