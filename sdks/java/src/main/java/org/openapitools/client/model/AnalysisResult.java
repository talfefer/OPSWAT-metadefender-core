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

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.AnalysisResultProcessInfo;
import org.openapitools.client.model.DLPResponse;
import org.openapitools.client.model.FileInformation;
import org.openapitools.client.model.MetascanReport;
import org.openapitools.client.model.VulnerabilityResponse;
import org.openapitools.client.model.YaraReport;

/**
 * AnalysisResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-05-15T23:48:50.618888Z[UTC]")
public class AnalysisResult {
  public static final String SERIALIZED_NAME_DATA_ID = "data_id";
  @SerializedName(SERIALIZED_NAME_DATA_ID)
  private String dataId;

  public static final String SERIALIZED_NAME_DLP_INFO = "dlp_info";
  @SerializedName(SERIALIZED_NAME_DLP_INFO)
  private DLPResponse dlpInfo;

  public static final String SERIALIZED_NAME_FILE_INFO = "file_info";
  @SerializedName(SERIALIZED_NAME_FILE_INFO)
  private FileInformation fileInfo;

  public static final String SERIALIZED_NAME_PROCESS_INFO = "process_info";
  @SerializedName(SERIALIZED_NAME_PROCESS_INFO)
  private AnalysisResultProcessInfo processInfo;

  public static final String SERIALIZED_NAME_SCAN_RESULTS = "scan_results";
  @SerializedName(SERIALIZED_NAME_SCAN_RESULTS)
  private MetascanReport scanResults;

  public static final String SERIALIZED_NAME_VULNERABILITY_INFO = "vulnerability_info";
  @SerializedName(SERIALIZED_NAME_VULNERABILITY_INFO)
  private VulnerabilityResponse vulnerabilityInfo;

  public static final String SERIALIZED_NAME_YARA = "yara";
  @SerializedName(SERIALIZED_NAME_YARA)
  private YaraReport yara;


  public AnalysisResult dataId(String dataId) {
    
    this.dataId = dataId;
    return this;
  }

   /**
   * data identifier of the requested file
   * @return dataId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "8101abae27be4d63859c55d9e0ed0135", value = "data identifier of the requested file")

  public String getDataId() {
    return dataId;
  }


  public void setDataId(String dataId) {
    this.dataId = dataId;
  }


  public AnalysisResult dlpInfo(DLPResponse dlpInfo) {
    
    this.dlpInfo = dlpInfo;
    return this;
  }

   /**
   * Get dlpInfo
   * @return dlpInfo
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public DLPResponse getDlpInfo() {
    return dlpInfo;
  }


  public void setDlpInfo(DLPResponse dlpInfo) {
    this.dlpInfo = dlpInfo;
  }


  public AnalysisResult fileInfo(FileInformation fileInfo) {
    
    this.fileInfo = fileInfo;
    return this;
  }

   /**
   * Get fileInfo
   * @return fileInfo
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public FileInformation getFileInfo() {
    return fileInfo;
  }


  public void setFileInfo(FileInformation fileInfo) {
    this.fileInfo = fileInfo;
  }


  public AnalysisResult processInfo(AnalysisResultProcessInfo processInfo) {
    
    this.processInfo = processInfo;
    return this;
  }

   /**
   * Get processInfo
   * @return processInfo
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public AnalysisResultProcessInfo getProcessInfo() {
    return processInfo;
  }


  public void setProcessInfo(AnalysisResultProcessInfo processInfo) {
    this.processInfo = processInfo;
  }


  public AnalysisResult scanResults(MetascanReport scanResults) {
    
    this.scanResults = scanResults;
    return this;
  }

   /**
   * Get scanResults
   * @return scanResults
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public MetascanReport getScanResults() {
    return scanResults;
  }


  public void setScanResults(MetascanReport scanResults) {
    this.scanResults = scanResults;
  }


  public AnalysisResult vulnerabilityInfo(VulnerabilityResponse vulnerabilityInfo) {
    
    this.vulnerabilityInfo = vulnerabilityInfo;
    return this;
  }

   /**
   * Get vulnerabilityInfo
   * @return vulnerabilityInfo
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public VulnerabilityResponse getVulnerabilityInfo() {
    return vulnerabilityInfo;
  }


  public void setVulnerabilityInfo(VulnerabilityResponse vulnerabilityInfo) {
    this.vulnerabilityInfo = vulnerabilityInfo;
  }


  public AnalysisResult yara(YaraReport yara) {
    
    this.yara = yara;
    return this;
  }

   /**
   * Get yara
   * @return yara
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public YaraReport getYara() {
    return yara;
  }


  public void setYara(YaraReport yara) {
    this.yara = yara;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnalysisResult analysisResult = (AnalysisResult) o;
    return Objects.equals(this.dataId, analysisResult.dataId) &&
        Objects.equals(this.dlpInfo, analysisResult.dlpInfo) &&
        Objects.equals(this.fileInfo, analysisResult.fileInfo) &&
        Objects.equals(this.processInfo, analysisResult.processInfo) &&
        Objects.equals(this.scanResults, analysisResult.scanResults) &&
        Objects.equals(this.vulnerabilityInfo, analysisResult.vulnerabilityInfo) &&
        Objects.equals(this.yara, analysisResult.yara);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dataId, dlpInfo, fileInfo, processInfo, scanResults, vulnerabilityInfo, yara);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnalysisResult {\n");
    sb.append("    dataId: ").append(toIndentedString(dataId)).append("\n");
    sb.append("    dlpInfo: ").append(toIndentedString(dlpInfo)).append("\n");
    sb.append("    fileInfo: ").append(toIndentedString(fileInfo)).append("\n");
    sb.append("    processInfo: ").append(toIndentedString(processInfo)).append("\n");
    sb.append("    scanResults: ").append(toIndentedString(scanResults)).append("\n");
    sb.append("    vulnerabilityInfo: ").append(toIndentedString(vulnerabilityInfo)).append("\n");
    sb.append("    yara: ").append(toIndentedString(yara)).append("\n");
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

