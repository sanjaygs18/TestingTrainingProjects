import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM_Assignment.as_handb_login import LoginPageHB
from POM_Assignment.add_items_to_cart import AddItemsToCart
from POM_Assignment.Add_to_basket import AddToBasketPage

class TestHollandBarrett:
    @pytest.fixture()
    def setupmethod(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.implicitly_wait(5)

    def test_loginfuncheck(self,setupmethod):
        tc1 = LoginPageHB(self.driver)
        self.driver.get("https://auth.hollandandbarrett.com/u/login")
        tc1.loginhandb("sanjay.saimurali18@gmail.com","H&b@1897")

        expect_title = self.driver.title
        actual_title = "Access Denied"
        assert actual_title == expect_title

    def test_addVitaminsItems(self,setupmethod):
        self.driver.get("https://www.hollandandbarrett.com/")
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.ID, "onetrust-reject-all-handler"))).click()
        tc1 = AddItemsToCart(self.driver)
        tc1.getIntoVitaminsSec()
        tc1.vitaminsItems("div.LayoutWidget-module_wrapper__GThIL:nth-child(10) div.LayoutWidget-module_layout__Wyiom div.SearchContentContainer-module_container__V2qWt div.SearchContentContainer-module_contentContainer__X8w2G div.ProductListContainer-module_list__SBhvf a.ProductCard-module_link__IYL9H:nth-child(1) > div.ProductCard-module_card__tfOGl")
        WebDriverWait(self.driver,5)

        self.driver.find_element(By.XPATH,"//a[normalize-space()='Home']").click()

    def test_addVeganItems(self,setupmethod):
        tc1 = AddItemsToCart(self.driver)
        tc1.getIntoVeganItems()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Vegan Chocolate']").click()
        tc1.veganItems("#products-list > div > div.ProductListContainer-module_list__hu7Eh > a:nth-child(1) > div")
        WebDriverWait(self.driver, 5)
        tc1 = AddToBasketPage()
        tc1.calsubtotal(self.driver,"#__next > div.jsx-3844687651.page-container > div.jsx-3844687651.page-container-inner-main > div:nth-child(2) > div.jsx-2398642508.jsx-2816424260.basket__container > div.jsx-2398642508.jsx-2816424260.basket__container-items > section > div > article")
        print(tc1.element)


