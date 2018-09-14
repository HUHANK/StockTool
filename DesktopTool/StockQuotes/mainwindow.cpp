#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QStandardItemModel>
#include "financial/stock.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_tabWidget_tabBarClicked(int index)
{
    qDebug("%d",index);
    if (0 == index) {
        init_HQTblView();
    }
}


void MainWindow::init_HQTblView()
{
    QTableView* tbl = ui->HQTblView;
    QStandardItemModel *model = new QStandardItemModel();
    model->setColumnCount(10);
    int n = 0;
    model->setHeaderData(n++, Qt::Horizontal, "指数代码");
    model->setHeaderData(n++, Qt::Horizontal, "指数名称");
    model->setHeaderData(n++, Qt::Horizontal, "涨跌幅");
    model->setHeaderData(n++, Qt::Horizontal, "开盘点位");
    model->setHeaderData(n++, Qt::Horizontal, "昨收点位");
    model->setHeaderData(n++, Qt::Horizontal, "收盘点位");
    model->setHeaderData(n++, Qt::Horizontal, "最高点位");
    model->setHeaderData(n++, Qt::Horizontal, "最低点位");
    model->setHeaderData(n++, Qt::Horizontal, "成交量(手)");
    model->setHeaderData(n++, Qt::Horizontal, "成交金额(亿)");
    tbl->setModel(model);

    tbl->verticalHeader()->hide();

    tbl->setEditTriggers(QAbstractItemView::NoEditTriggers);

    QMap<QString, QVariant> data = getStockIndex();

    QMap<QString, QVariant>::iterator it;
    for ( it = data.begin(); it != data.end(); it++ ) {
        QString key = it.key();
        if (key == "code") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,0, new QStandardItem(v));
                model->item(i,0)->setTextAlignment(Qt::AlignCenter);
            }
        }
        else if (key == "name") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,1, new QStandardItem(v));
                model->item(i,1)->setTextAlignment(Qt::AlignCenter);
            }
        }
        else if (key == "change") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,2, new QStandardItem(v));
                model->item(i,2)->setTextAlignment(Qt::AlignRight);
            }
        }
        else if (key == "open") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,3, new QStandardItem(v));
                model->item(i,3)->setTextAlignment(Qt::AlignRight);
            }
        }
        else if (key == "preclose") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,4, new QStandardItem(v));
                model->item(i,4)->setTextAlignment(Qt::AlignRight);
            }
        }
        else if (key == "close") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,5, new QStandardItem(v));
                model->item(i,5)->setTextAlignment(Qt::AlignRight);
            }
        }
        else if (key == "high") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,6, new QStandardItem(v));
                model->item(i,6)->setTextAlignment(Qt::AlignRight);
            }
        }
        else if (key == "low") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,7, new QStandardItem(v));
                model->item(i,7)->setTextAlignment(Qt::AlignRight);
            }
        }
        else if (key == "volume") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,8, new QStandardItem(v));
                model->item(i,8)->setTextAlignment(Qt::AlignRight);
            }
        }
        else if (key == "amount") {
            QMap<QString, QVariant> mv = data[key].toMap();
            for (int i=0; i<mv.size(); i++) {
                QString s = QString::number(i);
                QString v = mv[s].toString();
                model->setItem(i,9, new QStandardItem(v));
                model->item(i,9)->setTextAlignment(Qt::AlignRight);
            }
        }
    }
    model->sort(0);

}
