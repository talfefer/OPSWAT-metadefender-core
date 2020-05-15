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
 */

/*
 * OAIBatchResponse_scan_results.h
 *
 * Metascan analysis result.
 */

#ifndef OAIBatchResponse_scan_results_H
#define OAIBatchResponse_scan_results_H

#include <QJsonObject>

#include "OAIProcessingResultsIndexEnum.h"
#include "OAIProcessingResultsStringEnum.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBatchResponse_scan_results : public OAIObject {
public:
    OAIBatchResponse_scan_results();
    OAIBatchResponse_scan_results(QString json);
    ~OAIBatchResponse_scan_results() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBatchId() const;
    void setBatchId(const QString &batch_id);

    OAIProcessingResultsStringEnum getScanAllResultA() const;
    void setScanAllResultA(const OAIProcessingResultsStringEnum &scan_all_result_a);

    OAIProcessingResultsIndexEnum getScanAllResultI() const;
    void setScanAllResultI(const OAIProcessingResultsIndexEnum &scan_all_result_i);

    QString getStartTime() const;
    void setStartTime(const QString &start_time);

    qint32 getTotalAvs() const;
    void setTotalAvs(const qint32 &total_avs);

    qint32 getTotalTime() const;
    void setTotalTime(const qint32 &total_time);

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString batch_id;
    bool m_batch_id_isSet;
    bool m_batch_id_isValid;

    OAIProcessingResultsStringEnum scan_all_result_a;
    bool m_scan_all_result_a_isSet;
    bool m_scan_all_result_a_isValid;

    OAIProcessingResultsIndexEnum scan_all_result_i;
    bool m_scan_all_result_i_isSet;
    bool m_scan_all_result_i_isValid;

    QString start_time;
    bool m_start_time_isSet;
    bool m_start_time_isValid;

    qint32 total_avs;
    bool m_total_avs_isSet;
    bool m_total_avs_isValid;

    qint32 total_time;
    bool m_total_time_isSet;
    bool m_total_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBatchResponse_scan_results)

#endif // OAIBatchResponse_scan_results_H
