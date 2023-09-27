class Solution:
    def __init__(self, s, t):
        self.s = s
        self.t = t 


    def find_difference(self):
        s_count = {}
        t_count = {}

        for char in self.s:
            s_count[char] = s_count.get(char, 0)+1
        
        
        for char in self.t:
            t_count[char] = t_count.get(char, 0)+1

        for char , count in t_count.items():
            if char not in s_count or count>s_count[char]:
                return char
    


        



s = Solution('abcd', 'abcde')
print(s.find_difference())