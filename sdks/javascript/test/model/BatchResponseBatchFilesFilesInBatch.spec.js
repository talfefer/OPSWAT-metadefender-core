/**
 * MetaDefender Core
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.MetaDefenderCore);
  }
}(this, function(expect, MetaDefenderCore) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('BatchResponseBatchFilesFilesInBatch', function() {
    it('should create an instance of BatchResponseBatchFilesFilesInBatch', function() {
      // uncomment below and update the code to test BatchResponseBatchFilesFilesInBatch
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be.a(MetaDefenderCore.BatchResponseBatchFilesFilesInBatch);
    });

    it('should have the property dataId (base name: "data_id")', function() {
      // uncomment below and update the code to test the property dataId
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property detectedBy (base name: "detected_by")', function() {
      // uncomment below and update the code to test the property detectedBy
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property displayName (base name: "display_name")', function() {
      // uncomment below and update the code to test the property displayName
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property fileSize (base name: "file_size")', function() {
      // uncomment below and update the code to test the property fileSize
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property fileType (base name: "file_type")', function() {
      // uncomment below and update the code to test the property fileType
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property fileTypeDescription (base name: "file_type_description")', function() {
      // uncomment below and update the code to test the property fileTypeDescription
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property processInfo (base name: "process_info")', function() {
      // uncomment below and update the code to test the property processInfo
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property progressPercentage (base name: "progress_percentage")', function() {
      // uncomment below and update the code to test the property progressPercentage
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property scanAllResultA (base name: "scan_all_result_a")', function() {
      // uncomment below and update the code to test the property scanAllResultA
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property scanAllResultI (base name: "scan_all_result_i")', function() {
      // uncomment below and update the code to test the property scanAllResultI
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

    it('should have the property scannedWith (base name: "scanned_with")', function() {
      // uncomment below and update the code to test the property scannedWith
      //var instane = new MetaDefenderCore.BatchResponseBatchFilesFilesInBatch();
      //expect(instance).to.be();
    });

  });

}));
