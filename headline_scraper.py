# This is a special tool (library) that helps us send messages to websites
# Think of it like a digital postman that can fetch web pages for us
import requests

# This is another special tool that helps us read and understand website content
# Imagine it like a translator that turns messy website code into something we can read
from bs4 import BeautifulSoup

# This is a function (like a recipe) that will help us grab headlines from a website
def scrape_headlines(url):
    try:
        # Imagine this like sending a letter to a website asking "Can you send me your content?"
        # 'url' is the address of the website we want to visit
        response = requests.get(url)
        
        # This is like checking if the letter was delivered correctly
        # If something went wrong (like a bad address), it will raise an alarm (exception)
        response.raise_for_status()
        
        # Now we're using our special translator (BeautifulSoup) to understand the website's language
        # 'html.parser' is like a specific dictionary that helps translate website code
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This is like telling our translator: "Find me all the important text boxes"
        # We're looking for different types of headline tags that websites use
        # It's like searching for all the big, bold text on a page
        headlines = soup.find_all(['h1', 'h2', 'h3', 'article-title', 'headline'])
        
        # Create an empty list to store the headlines we find
        # Think of this like an empty basket we'll fill with headline texts
        headline_texts = []
        
        # Go through each headline we found
        for headline in headlines:
            # Extract the text from the headline, removing extra spaces
            # 'strip=True' is like cleaning up the text, removing extra whitespace
            headline_text = headline.get_text(strip=True)
            
            # Only add the headline to our basket if it's not empty
            if headline_text:
                headline_texts.append(headline_text)
        
        # Give back the list of headlines we collected
        return headline_texts
    
    # If anything goes wrong while trying to get the website (like no internet)
    except requests.RequestException as e:
        # Print out what went wrong
        print(f"Error fetching the website: {e}")
        # Return an empty list if we couldn't get any headlines
        return []

# This is the main function that runs when we start our program
def main():
    # The website we want to get headlines from
    url = 'https://ecomXf.com'
    
    # Use our headline grabbing function to get headlines
    headlines = scrape_headlines(url)
    
    # Print out the headlines we found
    print("Headlines found:")
    # 'enumerate' helps us number the headlines
    # So instead of just listing headlines, we'll list them like:
    # 1. First Headline
    # 2. Second Headline
    # and so on...
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")

# This is a special line that says "Run the main function when we start the program"
if __name__ == '__main__':
    main()
