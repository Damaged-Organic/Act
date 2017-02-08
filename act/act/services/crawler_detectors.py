# act/act/services/crawler_detector.py
class CrawlerDetector:
    HTTP_USER_AGENT = 'HTTP_USER_AGENT'

    _user_agents = []

    @classmethod
    def is_user_agent_matching(cls, request):
        request_user_agent = request.META.get(cls.HTTP_USER_AGENT, None)

        if request_user_agent:
            request_user_agent = request_user_agent.lower()

        matching = next((
            user_agent for user_agent in cls._user_agents
            if user_agent in request_user_agent),
            None)

        return matching


class FacebookCrawlerDetector(CrawlerDetector):
    _user_agents = ['facebookexternalhit', 'facebot']


class VkontakteCrawlerDetector(CrawlerDetector):
    _user_agents = ['vkshare']


class TwitterCrawlerDetector(CrawlerDetector):
    _user_agents = ['twitterbot']
