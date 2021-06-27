# Kermit the Spike Sorter!
After his great performance in the Muppet Show, Kermit decided to change his major to Computational Neuroscience!
recently, for improve his resume, he works for free to **sort spikes** in your **waveform (LFP) data**!:green_heart:

> "Just because you haven't found your talent yet doesn't mean you don't have one."
> -Kermit the Frog
<img src="https://imgs.smoothradio.com/images/224735?width=2001&crop=16_9&signature=HYi0DRkOL9-KYx1njHQ5R1TzQeY=" alt="alt text" width="100" height="500">

# Kermit abilities ?
Kermit has lots of abilities, here you can see all of them:
***He will learn more!***
* **Normalizing:**
  *  Min-Max Scalar
* **Dimensionality reduction:**
  *  Principal Component Analysis
  *  Fast Independent Analysis
  *  AutoEncoder
  *  Factor Analysis 
* **Clustering:**
  * k-nearest neighbor
# How Kermit works ?
Kermitsbrain is an object oriented program(Check the Manual with sample data)
First you should install pre-require libraries!(you can find them in requierment.txt)
then start the kermit's brain by typing:
```javascript
Yourname = Kermit(data,random_sead)
```
Now you can implement your pipeline with different functions!(See table below for more details)
Here's all of Kermit's brain functions:
|   Name |      Class / Function      |  Parameters  |   Definitions |
|:---: |:-------------:|:---: |:---:|
| Kermit |  Class | database,random sead |data structure : should be N * M that N = trials and M = features. random_sead: a number for reproduce results |
| Normalize |    Function   |   -   |-|
| PCA | Function |    data,n_component    |n_component: number of new feature dimension   |
| FactorAnalysis | Function |    data,n_component    |n_component: number of new feature dimension   |
| AE | Function |    data, batch_size, n_component, shuffle, num_workers     |batch_size: number of your batches(sample/steps), n_component: number of new feature imension, shuffle: True or False, num_workers: parallel processing(0,1,2)|
| KNN | Function |    data, k_max_number     |k_max_number: number of starting clusters for test(read more detail below)|  

**After** aplying your functions by starting the K-NN function:
```javascript
Yourname.KNN(data,K_max_number)
```
you can see how many neuron do you have in your data!
* k_max_number: this functions contains 2 part:  
  * i) K-NN alghorithm that test different Clustering with testing along your k_max_number 
  * ii) Error alghorithm that measure different distance between group centeroid and each member of group, at the end the best fitted Clusterd data will select and you can see number of neurons






