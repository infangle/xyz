class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def calc(i):
            if i == 0:
                return [1]  

            prev_row = calc(i - 1)  
            curr_row = [1]  
            for j in range(1, i):
                curr_row.append(prev_row[j - 1] + prev_row[j])

            curr_row.append(1)  
            return curr_row

        return calc(rowIndex)
