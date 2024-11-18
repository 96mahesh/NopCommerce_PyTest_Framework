from selenium import webdriver
from base_pages.Login_Admin_Page import Login_Admin_page
from utilities.read_properties import Read_config
from utilities.custom_logger import log_macker


class Test_01_Admin_Login:
    admin_page_url = Read_config.get_admin_Page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_inValid_username()
    logger = log_macker.log_gen()

    def test_title_verificaion(self, setup):
        self.logger.info("************** test_title_verificaion **************")
        self.logger.info("************** verification of login admin page title verification **************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "Your store. Login"
        #assert act_title == exp_title
        if act_title == exp_title:
            assert True
            self.logger.info("************** Test case pass **************")
            self.driver.close()
        else:
            self.logger.info("************** Test case fail **************")
            self.driver.save_screenshot(".\\screenshots\\test_title_verificaion.png")
            self.driver.close()
            assert False

    def test_valid_admin_login(self, setup):
        self.logger.info("************** test_valid_admin_login **************")
        self.logger.info("************** login valid credentials **************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.user_name(self.username)
        self.admin_lp.user_password(self.password)
        self.admin_lp.click_on_login()
        self.admin_lp.verify_dashBoard_page()

    def test_invalid_admin_login(self, setup):
        self.logger.info("************** test_invalid_admin_login **************")
        self.logger.info("************** login invalid credentials **************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.user_name(self.invalid_username)
        self.admin_lp.user_password(self.password)
        self.admin_lp.click_on_login()
        self.admin_lp.verify_errorMsg()


