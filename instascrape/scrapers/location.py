from __future__ import annotations

from typing import List

from instascrape.core._mappings import _LocationMapping
from instascrape.core._static_scraper import _StaticHtmlScraper
from instascrape.scrapers.post import Post

class Location(_StaticHtmlScraper):
    """Scraper for an Instagram profile page"""

    _Mapping = _LocationMapping

    # def get_recent_posts(self, amt: int = 12) -> List[Post]:
    #     """
    #     Return a list of the profiles recent posts

    #     Parameters
    #     ----------
    #     amt : int
    #         Amount of recent posts to return

    #     Returns
    #     -------
    #     posts : List[Post]
    #         List containing the recent 12 posts and their available data
    #     """
    #     if amt > 12:
    #         raise IndexError(
    #             f"{amt} is too large, 12 is max available posts. Getting more posts will require an out-of-the-box extension.")
    #     posts = []
    #     try:
    #         post_arr = self.json_dict["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"][
    #             "edges"
    #         ]
    #     except TypeError:
    #         raise ValueError(
    #             "Can't return posts without first scraping the Profile. Call the scrape method on your object first.")

    #     for post in post_arr[:amt]:
    #         json_dict = post["node"]
    #         mapping = _PostMapping.post_from_profile_mapping()
    #         post = Post(json_dict)
    #         post.scrape(mapping=mapping)
    #         posts.append(post)
    #     return posts

    def _url_from_suburl(self, suburl):
        raise ValueError("suburl not currently supported for Location scrape, please pass a full URL to the location you want to scrape")
