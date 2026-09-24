'''
Write a program to check the given string is palindrom or not
'''
def isPalindrome(phrase):
  s1= phrase.lower().replace(' ','').replace('.','') # make string to lowercase and replace spaces and .,! 
  if s1==s1[::-1]:          # do string scling and string compare
      return True           # If palindrome then return true
  else:
      return False          # else palindrome then return False
  
print(isPalindrome('Taco cat.'))
