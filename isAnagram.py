def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sCount = Counter(s)
        tCount = Counter(t)
        if(len(s) > len(t)):
            for value, occ in sCount.items():    
                if value not in tCount:
                    return False
                elif tCount.get(value) != occ:
                    return False
        else:
            for value, occ in tCount.items():    
                if value not in sCount:
                    return False
                elif sCount.get(value) != occ:
                    return False
        return True