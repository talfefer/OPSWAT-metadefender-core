/**
 * MetaDefender Core
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AnalysisResultProcessInfo from './AnalysisResultProcessInfo';
import DLPResponse from './DLPResponse';
import FileInformation from './FileInformation';
import MetascanReport from './MetascanReport';
import VulnerabilityResponse from './VulnerabilityResponse';
import YaraReport from './YaraReport';

/**
 * The AnalysisResult model module.
 * @module model/AnalysisResult
 * @version v4.18.0
 */
class AnalysisResult {
    /**
     * Constructs a new <code>AnalysisResult</code>.
     * @alias module:model/AnalysisResult
     */
    constructor() { 
        
        AnalysisResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnalysisResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnalysisResult} obj Optional instance to populate.
     * @return {module:model/AnalysisResult} The populated <code>AnalysisResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnalysisResult();

            if (data.hasOwnProperty('data_id')) {
                obj['data_id'] = ApiClient.convertToType(data['data_id'], 'String');
            }
            if (data.hasOwnProperty('dlp_info')) {
                obj['dlp_info'] = DLPResponse.constructFromObject(data['dlp_info']);
            }
            if (data.hasOwnProperty('file_info')) {
                obj['file_info'] = FileInformation.constructFromObject(data['file_info']);
            }
            if (data.hasOwnProperty('process_info')) {
                obj['process_info'] = AnalysisResultProcessInfo.constructFromObject(data['process_info']);
            }
            if (data.hasOwnProperty('scan_results')) {
                obj['scan_results'] = MetascanReport.constructFromObject(data['scan_results']);
            }
            if (data.hasOwnProperty('vulnerability_info')) {
                obj['vulnerability_info'] = VulnerabilityResponse.constructFromObject(data['vulnerability_info']);
            }
            if (data.hasOwnProperty('yara')) {
                obj['yara'] = YaraReport.constructFromObject(data['yara']);
            }
        }
        return obj;
    }


}

/**
 * data identifier of the requested file
 * @member {String} data_id
 */
AnalysisResult.prototype['data_id'] = undefined;

/**
 * @member {module:model/DLPResponse} dlp_info
 */
AnalysisResult.prototype['dlp_info'] = undefined;

/**
 * @member {module:model/FileInformation} file_info
 */
AnalysisResult.prototype['file_info'] = undefined;

/**
 * @member {module:model/AnalysisResultProcessInfo} process_info
 */
AnalysisResult.prototype['process_info'] = undefined;

/**
 * @member {module:model/MetascanReport} scan_results
 */
AnalysisResult.prototype['scan_results'] = undefined;

/**
 * @member {module:model/VulnerabilityResponse} vulnerability_info
 */
AnalysisResult.prototype['vulnerability_info'] = undefined;

/**
 * @member {module:model/YaraReport} yara
 */
AnalysisResult.prototype['yara'] = undefined;






export default AnalysisResult;

