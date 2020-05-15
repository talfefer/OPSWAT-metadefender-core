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


package org.openapitools.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.openapitools.model.BatchResponseBatchFiles;
import org.openapitools.model.BatchResponseProcessInfo;
import org.openapitools.model.BatchResponseScanResults;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import javax.validation.constraints.*;
import javax.validation.Valid;

/**
 * The response for a Batch status request.
 */
@ApiModel(description = "The response for a Batch status request.")
@JsonPropertyOrder({
  BatchResponse.JSON_PROPERTY_BATCH_FILES,
  BatchResponse.JSON_PROPERTY_BATCH_ID,
  BatchResponse.JSON_PROPERTY_IS_CLOSED,
  BatchResponse.JSON_PROPERTY_PROCESS_INFO,
  BatchResponse.JSON_PROPERTY_SCAN_RESULTS,
  BatchResponse.JSON_PROPERTY_USER_DATA
})
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaJerseyServerCodegen", date = "2020-05-15T23:49:49.064488Z[UTC]")
public class BatchResponse   {
  public static final String JSON_PROPERTY_BATCH_FILES = "batch_files";
  @JsonProperty(JSON_PROPERTY_BATCH_FILES)
  private BatchResponseBatchFiles batchFiles;

  public static final String JSON_PROPERTY_BATCH_ID = "batch_id";
  @JsonProperty(JSON_PROPERTY_BATCH_ID)
  private String batchId;

  public static final String JSON_PROPERTY_IS_CLOSED = "is_closed";
  @JsonProperty(JSON_PROPERTY_IS_CLOSED)
  private Boolean isClosed;

  public static final String JSON_PROPERTY_PROCESS_INFO = "process_info";
  @JsonProperty(JSON_PROPERTY_PROCESS_INFO)
  private BatchResponseProcessInfo processInfo;

  public static final String JSON_PROPERTY_SCAN_RESULTS = "scan_results";
  @JsonProperty(JSON_PROPERTY_SCAN_RESULTS)
  private BatchResponseScanResults scanResults;

  public static final String JSON_PROPERTY_USER_DATA = "user_data";
  @JsonProperty(JSON_PROPERTY_USER_DATA)
  private String userData;

  public BatchResponse batchFiles(BatchResponseBatchFiles batchFiles) {
    this.batchFiles = batchFiles;
    return this;
  }

  /**
   * Get batchFiles
   * @return batchFiles
   **/
  @JsonProperty("batch_files")
  @ApiModelProperty(value = "")
  @Valid 
  public BatchResponseBatchFiles getBatchFiles() {
    return batchFiles;
  }

  public void setBatchFiles(BatchResponseBatchFiles batchFiles) {
    this.batchFiles = batchFiles;
  }

  public BatchResponse batchId(String batchId) {
    this.batchId = batchId;
    return this;
  }

  /**
   * The batch unique identifer
   * @return batchId
   **/
  @JsonProperty("batch_id")
  @ApiModelProperty(example = "b7cc760038324b02908a5c111cb1563d", value = "The batch unique identifer")
  
  public String getBatchId() {
    return batchId;
  }

  public void setBatchId(String batchId) {
    this.batchId = batchId;
  }

  public BatchResponse isClosed(Boolean isClosed) {
    this.isClosed = isClosed;
    return this;
  }

  /**
   * The batch status (open/close).
   * @return isClosed
   **/
  @JsonProperty("is_closed")
  @ApiModelProperty(example = "false", value = "The batch status (open/close).")
  
  public Boolean getIsClosed() {
    return isClosed;
  }

  public void setIsClosed(Boolean isClosed) {
    this.isClosed = isClosed;
  }

  public BatchResponse processInfo(BatchResponseProcessInfo processInfo) {
    this.processInfo = processInfo;
    return this;
  }

  /**
   * Get processInfo
   * @return processInfo
   **/
  @JsonProperty("process_info")
  @ApiModelProperty(value = "")
  @Valid 
  public BatchResponseProcessInfo getProcessInfo() {
    return processInfo;
  }

  public void setProcessInfo(BatchResponseProcessInfo processInfo) {
    this.processInfo = processInfo;
  }

  public BatchResponse scanResults(BatchResponseScanResults scanResults) {
    this.scanResults = scanResults;
    return this;
  }

  /**
   * Get scanResults
   * @return scanResults
   **/
  @JsonProperty("scan_results")
  @ApiModelProperty(value = "")
  @Valid 
  public BatchResponseScanResults getScanResults() {
    return scanResults;
  }

  public void setScanResults(BatchResponseScanResults scanResults) {
    this.scanResults = scanResults;
  }

  public BatchResponse userData(String userData) {
    this.userData = userData;
    return this;
  }

  /**
   * Metadata submitted at batch creation.
   * @return userData
   **/
  @JsonProperty("user_data")
  @ApiModelProperty(example = "http://localhost:8008/", value = "Metadata submitted at batch creation.")
  
  public String getUserData() {
    return userData;
  }

  public void setUserData(String userData) {
    this.userData = userData;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BatchResponse batchResponse = (BatchResponse) o;
    return Objects.equals(this.batchFiles, batchResponse.batchFiles) &&
        Objects.equals(this.batchId, batchResponse.batchId) &&
        Objects.equals(this.isClosed, batchResponse.isClosed) &&
        Objects.equals(this.processInfo, batchResponse.processInfo) &&
        Objects.equals(this.scanResults, batchResponse.scanResults) &&
        Objects.equals(this.userData, batchResponse.userData);
  }

  @Override
  public int hashCode() {
    return Objects.hash(batchFiles, batchId, isClosed, processInfo, scanResults, userData);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BatchResponse {\n");
    
    sb.append("    batchFiles: ").append(toIndentedString(batchFiles)).append("\n");
    sb.append("    batchId: ").append(toIndentedString(batchId)).append("\n");
    sb.append("    isClosed: ").append(toIndentedString(isClosed)).append("\n");
    sb.append("    processInfo: ").append(toIndentedString(processInfo)).append("\n");
    sb.append("    scanResults: ").append(toIndentedString(scanResults)).append("\n");
    sb.append("    userData: ").append(toIndentedString(userData)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

