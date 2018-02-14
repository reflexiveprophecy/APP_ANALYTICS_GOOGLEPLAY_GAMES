from scrapy import Spider, Request
from googleplay.items import GoogleplayItem

class GoogleplaySpider(Spider):
    name = 'googleplay_spider'
    allowed_urls = ['https://play.google.com/store']
    start_urls = ['https://play.google.com/store/apps/category/GAME']

    def parse(self, response):
        genre_list = response.xpath('//div[@class="leaf-submenu-link-wrapper"]//a[@href]/@href').extract()
        #genre_list = response.xpath('//a[@class="child-submenu-link"]/@href').re(r'.*GAME.*')
        links = ['https://play.google.com' + link for link in genre_list]

        for url in links:
            yield Request(url, callback = self.parse_top)


    def parse_top(self, response):
        category_list = response.xpath('//a[@class = "title-link id-track-click"]/@href').extract()
        links = ['https://play.google.com'+ link for link in category_list][1:]

        for url in links:
            yield Request(url, callback = self.parse_toplist)


    def parse_toplist(self, response):
        spans = response.xpath('//span[@class="preview-overlay-container"]/@data-docid').extract()
        links = ['https://play.google.com/store/apps/details?id=' + span for span in spans]
        top_list = response.xpath('//h2/text()').extract_first()


        for url in links:
            yield Request(url, callback = self.parse_detail, meta = {'top_list':top_list})

    def parse_detail(self, response):
        top_list = response.meta['top_list']


        #indexing doesn't work because some apps don't have certain information
        #
        appname = response.xpath('//div[@class="id-app-title"]/text()').extract_first()
        companyname = response.xpath("//span[@itemprop='name']/text()").extract_first()
        gamecategory = response.xpath('//span[@itemprop="genre"]/text()').extract_first()
        starrating = response.xpath('//div[@class="score"]/text()').extract_first()
        appprice = response.xpath('//button//span/text()').re(r'^\$.+[Buy]')
        badgetitle = response.xpath('//span[@class = "badge-title"]/text()').extract_first()
        inapppurchase = response.xpath('//div[@class="inapp-msg"]/text()').extract_first()
        inappprice = response.xpath('//div[@class="content"]/text()').re(r'^\$.*')
        ads = response.xpath('//span[@class="ads-supported-label-msg"]/text()').extract_first()
        ratingnums = response.xpath('//span[@class="reviews-num"]/text()').extract_first()
        newcontent = response.xpath('//div[@class="recent-change"]/text()').extract()
        version = response.xpath('//div[@itemprop = "softwareVersion"]/text()').extract_first()
        requiredsystem = response.xpath('//div[@itemprop = "operatingSystems"]/text()').extract_first()
        developerinfo = response.xpath('//div[@class="content physical-address"]/text()').extract_first()
        contentrating = response.xpath('//div[@class="meta-info contains-text-link"]/div[@class = "content"]/text()').extract()
        installs = response.xpath('//div[@itemprop = "numDownloads"]/text()').extract_first()
        updatedate = response.xpath('//div[@itemprop = "datePublished"]/text()').extract_first()
        imagenum = response.xpath('//img[@class = "full-screenshot"]/@data-expand-target').extract()[-1]



        reviews = response.xpath('//div[@class="single-review"]')
        for review in reviews:
            reviewcontent = ''.join(review.xpath('./div[@class="review-body with-review-wrapper"]/text()').extract()).strip()
            reviewer = review.xpath('.//span[@class="author-name"]/text()').extract_first().strip()
            reviewrating = review.xpath('.//div[@class="tiny-star star-rating-non-editable-container"]/@aria-label').re(r'\d')
            reviewdate = review.xpath('.//span[@class = "review-date"]/text()').extract_first()

            item = GoogleplayItem()
            item['appname'] = appname
            item['companyname'] = companyname
            item['gamecategory'] = gamecategory
            item['starrating'] = starrating
            item['appprice'] = appprice
            item['badgetitle'] = badgetitle
            item['inapppurchase'] = inapppurchase
            item['inappprice'] = inappprice
            item['ads'] = ads
            item['ratingnums'] = ratingnums
            item['newcontent'] = newcontent
            item['version'] = version
            item['requiredsystem'] = requiredsystem
            item['developerinfo'] = developerinfo
            item['contentrating'] = contentrating
            item['installs'] = installs
            item['updatedate'] = updatedate
            item['imagenum'] = imagenum
            item['toplist'] = toplist
            item['reviewer'] = reviewer
            item['reviewcontent'] = reviewcontent
            item['reviewrating'] = reviewrating
            item['reviewdate'] = reviewdate

            yield item
