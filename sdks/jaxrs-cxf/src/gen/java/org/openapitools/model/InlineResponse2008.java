package org.openapitools.model;

import javax.validation.constraints.*;
import javax.validation.Valid;

import io.swagger.annotations.ApiModelProperty;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.XmlEnum;
import javax.xml.bind.annotation.XmlEnumValue;
import com.fasterxml.jackson.annotation.JsonProperty;

public class InlineResponse2008  {
  
  @ApiModelProperty(required = true, value = "")
  private String dataId;
 /**
   * Get dataId
   * @return dataId
  **/
  @JsonProperty("data_id")
  @NotNull
  public String getDataId() {
    return dataId;
  }

  public void setDataId(String dataId) {
    this.dataId = dataId;
  }

  public InlineResponse2008 dataId(String dataId) {
    this.dataId = dataId;
    return this;
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InlineResponse2008 {\n");
    
    sb.append("    dataId: ").append(toIndentedString(dataId)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private static String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

