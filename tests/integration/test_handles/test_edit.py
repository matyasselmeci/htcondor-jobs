# Copyright 2019 HTCondor Team, Computer Sciences Department,
# University of Wisconsin-Madison, WI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

import htcondor_jobs as jobs


def get_job_attr(handle, attr):
    ad = next(handle.query(projection=[attr]))
    return ad[attr]


def test_change_request_memory(long_sleep):
    handle = jobs.submit(long_sleep, count=1)

    handle.edit("RequestMemory", 12345)

    assert get_job_attr(handle, "RequestMemory") == 12345
