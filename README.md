<h1 align="center">
  My Home Kubernetes Cluster
  <br />
  <br />
  <img src="https://i.imgur.com/4l9bHvG.png" alt="ansible logo" width="150" />
  <img src="https://raspbernetes.github.io/img/logo.svg">
</h1>
<br />
<div align="center">

[![Discord](https://img.shields.io/badge/discord-chat-7289DA.svg?maxAge=60&style=for-the-badge&logo=discord)](https://discord.gg/DNCynrJ) [![k3s](https://img.shields.io/badge/v1.30.3-blue?style=for-the-badge&logo=kubernetes)](https://k3s.io/) [![GitHub last commit](https://img.shields.io/github/last-commit/christfriedbalizou/homelab?color=purple&style=for-the-badge)](https://github.com/christfriedbalizou/homelab/commits/main) ![GitHub Release](https://img.shields.io/github/release/christfriedbalizou/homelab?style=for-the-badge&logo=dependabot)


</div>

---

## :telescope:&nbsp; Overview
This repo is my home Kubernetes cluster declared using yaml files and contains everything I use to setup my cluster. The Kubernetes flavor I use is [k3s](https://k3s.io) to keep the size to a minimum. I use [Flux](https://fluxcd.io) to watch this repo and deploy any changes I push here. Each folder represents a different namespace. Visit my [ansible](ansible/) to see how I setup my cluster.

## :computer:&nbsp; Hardware

| Device              | Count | Memory    | Role               | Storage                               |
|:-------------------:|:-----:|:---------:|:------------------:|:-------------------------------------:|
| Ιntel NUC7i7BNH     |   1   | 32GB DDR4 |   K3s controller   |    256GB M.2 SSD                      |
| Ιntel Xeon          |   1   | 64GB DDR4 |   K3s controller   |    256GB M.2 SSD                      |
| Intel NUC7i5BNH     |   1   | 16GB DDR4 |   K3s controller   |    256GB M.2 SSG                      |
| Intel NUC7i5BNH     |   1   |  8GB DDR4 |   K3s worker       |    256GB M.2 SSG                      |
| Ιntel Celeron J4125 |   2   |  8GB DDR4 |   K3s worker       |    128GB M.2 SSD                      |
| Synology NAS DS423+ |   1   |  2GB DDR4 |   Main storage     | 56TB(2x12TB + 2x16TB) SHR + 4TB cache |

And some standby Rasbpberry Pi's 4B awaiting resurection when needed!

## :handshake:&nbsp; Thanks
I learned a lot from the people that have shared their clusters over from
[template-cluster-k3s](https://github.com/k8s-at-home/template-cluster-k3s/) and [Diaoul home-ops](https://github.com/Diaoul/home-ops) mainly [onedr0p](https://github.com/onedr0p/k3s-gitops)
and from the [k8s@home discord channel](https://discord.gg/DNCynrJ).
