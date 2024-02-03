class Solution(object):

    def getUnique(self, x):
        for i in range(1, len(x) + 1):
            unq = x[:i]
            if x == unq * (len(x) // len(unq)):
                return unq

    def getGreatestDivisor(self, ss, bs):
        ss_copy = ss
        unq = "".join(self.getUnique(ss))
        while len(ss) > len(unq):
            if bs == ss * (len(bs) // len(ss)) and ss_copy == ss * (len(ss_copy) // len(ss)):
                return ss
            ss = ss.replace(unq,"", 1)
        return unq

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if (set(str1) != set(str2)) or (str1+str2 != str2+str1):
            return ""

        if len(str1)>len(str2):
            if str2 not in str1:
                return ""
            if str1.replace(str2, "")=="":
                return str2
            else:
                return self.getGreatestDivisor(str2, str1)

        else:
            if str1 not in str2:
                return ""
            if str2.replace(str1, "")=="":
                return str1
            else:
                return self.getGreatestDivisor(str1, str2)

