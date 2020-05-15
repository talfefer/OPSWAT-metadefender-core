/* 
 * MetaDefender Core
 *
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  - -- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   - -- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// Result of metadata removal.
    /// </summary>
    [DataContract]
    public partial class DLPResponseDlpInfoMetadataRemoval :  IEquatable<DLPResponseDlpInfoMetadataRemoval>, IValidatableObject
    {
        /// <summary>
        /// Result of the metadata removal process, possible values: * &#x60;removed&#x60; * &#x60;not removed&#x60; * &#x60;failed to remove&#x60; 
        /// </summary>
        /// <value>Result of the metadata removal process, possible values: * &#x60;removed&#x60; * &#x60;not removed&#x60; * &#x60;failed to remove&#x60; </value>
        [JsonConverter(typeof(StringEnumConverter))]
        public enum ResultEnum
        {
            /// <summary>
            /// Enum Removed for value: removed
            /// </summary>
            [EnumMember(Value = "removed")]
            Removed = 1,

            /// <summary>
            /// Enum Notremoved for value: not removed
            /// </summary>
            [EnumMember(Value = "not removed")]
            Notremoved = 2,

            /// <summary>
            /// Enum Failedtoremove for value: failed to remove
            /// </summary>
            [EnumMember(Value = "failed to remove")]
            Failedtoremove = 3

        }

        /// <summary>
        /// Result of the metadata removal process, possible values: * &#x60;removed&#x60; * &#x60;not removed&#x60; * &#x60;failed to remove&#x60; 
        /// </summary>
        /// <value>Result of the metadata removal process, possible values: * &#x60;removed&#x60; * &#x60;not removed&#x60; * &#x60;failed to remove&#x60; </value>
        [DataMember(Name="result", EmitDefaultValue=false)]
        public ResultEnum? Result { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="DLPResponseDlpInfoMetadataRemoval" /> class.
        /// </summary>
        /// <param name="result">Result of the metadata removal process, possible values: * &#x60;removed&#x60; * &#x60;not removed&#x60; * &#x60;failed to remove&#x60; .</param>
        public DLPResponseDlpInfoMetadataRemoval(ResultEnum? result = default(ResultEnum?))
        {
            this.Result = result;
        }
        

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DLPResponseDlpInfoMetadataRemoval {\n");
            sb.Append("  Result: ").Append(Result).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as DLPResponseDlpInfoMetadataRemoval);
        }

        /// <summary>
        /// Returns true if DLPResponseDlpInfoMetadataRemoval instances are equal
        /// </summary>
        /// <param name="input">Instance of DLPResponseDlpInfoMetadataRemoval to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DLPResponseDlpInfoMetadataRemoval input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Result == input.Result ||
                    (this.Result != null &&
                    this.Result.Equals(input.Result))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Result != null)
                    hashCode = hashCode * 59 + this.Result.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
