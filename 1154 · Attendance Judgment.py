class Solution:
    """
    @param record: Attendance record.
    @return: If the student should be punished return true, else return false. 
    """
    def judge(self, record: str) -> bool:
        # Write your code here.
        n = len(record)

        # 紀錄連續遲到次數
        maxL = countL = 1

        # 紀錄缺勤次數
        countD = 0

        for i in range(n):
            if record[i] == 'D':
                countD += 1
            elif record[i] == 'L':
                if i < n-1 and record[i] == record[i+1]:
                    countL += 1
                    maxL = max(maxL, countL)
                else:
                    # 重新紀錄
                    countL = 1
        if maxL >= 3 or countD >= 2:
            return True
        
        return False
