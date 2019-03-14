# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['shiyanlou.com']

    @property
    def start_urls(self):
        url_tmp = 'https://www.shiyanlou.com/user/{}'
        return (url_tmp.format(i) for i in range(425000,424900,-10))

    def parse(self, response):
        #yield UserItem({
        yield {
            'name': response.xpath('//div[@class="userinfo-banner-meta"]'
                    '/span[@class="username"]/text()').extract_first(),
            'type': response.xpath('//a[@class="member-icon"]'
                    '/img/@title').extract_first(default='普通会员'),
            'status': response.xpath('//div[@class="userinfo-banner-status"]'
                      '/span[1]/text()').extract_first(),
            'school_job': response.xpath('//div[@class="userinfo-banner-status"]'
                          '/span[2]/text()').extract_first(),
            'join_date': response.xpath(
                         '//span[@class="join-date"]/text()').extract_first(),
            'level': response.css('span.user-level::text').extract_first(),
            'learn_courses_num': response.css(
                                 'span.latest-learn-num::text').extract_first()
        }
