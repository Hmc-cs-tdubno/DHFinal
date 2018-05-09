import sys
import os
import matplotlib.pyplot as plt
# import nltk
# from nltk.collocations import *
# othello_filter = lambda w: w.lower() in ['moor']
# bigram_measures = nltk.collocations.BigramAssocMeasures()
# trigram_measures = nltk.collocations.TrigramAssocMeasures()
# finder = nltk.collocations.BigramCollocationFinder.from_words(nltk.corpus.genesis.words("othello.txt"))
# #BigramCollocationFinder.from_words("abc def abc def eeee rrrr tttt yyyy uuuu iiii ooooo")#nltk.corpus.genesis.words('othello-tags.txt'))
# #print(finder)
# #print(finder.apply_word_filter(othello_filter))
# #print(finder.score_ngrams(bigram_measures.pmi)[0])  # doctest: +NORMALIZE_WHITESPACE
# bi_gram = finder.score_ngrams(bigram_measures.pmi)
# charactersFile='Oth_char.txt' 
# #Error check Characters file
# try: 
#     rawCharacters=open(charactersFile).read()
# except IOError: 
#     parser.error("Can't find Oth_char file. Do you have a characters.txt in this directory, or did you specify its location in an option?") 
# 
# 
# character_list = rawCharacters.upper().split(',')
# print(character_list)
# for character in character_list:
#     filename = character + '.txt'
#     f = open('Othello/' + filename, 'w+')
#     for i in bi_gram:
#         if character.upper() == (i[0][0]).upper() or character.upper() == (i[0][1]).upper():
#             f.write(str(i) +"\n")
#     f.close()
savedict={}
with open("../all-characters.txt","r") as f:
    chars = f.readlines();
    

def findchar(script):
    if(type(script)==str):
        sp=script.split()
    else:
        sp= [word for word in script]
        char =[word for word in sp if ((word.isupper()) and len(word)>1 and (word[-1].isalpha() and word[0].isalpha()))]
        final=[]
        for l in range(len(char)):
            if l==len(char)-1:
                final +=[char[l]]
            elif char[l+1]=="OF":
                final+=[char[l]+" "+char[l+1]+" "+char[l+2]]
                l+=2
            elif (char[l]=="LADY" or char[l]=="LORD"):
                final+=[char[l]+" "+char[l+1]]
                l+=1
            else:
                final+=[char[l]]
        print(list(set(final)))
    
def charstrip(filename):
    print(filename)
    frqdict={}
    with open(filename) as f:
        script=f.readlines()
    newpath = '../by_chars/'+filename+'/' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = '../by_chars/charts/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for char in chars:
        # print(char)
        char=char.rstrip()
        temp =[]
        written=False
        out = open('../by_chars/'+filename+'/'+char+'.txt', 'w+')
        write = False
        
        for line in script:
            words = line.split()
            if len(words)==0:
                pass    
            elif " ".join(words[0:len(char.split())])==char:
                line="bla "*len(char.split())+" ".join(words[len(char.split()):])
                write=True
                written=True
            elif words[0].isupper() and len(words[0])>1:
                write=False
            if(write):
                out.write(line+"\n")
                temp+=[len(line.split())]
            else:
                out.write("bla "*len(words)+"\n")
                temp+=[0]
        out.close()
        if(not written):
            os.remove('../by_chars/'+filename+'/'+char+'.txt')
        else:
            frqdict[char]=temp[:]
    x=len(frqdict)
    if x>0:    
        y=0
        z=0
        f, axarr = plt.subplots(x,sharex=True)
        plt.subplots_adjust(left=.16, bottom=None, right=.96, top=None, wspace=None, hspace=.01)
        print("done")
        for i in frqdict:
            cur =frqdict[i]
            axarr[y].plot(cur)
            axarr[y].set_yticks([])
            axarr[y].set_ylabel(i,fontsize=7,rotation=0,horizontalalignment='right')
            axarr[y].yaxis.set_label_coords(-0.01,-.35)
            z=len(cur)
            y+=1
        # plt.show()
        plt.savefig('../by_chars/charts/'+filename+'.pdf')
        plt.close()
    # 
def trial():
    for i in savedict:
        cur =savedict[i]
        axarr[y].plot(cur)
        axarr[y].set_yticks([])
        axarr[y].set_ylabel(i,rotation=0)
        axarr[y].yaxis.set_label_coords(0,0)
        z=len(cur)
        y+=1
    plt.show()
    
def main():
    # with open(sys.argv[1]) as f:
    #     scp = f.read().split()
    # # print(scp)
    # findchar(scp)
    for filename in os.listdir('.'):
        if(filename!="project.py"):
            charstrip(filename)

if __name__ == "__main__":
    main()