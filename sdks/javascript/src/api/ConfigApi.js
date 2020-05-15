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


import ApiClient from "../ApiClient";
import AdminConfigSession from '../model/AdminConfigSession';
import AdminConfigUpdate from '../model/AdminConfigUpdate';
import AdminConfigWebhook from '../model/AdminConfigWebhook';
import InlineObject1 from '../model/InlineObject1';
import InlineResponse200 from '../model/InlineResponse200';
import InlineResponse2001 from '../model/InlineResponse2001';
import InlineResponse500 from '../model/InlineResponse500';
import SkipList from '../model/SkipList';
import UNKNOWN_BASE_TYPE from '../model/UNKNOWN_BASE_TYPE';

/**
* Config service.
* @module api/ConfigApi
* @version v4.18.0
*/
export default class ConfigApi {

    /**
    * Constructs a new ConfigApi. 
    * @alias module:api/ConfigApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the configAuditLog operation.
     * @callback module:api/ConfigApi~configAuditLogCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InlineResponse200} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Audit clean up
     * Setting audit records (update history) clean up time (clean up records older than).  > _**Note**_:The clean up range is defined in `hours`.  
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:model/UNKNOWN_BASE_TYPE} opts.UNKNOWN_BASE_TYPE 
     * @param {module:api/ConfigApi~configAuditLogCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InlineResponse200}
     */
    configAuditLog(opts, callback) {
      opts = opts || {};
      let postBody = opts['UNKNOWN_BASE_TYPE'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = InlineResponse200;
      return this.apiClient.callApi(
        '/admin/config/auditlog', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configGetSkipHash operation.
     * @callback module:api/ConfigApi~configGetSkipHashCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SkipList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get 'skip by hash' list
     * Get the list of hashes whitelisted or blacklisted.
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:api/ConfigApi~configGetSkipHashCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SkipList}
     */
    configGetSkipHash(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SkipList;
      return this.apiClient.callApi(
        '/admin/config/skip', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configQuarantine operation.
     * @callback module:api/ConfigApi~configQuarantineCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InlineResponse200} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Quarantine clean up
     * Setting quarantine clean up time (clean up records older than).  > _**Note**_:The clean up range is defined in `hours`.  
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:model/UNKNOWN_BASE_TYPE} opts.UNKNOWN_BASE_TYPE 
     * @param {module:api/ConfigApi~configQuarantineCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InlineResponse200}
     */
    configQuarantine(opts, callback) {
      opts = opts || {};
      let postBody = opts['UNKNOWN_BASE_TYPE'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = InlineResponse200;
      return this.apiClient.callApi(
        '/admin/config/quarantine', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configSanitizedRepo operation.
     * @callback module:api/ConfigApi~configSanitizedRepoCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InlineResponse2001} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Sanitized files clean up
     * Setting sanitized files clean up time (clean up records older than).  > _**Note**_:The clean up range is defined in `minutes`.  
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:model/InlineObject1} opts.inlineObject1 
     * @param {module:api/ConfigApi~configSanitizedRepoCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InlineResponse2001}
     */
    configSanitizedRepo(opts, callback) {
      opts = opts || {};
      let postBody = opts['inlineObject1'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = InlineResponse2001;
      return this.apiClient.callApi(
        '/admin/config/sanitize', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configScanHistory operation.
     * @callback module:api/ConfigApi~configScanHistoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InlineResponse200} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Processing history clean up
     * Setting processing history clean up time (clean up records older than).  > _**Note**_:The clean up range is defined in `hours`.  
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:model/UNKNOWN_BASE_TYPE} opts.UNKNOWN_BASE_TYPE 
     * @param {module:api/ConfigApi~configScanHistoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InlineResponse200}
     */
    configScanHistory(opts, callback) {
      opts = opts || {};
      let postBody = opts['UNKNOWN_BASE_TYPE'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = InlineResponse200;
      return this.apiClient.callApi(
        '/admin/config/scanhistory', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configSession operation.
     * @callback module:api/ConfigApi~configSessionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AdminConfigSession} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Session settings
     * Configure settings for session generated upon a successful login See more at [Login](#operation/userLogin) 
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:model/AdminConfigSession} opts.adminConfigSession 
     * @param {module:api/ConfigApi~configSessionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AdminConfigSession}
     */
    configSession(opts, callback) {
      opts = opts || {};
      let postBody = opts['adminConfigSession'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AdminConfigSession;
      return this.apiClient.callApi(
        '/admin/config/session', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configUpdate operation.
     * @callback module:api/ConfigApi~configUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AdminConfigUpdate} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modules Update Source and Frequency
     * Setting update frequency for all modules and engines.  > _**Note**_:The clean up range is defined in `minutes`.  
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:model/AdminConfigUpdate} opts.adminConfigUpdate 
     * @param {module:api/ConfigApi~configUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AdminConfigUpdate}
     */
    configUpdate(opts, callback) {
      opts = opts || {};
      let postBody = opts['adminConfigUpdate'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AdminConfigUpdate;
      return this.apiClient.callApi(
        '/admin/config/update', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configUpdateSkipHash operation.
     * @callback module:api/ConfigApi~configUpdateSkipHashCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SkipList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modify 'skip by hash' list
     * Modify one (or more) of the sources for the Yara Engine. The request body containing whitelist's rules in array under \"whitelist\" key; Each object in the array represents a whitelist: comment: same comment for detailed more information this whitelist settings. engines: containing engine id's strings in array hash: md5, sha1 or sha256 hash 
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:model/SkipList} opts.skipList A list of all skip/white/black-listed hashes.
     * @param {module:api/ConfigApi~configUpdateSkipHashCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SkipList}
     */
    configUpdateSkipHash(opts, callback) {
      opts = opts || {};
      let postBody = opts['skipList'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SkipList;
      return this.apiClient.callApi(
        '/admin/config/skip', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configUpdateWebhook operation.
     * @callback module:api/ConfigApi~configUpdateWebhookCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AdminConfigWebhook} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Webhook set configuration
     * Modifying settings supported for webhook mode 
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:model/AdminConfigWebhook} opts.adminConfigWebhook 
     * @param {module:api/ConfigApi~configUpdateWebhookCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AdminConfigWebhook}
     */
    configUpdateWebhook(opts, callback) {
      opts = opts || {};
      let postBody = opts['adminConfigWebhook'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = ['apikey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AdminConfigWebhook;
      return this.apiClient.callApi(
        '/admin/config/webhook', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configWebhook operation.
     * @callback module:api/ConfigApi~configWebhookCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AdminConfigWebhook} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Webhook get configuration
     * Getting settings supported for webhook mode 
     * @param {Object} opts Optional parameters
     * @param {String} opts.apikey Generated `session_id` from [Login](#operation/userLogin) call can be used as an `apikey` for API calls that require authentication.                
     * @param {module:api/ConfigApi~configWebhookCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AdminConfigWebhook}
     */
    configWebhook(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'apikey': opts['apikey']
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AdminConfigWebhook;
      return this.apiClient.callApi(
        '/admin/config/webhook', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
