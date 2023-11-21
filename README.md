## ikido-github-action

This repository provides a GitHub Action for scanning PCB components with usage example

```yaml
name: Action
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  main:
    permissions: # Need to GitHub check managing adding report in the PR comments
      checks: write
      issues: write
      discussions: write
      pull-requests: write
      contents: read
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Run ikido-action
        uses: ikido-tech/ikido-github-action
        with :
          username: ${{ secrets.IKIDO_USERNAME }}
          # required: true
          # username used for authorization in IKIDO platform
          password: ${{ secrets.IKIDO_PASSWORD }}
          # required: true
          # password used for authorization in IKIDO platform
          project-path: './'
          # required: false
          # default: './'
          # Relative path to PCB project in the repo
```
Common example of usage you may find in `example/main.yaml`
