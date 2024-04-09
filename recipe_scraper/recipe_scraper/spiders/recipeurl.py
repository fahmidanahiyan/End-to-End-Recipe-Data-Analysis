import scrapy
import csv

class RecipeurlSpider(scrapy.Spider):
    name = "recipeurl"
    start_urls = ["https://www.skinnytaste.com/recipe-index/"]

    def __init__(self, *args, **kwargs):
        super(RecipeurlSpider, self).__init__(*args, **kwargs)
        self.i = 1

        self.output_file = 'recipes.csv'  

        # Open the CSV file and write header
        with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'id', 'name', 'url', 'rating', 'ingredients_list',
                'num_servings', 'nutrition_info', 'ww_value', 'duration', 'course',
                'cuisine', 'categories_list'
            ])
            writer.writeheader()

    def parse(self, response):
        items = response.css('article.type-post')
        for item in items:
            if (item.css('div.wprm-ww-points')):
                yield{
                    'id' : item.css('article::attr(id)').get(),
                    'name' : item.css('h2.entry-title > a::text').get(),
                    'url' : item.css('h2.entry-title > a::attr(href)').get()                    
                }
                # Follow the URL of the recipe to parse more information
                yield scrapy.Request(url=item.css('h2.entry-title > a::attr(href)').get(), callback=self.parse_recipe)
        self.i += 1
        if self.i <= 105:  
            next_page = f'https://www.skinnytaste.com/recipe-index/?_paged={self.i}'
            yield response.follow(next_page, callback=self.parse)

    def parse_recipe(self, response):
        recipe_block = response.css('div.wprm-recipe-container')
        recipe_details = {
            'id': recipe_block.css('div::attr(data-recipe-id)').get(),
            'name': recipe_block.css('div.wprm-recipe-header > h2::text').get(),
            'url': response.url,
            'rating': recipe_block.css('div.wprm-recipe-rating-details ::text').extract(),
            'ingredients_list': recipe_block.css('div.wprm-recipe-ingredient-group > ul > li > span.wprm-recipe-ingredient-name ::text').extract(),
            'num_servings': recipe_block.css('div::attr(data-servings)').get(),
            'nutrition_info': recipe_block.css('div.wprm-nutrition-label-container > span ::text').extract(),
            'ww_value': recipe_block.css('div.wprm-meta-nutrition > div > div > span::text').get(),
            'duration': recipe_block.css('div.wprm-cooktimes-wrap > div.wprm-recipe-times-container > div ::text').extract(),
            'course': recipe_block.css('span.wprm-recipe-course ::text').extract(),
            'cuisine': recipe_block.css('span.wprm-recipe-cuisine ::text').extract(),
            'categories_list': response.css('div.post-categories-wrapper > ul > li ::text').extract()
        }
        yield recipe_details

        # Append the recipe details to the CSV file
        with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'id', 'name', 'url', 'rating', 'ingredients_list',
                'num_servings', 'nutrition_info', 'ww_value', 'duration', 'course',
                'cuisine', 'categories_list'
            ])
            writer.writerow(recipe_details)