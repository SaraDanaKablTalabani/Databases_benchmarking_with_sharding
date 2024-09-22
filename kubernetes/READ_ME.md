installation:

 curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64
 sudo install minikube-linux-arm64 /usr/local/bin/minikube

 sudo minikube version

sudo usermod -aG docker $USER

minikube start --driver=docker

links:

https://github.com/kubernetes/minikube/issues/9762

https://k3s.io/
