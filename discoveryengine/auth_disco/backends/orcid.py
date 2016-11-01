from social.backends.oauth import BaseOAuth2
import requests
from xml.etree import ElementTree

class ORCIDOAuth2(BaseOAuth2):
    """ORCID OAuth2 authentication backend"""
    AUTHORIZATION_URL = 'https://orcid.org/oauth/authorize'
    SCOPE_SEPARATOR = ''
    ACCESS_TOKEN_METHOD = 'POST'
    ID_KEY = 'orcid'

    def indent(self, elem, level=0):
        i = "\n" + level*"  "
        j = "\n" + (level-1)*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                self.indent(subelem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = j
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = j
        return elem        

    def get_user_details(self, response):
        """Return user details from ORCID account"""
        print "GET_USER_DETAILS"
        print response
        return {
            'username': response.get('orcid'),
            'first_name': response.get('first_name'),
            'last_name': response.get('last_name'),
            'orcid': response.get('orcid'),
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        print "USER_DATA"
        orcid = kwargs.get('response').get('orcid')
        url = self.API_URL + orcid
        headers = {'Authorization': 'Bearer ' + access_token}
        try:
            r = requests.get(url, headers=headers)
            data = self._user_data_from_XML(r.content)
            data["orcid"] = orcid
            return data
        except ValueError:
            return None

    def _user_data_from_XML(self, xml_string):
        namespaces = {
            'ns0': 'http://www.orcid.org/ns/orcid',
        }
        tree = ElementTree.fromstring(xml_string)
        profile = tree.find('ns0:orcid-profile', namespaces)
        bio = profile.find('ns0:orcid-bio', namespaces)

        # Personal details
        details = bio.find('ns0:personal-details', namespaces)
        first_name = details.find('ns0:given-names', namespaces).text
        last_name = details.find('ns0:family-name', namespaces).text

        # Contact information
        contact = bio.find('ns0:contact-details', namespaces)
        email = None
        if contact:
            email = contact.find('ns0:email', namespaces).text

        return {
            'first_name': first_name, 
            'last_name': last_name,
            'email': email,
        }

class ORCIDPublicOAuth2(ORCIDOAuth2):
    """ORCID OAuth2 authentication backend for Public API"""
    name = 'orcid-public'
    ACCESS_TOKEN_URL = 'https://orcid.org/oauth/token'
    API_URL = 'https://pub.orcid.org/v1.2/'


class ORCIDMemberOAuth2(ORCIDOAuth2):
    """ORCID OAuth2 authentication backend for Member API"""
    name = 'orcid-member'
    ACCESS_TOKEN_URL = 'https://orcid.org/oauth/token'
    API_URL = 'https://api.orcid.org/v1.2/'


################################################################
################ ORCID SANDBOX OAUTH2 BACKENDS #################
################################################################
class ORCIDSandboxOAuth2(ORCIDOAuth2):
    """ORCID OAuth2 authentication backend"""
    AUTHORIZATION_URL = 'https://sandbox.orcid.org/oauth/authorize'

class ORCIDSandboxPublicOAuth2(ORCIDSandboxOAuth2):
    """ORCID OAuth2 authentication backend for Public API"""
    name = 'orcid-sandbox-public'
    ACCESS_TOKEN_URL = 'https://sandbox.orcid.org/oauth/token'
    API_URL = 'https://pub.sandbox.orcid.org/v1.2/'


class ORCIDSandboxMemberOAuth2(ORCIDSandboxOAuth2):
    """ORCID OAuth2 authentication backend for Member API"""
    name = 'orcid-sandbox-member'
    ACCESS_TOKEN_URL = 'https://sandbox.orcid.org/oauth/token'
    API_URL = 'https://api.sandbox.orcid.org/v1.2/'