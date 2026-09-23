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
    
    def extract_info(self):
        if self.soup is None:
            print("Failed to read fetched data")
            return

            print("\n---Extracting Information---")

            all_links = self.soup.find_all("a")

            for link in all_links:
                href = link.get("href")

                if href:
                    if href.startswith("mailto:"):
                        email = href.replace("mailto:", "")
                        print(f"Email found: {email}")

                    elif href.startswith("tel:"):
                        tel = href.replace("tel:", "")
                        print(f"Phone number scraped: {tel}")

    def extract_sites_metadata(self):
        if self.soup is None:
            print("Failed to fetch data")
            return

            sites_name = self.soup.find("h1")

            sites_address = self.soup.find("p", class_= "business-address")

            if sites_name:
                print(f"Company's name: {sites_name.text.strip()}")

            if sites_address:
                print(f"Company's address: {sites_address.text.strip()}")



user_url = input("Enter a url: ")

myscraper = WebScraper(user_url)

myscraper.fetch_site()
myscraper.extract_images()
myscraper.extract_info()
myscraper.extract_sites_metadata()
