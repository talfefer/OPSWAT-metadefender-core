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


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.DLPResponseDlpInfoHits;
import org.openapitools.client.model.DLPResponseDlpInfoMetadataRemoval;
import org.openapitools.client.model.DLPResponseDlpInfoRedact;
import org.openapitools.client.model.DLPResponseDlpInfoWatermark;
import org.junit.Assert;
import org.junit.Ignore;
import org.junit.Test;


/**
 * Model tests for DLPResponseDlpInfo
 */
public class DLPResponseDlpInfoTest {
    private final DLPResponseDlpInfo model = new DLPResponseDlpInfo();

    /**
     * Model tests for DLPResponseDlpInfo
     */
    @Test
    public void testDLPResponseDlpInfo() {
        // TODO: test DLPResponseDlpInfo
    }

    /**
     * Test the property 'certainty'
     */
    @Test
    public void certaintyTest() {
        // TODO: test certainty
    }

    /**
     * Test the property 'errors'
     */
    @Test
    public void errorsTest() {
        // TODO: test errors
    }

    /**
     * Test the property 'filename'
     */
    @Test
    public void filenameTest() {
        // TODO: test filename
    }

    /**
     * Test the property 'hits'
     */
    @Test
    public void hitsTest() {
        // TODO: test hits
    }

    /**
     * Test the property 'metadataRemoval'
     */
    @Test
    public void metadataRemovalTest() {
        // TODO: test metadataRemoval
    }

    /**
     * Test the property 'redact'
     */
    @Test
    public void redactTest() {
        // TODO: test redact
    }

    /**
     * Test the property 'severity'
     */
    @Test
    public void severityTest() {
        // TODO: test severity
    }

    /**
     * Test the property 'verdict'
     */
    @Test
    public void verdictTest() {
        // TODO: test verdict
    }

    /**
     * Test the property 'watermark'
     */
    @Test
    public void watermarkTest() {
        // TODO: test watermark
    }

}
