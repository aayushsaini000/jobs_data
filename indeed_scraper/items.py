# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JobsScrapyItem(scrapy.Item):
    job_applicants = scrapy.Field()
    description = scrapy.Field()
    staticCompanyName = scrapy.Field()
    industry = scrapy.Field()
    staticUrl = scrapy.Field()
    title = scrapy.Field()
    walkIn = scrapy.Field()
    address = scrapy.Field()
    maximumExperience = scrapy.Field()
    jobType = scrapy.Field()
    minimumExperience = scrapy.Field()
    employmentType = scrapy.Field()
    contactName = scrapy.Field()
    companyname = scrapy.Field()
    websiteUrl = scrapy.Field()
    details = scrapy.Field()
    jobIconType = scrapy.Field()
    jobId = scrapy.Field()
    companyId = scrapy.Field()
    createdDate = scrapy.Field()
    locations = scrapy.Field()
    keySkills = scrapy.Field()
    vacancy = scrapy.Field()
    salaryDetail = scrapy.Field()
    companyInfo = scrapy.Field()
    reviews = scrapy.Field()
    seo = scrapy.Field()
    recruiterProfile= scrapy.Field()
    viewCount = scrapy.Field()
    email = scrapy.Field()
    pass
