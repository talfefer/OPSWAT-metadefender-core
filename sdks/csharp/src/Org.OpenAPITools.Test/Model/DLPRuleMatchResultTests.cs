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
    ///  Class for testing DLPRuleMatchResult
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the model.
    /// </remarks>
    public class DLPRuleMatchResultTests
    {
        // TODO uncomment below to declare an instance variable for DLPRuleMatchResult
        //private DLPRuleMatchResult instance;

        /// <summary>
        /// Setup before each test
        /// </summary>
        [SetUp]
        public void Init()
        {
            // TODO uncomment below to create an instance of DLPRuleMatchResult
            //instance = new DLPRuleMatchResult();
        }

        /// <summary>
        /// Clean up after each test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of DLPRuleMatchResult
        /// </summary>
        [Test]
        public void DLPRuleMatchResultInstanceTest()
        {
            // TODO uncomment below to test "IsInstanceOf" DLPRuleMatchResult
            //Assert.IsInstanceOf(typeof(DLPRuleMatchResult), instance);
        }


        /// <summary>
        /// Test the property 'After'
        /// </summary>
        [Test]
        public void AfterTest()
        {
            // TODO unit test for the property 'After'
        }
        /// <summary>
        /// Test the property 'Before'
        /// </summary>
        [Test]
        public void BeforeTest()
        {
            // TODO unit test for the property 'Before'
        }
        /// <summary>
        /// Test the property 'Certainty'
        /// </summary>
        [Test]
        public void CertaintyTest()
        {
            // TODO unit test for the property 'Certainty'
        }
        /// <summary>
        /// Test the property 'CertaintyScore'
        /// </summary>
        [Test]
        public void CertaintyScoreTest()
        {
            // TODO unit test for the property 'CertaintyScore'
        }
        /// <summary>
        /// Test the property 'Hit'
        /// </summary>
        [Test]
        public void HitTest()
        {
            // TODO unit test for the property 'Hit'
        }
        /// <summary>
        /// Test the property 'IsRedacted'
        /// </summary>
        [Test]
        public void IsRedactedTest()
        {
            // TODO unit test for the property 'IsRedacted'
        }
        /// <summary>
        /// Test the property 'Severity'
        /// </summary>
        [Test]
        public void SeverityTest()
        {
            // TODO unit test for the property 'Severity'
        }

    }

}
