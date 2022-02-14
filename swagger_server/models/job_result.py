# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.job_result_time import JobResultTime  # noqa: F401,E501
from swagger_server import util


class JobResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, status: str=None, progress_message: str=None, failure_message: str=None, time: JobResultTime=None, result_url: str=None):  # noqa: E501
        """JobResult - a model defined in Swagger

        :param id: The id of this JobResult.  # noqa: E501
        :type id: int
        :param status: The status of this JobResult.  # noqa: E501
        :type status: str
        :param progress_message: The progress_message of this JobResult.  # noqa: E501
        :type progress_message: str
        :param failure_message: The failure_message of this JobResult.  # noqa: E501
        :type failure_message: str
        :param time: The time of this JobResult.  # noqa: E501
        :type time: JobResultTime
        :param result_url: The result_url of this JobResult.  # noqa: E501
        :type result_url: str
        """
        self.swagger_types = {
            'id': int,
            'status': str,
            'progress_message': str,
            'failure_message': str,
            'time': JobResultTime,
            'result_url': str
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'progress_message': 'progressMessage',
            'failure_message': 'failureMessage',
            'time': 'time',
            'result_url': 'resultUrl'
        }
        self._id = id
        self._status = status
        self._progress_message = progress_message
        self._failure_message = failure_message
        self._time = time
        self._result_url = result_url

    @classmethod
    def from_dict(cls, dikt) -> 'JobResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The jobResult of this JobResult.  # noqa: E501
        :rtype: JobResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this JobResult.

        Id of the job  # noqa: E501

        :return: The id of this JobResult.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this JobResult.

        Id of the job  # noqa: E501

        :param id: The id of this JobResult.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self) -> str:
        """Gets the status of this JobResult.

        The current status of the job  # noqa: E501

        :return: The status of this JobResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this JobResult.

        The current status of the job  # noqa: E501

        :param status: The status of this JobResult.
        :type status: str
        """
        allowed_values = ["pending", "inprogress", "completed", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def progress_message(self) -> str:
        """Gets the progress_message of this JobResult.

        The current progress of the job  # noqa: E501

        :return: The progress_message of this JobResult.
        :rtype: str
        """
        return self._progress_message

    @progress_message.setter
    def progress_message(self, progress_message: str):
        """Sets the progress_message of this JobResult.

        The current progress of the job  # noqa: E501

        :param progress_message: The progress_message of this JobResult.
        :type progress_message: str
        """

        self._progress_message = progress_message

    @property
    def failure_message(self) -> str:
        """Gets the failure_message of this JobResult.

        If the job status is `failed`, this will contain the failure message.  # noqa: E501

        :return: The failure_message of this JobResult.
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message: str):
        """Sets the failure_message of this JobResult.

        If the job status is `failed`, this will contain the failure message.  # noqa: E501

        :param failure_message: The failure_message of this JobResult.
        :type failure_message: str
        """

        self._failure_message = failure_message

    @property
    def time(self) -> JobResultTime:
        """Gets the time of this JobResult.


        :return: The time of this JobResult.
        :rtype: JobResultTime
        """
        return self._time

    @time.setter
    def time(self, time: JobResultTime):
        """Sets the time of this JobResult.


        :param time: The time of this JobResult.
        :type time: JobResultTime
        """

        self._time = time

    @property
    def result_url(self) -> str:
        """Gets the result_url of this JobResult.

        Signed S3 URL containing the result of the job - only present if  status is `completed`. The URL will only be valid for 30 minutes  from the time of calling this method. See the parent method for  details on result contents.  # noqa: E501

        :return: The result_url of this JobResult.
        :rtype: str
        """
        return self._result_url

    @result_url.setter
    def result_url(self, result_url: str):
        """Sets the result_url of this JobResult.

        Signed S3 URL containing the result of the job - only present if  status is `completed`. The URL will only be valid for 30 minutes  from the time of calling this method. See the parent method for  details on result contents.  # noqa: E501

        :param result_url: The result_url of this JobResult.
        :type result_url: str
        """

        self._result_url = result_url