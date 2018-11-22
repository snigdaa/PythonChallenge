import re

filename = open("paragraph.txt", 'r')
paragraph = filename.read()
filename.close()
#print(paragraph)
#paragraph = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword " \
#            "point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And " \
#            "the King saw, he knew not how, something new and overwhelming. The great green trees and the great red " \
#            "robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him " \
#            "and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his " \
#            "rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of " \
#            "black upon a world of crimson and gold."

splitted = re.split("(?<=[.!?]) +", paragraph)
lettercounter = 0
lettercountlist = []
wordcount = 0
wordcountlist = []
sentencecount = len(splitted)
letterslist = []

for sentence in splitted:
    words = sentence.split(" ")
    wordcount += len(words)
    #print(wordcount)
    wordcountlist.append(len(words))
    #print(words)
    for word in words:
        #print(word)
        for char in word:
            lettercounter += 1
        lettercountlist.append(lettercounter)
        lettercounter = 0
lettersperword = round((sum(lettercountlist)/wordcount),1)
wordspersentence = round((sum(wordcountlist)/sentencecount),1)

writefile = open("PyParaAnalysis.txt", 'w')
print("Paragraph Analysis\n ----------------")
writefile.write("Paragraph Analysis\n ----------------\n")
print(f"Approximate Word Count: {wordcount}")
writefile.write(f"Approximate Word Count: {wordcount}\n")
print(f"Approximate Sentence Count: {sentencecount}")
writefile.write(f"Approximate Sentence Count: {sentencecount}\n")
print(f"Average Letter Count: {lettersperword}")
writefile.write(f"Average Letter Count: {lettersperword}\n")
print(f"Average Sentence Length: {wordspersentence}")
writefile.write(f"Average Sentence Length: {wordspersentence}")
