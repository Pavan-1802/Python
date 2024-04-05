with open('story.txt','r') as f:
    story=f.read()

words=set()
start_of_word=-1
target_start='<'
target_end='>'

for i,char in enumerate(story):
    if char==target_start:
        start_of_word=i
    if char==target_end and start_of_word!=-1:
        words.add(story[start_of_word:i+1])

answers={}

for i in words:
    replacement=input("Enter a replacement for "+i+" ")
    answers[i]=replacement

for i in answers:
    story=story.replace(i,answers[i])

print(story)