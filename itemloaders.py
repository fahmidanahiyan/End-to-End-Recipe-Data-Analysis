from itemloaders.processors import Join, TakeFirst
from scrapy.loader import ItemLoader

class RecipeScraperLoader(ItemLoader):
    default_output_processor = TakeFirst()
    rating_in = Join()
    nutrition_info_in = Join()
    duration_in = Join()
    ingredients_list_in = Join(separator=', ')
    course_in = Join(separator=', ')
    cuisine_in = Join(separator=', ')
    categories_list_in = Join(separator=', ')

