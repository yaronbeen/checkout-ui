import asyncio
import json
from pyppeteer import launch

async def scrape_matchmaker_podcasts():
    # Launch a new browser instance
    browser = await launch()
    
    try:
        # Open a new page
        page = await browser.newPage()
        
        # Navigate to the matchmaker.fm website
        await page.goto('https://matchmaker.fm', {'waitUntil': 'networkidle0'})
        
        # Wait for the podcast elements to load
        await page.waitForSelector('.podcast-item', {'timeout': 10000})
        
        # Extract podcast information using page.evaluate to run JavaScript in the browser context
        podcasts = await page.evaluate('''() => {
            const podcastItems = document.querySelectorAll('.podcast-item');
            return Array.from(podcastItems).map(item => {
                const titleEl = item.querySelector('.podcast-title');
                const descriptionEl = item.querySelector('.podcast-description');
                const linkEl = item.querySelector('a');
                
                return {
                    title: titleEl ? titleEl.innerText.trim() : 'No Title',
                    description: descriptionEl ? descriptionEl.innerText.trim() : 'No Description',
                    link: linkEl ? linkEl.href : ''
                };
            });
        }''')
        
        return podcasts
    
    except Exception as e:
        print(f"An error occurred while scraping: {e}")
        return []
    
    finally:
        # Always close the browser, even if an error occurs
        await browser.close()

async def main():
    # Run the scraping function
    podcasts = await scrape_matchmaker_podcasts()
    
    # Print out the podcasts we found
    print("Podcasts found:")
    for i, podcast in enumerate(podcasts, 1):
        print(f"\n{i}. Podcast Details:")
        print(f"   Title: {podcast['title']}")
        print(f"   Description: {podcast['description']}")
        print(f"   Link: {podcast['link']}")
    
    # Optionally, save to a JSON file
    with open('matchmaker_podcasts.json', 'w', encoding='utf-8') as f:
        json.dump(podcasts, f, indent=2, ensure_ascii=False)
    
    print(f"\nTotal podcasts found: {len(podcasts)}")

# Run the async main function
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
