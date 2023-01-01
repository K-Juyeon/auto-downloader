import tkinter as tk
import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

global driver
global page_links
global doc_nums
global doc_number
global d_term
global p_term
global site
global flag

def start() :
    global driver
    global page_links
    global doc_nums
    global doc_number
    global d_term
    global site
    global flag

    id = textID.get()
    password = textPW.get()

    driver = selenium.webdriver.Chrome('./chromedriver/chromedriver')

    driver.get('https://cs.inhatc.ac.kr/cs/1763/subview.do?enc=Zm5jdDF8QEB8JTJGc3ViTG9naW4lMkZjcyUyRnZpZXcuZG8lM0Y%3D')
    # menu1760_obj121 > div._fnctWrap > form:nth-child(3) > div > table > tbody > tr:nth-child(1) > td.td-num

    id_box = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR, '#inputUserId')
    pw_box = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR, '#inputUserPwd')
    login_btn = driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, '_loginSubmit')
    id_box.send_keys(id)
    pw_box.send_keys(password)

    login_btn.click()

    if pickSite.get() == 1 :
        flag = '1761'
    elif pickSite.get() == 2 :
        flag = '1760'


    # array = site.split('/')
    # flag = array[4]

    if flag == '1760' :
        driver.get('https://cs.inhatc.ac.kr/cs/1760/subview.do')
    elif flag == '1761' :
        driver.get('https://cs.inhatc.ac.kr/cs/1761/subview.do')

    page_btns = list()
    doc_nums = list()

    page_links = dict()


    if flag == '1761' :
        doc_number = int(driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                             '#menu1761_obj122 > div._fnctWrap > form:nth-child(2) > div.board-search > div.util-search > strong').text)
    elif flag == '1760' :
        doc_number = int(driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                         '#menu1760_obj121 > div._fnctWrap > form:nth-child(2) > div.board-search > div.util-search > strong').text)

    # page_count = int((doc_number / 100) + 1)
    page_count = 1
    # for i in range(2, 10 + 1):
    #
    #     page_btns.append(page_btn)
    #     print(page_btn.text)
    d_term = 10
    # for i in range(page_count):

def scanAll() :
    global doc_number
    global d_term
    global p_term
    global flag

    if flag == '1760' :
        for i in range(1):
            print(f'page number: {1 + (i * 10)}')

            if doc_number >= 100:
                doc_number -= 100
                p_term = 10
            else:
                p_term = int(doc_number / 10)
                d_term = doc_number - (p_term * 10)
                doc_number = 0

            for j in range(2, p_term + 1):
                page_btn = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                               f'#menu1760_obj121 > div._fnctWrap > form:nth-child(4) > div > div > ul > li:nth-child({j}) > a')
                # time.sleep(1)
                print(f'page number: {page_btn.text}')
                for k in range(1, d_term + 1):
                    doc_num = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                                  f'#menu1760_obj121 > div._fnctWrap > form:nth-child(3) > div > table > tbody > tr:nth-child({k}) > td.td-num')
                    # doc_nums.append(int(doc_num.text))
                    page_links[int(doc_num.text)] = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                                                        f'#menu1760_obj121 > div._fnctWrap > form:nth-child(3) > div > table > tbody > tr:nth-child({k}) > td.td-subject > a').get_attribute(
                        'href')
                page_btn.click()
            if doc_number != 0:
                driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                    '#menu1760_obj121 > div._fnctWrap > form:nth-child(4) > div > div > a._next').click()
            print(page_links)
    elif flag == '1761' :
        for i in range(1):
            print(f'page number: {1 + (i * 10)}')

            if doc_number >= 100:
                doc_number -= 100
                p_term = 10
            else:
                p_term = int(doc_number / 10)
                d_term = doc_number - (p_term * 10)
                doc_number = 0

            for j in range(2, p_term + 1):
                page_btn = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                               f'#menu1761_obj122 > div._fnctWrap > form:nth-child(4) > div > div > ul > li:nth-child({j}) > a')
                # time.sleep(1)
                print(f'page number: {page_btn.text}')
                for k in range(1, d_term + 1):
                    doc_num = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                                  f'#menu1761_obj122 > div._fnctWrap > form:nth-child(3) > div > table > tbody > tr:nth-child({k}) > td.td-num')
                    # doc_nums.append(int(doc_num.text))
                    page_links[int(doc_num.text)] = driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                                                        f'#menu1761_obj122 > div._fnctWrap > form:nth-child(3) > div > table > tbody > tr:nth-child({k}) > td.td-subject > a').get_attribute(
                        'href')
                page_btn.click()
            if doc_number != 0:
                driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR,
                                    '#menu1761_obj122 > div._fnctWrap > form:nth-child(4) > div > div > a._next').click()
            print(page_links)


    textAll.configure(text=f'[{list(page_links.keys())[0]} ~ {list(page_links.keys())[-1]}]')


# print(f'현재 게시글 번호 범위 [{list(page_links.keys())[0]} ~ {list(page_links.keys())[-1]}]')
# start = int(input('시작 게시글 번호: '))
# end = int(input('끝 게시글 번호: '))

def download() :
    start = int(textStart.get())
    end = int(textEnd.get())

    for i in range(start, end + 1):
        print(page_links.get(i))
        driver.get(page_links.get(i))
        # file01 = driver.find_element(By.CSS_SELECTOR, f"#menu1760_obj121 > div._fnctWrap > div.view-file > dl > dd > ul > li:nth-child({1}) > a")
        files = driver.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR, f'body > div > div.view-file > dl > dd > ul > li > a')

        for file in files:
            file.click()
            print(file.text)
        print('==================')

        time.sleep(0.01)

root = tk.Tk()
root.title('민원 게시판 다운로더')
root.geometry('350x230')

# menu1760_obj121 > div._fnctWrap > div.view-file > dl > dd > ul > li:nth-child(1) > a
# print(doc_nums)
# print(page_links)
# menu1760_obj121 > div._fnctWrap > form:nth-child(4) > div > div > ul > li:nth-child(3) > a
# menu1760_obj121 > div._fnctWrap > form:nth-child(4) > div > div > ul > li:nth-child(3) > a
# print(doc_num)

lblSite = tk.Label(root, text='게시판 선택')
lblSite.grid(row=0, column=0)

pickSite = tk.IntVar()
btn1 = tk.Radiobutton(root, text='온라인민원신청', value=1, variable=pickSite)
btn2 = tk.Radiobutton(root, text='서면수강신청', value=2, variable=pickSite)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)

lbl = tk.Label(root)
lbl.grid(row=1, column=0)

labelAll = tk.Label(root, text='전체 게시글 범위')
labelAll.grid(row=2, column=0)

textAll = tk.Label(root, text="")
textAll.grid(row=2, column=1, columnspan=2)

labelID = tk.Label(root, text='ID')
labelID.grid(row=3, column=0)

textID = tk.Entry(root, width=30)
textID.grid(row=3, column=1, columnspan=2)

labelPW = tk.Label(root, text='PW')
labelPW.grid(row=4, column=0)

textPW = tk.Entry(root, width=30)
textPW.grid(row=4, column=1, columnspan=2)

button1 = tk.Button(root, text='불러오기', command=lambda:[start(), scanAll()])
button1.grid(row=5, columnspan=3)

lbl = tk.Label(root)
lbl.grid(row=6, column=0)

labelStart = tk.Label(root, text='시작 게시글 번호')
labelStart.grid(row=7, column=0)

textStart = tk.Entry(root, width=30)
textStart.grid(row=7, column=1, columnspan=2)

labelEnd = tk.Label(root, text='끝 게시글 번호')
labelEnd.grid(row=8, column=0)

textEnd = tk.Entry(root, width=30)
textEnd.grid(row=8, column=1, columnspan=2)

button2 = tk.Button(root, text='DOWNLOAD', command=download)
button2.grid(row=9, columnspan=3)

root.mainloop()