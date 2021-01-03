# -*-coding:utf8 -*-
import requests
import json


class TaoBao(object):
    def __init__(self,url):
        self.url = url
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/78.0.3904.108 Safari/537.36'}

    def cookies(self):
        cookie = "t=917628a9a97b9af5660eb64b5b461491; cna=lBs0F2OwJ0kCAXLxgVLNhY0c; _samesite_flag_=true; " \
                  "cookie2=13a0f19b65cab85fd062a43486ef7721; _tb_token_=e65335f81b8bd; xlly_s=1; " \
                  "_m_h5_tk=b60d01a32abe8762b7cd9c92dd2dbbf1_1609677961816; _m_h5_tk_enc=43abb96ba1b31b99c3019ea74af33405;" \
                  " isg=BMvLHl_NEGPQbUyNB6G2yT1zWm-1YN_iSgBb-T3InopgXOu-xTDlMmm9Nlyy-zfa; " \
                  "l=eBLoFikqOe8R7a2JBOfZhurza77T9IRA_uPzaNbMiOCP9gfB5JI1WZ8bX7L6CnGVhsNyR3rEQAfYBeYBq_C-nxvtNSVsrXkmn;" \
                  " tfstk=cvDFBu_TappeGdwWMJwPNVpmibodZpPugOr8tbtO72wckWPhiMQ8j7K4boe90Wf.."
        cookies2 = {i.split('=')[0]: i.split('=')[1] for i in cookie.split(';')}
        return cookies2

    def run(self):
        response = requests.get(self.url, headers=self.headers, cookies=self.cookies())
        print(response.content.decode('utf8'))


if __name__ == '__main__':
    url = 'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?jsv=2.5.1&' \
          'appKey=12574478&t=1609669066258&sign=6a3dd1cc30e92c27ce49a4b7a9175a9a&api=mtop.alimama.union.xt.en.api.entry' \
          '&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2' \
          '&data=%7B%22pNum%22%3A0%2C%22pSize%22%3A%2260%22%2C%22refpid%22%3A%22mm_26632360_8858797_29866178%22%2C' \
          '%22variableMap%22%3A%22%7B%5C%22q%5C%22%3A%5C%22%E7%89%9B%E4%BB%94%E8%A3%A4%5C%22%2C%5C%22navigator%5' \
          'C%22%3Afalse%2C%5C%22union_lens%5C%22%3A%5C%22recoveryid%3A201_11.170.86.133_4369103_1609668600352%3' \
          'Bprepvid%3A201_11.170.86.133_4369103_1609668600352%5C%22%2C%5C%22recoveryId%5C%22%3A%5C%22201_11.8' \
          '8.140.18_4372151_1609669067507%5C%22%7D%22%2C%22qieId%22%3A%2236308%22%2C%22spm%22%3A%22a2e0b.203501' \
          '58.31919782%22%2C%22app_pvid%22%3A%22201_11.88.140.18_4372151_1609669067507%22%2C%22ctm%22%3A%22spm-ur' \
          'l%3Aa2e0b.20350158.search.1%3Bpage_url%3Ahttps%253A%252F%252Fuland.taobao.com%252Fsem%252Ftbsearch%2' \
          '53Frefpid%253Dmm_26632360_8858797_29866178%2526keyword%253D%2525E7%252589%25259B%2525E4%2525BB%252594%' \
          '2525E8%2525A3%2525A4%2526clk1%253D61681b0173c7d16a2ee8e178e3636d9a%2526upsId%253D61681b0173c7d16a2ee8' \
          'e178e3636d9a%2526spm%253Da2e0b.20350158.search.1%2526pid%253Dmm_26632360_8858797_29866178%2526union' \
          '_lens%253Drecoveryid%25253A201_11.170.86.133_4369103_1609668600352%25253Bprepvid%25253A201_11.170.8' \
          '6.133_4369103_1609668600352%22%7D'
    taobao = TaoBao(url)
    taobao.run()
