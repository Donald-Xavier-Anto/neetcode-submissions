class Solution:
    def isValid(self, s: str) -> bool:
        def match(s, t):
            if s=='{' and t=='}':
                return True
            if s=='[' and t==']':
                return True
            if s=='(' and t==')':
                return True
            return False
        st = []
        for i in s:
            if i in ['{', '[', '(']:
                st.append(i)
            else:
                if len(st)>0 and match(st[len(st)-1],i):
                    st.pop()
                else:
                    return False
        if len(st)>0:
            return False
        return True 
        