
###########  Q1

word ="Grow Gratitude"

# a)	How do you access the letter “G” of “Growth”?

print(word[0])


#b)	How do you find the length of the string?
 
len(word)


#c)	Count how many times “G” is in the string.

print(word.count('G')) 


###########   Q2

"""
2.	Create a string “Being aware of a single shortcoming within yourself is
 far more useful than being aware of a thousand in someone else.”
Code for the following
a)	Count the number of characters in the string.
"""

sentence_2 = 'Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.'

sentence_2

print(sentence_2.count(' '))


"""
3.	Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
Code for the following tasks:
a)	get one char of the word
b)	get the first three char
c)	get the last three char """



sentence_3 =  "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

##  a)	get one char of the word
print (sentence_3[0])


#b)	get the first three char

print (sentence_3[0:3])


#   c)	get the last three char 

print (sentence_3[-3:])


"""4.	create a string "stay positive and optimistic". Now write a code to split on whitespace.
Write a code to find if:
a)	The string starts with “H”
b)	The string ends with “d”
c)	The string ends with “c”
"""

sentence_4 ='stay positive and optimistic.' 
#Now write a code to split on whitespace.'

sentence_4.split(' ') # Split on whitespace

#a)	The string starts with “H”

sentence_4.startswith("H")


##b)	The string ends with “d”
sentence_4.endswith("d")

##c)	The string ends with “c”

sentence_4.endswith("c")



"""5.	Write a code to print " 🪐 " one hundred and eight times. (only in python)"""

print( " 🪐 "* 108 )


"""7.	Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”"""

sentence_7 ='Grow Gratitude'


sentence_7.replace("Grow", "Growth of " )

"""8.	A story was printed in a pdf, which isn’t making any sense. i.e.:
“.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”
You have noticed that the story is printed in a reversed order. Rectify the same and write a code to print the same story in a correct order.
"""

story = '.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A'


print (''.join(reversed(story)))
