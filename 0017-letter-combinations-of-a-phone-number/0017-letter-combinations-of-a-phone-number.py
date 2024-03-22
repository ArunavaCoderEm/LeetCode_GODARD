from itertools import product

def gen_per(word_list):
    char_lists = [list(word) for word in word_list]
    combinations = product(*char_lists)
    permutations = [''.join(combination) for combination in combinations]
    return permutations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) == 0): return []
        dig = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        for i in digits:
            if(i in dig.keys()):
                res.append(dig[i])
        fin_res = list(gen_per(res))
        return fin_res