# JupyterHub addon for Microk8s

## Usage

Please make sure you have `dns` addon enabled and a default `StorageClass` exists in your microk8s cluster.
For convenience, you can use

```sh
microk8s enable dns
microk8s enable hostpath-storage
```

To visit jupyterhub externally, you can enable `ingress` and `metallb` addons.

```sh
microk8s enable ingress
# the ip pool varies depending on your setup. see https://microk8s.io/docs/addon-metallb for more info
microk8s enable metallb:10.64.140.43-10.64.140.49
```

To use jupyterhub

```sh
# Add repo
microk8s addons repo add https://github.com/yuhuishi-convect/jhub-addon

# Enable jupyterhub
microk8s enable jupyterhub

# Alternatively you can provide a values.yaml to configure jupyterhub
# See https://zero-to-jupyterhub.readthedocs.io/en/latest/resources/reference.html for a comprehensive reference
microk8s enable jupyterhub -- -f /path/to/values.yaml

# to view the ip address to for the jupyterhub service
microk8s kubectl get svc -n jhub

# disable the addon
microk8s disable jupyterhub
```

## Configuration

You can supply a `values.yaml` to use with the addon by 

```sh
microk8s enable jupyterhub -- -f /path/to/values.yaml
```