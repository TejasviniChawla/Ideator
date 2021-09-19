# -*- coding: utf-8 -*-
"""Ideator_compiled.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fuT7gSqCT3t_uEkRTESZXKGTiiYekRIP

#Libraries
"""

#!pip install PyDictionary

from PyDictionary import PyDictionary
dictionary=PyDictionary()

from bs4 import BeautifulSoup
import requests

import numpy

"""#Functions"""

def listToString(s):  
    str1 = " " 
    return (str1.join(s)) 


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


import re
import pprint
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#remove stop words
def remove_stopwords(desc):
 
  stop_words = stopwords.words("english")
  desc = ' '.join([word for word in desc.split(' ') if word not in stop_words])
  return(desc)


#remove punctuation
def remove_punc(desc):
  from nltk.tokenize import RegexpTokenizer
  tokenizer = RegexpTokenizer(r'\w+')
  desc= tokenizer.tokenize(desc)
  desc= listToString(desc)
  desc=desc.lower()
  return(desc)

#adding the position/description (what they are: part of grammar)
def pos(desc):
  desc_= nltk.sent_tokenize(desc)
  desc_= [nltk.word_tokenize(sent) for sent in desc_]
  desc_= [nltk.pos_tag(sent) for sent in desc_]
  return(desc_)

#removing determiners and prepositions
def remove_dt_prp(fin_desc):
  l= len(fin_desc)
  for i in range(0,l-1):
    if fin_desc[i][1]=="DT" or fin_desc=="PRP":
      fin_desc.pop([i][0])
      l=len(fin_desc)

  #only taking the words and not what topic of grammar they are
  add.end= []
  l= len(fin_desc)
  for a in range(0, l):
    wrd= fin_desc[a][0]
    add.end.append(wrd)
  return(add.end)

def links(num_links, head):
  l=[]
  try: 
      from googlesearch import search 
  except ImportError:  
      print("No module named 'google' found") 
    
  # to search 
  for j in search(head, num=10, tld= 'com' , start=0, stop=num_links, pause=2): 
      l.append(j)

      #print(j) 
  return(l)

def list_of_sites(l):
  l.append(" ")

  for a in range(0,len(l)-1):

    for b in range(a+1, len(l)):

      if len(l[a])< len(l[b]):
              x = l[b].find(l[a])
          
              if x==0:
                l[b]=l[a]

  lis = [] 
  [lis.append(w) for w in l if w not in lis] 

  #removing ""
  lis.pop(len(lis)-1)
  return(lis)

#none type object coming non iterable under extadd.end... 
def end_with_syn(end, l):
  syn= []
  for i in range(0, len(add.end)):
    g= dictionary.synonym(add.end[i])
    syn.append(g)


  output=[]
  def reemovNestings(l): 
      for i in l: 
          if type(i) == list: 
              reemovNestings(i) 
          else: 
              output.append(i) 


  reemovNestings(syn) 
  add.end.extend(output)
  return(add.end)

def listToString2(s):  
    str1 = "" 
    return (str1.join(s)) 

def split(word): 
    return list(word)

#metadesc and score on list

def metadesc_score(lis, end):
  metadesc_score.d= []
  s= []

  def extract_meta(url):
      print(url)
      r = requests.get(url)
      soup = BeautifulSoup(r.text, features="html.parser")
      meta = soup.findAll('meta')
      if len(meta)>2:
        return(meta[2])
      else:
        return 0



  if __name__ == '__main__':
    for i in lis:
      _url = i
      a=extract_meta(_url)
      a=str(a)
      stopwords_2 = ['<meta', 'name="description"/>']
      awords = a.split()

      resultwords  = [word for word in awords if word.lower() not in stopwords_2]
      result = ' '.join(resultwords)
      a= result
      a= a.split()

      word = a[0]
      word=split(word)
      del word[0:9]

      a[0]= listToString2(word)
      metadesc_score.d.append(a)

      #score
      score= 0
      for x in range(0, len(a)):
        a[x]= a[x].lower()
        if (a[x] in add.end): 
          score+=1
      s.append(score)

  return(s)

def sorting_s_to_lis(s, lis):
  s = numpy.array(s) 
  #[::-1] for reversing
  sort_index = numpy.argsort(s)[::-1]
  x=0
  while x<len(lis):
    # lis[x]=lis[sort_index[x]]
    x+=1

  return(lis)

"""#Variables"""

# head= "Image caption generator"
# desc= "It will recognize the context of the image using CV and then give a suitable description using NLP."

# num_links= 6

"""#Applying the Functions"""
def add(num_links, head, desc):
  #applying the functions
  print("Remove_stopwords")
  desc= remove_stopwords(desc)
  print("Remove_punc")
  desc= remove_punc(desc)

  #as list was coming as [[]].. therefore to make it one list: by taking only the first one
  fin_desc= pos(desc)
  fin_desc= fin_desc[0]
  add.end= remove_dt_prp(fin_desc)

  l= links(num_links,head)

  lis= list_of_sites(l)

  add.end= end_with_syn(add.end, l)

  s= metadesc_score(lis, add.end)

  lis= sorting_s_to_lis(s, lis)
  return lis


"""#Final Output"""
# print(add(num_links, head, desc))
# print(lis)

# metadesc_score(lis, add.end)
# desc_of_res_link= (metadesc_score.d)

"""# Retrieving the meta-desc from the sites."""

# print(desc_of_res_link)

"""descrip= []
for i in range(0,num_links):
if listToString(desc_of_res_link[i])!= "":
descrip.appadd.end(listToString(desc_of_res_link[i]))
else:
descrip.appadd.end(head)

print(descrip)"""

