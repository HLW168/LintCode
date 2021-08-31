class Solution:
    """
    @param target: the target
    @param position: the initial position
    @param speed: the speed
    @return: How many car fleets will arrive at the destination
    """
    def carFleet(self, target, position, speed):
        # Write your code here
        time=[float(target-p)/s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res
