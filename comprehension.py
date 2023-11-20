#list1=[2,-3,-2,5,6]
#list2=[i for i in list1 if(i>0)]
#print(f"positive list={list2}")
#list1=[1,2,3,4,5,6]
#list2=[i**2 for i in list1]
#print(f"square list={list2}")
#word=input("enter the word;")
#listvowel=[i for i in word if i in 'aeiouAEIOU']
#print(f"vowels are {listvowel}")
#w=input("enter any character:")
#listordinals=[ord(i) for i in w]
#print(listordinals)
s=input("enter a sentence:");
print(s)
wordslist=s.split()
print(wordslist)
for i in wordslist:
    print(f"{i} occurs {wordslist.count(i)} times")
