<h1 align="center">
  My Home Kubernetes Cluster
  <br />
  <br />
  <img src="https://i.imgur.com/4l9bHvG.png" alt="ansible logo" width="150" />
  <img src="https://raspbernetes.github.io/img/logo.svg">
</h1>
<br />
<div align="center">

[![Discord](https://img.shields.io/badge/discord-chat-7289DA.svg?maxAge=60&style=plastic&logo=discord)](https://discord.gg/DNCynrJ) [![k3s](https://img.shields.io/badge/k3s-v1.21.7-blue?style=plastic&logo=kubernetes)](https://k3s.io/) [![GitHub last commit](https://img.shields.io/github/last-commit/christfriedbalizou/homelab?color=purple&style=plastic)](https://github.com/christfriedbalizou/homelab/commits/main) [![Lint](https://github.com/ChristfriedBalizou/homelab/actions/workflows/lint.yaml/badge.svg)](https://github.com/ChristfriedBalizou/homelab/actions/workflows/lint.yaml) [![pre-commit](https://github.com/ChristfriedBalizou/homelab/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/ChristfriedBalizou/homelab/actions/workflows/pre-commit.yml)

</div>

---

## :telescope:&nbsp; Overview
This repo is my home Kubernetes cluster declared using yaml files and contains everything I use to setup my cluster. The Kubernetes flavor I use is [k3s](https://k3s.io) to keep the size to a minimum. I use [Flux](https://fluxcd.io) to watch this repo and deploy any changes I push here. Each folder represents a different namespace. Visit my [ansible](provision/ansible/) to see how I setup my cluster.

## :computer:&nbsp; Hardware

| Device              | Count | Memory    | Role           | Storage             | Notes                                      |
|:-------------------:|:-----:|:---------:|:--------------:|:-------------------:|:------------------------------------------:|
| Ιntel Celeron J4125 |   1   |  4GB DDR4 |   K3s master   |    128GB M.2 SSD    |  1TB SSD plugged in to provide nfs storage |
| Ιntel Celeron J4125 |   1   |  8GB DDR4 |   K3s worker   |    128GB M.2 SSD    |  2TB SSD plugged in to provide nfs storage |
| Raspberry Pi 4B     |   1   |    4GB    |   K3s worker   |        64GB         |                                            |

And some standby Rasbpberry Pi's 4B awaiting resurection when needed!

## :handshake:&nbsp; Thanks
I learned a lot from the people that have shared their clusters over from
[template-cluster-k3s](https://github.com/k8s-at-home/template-cluster-k3s/) and [Diaoul home-ops](https://github.com/Diaoul/home-ops) mainly [onedr0p](https://github.com/onedr0p/k3s-gitops)
and from the [k8s@home discord channel](https://discord.gg/DNCynrJ).
