import requests, uuid
from celery import shared_task
from django.conf import settings
from decouple import config


@shared_task
def download_random_wallpaper(orientation_type):
    # Your Unsplash API access key (Client ID)
    ACCESS_KEY = config('ACCESS_KEY')

    # Base URL for the Unsplash API
    BASE_URL = 'https://api.unsplash.com/photos/random/'

    # Set up headers with your API key
    headers = {
        'Authorization': f'Client-ID {ACCESS_KEY}'
    }

    # Parameters for the random image request (you can adjust them)
    params = {
        'orientation': orientation_type,  # You can change this to 'portrait' for mobile wallpapers
        # 'w': 1920,                          # Width for desktop wallpaper
        # 'h': 1080                           # Height for desktop wallpaper
    }
    # Make a GET request to the Unsplash API
    response = requests.get(BASE_URL, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the image URL
        image_url = data['urls']['full']
        # Make a filename
        filename = settings.BASE_DIR / 'images' / (data.get('slug', str(uuid.uuid4())) + '.jpg')
        # Get image response
        image_response = requests.get(image_url)
        # Save image
        with open(filename, 'wb') as f:
            f.write(image_response.content)
    else:
        print("Failed to retrieve a random wallpaper. Status code:", response.status_code)