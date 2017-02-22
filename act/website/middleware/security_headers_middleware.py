# act_project/act/website/middleware/security_headers_middleware.py
from django.conf import settings


class SecurityHeadersMiddleware(object):
    '''
    Class adds an appropriate headers to follow Mozilla Web Security guidelines
    '''
    def process_response(self, request, response):
        response = self.csp_header(response)

        return response

    def csp_header(self, response):
        '''
        Modifies response to add Content Security Policy (CSP) header
        https://wiki.mozilla.org/Security/Guidelines/Web_Security#Content_Security_Policy
        '''
        if getattr(settings, 'CONTENT_SECURITY_POLICY', False):
            csp_parts = {
                'default-src': "'self'",
                'img-src': "'self' https:",
                'font-src': "'self' https://fonts.gstatic.com",
                'style-src': (
                    "'self' 'unsafe-inline' https://fonts.googleapis.com"
                ),
                'script-src': (
                    "'self'"
                    " 'unsafe-inline'"
                    " 'unsafe-eval'"
                    " https://ajax.googleapis.com"
                    " https://maps.googleapis.com"
                    " https://www.google-analytics.com"
                ),
                'child-src': (
                    "https://www.youtube.com"
                ),
            }

            response['Content-Security-Policy'] = ''.join(
                '{0} {1};'.format(key, value)
                for key, value in csp_parts.items()
            )

        return response
