----------------------------------------------------------------------------
QUESTION
----------------------------------------------------------------------------

Description:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode
    
Example1:

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
    
Example2:

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

----------------------------------------------------------------------------
SOLUTION
----------------------------------------------------------------------------

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        ans = ""
        for s in strs:
            ans += str(len(s)) + '#' + s
        return ans

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        ans = []
        #for c in str:
        
        ch = 0
        while ch < len(str):

            i = ch
            no = ""
            while str[i] != "#":
                no += str[i]
                i += 1
            num = int(no)
            tempStr = str[i+1 : i+1+num]
            ans.append(tempStr)
            ch = i+1+num
        
        return ans
