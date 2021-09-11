"""
Name : main.py
Author  : Hongliang Liu
Contect : honglian@andrew.cmu.edu
Time    : 2021/9/11 15:39
Desc: provide API for GUI,
take a query and break it down,
figure out what should method should it call,
process all the data,
and return gui what they want
"""
from organize.organize import organize
from pre_process.pre_process import pre_process
from scraper.scrape import *
from analysis.analysis import analysis


class main_process():
    def __init__(self,p_name,ranking):
        self.pname=p_name
        self.ranking=ranking

    def scraper(self):
        self.scp_A=scrape_A
        self.scp_B=scrape_B
        self.scp_C=scrape_C
        return True

    def pre_process(self):
        self.ppc=pre_process
        return True

    def organize(self):
        self.ogn=organize
        return True

    def analysis(self):
        self.anls=analysis
        return True