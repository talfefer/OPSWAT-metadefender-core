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
import org.openapitools.model.AdminConfigUpdateDisabledupdate;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import javax.validation.constraints.*;
import javax.validation.Valid;

/**
 * API object for /admin/config/update
 */
@ApiModel(description = "API object for /admin/config/update")
@JsonPropertyOrder({
  AdminConfigUpdate.JSON_PROPERTY_AUTOUPDATEPERIOD,
  AdminConfigUpdate.JSON_PROPERTY_DELETEAFTERIMPORT,
  AdminConfigUpdate.JSON_PROPERTY_DISABLEDUPDATE,
  AdminConfigUpdate.JSON_PROPERTY_PICKUPFOLDER,
  AdminConfigUpdate.JSON_PROPERTY_SOURCE
})
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaJerseyServerCodegen", date = "2020-05-15T23:49:49.064488Z[UTC]")
public class AdminConfigUpdate   {
  public static final String JSON_PROPERTY_AUTOUPDATEPERIOD = "autoupdateperiod";
  @JsonProperty(JSON_PROPERTY_AUTOUPDATEPERIOD)
  private Integer autoupdateperiod;

  public static final String JSON_PROPERTY_DELETEAFTERIMPORT = "deleteafterimport";
  @JsonProperty(JSON_PROPERTY_DELETEAFTERIMPORT)
  private Boolean deleteafterimport;

  public static final String JSON_PROPERTY_DISABLEDUPDATE = "disabledupdate";
  @JsonProperty(JSON_PROPERTY_DISABLEDUPDATE)
  private List<AdminConfigUpdateDisabledupdate> disabledupdate = null;

  public static final String JSON_PROPERTY_PICKUPFOLDER = "pickupfolder";
  @JsonProperty(JSON_PROPERTY_PICKUPFOLDER)
  private String pickupfolder;

  /**
   * Define where the updates will be loaded from. &lt;p&gt; This can be either:   * &#x60;internet&#x60; -&gt; if selected, will check for new updates every &#x60;autoupdateperiod&#x60; minutes   * &#x60;folder&#x60; -&gt; make sure that MetaDefender has access/permission to that folder   * &#x60;manual&#x60; -&gt; requires manually uploading the packages in Inventory &gt; Modules &gt; Upload package. 
   */
  public enum SourceEnum {
    INTERNET("internet"),
    
    FOLDER("folder"),
    
    MANUAL("manual");

    private String value;

    SourceEnum(String value) {
      this.value = value;
    }

    @Override
    @JsonValue
    public String toString() {
      return String.valueOf(value);
    }

    @JsonCreator
    public static SourceEnum fromValue(String value) {
      for (SourceEnum b : SourceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }
  }

  public static final String JSON_PROPERTY_SOURCE = "source";
  @JsonProperty(JSON_PROPERTY_SOURCE)
  private SourceEnum source;

  public AdminConfigUpdate autoupdateperiod(Integer autoupdateperiod) {
    this.autoupdateperiod = autoupdateperiod;
    return this;
  }

  /**
   * The interval (in minutes) for checking for new updates.
   * @return autoupdateperiod
   **/
  @JsonProperty("autoupdateperiod")
  @ApiModelProperty(example = "240", value = "The interval (in minutes) for checking for new updates.")
  
  public Integer getAutoupdateperiod() {
    return autoupdateperiod;
  }

  public void setAutoupdateperiod(Integer autoupdateperiod) {
    this.autoupdateperiod = autoupdateperiod;
  }

  public AdminConfigUpdate deleteafterimport(Boolean deleteafterimport) {
    this.deleteafterimport = deleteafterimport;
    return this;
  }

  /**
   * If you want to clean the pickup folder after the updates have been applied.
   * @return deleteafterimport
   **/
  @JsonProperty("deleteafterimport")
  @ApiModelProperty(example = "true", value = "If you want to clean the pickup folder after the updates have been applied.")
  
  public Boolean getDeleteafterimport() {
    return deleteafterimport;
  }

  public void setDeleteafterimport(Boolean deleteafterimport) {
    this.deleteafterimport = deleteafterimport;
  }

  public AdminConfigUpdate disabledupdate(List<AdminConfigUpdateDisabledupdate> disabledupdate) {
    this.disabledupdate = disabledupdate;
    return this;
  }

  public AdminConfigUpdate addDisabledupdateItem(AdminConfigUpdateDisabledupdate disabledupdateItem) {
    if (this.disabledupdate == null) {
      this.disabledupdate = new ArrayList<AdminConfigUpdateDisabledupdate>();
    }
    this.disabledupdate.add(disabledupdateItem);
    return this;
  }

  /**
   * Lockdown a time interval when the engines are not allowed to update.
   * @return disabledupdate
   **/
  @JsonProperty("disabledupdate")
  @ApiModelProperty(value = "Lockdown a time interval when the engines are not allowed to update.")
  @Valid 
  public List<AdminConfigUpdateDisabledupdate> getDisabledupdate() {
    return disabledupdate;
  }

  public void setDisabledupdate(List<AdminConfigUpdateDisabledupdate> disabledupdate) {
    this.disabledupdate = disabledupdate;
  }

  public AdminConfigUpdate pickupfolder(String pickupfolder) {
    this.pickupfolder = pickupfolder;
    return this;
  }

  /**
   * The folder where MetaDefender will look for the new engine files.
   * @return pickupfolder
   **/
  @JsonProperty("pickupfolder")
  @ApiModelProperty(example = "/tmp/core-data/update_autoadd", value = "The folder where MetaDefender will look for the new engine files.")
  
  public String getPickupfolder() {
    return pickupfolder;
  }

  public void setPickupfolder(String pickupfolder) {
    this.pickupfolder = pickupfolder;
  }

  public AdminConfigUpdate source(SourceEnum source) {
    this.source = source;
    return this;
  }

  /**
   * Define where the updates will be loaded from. &lt;p&gt; This can be either:   * &#x60;internet&#x60; -&gt; if selected, will check for new updates every &#x60;autoupdateperiod&#x60; minutes   * &#x60;folder&#x60; -&gt; make sure that MetaDefender has access/permission to that folder   * &#x60;manual&#x60; -&gt; requires manually uploading the packages in Inventory &gt; Modules &gt; Upload package. 
   * @return source
   **/
  @JsonProperty("source")
  @ApiModelProperty(example = "internet", value = "Define where the updates will be loaded from. <p> This can be either:   * `internet` -> if selected, will check for new updates every `autoupdateperiod` minutes   * `folder` -> make sure that MetaDefender has access/permission to that folder   * `manual` -> requires manually uploading the packages in Inventory > Modules > Upload package. ")
  
  public SourceEnum getSource() {
    return source;
  }

  public void setSource(SourceEnum source) {
    this.source = source;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdminConfigUpdate adminConfigUpdate = (AdminConfigUpdate) o;
    return Objects.equals(this.autoupdateperiod, adminConfigUpdate.autoupdateperiod) &&
        Objects.equals(this.deleteafterimport, adminConfigUpdate.deleteafterimport) &&
        Objects.equals(this.disabledupdate, adminConfigUpdate.disabledupdate) &&
        Objects.equals(this.pickupfolder, adminConfigUpdate.pickupfolder) &&
        Objects.equals(this.source, adminConfigUpdate.source);
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoupdateperiod, deleteafterimport, disabledupdate, pickupfolder, source);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdminConfigUpdate {\n");
    
    sb.append("    autoupdateperiod: ").append(toIndentedString(autoupdateperiod)).append("\n");
    sb.append("    deleteafterimport: ").append(toIndentedString(deleteafterimport)).append("\n");
    sb.append("    disabledupdate: ").append(toIndentedString(disabledupdate)).append("\n");
    sb.append("    pickupfolder: ").append(toIndentedString(pickupfolder)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
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

