import unittest

from base.Browser import Browser
from page.page_login import PageLogin


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()

    def tearDown(self):
        self.browser.quit(5)

    def test_login(self):
        pl = PageLogin(self.browser)
        username = pl.login("thr", "123")
        self.assertEqual('thr', username)


if __name__ == '__main__':
    unittest.main()
