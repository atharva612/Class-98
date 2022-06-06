from importlib.machinery import WindowsRegistryFinder


def wordCountFromFile():
    filename=input("enter file name")
    file=open(filename,'r')
    wordcount=0
    for line in file:
        word=line.split()
        wordcount=wordcount+len(word)

    print('no of words: ')
    print(wordcount)

wordCountFromFile()        

