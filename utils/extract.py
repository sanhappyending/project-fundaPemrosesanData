import datetime
import time
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def fetching_content(url):
    """
        Mengambil konten HTML dari URL yang diberikan
    """
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None


def extract_store_products(item):
    """
        Mengambil data title, price, rating, colors, size, gender
    """
    try:
        product_title = item.find('h3').text.strip()

        prices = item.find('div', class_='price-container')
        if not prices:
            return None
        price = prices.find('span', class_='price').text.strip()

        product_element = item.find('div', class_='product-details')
        if not product_element:
            return None
        
        rating_find = product_element.find(
            'p',
            string=lambda string: string and 'Rating:' in string
        )

        color_find = product_element.find(
            'p',
            string=lambda string: string and 'Colors' in string
        )

        size_find = product_element.find(
            'p',
            string=lambda string: string and 'Size:' in string
        )

        gender_find = product_element.find(
            'p',
            string=lambda string: string and 'Gender:' in string
        )

        product_data = {
            "Title": product_title,
            "Price": price,
            "Rating": rating_find.text.strip() if rating_find else None,
            "Colors": color_find.text.strip() if color_find else None,
            "Size": size_find.text.strip() if size_find else None,
            "Gender": gender_find.text.strip() if gender_find else None,
            "Timestamp": datetime.datetime.now()
        }

        return product_data

    except Exception as e:
        print(f"Error extracting product: {e}")
        return None
 
def scrape_store_products(base_url, delay=2, max_pages=50):
    """
        Scraping seluruh data fashion
    """
    result = []
    total_pages = 50

    for page in range(1, total_pages + 1):

        if page == 1:
            url = base_url
        else:
            url = f"{base_url}page{page}"

        print(f"Scraping halaman: {url}")

        try:
            content = fetching_content(url)

            if not content:
                print(f"Gagal mengambil halaman {page}")
                break

            soup = BeautifulSoup(content, "html.parser")

            elements = soup.find_all(
                "div",
                class_="collection-card"
            )

            if not elements:
                print(f"Tidak ada produk di halaman {page}")
                break

            for item in elements:

                product = extract_store_products(item)

                if product:
                    result.append(product)

            time.sleep(delay)

        except Exception as e:
            print(f"Error saat scraping halaman {page}: {e}")
            break

    return result