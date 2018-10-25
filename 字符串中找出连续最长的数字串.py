


#s = raw_input()
s = 'abcd12345ed125ss123456789'

ok = ''
res = 0 
left = 0 
start = 0
while left < len(s):
    if '0' <= s[left] <= '9':
        if res == 0:
            start = left
        res += 1
    else:
        if res > len(ok):
            ok = s[start:start + res]
        res = 0
    left += 1

if res != 0:
    print s[start:start+res] if res > len(ok) else ok
