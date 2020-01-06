import scrapy
from .. items import JobsScrapyItem
import requests


class jobsSpider(scrapy.Spider):
    name = "jobs"
    
    custom_settings = {
        'ITEM_PIPELINES': {
            'indeed_scraper.pipelines.JobsScrapyPipeline': 30000
        }
    }
    headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'appid':'121',
    'systemid':'Naukri'
    }

    start_urls = [
                #'https://www.naukri.com/accounting-jobs?xt=catsrch&qf[]=1',
                #'https://www.naukri.com/bank-jobs?xt=catsrch&qf[]=6'
                #'https://www.naukri.com/hr-jobs?xt=catsrch&qf[]=12',
                #'https://www.naukri.com/application-programming-jobs?xt=catsrch&qf[]=24.01',
                'https://www.naukri.com/information-technology-jobs?xt=catsrch&qf[]=24',
                'https://www.naukri.com/bpo-jobs?xt=catsrch&qf[]=8',
                #'https://www.naukri.com/marketing-jobs?xt=catsrch&qf[]=15',
                #'https://www.naukri.com/pharma-jobs?xt=catsrch&qf[]=16',
                #'https://www.naukri.com/maintenance-jobs?xt=catsrch&qf[]=19',
                #'https://www.naukri.com/sales-jobs?xt=catsrch&qf[]=22',
                #'https://www.naukri.com/teaching-jobs?xt=catsrch&qf[]=36',
                #'https://www.naukri.com/bpo-jobs?xt=catsrch&qi[]=7',
                #'https://www.naukri.com/bank-jobs?xt=catsrch&qi[]=14',
                #'https://www.naukri.com/engineering-jobs?xt=catsrch&qi[]=12',
                #'https://www.naukri.com/teaching-jobs?xt=catsrch&qi[]=26',
                #'https://www.naukri.com/information-technology-jobs?xt=catsrch&qi[]=25',
                #'https://www.naukri.com/medical-jobs?xt=catsrch&qi[]=20',
                #'https://www.naukri.com/recruitment-jobs?xt=catsrch&qi[]=34',
                #'https://www.naukri.com/consultant-jobs?xt=catsrch&qi[]=52'
        ]

    def start_requests(self):        
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
        
    def parse(self,response):
        validating = response.css(".srp_container div::attr(id)").extract()
        if validating:
            del validating[0]
            items = JobsScrapyItem()
            for val in validating:
                idss = "#"+val
                variable = response.css(""+idss+"::attr(data-url)").get()
                if variable is not None:
                    x = variable.split("?",1)[1] 
                    respon = requests.get(url="https://www.naukri.com/jobapi/v3/job/"+str(val)+"?"+str(x),headers=self.headers)
                    res = respon.json()
                    if "jobDetails" in res:
                        if res['jobDetails'] is not None:
                            jobs_details = res['jobDetails'] if "jobDetails" in res else None
                            job_applicants = jobs_details['applyCount'] if "applyCount" in jobs_details else None
                            description = jobs_details['description'] if "description" in jobs_details else None
                            staticCompanyName = jobs_details['staticCompanyName'] if "staticCompanyName" in jobs_details else None
                            industry = jobs_details['industry'] if "industry" in jobs_details else None 
                            staticUrl = jobs_details['staticUrl'] if "staticUrl" in jobs_details else None
                            recruiterProfile = jobs_details['recruiterProfile'] if "recruiterProfile" in jobs_details else None
                            title = jobs_details['title'] if "title" in jobs_details else None
                            walkIn = jobs_details['walkIn'] if "walkIn" in jobs_details else None
                            maximumExperience = jobs_details['maximumExperience'] if "maximumExperience" in jobs_details else None
                            jobType = jobs_details['jobType'] if "jobType" in jobs_details else None
                            viewCount = jobs_details['viewCount'] if "viewCount" in jobs_details else None
                            email = jobs_details['email'] if "email" in jobs_details else None
                            minimumExperience = jobs_details['minimumExperience'] if "minimumExperience" in jobs_details else None
                            employmentType = jobs_details['employmentType'] if "employmentType" in jobs_details else None
                            contactName = jobs_details['contactName'] if "contactName" in jobs_details else None
                            companyDetail = jobs_details['companyDetail'] if "companyDetail" in jobs_details else None

                            companyname = companyDetail['name'] if "name" in companyDetail else None
                            websiteUrl = companyDetail['websiteUrl'] if "websiteUrl" in companyDetail else None
                            details = companyDetail['details'] if "details" in companyDetail else None
                            address = companyDetail['address'] if "address" in companyDetail else None


                            jobIconType = jobs_details['jobIconType'] if "jobIconType" in jobs_details else None
                            jobId  = jobs_details['jobId'] if "jobId" in jobs_details else None
                            companyId = jobs_details['companyId'] if "companyId" in jobs_details else None
                            createdDate = jobs_details['createdDate'] if "createdDate" in jobs_details else None

                            locations = jobs_details['locations'] if "locations" in jobs_details else None
                            keySkills = jobs_details['keySkills'] if "keySkills" in jobs_details else None

                            vacancy = jobs_details['vacancy'] if "vacancy" in jobs_details else None
                            salaryDetail = jobs_details['salaryDetail'] if "salaryDetail" in jobs_details else None

                            seo = res['seo']
                            if 'ambitionBoxDetails' in res:
                                ambitionBoxDetails = res['ambitionBoxDetails'] 
                                companyInfo = ambitionBoxDetails['companyInfo'] if "companyInfo" in ambitionBoxDetails else None
                                reviews = ambitionBoxDetails['reviews'] if "reviews" in ambitionBoxDetails else None
                            else:
                                companyInfo = None
                                reviews = None

                        
                            items['job_applicants']=job_applicants
                            items['description']=description
                            items['staticCompanyName']=staticCompanyName
                            items['industry']=industry
                            items['staticUrl']=staticUrl
                            items['title']=title
                            items['walkIn']=walkIn
                            items['maximumExperience']=maximumExperience
                            items['jobType']=jobType
                            items['minimumExperience']=minimumExperience
                            items['employmentType']=employmentType
                            items['contactName']=contactName
                            items['websiteUrl']=websiteUrl
                            items['companyname']=companyname
                            items['details']=details
                            items['address']=address
                            items['jobIconType']=jobIconType
                            items['jobId']=jobId
                            items['companyId']=companyId
                            items['createdDate']=createdDate
                            items['locations']=locations
                            items['keySkills']=keySkills
                            items['vacancy']=vacancy
                            items['salaryDetail']=salaryDetail
                            items['companyInfo']=companyInfo
                            items['reviews']=reviews
                            items['seo']=seo
                            items['recruiterProfile']=recruiterProfile
                            items['viewCount'] = viewCount
                            items['email'] = email
                            yield items  
                        else:
                            pass
                    else:
                        pass
                else:
                    pass   
            next_page = response.css("div .pagination a::attr(href)").extract()
            if next_page:
                next_page_l = next_page[-1]
                print("next_page_url===============================>",next_page_l,"=========================>")
                yield scrapy.Request(url=next_page_l,callback=self.parse)
            else:
                pass        
        else:
            pass
                
                



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