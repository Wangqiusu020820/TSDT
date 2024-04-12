from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张三听说有一个很酷的在线待办事项应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到网页的标题和头部都包含'To-Do'这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # 应用有一个输入代办事项的文本输入框
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 他在文本输入框中输入了'Buy flowers'
        inputbox.send_keys('Buy flowers')

        # 他按了回车键后，页面更新了
        # 待办事项表格中显示了'1: Buy flowers'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(
            '1: Buy flowers',
            [row.text for row in rows]
        )

        # 页面中又显示了一个文本输入框，可以输入其他的待办事项
        # 他输入了'Send a gift to Lisi'
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Send a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 页面再次更新，他的清单中显示了这两个待办事项
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(
            '1: Buy flowers',
            [row.text for row in rows]
        )
        self.assertIn(
            '2: Send a gift to Lisi',
            [row.text for row in rows]
        )

        # 张三想知道这个网站是否会记住他的清单
        # 他看到网站为他生成了一个唯一的URL
        self.fail('Finish the test!')

        # 他访问这个URL，发现他的待办事项列表还在
        # 他满意地离开了

if __name__ == '__main__':
    unittest.main(warnings='ignore')
