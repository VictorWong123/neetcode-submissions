class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0 

        for i in range(len(digits)-1,-1,-1):
            print(digits)
            if carry >0:
                if digits[i] +1>=10:
                    digits[i] = (digits[i] +1)%10
                    carry = 1 
                else:
                    digits[i]+=1
                    carry = 0 

            if i == len(digits)-1:
                if digits[i] +1>=10:
                    digits[i] = (digits[i] +1)%10
                    carry = 1 
                else:
                    digits[i]+=1
                    carry = 0 
        if carry>0:
            digits.insert(0,1)

        return digits
                
