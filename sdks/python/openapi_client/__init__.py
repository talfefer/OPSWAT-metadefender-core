# coding: utf-8

# flake8: noqa

"""
    MetaDefender Core

    ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works.   # noqa: E501

    The version of the OpenAPI document: v4.18.0
    Contact: feedback@opswat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.admin_api import AdminApi
from openapi_client.api.analysis_api import AnalysisApi
from openapi_client.api.auth_api import AuthApi
from openapi_client.api.batch_api import BatchApi
from openapi_client.api.config_api import ConfigApi
from openapi_client.api.engines_api import EnginesApi
from openapi_client.api.license_api import LicenseApi
from openapi_client.api.stats_api import StatsApi
from openapi_client.api.yara_api import YaraApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.models.av_engine_scan_report import AVEngineScanReport
from openapi_client.models.admin_config_session import AdminConfigSession
from openapi_client.models.admin_config_update import AdminConfigUpdate
from openapi_client.models.admin_config_update_disabledupdate import AdminConfigUpdateDisabledupdate
from openapi_client.models.admin_config_webhook import AdminConfigWebhook
from openapi_client.models.analysis_result import AnalysisResult
from openapi_client.models.analysis_result_process_info import AnalysisResultProcessInfo
from openapi_client.models.analysis_result_process_info_post_processing import AnalysisResultProcessInfoPostProcessing
from openapi_client.models.batch_id import BatchId
from openapi_client.models.batch_response import BatchResponse
from openapi_client.models.batch_response_batch_files import BatchResponseBatchFiles
from openapi_client.models.batch_response_batch_files_files_in_batch import BatchResponseBatchFilesFilesInBatch
from openapi_client.models.batch_response_batch_files_process_info import BatchResponseBatchFilesProcessInfo
from openapi_client.models.batch_response_process_info import BatchResponseProcessInfo
from openapi_client.models.batch_response_scan_results import BatchResponseScanResults
from openapi_client.models.dlp_response import DLPResponse
from openapi_client.models.dlp_response_dlp_info import DLPResponseDlpInfo
from openapi_client.models.dlp_response_dlp_info_hits import DLPResponseDlpInfoHits
from openapi_client.models.dlp_response_dlp_info_hits_ccn import DLPResponseDlpInfoHitsCcn
from openapi_client.models.dlp_response_dlp_info_metadata_removal import DLPResponseDlpInfoMetadataRemoval
from openapi_client.models.dlp_response_dlp_info_redact import DLPResponseDlpInfoRedact
from openapi_client.models.dlp_response_dlp_info_watermark import DLPResponseDlpInfoWatermark
from openapi_client.models.dlp_rule_match_result import DLPRuleMatchResult
from openapi_client.models.deep_cdr_details import DeepCDRDetails
from openapi_client.models.deep_cdr_details_details import DeepCDRDetailsDetails
from openapi_client.models.file_information import FileInformation
from openapi_client.models.inline_object import InlineObject
from openapi_client.models.inline_object1 import InlineObject1
from openapi_client.models.inline_object2 import InlineObject2
from openapi_client.models.inline_response200 import InlineResponse200
from openapi_client.models.inline_response2001 import InlineResponse2001
from openapi_client.models.inline_response20010 import InlineResponse20010
from openapi_client.models.inline_response20011 import InlineResponse20011
from openapi_client.models.inline_response20012 import InlineResponse20012
from openapi_client.models.inline_response20013 import InlineResponse20013
from openapi_client.models.inline_response2002 import InlineResponse2002
from openapi_client.models.inline_response2003 import InlineResponse2003
from openapi_client.models.inline_response2004 import InlineResponse2004
from openapi_client.models.inline_response2005 import InlineResponse2005
from openapi_client.models.inline_response2006 import InlineResponse2006
from openapi_client.models.inline_response2007 import InlineResponse2007
from openapi_client.models.inline_response2007_issues import InlineResponse2007Issues
from openapi_client.models.inline_response2007_issues_general import InlineResponse2007IssuesGeneral
from openapi_client.models.inline_response2007_issues_source import InlineResponse2007IssuesSource
from openapi_client.models.inline_response2008 import InlineResponse2008
from openapi_client.models.inline_response2009 import InlineResponse2009
from openapi_client.models.inline_response400 import InlineResponse400
from openapi_client.models.inline_response403 import InlineResponse403
from openapi_client.models.inline_response500 import InlineResponse500
from openapi_client.models.license_information import LicenseInformation
from openapi_client.models.metascan_report import MetascanReport
from openapi_client.models.metascan_report_scan_details import MetascanReportScanDetails
from openapi_client.models.new_user_role_request import NewUserRoleRequest
from openapi_client.models.new_user_role_request_rights import NewUserRoleRequestRights
from openapi_client.models.new_user_role_response import NewUserRoleResponse
from openapi_client.models.new_user_role_response_all_of import NewUserRoleResponseAllOf
from openapi_client.models.processing_results_index_enum import ProcessingResultsIndexEnum
from openapi_client.models.processing_results_string_enum import ProcessingResultsStringEnum
from openapi_client.models.role_permission_object import RolePermissionObject
from openapi_client.models.scan_result_enum import ScanResultEnum
from openapi_client.models.skip_list import SkipList
from openapi_client.models.stat_nodes_engines import StatNodesEngines
from openapi_client.models.stat_nodes_issues import StatNodesIssues
from openapi_client.models.stat_nodes_statuses import StatNodesStatuses
from openapi_client.models.user_login import UserLogin
from openapi_client.models.user_request import UserRequest
from openapi_client.models.user_request_all_of import UserRequestAllOf
from openapi_client.models.user_response import UserResponse
from openapi_client.models.vulnerability_response import VulnerabilityResponse
from openapi_client.models.vulnerability_response_result import VulnerabilityResponseResult
from openapi_client.models.vulnerability_response_result_details import VulnerabilityResponseResultDetails
from openapi_client.models.vulnerability_response_result_details_cvss import VulnerabilityResponseResultDetailsCvss
from openapi_client.models.vulnerability_response_result_detected_product import VulnerabilityResponseResultDetectedProduct
from openapi_client.models.vulnerability_response_result_detected_product_product import VulnerabilityResponseResultDetectedProductProduct
from openapi_client.models.vulnerability_response_result_detected_product_vendor import VulnerabilityResponseResultDetectedProductVendor
from openapi_client.models.vulnerability_response_result_detected_product_version_data import VulnerabilityResponseResultDetectedProductVersionData
from openapi_client.models.vulnerability_response_result_vulnerabilites import VulnerabilityResponseResultVulnerabilites
from openapi_client.models.yara_report import YaraReport
from openapi_client.models.yara_sources_object import YaraSourcesObject
from openapi_client.models.yara_sources_object_http_sources import YaraSourcesObjectHttpSources
from openapi_client.models.yara_sources_object_local_sources import YaraSourcesObjectLocalSources

