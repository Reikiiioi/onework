import requests, time
from os import name, system
from os.path import exists, isfile
from random import choice, randint
from threading import Thread
from time import sleep
from colorama import Fore, Style
from requests import get, post
from user_agent import generate_user_agent
from termcolor import colored
import os


def logo1():
    os.system('cls||clear')
    print('''
        
          ||
          ||
          ||
          ||
          ||
                                                                            

                                    сделано Reikiiioi. *
                                TG/VK: @ECTECTBEHHA. *
            сделано для бесплатного использования. *
                                           кряк. *
        ''')
    
def logo2():
    os.system('cls||clear')
    print('''
         _____    
        |  __ \  || 
        | |__) | ||
        |  _  /  ||
        | | \ \  || 
        |_|  \_\ ||
                                                                            

                                    сделано Reikiiioi. -*
                                TG/VK: @ECTECTBEHHA. -*
            сделано для бесплатного использования. -*
                                           кряк. -*
        ''')

def logo3():
    os.system('cls||clear')
    print('''
         _____    ______  
        |  __ \  |  ____| ||
        | |__) | | |__    ||
        |  _  /  |  __|   ||
        | | \ \  | |____  ||
        |_|  \_\ |______| ||
                                                                            

                                    сделано Reikiiioi. --*
                                TG/VK: @ECTECTBEHHA. --*
            сделано для бесплатного использования. --*
                                           кряк. --*
        ''')

def logo4():
    os.system('cls||clear')
    print('''
         _____    ______   _____  
        |  __ \  |  ____| |_   _| ||
        | |__) | | |__      | |   ||
        |  _  /  |  __|     | |   ||
        | | \ \  | |____   _| |_  ||
        |_|  \_\ |______| |_____| ||
                                                                            

                                    сделано Reikiiioi. ---*
                                TG/VK: @ECTECTBEHHA. ---*
            сделано для бесплатного использования. ---*
                                           кряк. ---*
        ''')
    
def logo5():
    os.system('cls||clear')
    print('''
         _____    ______   _____   _  __  
        |  __ \  |  ____| |_   _| | |/ /  ||
        | |__) | | |__      | |   | ' /   || 
        |  _  /  |  __|     | |   |  <    ||
        | | \ \  | |____   _| |_  | . \   ||
        |_|  \_\ |______| |_____| |_|\_\  ||
                                                                            

                                    сделано Reikiiioi. ----*
                                TG/VK: @ECTECTBEHHA. ----*
            сделано для бесплатного использования. ----*
                                           кряк. ----*
        ''')
    
def logo6():
    os.system('cls||clear')
    print('''
         _____    ______   _____   _  __  _____    
        |  __ \  |  ____| |_   _| | |/ / |_   _| ||
        | |__) | | |__      | |   | ' /    | |   ||
        |  _  /  |  __|     | |   |  <     | |   ||
        | | \ \  | |____   _| |_  | . \   _| |_  ||
        |_|  \_\ |______| |_____| |_|\_\ |_____| ||
                                                                            

                                    сделано Reikiiioi. -----*
                                TG/VK: @ECTECTBEHHA. -----*
            сделано для бесплатного использования. -----*
                                           кряк. -----*
        ''')
    
def logo7():
    os.system('cls||clear')
    print('''
         _____    ______   _____   _  __  _____   _____   
        |  __ \  |  ____| |_   _| | |/ / |_   _| |_   _| ||
        | |__) | | |__      | |   | ' /    | |     | |   ||
        |  _  /  |  __|     | |   |  <     | |     | |   ||
        | | \ \  | |____   _| |_  | . \   _| |_   _| |_  ||
        |_|  \_\ |______| |_____| |_|\_\ |_____| |_____| ||
                                                                            

                                    сделано Reikiiioi. ------*
                                TG/VK: @ECTECTBEHHA. ------*
            сделано для бесплатного использования. ------*
                                           кряк. ------*
        ''')
    
def logo8():
    os.system('cls||clear')
    print('''
         _____    ______   _____   _  __  _____   _____   _____    
        |  __ \  |  ____| |_   _| | |/ / |_   _| |_   _| |_   _|  ||
        | |__) | | |__      | |   | ' /    | |     | |     | |    ||
        |  _  /  |  __|     | |   |  <     | |     | |     | |    ||
        | | \ \  | |____   _| |_  | . \   _| |_   _| |_   _| |_   ||
        |_|  \_\ |______| |_____| |_|\_\ |_____| |_____| |_____|  ||
                                                                            

                                    сделано Reikiiioi. -------*
                                TG/VK: @ECTECTBEHHA. -------*
            сделано для бесплатного использования. -------*
                                           кряк. -------*
        ''')
    
def logo9():
    os.system('cls||clear')
    print('''
         _____    ______   _____   _  __  _____   _____   _____    ____    
        |  __ \  |  ____| |_   _| | |/ / |_   _| |_   _| |_   _|  / __ \  ||
        | |__) | | |__      | |   | ' /    | |     | |     | |   | |  | | ||
        |  _  /  |  __|     | |   |  <     | |     | |     | |   | |  | | ||
        | | \ \  | |____   _| |_  | . \   _| |_   _| |_   _| |_  | |__| | ||
        |_|  \_\ |______| |_____| |_|\_\ |_____| |_____| |_____|  \____/  ||
                                                                            

                                    сделано Reikiiioi. --------*
                                TG/VK: @ECTECTBEHHA. --------*
            сделано для бесплатного использования. --------*
                                           кряк. --------*
        ''')
    
def logo10():
    os.system('cls||clear')
    print('''
         _____    ______   _____   _  __  _____   _____   _____    ____    _____ 
        |  __ \  |  ____| |_   _| | |/ / |_   _| |_   _| |_   _|  / __ \  |_   _| ||
        | |__) | | |__      | |   | ' /    | |     | |     | |   | |  | |   | |   ||
        |  _  /  |  __|     | |   |  <     | |     | |     | |   | |  | |   | |   ||
        | | \ \  | |____   _| |_  | . \   _| |_   _| |_   _| |_  | |__| |  _| |_  ||
        |_|  \_\ |______| |_____| |_|\_\ |_____| |_____| |_____|  \____/  |_____| ||
                                                                            

                                    сделано Reikiiioi. ---------*
                                TG/VK: @ECTECTBEHHA. ---------*
            сделано для бесплатного использования. ---------*
                                           кряк. ---------*
        ''')
    
def aq():
    os.system('cls||clear')
    print('''
        Имя: Лео (полное - Лев)
        Особенности: нету
        Описание: нет


''')
    time.sleep(1)
    o = input('Нажмите Enter, что бы выйти или нажмите f что бы вернуться: ')
    if o == 'f':
        logo11()
    time.sleep(1)

def aqq():
    os.system('cls||clear')
    print('''
        Имя: Лео (полное - Лев)
        Особенности: нету
        Описание: дефолтный и скромный парень, не обижу)


''')
    time.sleep(1)
    o = input('Нажмите Enter, что бы выйти или нажмите f что бы вернуться: ')
    if o == 'f':
        logo11()
    time.sleep(1)

def bq():
    os.system('cls||clear')
    print('''
        Телефон: +79330320068
        TG: @ECTECTBEHHA
        ВКонтакте: @ECTECTBEHHA
          Просьба не звонить и не спамить, а то - ЧС
''')
    time.sleep(1)
    o = input('Нажмите Enter, что бы выйти или нажмите f что бы вернуться: ')
    if o == 'f':
        logo11()
    time.sleep(1)

def uq():
    os.system('cls||clear')
    print('''
    Напиши текст и система найдёт это в интернете!
''')
    t = input('Пишите текст: ')
    time.sleep(0.5)
    os.system('cls||clear')
    print('''Идёт поиск в интренете!
          ваш текст: ''' + t)
    time.sleep(1)
    w = input('Нажмите Enter, что бы выйти или нажмите f что бы вернуться: ')
    if w == 'f':
        cq()

def cq():
    os.system('cls||clear')
    print('''
        [u] - система найди!


''')
    time.sleep(1)
    o = input('Нажмите Enter, что бы выйти или нажмите f что бы вернуться: ')
    if o == 'f':
        logo11()
    if o == 'u':
        uq()
    time.sleep(1)

def dq():
    os.system('cls||clear')
    print('''
        Вы автоматически принимаете законы РФ при скачивание данного файла!
            Мы не несём за вас отвестенность!
                Любые действия сделанные тут вами - ваше дело и отвестенность!


''')
    time.sleep(1)
    o = input('Нажмите Enter, что бы выйти или нажмите f что бы вернуться: ')
    if o == 'f':
        logo11()
    time.sleep(1)

def logo11():
    os.system('cls||clear')
    print('''
         _____    ______   _____   _  __  _____   _____   _____    ____    _____ 
        |  __ \  |  ____| |_   _| | |/ / |_   _| |_   _| |_   _|  / __ \  |_   _| 
        | |__) | | |__      | |   | ' /    | |     | |     | |   | |  | |   | |   
        |  _  /  |  __|     | |   |  <     | |     | |     | |   | |  | |   | |   
        | | \ \  | |____   _| |_  | . \   _| |_   _| |_   _| |_  | |__| |  _| |_   _ 
        |_|  \_\ |______| |_____| |_|\_\ |_____| |_____| |_____|  \____/  |_____| (_)
                                                                            

                                    сделано Reikiiioi. --------| a | + Информация
                                TG/VK: @ECTECTBEHHA. --------| b | + Контакты
            сделано для бесплатного использования. --------| c | + Функции
                                           кряк. --------| d | + Важно!!!
ответ надо дать буквой!!!


''')
    time.sleep(1)
    fun()
    
def fun():
    g = input("Нажмите Enter, что бы выйти или выберите что хотите сделать (ответ надо дать буквой): ")
    if g == 'a':
        aq()
    if g == 'b':
        bq()
    if g == 'c':
        cq()
    if g == 'd':
        dq()
time.sleep(2)
logo1()
time.sleep(0.1)
logo2()
time.sleep(0.1)
logo3()
time.sleep(0.1)
logo4()
time.sleep(0.1)
logo5()
time.sleep(0.1)
logo6()
time.sleep(0.1)
logo7()
time.sleep(0.1)
logo8()
time.sleep(0.1)
logo9()
time.sleep(0.1)
logo10()
time.sleep(0.3)
logo11()
time.sleep(1)
