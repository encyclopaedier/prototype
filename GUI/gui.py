"""
Name : gui.py
Author  : Hongliang Liu
Contect : honglian@andrew.cmu.edu
Time    : 2021/9/11 16:00
Desc:gui used to communicate with users
"""

from main.main_process import main_process
'''
start a interface and respond to users
'''

#datas might be used for program
product_name=['1']
rank=['1']
over_flag=1


def concat_query(p_name,ranking):
    result=main_process
    res=result(p_name,ranking)
    return res


while(over_flag):
    p_name=input('product name:')
    ranking=input('sort by:')
    #make sure the product and ranking nutrition exist
    if p_name in product_name and ranking in rank:
        concat_query(p_name,ranking)
    elif ranking not in rank:
        print('ranking basis not found!')
    elif p_name in product_name:
        print('product not found!')


    flag=input('continue? \n\'Y\'for continue, any button for exit:')
    over_flag=1 if flag=='Y' else 0
