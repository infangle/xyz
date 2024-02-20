class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billc = [0]*3 #number of each type of bill
        for bill in bills:
            if bill == 5:
                billc[0] += 1
            elif bill == 10:
                if billc[0] > 0:
                    billc[0] -= 1
                    billc[1] += 1
                else:
                    return False
            elif bill == 20:
                if billc[0] > 0 and billc[1] > 0:
                    billc[0] -= 1
                    billc[1] -= 1
                    billc[2] += 1
                elif billc[0] >= 3:
                    billc[0] -= 3
                    billc[2] += 1
                else:
                    return False
        return True