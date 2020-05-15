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
 * OAIAdminConfigUpdate.h
 *
 * API object for /admin/config/update
 */

#ifndef OAIAdminConfigUpdate_H
#define OAIAdminConfigUpdate_H

#include <QJsonObject>

#include "OAIAdminConfigUpdate_disabledupdate.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAdminConfigUpdate : public OAIObject {
public:
    OAIAdminConfigUpdate();
    OAIAdminConfigUpdate(QString json);
    ~OAIAdminConfigUpdate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAutoupdateperiod() const;
    void setAutoupdateperiod(const qint32 &autoupdateperiod);

    bool isDeleteafterimport() const;
    void setDeleteafterimport(const bool &deleteafterimport);

    QList<OAIAdminConfigUpdate_disabledupdate> getDisabledupdate() const;
    void setDisabledupdate(const QList<OAIAdminConfigUpdate_disabledupdate> &disabledupdate);

    QString getPickupfolder() const;
    void setPickupfolder(const QString &pickupfolder);

    QString getSource() const;
    void setSource(const QString &source);

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 autoupdateperiod;
    bool m_autoupdateperiod_isSet;
    bool m_autoupdateperiod_isValid;

    bool deleteafterimport;
    bool m_deleteafterimport_isSet;
    bool m_deleteafterimport_isValid;

    QList<OAIAdminConfigUpdate_disabledupdate> disabledupdate;
    bool m_disabledupdate_isSet;
    bool m_disabledupdate_isValid;

    QString pickupfolder;
    bool m_pickupfolder_isSet;
    bool m_pickupfolder_isValid;

    QString source;
    bool m_source_isSet;
    bool m_source_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAdminConfigUpdate)

#endif // OAIAdminConfigUpdate_H
