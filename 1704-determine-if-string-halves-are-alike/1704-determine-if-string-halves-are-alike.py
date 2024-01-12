class Solution(object):
    def halvesAreAlike(self, s):
        l = ['a','e','i','o','u','A',"E","I","O","U"]
        count1 = 0
        count2 = 0
        a = s[0:len(s)//2]
        b = s[len(s)//2:len(s)]
        for i,j in zip(a,b):
            if (i in l):
                count1+=1
            if (j in l):
                count2+=1   
        return count2==count1
        