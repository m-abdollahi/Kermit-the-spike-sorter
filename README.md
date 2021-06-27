# Kermit the Spike Sorter!
After his great performance in the Muppet Show, Kermit decided to change his major to Computational Neuroscience!
recently, for improve his resume, he works for free to **sort spikes** in your **waveform (LFP) data**!:green_heart:

> "Just because you haven't found your talent yet doesn't mean you don't have one."
> -Kermit the Frog
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
***data structure : should be N * M that N = trials and M = features.***

***random_sead: a number for reproduce results.***

Here's all of Kermit's brain functions:
|   Name |      Class / Function      |  Parameters  |
|:---: |:-------------:|:---: |
| Kermit |  Class | database,random sead |
| Normalize |    Function   |   -   |
| PCA | Function |    data,n_component    |
| ICA | Function |    data,n_component    |
| FactorAnalysis | Function |    data,n_component    |
| AE | Function |    data, batch_size, n_component, shuffle, num_workers     |
| KNN | Function |    data, k_max_number     |






