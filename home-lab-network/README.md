Home lab overview
This lab simulates a small, isolated network with two Ubuntu virtual machines acting as a server and client. The VMs run on a VirtualBox internal network with static IP addresses and no direct internet access.

What I configured
Set up two Ubuntu VMs on a VirtualBox Internal Network and configured static IP addresses for each host.

Verified connectivity using ICMP ping in both directions between the server and client.

Enabled the UFW firewall on both VMs with a default deny policy for incoming traffic and allowed only essential services (such as SSH).

Created separate non‑admin user accounts and applied system updates on both machines to practice basic system hardening.

## Network diagram

```mermaid
graph LR
  Client[Ubuntu Client\n192.168.10.11] -- ICMP/SSH --> Server[Ubuntu Server\n192.168.10.10]
  subgraph VirtualBox Internal Network (LabNet1)
    Client
    Server
  end
```
