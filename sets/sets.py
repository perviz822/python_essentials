import pandas as pd
from pypdf import PdfReader
import re

#1. Email Overlap in Marketing Campaigns
#Problem:
#You work for a small e-commerce site running two separate ad campaigns: one on Facebook, one on Instagram. You get two large CSV files, each with emails of users who interacted. Your boss wants:

#Total number of unique leads.

#Number of users who saw both ads.

#Number of users who saw only one ad.
#your Task:
#Write a script that takes the two email lists and produces these three numbers.






s1 = set(pd.read_csv('sets/facebook_campaign.csv')['emails'])

s2 = set (pd.read_csv('sets/instagram_campaign.csv')['emails'])


def boss_requirements_for_marketing_campaign(s1:set[str] , s2:set[str])-> tuple[int,int,int] :
    total_unique_leads = s1.union(s2)
    leads_who_saw_both =  s1.intersection(s2)
    leads_who_saw_only_one =  total_unique_leads -leads_who_saw_both

    return (len(total_unique_leads),len(leads_who_saw_both),len(leads_who_saw_only_one))












'''
Plagiarism Checker (Basic)
Problem:
Given two student essays (as plain text), you need to compare them and find:
The percentage of unique words they have in common.
A list of uncommon words in one vs. the other.
This could help you flag suspiciously similar submissions.

'''

def plagiarism_checker(file_path1:str, file_path2:str):
    reader1 = PdfReader(file_path1)
    reader2 = PdfReader(file_path2)

    essay1_content = re.sub(r'\s+',' ',reader1.pages[0].extract_text()).strip().lower()
    essay2_content = re.sub(r'\s+',' ',reader2.pages[0].extract_text()).strip().lower()
    essay1_words = set(essay1_content.split(' '))
    essay2_words = set(essay2_content.split(' '))

    common_words = len(essay2_words.intersection(essay1_words))
    all_words = len(essay1_words.union(essay2_words))


    similarity = common_words / all_words

    return  "{:.2f}".format(similarity)






print(plagiarism_checker('sets/essay1.pdf','sets/essay2.pdf'))








