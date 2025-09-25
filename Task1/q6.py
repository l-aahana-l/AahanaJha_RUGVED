def isAnagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return sorted(str1) == sorted(str2)
string1=input("String 1:")
string2=input("String 2:")
print("The strings are an anagram" if isAnagram(string1,string2)==True else "The Strings are not an anagram")
