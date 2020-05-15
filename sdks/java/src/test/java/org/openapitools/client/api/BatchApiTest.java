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
import org.openapitools.client.model.BatchId;
import org.openapitools.client.model.BatchResponse;
import org.openapitools.client.model.InlineResponse400;
import org.openapitools.client.model.InlineResponse500;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for BatchApi
 */
@Ignore
public class BatchApiTest {

    private final BatchApi api = new BatchApi();

    
    /**
     * Cancel Batch
     *
     * When cancelling a batch, the connected analysis that are still in progress will be cancelled also.   The cancelled batch will be closed.      
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void batchCancelTest() throws ApiException {
        String batchId = null;
        String apikey = null;
        Object response = api.batchCancel(batchId, apikey);

        // TODO: test validations
    }
    
    /**
     * Close Batch
     *
     * The batch will be closed and files can no longer can be added to the current batch.      
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void batchCloseTest() throws ApiException {
        String batchId = null;
        String apikey = null;
        BatchResponse response = api.batchClose(batchId, apikey);

        // TODO: test validations
    }
    
    /**
     * Initiate Batch
     *
     * Create a new batch and retrieve the batch_id
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void batchCreateTest() throws ApiException {
        String apikey = null;
        String rule = null;
        String userAgent = null;
        String userData = null;
        BatchId response = api.batchCreate(apikey, rule, userAgent, userData);

        // TODO: test validations
    }
    
    /**
     * Download Signed Batch Result
     *
     * Download digitally signed status report for the entire batch
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void batchSignedResultTest() throws ApiException {
        String batchId = null;
        String apikey = null;
        api.batchSignedResult(batchId, apikey);

        // TODO: test validations
    }
    
    /**
     * Status of Batch Analysis
     *
     * Retrieve status report for the entire batch
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void batchStatusTest() throws ApiException {
        String batchId = null;
        String apikey = null;
        BatchResponse response = api.batchStatus(batchId, apikey);

        // TODO: test validations
    }
    
}
