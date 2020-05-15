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
import com.fasterxml.jackson.annotation.JsonValue;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.model.AnalysisResultProcessInfoPostProcessing;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import javax.validation.constraints.*;
import javax.validation.Valid;

/**
 * Processing information
 */
@ApiModel(description = "Processing information")
@JsonPropertyOrder({
  AnalysisResultProcessInfo.JSON_PROPERTY_BLOCKED_REASON,
  AnalysisResultProcessInfo.JSON_PROPERTY_FILE_TYPE_SKIPPED_SCAN,
  AnalysisResultProcessInfo.JSON_PROPERTY_OUTDATED_DATA,
  AnalysisResultProcessInfo.JSON_PROPERTY_PROCESSING_TIME,
  AnalysisResultProcessInfo.JSON_PROPERTY_PROFILE,
  AnalysisResultProcessInfo.JSON_PROPERTY_PROGRESS_PERCENTAGE,
  AnalysisResultProcessInfo.JSON_PROPERTY_QUEUE_TIME,
  AnalysisResultProcessInfo.JSON_PROPERTY_RESULT,
  AnalysisResultProcessInfo.JSON_PROPERTY_USER_AGENT,
  AnalysisResultProcessInfo.JSON_PROPERTY_USERNAME,
  AnalysisResultProcessInfo.JSON_PROPERTY_VERDICTS,
  AnalysisResultProcessInfo.JSON_PROPERTY_POST_PROCESSING
})
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaJerseyServerCodegen", date = "2020-05-15T23:49:49.064488Z[UTC]")
public class AnalysisResultProcessInfo   {
  public static final String JSON_PROPERTY_BLOCKED_REASON = "blocked_reason";
  @JsonProperty(JSON_PROPERTY_BLOCKED_REASON)
  private String blockedReason;

  public static final String JSON_PROPERTY_FILE_TYPE_SKIPPED_SCAN = "file_type_skipped_scan";
  @JsonProperty(JSON_PROPERTY_FILE_TYPE_SKIPPED_SCAN)
  private Boolean fileTypeSkippedScan;

  /**
   * Gets or Sets outdatedData
   */
  public enum OutdatedDataEnum {
    ENGINEDEFINITION("enginedefinition"),
    
    CONFIGURATION("configuration"),
    
    SANITIZATION("sanitization");

    private String value;

    OutdatedDataEnum(String value) {
      this.value = value;
    }

    @Override
    @JsonValue
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static OutdatedDataEnum fromValue(String value) {
      for (OutdatedDataEnum b : OutdatedDataEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }
  }

  public static final String JSON_PROPERTY_OUTDATED_DATA = "outdated_data";
  @JsonProperty(JSON_PROPERTY_OUTDATED_DATA)
  private List<OutdatedDataEnum> outdatedData = null;

  public static final String JSON_PROPERTY_PROCESSING_TIME = "processing_time";
  @JsonProperty(JSON_PROPERTY_PROCESSING_TIME)
  private Integer processingTime;

  public static final String JSON_PROPERTY_PROFILE = "profile";
  @JsonProperty(JSON_PROPERTY_PROFILE)
  private String profile;

  public static final String JSON_PROPERTY_PROGRESS_PERCENTAGE = "progress_percentage";
  @JsonProperty(JSON_PROPERTY_PROGRESS_PERCENTAGE)
  private Integer progressPercentage;

  public static final String JSON_PROPERTY_QUEUE_TIME = "queue_time";
  @JsonProperty(JSON_PROPERTY_QUEUE_TIME)
  private Integer queueTime;

  public static final String JSON_PROPERTY_RESULT = "result";
  @JsonProperty(JSON_PROPERTY_RESULT)
  private String result;

  public static final String JSON_PROPERTY_USER_AGENT = "user_agent";
  @JsonProperty(JSON_PROPERTY_USER_AGENT)
  private String userAgent;

  public static final String JSON_PROPERTY_USERNAME = "username";
  @JsonProperty(JSON_PROPERTY_USERNAME)
  private String username;

  public static final String JSON_PROPERTY_VERDICTS = "verdicts";
  @JsonProperty(JSON_PROPERTY_VERDICTS)
  private List<String> verdicts = null;

  public static final String JSON_PROPERTY_POST_PROCESSING = "post_processing";
  @JsonProperty(JSON_PROPERTY_POST_PROCESSING)
  private AnalysisResultProcessInfoPostProcessing postProcessing;

  public AnalysisResultProcessInfo blockedReason(String blockedReason) {
    this.blockedReason = blockedReason;
    return this;
  }

  /**
   * Provides the reason why the file is blocked (if so).
   * @return blockedReason
   **/
  @JsonProperty("blocked_reason")
  @ApiModelProperty(example = "Sensitive Data Found", value = "Provides the reason why the file is blocked (if so).")
  
  public String getBlockedReason() {
    return blockedReason;
  }

  public void setBlockedReason(String blockedReason) {
    this.blockedReason = blockedReason;
  }

  public AnalysisResultProcessInfo fileTypeSkippedScan(Boolean fileTypeSkippedScan) {
    this.fileTypeSkippedScan = fileTypeSkippedScan;
    return this;
  }

  /**
   * Indicates if the input file&#39;s detected type was configured to skip scanning.
   * @return fileTypeSkippedScan
   **/
  @JsonProperty("file_type_skipped_scan")
  @ApiModelProperty(example = "false", value = "Indicates if the input file's detected type was configured to skip scanning.")
  
  public Boolean getFileTypeSkippedScan() {
    return fileTypeSkippedScan;
  }

  public void setFileTypeSkippedScan(Boolean fileTypeSkippedScan) {
    this.fileTypeSkippedScan = fileTypeSkippedScan;
  }

  public AnalysisResultProcessInfo outdatedData(List<OutdatedDataEnum> outdatedData) {
    this.outdatedData = outdatedData;
    return this;
  }

  public AnalysisResultProcessInfo addOutdatedDataItem(OutdatedDataEnum outdatedDataItem) {
    if (this.outdatedData == null) {
      this.outdatedData = new ArrayList<OutdatedDataEnum>();
    }
    this.outdatedData.add(outdatedDataItem);
    return this;
  }

  /**
   * array of flags - if occur - describing outdated data in the result, these can be   * enginedefinitions: at least one of the AV engines the item was scanned with has a newer definition database   * configuration: the process&#39; rule - or any item used by the rule - was modified since the item was processed   * sanitization: if item was sanitized this flag notifies that the sanitization information regarding this result is outdated, meaning the sanitized item is no longer available               
   * @return outdatedData
   **/
  @JsonProperty("outdated_data")
  @ApiModelProperty(example = "[enginedefinition, configuration, sanitization]", value = "array of flags - if occur - describing outdated data in the result, these can be   * enginedefinitions: at least one of the AV engines the item was scanned with has a newer definition database   * configuration: the process' rule - or any item used by the rule - was modified since the item was processed   * sanitization: if item was sanitized this flag notifies that the sanitization information regarding this result is outdated, meaning the sanitized item is no longer available               ")
  
  public List<OutdatedDataEnum> getOutdatedData() {
    return outdatedData;
  }

  public void setOutdatedData(List<OutdatedDataEnum> outdatedData) {
    this.outdatedData = outdatedData;
  }

  public AnalysisResultProcessInfo processingTime(Integer processingTime) {
    this.processingTime = processingTime;
    return this;
  }

  /**
   * Total time elapsed during processing file on the node (in milliseconds).
   * @return processingTime
   **/
  @JsonProperty("processing_time")
  @ApiModelProperty(example = "4804", value = "Total time elapsed during processing file on the node (in milliseconds).")
  
  public Integer getProcessingTime() {
    return processingTime;
  }

  public void setProcessingTime(Integer processingTime) {
    this.processingTime = processingTime;
  }

  public AnalysisResultProcessInfo profile(String profile) {
    this.profile = profile;
    return this;
  }

  /**
   * The used rule name.
   * @return profile
   **/
  @JsonProperty("profile")
  @ApiModelProperty(example = "File process", value = "The used rule name.")
  
  public String getProfile() {
    return profile;
  }

  public void setProfile(String profile) {
    this.profile = profile;
  }

  public AnalysisResultProcessInfo progressPercentage(Integer progressPercentage) {
    this.progressPercentage = progressPercentage;
    return this;
  }

  /**
   * Percentage of processing completed (from 1-100).
   * @return progressPercentage
   **/
  @JsonProperty("progress_percentage")
  @ApiModelProperty(example = "100", value = "Percentage of processing completed (from 1-100).")
  
  public Integer getProgressPercentage() {
    return progressPercentage;
  }

  public void setProgressPercentage(Integer progressPercentage) {
    this.progressPercentage = progressPercentage;
  }

  public AnalysisResultProcessInfo queueTime(Integer queueTime) {
    this.queueTime = queueTime;
    return this;
  }

  /**
   * Total time elapsed while the file waits in the queue (in milliseconds).
   * @return queueTime
   **/
  @JsonProperty("queue_time")
  @ApiModelProperty(example = "321", value = "Total time elapsed while the file waits in the queue (in milliseconds).")
  
  public Integer getQueueTime() {
    return queueTime;
  }

  public void setQueueTime(Integer queueTime) {
    this.queueTime = queueTime;
  }

  public AnalysisResultProcessInfo result(String result) {
    this.result = result;
    return this;
  }

  /**
   * The final result of processing the file (Allowed / Blocked / Processing).
   * @return result
   **/
  @JsonProperty("result")
  @ApiModelProperty(example = "Blocked", value = "The final result of processing the file (Allowed / Blocked / Processing).")
  
  public String getResult() {
    return result;
  }

  public void setResult(String result) {
    this.result = result;
  }

  public AnalysisResultProcessInfo userAgent(String userAgent) {
    this.userAgent = userAgent;
    return this;
  }

  /**
   * Identifier for the REST Client that calls the API.
   * @return userAgent
   **/
  @JsonProperty("user_agent")
  @ApiModelProperty(example = "webscan", value = "Identifier for the REST Client that calls the API.")
  
  public String getUserAgent() {
    return userAgent;
  }

  public void setUserAgent(String userAgent) {
    this.userAgent = userAgent;
  }

  public AnalysisResultProcessInfo username(String username) {
    this.username = username;
    return this;
  }

  /**
   * User identifier who submitted scan request earlier.
   * @return username
   **/
  @JsonProperty("username")
  @ApiModelProperty(example = "LOCAL/admin", value = "User identifier who submitted scan request earlier.")
  
  public String getUsername() {
    return username;
  }

  public void setUsername(String username) {
    this.username = username;
  }

  public AnalysisResultProcessInfo verdicts(List<String> verdicts) {
    this.verdicts = verdicts;
    return this;
  }

  public AnalysisResultProcessInfo addVerdictsItem(String verdictsItem) {
    if (this.verdicts == null) {
      this.verdicts = new ArrayList<String>();
    }
    this.verdicts.add(verdictsItem);
    return this;
  }

  /**
   * Aggregated list of potential issues.
   * @return verdicts
   **/
  @JsonProperty("verdicts")
  @ApiModelProperty(example = "[Sensitive Data Found]", value = "Aggregated list of potential issues.")
  
  public List<String> getVerdicts() {
    return verdicts;
  }

  public void setVerdicts(List<String> verdicts) {
    this.verdicts = verdicts;
  }

  public AnalysisResultProcessInfo postProcessing(AnalysisResultProcessInfoPostProcessing postProcessing) {
    this.postProcessing = postProcessing;
    return this;
  }

  /**
   * Get postProcessing
   * @return postProcessing
   **/
  @JsonProperty("post_processing")
  @ApiModelProperty(value = "")
  @Valid 
  public AnalysisResultProcessInfoPostProcessing getPostProcessing() {
    return postProcessing;
  }

  public void setPostProcessing(AnalysisResultProcessInfoPostProcessing postProcessing) {
    this.postProcessing = postProcessing;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnalysisResultProcessInfo analysisResultProcessInfo = (AnalysisResultProcessInfo) o;
    return Objects.equals(this.blockedReason, analysisResultProcessInfo.blockedReason) &&
        Objects.equals(this.fileTypeSkippedScan, analysisResultProcessInfo.fileTypeSkippedScan) &&
        Objects.equals(this.outdatedData, analysisResultProcessInfo.outdatedData) &&
        Objects.equals(this.processingTime, analysisResultProcessInfo.processingTime) &&
        Objects.equals(this.profile, analysisResultProcessInfo.profile) &&
        Objects.equals(this.progressPercentage, analysisResultProcessInfo.progressPercentage) &&
        Objects.equals(this.queueTime, analysisResultProcessInfo.queueTime) &&
        Objects.equals(this.result, analysisResultProcessInfo.result) &&
        Objects.equals(this.userAgent, analysisResultProcessInfo.userAgent) &&
        Objects.equals(this.username, analysisResultProcessInfo.username) &&
        Objects.equals(this.verdicts, analysisResultProcessInfo.verdicts) &&
        Objects.equals(this.postProcessing, analysisResultProcessInfo.postProcessing);
  }

  @Override
  public int hashCode() {
    return Objects.hash(blockedReason, fileTypeSkippedScan, outdatedData, processingTime, profile, progressPercentage, queueTime, result, userAgent, username, verdicts, postProcessing);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnalysisResultProcessInfo {\n");
    
    sb.append("    blockedReason: ").append(toIndentedString(blockedReason)).append("\n");
    sb.append("    fileTypeSkippedScan: ").append(toIndentedString(fileTypeSkippedScan)).append("\n");
    sb.append("    outdatedData: ").append(toIndentedString(outdatedData)).append("\n");
    sb.append("    processingTime: ").append(toIndentedString(processingTime)).append("\n");
    sb.append("    profile: ").append(toIndentedString(profile)).append("\n");
    sb.append("    progressPercentage: ").append(toIndentedString(progressPercentage)).append("\n");
    sb.append("    queueTime: ").append(toIndentedString(queueTime)).append("\n");
    sb.append("    result: ").append(toIndentedString(result)).append("\n");
    sb.append("    userAgent: ").append(toIndentedString(userAgent)).append("\n");
    sb.append("    username: ").append(toIndentedString(username)).append("\n");
    sb.append("    verdicts: ").append(toIndentedString(verdicts)).append("\n");
    sb.append("    postProcessing: ").append(toIndentedString(postProcessing)).append("\n");
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

