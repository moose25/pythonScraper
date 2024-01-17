import requests
from bs4 import BeautifulSoup

def get_bbc_headlines(url):
    headlines = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Updated to target <h2> tags with 'data-testid' attribute
        articles = soup.find_all('h2', attrs={'data-testid': 'card-headline'})

        for article in articles:
            title = article.get_text(strip=True)
            link = article.find_parent('a', href=True)
            if link and not link['href'].startswith('http'):
                link = f'https://www.bbc.com{link["href"]}'
            elif link:
                link = link['href']
            else:
                link = 'No link available'
            headlines.append({'title': title, 'link': link})
    except requests.RequestException as e:
        print(f"Error during requests to {url} : {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return headlines

if __name__ == "__main__":
    url = 'https://www.bbc.com/'
    headlines = get_bbc_headlines(url)
    for headline in headlines:
        print(headline)
