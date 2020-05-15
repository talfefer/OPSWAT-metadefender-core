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

#include "OAIBatchApi.h"
#include "OAIHelpers.h"

#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIBatchApi::OAIBatchApi(const QString &scheme, const QString &host, int port, const QString &basePath, const int timeOut)
    : _scheme(scheme),
      _host(host),
      _port(port),
      _basePath(basePath),
      _timeOut(timeOut),
      isResponseCompressionEnabled(false),
      isRequestCompressionEnabled(false) {}

OAIBatchApi::~OAIBatchApi() {
}

void OAIBatchApi::setScheme(const QString &scheme) {
    _scheme = scheme;
}

void OAIBatchApi::setHost(const QString &host) {
    _host = host;
}

void OAIBatchApi::setPort(int port) {
    _port = port;
}

void OAIBatchApi::setBasePath(const QString &basePath) {
    _basePath = basePath;
}

void OAIBatchApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIBatchApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIBatchApi::addHeaders(const QString &key, const QString &value) {
    defaultHeaders.insert(key, value);
}

void OAIBatchApi::enableRequestCompression() {
    isRequestCompressionEnabled = true;
}

void OAIBatchApi::enableResponseCompression() {
    isResponseCompressionEnabled = true;
}

void OAIBatchApi::abortRequests(){
    emit abortRequestsSignal();
}

void OAIBatchApi::batchCancel(const QString &batch_id, const QString &apikey) {
    QString fullPath = QString("%1://%2%3%4%5")
                           .arg(_scheme)
                           .arg(_host)
                           .arg(_port ? ":" + QString::number(_port) : "")
                           .arg(_basePath)
                           .arg("/file/{batchId}/cancel");
    QString batch_idPathParam("{");
    batch_idPathParam.append("batchId").append("}");
    fullPath.replace(batch_idPathParam, QUrl::toPercentEncoding(::OpenAPI::toStringValue(batch_id)));

    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (apikey != nullptr) {
        input.headers.insert("apikey", apikey);
    }

    foreach (QString key, this->defaultHeaders.keys()) { input.headers.insert(key, this->defaultHeaders.value(key)); }

    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBatchApi::batchCancelCallback);
    connect(this, &OAIBatchApi::abortRequestsSignal, worker, &QObject::deleteLater); 
    worker->execute(&input);
}

void OAIBatchApi::batchCancelCallback(OAIHttpRequestWorker *worker) {
    QString msg;
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    } else {
        msg = "Error: " + worker->error_str;
        error_str = QString("%1, %2").arg(worker->error_str).arg(QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        emit batchCancelSignal(output);
        emit batchCancelSignalFull(worker, output);
    } else {
        emit batchCancelSignalE(output, error_type, error_str);
        emit batchCancelSignalEFull(worker, error_type, error_str);
    }
}

void OAIBatchApi::batchClose(const QString &batch_id, const QString &apikey) {
    QString fullPath = QString("%1://%2%3%4%5")
                           .arg(_scheme)
                           .arg(_host)
                           .arg(_port ? ":" + QString::number(_port) : "")
                           .arg(_basePath)
                           .arg("/file/batch/{batchId}/close");
    QString batch_idPathParam("{");
    batch_idPathParam.append("batchId").append("}");
    fullPath.replace(batch_idPathParam, QUrl::toPercentEncoding(::OpenAPI::toStringValue(batch_id)));

    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (apikey != nullptr) {
        input.headers.insert("apikey", apikey);
    }

    foreach (QString key, this->defaultHeaders.keys()) { input.headers.insert(key, this->defaultHeaders.value(key)); }

    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBatchApi::batchCloseCallback);
    connect(this, &OAIBatchApi::abortRequestsSignal, worker, &QObject::deleteLater); 
    worker->execute(&input);
}

void OAIBatchApi::batchCloseCallback(OAIHttpRequestWorker *worker) {
    QString msg;
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    } else {
        msg = "Error: " + worker->error_str;
        error_str = QString("%1, %2").arg(worker->error_str).arg(QString(worker->response));
    }
    OAIBatchResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        emit batchCloseSignal(output);
        emit batchCloseSignalFull(worker, output);
    } else {
        emit batchCloseSignalE(output, error_type, error_str);
        emit batchCloseSignalEFull(worker, error_type, error_str);
    }
}

void OAIBatchApi::batchCreate(const QString &apikey, const QString &rule, const QString &user_agent, const QString &user_data) {
    QString fullPath = QString("%1://%2%3%4%5")
                           .arg(_scheme)
                           .arg(_host)
                           .arg(_port ? ":" + QString::number(_port) : "")
                           .arg(_basePath)
                           .arg("/file/batch");

    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (apikey != nullptr) {
        input.headers.insert("apikey", apikey);
    }

    if (rule != nullptr) {
        input.headers.insert("rule", rule);
    }

    if (user_agent != nullptr) {
        input.headers.insert("user_agent", user_agent);
    }

    if (user_data != nullptr) {
        input.headers.insert("user-data", user_data);
    }

    foreach (QString key, this->defaultHeaders.keys()) { input.headers.insert(key, this->defaultHeaders.value(key)); }

    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBatchApi::batchCreateCallback);
    connect(this, &OAIBatchApi::abortRequestsSignal, worker, &QObject::deleteLater); 
    worker->execute(&input);
}

void OAIBatchApi::batchCreateCallback(OAIHttpRequestWorker *worker) {
    QString msg;
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    } else {
        msg = "Error: " + worker->error_str;
        error_str = QString("%1, %2").arg(worker->error_str).arg(QString(worker->response));
    }
    OAIBatchId output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        emit batchCreateSignal(output);
        emit batchCreateSignalFull(worker, output);
    } else {
        emit batchCreateSignalE(output, error_type, error_str);
        emit batchCreateSignalEFull(worker, error_type, error_str);
    }
}

void OAIBatchApi::batchSignedResult(const QString &batch_id, const QString &apikey) {
    QString fullPath = QString("%1://%2%3%4%5")
                           .arg(_scheme)
                           .arg(_host)
                           .arg(_port ? ":" + QString::number(_port) : "")
                           .arg(_basePath)
                           .arg("/file/batch/{batchId}/certificate");
    QString batch_idPathParam("{");
    batch_idPathParam.append("batchId").append("}");
    fullPath.replace(batch_idPathParam, QUrl::toPercentEncoding(::OpenAPI::toStringValue(batch_id)));

    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");

    if (apikey != nullptr) {
        input.headers.insert("apikey", apikey);
    }

    foreach (QString key, this->defaultHeaders.keys()) { input.headers.insert(key, this->defaultHeaders.value(key)); }

    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBatchApi::batchSignedResultCallback);
    connect(this, &OAIBatchApi::abortRequestsSignal, worker, &QObject::deleteLater); 
    worker->execute(&input);
}

void OAIBatchApi::batchSignedResultCallback(OAIHttpRequestWorker *worker) {
    QString msg;
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    } else {
        msg = "Error: " + worker->error_str;
        error_str = QString("%1, %2").arg(worker->error_str).arg(QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        emit batchSignedResultSignal();
        emit batchSignedResultSignalFull(worker);
    } else {
        emit batchSignedResultSignalE(error_type, error_str);
        emit batchSignedResultSignalEFull(worker, error_type, error_str);
    }
}

void OAIBatchApi::batchStatus(const QString &batch_id, const QString &apikey) {
    QString fullPath = QString("%1://%2%3%4%5")
                           .arg(_scheme)
                           .arg(_host)
                           .arg(_port ? ":" + QString::number(_port) : "")
                           .arg(_basePath)
                           .arg("/file/batch/{batchId}");
    QString batch_idPathParam("{");
    batch_idPathParam.append("batchId").append("}");
    fullPath.replace(batch_idPathParam, QUrl::toPercentEncoding(::OpenAPI::toStringValue(batch_id)));

    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");

    if (apikey != nullptr) {
        input.headers.insert("apikey", apikey);
    }

    foreach (QString key, this->defaultHeaders.keys()) { input.headers.insert(key, this->defaultHeaders.value(key)); }

    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIBatchApi::batchStatusCallback);
    connect(this, &OAIBatchApi::abortRequestsSignal, worker, &QObject::deleteLater); 
    worker->execute(&input);
}

void OAIBatchApi::batchStatusCallback(OAIHttpRequestWorker *worker) {
    QString msg;
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    } else {
        msg = "Error: " + worker->error_str;
        error_str = QString("%1, %2").arg(worker->error_str).arg(QString(worker->response));
    }
    OAIBatchResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        emit batchStatusSignal(output);
        emit batchStatusSignalFull(worker, output);
    } else {
        emit batchStatusSignalE(output, error_type, error_str);
        emit batchStatusSignalEFull(worker, error_type, error_str);
    }
}

} // namespace OpenAPI
