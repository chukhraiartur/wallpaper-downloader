FROM python:3.8.10
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./wallpaper_downloader ./wallpaper_downloader

CMD [ "python3", "./wallpaper_downloader/manage.py", "runserver", "0.0.0.0:8000" ]