import scrapy
#from .. items import JobsScrapyItem
from selenium import webdriver
import time
from scrapy.http import FormRequest, TextResponse

#----------Class for scraping btc popular addresses----------
class Super(scrapy.Spider):
    name = "amazon"
    start_urls = ['https://resumes.indeed.com/resume/91d7f36dfe695dee?s=l%3Dnoida%26q%3Dpython%2520developer%26searchFields%3D']

    def __init__(self, keyword=None, **kwargs):
        self.keyword = keyword
        self.driver = webdriver.PhantomJS(r"C:/Users/etech/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    

    def parse(self,response):
        self.driver.get(response.url)

        selector = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
        time.sleep(4)
        items = selector.css('#education-EeiiqoQoZTGTLg2SBVVUiQ span::text').extract()
        time.sleep(2)
        print(items)

        '''    
    driver.get("https://resumes.indeed.com/resume/91d7f36dfe695dee?s=l%3Dnoida%26q%3Dpython%2520developer%26searchFields%3D")
    html = driver.page_source
    title = driver.find_element_by_class_name('locality').text
    

    start_urls = [
                'https://resumes.indeed.com/resume/91d7f36dfe695dee?s=l%3Dnoida%26q%3Dpython%2520developer%26searchFields%3D'
        ]

    def start_requests(self):        
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
        
    def parse(self,response):
        print("respo nse ===============================>",response.status,"<=========================")
        validating = response.xpath('//a')
        print(response.text)
        '''    
        
        
        '''
        if validating:
            spliting = validating.split()
            number_results = spliting[-1]
            print("numbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrr",number_results)
            if int(number_results) > 10000:
                items = JobsScrapyItem()
                data_count = len(response.css("#jdUrl::text").extract())
                for indx in range(0,data_count):
                    print("indexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",indx)
                    job_title = response.css("#jdUrl::text").extract()[indx]
                    company_name = response.css(".org::text").extract()[indx]
                    exprience_required = response.css(".exp::text").extract()[indx]
                    job_location = response.css(".loc span::text").extract()[indx]
                    key_skills = response.css(".skill::text").extract()[indx]
                    source_url = response.url
                    source = "Naukri.com"

                    items['job_title']=job_title
                    items['company_name']=company_name
                    items['exprience_required']=exprience_required
                    items['job_location']=job_location
                    items['key_skills']=key_skills
                    items['source_url']=source_url
                    items['source']=source
                    yield items     
                next_page = response.css("div .pagination a::attr(href)").extract()
                if next_page:
                    next_page_url = next_page[-1]
                    print("next_page_url===============================>",next_page_url,"=========================>")
                    yield scrapy.Request(url=next_page_url,meta = {
                      'dont_redirect': True,
                      'handle_httpstatus_list': [302]
                  },callback=self.parse)
                else:
                    print("no next pageeeeeeeeeeeeeeeeeeeee url available")
                    pass
            else:
                print("results not ==========================> 10000")
                pass
        else:
            print("number of total results not ==========================> available")
            pass
        '''