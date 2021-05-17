[![Schedule - Renovate Helm Releases](https://github.com/ChristfriedBalizou/homelab/actions/workflows/renovate-schedule.yaml/badge.svg)](https://github.com/ChristfriedBalizou/homelab/actions/workflows/renovate-schedule.yaml)
[![Schedule - Update Flux](https://github.com/ChristfriedBalizou/homelab/actions/workflows/flux-schedule.yaml/badge.svg)](https://github.com/ChristfriedBalizou/homelab/actions/workflows/flux-schedule.yaml)


# homelab

<p align="center">
  <img src="https://i.imgur.com/EXNTJnA.png" alt="kubernetes home logo" width="150" align="center" />
  <br/><br/>
  <b>My home self hosted K3s cluster</b>
</p>

## Installing


1. Installing the primary node

```bash
k3sup install \
    --host=<host> \
    --user=<user> \
    --k3s-version=v1.21.1+k3s1 \
    --k3s-extra-args="--disable servicelb --disable traefik"
```

2. Join workers nodes

```bash
k3sup join \
    --host=<host> \
    --server-host=<host> \
    --k3s-version=v1.21.1+k3s1 \
    --user=<user> \
```

## :handshake:&nbsp; Acknowledgement

I learned from people who shared their clusters configuration [home-ops](https://github.com/Diaoul/home-ops)
and from the [template-cluster-k3s](https://github.com/k8s-at-home/template-cluster-k3s/) repository.
