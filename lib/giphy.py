import giphy_client as giphy
import random


class GiphyAPIWrapper:
    """
    Easy to use wrapper around the giphypop library and by extension
    the giphy API.
    """
    def __init__(self):
        self.instance = giphy.DefaultApi()
        self.api_key = "hhRtAzeoA7ZDemvZbk2P86JMN1dIamuG"

    def search(self, term: str, limit: int = 10):
        response = self.instance.gifs_search_get(self.api_key, term, limit=limit, lang="en", fmt="json")
        return response.data[random.randint(0, limit)].images.downsized.url


