# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipeScraperItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()
    ingredients_list = scrapy.Field()
    num_servings = scrapy.Field()
    nutrition_info = scrapy.Field()
    ww_value = scrapy.Field()
    duration = scrapy.Field()
    course = scrapy.Field()
    cuisine = scrapy.Field()
    categories_list = scrapy.Field()   
