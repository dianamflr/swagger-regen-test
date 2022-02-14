import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def delete_job(job_id):  # noqa: E501
    """Delete an RSA job

    Deletes an RSA job, and will return success if job has been successfully deleted. # noqa: E501

    :param job_id: Id of the RSA job
    :type job_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_job(job_id):  # noqa: E501
    """Get RSA Job Status/Result

    Gets the job status/result  The resultUrl, when appropriate, will contain a report of the RSA job. # noqa: E501

    :param job_id: Id of the RSA job
    :type job_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def post_job(body=None):  # noqa: E501
    """Queues a New RSA Job

    Queues a new RSA job for the given parameters and returns the id of the newly  created job.  Prior to starting the job (e.g. just before executing), the job status  should become &#x60;inprogress&#x60; and following the successful completion and  saving of results, the job status will become &#x60;completed&#x60;. It is  expected that the RSA job would be in a &#x60;pending&#x60; state for only  moments.  The resultUrl, when appropriate, will contain a report of the RSA job. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
        test = 'TESTING REGEN CODE'

    return test
