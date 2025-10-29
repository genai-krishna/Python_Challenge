import requests
import time
import urllib.robotparser
import os

# ---------------------------------------------------------
# Function: Check robots.txt permission
# ---------------------------------------------------------
def is_scraping_allowed(url, user_agent='*'):
    """
    Checks if scraping is allowed for the given URL using robots.txt.
    """
    base_url = "/".join(url.split("/")[:3]) + "/robots.txt"
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(base_url)

    try:
        rp.read()
        return rp.can_fetch(user_agent, url)
    except Exception as e:
        print(f"[Warning] Could not read robots.txt: {e}")
        return False


# ---------------------------------------------------------
# Function: Scrape website and save content
# ---------------------------------------------------------
def scrape_website(url):
    """
    Fetches HTML content safely and saves it to a fixed folder.
    """
    if not is_scraping_allowed(url):
        print("🚫 Scraping not allowed by robots.txt for this URL.")
        return

    print("⏳ Waiting 3 seconds before making the request (Rate Limiting)...")
    time.sleep(3)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        print("\n✅ Scraping Successful!")
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Content Size: {len(response.text)} bytes")

        # Save path
        save_path = r"F:\GenAI_Training\Python_Training\scraped_content.txt"

        # Ensure folder exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Write content to file
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"💾 HTML content saved successfully at:\n{save_path}")

        # Preview
        print("\n------ Preview of HTML Content ------")
        print(response.text[:300])
        print("\n------------------------------------")

    except requests.exceptions.Timeout:
        print("❌ Error: The request timed out.")
    except requests.exceptions.HTTPError as errh:
        print(f"❌ HTTP Error: {errh}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Unable to reach the server.")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e}")


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
def main():
    print("===== Website Web Scraper =====")
    url = input("Enter website URL (e.g., https://example.com): ").strip()
    if not url:
        print("⚠️ No URL entered. Exiting program.")
        return
    scrape_website(url)
    print("\nProgram finished safely ✅")


if __name__ == "__main__":
    main()
