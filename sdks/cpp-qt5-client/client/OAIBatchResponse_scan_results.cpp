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

#include "OAIBatchResponse_scan_results.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBatchResponse_scan_results::OAIBatchResponse_scan_results(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBatchResponse_scan_results::OAIBatchResponse_scan_results() {
    this->initializeModel();
}

OAIBatchResponse_scan_results::~OAIBatchResponse_scan_results() {}

void OAIBatchResponse_scan_results::initializeModel() {

    m_batch_id_isSet = false;
    m_batch_id_isValid = false;

    m_scan_all_result_a_isSet = false;
    m_scan_all_result_a_isValid = false;

    m_scan_all_result_i_isSet = false;
    m_scan_all_result_i_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_total_avs_isSet = false;
    m_total_avs_isValid = false;

    m_total_time_isSet = false;
    m_total_time_isValid = false;
}

void OAIBatchResponse_scan_results::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBatchResponse_scan_results::fromJsonObject(QJsonObject json) {

    m_batch_id_isValid = ::OpenAPI::fromJsonValue(batch_id, json[QString("batch_id")]);
    m_batch_id_isSet = !json[QString("batch_id")].isNull() && m_batch_id_isValid;

    m_scan_all_result_a_isValid = ::OpenAPI::fromJsonValue(scan_all_result_a, json[QString("scan_all_result_a")]);
    m_scan_all_result_a_isSet = !json[QString("scan_all_result_a")].isNull() && m_scan_all_result_a_isValid;

    m_scan_all_result_i_isValid = ::OpenAPI::fromJsonValue(scan_all_result_i, json[QString("scan_all_result_i")]);
    m_scan_all_result_i_isSet = !json[QString("scan_all_result_i")].isNull() && m_scan_all_result_i_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(start_time, json[QString("start_time")]);
    m_start_time_isSet = !json[QString("start_time")].isNull() && m_start_time_isValid;

    m_total_avs_isValid = ::OpenAPI::fromJsonValue(total_avs, json[QString("total_avs")]);
    m_total_avs_isSet = !json[QString("total_avs")].isNull() && m_total_avs_isValid;

    m_total_time_isValid = ::OpenAPI::fromJsonValue(total_time, json[QString("total_time")]);
    m_total_time_isSet = !json[QString("total_time")].isNull() && m_total_time_isValid;
}

QString OAIBatchResponse_scan_results::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBatchResponse_scan_results::asJsonObject() const {
    QJsonObject obj;
    if (m_batch_id_isSet) {
        obj.insert(QString("batch_id"), ::OpenAPI::toJsonValue(batch_id));
    }
    if (scan_all_result_a.isSet()) {
        obj.insert(QString("scan_all_result_a"), ::OpenAPI::toJsonValue(scan_all_result_a));
    }
    if (scan_all_result_i.isSet()) {
        obj.insert(QString("scan_all_result_i"), ::OpenAPI::toJsonValue(scan_all_result_i));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("start_time"), ::OpenAPI::toJsonValue(start_time));
    }
    if (m_total_avs_isSet) {
        obj.insert(QString("total_avs"), ::OpenAPI::toJsonValue(total_avs));
    }
    if (m_total_time_isSet) {
        obj.insert(QString("total_time"), ::OpenAPI::toJsonValue(total_time));
    }
    return obj;
}

QString OAIBatchResponse_scan_results::getBatchId() const {
    return batch_id;
}
void OAIBatchResponse_scan_results::setBatchId(const QString &batch_id) {
    this->batch_id = batch_id;
    this->m_batch_id_isSet = true;
}

OAIProcessingResultsStringEnum OAIBatchResponse_scan_results::getScanAllResultA() const {
    return scan_all_result_a;
}
void OAIBatchResponse_scan_results::setScanAllResultA(const OAIProcessingResultsStringEnum &scan_all_result_a) {
    this->scan_all_result_a = scan_all_result_a;
    this->m_scan_all_result_a_isSet = true;
}

OAIProcessingResultsIndexEnum OAIBatchResponse_scan_results::getScanAllResultI() const {
    return scan_all_result_i;
}
void OAIBatchResponse_scan_results::setScanAllResultI(const OAIProcessingResultsIndexEnum &scan_all_result_i) {
    this->scan_all_result_i = scan_all_result_i;
    this->m_scan_all_result_i_isSet = true;
}

QString OAIBatchResponse_scan_results::getStartTime() const {
    return start_time;
}
void OAIBatchResponse_scan_results::setStartTime(const QString &start_time) {
    this->start_time = start_time;
    this->m_start_time_isSet = true;
}

qint32 OAIBatchResponse_scan_results::getTotalAvs() const {
    return total_avs;
}
void OAIBatchResponse_scan_results::setTotalAvs(const qint32 &total_avs) {
    this->total_avs = total_avs;
    this->m_total_avs_isSet = true;
}

qint32 OAIBatchResponse_scan_results::getTotalTime() const {
    return total_time;
}
void OAIBatchResponse_scan_results::setTotalTime(const qint32 &total_time) {
    this->total_time = total_time;
    this->m_total_time_isSet = true;
}

bool OAIBatchResponse_scan_results::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_batch_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (scan_all_result_a.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (scan_all_result_i.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_avs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBatchResponse_scan_results::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
