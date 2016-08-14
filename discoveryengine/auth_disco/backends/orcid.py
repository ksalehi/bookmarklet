from social.backends.oauth import BaseOAuth2

class ORCIDOAuth2(BaseOAuth2):
    """ORCID OAuth2 authentication backend"""
    AUTHORIZATION_URL = 'https://sandbox.orcid.org/oauth/authorize'
    SCOPE_SEPARATOR = ' '

    def auth_complete_params(self, state=None):
        data = super(ORCIDOAuth2, self).auth_complete_params(state)
        print data
        return data


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