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
    /// API object for /admin/config/session
    /// </summary>
    [DataContract]
    public partial class AdminConfigSession :  IEquatable<AdminConfigSession>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="AdminConfigSession" /> class.
        /// </summary>
        /// <param name="absoluteSessionTimeout">The interval (in milliseconds) for overall session length timeout (regardless of activity)..</param>
        /// <param name="allowCrossIpSessions">Allow requests from the same user to come from different IPs..</param>
        /// <param name="allowDuplicateSession">Allow same user to have multiple active sessions..</param>
        /// <param name="sessionTimeout">The interval (in milliseconds) for the user&#39;s session timeout, based on last activity. Timer starts after the last activity for the apikey..</param>
        public AdminConfigSession(int absoluteSessionTimeout = default(int), bool allowCrossIpSessions = default(bool), bool allowDuplicateSession = default(bool), int sessionTimeout = default(int))
        {
            this.AbsoluteSessionTimeout = absoluteSessionTimeout;
            this.AllowCrossIpSessions = allowCrossIpSessions;
            this.AllowDuplicateSession = allowDuplicateSession;
            this.SessionTimeout = sessionTimeout;
        }
        
        /// <summary>
        /// The interval (in milliseconds) for overall session length timeout (regardless of activity).
        /// </summary>
        /// <value>The interval (in milliseconds) for overall session length timeout (regardless of activity).</value>
        [DataMember(Name="absoluteSessionTimeout", EmitDefaultValue=false)]
        public int AbsoluteSessionTimeout { get; set; }

        /// <summary>
        /// Allow requests from the same user to come from different IPs.
        /// </summary>
        /// <value>Allow requests from the same user to come from different IPs.</value>
        [DataMember(Name="allowCrossIpSessions", EmitDefaultValue=false)]
        public bool AllowCrossIpSessions { get; set; }

        /// <summary>
        /// Allow same user to have multiple active sessions.
        /// </summary>
        /// <value>Allow same user to have multiple active sessions.</value>
        [DataMember(Name="allowDuplicateSession", EmitDefaultValue=false)]
        public bool AllowDuplicateSession { get; set; }

        /// <summary>
        /// The interval (in milliseconds) for the user&#39;s session timeout, based on last activity. Timer starts after the last activity for the apikey.
        /// </summary>
        /// <value>The interval (in milliseconds) for the user&#39;s session timeout, based on last activity. Timer starts after the last activity for the apikey.</value>
        [DataMember(Name="sessionTimeout", EmitDefaultValue=false)]
        public int SessionTimeout { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class AdminConfigSession {\n");
            sb.Append("  AbsoluteSessionTimeout: ").Append(AbsoluteSessionTimeout).Append("\n");
            sb.Append("  AllowCrossIpSessions: ").Append(AllowCrossIpSessions).Append("\n");
            sb.Append("  AllowDuplicateSession: ").Append(AllowDuplicateSession).Append("\n");
            sb.Append("  SessionTimeout: ").Append(SessionTimeout).Append("\n");
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
            return this.Equals(input as AdminConfigSession);
        }

        /// <summary>
        /// Returns true if AdminConfigSession instances are equal
        /// </summary>
        /// <param name="input">Instance of AdminConfigSession to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(AdminConfigSession input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.AbsoluteSessionTimeout == input.AbsoluteSessionTimeout ||
                    (this.AbsoluteSessionTimeout != null &&
                    this.AbsoluteSessionTimeout.Equals(input.AbsoluteSessionTimeout))
                ) && 
                (
                    this.AllowCrossIpSessions == input.AllowCrossIpSessions ||
                    (this.AllowCrossIpSessions != null &&
                    this.AllowCrossIpSessions.Equals(input.AllowCrossIpSessions))
                ) && 
                (
                    this.AllowDuplicateSession == input.AllowDuplicateSession ||
                    (this.AllowDuplicateSession != null &&
                    this.AllowDuplicateSession.Equals(input.AllowDuplicateSession))
                ) && 
                (
                    this.SessionTimeout == input.SessionTimeout ||
                    (this.SessionTimeout != null &&
                    this.SessionTimeout.Equals(input.SessionTimeout))
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
                if (this.AbsoluteSessionTimeout != null)
                    hashCode = hashCode * 59 + this.AbsoluteSessionTimeout.GetHashCode();
                if (this.AllowCrossIpSessions != null)
                    hashCode = hashCode * 59 + this.AllowCrossIpSessions.GetHashCode();
                if (this.AllowDuplicateSession != null)
                    hashCode = hashCode * 59 + this.AllowDuplicateSession.GetHashCode();
                if (this.SessionTimeout != null)
                    hashCode = hashCode * 59 + this.SessionTimeout.GetHashCode();
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
