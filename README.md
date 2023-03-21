# Webscrapping Market Datas with Python/Selenium and Sending Them to Postgresql Database
 
## Requirements
### Make sure all Python libraries installed:
* pip install bs4
* pip install chromedriver-py
* pip install selenium
### Download correct 'chromedriver' which is compatible with your Google Chrome Browser
#### Learn: 
* Click Right-top 3 dot icon on Google Chrome -> Help -> About Google Chrome
* You will see your current Google Chrome version.
### Define correct values for your variables in 'python_to_pgadmin.py' 
* Learn your own Postgresql informations.
* Define: hostname, database, username, pwd(password), port_id correctly.

## Run 'marketveriler-selenium.py' file, it might take long time


# Some Results from the Database:
(Note: This results are old and not 100% correct, but codes are remastered and scrapping datas correctly!)

* In Postgresql we got some informations about our datas.
select * from products;
![image](https://user-images.githubusercontent.com/44267861/226697720-2caaacff-dd98-44b8-b663-d90112f18dcc.png)
