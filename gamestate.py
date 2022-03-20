###########################################
#  This is the Gamestate class
#  This class maintains the "current state of play" during a game
###########################################

from numpy import random
import numpy as np

# NOTE: common word list source is https://7esl.com/5-letter-words/ 


class Gamestate():
 
    def init(self):
        self.guesses = []
        self.results = []
        
        wordlistfilename = 'commonwords.txt'
        wordlist = []
        with open(wordlistfilename) as f:
            for line in f:
                word = line.strip()
                wordlist.append(word)
        randint = np.random.randint(len(wordlist))
        
        self.targetword = wordlist[randint].upper()
        #print('targetword is ', self.targetword)   # <<<---- debugging purposes only!!!!!
    def add_guess(self,string):
        string = string.upper()
        if( not string.isalpha()):
            print('ERROR: string contains non-alphabetic characters')
        elif( len(string) != 5):
            print('ERROR: string is not a five letter word')
        else:
            self.guesses.append(string)
            self.results.append(self.compute_colours(string))
            
    # example: compute_colours('alpha','black') == ['y','g','b','b','b']
    def compute_colours(self, string):
    
        # STAGE 1: work out the correct colours
        result = list('bbbbb')
        temp1 = list(string)
        temp2 = list(self.targetword) 
        for i in range(5):
            if(temp1[i] == temp2[i]):
                result[i] = 'g'
                temp1[i] = '-'
                temp2[i] = '-'        
        for i in range(5):
            if(temp1[i] != '-'):
                for j in range(5):
                    if( temp2[j] == temp1[i]):
                        temp1[i] = '-'
                        temp2[j] = '-'
                        result[i] = 'y'
                        
        # STAGE 2: now make one random blob an impostor :-)                
        foo = np.random.randint(5)
        impostor = result[foo]
        while( impostor == result[foo]):
            impostor = random.choice(['b','g','y'])
        result[foo] = impostor 
        
        return result   # return a list of characters! 