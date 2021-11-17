import requests

def Ping():
    
    sunsigns = ["aries", "taurus", "gemini", "cancer", "leo", "virgo",
           "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
    timeframe = ["today", "week", "month", "year"]
    
    for time in timeframe:
        for sign in sunsigns:
            horo = f"http://horoscope-api.herokuapp.com/horoscope/{time}/{sign}"
            response = requests.get(horo)
            
            try:
                return response.json()["horoscope"]
                    
            except ValueError:
                return "Link Not Found"
                
def test_link_check():
    assert Ping() != "Link Not Found"

if __name__ == "__main__":
    print(test_link_check())