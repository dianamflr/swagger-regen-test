# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRSAController(BaseTestCase):
    """RSAController integration test stubs"""

    def test_delete_job(self):
        """Test case for delete_job

        Delete an RSA job
        """
        response = self.client.open(
            '/rsa/rsa/{job_id}'.format(job_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job(self):
        """Test case for get_job

        Get RSA Job Status/Result
        """
        response = self.client.open(
            '/rsa/rsa/job/{job_id}'.format(job_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_job(self):
        """Test case for post_job

        Queues a New RSA Job
        """
        body = Body()
        response = self.client.open(
            '/rsa/rsa/job',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
