from browser import Browser
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.productpage import ProductPage
from pages.boxpage import BoxPage
from utils.customlogger import LogGen


def before_all(context):
    context.browser = Browser()
    context.homepage = HomePage()
    context.loginpage = LoginPage()
    context.productpage = ProductPage()
    context.boxpage = BoxPage()
    context.customlogger = LogGen()


def after_all(context):
    context.browser.close()
