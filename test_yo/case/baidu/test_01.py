import unittest
import requests

class Test_Kuaidi(unittest.TestCase):
    def setUp(self) -> None:
        self.headers ={
           "User-Agent":"Mozilla / 5.0(Macintosh;IntelMacOSX10_14_5) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 77.0.3865.90Safari / 537.36"
        }
    def test_yunda(self):
        danhao = '4301403791333'
        kd = 'yunda'
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html"%(danhao,kd)
        print(self.url)
        r = requests.get(self.url,headers = self.headers,verify = False)
        result = r.json()




