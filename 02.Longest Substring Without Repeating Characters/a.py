class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    max = len(s)
    count = 1
    subs = ""
    prev = s[0]
    big = 0
    maxsubs = ""

    for x in range(1, max):
        if prev == s[x]:
            subs = s[x]
            count = 1
        else:
            subs += s[x]
            count += 1

        big = count
        maxsubs = subs

    print(maxsubs)
    print(big)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
