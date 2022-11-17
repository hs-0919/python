# 가수 한 명을 탄생!

# import pack2.pack024
from pack2.class4 import SingerType

def process():
    
    youngwoung = SingerType()
    print('영웅의 타이틀 송 : ', youngwoung.title_song)
    youngwoung.sing()

def process2():
    bts = SingerType()
    bts.sing()
    bts.title_song = 'yet to come'
    bts.sing()
    bts.co = 'HIVE'
    print('소속사:', bts.co)
    print()
    blackPink = SingerType()
    blackPink.title_song='셧다운'
    blackPink.sing()
    # print('소속사:', blackPink.co) -> err
    
# process()

if __name__ == '__main__':
    process()
    print('------')
    process2()

