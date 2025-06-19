# BAND API Client

A Python CLI tool and API wrapper for interacting with the [BAND](https://band.us/) social platform's API. This project allows you to fetch bands, posts, comments, and more, using your BAND API credentials.

## Features
- Fetch your BAND groups and posts
- Retrieve comments for posts
- Snapshot posts and comments with pagination
- CLI interface for easy access
- Error handling with descriptive messages

## Requirements
- Python 3.8+
- BAND API credentials (see below)

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd band-client
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root (or copy `example.env`):

```
BAND_ACCESS_TOKEN=your_band_access_token
BAND_KEY=your_band_key
BAND_CLIENT_ID=your_client_id
BAND_CLIENT_SECRET=your_client_secret
```

- You can obtain these credentials from the [BAND Developer Portal](https://developers.band.us/).

## Usage

### CLI

The CLI is powered by [fire](https://github.com/google/python-fire). Example usage:

```bash
python main.py band get_bands
python main.py band get_posts --band_key=YOUR_BAND_KEY
python main.py band get_comments --post_key=POST_KEY
```

You can pass additional parameters as keyword arguments.

### As a Python Module

```python
from api import BandAPI
import os

api = BandAPI(
    client_id=os.getenv("BAND_CLIENT_ID"),
    client_secret=os.getenv("BAND_CLIENT_SECRET"),
    access_token=os.getenv("BAND_ACCESS_TOKEN"),
    band_key=os.getenv("BAND_KEY"),
)

bands = api.get_bands()
posts = api.get_posts()
```

## Error Handling

Error codes and messages are mapped in `misc.py` for easier debugging.

## License

This project is licensed under the terms of the LICENSE file.

## Acknowledgements
- [BAND Open API Documentation](https://developers.band.us/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [fire](https://github.com/google/python-fire)
