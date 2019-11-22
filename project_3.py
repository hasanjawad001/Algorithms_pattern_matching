
class PM:
    def __init__(self, t, p):
        self.t = t
        self.p = p

    def brute_force(self):
        t=self.t
        p=self.p
        n=len(t)
        m=len(p)

        i=0
        for i in range(0, n-m):
            j = 0
            while(j<m and t[i+j]==p[j]):
                j=j+1
                if j==m:
                    return i
        return -1

    def failure_function(self,p):
        f=[]
        m=len(p)
        for i in p:
            f.append(0)
        l = 0
        i = 1
        while i < m:
            if p[i] == p[l]:
                l += 1
                f[i] = l
                i += 1
            else:
                if l != 0:
                    l = f[l - 1]
                else:
                    f[i] = 0
                    i += 1
        return f

    def kmp(self):
        t=self.t
        p=self.p
        n=len(t)
        m=len(p)

        f = self.failure_function(p)

        i=0
        j=0
        while(i<n):
            if t[i]==p[j]:
                if j==m-1:
                    return i-j
                else:
                    i+=1
                    j+=1
            else:
                if j==0:
                    i+=1
                else:
                    j=f[j-1]
        return -1

    def shift_table(self,p):
        m=len(p)
        st = {
            'def': m
        }
        for i in range(m-1):
            st[p[i]] = m-i-1
        return st

    def shift_value(self, st, c):
        if c in st.keys():
            return st[c]
        else:
            return st['def']

    def bm_horspool(self):
        t = self.t
        p = self.p
        n = len(t)
        m = len(p)

        st = self.shift_table(p)
        i=m-1
        while(i<=n-1):
            k=0
            while(k<=m-1 and p[m-1-k]==t[i-k]):
                k=k+1
            if (k==m):
                return i-m+1
            else:
                i = i + self.shift_value(st,t[i])
        return -1


if __name__=='__main__':
    text = 'jim saw me in a barbershop'
    pattern = 'barber'
    pm=PM(text, pattern)

    # brute force
    i=pm.brute_force()
    print('Brute-force (matched at) index: %s.'%(i))

    # bm horspool
    i = pm.bm_horspool()
    print('BM Horspool (matched at) index: %s.'%(i))

    # kmp
    i=pm.kmp()
    print('KMP (matched at) index: %s.'%(i))
