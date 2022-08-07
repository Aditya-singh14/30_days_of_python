sentence=input("Enter a sentence : ")
new_sentence=sentence.split()

for i in new_sentence:
    rev=new_sentence[::-1]
print(' '.join(rev))
    