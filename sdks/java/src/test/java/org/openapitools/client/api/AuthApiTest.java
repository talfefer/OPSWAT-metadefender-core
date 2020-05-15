/*
 * MetaDefender Core
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.InlineObject;
import org.openapitools.client.model.InlineObject2;
import org.openapitools.client.model.InlineResponse403;
import org.openapitools.client.model.InlineResponse500;
import org.openapitools.client.model.UserLogin;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AuthApi
 */
@Ignore
public class AuthApiTest {

    private final AuthApi api = new AuthApi();

    
    /**
     * Change Password
     *
     * Modify the current password for the user identified by apikey
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userChangePassTest() throws ApiException {
        String apikey = null;
        InlineObject2 inlineObject2 = null;
        api.userChangePass(apikey, inlineObject2);

        // TODO: test validations
    }
    
    /**
     * Login
     *
     * Initiate a new session. Required for using protected REST APIs.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userLoginTest() throws ApiException {
        InlineObject inlineObject = null;
        UserLogin response = api.userLogin(inlineObject);

        // TODO: test validations
    }
    
    /**
     * Logout
     *
     * Destroy session for not using protected REST APIs.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void userLogoutTest() throws ApiException {
        String apikey = null;
        api.userLogout(apikey);

        // TODO: test validations
    }
    
}
