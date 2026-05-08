**Week 7 Azure Blast Architecture**

This folder contains the architecture diagram for the upgraded demo path:

- `assessment1`-style raw SQL Python Web API built with Flask
- Python native database connections only, no ORM framework
- Flask is the web framework, not the ORM
- GitHub Actions for build and image publish
- AKS as the runtime target
- ArgoCD for GitOps sync
- Argo Rollouts for canary / blue-green release control
- Azure DB as the cloud database target, accessed through a native driver
- SQLite only for local demo / single-instance mode

Open `architecture.drawio` in diagrams.net / draw.io.

Suggested next step:
- I can now turn this into a concrete repo split: app repo, Helm/GitOps repo, and a Terraform deployment repo.
