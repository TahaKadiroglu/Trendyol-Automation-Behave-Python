from behave import *
import time
from utils.customlogger import LogGen
mylog = LogGen.customloggerrr()

@given('Launch The Chrome Browser')
def LaunchChromeBrowser(context):
    context.homepage.navigate("https://www.trendyol.com/")


@when('Open TrendyolHomePage and Click Login Button')
def TrendyolHomePage(context):
    context.homepage.search()


@then('Enter username "{username}" and password "{password}"')
def LoginProcess(context, username, password):
    context.loginpage.email(username)
    context.loginpage.password(password)
    context.loginpage.search()


@then('Search for Iphone13 and Filter the products')
def SearchforIphone(context):
    context.homepage.searchforproduct()
    context.homepage.filterproducts()


@then('Open Product Page')
def ProductPage(context):
    context.productpage.changethewindow()
    context.productpage.checkoutthephotos()
    time.sleep(3)
    context.productpage.morecomments()
    time.sleep(3)
    context.productpage.scrollpage()
    time.sleep(3)
    context.productpage.sepeteekle()
    mylog.info("Urun Sepete Eklenmistir.")

@then('Go to Box Page')
def BoxPage(context):
    context.boxpage.trash()

