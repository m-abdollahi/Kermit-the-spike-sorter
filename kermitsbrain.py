class Kermit():
    def __init__(self,database,random_sead):
        self.database = database
        self.random_sead = random_sead
        self.errors = []
        
        
    def Normalize(self):
        self.data = MinMaxScaler()
        return self.data.fit_transform(self.database)
        
            
    def PCA(self,data,n_component):
        self.datapca = PCA(n_components=n_component,random_state=self.random_sead)
        return self.datapca.fit_transform(data)

                
    def ICA(self,data,n_component):
        self.dataica = ICA(n_components=n_component,random_state=self.random_sead)
        return self.dataica.fit_transform(data)
    
    def FactorAnalysis(self,data,n_component):
        self.datafactoranalysis = FactorAnalysis(n_components=n_component,random_state=self.random_sead)
        return self.datafactoranalysis.fit_transform(data)
    
    def AE(self,data,batch_size,shuffle=True,num_workers=0):
            self.features = []
            self.outputs = []
            print("Creating Datasets...")
            class spikedataset(Dataset):
                def __init__(self,transform=None):
                    #dta loading
                    self.wawes =  torch.tensor(data).type('torch.FloatTensor')
                    self.len_samples = len(self.wawes)
                    self.features_samples = len(self.wawes[0])
                    self.transform = transform
                    print(type(self.wawes))
                
                def __getitem__(self,index):
                    #getting item and indexing
                    sample = self.wawes[index]
                    if self.transform:
                        sample = self.transform(sample)
                    return sample
                        
                    
                def __len__(self):
                    #number of samples
                    return self.len_samples
                
            gg = spikedataset()
            dataloader = DataLoader(dataset=gg,batch_size=batch_size,shuffle=shuffle,num_workers=num_workers)
            
            print("########### Dataset Loaded! ########### ")
            print("########### Creating Deep Autoencoder Model... ###########")
            class Autoencoder(nn.Module):
                    def __init__(self):
                        super().__init__()
                        #shape of Data from N to V 
                        self.encoder = nn.Sequential(
                            nn.Linear(48,32),
                            nn.ReLU(),
                            nn.Linear(32,16),
                            nn.ReLU(),
                            nn.Linear(16,2),
                            
                        )
                        #Shape of Data from V to N
                        self.decoder = nn.Sequential(
                            nn.Linear(2,16),
                            nn.ReLU(),
                            nn.Linear(16,32),
                            nn.ReLU(),
                            nn.Linear(32,48),
                            nn.Sigmoid()
                            
                        )
                    
                    
                    def forward(self, x):
                        encoded = self.encoder(x)
                        decoded = self.decoder(encoded)
                        return encoded,decoded
                # NOTE : [-1 -> 1] -> tanh function
            print("########### Model Created ###########")
            model = Autoencoder()
            criterion = nn.MSELoss()
            optimizer = optim.Adam(model.parameters(),lr=1e-3) #weight_decay=1e-5
            num_epochs = 60
            print("########### Start Training ... ########### ")
            for epoch in range(num_epochs):
                for (step,spikes) in enumerate(dataloader):
                    recon_encod,recon_decode = model(spikes)
                    loss = criterion(recon_decode,spikes)
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()
                    
                print(f'Epochs: {epoch+1}, Loss: {loss.item():.4f}')
                self.outputs.append((epoch,spikes.detach().numpy(),recon_decode.detach().numpy()))
                self.features.append((epoch,recon_encod.detach().numpy()))
            return self.outputs , self.features
    def KNN(self,data,k_max_number):
        
        for i in range(k_max_number):
                X = data
                model = KMeans(n_clusters=i+1)
                # fit the model
                model.fit(X)
                # assign a cluster to each example
                yhat = model.predict(X)
                # retrieve unique clusters
                clusters = unique(yhat)
                cent = model.cluster_centers_
                
                error=[]
                
            
                for ii in clusters:
                    for i in range(len(zz[yhat==ii])):
                        temp = []
                        gg =(zz[yhat==ii][i][0]-cent[ii][0])**2 + (zz[yhat==ii][i][1]-cent[ii][1])**2
                        temp.append(gg)
                        
                    error.append(np.sum(temp))
                #print(np.sum(error))
                self.errors.append(np.sum(error))
        print(f'Number of Neurons: {np.argmin(self.errors)+1}')
                
        
