import requests
urls=["https://www.google.com", "https://www.youtube.com", "https://hafkaljfdkahfdiiiiowhreih.com", "https://x.com"]
for ur in urls:
    try:
        response=requests.get(ur,timeout=5)
        print(f"{ur}  :  {response.status_code}")
    except Exception:
         print(f"{ur} down")
