
"""
Imports OS, NLTK packages, modules and SQLLite
"""
import os #import os for normal use
import nltk #import nltk package to do the word analysis
from nltk.corpus import stopwords #import the stopwords (will be installed in the class wordanalysis)
from nltk.tokenize import word_tokenize #import the word_tokenize (will be installed in the class wordanalysis)
from nltk.stem.wordnet import WordNetLemmatizer #import the WordNetLemmatizer (will be installed in the class wordanalysis)

import string
from collections import Counter #import collections package to count the words

'''
This class does the word analysis, including writing, analysing and deleting the txt.
'''
class WordAnalysis:#Created the class.
    
    pn = os.path.abspath(__file__) # pn is now the path of this file, which is a string
    path = pn.split("word_analysis")[0] #'path' gets the upper directory
    
    
    #standard stop words obtained from nltk
    stops = set(stopwords.words('english'))
    
    #excluded items should include punctuation
    exclude = set(string.punctuation)
    
    #lemmatize the words and return the base of the word
    lemma = WordNetLemmatizer()
    
    '''
    This method is for cleaning a document (text) by removing stop words, punctuations and normalizing words.
    
    @param doc the document (or list of words) to clean up
    @return normalized - a normalized text that is cleaned
    '''
    def clean(self,doc):

        #removes the stop words
        stop_free= "".join([i for i in doc.split() if i not in self.stops])
        
        #removes punctuations
        punc_free = "".join(ch for ch in stop_free if ch not in self.exclude)
        
        #lemmatizes the words
        normalized = "".join(self.lemma.lemmatize(word) for word in punc_free)
        
        return normalized
                
    '''
    This method runs the cleaning by first getting the document from the full document.
    The method takes a document(text) and calls the clean method.
    @param doc_complete the complete set of documents
    '''    
    def runClean(self,doc_complete):
        
        #document from set of documents to be cleaned
        doc_clean = [self.clean(doc) for doc in doc_complete] 
        
        return doc_clean
        
    '''
    This function is the main function of word analysis.
    It Tokenizes, Cleans and returns the most used word in the document
    @param self, the method itself.
    @return none
    '''
    def word_count(self, filename):
        
        #opens and reads the pinlc.txt
         
        f = open(os.path.join(self.path,'data',filename), 'r')
        
        #stores the content to 'text'
        text=f.read()
        
        #text is now all in lowercase
        text = text.lower()
        
        #document is split into individual words
        toctext = word_tokenize(text)
        
        #initiates the class WordAnalysis, running the constructors
        wc = WordAnalysis()
        
        #runs the runClean method with toctext
        clean_text = wc.runClean(toctext)
        
        #removes '' from clean_text.
        while '' in clean_text: clean_text.remove('')
        
        #runs the Counter function to return the most used word
        count = Counter(clean_text)
        
        print("The fifty most used words in " + filename + " are:")
        print(count.most_common(50))
        
        
           
            