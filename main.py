import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_name_list(path:str, column:str):

    data = pd.read_csv(path)
    name_list = list(data.loc[:,column].unique())
    
    return name_list

def download_file(route:str, dest_dir:str=''):
    
    page = requests.get(route)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
    print(soup)

path = 'data/RNAs.csv'
column = 'Nomenclatura'
route = 'https://www.ncbi.nlm.nih.gov/gene/?term=Homo+sapiens+DACOR1'

#with open("test.html", "w") as f:
#    f.write(str(download_file(route).prettify()))
