# dataset-dinov2-container
Dinov2 ImageNet-1k requires the dataset to be in a very specific format, personally i run my machine learning clusters on kubernetes and within this repository are container images i have created to download and create the dataset in the format necessary for compatibility with the dinov2 code.
-clusterDatasetYAML: yaml code for dataset resource on cluster
-datasetCreationContainer: files used for creation of datasetCreation container image
-datasetCreationYAML: pod specifications that download the dataset from the internet in a streaming fashion
-datasetFinalContainer: files used for creation of datasetFinal container image
-datasetFinalYAML: pod specification that takes the downloaded files and formats them in the correct fashion

TO USE:
- replace clusterDatatasetYAML/minikubePV path with local path where you want the dataset to be downloaded
- create a configmap named hf-token that contains the key pair HF_TOKEN:"string of your huggingface access token"

'''bash
kubectl apply -f clusterDatasetYAML
kubectl apply -f datasetCreationYAML
#wait for all pod execution to complete, then
kubectl apply -f datasetFinalYAML
'''

NOTES
- the datasetCreation container performs the download, decompression and dearchiving in a streaming fashion, this implementation reduces greatly filesystem operation which i found very important when needing to access AWS EFS through a mount point (otherwise the bandwith iops would saturate). This is obviously a niche use case, but if you find yourself in a similar situation you can check out [].
- this version of the YAML files are for a local minikube implementation, some modification necessary to use them on AWS EKS 
- datasetFinal container is quite bulky because it not only requires pytorch due to facebook's implementation of their dataset formating code
