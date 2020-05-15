/* 
 * MetaDefender Core
 *
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  - -- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   - -- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using NUnit.Framework;

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Model;
using Org.OpenAPITools.Client;
using System.Reflection;
using Newtonsoft.Json;

namespace Org.OpenAPITools.Test
{
    /// <summary>
    ///  Class for testing AnalysisResultProcessInfo
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the model.
    /// </remarks>
    public class AnalysisResultProcessInfoTests
    {
        // TODO uncomment below to declare an instance variable for AnalysisResultProcessInfo
        //private AnalysisResultProcessInfo instance;

        /// <summary>
        /// Setup before each test
        /// </summary>
        [SetUp]
        public void Init()
        {
            // TODO uncomment below to create an instance of AnalysisResultProcessInfo
            //instance = new AnalysisResultProcessInfo();
        }

        /// <summary>
        /// Clean up after each test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of AnalysisResultProcessInfo
        /// </summary>
        [Test]
        public void AnalysisResultProcessInfoInstanceTest()
        {
            // TODO uncomment below to test "IsInstanceOf" AnalysisResultProcessInfo
            //Assert.IsInstanceOf(typeof(AnalysisResultProcessInfo), instance);
        }


        /// <summary>
        /// Test the property 'BlockedReason'
        /// </summary>
        [Test]
        public void BlockedReasonTest()
        {
            // TODO unit test for the property 'BlockedReason'
        }
        /// <summary>
        /// Test the property 'FileTypeSkippedScan'
        /// </summary>
        [Test]
        public void FileTypeSkippedScanTest()
        {
            // TODO unit test for the property 'FileTypeSkippedScan'
        }
        /// <summary>
        /// Test the property 'OutdatedData'
        /// </summary>
        [Test]
        public void OutdatedDataTest()
        {
            // TODO unit test for the property 'OutdatedData'
        }
        /// <summary>
        /// Test the property 'ProcessingTime'
        /// </summary>
        [Test]
        public void ProcessingTimeTest()
        {
            // TODO unit test for the property 'ProcessingTime'
        }
        /// <summary>
        /// Test the property 'Profile'
        /// </summary>
        [Test]
        public void ProfileTest()
        {
            // TODO unit test for the property 'Profile'
        }
        /// <summary>
        /// Test the property 'ProgressPercentage'
        /// </summary>
        [Test]
        public void ProgressPercentageTest()
        {
            // TODO unit test for the property 'ProgressPercentage'
        }
        /// <summary>
        /// Test the property 'QueueTime'
        /// </summary>
        [Test]
        public void QueueTimeTest()
        {
            // TODO unit test for the property 'QueueTime'
        }
        /// <summary>
        /// Test the property 'Result'
        /// </summary>
        [Test]
        public void ResultTest()
        {
            // TODO unit test for the property 'Result'
        }
        /// <summary>
        /// Test the property 'UserAgent'
        /// </summary>
        [Test]
        public void UserAgentTest()
        {
            // TODO unit test for the property 'UserAgent'
        }
        /// <summary>
        /// Test the property 'Username'
        /// </summary>
        [Test]
        public void UsernameTest()
        {
            // TODO unit test for the property 'Username'
        }
        /// <summary>
        /// Test the property 'Verdicts'
        /// </summary>
        [Test]
        public void VerdictsTest()
        {
            // TODO unit test for the property 'Verdicts'
        }
        /// <summary>
        /// Test the property 'PostProcessing'
        /// </summary>
        [Test]
        public void PostProcessingTest()
        {
            // TODO unit test for the property 'PostProcessing'
        }

    }

}
