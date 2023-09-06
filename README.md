# Wallpaper Downloader

Welcome to Wallpaper Downloader! This is a Django web application that allows you to download wallpapers from Unsplash.

## Getting Started

Follow these steps to set up the project and run it locally:

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Obtaining an Unsplash API Key

1. Go to the [Unsplash Developer](https://unsplash.com/developers) website.
2. Create an account or log in if you already have one.
3. Once logged in, go to the [Applications](https://unsplash.com/oauth/applications) page.
4. Click on the "New Application" button to create a new application.
5. Fill out the required fields, and when asked for a **Redirect URI**, you can use `http://localhost:8000/complete/unsplash/` for local development.
6. After creating the application, you will see your **Access Key**. Copy it; you'll need it later.

### Setting Up Your Environment

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/wallpaper-downloader.git
```

2. Navigate to the project directory:

```bash
cd wallpaper-downloader
```

3. Create a `.env` file in the project root directory. You can do this using the following command:

```bash
touch .env
```

4. Open the `.env` file with a text editor and add your Unsplash API key to it:

```env
UNSPLASH_ACCESS_KEY=your-access-key-goes-here
```

Replace `your-access-key-goes-here` with the Access Key you obtained from Unsplash.

### Running the Application

1. Build and start the Docker containers using Docker Compose:

```bash
sudo docker-compose up --build
```

2. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the Wallpaper Downloader application.

3. Use the application to select the download type (desktop or mobile) and specify the folder path where you want to save the downloaded wallpapers.

4. Click the "Download" button to initiate the wallpaper download.

### Stopping the Application

To stop the application, press `Ctrl + C` in the terminal where Docker Compose is running. Then, run the following command to clean up the containers:

```bash
sudo docker-compose down
```

## Feedback and Contributions

If you have feedback or would like to contribute to this project, please feel free to create an issue or submit a pull request.

Happy wallpaper downloading!