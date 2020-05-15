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
import AnalysisResultProcessInfoPostProcessing from './AnalysisResultProcessInfoPostProcessing';

/**
 * The AnalysisResultProcessInfo model module.
 * @module model/AnalysisResultProcessInfo
 * @version v4.18.0
 */
class AnalysisResultProcessInfo {
    /**
     * Constructs a new <code>AnalysisResultProcessInfo</code>.
     * Processing information
     * @alias module:model/AnalysisResultProcessInfo
     */
    constructor() { 
        
        AnalysisResultProcessInfo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnalysisResultProcessInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnalysisResultProcessInfo} obj Optional instance to populate.
     * @return {module:model/AnalysisResultProcessInfo} The populated <code>AnalysisResultProcessInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnalysisResultProcessInfo();

            if (data.hasOwnProperty('blocked_reason')) {
                obj['blocked_reason'] = ApiClient.convertToType(data['blocked_reason'], 'String');
            }
            if (data.hasOwnProperty('file_type_skipped_scan')) {
                obj['file_type_skipped_scan'] = ApiClient.convertToType(data['file_type_skipped_scan'], 'Boolean');
            }
            if (data.hasOwnProperty('outdated_data')) {
                obj['outdated_data'] = ApiClient.convertToType(data['outdated_data'], ['String']);
            }
            if (data.hasOwnProperty('processing_time')) {
                obj['processing_time'] = ApiClient.convertToType(data['processing_time'], 'Number');
            }
            if (data.hasOwnProperty('profile')) {
                obj['profile'] = ApiClient.convertToType(data['profile'], 'String');
            }
            if (data.hasOwnProperty('progress_percentage')) {
                obj['progress_percentage'] = ApiClient.convertToType(data['progress_percentage'], 'Number');
            }
            if (data.hasOwnProperty('queue_time')) {
                obj['queue_time'] = ApiClient.convertToType(data['queue_time'], 'Number');
            }
            if (data.hasOwnProperty('result')) {
                obj['result'] = ApiClient.convertToType(data['result'], 'String');
            }
            if (data.hasOwnProperty('user_agent')) {
                obj['user_agent'] = ApiClient.convertToType(data['user_agent'], 'String');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
            if (data.hasOwnProperty('verdicts')) {
                obj['verdicts'] = ApiClient.convertToType(data['verdicts'], ['String']);
            }
            if (data.hasOwnProperty('post_processing')) {
                obj['post_processing'] = AnalysisResultProcessInfoPostProcessing.constructFromObject(data['post_processing']);
            }
        }
        return obj;
    }


}

/**
 * Provides the reason why the file is blocked (if so).
 * @member {String} blocked_reason
 */
AnalysisResultProcessInfo.prototype['blocked_reason'] = undefined;

/**
 * Indicates if the input file's detected type was configured to skip scanning.
 * @member {Boolean} file_type_skipped_scan
 */
AnalysisResultProcessInfo.prototype['file_type_skipped_scan'] = undefined;

/**
 * array of flags - if occur - describing outdated data in the result, these can be   * enginedefinitions: at least one of the AV engines the item was scanned with has a newer definition database   * configuration: the process' rule - or any item used by the rule - was modified since the item was processed   * sanitization: if item was sanitized this flag notifies that the sanitization information regarding this result is outdated, meaning the sanitized item is no longer available               
 * @member {Array.<module:model/AnalysisResultProcessInfo.OutdatedDataEnum>} outdated_data
 */
AnalysisResultProcessInfo.prototype['outdated_data'] = undefined;

/**
 * Total time elapsed during processing file on the node (in milliseconds).
 * @member {Number} processing_time
 */
AnalysisResultProcessInfo.prototype['processing_time'] = undefined;

/**
 * The used rule name.
 * @member {String} profile
 */
AnalysisResultProcessInfo.prototype['profile'] = undefined;

/**
 * Percentage of processing completed (from 1-100).
 * @member {Number} progress_percentage
 */
AnalysisResultProcessInfo.prototype['progress_percentage'] = undefined;

/**
 * Total time elapsed while the file waits in the queue (in milliseconds).
 * @member {Number} queue_time
 */
AnalysisResultProcessInfo.prototype['queue_time'] = undefined;

/**
 * The final result of processing the file (Allowed / Blocked / Processing).
 * @member {String} result
 */
AnalysisResultProcessInfo.prototype['result'] = undefined;

/**
 * Identifier for the REST Client that calls the API.
 * @member {String} user_agent
 */
AnalysisResultProcessInfo.prototype['user_agent'] = undefined;

/**
 * User identifier who submitted scan request earlier.
 * @member {String} username
 */
AnalysisResultProcessInfo.prototype['username'] = undefined;

/**
 * Aggregated list of potential issues.
 * @member {Array.<String>} verdicts
 */
AnalysisResultProcessInfo.prototype['verdicts'] = undefined;

/**
 * @member {module:model/AnalysisResultProcessInfoPostProcessing} post_processing
 */
AnalysisResultProcessInfo.prototype['post_processing'] = undefined;





/**
 * Allowed values for the <code>outdatedData</code> property.
 * @enum {String}
 * @readonly
 */
AnalysisResultProcessInfo['OutdatedDataEnum'] = {

    /**
     * value: "enginedefinition"
     * @const
     */
    "enginedefinition": "enginedefinition",

    /**
     * value: "configuration"
     * @const
     */
    "configuration": "configuration",

    /**
     * value: "sanitization"
     * @const
     */
    "sanitization": "sanitization"
};



export default AnalysisResultProcessInfo;

