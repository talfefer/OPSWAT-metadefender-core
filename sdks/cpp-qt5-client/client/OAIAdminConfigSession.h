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
 * OAIAdminConfigSession.h
 *
 * API object for /admin/config/session
 */

#ifndef OAIAdminConfigSession_H
#define OAIAdminConfigSession_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAdminConfigSession : public OAIObject {
public:
    OAIAdminConfigSession();
    OAIAdminConfigSession(QString json);
    ~OAIAdminConfigSession() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAbsoluteSessionTimeout() const;
    void setAbsoluteSessionTimeout(const qint32 &absolute_session_timeout);

    bool isAllowCrossIpSessions() const;
    void setAllowCrossIpSessions(const bool &allow_cross_ip_sessions);

    bool isAllowDuplicateSession() const;
    void setAllowDuplicateSession(const bool &allow_duplicate_session);

    qint32 getSessionTimeout() const;
    void setSessionTimeout(const qint32 &session_timeout);

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 absolute_session_timeout;
    bool m_absolute_session_timeout_isSet;
    bool m_absolute_session_timeout_isValid;

    bool allow_cross_ip_sessions;
    bool m_allow_cross_ip_sessions_isSet;
    bool m_allow_cross_ip_sessions_isValid;

    bool allow_duplicate_session;
    bool m_allow_duplicate_session_isSet;
    bool m_allow_duplicate_session_isValid;

    qint32 session_timeout;
    bool m_session_timeout_isSet;
    bool m_session_timeout_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAdminConfigSession)

#endif // OAIAdminConfigSession_H
