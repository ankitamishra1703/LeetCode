class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for j in range(len(t)):
            if i==len(s):
                return True
            else:
                if s[i] == t[j]:
                    i+=1
        return i==len(s)

        # def isSubsequence(s: str, t: str) -> bool:
    # Initialize pointer for s
    # i = 0

    # # Traverse through t
    # for j in range(len(t)):
    #     # If we found all characters in s
    #     if i == len(s):
    #         return True
    #     # If characters match, move pointer in s
    #     if s[i] == t[j]:
    #         i += 1

    # # Check if we found all characters
    # return i == len(s)