def count_vowels(s):
    vowels ="aieouAIEOU"
    count = 0
    for i in s:
        if i in vowels:
            count+=1
    return count    
    
    
s = "hello world"

print(count_vowels(s))

    