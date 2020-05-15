# coding: utf-8

"""
    MetaDefender Core

    ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works.   # noqa: E501

    The version of the OpenAPI document: v4.18.0
    Contact: feedback@opswat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.inline_response20013 import InlineResponse20013  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse20013(unittest.TestCase):
    """InlineResponse20013 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20013
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response20013.InlineResponse20013()  # noqa: E501
        if include_optional :
            return InlineResponse20013(
                external_nodes_allowed = False, 
                max_node_count = 1, 
                statuses = [
                    openapi_client.models._stat_nodes_statuses._stat_nodes_statuses(
                        address = '0', 
                        cpu_cores = 8, 
                        engines = [
                            openapi_client.models._stat_nodes_engines._stat_nodes_engines(
                                active = True, 
                                db_ver = '25050', 
                                def_time = '2020-04-17T02:37:05.000Z', 
                                eng_name = 'ClamAV', 
                                eng_ver = '3.0-43', 
                                engine_type = 'av', 
                                id = 'clamav_1_linux', )
                            ], 
                        free_disk_space = 173993443328, 
                        id = ':69', 
                        issues = [
                            openapi_client.models._stat_nodes_issues._stat_nodes_issues(
                                description = '1 engines are not deployed to this node', 
                                severity = 'warning', )
                            ], 
                        load = 14, 
                        os = 'Linux Mint 18.3 Sylvia', 
                        scan_queue = 24, 
                        total_memory = 40100, 
                        version = '4.18.0', )
                    ]
            )
        else :
            return InlineResponse20013(
        )

    def testInlineResponse20013(self):
        """Test InlineResponse20013"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
