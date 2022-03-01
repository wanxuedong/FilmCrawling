# coding:utf-8
import Knn
from package import ADC
from package import BiD
from package import EightO
from package import FourKW
from package import MeiJW
from package import MeiJx
from package import MeiMDX
from package import MuG
from package import NaiF
from package import NineN
from package import NineYKK
from package import OneNZF
from package import QuanM
from package import ReallyNotCard
from package import TenZEZ
from package import TianZ
from package import XiangKJ
from package import YiXDM
from package import VipYY
from package import NiKDM
from package import PianK
from package import MeiJTT


# 累计 427840
# 检查是否存在指定的最新电影
from upload import Upload


def checkNewFilm(filmName):
    print ('检查最新电影 《' + filmName + '》  是否存在 \n')

    # 31454 完成
    ReallyNotCard.checkTarget(filmName)
    # 45850
    ADC.checkTarget(filmName)
    # 7606 完成
    OneNZF.checkTarget(filmName)
    # 7346
    MeiJx.checkTarget(filmName)
    EightO.checkTarget(filmName)
    # 23923 完成
    TianZ.checkTarget(filmName)
    # 14581 完成
    XiangKJ.checkTarget(filmName)
    # 57882 完成
    NaiF.checkTarget(filmName)
    # 31316 完成
    FourKW.checkTarget(filmName)
    # 11504 完成
    NineN.checkTarget(filmName)
    # 25819 完成
    TenZEZ.checkTarget(filmName)
    # 7802 完成
    MeiMDX.checkTarget(filmName)
    # 17846 完成
    BiD.checkTarget(filmName)
    # 36437 完成
    QuanM.checkTarget(filmName)
    # 47669 完成
    NineYKK.checkTarget(filmName)
    #
    MuG.checkTarget(filmName)
    # 3010 完成
    MeiJW.checkTarget(filmName)
    # 3180 完成
    YiXDM.checkTarget(filmName)
    # 24575 完成
    VipYY.checkTarget(filmName)
    # 14929 完成
    NiKDM.checkTarget(filmName)
    # 15111 完成
    PianK.checkTarget(filmName)
    #
    MeiJTT.checkTarget(filmName)

    print ('\n检查结束！')


# 程序入口
def entrance():
    # checkNewFilm('八佰')
    # MeiJx.run()
    Upload.main()


# 设置程序入口
if __name__ == '__main__':
    Knn.main()
    # entrance()
