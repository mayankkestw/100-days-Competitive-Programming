
"""
Monk Teaches Palindrome

Monk introduces the concept of palindrome saying,"A palindrome is a sequence of characters which reads the same backward or forward." 
Now, since he loves things to be binary, he asks you to find whether the given string is palindrome or not. If a given string is palindrome, you need to state that it is even palindrome (palindrome with even length) or odd palindrome (palindrome with odd length).

Input:
The first line consists of T, denoting the number of test cases.
Next follow T lines, each line consisting of a string of lowercase English alphabets.

Output:
For each string , you need to find whether it is palindrome or not.
If it is not a palindrome, print NO.
If it is a palindrome, print YES followed by a space; then print EVEN it is an even palindrome else print ODD.
Output for each string should be in a separate line.

"""
def Palindrome(string):
    if string == string[::-1]:
        YesNo = "YES"
        if len(string)%2 ==0:
            EvenOdd = "EVEN"
        else:
            EvenOdd = "ODD"
        return YesNo, EvenOdd
    else:
        YesNo = "NO"
        EvenOdd = None
        return YesNo, EvenOdd
    
    
    
T = int(input())
for i in range(T):
    s = str(input())
    YesNo, EvenOdd = Palindrome(s)
    if EvenOdd!=None:    
        print(YesNo, EvenOdd)
    else:
        print(YesNo)
