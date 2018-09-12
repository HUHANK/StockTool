#ifndef NET_H
#define NET_H
#include <QString>

QByteArray TcpSend(const char* sip, const int port, const char*str, const int len);

class HttpClient
{
public:
    HttpClient();
    ~HttpClient();

    QByteArray get(const char* url);
private:
    bool parseUrl(const char* url);
    QString genHead(const char* type);

    QString m_uri;
    int     m_port;
    QString m_ip;

    QString m_oProtocol;
    QString m_oContentType;
    QString m_oHost;
    QString m_oUserAgent;
    QString m_oAccept;
    QString m_oAcceptEncoding;
    QString m_oAcceptLanguage;

};

#endif // NET_H
