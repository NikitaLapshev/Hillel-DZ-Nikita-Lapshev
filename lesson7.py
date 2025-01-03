from abc import ABC, abstractmethod
from time import time

class SocialChannel(ABC):
    def __init__(self, followers: int):
        self.followers = followers

    @abstractmethod
    def post_message(self, message: str) -> None:
        return self.post_message()

class YouTubeChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"We publish on YouTube: {message}")


class FacebookChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"We publish on Facebook: {message}")

class TwitterChannel(SocialChannel):
    def post_message(self, message: str) -> None:
        print(f"We publish on twitter: {message}")

class Post:
        def __init__(self, message: str, timestamp: int):
            self.message = message
            self.timestamp = timestamp

def post_a_message(channel: SocialChannel, message: str) -> None:
            return channel.post_message(message)

def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
            for post in posts:
                if post.timestamp <= time():
                    for channel in channels:
                        post_a_message(channel, post.message)


youtube = YouTubeChannel(followers=1000)
facebook = FacebookChannel(followers=1500)
twitter = TwitterChannel(followers=2000)


post1 = Post("Hello subscriber!", timestamp=int(time()) - 15)
post2 = Post("New video is already on the channel!", timestamp=int(time()) + 20)


process_schedule([post1, post2], [youtube, facebook, twitter])

