#include "stock.h"
#include "../util/net.h"
#include <QJsonDocument>
#include <QJsonParseError>
#include <QJsonObject>
#include <QStringList>
#include <QJsonArray>

QString G_PRE_URL = "http://10.10.19.68:6688";

QByteArray getStockIndex()
{
    QString uri = "/get_index";
    QString url = G_PRE_URL + uri;
    HttpClient http;
    QByteArray data = http.get(url.toStdString().c_str());

    QJsonParseError jsonError;
    QJsonDocument doc = QJsonDocument::fromJson(data, &jsonError);
    if (!doc.isNull() && jsonError.error == QJsonParseError::NoError) {
        QStringList keys;
        if (doc.isObject()) {
            QJsonObject obj = doc.object();
            keys = obj.keys();
            for(int i=0; i<keys.count(); i++) {
                qDebug(keys.at(i).toStdString().c_str());
                QJsonValue value = obj.value(keys.at(i));
                qDebug("%d", value.type());
                if (value.type() == QJsonValue::Array) {
                    QJsonArray arr = value.toArray();

                }
            }
        }

    }

}
