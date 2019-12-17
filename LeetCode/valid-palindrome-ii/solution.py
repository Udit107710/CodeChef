class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list(s)
        front = 0
        end = len(l) - 1
        count = 0
        flag = False
        print(l, s)
        while(front<end):
            print(l[front], l[end])
            if l[front] == l[end]:
                front+=1
                end-=1
            elif l[front+1] == l[end]:
                front+=1
                count+=1
            elif l[end-1] == l[front]:
                end-=1
                count+=1
            else:
                flag = True
                break
        if flag:
            return False
        else:
            return True

print(Solution().validPalindrome("abca"))