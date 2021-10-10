# by using technique "two pointers"
# time complexity is O(n), where n is length of given string
# space complexity is O(n), where n is length of given string
s = input()
l = mx = cnt = 0
my_dict = {}
for i in range(len(s)):
    if s[i] not in my_dict:
        my_dict[s[i]] = 1
    else:
        my_dict[s[i]] += 1
    cnt += 1
    while my_dict[s[i]] == 2:
        my_dict[s[l]] -= 1
        l += 1
        cnt -= 1
    mx = max( mx, cnt )
print(mx)
