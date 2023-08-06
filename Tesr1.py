import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

import Funciones


tg=.2
class base_test(unittest.TestCase):

    def setUp(self):
        service = Service("C:\selenium\chromedriver.exe")
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)





    def test1(self):
        driver = self.driver
        f= Funciones.Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/text-box",tg)
        f.Texto_Mixto("id","userName","Rodrigo",tg)
        f.Texto_Mixto("id","userEmail","rodrigo@gmail.com",tg)
        f.Texto_Mixto("id","currentAddress","Demo uno de texto, para pruebas.",tg)
        f.Texto_Mixto("id","permanentAddress","Demo uno de texto, para pruebas.",tg)
        f.Click_Mixto("id","submit",tg)








    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()






