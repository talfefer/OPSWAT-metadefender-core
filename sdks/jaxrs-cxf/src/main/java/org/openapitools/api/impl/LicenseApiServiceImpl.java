package org.openapitools.api.impl;

import org.openapitools.api.*;
import org.openapitools.model.InlineResponse500;
import org.openapitools.model.LicenseInformation;
import org.openapitools.model.UNKNOWN_BASE_TYPE;

import java.io.InputStream;
import java.io.OutputStream;
import java.util.List;
import java.util.Map;
import javax.ws.rs.*;
import javax.ws.rs.core.Response;
import org.apache.cxf.jaxrs.model.wadl.Description;
import org.apache.cxf.jaxrs.model.wadl.DocTarget;

import org.apache.cxf.jaxrs.ext.multipart.*;

import io.swagger.annotations.Api;

/**
 * MetaDefender Core
 *
 * <p>## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 */
public class LicenseApiServiceImpl implements LicenseApi {
    /**
     * Activate license
     *
     * This API initiates an online activation of the deployment.  In case of error, check the application logs for more details.
     *
     */
    public void licenseActivation(String apikey, UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE) {
        // TODO: Implement...
        
        
    }
    
    /**
     * Get Current License Information
     *
     * Fetch all details about the licensing status of the product.
     *
     */
    public LicenseInformation licenseGet(String apikey) {
        // TODO: Implement...
        
        return null;
    }
    
    /**
     * Upload license key
     *
     * Uploading a license file to the Metadefender Core.  There are two ways two obtain a license key file:  - via https://portal.opswat.com/activation portal  - via activation server REST API: https://activation.dl.opswat.com/activation?key&#x3D;%activation_key%&amp;deployment&#x3D;%deployment_unique_ID%&amp;quantity&#x3D;%quantity%  Deployment unique ID can be fetched via Get Current License Information API.      
     *
     */
    public void licenseUpload(String apikey, String body) {
        // TODO: Implement...
        
        
    }
    
}

