    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        if("IV" in s):
            occ = s.count("IV")
            val+=(4*occ);
            s = s.replace("IV","");
            
        if("IX" in s):
            occ = s.count("IX")
            val+=(9*occ);
            s = s.replace("IX","");
            
        if("XL" in s):
            occ = s.count("XL")
            val+=(40*occ);
            s = s.replace("XL","");
            
        if("XC" in s):
            occ = s.count("XC")
            val+=(90*occ);
            s = s.replace("XC","");
            
        if("CD" in s):
            occ = s.count("CD")
            val+=(400*occ);
            s = s.replace("CD","");
            
        if("CM" in s):
            occ = s.count("CM")
            val+=(900*occ);
            s = s.replace("CM","");
            
        romanChars = list(s)
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for value in romanChars:
            val+= d.get(value)
        return val