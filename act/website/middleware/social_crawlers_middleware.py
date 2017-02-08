# act/website/middleware/social_crawlers_middleware.py
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import format_html

from act.services.crawler_detectors import (
    FacebookCrawlerDetector, VkontakteCrawlerDetector, TwitterCrawlerDetector,
)

from ..models import Scraping


class SocialCrawlersMiddleware(object):
    crawler_detectors = (
        FacebookCrawlerDetector,
        VkontakteCrawlerDetector,
        TwitterCrawlerDetector,
    )

    def process_response(self, request, response):
        if self.is_crawler(request):
            scraped = get_object_or_404(Scraping, path=request.path)

            response.content = render_to_string(
                'website/middleware/social_crawlers.html',
                {'head': format_html(scraped.head)})

        return response

    def is_crawler(self, request):
        for crawler_detector in self.crawler_detectors:
            if crawler_detector.is_user_agent_matching(request):
                return True

        return False
