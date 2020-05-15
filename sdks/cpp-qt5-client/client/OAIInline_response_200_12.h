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
 * OAIInline_response_200_12.h
 *
 * 
 */

#ifndef OAIInline_response_200_12_H
#define OAIInline_response_200_12_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInline_response_200_12 : public OAIObject {
public:
    OAIInline_response_200_12();
    OAIInline_response_200_12(QString json);
    ~OAIInline_response_200_12() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isActive() const;
    void setActive(const bool &active);

    QString getDefTime() const;
    void setDefTime(const QString &def_time);

    qint32 getDownloadProgress() const;
    void setDownloadProgress(const qint32 &download_progress);

    QString getDownloadTime() const;
    void setDownloadTime(const QString &download_time);

    QString getEngId() const;
    void setEngId(const QString &eng_id);

    QString getEngName() const;
    void setEngName(const QString &eng_name);

    QString getEngType() const;
    void setEngType(const QString &eng_type);

    QString getEngVer() const;
    void setEngVer(const QString &eng_ver);

    QString getEngineType() const;
    void setEngineType(const QString &engine_type);

    QString getState() const;
    void setState(const QString &state);

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool active;
    bool m_active_isSet;
    bool m_active_isValid;

    QString def_time;
    bool m_def_time_isSet;
    bool m_def_time_isValid;

    qint32 download_progress;
    bool m_download_progress_isSet;
    bool m_download_progress_isValid;

    QString download_time;
    bool m_download_time_isSet;
    bool m_download_time_isValid;

    QString eng_id;
    bool m_eng_id_isSet;
    bool m_eng_id_isValid;

    QString eng_name;
    bool m_eng_name_isSet;
    bool m_eng_name_isValid;

    QString eng_type;
    bool m_eng_type_isSet;
    bool m_eng_type_isValid;

    QString eng_ver;
    bool m_eng_ver_isSet;
    bool m_eng_ver_isValid;

    QString engine_type;
    bool m_engine_type_isSet;
    bool m_engine_type_isValid;

    QString state;
    bool m_state_isSet;
    bool m_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInline_response_200_12)

#endif // OAIInline_response_200_12_H
