import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class WebScraper:
    def __init__(self, target_url):
        self.url = target_url
        self.soup = None

    def fetch_site(self):
        try:
            print(f"Connecting to {self.url}...")
            response = requests.get(self.url, timeout=20)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, "html.parser")
            print("Successfully connected and parsed the HTML")
        except Exception as e:
            print(f"Failed to fetch the page: {e}")

    def extract_images(self):
        if self.soup is None:
            print("Failed to read fetched data")
            return []

        print("\n---Extracting Images---")
        images = self.soup.find_all("img")

        found = []
        for img in images:
            image_url = img.get("src")
            if image_url:
                found.append(image_url)

        return found

    def extract_info(self):
        if self.soup is None:
            print("Failed to read fetched data")
            return {"emails": [], "phones": []}

        print("\n---Extracting Information---")
        all_links = self.soup.find_all("a")

        emails = []
        phones = []
        for link in all_links:
            href = link.get("href")
            if href:
                if href.startswith("mailto:"):
                    emails.append(href.replace("mailto:", ""))
                elif href.startswith("tel:"):
                    phones.append(href.replace("tel:", ""))

        return {"emails": emails, "phones": phones}

    def extract_sites_metadata(self):
        if self.soup is None:
            print("Failed to fetch data")
            return {}

        sites_name = self.soup.find("h1")
        sites_address = self.soup.find("p", class_="business-address")

        metadata = {}
        if sites_name:
            metadata["name"] = sites_name.text.strip()
        if sites_address:
            metadata["address"] = sites_address.text.strip()

        return metadata

    def display_results(self, images, info, metadata):
        print("\n---Results---")

        print(f"\nImages found: {len(images)}")
        for img_url in images:
            print(f"  {img_url}")

        print(f"\nEmails found: {len(info['emails'])}")
        for email in info["emails"]:
            print(f"  {email}")

        print(f"\nPhones found: {len(info['phones'])}")
        for phone in info["phones"]:
            print(f"  {phone}")

        if metadata.get("name"):
            print(f"\nCompany's name: {metadata['name']}")
        if metadata.get("address"):
            print(f"Company's address: {metadata['address']}")


if __name__ == "__main__":
    while True:
        raw_input_ = input("Enter a url: ")
        user_url = raw_input_.strip()

        if len(user_url) == 0:
            print("Empty fields")
            continue

        try:
            parsed_url = urlparse(user_url)

            if not parsed_url.scheme or not parsed_url.netloc:
                raise ValueError("Missing protocol or domain network location.")

            if parsed_url.scheme not in ["http", "https"]:
                raise ValueError("Unsupported protocol: only http and https are allowed.")

            break

        except ValueError as err:
            print(f"Input Error: '{user_url}' is not a valid web URL.")
            print(f"Details: '{err}'.")
            print(f"Example of proper format: https://toscrape.com\n")

    myscraper = WebScraper(user_url)

    myscraper.fetch_site()
    images = myscraper.extract_images()
    info = myscraper.extract_info()
    metadata = myscraper.extract_sites_metadata()
    myscraper.display_results(images, info, metadata)
