from SeleniumEntry import Secretary
from ZillowScrape import Realtor

ZILLOW_LINK = 'https://www.zillow.com/homes/for_sale/3-_beds/2.0-_baths/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Goldsboro%2C%20NC%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.84828268214704%2C%22east%22%3A-76.63478170558454%2C%22south%22%3A34.244237693569104%2C%22north%22%3A35.91860169207511%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A100000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A337%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%2C%22customRegionId%22%3A%22709e3606a1X1-CR705vcxyl4u_tt63d%22%7D'
GOOGLE_FORM = 'https://forms.gle/bvRX7PnN4Rq6N7uu7'
realtor = Realtor()
realtor.get_listings(ZILLOW_LINK)
assistant = Secretary()
assistant.enter_data(url=GOOGLE_FORM, data=realtor.formatted_listings, len=realtor.listing_number)
