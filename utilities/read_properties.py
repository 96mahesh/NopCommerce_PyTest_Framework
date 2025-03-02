import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:

    @staticmethod
    def get_admin_Page_url():
        url = config.get("admin login info","admin_page_url")
        return url

    @staticmethod
    def get_username():
        username = config.get("admin login info","username")
        return username

    @staticmethod
    def get_password():
        password = config.get("admin login info", "password")
        return password

    @staticmethod
    def get_inValid_username():
        invali_dusername = config.get("admin login info", "invalid_username")
        return invali_dusername

