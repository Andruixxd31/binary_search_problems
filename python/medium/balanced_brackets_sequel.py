class Solution:
    def solve(self, s):
        st = []
        op = ["(","[","{"]
        cl = [")","]","}"]
        for c in s:
            if c in op: st.append(c)
            elif len(st) > 0:
                if cl.index(c) == op.index(st[-1]):
                    st.pop()
                else: break
            else: return False
        return True if len(st) == 0 else False
