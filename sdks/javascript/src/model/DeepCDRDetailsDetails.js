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

/**
 * The DeepCDRDetailsDetails model module.
 * @module model/DeepCDRDetailsDetails
 * @version v4.18.0
 */
class DeepCDRDetailsDetails {
    /**
     * Constructs a new <code>DeepCDRDetailsDetails</code>.
     * @alias module:model/DeepCDRDetailsDetails
     * @param action {module:model/DeepCDRDetailsDetails.ActionEnum} The type of action that was performed
     * @param objectName {String} The object type that was sanitized/removed.
     */
    constructor(action, objectName) { 
        
        DeepCDRDetailsDetails.initialize(this, action, objectName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, action, objectName) { 
        obj['action'] = action;
        obj['object_name'] = objectName;
    }

    /**
     * Constructs a <code>DeepCDRDetailsDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeepCDRDetailsDetails} obj Optional instance to populate.
     * @return {module:model/DeepCDRDetailsDetails} The populated <code>DeepCDRDetailsDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeepCDRDetailsDetails();

            if (data.hasOwnProperty('action')) {
                obj['action'] = ApiClient.convertToType(data['action'], 'String');
            }
            if (data.hasOwnProperty('object_name')) {
                obj['object_name'] = ApiClient.convertToType(data['object_name'], 'String');
            }
            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('object_details')) {
                obj['object_details'] = ApiClient.convertToType(data['object_details'], 'String');
            }
            if (data.hasOwnProperty('file_name')) {
                obj['file_name'] = ApiClient.convertToType(data['file_name'], 'String');
            }
        }
        return obj;
    }


}

/**
 * The type of action that was performed
 * @member {module:model/DeepCDRDetailsDetails.ActionEnum} action
 */
DeepCDRDetailsDetails.prototype['action'] = undefined;

/**
 * The object type that was sanitized/removed.
 * @member {String} object_name
 */
DeepCDRDetailsDetails.prototype['object_name'] = undefined;

/**
 * The number of objects that were sanitized/removed.
 * @member {Number} count
 */
DeepCDRDetailsDetails.prototype['count'] = undefined;

/**
 * Additional information about the sanitized object
 * @member {String} object_details
 */
DeepCDRDetailsDetails.prototype['object_details'] = undefined;

/**
 * If an embedded file was sanitized.
 * @member {String} file_name
 */
DeepCDRDetailsDetails.prototype['file_name'] = undefined;





/**
 * Allowed values for the <code>action</code> property.
 * @enum {String}
 * @readonly
 */
DeepCDRDetailsDetails['ActionEnum'] = {

    /**
     * value: "sanitized"
     * @const
     */
    "sanitized": "sanitized",

    /**
     * value: "removed"
     * @const
     */
    "removed": "removed"
};



export default DeepCDRDetailsDetails;

