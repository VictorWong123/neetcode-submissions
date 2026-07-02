class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        translator = str.maketrans('', '', string.punctuation)

        s = s.strip("?").lower().replace(" ","")
        s = s.translate(translator)

        st = s[::-1]

        print(st)
        print(s)
        return st==s