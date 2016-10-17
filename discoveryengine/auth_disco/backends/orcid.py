from social.backends.oauth import BaseOAuth2

class ORCIDOAuth2(BaseOAuth2):
    """ORCID OAuth2 authentication backend"""
    AUTHORIZATION_URL = 'https://sandbox.orcid.org/oauth/authorize'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        print response
        return {
            'username': response.get('orcid'),
            'first_name': response.get('name').split(' ')[0],
            'last_name': response.get('name').split(' ')[-1],
            'orcid': response.get('orcid'),
        }

class ORCIDPublicOAuth2(ORCIDOAuth2):
    """ORCID OAuth2 authentication backend for Public API"""
    name = 'orcid-public'
    ACCESS_TOKEN_URL = 'https://sandbox.orcid.org/oauth/token'
    API_URL = 'https://pub.sandbox.orcid.org/v1.2/'


class ORCIDMemberOAuth2(ORCIDOAuth2):
    """ORCID OAuth2 authentication backend for Member API"""
    name = 'orcid-member'
    ACCESS_TOKEN_URL = 'https://sandbox.orcid.org/oauth/token'
    API_URL = 'https://api.sandbox.orcid.org/v1.2/'