#Crawler code
import scrapy

class FlipkartSpider(scrapy.Spider):
    name = "Flipkart"
    start_urls = ['https://www.flipkart.com/philips-qt3310-15-runtime-30-min-trimmer-men/p/itmc7efd5003ea13?pid=SHVEHHFBMHJZUZWS&lid=LSTSHVEHHFBMHJZUZWSME3T6F&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&fm=SEARCH&iid=1e7ea25d-c1f2-46ae-814c-6b95972b7aa4.SHVEHHFBMHJZUZWS.SEARCH&ppt=sp&ppn=sp&ssid=6j016yaa0w0000001589609472273&qH=705a17deac7a99db']

    def parse(self,response):
        SET_SELECTOR  = '.set'
        for flipkart in response.css(SET_SELECTOR):
            Title_Selector = 'h1::text'
            yield{
                'name': flipkart.css(Title_Selector).extract_first(),
            }


