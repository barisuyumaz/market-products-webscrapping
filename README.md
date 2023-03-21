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
=============
* select * from products;
![image](https://user-images.githubusercontent.com/44267861/226697720-2caaacff-dd98-44b8-b663-d90112f18dcc.png)
=============
* select origin,count(*) from products where origin != 'TÜRKİYE' group by origin order by origin; --hangi ülkenin kaç ürünü var
![product_origin_bar](https://user-images.githubusercontent.com/44267861/226697996-a0865e17-17bb-47c2-8333-79d4d0d44809.png)
=============
* select product_brand,count(*) as itemcount from products 
* where product_brand != ''
* group by product_brand order by itemcount desc limit 10;
* --en çok ürünü bulunan 10 marka
![image](https://user-images.githubusercontent.com/44267861/226698814-e2b0d28e-0476-46f5-8b99-01c8a2e4502c.png)
=============
select product_category,count(*) as itemcount from products
group by product_category order by itemcount desc; --miktar olarak en çok hangi çeşitte ürün var?
![kategori-miktar](https://user-images.githubusercontent.com/44267861/226699546-a189e2aa-aa93-4883-a857-8616f63a8e80.png)
![kategori-miktar-pasta](https://user-images.githubusercontent.com/44267861/226699564-d708e1dc-5531-4624-a27d-f6a8206177e7.png)

