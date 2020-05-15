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
    /// | scan_result_a                | scan_result_i | |- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -|- -- -- -- -- -- -- --| | No Threat Detected           | 0             | | Infected                     | 1             | | Suspicious                   | 2             | | Failed                       | 3             | | Cleaned / Deleted            | 4             | | Scan Skipped - Whitelisted   | 7             | | Scan Skipped - Blacklisted   | 8             | | Exceeded Archive Depth       | 9             | | Not Scanned                  | 10            | | Encrypted Archive            | 12            | | Exceeded Archive Size        | 13            | | Exceeded Archive File Number | 14            | | Password Protected Document  | 15            | | Exceeded Archive Timeout     | 16            | | File type Mismatch           | 17            | | Potentially Vulnerable File  | 18            | | Canceled                     | 19            | | Sensitive data found         | 20            | | Yara Rule Matched            | 21            | | Potentially Unwanted Program | 22            | | Unsupported file type        | 23            | | In Progress                  | 255           | 
    /// </summary>
    /// <value>| scan_result_a                | scan_result_i | |- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -|- -- -- -- -- -- -- --| | No Threat Detected           | 0             | | Infected                     | 1             | | Suspicious                   | 2             | | Failed                       | 3             | | Cleaned / Deleted            | 4             | | Scan Skipped - Whitelisted   | 7             | | Scan Skipped - Blacklisted   | 8             | | Exceeded Archive Depth       | 9             | | Not Scanned                  | 10            | | Encrypted Archive            | 12            | | Exceeded Archive Size        | 13            | | Exceeded Archive File Number | 14            | | Password Protected Document  | 15            | | Exceeded Archive Timeout     | 16            | | File type Mismatch           | 17            | | Potentially Vulnerable File  | 18            | | Canceled                     | 19            | | Sensitive data found         | 20            | | Yara Rule Matched            | 21            | | Potentially Unwanted Program | 22            | | Unsupported file type        | 23            | | In Progress                  | 255           | </value>
    
    [JsonConverter(typeof(StringEnumConverter))]
    
    public enum ProcessingResultsStringEnum
    {
        /// <summary>
        /// Enum ThreatDetected for value: Threat Detected
        /// </summary>
        [EnumMember(Value = "Threat Detected")]
        ThreatDetected = 1,

        /// <summary>
        /// Enum Infected for value: Infected
        /// </summary>
        [EnumMember(Value = "Infected")]
        Infected = 2,

        /// <summary>
        /// Enum Suspicious for value: Suspicious
        /// </summary>
        [EnumMember(Value = "Suspicious")]
        Suspicious = 3,

        /// <summary>
        /// Enum Failed for value: Failed
        /// </summary>
        [EnumMember(Value = "Failed")]
        Failed = 4,

        /// <summary>
        /// Enum CleanedDeleted for value: Cleaned / Deleted
        /// </summary>
        [EnumMember(Value = "Cleaned / Deleted")]
        CleanedDeleted = 5,

        /// <summary>
        /// Enum ScanSkippedWhitelisted for value: Scan Skipped - Whitelisted
        /// </summary>
        [EnumMember(Value = "Scan Skipped - Whitelisted")]
        ScanSkippedWhitelisted = 6,

        /// <summary>
        /// Enum ScanSkippedBlacklisted for value: Scan Skipped - Blacklisted
        /// </summary>
        [EnumMember(Value = "Scan Skipped - Blacklisted")]
        ScanSkippedBlacklisted = 7,

        /// <summary>
        /// Enum ExceededArchiveDepth for value: Exceeded Archive Depth
        /// </summary>
        [EnumMember(Value = "Exceeded Archive Depth")]
        ExceededArchiveDepth = 8,

        /// <summary>
        /// Enum NotScanned for value: Not Scanned
        /// </summary>
        [EnumMember(Value = "Not Scanned")]
        NotScanned = 9,

        /// <summary>
        /// Enum EncryptedArchive for value: Encrypted Archive
        /// </summary>
        [EnumMember(Value = "Encrypted Archive")]
        EncryptedArchive = 10,

        /// <summary>
        /// Enum ExceededArchiveSize for value: Exceeded Archive Size
        /// </summary>
        [EnumMember(Value = "Exceeded Archive Size")]
        ExceededArchiveSize = 11,

        /// <summary>
        /// Enum ExceededArchiveFileNumber for value: Exceeded Archive File Number
        /// </summary>
        [EnumMember(Value = "Exceeded Archive File Number")]
        ExceededArchiveFileNumber = 12,

        /// <summary>
        /// Enum PasswordProtectedDocument for value: Password Protected Document
        /// </summary>
        [EnumMember(Value = "Password Protected Document")]
        PasswordProtectedDocument = 13,

        /// <summary>
        /// Enum ExceededArchiveTimeout for value: Exceeded Archive Timeout
        /// </summary>
        [EnumMember(Value = "Exceeded Archive Timeout")]
        ExceededArchiveTimeout = 14,

        /// <summary>
        /// Enum FiletypeMismatch for value: File type Mismatch
        /// </summary>
        [EnumMember(Value = "File type Mismatch")]
        FiletypeMismatch = 15,

        /// <summary>
        /// Enum PotentiallyVulnerableFile for value: Potentially Vulnerable File
        /// </summary>
        [EnumMember(Value = "Potentially Vulnerable File")]
        PotentiallyVulnerableFile = 16,

        /// <summary>
        /// Enum Canceled for value: Canceled
        /// </summary>
        [EnumMember(Value = "Canceled")]
        Canceled = 17,

        /// <summary>
        /// Enum Sensitivedatafound for value: Sensitive data found
        /// </summary>
        [EnumMember(Value = "Sensitive data found")]
        Sensitivedatafound = 18,

        /// <summary>
        /// Enum YaraRuleMatched for value: Yara Rule Matched
        /// </summary>
        [EnumMember(Value = "Yara Rule Matched")]
        YaraRuleMatched = 19,

        /// <summary>
        /// Enum PotentiallyUnwantedProgram for value: Potentially Unwanted Program
        /// </summary>
        [EnumMember(Value = "Potentially Unwanted Program")]
        PotentiallyUnwantedProgram = 20,

        /// <summary>
        /// Enum Unsupportedfiletype for value: Unsupported file type
        /// </summary>
        [EnumMember(Value = "Unsupported file type")]
        Unsupportedfiletype = 21,

        /// <summary>
        /// Enum InProgress for value: In Progress
        /// </summary>
        [EnumMember(Value = "In Progress")]
        InProgress = 22

    }

}
