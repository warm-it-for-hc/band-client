import os

import fire
from dotenv import load_dotenv

from api import BandAPI

load_dotenv()


class CLI:

    @classmethod
    def band(cls):
        return BandAPI(
            client_id=os.getenv("BAND_CLIENT_ID"),
            client_secret=os.getenv("BAND_CLIENT_SECRET"),
            access_token=os.getenv("BAND_ACCESS_TOKEN"),
            band_key=os.getenv("BAND_KEY"),
        )


if __name__ == "__main__":
    fire.Fire(CLI)
