#include "stock.h"
#include "../util/net.h"
#include <QJsonDocument>
#include <QJsonParseError>
#include <QJsonObject>
#include <QStringList>
#include <QJsonArray>
#include <QDebug>

QString G_PRE_URL = "http://10.10.19.68:6688";

QMap<QString, QVariant> paresJson(QByteArray &data) {
    QMap<QString, QVariant> ret;

    QJsonParseError jsonError;
    QJsonDocument doc = QJsonDocument::fromJson(data, &jsonError);
    if (!doc.isNull() && jsonError.error == QJsonParseError::NoError) {
        QStringList keys;
        if (doc.isObject()) {
            QJsonObject obj = doc.object();
            keys = obj.keys();
            for(int i=0; i<keys.count(); i++) {
                //qDebug(keys.at(i).toStdString().c_str());
                QJsonValue value = obj.value(keys.at(i));
                //qDebug("%d", value.type());

                if (value.type() == QJsonValue::Object) {
                    QVariant v = value.toVariant();
                    if ( v.canConvert(QVariant::Map) ) {
                        QMap<QString, QVariant> m = v.toMap();
                        ret[keys.at(i)] = m;
                        /*
                        QMap<QString, QVariant>::iterator it;
                        for (it = m.begin(); it != m.end(); it++) {
                            qDebug() << it.key();
                            qDebug() << it.value().toString();

                        }*/
                    }
                }
            }
        }

    }
    return ret;
}

QMap<QString, QVariant> getStockIndex()
{
    QString uri = "/get_index";
    QString url = G_PRE_URL + uri;
    HttpClient http;
    QByteArray data = http.get(url.toStdString().c_str());
    qDebug(data.data());
    QMap<QString, QVariant> ret = paresJson(data);

    return ret;
}
