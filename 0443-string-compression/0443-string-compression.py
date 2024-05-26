class Solution:
    ## this silly problem took me 20 mins just because I forgot dictionaries
    ## can't have duplicate keys !!!!! NICEEEEEEE
    def compress(self, chars: List[str]) -> int:
        c = {}
        count = 1
        i = 0
        while (i < len(chars) - 1):
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                c[f"{chars[i]}{i}"] = count
                count = 1
            i += 1      
        c[chars[i]] = count   
        chars.clear()   
        print(c)
        for k, m in c.items():
            chars.append(k[0])
            if (m > 1):
                for digit in str(m):
                    chars.append(digit)    
        return len(chars)