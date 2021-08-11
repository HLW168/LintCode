class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        # write your code here
        path_list, res_path = path.split("/"), []
        for p in path_list:
            if p == "." or p =="":
                continue
            elif res_path and p == "..":
                res_path.pop()
            elif p != "..":
                res_path.append("/" + p)
        if not res_path:
            return "/"
        return "".join(res_path)
