class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        lastWord = ""
        foundLastWord = False
        for i in range(len(A)-1, -1, -1):           
            if A[i] == " ":
                if foundLastWord==True:
                    return len(lastWord)
            else:
               foundLastWord = True
               lastWord += A[i]             
        
        return len(lastWord)