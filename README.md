Spotify e-Ink Album Art Display

DEPENDENCIES
pip install spotipy requests Pillow
Note: Ensure you have the Waveshare e-Paper library installed and the waveshare_epd folder is in your project directory.

To get your CLIENT_ID and CLIENT_SECRET, follow these steps:

-Go to the Dashboard: Visit the Spotify Developer Dashboard and log in.
-Create an App: Click "Create app". Give it a name (e.g., "e-Ink Display") and a description.
-Redirect URI: Click "Settings" and add http://localhost:8888/callback to the Redirect URIs field. Save the changes.
-Get Credentials: On your app dashboard, click "Settings" again to find your Client ID and Client Secret.

QUICK START:
Open the script and replace the placeholders with your credentials:
-client_id: Your Spotify Client ID.
-client_secret: Your Spotify Client Secret.
-redirect_uri: http://localhost:8888/callback

First Run: A browser window will open asking you to log in and authorize the app. Once done, it will redirect to a URL. Copy that URL and paste it back into the terminal if prompted.
