from bs4 import  BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import python_to_pgadmin as pyToPg

#Links
sok_link = 'https://www.sokmarket.com.tr'
#---

#Arranging chromdriver
width = 1024
height = 768

chrome_options = Options()
chrome_options.page_load_strategy = 'normal'
chrome_options.add_argument('--enable-automation')
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--lang=en')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-insecure-localhost')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-browser-side-navigation')
chrome_options.add_argument('--mute-audio')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--force-device-scale-factor=1')
chrome_options.add_argument(f'window-size={width}x{height}')

chrome_options.add_experimental_option(
    'prefs', {
        'intl.accept_languages': 'en,en_US',
        'download.prompt_for_download': False,
        'download.default_directory': '/dev/null',
        'automatic_downloads': 2,
        'download_restrictions': 3,
        'notifications': 2,
        'media_stream': 2,
        'media_stream_mic': 2,
        'media_stream_camera': 2,
        'durable_storage': 2,
    }
)

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
browser.set_page_load_timeout(1000)  # Timeout 10 seconds
#-------------



#Functions---------------------------

#Verilen linki chromedriver ile açılmasını sağlayan method
def get_source_soup_general(link):
    browser.get(link)
    time.sleep(1)

    pageSource = browser.page_source.encode('utf-8')

    return BeautifulSoup(pageSource,"html.parser")

#Verilen bs4 ile düzenlenmiş kaynak kodundaki bilgileri alıp, istenilen bilgileri döndürür
def get_each_products_info(product_soup_x, id):
    #name
    try:
        product_name = product_soup_x.find("h1",{"class":"info-title"}).text
    except:
        product_name = ""
    
    #price
    try:
        product_price = product_soup_x.find("div",{"class":"pricetag info-price"}).find("span",{"class":""}).text
    except:
        product_price = ""
    
    #brand
    try:
        product_brand = product_soup_x.find(text="Marka").parent.parent.find("span").text
    except:
        product_brand = ""
    
    #origin
    try:
        product_origin = product_soup_x.find(text="Menşei").parent.parent.find("span").text
    except:
        product_origin = ""

    #code
    try:
        product_code = product_soup_x.find(text="Ürün Kodu").parent.parent.find("span").text
    except:
        product_code = ""
    
    #stock info
    try:
        product_stock = product_soup_x.find("div",{"class":"stock-alert"}).text
        product_stock = int(product_stock[4:6])
    except:
        product_stock = ""
    
    try:
        #narrow category, main category
        product_categories = product_soup_x.find("ul",{"class":"breadcrumbs-list"}).find_all("a")
        product_n_category = product_categories[2].text
        product_main_category =product_categories[1].text
    except:
        product_n_category = ""
        product_main_category = ""
    
    return (id,product_code,product_name,product_price,product_brand,product_stock,product_origin,product_main_category,product_n_category)
			
#------------------------------------

#Main--------------------------------


#Şok'un ana sayfasına girer ve oradaki kategori bilgilerini çeker
browser = webdriver.Chrome()
browser.get(sok_link)
time.sleep(1)

pageSource = browser.page_source.encode('utf-8')
pageSource = str(pageSource).replace("amp;","") #son ana kategorideki amp; yüzünden parentına ulaşılmıyordu

main_page_soup = BeautifulSoup(pageSource,"html.parser")


veri = main_page_soup.find_all("h3",{"class":"category-title"})
veri = veri[1:] #dahil olan kampanya itemını çıkarıyoruz
#---------------------


#Hangi kategoride kaç ürün olduğunun bilgisini çeker
quantity = []
for i in range(len(veri)):
    quantity.append([])
#------------------------------------

start_time = time.time()#program çalıştırıldıktan bitene kadar ne kadar süre geçtiğini hesaplar


id_value = 0 #her satır için bir id bilgisi veriyoruz

for i in veri: # Ana kategori
    narrow_ctg_link = sok_link+i.parent['href']

    category_in_soup = get_source_soup_general(narrow_ctg_link)

    category_in_list = category_in_soup.find("div",{"class":"wrapper wide"}).find_all("a")
    for j in category_in_list: # Dar kategori

        products_in_soup = get_source_soup_general(sok_link+j['href'])

        product_in_list = products_in_soup.find_all("a",{"class":"productbox-wrap link-to-pages-productDetail"})
        quantity[veri.index(i)].append({j.text:len(product_in_list)})
        for k in product_in_list: #teker teker ürünler
            product_soup = get_source_soup_general(sok_link+k['href'])

            row_tuple = get_each_products_info(product_soup, id_value) # 1 ürünün tüm bilgilerini al
            pyToPg.InsertData(row_tuple)
            id_value += 1
            browser.back() #bi geri dönüp öyle gir diğer sayfaya
        browser.back()
    browser.back()

browser.close()


"""                """
print("--- %s seconds ---" % (time.time() - start_time))

print(quantity)
