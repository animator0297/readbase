from struct import *
#from numeric import *
import numpy as np
from matplotlib import pyplot
plt=pyplot 
class readbase:
    def __init__(self):
        self.data = []
        self.fname='ri2248_015-1957_bdbd.base'
        self.fh=None
            
    
    def opn(self):
        self.fh=open(self.fname, 'rb')

  
    def gethat(self):
        version=self.fh.read(8)
        self.data.append(version)
        session=self.fh.read(20)
        self.data.append(session)
        numberscan, =unpack('i',self.fh.read(4))
        self.data.append(numberscan)
        namescan=self.fh.read(20)
        self.data.append(namescan)
        idst1, =unpack('i',self.fh.read(4))
        self.data.append(idst1)
        namest1=self.fh.read(4)
        self.data.append(namest1)
        polariz1, =unpack('i',self.fh.read(4))
        self.data.append(polariz1)
        idst2, =unpack('i',self.fh.read(4))
        self.data.append(idst2)
        namest2= self.fh.read(4)
        self.data.append(namest2)
        polariz2, =unpack('i', self.fh.read(4))
        self.data.append(polariz2)
        channel, =unpack('i',self.fh.read(4))
        self.data.append(channel)
        spectrum, =unpack('i', self.fh.read(4))
        self.data.append(spectrum)
        time, =unpack('i', self.fh.read(4))
        year, =unpack('i', self.fh.read(4))
        day, =unpack('i', self.fh.read(4))
        hour, =unpack('i', self.fh.read(4))
        min, =unpack('i', self.fh.read(4))
        sec, =unpack('i', self.fh.read(4))
        sample, =unpack('i', self.fh.read(4))
        # self.data.append(time,year,day,hour,min,sec,sample)
        self.data += [time,year,day,hour,min,sec,sample]

    #def spectra(self):
       # self.data.time
        #self.data.channel
        #self.data.spectrum
        self.doc=np.zeros((time,channel,spectrum),dtype=np.complex)
        print self.doc.shape
        for i in range(time):
            for j in range(channel):
                for k in range(spectrum):
                    self.doc[i,j,k]=complex(unpack('f', self.fh.read(4))[0],\
                                            unpack('f', self.fh.read(4))[0])
        self.shear=self.doc[0,12,:]
        print self.shear
        plt.plot(self.shear)
        plt.show()                    
        #self.doc.append()
        


        


        


     

