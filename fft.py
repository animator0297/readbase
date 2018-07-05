from struct import *
#from numeric import *
import numpy as np
from matplotlib import pyplot
plt=pyplot

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as py
import plotly.graph_objs as go
from plotly import tools


plt=pyplot 
class readbase:

    def __init__(self):
        self.data = []
        self.fname='r2182a_182-0503a_bvzv.base'
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
        self.data += [time,year,day,hour,min,sec,sample]



        self.doc=np.zeros((time,channel,spectrum),dtype=np.complex)
        print self.doc.shape
        for i in range(time):
            for j in range(channel):
                for k in range(spectrum):
                    self.doc[i,j,k]=complex(unpack('f', self.fh.read(4))[0],\
                                            unpack('f', self.fh.read(4))[0])
        self.corr=self.doc[:,3,1021]
        print self.corr
        #self.h=abs(np.fft.fftshift(np.fft.ifft2(self.corr, axes=(-1,-2))))
        self.h=abs(np.fft.ifft2(self.corr))
        plt.plot(self.h)
        plt.show()

        #data = [go.Surface(z=self.h)]
        #layout=go.Layout(title='delays',xaxis=dict(title='delays'),yaxis=dict(title='accumulation periods'))
        #fig = go.Figure(data=data, layout=layout)
        #py.plot(fig)

        
       
        #        fig.colorbar(surf, shrink=0.5, aspect=10)
       

       