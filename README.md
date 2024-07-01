# End-to-End Recipe Data Analysis

You can check out the full project presentation video [here](https://youtu.be/JQI9JXezkBg).

## Table of Contents

- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Data Cleaning and Processing](#data-cleaning-and-processing)
- [Data Modeling](#data-modeling)
- [Data Visualization](#data-visualization)
- [Dashboards](#dashboards)
- [Conclusion](#conclusion)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project involves performing data analytics on recipe data collected from a popular recipe website. The analysis includes various aspects such as ratings, nutritional values, preparation time, ingredients list, course, cuisine, and category.

## Data Collection

I collected comprehensive data on all recipes from the website [Skinnytaste]([https://www.skinnytaste.com/]). For each recipe, I extracted the following information: recipe ID, name, URL, rating, ingredients list, number of servings, nutritional information, Weight Watchers value, duration, course, cuisine, and categories list.
I used Scrapy, a fast and high-level web crawling and web scraping framework, to collect the data. The data was structured using an item schema and cleaned during parsing using Scrapy's ItemLoaders.

## Data Cleaning and Processing

The raw dataset required extensive cleaning:
- Split the 'rating' column into 'rating value' and 'votes number'.
- Created individual columns for each nutrition type from the 'nutrition_info' column.
- Split the 'duration' column into separate columns for each duration type.
- Used the `ingredient parser` Python package for parsing ingredient names from ingredient sentences.
- Cleaned the 'course', 'cuisine', and 'categories' columns.

## Data Modeling

Separate dataframes were created for unique lists of ingredients, courses, cuisines, and categories, and saved as CSV files. Data files were also created for relational mapping to link recipes with their respective ingredients, courses, cuisines, and categories.

## Data Visualization

Two interactive dashboards were created in Tableau to analyze and share insights using multiple visualizations from bar chart, line chart to word cloud, scatter plot and tree map. Filters for category, course, and cuisine name were used to interact with visualizations.

- Compared cuisines based on ratings and courses based on duration using tree map and area map.
- Analyzed the distribution of commonly used ingredients using word clouds.
- Examined the correlation between the number of servings and total recipe duration using scatter plot.
- Visualized the nutritional value distribution across different courses using line charts and bar charts.
- Investigated the Weight Watchers values for different categories and how each nutrition type contributes to the Weight Watchers values.

## Conclusion

This project provides comprehensive insights into recipe data, highlighting patterns in ingredients, duration, and nutritional values across different courses, cuisines, and categories. The interactive dashboards allow users to explore the data dynamically.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fahmidanahiyan/Recipe-Data-Analysis.git

2. Install the required packages:
   ```bash  
    pip install -r requirements.txt
   
## Usage

1. Run the data scraping script:
   ```bash 
   scrapy crawl recipeurl

2. You will get a file named 'recipes.csv' containing all the raw data.
   
3. Import the file as df in the data processing notebook.

4. Initiate data processing
   ```bash  
    jupyter nbconvert --execute Recipe_data_processing.ipynb
   
5. You will get nine dataset files. Load them into Tableau.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements. If you come up with some interesting findings, add the Tableau dashboard link to the repo.

## License

All Rights of this data belong to Skinnytaste.com
