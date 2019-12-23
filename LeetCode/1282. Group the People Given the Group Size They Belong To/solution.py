'''
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 
'''

# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/



from collections import defaultdict
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        sizes = defaultdict(list)
        for index in range(0, len(groupSizes)):
            sizes[groupSizes[index]].append(index)
        
        answer = []
        
        for key, values in sizes.items():
            for index in range(0,len(values) ,key):
                answer.append(values[index:index+key])
        return answer