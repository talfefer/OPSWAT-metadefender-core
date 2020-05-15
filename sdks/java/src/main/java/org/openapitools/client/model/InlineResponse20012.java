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

/**
 * InlineResponse20012
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-05-15T23:48:50.618888Z[UTC]")
public class InlineResponse20012 {
  public static final String SERIALIZED_NAME_ACTIVE = "active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_DEF_TIME = "def_time";
  @SerializedName(SERIALIZED_NAME_DEF_TIME)
  private String defTime;

  public static final String SERIALIZED_NAME_DOWNLOAD_PROGRESS = "download_progress";
  @SerializedName(SERIALIZED_NAME_DOWNLOAD_PROGRESS)
  private Integer downloadProgress;

  public static final String SERIALIZED_NAME_DOWNLOAD_TIME = "download_time";
  @SerializedName(SERIALIZED_NAME_DOWNLOAD_TIME)
  private String downloadTime;

  public static final String SERIALIZED_NAME_ENG_ID = "eng_id";
  @SerializedName(SERIALIZED_NAME_ENG_ID)
  private String engId;

  public static final String SERIALIZED_NAME_ENG_NAME = "eng_name";
  @SerializedName(SERIALIZED_NAME_ENG_NAME)
  private String engName;

  public static final String SERIALIZED_NAME_ENG_TYPE = "eng_type";
  @SerializedName(SERIALIZED_NAME_ENG_TYPE)
  private String engType;

  public static final String SERIALIZED_NAME_ENG_VER = "eng_ver";
  @SerializedName(SERIALIZED_NAME_ENG_VER)
  private String engVer;

  /**
   * Engine&#39;s type:    * av   * archive   * filetype 
   */
  @JsonAdapter(EngineTypeEnum.Adapter.class)
  public enum EngineTypeEnum {
    AV("av"),
    
    ARCHIVE("archive"),
    
    FILETYPE("filetype");

    private String value;

    EngineTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EngineTypeEnum fromValue(String value) {
      for (EngineTypeEnum b : EngineTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EngineTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EngineTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EngineTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EngineTypeEnum.fromValue(value);
      }
    }
  }

  public static final String SERIALIZED_NAME_ENGINE_TYPE = "engine_type";
  @SerializedName(SERIALIZED_NAME_ENGINE_TYPE)
  private EngineTypeEnum engineType;

  /**
   * Status of the engine:   * downloading   * downloaded   * staging   * production   * removed   * temporary failed   * permanently failed   * content invalid   * download failed 
   */
  @JsonAdapter(StateEnum.Adapter.class)
  public enum StateEnum {
    DOWNLOADING("downloading"),
    
    DOWNLOADED("downloaded"),
    
    STAGING("staging"),
    
    PRODUCTION("production"),
    
    REMOVED("removed"),
    
    TEMPORARY_FAILED("temporary failed"),
    
    PERMANENTLY_FAILED("permanently failed"),
    
    CONTENT_INVALID("content invalid"),
    
    DOWNLOAD_FAILED("download failed");

    private String value;

    StateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StateEnum fromValue(String value) {
      for (StateEnum b : StateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StateEnum.fromValue(value);
      }
    }
  }

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private StateEnum state;


  public InlineResponse20012 active(Boolean active) {
    
    this.active = active;
    return this;
  }

   /**
   * If used by at least one engine
   * @return active
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "true", value = "If used by at least one engine")

  public Boolean getActive() {
    return active;
  }


  public void setActive(Boolean active) {
    this.active = active;
  }


  public InlineResponse20012 defTime(String defTime) {
    
    this.defTime = defTime;
    return this;
  }

   /**
   * The database definition time for this engine
   * @return defTime
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "2020-04-17T02:37:05.000Z", value = "The database definition time for this engine")

  public String getDefTime() {
    return defTime;
  }


  public void setDefTime(String defTime) {
    this.defTime = defTime;
  }


  public InlineResponse20012 downloadProgress(Integer downloadProgress) {
    
    this.downloadProgress = downloadProgress;
    return this;
  }

   /**
   * The percentage progress of download
   * @return downloadProgress
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "100", value = "The percentage progress of download")

  public Integer getDownloadProgress() {
    return downloadProgress;
  }


  public void setDownloadProgress(Integer downloadProgress) {
    this.downloadProgress = downloadProgress;
  }


  public InlineResponse20012 downloadTime(String downloadTime) {
    
    this.downloadTime = downloadTime;
    return this;
  }

   /**
   * When this engine downloaded from the update server.
   * @return downloadTime
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "2020-04-17T08:17:22.810Z", value = "When this engine downloaded from the update server.")

  public String getDownloadTime() {
    return downloadTime;
  }


  public void setDownloadTime(String downloadTime) {
    this.downloadTime = downloadTime;
  }


  public InlineResponse20012 engId(String engId) {
    
    this.engId = engId;
    return this;
  }

   /**
   * Engine internal ID
   * @return engId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "clamav_1_linux", value = "Engine internal ID")

  public String getEngId() {
    return engId;
  }


  public void setEngId(String engId) {
    this.engId = engId;
  }


  public InlineResponse20012 engName(String engName) {
    
    this.engName = engName;
    return this;
  }

   /**
   * Engine name
   * @return engName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "ClamAV", value = "Engine name")

  public String getEngName() {
    return engName;
  }


  public void setEngName(String engName) {
    this.engName = engName;
  }


  public InlineResponse20012 engType(String engType) {
    
    this.engType = engType;
    return this;
  }

   /**
   * Engine type in human readable form
   * @return engType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "Bundled engine", value = "Engine type in human readable form")

  public String getEngType() {
    return engType;
  }


  public void setEngType(String engType) {
    this.engType = engType;
  }


  public InlineResponse20012 engVer(String engVer) {
    
    this.engVer = engVer;
    return this;
  }

   /**
   * Engine&#39;s version (format differs from one engine to another).
   * @return engVer
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "3.0-43", value = "Engine's version (format differs from one engine to another).")

  public String getEngVer() {
    return engVer;
  }


  public void setEngVer(String engVer) {
    this.engVer = engVer;
  }


  public InlineResponse20012 engineType(EngineTypeEnum engineType) {
    
    this.engineType = engineType;
    return this;
  }

   /**
   * Engine&#39;s type:    * av   * archive   * filetype 
   * @return engineType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "av", value = "Engine's type:    * av   * archive   * filetype ")

  public EngineTypeEnum getEngineType() {
    return engineType;
  }


  public void setEngineType(EngineTypeEnum engineType) {
    this.engineType = engineType;
  }


  public InlineResponse20012 state(StateEnum state) {
    
    this.state = state;
    return this;
  }

   /**
   * Status of the engine:   * downloading   * downloaded   * staging   * production   * removed   * temporary failed   * permanently failed   * content invalid   * download failed 
   * @return state
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "production", value = "Status of the engine:   * downloading   * downloaded   * staging   * production   * removed   * temporary failed   * permanently failed   * content invalid   * download failed ")

  public StateEnum getState() {
    return state;
  }


  public void setState(StateEnum state) {
    this.state = state;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InlineResponse20012 inlineResponse20012 = (InlineResponse20012) o;
    return Objects.equals(this.active, inlineResponse20012.active) &&
        Objects.equals(this.defTime, inlineResponse20012.defTime) &&
        Objects.equals(this.downloadProgress, inlineResponse20012.downloadProgress) &&
        Objects.equals(this.downloadTime, inlineResponse20012.downloadTime) &&
        Objects.equals(this.engId, inlineResponse20012.engId) &&
        Objects.equals(this.engName, inlineResponse20012.engName) &&
        Objects.equals(this.engType, inlineResponse20012.engType) &&
        Objects.equals(this.engVer, inlineResponse20012.engVer) &&
        Objects.equals(this.engineType, inlineResponse20012.engineType) &&
        Objects.equals(this.state, inlineResponse20012.state);
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, defTime, downloadProgress, downloadTime, engId, engName, engType, engVer, engineType, state);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InlineResponse20012 {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    defTime: ").append(toIndentedString(defTime)).append("\n");
    sb.append("    downloadProgress: ").append(toIndentedString(downloadProgress)).append("\n");
    sb.append("    downloadTime: ").append(toIndentedString(downloadTime)).append("\n");
    sb.append("    engId: ").append(toIndentedString(engId)).append("\n");
    sb.append("    engName: ").append(toIndentedString(engName)).append("\n");
    sb.append("    engType: ").append(toIndentedString(engType)).append("\n");
    sb.append("    engVer: ").append(toIndentedString(engVer)).append("\n");
    sb.append("    engineType: ").append(toIndentedString(engineType)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
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

