import scrapy
from seiya.spider.items import JobItem

class JobsSpider(scrapy.Spider):
    #拉勾网职位数据爬虫
    name = 'jobs'
    allowed_domains = ['lagou.com']
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'user_trace_token=20190502222717-689cbec5-f27d-46ad-a189-91518b1ba2f8; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1556807247,1556958216,1557285796; _ga=GA1.2.112375705.1556807247; LGUID=20190502222727-68eec688-6ce6-11e9-9dd7-5254005c3644; LG_LOGIN_USER_ID=08e9e145b49f04386659832524fdd3016ceb337013c4216b08726ab9cdb674e7; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=5ac8a3994947726134cd047054454c634613e883e9a88f90ccf16c9cea166655; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEEAAJA20164625575CE75D610247FF447F8ACC; SEARCH_ID=70982830499e412f9dc12ab2afd4bb23; _putrc=69C4385F402C7776123F89F2B170EADC; X_HTTP_TOKEN=47cabfb0bd1db0d10095827551d1998824bdd9363d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557285901; _gat=1; _gid=GA1.2.624163189.1557285797; LGSID=20190508112317-9f672bd9-7140-11e9-9ed0-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; LGRID=20190508112501-dd07b917-7140-11e9-8971-525400f775ce; login=true; unick=%E5%90%B4%E4%BC%9F%E5%8A%9B; TG-TRACK-CODE=index_code',
        'Host':'www.lagou.com',
        'Upgrade-Insecure-Requsets':'1'
}

    def start_requests(self):
        urls = ['https://www.lagou.com/zhaopin/{}/'.format(i) for i in range(26,31)]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,headers=self.headers)

    def parse(self,response):
        for job in response.css('ul.item_con_list li'):
            title = job.xpath('.//div[@class="list_item_top"]/div[@class="position"]/div[@class="p_top"]/a/h3/text()').extract_first()
            city = job.xpath('.//div[@class="list_item_top"]/div[@class="position"]/div[@class="p_top"]/a/span/em/text()').extract_first()
            salary = job.xpath('.//div[@class="list_item_top"]/div[@class="position"]/div[@class="p_bot"]/div[@class="li_b_l"]/span/text()').extract_first()
            experience,education = job.xpath('.//div[@class="list_item_top"]/div[@class="position"]/div[@class="p_bot"]/div[@class="li_b_l"]/text()').re(r'(.+)\s*/\s*(.+)')
            tags = job.xpath('.//div[@class="list_item_bot"]/div[@class="li_b_l"]/span/text()').extract()
            company = job.xpath('.//div[@class="list_item_top"]/div[@class="company"]/div[@class="company_name"]/a/text()').extract_first()
            yield JobItem({
                'title':title,
                'city':city,
                'salary':salary,
                'experience':experience,
                'education':education,
                'tags':tags,
                'company':company
                })
