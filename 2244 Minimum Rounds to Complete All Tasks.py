from collections import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        freq = Counter(tasks)
        freq = sorted(freq.items())
        cnt = 0

        for p in freq:
            if p[1] == 1:
                return -1
            elif p[1] % 3 == 0:
                cnt += p[1] // 3
            else: 
                cnt += p[1] // 3 + 1
        return cnt
      
