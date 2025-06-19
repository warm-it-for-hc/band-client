import time

import requests

from misc import RESULT_CODES


def handler(res) -> tuple[dict, dict]:
    data = res.json()
    code_info = RESULT_CODES.get(
        data["result_code"], {"message": "", "description": "", "resolution": ""}
    )
    if data["result_code"] == 1:
        return data
    raise Exception(code_info)


def generator(f, **kwargs):
    while True:
        try:
            data = f(**kwargs)
            kwargs = data["result_data"]["paging"]["next_params"]
            yield data

            if kwargs is None:
                break

        except Exception as e:
            raise e

        time.sleep(2)


class BandAPI:
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        access_token: str = None,
        band_key: str = None,
    ):

        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.band_key = band_key

    def get_bands(self, access_token: str = None, **kwargs):
        url = "https://openapi.band.us/v2.1/bands"
        params = {"access_token": access_token or self.access_token, **kwargs}
        return handler(requests.get(url, params=params))

    def get_posts(
        self,
        access_token: str = None,
        band_key: str = None,
        locale: str = "ko_KR",
        **kwargs,
    ):
        url = "https://openapi.band.us/v2/band/posts"
        params = {
            "access_token": access_token or self.access_token,
            "band_key": band_key or self.band_key,
            "locale": locale,
            **kwargs,
        }
        return handler(requests.get(url, params=params))

    def get_specific_post(
        self, post_key: str, access_token: str = None, band_key: str = None, **kwargs
    ):
        url = "https://openapi.band.us/v2.1/band/post"
        params = {
            "access_token": access_token or self.access_token,
            "band_key": band_key or self.band_key,
            "post_key": post_key,
            **kwargs,
        }
        return handler(requests.get(url, params=params))

    def get_comments(
        self,
        post_key: str,
        access_token: str = None,
        band_key: str = None,
        sort: str = None,
        **kwargs,
    ):
        url = "https://openapi.band.us/v2/band/post/comments"
        params = {
            "access_token": access_token or self.access_token,
            "band_key": band_key or self.band_key,
            "post_key": post_key,
            "sort": sort,
            **kwargs,
        }
        return handler(requests.get(url, params=params))

    def snapshot(
        self,
        before: str = None,
        after: str = None,
        limit: int = float("inf"),
        access_token: str = None,
        band_key: str = None,
        specific: bool = False,
    ):
        """
        parameters:
        - before: str, post_key to stop before (includes this post)
        - after: str, post_key to start after (does not include this post)

          new (-----] old
        after (-----] before
        """
        stop = False
        count = 0
        for posts in generator(
            self.get_posts,
            after=after,
            access_token=access_token or self.access_token,
            band_key=band_key or self.band_key,
        ):
            for post in posts["result_data"]["items"]:

                if specific:
                    post = self.get_specific_post(
                        post_key=post["post_key"],
                        access_token=access_token or self.access_token,
                        band_key=band_key or self.band_key,
                    )["result_data"]["post"]

                count += 1

                temp = []
                for comments in generator(
                    self.get_comments,
                    post_key=post["post_key"],
                    access_token=access_token or self.access_token,
                    band_key=band_key or self.band_key,
                ):
                    temp.extend(comments["result_data"]["items"])
                post["comments"] = temp
                yield post

                if (count >= limit) or (post["post_key"] == before):
                    stop = True
                    break

            if stop:
                break
