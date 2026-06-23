class Solution:
    def decodeString(self, s: str) -> str:
        a = []
        x = 0
        while(x < len(s)):
            if s[x] != ']':
                a.append(s[x])
            else:
                temp=''
                while(a and a[-1]!='['):
                    temp += a[-1]
                    a.pop()
                if a and a[-1]=='[':
                    a.pop()
                
                temp=temp[::-1]
             
                num = ''
                while(a and a[-1].isdigit()):
                    num += a[-1]
                  
                    a.pop()

                num = int(num[::-1])
                a += num*temp

            
            
            x+=1

        return  ''.join(a)
                
