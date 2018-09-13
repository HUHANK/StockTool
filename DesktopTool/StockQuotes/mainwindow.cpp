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
    model->setColumnCount(3);
    int n = 0;
    model->setHeaderData(n++, Qt::Horizontal, "代码");
    model->setHeaderData(n++, Qt::Horizontal, "名称");
    model->setHeaderData(n++, Qt::Horizontal, "涨幅");
    tbl->setModel(model);

    tbl->verticalHeader()->hide();

    tbl->setEditTriggers(QAbstractItemView::NoEditTriggers);

    QByteArray data = getStockIndex();
    //qDebug(data.data());

}
