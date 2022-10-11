# 상속

class ElecProduct:
    volume = 0
    
    def volumeControl(self, volume):
        pass
    
    

class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        self.volume += volume
        print('TV소리 크기: ', self.volume)

class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        imsi = self.volume + volume
        self.volume = imsi
        
        print('ElecRadio 크기는: ', self.volume)
        
tv = ElecTv()
radio = ElecRadio()

abc = tv
abc.volumeControl(3)

abc = radio
abc.volumeControl(3)
        
        
        