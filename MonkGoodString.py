"""
Little Monk and Good String

Little monk loves good string. Good String is a string that only contains vowels . Now, his teacher gave him a string S. Little monk is wondering what is the length of the longest good string which is a substring of S.

Note: Strings contains only lower case English Alphabets.

Input:
First line contains a string S, (1 <= |S| <= 10^5) , where S denotes the length of the string.

Output:
Print an integer denoting the length of the longest good substring, that is substring consists of only vowels.

"""

def GoodString(string, vowels):
    string = string.lower()
    print(string)
    Length = 0
    l = 0
    for i in string:
        if i in vowels:
            Length +=1
            if Length>l:
                l = Length
        else:
            Length = 0
    return l
    
    
    
S = input()

vowels = 'aeiou'

result = GoodString(S, vowels)
print(result)