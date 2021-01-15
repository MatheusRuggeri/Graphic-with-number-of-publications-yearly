from selenium import webdriver
import matplotlib.pyplot as plt
from webdriver_manager.chrome import ChromeDriverManager
import time
import numpy as np
import os

loggin = True
dailies = True
# Put here the first page in the book that you want to download
BASE_URL = 'https://scholar.google.com.br/scholar?q='

print('What subject do you want to google?', end='')
input_text = input()
input_text_bk = input_text
input_text = input_text.replace(' ', '+')

print('What is the starting year ?', end='')
start_year = input()
start_year = int(start_year)

print('And when should I stop?', end='')
end_year = input()
end_year = int(end_year)

# Uses webdriver_manager to create a chrome session
browser = webdriver.Chrome(ChromeDriverManager().install())

# Move to my second screen
#browser.set_window_position(2000, 10)

# ToFla maximize the browser window 
browser.maximize_window() 

year_list = []
results_list = []

for year in range(start_year, end_year + 1):
    # Open the page
    browser.get(BASE_URL + input_text + '&as_ylo=' + str(year) + '&as_yhi=' + str(year))

    # Get all the text in this element
    results = browser.find_element_by_xpath('//*[@id="gs_ab_md"]').text
    
    # Remove what I don't want
    results = results.replace('Aproximadamente ', '').replace('resultados ', '')
    results = results.split()[0]
    results = results.replace('.', '')
    results = int(results)
    
    print('In ' + str(year) + ' there was ' + str(results))
    
    # Put in 2 lists
    year_list.append(year)
    results_list.append(results)
    
    time.sleep(2)
  
# When it's all done, close the browser
browser.close() 


fig, ax = plt.subplots()
ax.plot(year_list, results_list)
#ax.plot(secondXPlot, secondYPlot)

ax.set(xlabel='Resultados', ylabel='Ano', title=input_text_bk + ' publications between ' + str(start_year) + ' and ' +  str(end_year))
ax.grid()

plt.xticks(np.arange(min(year_list), max(year_list)+1, 1))

plt.gcf().set_size_inches(8, 5)
fig.savefig('export' + os.sep + input_text_bk + '-' + str(start_year) + '-' +  str(end_year) + ".png", dpi = 300)
#plt.close(fig)
plt.show()
    