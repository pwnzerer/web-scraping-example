import scrapy

class ProductSpider(scrapy.Spider):
    name = "well_ca_spider"
    
    start_urls = ["https://well.ca/products/navitas-naturals-organic-acai-powder_99112.html"]
    
    def parse(self, response):
        data_dict = {}
        data_dict["product_title"] = response.xpath("/html/body/section/div[1]/div[2]/div[3]/div[1]/span").get()
        data_dict["product_price"] = response.xpath("/html/body/section/div[1]/div[2]/div[3]/div[1]/div[2]/p").get()
        data_dict["product_image"] = response.xpath("/html/body/section/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/div/img/@src").get()
        data_dict["product_overall_rating"] = response.xpath("/html/body/section/div[1]/div[2]/div[5]/div[4]/div/div/div/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/span[2]").get()
        data_dict["product_rating_count"] = response.css(".bv_numReviews_text::text").get()
        data_dict["product_brand"] = response.xpath("/html/body/section/div[1]/div[2]/div[3]/div[1]/a").get()
        
        path_elemnts = response.css("[itemprop='name']::text").getall()
        path_string = " > ".join(path_elemnts)
        data_dict["Categories"] = path_string
        print(data_dict)
        yield data_dict
