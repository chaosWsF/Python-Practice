class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(set(s)) <= 2:
            return len(set(s))
        else:
            result = len(s)
            s_list = [s]
            for _ in range(len(s)):
                if not decideLoop(s_list, result):
                    result -= 1
                    s_list = [s[i:i+result] for i in range(len(s)-result+1)]
                else:
                    result = decideLoop(s_list, result)
                    break
            
            return result


def decideLoop(strList, result):
    for s in strList:
        if len(set(s)) != result:
            continue
        else:
            return len(set(s))
    
    return False

if __name__ == '__main__':
    # input1 = 'abcabcbb'
    # input1 = 'bbbbb'
    # input1 = 'pwwkew'
    # input1 = 'abaababa'
    # input1 = ''
    input1 = ''
    sol = Solution()
    print(sol.lengthOfLongestSubstring(input1))