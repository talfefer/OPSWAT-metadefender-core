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
from openapi_client.models.analysis_result import AnalysisResult  # noqa: E501
from openapi_client.rest import ApiException

class TestAnalysisResult(unittest.TestCase):
    """AnalysisResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnalysisResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.analysis_result.AnalysisResult()  # noqa: E501
        if include_optional :
            return AnalysisResult(
                data_id = '8101abae27be4d63859c55d9e0ed0135', 
                dlp_info = openapi_client.models.dlp_response.DLPResponse(
                    dlp_info = openapi_client.models.dlp_response_dlp_info.DLPResponse_dlp_info(
                        certainty = 'High', 
                        errors = {redact=File structure invalid.}, 
                        filename = 'OPSWAT_Proactive_DLP_CCN_proactive-dlp-processed_by_OPSWAT_MetaDefender_8101abae27be4d63859c55d9e0ed0135.pdf', 
                        hits = openapi_client.models.dlp_response_dlp_info_hits.DLPResponse_dlp_info_hits(
                            ccn = openapi_client.models.dlp_response_dlp_info_hits_ccn.DLPResponse_dlp_info_hits_ccn(
                                display_name = 'Credit Card Number', ), ), 
                        metadata_removal = openapi_client.models.dlp_response_dlp_info_metadata_removal.DLPResponse_dlp_info_metadata_removal(
                            result = 'not removed', ), 
                        redact = openapi_client.models.dlp_response_dlp_info_redact.DLPResponse_dlp_info_redact(
                            result = 'redacted', ), 
                        severity = 0, 
                        verdict = 1, 
                        watermark = openapi_client.models.dlp_response_dlp_info_watermark.DLPResponse_dlp_info_watermark(
                            result = 'added', ), ), ), 
                file_info = openapi_client.models.file_information.FileInformation(
                    display_name = 'OPSWAT_Proactive_DLP_CCN.pdf', 
                    file_size = 75906, 
                    file_type = 'application/pdf', 
                    file_type_description = 'Adobe Portable Document Format', 
                    md5 = 'c4863c8ce44fb7ae84eb48c9b78f8b5e', 
                    sha1 = 'a33c72a996a9603d479e3dff3d23bf619c975fbe', 
                    sha256 = 'b9fdc10b47950b9e503ef4dc0ef42d28e7c37ccd749d4a5dcd7d9b3218996b7f', 
                    upload_timestamp = '2020-03-12T08:37:05.412Z', ), 
                process_info = openapi_client.models.analysis_result_process_info.AnalysisResult_process_info(
                    blocked_reason = 'Sensitive Data Found', 
                    file_type_skipped_scan = False, 
                    outdated_data = [enginedefinition, configuration, sanitization], 
                    processing_time = 4804, 
                    profile = 'File process', 
                    progress_percentage = 100, 
                    queue_time = 321, 
                    result = 'Blocked', 
                    user_agent = 'webscan', 
                    username = 'LOCAL/admin', 
                    verdicts = [Sensitive Data Found], 
                    post_processing = openapi_client.models.analysis_result_process_info_post_processing.AnalysisResult_process_info_post_processing(
                        actions_failed = 'Sanitization Failed | PAscript failed', 
                        actions_ran = 'Sanitized | PAscript', 
                        converted_destination = 'OPSWAT_Proactive_DLP_CCN_sanitized.pdf', 
                        converted_to = '0', 
                        copy_move_destination = '0', 
                        sanitization_details = null, ), ), 
                scan_results = openapi_client.models.metascan_report.MetascanReport(
                    data_id = '8101abae27be4d63859c55d9e0ed0135', 
                    progress_percentage = 100, 
                    scan_all_result_a = Sensitive Data Found, 
                    scan_all_result_i = 20, 
                    start_time = '2020-03-12T08:37:05.427Z', 
                    total_avs = 1, 
                    total_time = 4804, 
                    scan_details = openapi_client.models.metascan_report_scan_details.MetascanReport_scan_details(
                        clam_av = openapi_client.models.av_engine_scan_report.AVEngineScanReport(
                            def_time = '2020-03-11T11:08:00.000Z', 
                            eng_id = 'clamav_1_windows', 
                            location = 'local', 
                            scan_result_i = 0, 
                            scan_time = 336, 
                            threat_found = '0', 
                            wait_time = 3, ), ), ), 
                vulnerability_info = openapi_client.models.vulnerability_response.VulnerabilityResponse(
                    result = openapi_client.models.vulnerability_response_result.VulnerabilityResponse_result(
                        code = 0, 
                        hash = 'B428501D1FAD1BA14AA2FC3F9B5F051EC8721EA2', 
                        method = 50700, 
                        timestamp = '1493020752', 
                        timing = 48, 
                        detected_product = openapi_client.models.vulnerability_response_result_detected_product.VulnerabilityResponse_result_detected_product(
                            has_vulnerability = True, 
                            is_current = False, 
                            product = openapi_client.models.vulnerability_response_result_detected_product_product.VulnerabilityResponse_result_detected_product_product(
                                id = 104, 
                                name = 'Adobe Flash Player', ), 
                            remediation_link = 'http://get.adobe.com/flashplayer/', 
                            severity = 'critical', 
                            sig_name = 'Adobe Flash Player', 
                            signature = 107, 
                            vendor = openapi_client.models.vulnerability_response_result_detected_product_vendor.VulnerabilityResponse_result_detected_product_vendor(
                                id = 91, 
                                name = 'Adobe Systems Inc.', ), 
                            version = '20.0.0.235', 
                            version_data = openapi_client.models.vulnerability_response_result_detected_product_version_data.VulnerabilityResponse_result_detected_product_version_data(
                                count_behind = 65, 
                                feed_id = 200005, 
                                version = '25.0.0.149', ), ), 
                        vulnerabilites = [
                            openapi_client.models.vulnerability_response_result_vulnerabilites.VulnerabilityResponse_result_vulnerabilites(
                                description = 'Adobe Flash Player before 18.0.0.324 and 19.x and 20.x before 20.0.0.267 on Windows and OS X and before 11.2.202.559 on Linux, Adobe AIR before 20.0.0.233, Adobe AIR SDK before 20.0.0.233, and Adobe AIR SDK & Compiler before 20.0.0.233 allow attackers to execute arbitrary code or cause a denial of service (memory corruption) via unspecified vectors, a different vulnerability than CVE-2015-8460, CVE-2015-8636, and CVE-2015-8645.
', 
                                details = openapi_client.models.vulnerability_response_result_details.VulnerabilityResponse_result_details(
                                    cpe = 'cpe:/a:adobe:flash player', 
                                    cve = 'CVE-2015-8459', 
                                    cvss = openapi_client.models.vulnerability_response_result_details_cvss.VulnerabilityResponse_result_details_cvss(
                                        access_complexity = 'LOW', 
                                        access_vector = 'NETWORK', 
                                        authentication = 'NONE', 
                                        availability_impact = '0', 
                                        confidentiality_impact = 'COMPLETE', 
                                        generated_on_epoch = '1451411824', 
                                        integrity_impact = 'COMPLETE', 
                                        score = '10.0', 
                                        source = 'http://nvd.nist.gov', ), 
                                    cwe = 'CWE-119', 
                                    last_modified_epoch = '1487300348', 
                                    published_epoch = '1451347140', 
                                    references = [
                                        'http://lists.opensuse.org/opensuse-security-announce/2015-12/msg00045.html'
                                        ], ), 
                                severity = 'CRITICAL', 
                                severity_index = 5, 
                                static_id = 20158459, )
                            ], ), ), 
                yara = openapi_client.models.yara_report.YaraReport(
                    hits = openapi_client.models.hits.hits(), 
                    verdict = 0, )
            )
        else :
            return AnalysisResult(
        )

    def testAnalysisResult(self):
        """Test AnalysisResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
