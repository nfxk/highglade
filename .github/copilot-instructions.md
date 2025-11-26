# AI generation system prompt

## Project Overview

This repository contains the configuration of the infrastructure of the Highglade network.
It is a simple homelab setup with configurations for Talos.

## Folder Structure

- '/cluster/main/talos': Specific configuration for talos nodes.
- '/cluster/main/talos-examples': old configuration not used anymore but kept for personal reference.
- '/cluster/old': old configuration not used anymore but kept for personal reference.
- '/cluster/shared': contains shared configuration for all worker and controlplane nodes
- '/clusterconfig': This is where the configuration files for each Talos node will be generated to.
- '/kubernetes': configuration files for kubernetes resources
- '/kustomize': application configuration files for the kubernetes cluster
- '/patches': patches for talos nodes
- '/proxmox': folder specific to proxmox configuration
- '/scripts':

## Libraries and Frameworks

- Talosctl for managing kubernetes nodes.
- talhelper for generating configuration files.
- jinja for templating.
