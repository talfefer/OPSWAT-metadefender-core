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

#include "OAIInline_object_2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInline_object_2::OAIInline_object_2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInline_object_2::OAIInline_object_2() {
    this->initializeModel();
}

OAIInline_object_2::~OAIInline_object_2() {}

void OAIInline_object_2::initializeModel() {

    m_old_password_isSet = false;
    m_old_password_isValid = false;

    m_new_password_isSet = false;
    m_new_password_isValid = false;
}

void OAIInline_object_2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInline_object_2::fromJsonObject(QJsonObject json) {

    m_old_password_isValid = ::OpenAPI::fromJsonValue(old_password, json[QString("old_password")]);
    m_old_password_isSet = !json[QString("old_password")].isNull() && m_old_password_isValid;

    m_new_password_isValid = ::OpenAPI::fromJsonValue(new_password, json[QString("new_password")]);
    m_new_password_isSet = !json[QString("new_password")].isNull() && m_new_password_isValid;
}

QString OAIInline_object_2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInline_object_2::asJsonObject() const {
    QJsonObject obj;
    if (m_old_password_isSet) {
        obj.insert(QString("old_password"), ::OpenAPI::toJsonValue(old_password));
    }
    if (m_new_password_isSet) {
        obj.insert(QString("new_password"), ::OpenAPI::toJsonValue(new_password));
    }
    return obj;
}

QString OAIInline_object_2::getOldPassword() const {
    return old_password;
}
void OAIInline_object_2::setOldPassword(const QString &old_password) {
    this->old_password = old_password;
    this->m_old_password_isSet = true;
}

QString OAIInline_object_2::getNewPassword() const {
    return new_password;
}
void OAIInline_object_2::setNewPassword(const QString &new_password) {
    this->new_password = new_password;
    this->m_new_password_isSet = true;
}

bool OAIInline_object_2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_old_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_password_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInline_object_2::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
