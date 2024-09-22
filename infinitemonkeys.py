import random
def generate1(strlen):
    alphabet="abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res =res + alphabet[random.randrange(27)]
    return res
print(generate1(28))

def score(goal,testString):
    numsame=0
    for i in range(len(goal)):
        if goal[i]==testString[i]:
            numsame=numsame+i
    return numsame/len(goal)
def main():
    goalString='methinks it is like a weasel'
    newString=generate1(28)
    best=0
    newscore=score(goalString,newString)
    while newscore<1:
        if newscore>best:
            print(newscore,newString)
            best=newscore
        newString=generate1(28)
        newscore=score(goalString,newString)
main()