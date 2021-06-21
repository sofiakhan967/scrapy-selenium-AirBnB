import scrapy
from scrapy_selenium import SeleniumRequest

class AlibaugSpider(scrapy.Spider):
    name = 'alibaug'
    #allowed_domains = ['www.airbnb.in']
   # url= ['']
    def start_requests(self):
        yield SeleniumRequest(url='https://www.airbnb.co.in/s/Alibag/homes?refinement_paths%5B%5D=%2Fhomes&search_type=filter_change&tab_id=home_tab&place_id=ChIJa_kmmDt66DsRgYv2gFZOY6k&flexible_trip_dates%5B%5D=july&flexible_trip_dates%5B%5D=june&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&room_types%5B%5D=Entire%20home%2Fapt',callback=self.parse)
    def parse(self, response):
        for hotel in response.xpath('//div[@class="_fhph4u"]/div[@class="_8ssblpx"]'):
            yield{
                'name':hotel.xpath('.//div/div[1]/div/div/div[@class="_8s3ctt"]/div[2]/div[@class="_r6zroz"]/div/div[@class="_5kaapu"]/span/text()').get(),
                'price':hotel.xpath('.//div/div[1]/div/div/div[@class="_8s3ctt"]/div[2]/div[@class="_h34mg6"]/div[@class="_ls0e43"]/div/div/span[@class="_krjbj"]/text()').get(),
                'rating':hotel.xpath('.//div/div[1]/div/div/div[@class="_8s3ctt"]/div[2]/div[@class="_h34mg6"]/div[@class="_1hxyyw3"]/span/span[2]/text()').get(),
            }
        next_page=response.xpath('//div[@class="_jro6t0"]/a[@class="_za9j7e"]/@href').get()
        if next_page:
            next_page1=f"https://www.airbnb.co.in{next_page}"
            yield SeleniumRequest(url=next_page1,callback=self.parse)


          #  'price':hotel.xpath('.//div/div/div/div[2]/div/div/div/div[2]/div[2]/div[5]/div[2]/div/div/div/span/text()').get()
# //div[@class="_fhph4u"]/div[@class="_8ssblpx"]/div/div[1]/div/div/div[@class="_8s3ctt"]/div[2]/div[@class="_h34mg6"]/div[@class="_ls0e43"]/div/div/span/text()       

#//div[@class="_fhph4u"]/div[@class="_8ssblpx"]/div/div[1]/div/div/div[@class="_8s3ctt"]/div[2]/div[@class="_r6zroz"]/div/div[@class="_5kaapu"]/span/text()