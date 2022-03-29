# Automated Wikipedia Page Table Scraping
## Goal: To extract table data from a Wikipedia page into an Excel spreadsheet to make research data easier to obtain. 
* Wikipedia is does not provide ways to download raw data directly from the page, resulting in having to manually extract.
* This wastes time when researchers may need multiple pages of raw data.
* This was created to simplify and automate the process of copying and pasting the data into spreadsheet.
## Tools:
* Python
  * BeautifulSoup - bs4
  * json
  * requests
  * pandas
* HTML

### Step 1: Website Link
Select and copy a Wikipedia link that contains raw data (organized in a table)
- Provided Testers: 
  * https://en.wikipedia.org/wiki/List_of_countries_by_percentage_of_population_living_in_poverty
  * https://en.wikipedia.org/wiki/The_World%27s_Billionaires
  * https://en.wikipedia.org/wiki/List_of_U.S._states_by_median_home_price
  * https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions

### Step 2: Directory
Save file to desired directory so that the files will save in the same location

### Step 3: Imported Libraries
Unless already installed, open terminal and install libraries:
* pip install json
* pip install requests
* pip install pandas
* pip install beautifulsoup4

## Potential Improvements:
- Parse through sheets containing Wikipedia links
- Broaden the scope for different websites
- Search a database website to parse data
