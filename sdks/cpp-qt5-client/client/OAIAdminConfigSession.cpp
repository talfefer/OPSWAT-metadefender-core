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

#include "OAIAdminConfigSession.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAdminConfigSession::OAIAdminConfigSession(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAdminConfigSession::OAIAdminConfigSession() {
    this->initializeModel();
}

OAIAdminConfigSession::~OAIAdminConfigSession() {}

void OAIAdminConfigSession::initializeModel() {

    m_absolute_session_timeout_isSet = false;
    m_absolute_session_timeout_isValid = false;

    m_allow_cross_ip_sessions_isSet = false;
    m_allow_cross_ip_sessions_isValid = false;

    m_allow_duplicate_session_isSet = false;
    m_allow_duplicate_session_isValid = false;

    m_session_timeout_isSet = false;
    m_session_timeout_isValid = false;
}

void OAIAdminConfigSession::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAdminConfigSession::fromJsonObject(QJsonObject json) {

    m_absolute_session_timeout_isValid = ::OpenAPI::fromJsonValue(absolute_session_timeout, json[QString("absoluteSessionTimeout")]);
    m_absolute_session_timeout_isSet = !json[QString("absoluteSessionTimeout")].isNull() && m_absolute_session_timeout_isValid;

    m_allow_cross_ip_sessions_isValid = ::OpenAPI::fromJsonValue(allow_cross_ip_sessions, json[QString("allowCrossIpSessions")]);
    m_allow_cross_ip_sessions_isSet = !json[QString("allowCrossIpSessions")].isNull() && m_allow_cross_ip_sessions_isValid;

    m_allow_duplicate_session_isValid = ::OpenAPI::fromJsonValue(allow_duplicate_session, json[QString("allowDuplicateSession")]);
    m_allow_duplicate_session_isSet = !json[QString("allowDuplicateSession")].isNull() && m_allow_duplicate_session_isValid;

    m_session_timeout_isValid = ::OpenAPI::fromJsonValue(session_timeout, json[QString("sessionTimeout")]);
    m_session_timeout_isSet = !json[QString("sessionTimeout")].isNull() && m_session_timeout_isValid;
}

QString OAIAdminConfigSession::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAdminConfigSession::asJsonObject() const {
    QJsonObject obj;
    if (m_absolute_session_timeout_isSet) {
        obj.insert(QString("absoluteSessionTimeout"), ::OpenAPI::toJsonValue(absolute_session_timeout));
    }
    if (m_allow_cross_ip_sessions_isSet) {
        obj.insert(QString("allowCrossIpSessions"), ::OpenAPI::toJsonValue(allow_cross_ip_sessions));
    }
    if (m_allow_duplicate_session_isSet) {
        obj.insert(QString("allowDuplicateSession"), ::OpenAPI::toJsonValue(allow_duplicate_session));
    }
    if (m_session_timeout_isSet) {
        obj.insert(QString("sessionTimeout"), ::OpenAPI::toJsonValue(session_timeout));
    }
    return obj;
}

qint32 OAIAdminConfigSession::getAbsoluteSessionTimeout() const {
    return absolute_session_timeout;
}
void OAIAdminConfigSession::setAbsoluteSessionTimeout(const qint32 &absolute_session_timeout) {
    this->absolute_session_timeout = absolute_session_timeout;
    this->m_absolute_session_timeout_isSet = true;
}

bool OAIAdminConfigSession::isAllowCrossIpSessions() const {
    return allow_cross_ip_sessions;
}
void OAIAdminConfigSession::setAllowCrossIpSessions(const bool &allow_cross_ip_sessions) {
    this->allow_cross_ip_sessions = allow_cross_ip_sessions;
    this->m_allow_cross_ip_sessions_isSet = true;
}

bool OAIAdminConfigSession::isAllowDuplicateSession() const {
    return allow_duplicate_session;
}
void OAIAdminConfigSession::setAllowDuplicateSession(const bool &allow_duplicate_session) {
    this->allow_duplicate_session = allow_duplicate_session;
    this->m_allow_duplicate_session_isSet = true;
}

qint32 OAIAdminConfigSession::getSessionTimeout() const {
    return session_timeout;
}
void OAIAdminConfigSession::setSessionTimeout(const qint32 &session_timeout) {
    this->session_timeout = session_timeout;
    this->m_session_timeout_isSet = true;
}

bool OAIAdminConfigSession::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_absolute_session_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allow_cross_ip_sessions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allow_duplicate_session_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_session_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAdminConfigSession::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
