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
    /// Contains information about result of sanitization process and any action done after finalizing the process using Post Actions.
    /// </summary>
    [DataContract]
    public partial class AnalysisResultProcessInfoPostProcessing :  IEquatable<AnalysisResultProcessInfoPostProcessing>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="AnalysisResultProcessInfoPostProcessing" /> class.
        /// </summary>
        /// <param name="actionsFailed">Empty string if no action failed or list of failed actions, separated by \&quot;|\&quot;..</param>
        /// <param name="actionsRan">List of successful actions, separated by \&quot;|\&quot;. Empty string if otherwise..</param>
        /// <param name="convertedDestination">Contains the name of the sanitized file..</param>
        /// <param name="convertedTo">Contains target type name of sanitization..</param>
        /// <param name="copyMoveDestination">Contains target type name of sanitization..</param>
        /// <param name="sanitizationDetails">Contains target type name of sanitization..</param>
        public AnalysisResultProcessInfoPostProcessing(string actionsFailed = default(string), string actionsRan = default(string), string convertedDestination = default(string), string convertedTo = default(string), string copyMoveDestination = default(string), DeepCDRDetails sanitizationDetails = default(DeepCDRDetails))
        {
            this.ActionsFailed = actionsFailed;
            this.ActionsRan = actionsRan;
            this.ConvertedDestination = convertedDestination;
            this.ConvertedTo = convertedTo;
            this.CopyMoveDestination = copyMoveDestination;
            this.SanitizationDetails = sanitizationDetails;
        }
        
        /// <summary>
        /// Empty string if no action failed or list of failed actions, separated by \&quot;|\&quot;.
        /// </summary>
        /// <value>Empty string if no action failed or list of failed actions, separated by \&quot;|\&quot;.</value>
        [DataMember(Name="actions_failed", EmitDefaultValue=false)]
        public string ActionsFailed { get; set; }

        /// <summary>
        /// List of successful actions, separated by \&quot;|\&quot;. Empty string if otherwise.
        /// </summary>
        /// <value>List of successful actions, separated by \&quot;|\&quot;. Empty string if otherwise.</value>
        [DataMember(Name="actions_ran", EmitDefaultValue=false)]
        public string ActionsRan { get; set; }

        /// <summary>
        /// Contains the name of the sanitized file.
        /// </summary>
        /// <value>Contains the name of the sanitized file.</value>
        [DataMember(Name="converted_destination", EmitDefaultValue=false)]
        public string ConvertedDestination { get; set; }

        /// <summary>
        /// Contains target type name of sanitization.
        /// </summary>
        /// <value>Contains target type name of sanitization.</value>
        [DataMember(Name="converted_to", EmitDefaultValue=false)]
        public string ConvertedTo { get; set; }

        /// <summary>
        /// Contains target type name of sanitization.
        /// </summary>
        /// <value>Contains target type name of sanitization.</value>
        [DataMember(Name="copy_move_destination", EmitDefaultValue=false)]
        public string CopyMoveDestination { get; set; }

        /// <summary>
        /// Contains target type name of sanitization.
        /// </summary>
        /// <value>Contains target type name of sanitization.</value>
        [DataMember(Name="sanitization_details", EmitDefaultValue=false)]
        public DeepCDRDetails SanitizationDetails { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class AnalysisResultProcessInfoPostProcessing {\n");
            sb.Append("  ActionsFailed: ").Append(ActionsFailed).Append("\n");
            sb.Append("  ActionsRan: ").Append(ActionsRan).Append("\n");
            sb.Append("  ConvertedDestination: ").Append(ConvertedDestination).Append("\n");
            sb.Append("  ConvertedTo: ").Append(ConvertedTo).Append("\n");
            sb.Append("  CopyMoveDestination: ").Append(CopyMoveDestination).Append("\n");
            sb.Append("  SanitizationDetails: ").Append(SanitizationDetails).Append("\n");
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
            return this.Equals(input as AnalysisResultProcessInfoPostProcessing);
        }

        /// <summary>
        /// Returns true if AnalysisResultProcessInfoPostProcessing instances are equal
        /// </summary>
        /// <param name="input">Instance of AnalysisResultProcessInfoPostProcessing to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(AnalysisResultProcessInfoPostProcessing input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.ActionsFailed == input.ActionsFailed ||
                    (this.ActionsFailed != null &&
                    this.ActionsFailed.Equals(input.ActionsFailed))
                ) && 
                (
                    this.ActionsRan == input.ActionsRan ||
                    (this.ActionsRan != null &&
                    this.ActionsRan.Equals(input.ActionsRan))
                ) && 
                (
                    this.ConvertedDestination == input.ConvertedDestination ||
                    (this.ConvertedDestination != null &&
                    this.ConvertedDestination.Equals(input.ConvertedDestination))
                ) && 
                (
                    this.ConvertedTo == input.ConvertedTo ||
                    (this.ConvertedTo != null &&
                    this.ConvertedTo.Equals(input.ConvertedTo))
                ) && 
                (
                    this.CopyMoveDestination == input.CopyMoveDestination ||
                    (this.CopyMoveDestination != null &&
                    this.CopyMoveDestination.Equals(input.CopyMoveDestination))
                ) && 
                (
                    this.SanitizationDetails == input.SanitizationDetails ||
                    (this.SanitizationDetails != null &&
                    this.SanitizationDetails.Equals(input.SanitizationDetails))
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
                if (this.ActionsFailed != null)
                    hashCode = hashCode * 59 + this.ActionsFailed.GetHashCode();
                if (this.ActionsRan != null)
                    hashCode = hashCode * 59 + this.ActionsRan.GetHashCode();
                if (this.ConvertedDestination != null)
                    hashCode = hashCode * 59 + this.ConvertedDestination.GetHashCode();
                if (this.ConvertedTo != null)
                    hashCode = hashCode * 59 + this.ConvertedTo.GetHashCode();
                if (this.CopyMoveDestination != null)
                    hashCode = hashCode * 59 + this.CopyMoveDestination.GetHashCode();
                if (this.SanitizationDetails != null)
                    hashCode = hashCode * 59 + this.SanitizationDetails.GetHashCode();
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
