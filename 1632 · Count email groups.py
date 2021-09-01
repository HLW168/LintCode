class Solution:
    """
    @param emails: Original email
    @return: Return the count of groups which has more than one email address in it.
    """
    def countGroups(self, emails):
        # Write your code here
        groups = {}
        count = 0
        for email in emails:
            processed_email = self.process(email)
            print(processed_email)
            if processed_email in groups:
                if groups[processed_email] == 1:
                    count += 1
                    groups[processed_email] += 1
            else:
                groups[processed_email] = 1
        return count
            

    def process(self, email):
        email = list(email)
        # 初始化
        before_at = True
        c = 0
        plus = False
        res = []

        while c < len(email):
            if email[c] == '@':
                # 表示後面的字符都是在 ＠ 之後
                before_at = False
                plus = False
                res.append(email[c])
                c += 1
                continue
            if email[c] == '.' and before_at:
                # 不需要 append 跳過即可
                c += 1
                continue
            if email[c] == '+' and before_at:
                plus = True
                c += 1
                continue
            if plus: # 加號後面的
                # c 往前走就好了
                c += 1
                continue
            
            res.append(email[c])
            c += 1

        return "".join(res)
