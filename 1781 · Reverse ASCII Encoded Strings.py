class Solution:
    """
    @param encodeString: an encode string
    @return: a reversed decoded string
    """
    def reverseAsciiEncodedString(self, encodeString):
        # Write your code here
        # 倒數兩位開始取，轉成 character
        if encodeString is None:
            return ""
        
        asciiNumber = 0
        reverseDecodedString = ""

        for i in range(len(encodeString)-1, 0, -2):
            asciiNumber = int(encodeString[i-1])*10 + int(encodeString[i])
            reverseDecodedString += chr(asciiNumber)

        return reverseDecodedString
