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

#include "OAIMetascanReport_scan_details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMetascanReport_scan_details::OAIMetascanReport_scan_details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMetascanReport_scan_details::OAIMetascanReport_scan_details() {
    this->initializeModel();
}

OAIMetascanReport_scan_details::~OAIMetascanReport_scan_details() {}

void OAIMetascanReport_scan_details::initializeModel() {

    m_clam_av_isSet = false;
    m_clam_av_isValid = false;
}

void OAIMetascanReport_scan_details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMetascanReport_scan_details::fromJsonObject(QJsonObject json) {

    m_clam_av_isValid = ::OpenAPI::fromJsonValue(clam_av, json[QString("ClamAV")]);
    m_clam_av_isSet = !json[QString("ClamAV")].isNull() && m_clam_av_isValid;
}

QString OAIMetascanReport_scan_details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMetascanReport_scan_details::asJsonObject() const {
    QJsonObject obj;
    if (clam_av.isSet()) {
        obj.insert(QString("ClamAV"), ::OpenAPI::toJsonValue(clam_av));
    }
    return obj;
}

OAIAVEngineScanReport OAIMetascanReport_scan_details::getClamAv() const {
    return clam_av;
}
void OAIMetascanReport_scan_details::setClamAv(const OAIAVEngineScanReport &clam_av) {
    this->clam_av = clam_av;
    this->m_clam_av_isSet = true;
}

bool OAIMetascanReport_scan_details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (clam_av.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMetascanReport_scan_details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
