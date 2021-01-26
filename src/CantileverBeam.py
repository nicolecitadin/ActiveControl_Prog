import numpy as np
from scipy import linalg


class CantileverBeam:
    """
    Classe que implementa o modelo baseado em elementos finitos para a
    simulação de uma viga engastada
    """

    # Parâmetros gerais
    m = 1  # massa: sempre 1 para todas as vigas

    def __init__(self, npoints, width, thickness, lenght, density, elasticmod, Tsampling, 
                nmodes=5, damp=[0.002, 0.002, 0.001, 0.001, 0.001], forcescaler=1, noisestd=0):
        """
        Construtor da classe. Os parâmetros já tem valores padrão relacionados com os valores de referência da viga utilizada.
            - npoints: número de partes no modelo por elementos finitos (quanto maior, mais detalhada e complexa a simulação);
            - width: largura da viga em metros;
            - thickness: espessura da viga em metros;
            - length: comprimento da viga em metros;
            - density: densidade da viga;
            - elasticmod: módulo de elasticidade em Pa, depende do material da viga.
            - Tsampling: período de amostragem utilizado na simulação (em segundos)
            - nmodes: número de modos de vibração simulados;
            - damp: fator de amortecimento para cada modo (tipicamente determinado experimentalmente);
            - noisestd: desvio padrão do ruído de medição.
        """
        self.Ts = Tsampling
        self.npoints = npoints
        self.nmodes = nmodes
        self.width = width
        self.thickness = thickness
        self.lenght = lenght
        self.density = density
        self.elasticmod = elasticmod
        self.forcescaler = forcescaler  # Permite definir um 'scaler' para força, simulando por exemplo uma conversão de Volts para 
                                        # Newton caso a força seja gerada a partir de uma tensão elétrica
        self.forcescaler1 = forcescaler
        self.magnetdist = 1e-3
        self.evaluateModesAndFreqs()
        self.memiir = 3
        self.Fs = 1 / self.Ts 
        self.wn = 2 * np.pi * self.freqsHz  # Undamped natural frequency
        self.zeta = np.array(damp)
        self.wd = self.wn * np.sqrt(1-self.zeta[:self.nmodes]**2)  # Damped natural frequency
        self.Aiir = np.zeros((self.nmodes, self.memiir-1))  # Coeficientes dos denominadores dos IIRs de cada modo
        self.Biir = np.zeros((self.nmodes, self.memiir))  # Coeficientes dos numeradores dos IIRs de cada modo

        # Cálculo dos coeficientes dos filtros IIR
        for k in range(0, self.nmodes):
            self.Biir[k,0] = 0
            self.Biir[k,1] = np.exp(-self.zeta[k]*self.wn[k]*self.Ts) * np.sin(self.wd[k]*self.Ts)
            self.Biir[k,2] = 0
            self.Aiir[k,0] = -2 * np.exp(-self.zeta[k]*self.wn[k]*self.Ts) * np.cos(self.wd[k]*self.Ts)
            self.Aiir[k,1] = np.exp(-2*self.zeta[k]*self.wn[k]*self.Ts)
        
        self.reset()
        self.noisestd = noisestd
        self.setaccelg(False)

    def evaluateModesAndFreqs(self):
        """
        Cálculo dos modos de vibração e das frequências de ressonância.
        """
        I = (self.width * self.thickness**3) / 12 # Inertial moment
        beam_mass = self.density * self.width * self.thickness * self.lenght
        # Mass matrix
        M = np.matrix(np.eye(self.npoints) * (beam_mass/self.npoints))
        M[0,0] = M[0,0]/2 
        deltax = self.lenght / self.npoints
        A = np.zeros((self.npoints, self.npoints))
        for r in range(self.npoints):
            for c in range(r+1):
                k = self.npoints - r
                l = self.npoints - c
                A[r,c] = ((deltax**3)/(6*self.elasticmod*I)) * (3* k**2 * l - k**3)
                A[c,r] = A[r,c]
        K = linalg.inv(A)
        L = linalg.cholesky(M)
        Kt = linalg.inv(L.T) @ K @ linalg.inv(L)
        ww, P = linalg.eig(Kt)
        ww =  np.real(ww)
        sidxs = np.argsort(ww) 
        U = linalg.inv(L) @ P
        self.vmod = np.zeros((self.npoints, self.nmodes))
        self.freqsHz = np.zeros(self.nmodes)
        for k in range(self.nmodes):
            self.vmod[:,k] = U[::-1,sidxs[k]]
            self.freqsHz[k] = np.sqrt(ww[sidxs[k]])/2/np.pi

    def configforcescaler(self, forcescl, magnetdist=1e-3):
        """
        Permite configurar um *force scaler* relacionado também com a distância do atuador magnético em relação à viga,
        sabendo que a força é reduzida com o quadrado da distância. Pode ser necessário reavaliar a precisão desta etapa.
        """
        self.forcescaler1 = forcescl
        self.forcescaler = forcescl / ((magnetdist * 1000) ** 2)
        self.magnetdist = magnetdist
    
    def setforce(self, pos, val):
        """
        Seta a força aplicada à viga considerando o forcescaler
        """
        self.f[pos] = self.forcescaler * val

    def setforcenl(self, pos, val):
        """
        Tentativa de simular o comportamento não linear na aplicação da força à viga, considerando que a força é
        proporcional ao quadrado da distância entre o atuador e a viga
        """
        self.f[pos] = self.forcescaler1 * val / (((self.magnetdist + self.x[pos]) * 1000) ** 2)
    
    def setaccelg(self, val):
        """
        Define a saída de aceleração em g (True) ou m/s^2 (False)
        """
        if val:
            self.getaccel = self.getaccelg
        else:
            self.getaccel = self.getaccelms2
    
    def getaccelms2(self, pos):
        """
        Retorna o valor da aceleração em m/s^2.
        """
        return self.a[pos] + np.random.randn()*self.noisestd
    
    def getaccelg(self, pos):
        """
        Retorna o valor da aceleração em g.
        """
        return (self.a[pos] + np.random.randn()*self.noisestd)/9.80665
    
    def reset(self):
        """
        Reseta a viga para o estado de repouso.
        """
        self.f = np.zeros(self.npoints)
        self.x = np.zeros(self.npoints)
        self.a = np.zeros(self.npoints)
        self.xiir = np.zeros((self.npoints, self.memiir))
        self.yiir = np.zeros((self.npoints, self.memiir))
        self.bufdesloc = np.zeros(self.npoints)
        self.bufvel = np.zeros((self.npoints, 2))
    
    def update(self):
        """
        Atualiza a viga após a aplicação de uma força, para o próximo passo de tempo.
        """
        self.bufvel[:,1] = self.bufvel[:,0]
        self.bufdesloc[:] = self.x
        self.x = np.zeros(self.npoints)
        for k in range(0, self.nmodes):
            self.xiir[k, 1:self.memiir] = self.xiir[k, 0:self.memiir-1]
            self.xiir[k,0] = self.vmod[:,k] @ self.f
            self.yiir[k,1:self.memiir] = self.yiir[k,0:self.memiir-1]
            self.yiir[k,0] = (self.Biir[k,:] @ self.xiir[k,:] - self.Aiir[k,:] @ self.yiir[k,1:self.memiir])
            self.x = self.x + self.Ts / (self.m*self.wd[k]) * self.yiir[k,0] * self.vmod[:,k]
        self.bufvel[:,0] = (self.x - self.bufdesloc) * self.Fs
        self.a = (self.bufvel[:,0] - self.bufvel[:, 1]) * self.Fs