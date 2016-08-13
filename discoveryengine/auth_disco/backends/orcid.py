from social.backends.oauth import BaseOAuth2

class ORCIDOAuth2(BaseOAuth2):
	"""ORCID OAuth2 authentication backend"""
	AUTHORIZATION_URL = 'https://orcid.org/oauth/authorize'
	SCOPE_SEPARATOR = ' '


class ORCIDPublicOAuth2(ORCIDOAuth2):
	"""ORCID OAuth2 authentication backend for Public API"""
	name = 'orcid-public'
	ACCESS_TOKEN_URL = 'https://pub.orcid.org/oauth/token'
	API_URL = 'https://pub.orcid.org/v1.2/'


class ORCIDMemberOAuth2(ORCIDOAuth2):
	"""ORCID OAuth2 authentication backend for Member API"""
	name = 'orcid-member'
	ACCESS_TOKEN_URL = 'https://api.orcid.org/oauth/token'
	API_URL = 'https://api.orcid.org/v1.2/'