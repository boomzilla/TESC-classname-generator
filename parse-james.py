#This program takes a file containing a grammar,
#parses it, using the grammar to generate random
#sentences.
#
#Coded by Ian Ruotsala, Sep. 7, 2008

#update:
#James Newman's automatic course title generation 
#hard-coded into source
#
#Coded for Python 2.*, probably won't run in Python 3
#--ICR, 2011, May 19

import random

DEBUG = False

JAMES = "<title>:=<zzz> : <zzz>|<zzz>\n" + \
"<c>:=<adj> <noun>|<noun>\n" + \
"<xxx>:=<c>|<c> and <c>|<c> <prep> <c>|<c> and <c>  <prep> <c>\n" + \
"<yyy>:=<vbing> <c>|<c>\n" + \
"<zzz>:=<xxx>|<yyy>\n" + \
"<prep>:=to|from|of|in\n" + \
"<noun>:=alternatives|foundations|representations|narratives|crafts|biodiversity|knowledge|abjection|art|time|argentina|plants|people|ecoliteracy|change|mausoleum\n" + \
"<vbing>:=drawing|defending|writing|rewriting|interogating|looking|re-interpretting\n" + \
"<adj>:=real|literary|imagined|cultural|evolutionary|social|forbidden|sustainable\n"

def parse_grammar(grammar):
    #this function converts the grammar string
    #into a dictionary, with the rules as keys,
    #returns the dictionary
    lines = grammar.splitlines()
    grammar_dict = {}
    for line in lines:
        line_split = line.split(":=")
        grammar_dict[line_split[0]] = line_split[1].split("|")

    return grammar_dict

def generate_sentence(grammar_dict, rule):
    #this function returns a randomly generated
    #string based on the passed grammar
    g_list = grammar_dict.get(rule)
    g_string = random.choice(g_list)
    to_return = ""

    sub_list = g_string.split()
    for rule in sub_list:
            if DEBUG:
                    print to_return
            if (rule[0] == "<"):
                to_return += generate_sentence(grammar_dict, rule)
            else:
                to_return += rule + " "
    
    return to_return

#name = raw_input("enter file name: ")
#grammar_file = open(name, 'r')
#grammar = grammar_file.read()
grammar_dict = parse_grammar(JAMES)
#rule = raw_input("With which rule should I begin? ")
if DEBUG:
    print grammar_dict
    print "\n"
rule = "<title>"
print (generate_sentence(grammar_dict, rule))

