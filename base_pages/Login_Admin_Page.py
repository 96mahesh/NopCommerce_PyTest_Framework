import time
from selenium.webdriver.common.by import By


class Login_Admin_page:
    textbox_username_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"
    btn_login_xpath = "//button[text()='Log in']"
    dashboard_xpath = "//h1[contains(text(),'Dashboard')]"
    error_msg_xpath="//li"
    expected_title = "Dashboard"
    exp_error_msg= "No customer account found"

    def __init__(self, driver):
        self.driver = driver

    def user_name(self, username):
        time.sleep(2)
        userelement = self.driver.find_element(By.XPATH, self.textbox_username_xpath)
        userelement.clear()
        userelement.send_keys(username)

    def user_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def verify_dashBoard_page(self):
        actual_Text = self.driver.find_element(By.XPATH, self.dashboard_xpath).text
        if actual_Text == self.expected_title:
            assert True


        else:
            assert False

    def verify_errorMsg(self):
        errormsg = self.driver.find_element(By.XPATH, self.error_msg_xpath).text
        print(errormsg)

        assert  errormsg == self.exp_error_msg



