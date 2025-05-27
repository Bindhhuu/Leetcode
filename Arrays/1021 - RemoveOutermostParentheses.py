class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        st = []
        for j in s:
            if j == "(":
                if i > 0:
                    st.append(j)
                i += 1
            else:
                i -= 1
                if i > 0:
                    st.append(j)
        return ''.join(st)
                        
