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

#include "OAIAnalysisResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAnalysisResult::OAIAnalysisResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAnalysisResult::OAIAnalysisResult() {
    this->initializeModel();
}

OAIAnalysisResult::~OAIAnalysisResult() {}

void OAIAnalysisResult::initializeModel() {

    m_data_id_isSet = false;
    m_data_id_isValid = false;

    m_dlp_info_isSet = false;
    m_dlp_info_isValid = false;

    m_file_info_isSet = false;
    m_file_info_isValid = false;

    m_process_info_isSet = false;
    m_process_info_isValid = false;

    m_scan_results_isSet = false;
    m_scan_results_isValid = false;

    m_vulnerability_info_isSet = false;
    m_vulnerability_info_isValid = false;

    m_yara_isSet = false;
    m_yara_isValid = false;
}

void OAIAnalysisResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAnalysisResult::fromJsonObject(QJsonObject json) {

    m_data_id_isValid = ::OpenAPI::fromJsonValue(data_id, json[QString("data_id")]);
    m_data_id_isSet = !json[QString("data_id")].isNull() && m_data_id_isValid;

    m_dlp_info_isValid = ::OpenAPI::fromJsonValue(dlp_info, json[QString("dlp_info")]);
    m_dlp_info_isSet = !json[QString("dlp_info")].isNull() && m_dlp_info_isValid;

    m_file_info_isValid = ::OpenAPI::fromJsonValue(file_info, json[QString("file_info")]);
    m_file_info_isSet = !json[QString("file_info")].isNull() && m_file_info_isValid;

    m_process_info_isValid = ::OpenAPI::fromJsonValue(process_info, json[QString("process_info")]);
    m_process_info_isSet = !json[QString("process_info")].isNull() && m_process_info_isValid;

    m_scan_results_isValid = ::OpenAPI::fromJsonValue(scan_results, json[QString("scan_results")]);
    m_scan_results_isSet = !json[QString("scan_results")].isNull() && m_scan_results_isValid;

    m_vulnerability_info_isValid = ::OpenAPI::fromJsonValue(vulnerability_info, json[QString("vulnerability_info")]);
    m_vulnerability_info_isSet = !json[QString("vulnerability_info")].isNull() && m_vulnerability_info_isValid;

    m_yara_isValid = ::OpenAPI::fromJsonValue(yara, json[QString("yara")]);
    m_yara_isSet = !json[QString("yara")].isNull() && m_yara_isValid;
}

QString OAIAnalysisResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAnalysisResult::asJsonObject() const {
    QJsonObject obj;
    if (m_data_id_isSet) {
        obj.insert(QString("data_id"), ::OpenAPI::toJsonValue(data_id));
    }
    if (dlp_info.isSet()) {
        obj.insert(QString("dlp_info"), ::OpenAPI::toJsonValue(dlp_info));
    }
    if (file_info.isSet()) {
        obj.insert(QString("file_info"), ::OpenAPI::toJsonValue(file_info));
    }
    if (process_info.isSet()) {
        obj.insert(QString("process_info"), ::OpenAPI::toJsonValue(process_info));
    }
    if (scan_results.isSet()) {
        obj.insert(QString("scan_results"), ::OpenAPI::toJsonValue(scan_results));
    }
    if (vulnerability_info.isSet()) {
        obj.insert(QString("vulnerability_info"), ::OpenAPI::toJsonValue(vulnerability_info));
    }
    if (yara.isSet()) {
        obj.insert(QString("yara"), ::OpenAPI::toJsonValue(yara));
    }
    return obj;
}

QString OAIAnalysisResult::getDataId() const {
    return data_id;
}
void OAIAnalysisResult::setDataId(const QString &data_id) {
    this->data_id = data_id;
    this->m_data_id_isSet = true;
}

OAIDLPResponse OAIAnalysisResult::getDlpInfo() const {
    return dlp_info;
}
void OAIAnalysisResult::setDlpInfo(const OAIDLPResponse &dlp_info) {
    this->dlp_info = dlp_info;
    this->m_dlp_info_isSet = true;
}

OAIFileInformation OAIAnalysisResult::getFileInfo() const {
    return file_info;
}
void OAIAnalysisResult::setFileInfo(const OAIFileInformation &file_info) {
    this->file_info = file_info;
    this->m_file_info_isSet = true;
}

OAIAnalysisResult_process_info OAIAnalysisResult::getProcessInfo() const {
    return process_info;
}
void OAIAnalysisResult::setProcessInfo(const OAIAnalysisResult_process_info &process_info) {
    this->process_info = process_info;
    this->m_process_info_isSet = true;
}

OAIMetascanReport OAIAnalysisResult::getScanResults() const {
    return scan_results;
}
void OAIAnalysisResult::setScanResults(const OAIMetascanReport &scan_results) {
    this->scan_results = scan_results;
    this->m_scan_results_isSet = true;
}

OAIVulnerabilityResponse OAIAnalysisResult::getVulnerabilityInfo() const {
    return vulnerability_info;
}
void OAIAnalysisResult::setVulnerabilityInfo(const OAIVulnerabilityResponse &vulnerability_info) {
    this->vulnerability_info = vulnerability_info;
    this->m_vulnerability_info_isSet = true;
}

OAIYaraReport OAIAnalysisResult::getYara() const {
    return yara;
}
void OAIAnalysisResult::setYara(const OAIYaraReport &yara) {
    this->yara = yara;
    this->m_yara_isSet = true;
}

bool OAIAnalysisResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (dlp_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (file_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (process_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (scan_results.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (vulnerability_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (yara.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAnalysisResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
