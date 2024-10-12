## yesterday similar

def extract_all (arr):
    st = []
    en = []

    for i in arr:
        st.append(i[0])
        en.append(i[1])

    return (st, en)

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        st, en = extract_all(intervals)

        st.sort()
        en.sort()

        no_of_groups, ends = 0, 0

        for i in range (len(en)):
            if(st[i] > en[ends]): ends += 1
            else: no_of_groups += 1
        
        return no_of_groups