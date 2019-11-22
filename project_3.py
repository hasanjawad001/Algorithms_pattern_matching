
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

    def bm_horspool(self):
        t = self.t
        p = self.p
        n = len(t)
        m = len(p)

        i = 0
        for i in range(0, n - m):
            j = 0
            while (j < m and t[i + j] == p[j]):
                j = j + 1
                if j == m:
                    return i
        return -1


if __name__=='__main__':
    text = 'abc abcdab abcdabcdabde'
    pattern = 'abcdabd'
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
