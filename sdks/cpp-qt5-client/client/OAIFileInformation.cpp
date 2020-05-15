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

#include "OAIFileInformation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFileInformation::OAIFileInformation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFileInformation::OAIFileInformation() {
    this->initializeModel();
}

OAIFileInformation::~OAIFileInformation() {}

void OAIFileInformation::initializeModel() {

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_file_size_isSet = false;
    m_file_size_isValid = false;

    m_file_type_isSet = false;
    m_file_type_isValid = false;

    m_file_type_description_isSet = false;
    m_file_type_description_isValid = false;

    m_md5_isSet = false;
    m_md5_isValid = false;

    m_sha1_isSet = false;
    m_sha1_isValid = false;

    m_sha256_isSet = false;
    m_sha256_isValid = false;

    m_upload_timestamp_isSet = false;
    m_upload_timestamp_isValid = false;
}

void OAIFileInformation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFileInformation::fromJsonObject(QJsonObject json) {

    m_display_name_isValid = ::OpenAPI::fromJsonValue(display_name, json[QString("display_name")]);
    m_display_name_isSet = !json[QString("display_name")].isNull() && m_display_name_isValid;

    m_file_size_isValid = ::OpenAPI::fromJsonValue(file_size, json[QString("file_size")]);
    m_file_size_isSet = !json[QString("file_size")].isNull() && m_file_size_isValid;

    m_file_type_isValid = ::OpenAPI::fromJsonValue(file_type, json[QString("file_type")]);
    m_file_type_isSet = !json[QString("file_type")].isNull() && m_file_type_isValid;

    m_file_type_description_isValid = ::OpenAPI::fromJsonValue(file_type_description, json[QString("file_type_description")]);
    m_file_type_description_isSet = !json[QString("file_type_description")].isNull() && m_file_type_description_isValid;

    m_md5_isValid = ::OpenAPI::fromJsonValue(md5, json[QString("md5")]);
    m_md5_isSet = !json[QString("md5")].isNull() && m_md5_isValid;

    m_sha1_isValid = ::OpenAPI::fromJsonValue(sha1, json[QString("sha1")]);
    m_sha1_isSet = !json[QString("sha1")].isNull() && m_sha1_isValid;

    m_sha256_isValid = ::OpenAPI::fromJsonValue(sha256, json[QString("sha256")]);
    m_sha256_isSet = !json[QString("sha256")].isNull() && m_sha256_isValid;

    m_upload_timestamp_isValid = ::OpenAPI::fromJsonValue(upload_timestamp, json[QString("upload_timestamp")]);
    m_upload_timestamp_isSet = !json[QString("upload_timestamp")].isNull() && m_upload_timestamp_isValid;
}

QString OAIFileInformation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFileInformation::asJsonObject() const {
    QJsonObject obj;
    if (m_display_name_isSet) {
        obj.insert(QString("display_name"), ::OpenAPI::toJsonValue(display_name));
    }
    if (m_file_size_isSet) {
        obj.insert(QString("file_size"), ::OpenAPI::toJsonValue(file_size));
    }
    if (m_file_type_isSet) {
        obj.insert(QString("file_type"), ::OpenAPI::toJsonValue(file_type));
    }
    if (m_file_type_description_isSet) {
        obj.insert(QString("file_type_description"), ::OpenAPI::toJsonValue(file_type_description));
    }
    if (m_md5_isSet) {
        obj.insert(QString("md5"), ::OpenAPI::toJsonValue(md5));
    }
    if (m_sha1_isSet) {
        obj.insert(QString("sha1"), ::OpenAPI::toJsonValue(sha1));
    }
    if (m_sha256_isSet) {
        obj.insert(QString("sha256"), ::OpenAPI::toJsonValue(sha256));
    }
    if (m_upload_timestamp_isSet) {
        obj.insert(QString("upload_timestamp"), ::OpenAPI::toJsonValue(upload_timestamp));
    }
    return obj;
}

QString OAIFileInformation::getDisplayName() const {
    return display_name;
}
void OAIFileInformation::setDisplayName(const QString &display_name) {
    this->display_name = display_name;
    this->m_display_name_isSet = true;
}

qint32 OAIFileInformation::getFileSize() const {
    return file_size;
}
void OAIFileInformation::setFileSize(const qint32 &file_size) {
    this->file_size = file_size;
    this->m_file_size_isSet = true;
}

QString OAIFileInformation::getFileType() const {
    return file_type;
}
void OAIFileInformation::setFileType(const QString &file_type) {
    this->file_type = file_type;
    this->m_file_type_isSet = true;
}

QString OAIFileInformation::getFileTypeDescription() const {
    return file_type_description;
}
void OAIFileInformation::setFileTypeDescription(const QString &file_type_description) {
    this->file_type_description = file_type_description;
    this->m_file_type_description_isSet = true;
}

QString OAIFileInformation::getMd5() const {
    return md5;
}
void OAIFileInformation::setMd5(const QString &md5) {
    this->md5 = md5;
    this->m_md5_isSet = true;
}

QString OAIFileInformation::getSha1() const {
    return sha1;
}
void OAIFileInformation::setSha1(const QString &sha1) {
    this->sha1 = sha1;
    this->m_sha1_isSet = true;
}

QString OAIFileInformation::getSha256() const {
    return sha256;
}
void OAIFileInformation::setSha256(const QString &sha256) {
    this->sha256 = sha256;
    this->m_sha256_isSet = true;
}

QString OAIFileInformation::getUploadTimestamp() const {
    return upload_timestamp;
}
void OAIFileInformation::setUploadTimestamp(const QString &upload_timestamp) {
    this->upload_timestamp = upload_timestamp;
    this->m_upload_timestamp_isSet = true;
}

bool OAIFileInformation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_type_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_md5_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sha1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sha256_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_upload_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFileInformation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
