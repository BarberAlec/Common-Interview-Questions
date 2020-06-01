
class palindrome:
    def check4Palindrome(self,st):
        bw_st = st[::-1]
        return st == bw_st

    def palindromeSimple(self,st):
        l =len(st)
        for i in range(l//2):
            if st[i] != st[-(i+1)]:
                return False
        return True


sol = palindrome()
print(sol.check4Palindrome('thissiht'))
print(sol.palindromeSimple('thissiht'))



# Reverse linked list
# reverse a string recurisvely and iteratively