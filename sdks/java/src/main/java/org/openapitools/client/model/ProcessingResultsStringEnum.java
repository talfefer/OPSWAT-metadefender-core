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
import io.swagger.annotations.ApiModel;
import com.google.gson.annotations.SerializedName;

import java.io.IOException;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

/**
 * | scan_result_a                | scan_result_i | |------------------------------|---------------| | No Threat Detected           | 0             | | Infected                     | 1             | | Suspicious                   | 2             | | Failed                       | 3             | | Cleaned / Deleted            | 4             | | Scan Skipped - Whitelisted   | 7             | | Scan Skipped - Blacklisted   | 8             | | Exceeded Archive Depth       | 9             | | Not Scanned                  | 10            | | Encrypted Archive            | 12            | | Exceeded Archive Size        | 13            | | Exceeded Archive File Number | 14            | | Password Protected Document  | 15            | | Exceeded Archive Timeout     | 16            | | File type Mismatch           | 17            | | Potentially Vulnerable File  | 18            | | Canceled                     | 19            | | Sensitive data found         | 20            | | Yara Rule Matched            | 21            | | Potentially Unwanted Program | 22            | | Unsupported file type        | 23            | | In Progress                  | 255           | 
 */
@JsonAdapter(ProcessingResultsStringEnum.Adapter.class)
public enum ProcessingResultsStringEnum {
  
  THREAT_DETECTED("Threat Detected"),
  
  INFECTED("Infected"),
  
  SUSPICIOUS("Suspicious"),
  
  FAILED("Failed"),
  
  CLEANED_DELETED("Cleaned / Deleted"),
  
  SCAN_SKIPPED_WHITELISTED("Scan Skipped - Whitelisted"),
  
  SCAN_SKIPPED_BLACKLISTED("Scan Skipped - Blacklisted"),
  
  EXCEEDED_ARCHIVE_DEPTH("Exceeded Archive Depth"),
  
  NOT_SCANNED("Not Scanned"),
  
  ENCRYPTED_ARCHIVE("Encrypted Archive"),
  
  EXCEEDED_ARCHIVE_SIZE("Exceeded Archive Size"),
  
  EXCEEDED_ARCHIVE_FILE_NUMBER("Exceeded Archive File Number"),
  
  PASSWORD_PROTECTED_DOCUMENT("Password Protected Document"),
  
  EXCEEDED_ARCHIVE_TIMEOUT("Exceeded Archive Timeout"),
  
  FILE_TYPE_MISMATCH("File type Mismatch"),
  
  POTENTIALLY_VULNERABLE_FILE("Potentially Vulnerable File"),
  
  CANCELED("Canceled"),
  
  SENSITIVE_DATA_FOUND("Sensitive data found"),
  
  YARA_RULE_MATCHED("Yara Rule Matched"),
  
  POTENTIALLY_UNWANTED_PROGRAM("Potentially Unwanted Program"),
  
  UNSUPPORTED_FILE_TYPE("Unsupported file type"),
  
  IN_PROGRESS("In Progress");

  private String value;

  ProcessingResultsStringEnum(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static ProcessingResultsStringEnum fromValue(String value) {
    for (ProcessingResultsStringEnum b : ProcessingResultsStringEnum.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<ProcessingResultsStringEnum> {
    @Override
    public void write(final JsonWriter jsonWriter, final ProcessingResultsStringEnum enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public ProcessingResultsStringEnum read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return ProcessingResultsStringEnum.fromValue(value);
    }
  }
}

