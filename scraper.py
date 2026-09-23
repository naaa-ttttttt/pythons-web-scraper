import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, target_url):
        self.url = target_url
        self.soup = None
    
    def fetch_site(self):
        try: 
            print(f"Connecting to {self.url}...")

            response = request.get(self.url, timeout= 20)

            response.raise_for_status()

            self.soup = BeautifulSoup(response.text, "html.parser")

            print("Successfully connected and parsed the HTML")
        
        except:
            print(f"failed to fetch the page: {e}")

    def extract_images(self):
       if self.soup is None:
           print("Failed to read fetched data")
           return

           print("\n---Extracting Images---")

           images = self.soup.find_all("img")

           for img in images:
               image_url = img.get("src")

               if image_url:
                   print(f"Image Found: {image_url}")





