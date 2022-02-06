with open('final.txt', 'r') as f: #open the file
    wordList = f.readlines() #put the lines to a variable (list).

puzzle = "ENCDTONER"
letter = "T"
answers = []

for word in wordList:
    temppuzzle = puzzle
    word=word[:-1]
    valid = True
    if (letter in word):
        for i in word:
            if i in temppuzzle:
                temppuzzle = temppuzzle.replace(str(i),"0",1)
            else:
                valid = False
                break;
        if valid:
            answers.append(word)
print(answers)

# for i in range(10):
#     for word in wordList:
#         word=word[:-1]
#         if len(word) == 10-i:
#             answers.append(word)

# with open('final.txt', 'w') as f:
#     for item in answers:
#         f.write("%s\n" % item)