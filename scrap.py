
import requests
from bs4 import BeautifulSoup
 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.content)

print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())