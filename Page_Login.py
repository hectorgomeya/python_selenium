
import Funciones


class Pagina_Login():

    def __init__(self,driver):
        self.driver=driver

    def Login_Master(self,url,name,clave,t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar(url,t)
        f.Texto_Xpath_Valida("//input[contains(@id,'user-name')]", name, t)
        f.Texto_Xpath_Valida("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_Valida("//input[contains(@id,'login-button')]",t)
        f.Salida()


