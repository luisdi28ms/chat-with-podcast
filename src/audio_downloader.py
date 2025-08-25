import requests
import xml.etree.ElementTree as ET

def download_latest_mp3_from_feed(feed_url):
    # Fetch the RSS feed
    response = requests.get(feed_url)
    response.raise_for_status()

    # Parse the XML content of the feed
    root = ET.fromstring(response.content)

    # Find all items in the feed (usually under channel/item)
    channel = root.find('channel')
    items = channel.findall('item')

    if not items:
        print("No items found in the feed.")
        return

    # Get the latest item (usually the first one)
    latest_item = items[0]

    # Find the enclosure tag with the mp3 url
    enclosure = latest_item.find('enclosure')
    if enclosure is None:
        print("No enclosure found in the latest feed item.")
        return

    mp3_url = enclosure.get('url')
    if not mp3_url:
        print("No URL found in the enclosure tag.")
        return

    # Download the mp3 content
    print(f"Downloading mp3 from: {mp3_url}")
    mp3_response = requests.get(mp3_url, stream=True)
    mp3_response.raise_for_status()

    # Extract the file name from the URL or use a default name
    file_name = mp3_url.split('/')[-1].split('?')[0] or "latest_podcast.mp3"

    # Save the mp3 to a file
    with open(file_name, 'wb') as f:
        for chunk in mp3_response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Downloaded latest mp3 as {file_name}")

# Example usage
feed_url = "https://feeds.megaphone.fm/STU4418364045"
download_latest_mp3_from_feed(feed_url)

