import re
import os
from collections import Counter
def main():
	lines1=open("Hindi_synset_w-x.txt").readlines()
	word=input("enter any word: ").strip()
	pos=input("enter the POS: ").upper()
	index=input("enter the index: ").strip()
	search_word=word+"#"+pos+"\t"+index
	print(search_word)
	output_cluster=os.popen("grep -i \"^"+search_word+"\" \"/home/nmn/Hindi_wordnet_programs/wikipedia_stanford_cluster_a1_N200_n200_labelled\"").read().split("\n")
	print("output_cluster= "+str(output_cluster))
	cluster1=str(output_cluster).split("\t")
	cluster1=cluster1[len(cluster1)-2]
	print("*"*10)
	print("#"*10)
	cluster1=cluster1.split(",")
	print("cluster1= "+str(cluster1))
	POS_DICT={'NN':'_noun','VB':'_verb','JJ':'_adjective','RB':'_adverb'}
	if pos in POS_DICT:
		n=POS_DICT[pos]
		print(n)
	hindi_list =set()
	b=[]
	print(cluster1)
	for i in cluster1:
		try:
			word,pos=i.split("#")
			output_shabdanjali=os.popen("grep -i ^"+word.strip()+n+" \"/home/nmn/Hindi_wordnet_programs/default-iit-bombay-shabdanjali-dic.txt\"").read()
			a=output_shabdanjali.split()[-1]
			c=a.split("/")
			b=b+c
		except:
			continue
	x=set()
	x=Counter(b)
	print(x)
	i=0
	for line1 in lines1:
		i=i+1
		set2=eval(line1) 
		set3 = [value for value in x if value in set2]
		if set3:
			if len(set3)>4: 																																																																																																																																																																																																																																																															
				print("set1 intersection set2 : ", set3)
				print(i)
				print(os.popen("sed -n "+str(i)+"p"+" \"/home/nmn/Hindi_wordnet_programs/Hindi_synset\"").read())
				print("*"*10)
				
if __name__ == '__main__':
	main()		
