class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.split(' ')
        print(last_word)
        l = len(last_word)
        for i in range(l):
            if last_word[l-i-1]!='':
                return len(last_word[l-i-1])
        else:
            return 0