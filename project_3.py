
class PM:
    def __init__(self, t, p):
        self.t = t
        self.p = p

    def brute_force(self):
        t=self.t
        p=self.p
        n=len(t)
        m=len(p)

        nc=0
        i=0
        for i in range(0, n-m+1):
            j = 0
            while(j<m and t[i+j]==p[j]):
                nc+=1
                j=j+1
                if j==m:
                    return i, nc
            nc+=1
        return -1, nc

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

        nc=0
        i=0
        j=0
        while(i<n):
            if t[i]==p[j]:
                nc += 1
                if j==m-1:
                    return i-j, nc
                else:
                    i+=1
                    j+=1
            else:
                nc += 1
                if j==0:
                    i+=1
                else:
                    j=f[j-1]
        return -1, nc

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

        nc=0
        st = self.shift_table(p)
        i=m-1
        while(i<=n-1):
            k=0
            while(k<=m-1 and p[m-1-k]==t[i-k]):
                nc+=1
                k=k+1
            if (k==m):
                return i-m+1, nc
            else:
                i = i + self.shift_value(st,t[i])
            nc+=1
        return -1, nc


if __name__=='__main__':
    from pprint import pprint
    experiment_log = {}
    experiment_list = \
    [
        ('barber', 'jim saw me in a barbershop'),
        ('fox', 'the quick fox jumps over the lazy dog'),
        ('abcdabd', 'abc abcdab abcdabcdabde'),
        ('needle', 'findinahaystackneedleina'),
        ('baobab', 'bird loved bananas'),
        ('baobab', 'bess knew about baobabs'),
        ('country', 'i am in a new country'),
        ('student', 'this is algorithm class'),
        ('present', 'this pattern is present here'),
        ('absent', 'this pattern is not present here')
    ]
    for i in range(len(experiment_list)):
        print('#######################################################################################################')
        e=experiment_list[i]
        pattern = e[0]
        text = e[1]
        print('EXPERIMENT NO ===> %s'%(str(i+1)))
        print('PATTERN ===> %s'%(pattern))
        print('TEXT ===> %s'%(text))
        # pattern matcher
        pm=PM(text, pattern)
        # brute force
        ibf, nbf=pm.brute_force()
        print('Brute-force (matched at) index: %s.'%(ibf))
        # bm horspool
        ibmh, nbmh = pm.bm_horspool()
        print('BM Horspool (matched at) index: %s.'%(ibmh))
        # kmp
        ikmp, nkmp=pm.kmp()
        print('KMP (matched at) index: %s.'%(ikmp))
        log = {
            'Brute-force': nbf,
            'BM Horspool': nbmh,
            'KMP': nkmp
        }
        experiment_log[str(i+1)]=log
        print('#######################################################################################################')
    print()
    print()
    print('<=== TABLE (EXPERIMENT) ===>')
    pprint(experiment_log)