
import requests
from bs4 import BeautifulSoup
s = requests.session()
payload = {
    'log' : 'admin',
    'pwd' : '123456aA',
}
response = s.post("http://45.79.43.178/source_carts/wordpress/wp-login.php",data = payload)
r = s.get("http://45.79.43.178/source_carts/wordpress/wp-admin/").text
soup = BeautifulSoup(r ,'lxml')
x = soup.find("span",class_="display-name").text
print(x)