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
    //QString url = "http://hq.sinajs.cn/rn=xppzh&list=sh000001,sh000002,sh000003,sh000008,sh000009,sh000010,sh000011,sh000012,sh000016,sh000017,sh000300,sh000905,sz399001,sz399002,sz399003,sz399004,sz399005,sz399006,sz399008,sz399100,sz399101,sz399106,sz399107,sz399108,sz399333,sz399606";
    HttpClient http;
    QByteArray data = http.get(url.toStdString().c_str());
    qDebug(data.data());
    QMap<QString, QVariant> ret = paresJson(data);

    return ret;
}
