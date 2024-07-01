import scrapy
import csv
from recipe_scraper.itemloaders import RecipeScraperLoader 
from recipe_scraper.items import RecipeScraperItem

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
        recipe = RecipeScraperLoader(item=RecipeScraperItem(), selector=recipe_block)
        recipe.add_css('id','div::attr(data-recipe-id)')
        recipe.add_css('name','div.wprm-recipe-header > h2::text')
        recipe.add_value('url', response.url)
        recipe.add_css('rating','div.wprm-recipe-rating-details ::text')
        recipe.add_value('ingredients_list', recipe_block.css('div.wprm-recipe-ingredient-group > ul > li > span.wprm-recipe-ingredient-name ::text').extract())
        recipe.add_css('num_servings','div::attr(data-servings)')
        recipe.add_css('nutrition_info','div.wprm-nutrition-label-container > span ::text')
        recipe.add_css('ww_value','div.wprm-meta-nutrition > div > div > span::text')
        recipe.add_css('duration','div.wprm-cooktimes-wrap > div.wprm-recipe-times-container > div ::text')
        recipe.add_value('course',recipe_block.css('span.wprm-recipe-course ::text').extract())
        recipe.add_value('cuisine',recipe_block.css('span.wprm-recipe-cuisine ::text').extract())
        recipe.add_value('categories_list', response.css('div.post-categories-wrapper > ul > li ::text').extract())
        yield recipe.load_item()

        # Append the recipe details to the CSV file
        with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'id', 'name', 'url', 'rating', 'ingredients_list',
                'num_servings', 'nutrition_info', 'ww_value', 'duration', 'course',
                'cuisine', 'categories_list'
            ])
            writer.writerow(recipe.load_item())