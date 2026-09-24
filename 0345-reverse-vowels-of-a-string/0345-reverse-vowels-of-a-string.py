class Solution:

    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l=len(s)
        x=0
        y=l-1
        while x<y:
            if s[x]=='a' or s[x]=='e' or s[x]=='i' or s[x]=='o' or s[x]=='u' or \
               s[x]=='A' or s[x]=='E' or s[x]=='I' or s[x]=='O' or s[x]=='U':

                if s[y]=='a' or s[y]=='e' or s[y]=='i' or s[y]=='o' or s[y]=='u' or \
                   s[y]=='A' or s[y]=='E' or s[y]=='I' or s[y]=='O' or s[y]=='U':
                    a=s[y]
                    s[y]=s[x]
                    s[x]=a
                    x+=1
                    y-=1
                else:
                    y-=1
            else:
                x+=1
        return ''.join(s)