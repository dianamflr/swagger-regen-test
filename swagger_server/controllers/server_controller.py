import connexion
import six

from swagger_server import util


def healthcheck():  # noqa: E501
    """Healthcheck for Appliation Load Balancer

    Healtch check response for server # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
