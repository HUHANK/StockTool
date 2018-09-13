#include "net.h"
#include <QTcpSocket>

QByteArray TcpSend(const char* sip, const int port, const char*str, const int len)
{
    QTcpSocket socket;
    socket.abort();
    socket.connectToHost(sip, port);
    socket.waitForConnected();

    socket.write(str, len);
    socket.waitForBytesWritten();

    QByteArray res = {0};
    while( socket.waitForReadyRead() )
    {
        QByteArray data = socket.readAll();
        res += data;
    }
    socket.close();
    return res;
}


HttpClient::HttpClient() {
    m_uri = "";

    m_oProtocol = "HTTP/1.1";
    m_oContentType = "text/html";
    m_oHost = "";
    m_oUserAgent = "User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)";
    m_oAccept = "text/html";
    m_oAcceptEncoding = "gzip, deflate";
    m_oAcceptLanguage = "utf-8";
}

HttpClient::~HttpClient() {

}

QByteArray HttpClient::get(const char* url) {
    QByteArray ret ;
    if (!parseUrl(url)) return ret;
    QString header = genHead("GET");

    ret = TcpSend(m_ip.toStdString().c_str(), m_port, header.toStdString().c_str(), strlen(header.toStdString().c_str()));

    char br[3] = {13,10,0};
    char slen[32] = {0};
    char* p = strstr(ret.data(), "Conten-Length:");
    char* p2 = strstr(p, br);
    if (!p || !p2) {
        return QByteArray();
    }
    strncpy(slen, p+14, p2-p-14);
    int packLen = atoi(slen);
    //qDebug(slen);
    //qDebug("%d", packLen);

    QByteArray d = ret.right(packLen);
    //qDebug(d.data());
    return d;
}

QString HttpClient::genHead(const char* type) {
    QString ret = "";
    if (strcmp(type, "GET") == 0) {
        ret += "GET " + m_uri + " " + m_oProtocol;
        ret.append(13); ret.append(10);
        ret += "Connection: Keep-Alive";
        ret.append(13); ret.append(10);
        if (m_oUserAgent != "") {
            ret += "User-Agent: " + m_oUserAgent;
            ret.append(13); ret.append(10);
        }
        ret.append(13); ret.append(10);
        ret.append(13); ret.append(10);
    }
    return ret;
}

bool HttpClient::parseUrl(const char* url) {
    if (!url) {
        qErrnoWarning("HttpClient::parseUrl param Error!");
        return false;
    }
    if (strncmp(url, "http", 4) != 0) {
        qErrnoWarning("HttpClient not HTTP Protocol!");
        return false;
    }
    m_uri = "";
    char buf[256] = {0};
    char* p = (char*)url;
    p = p + 4 + 1 + 2; /*http : //*/
    /*IP+Port*/
    char* tmp = strstr(p, "/");
    if (tmp == nullptr) {
        strcpy(buf, p);
        m_uri = "/";
    } else {
        strncpy(buf, p, (tmp-p));
    }
    p = p + (tmp-p);

    tmp = strstr(buf, ":");
    if (nullptr == tmp) {
        m_ip = QString::fromUtf8(buf);
        m_port = 80;
    } else {
        tmp = strtok(buf, ":");
        if (tmp) {
            m_ip = QString::fromUtf8(tmp);
            tmp = strtok(NULL, ":");
            if (tmp) {
                m_port = atoi(tmp);
            }
        }
    }

    if (m_uri != "/") {
        m_uri = QString::fromUtf8(p);
    }
    return true;
}

