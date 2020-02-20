class Solution:
    def lengthOfLongestSubstring(self, s):
        if uniqueOrder(s) in s:
            return len(set(s))
        else:
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


def uniqueOrder(s):
    seen = {}
    ss_list = []
    for ss in s:
        if ss in seen:
            continue
        seen[ss] = 1
        ss_list.append(ss)

    return ''.join(ss_list)


def decideLoop(strList, result):
    for s in strList:
        if len(set(s)) != result:
            continue
        else:
            return len(set(s))
    
    return False

# =============================================================
# class Solution:
#     # @return an integer
#     def lengthOfLongestSubstring(self, s):
#         start = maxLength = 0
#         usedChar = {}
        
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)

#             usedChar[s[i]] = i

#         return maxLength
# =============================================================