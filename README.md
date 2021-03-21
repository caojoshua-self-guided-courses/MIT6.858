# MIT 6.858 Computer Systems Security

Self learning of [MIT 6.858 Computer Systems Security from MIT Open Courseware](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-858-computer-systems-security-fall-2014/index.htm). This course is suitable for self learning because it provides labs, lecture videos, readings and more.

## Organization
This repository is forked from the original repo (git://g.csail.mit.edu/6.858-lab-2014) and contains the 6 lab assignments.
* The [main branch](https://github.com/caojoshua/MIT6.858/) holds lab1 and lab2
* The [lab3 branch](https://github.com/caojoshua/MIT6.858/tree/lab3) holds lab3
* The [lab5 branch](https://github.com/caojoshua/MIT6.858/tree/lab5) holds lab5
* The [lab6 branch](https://github.com/caojoshua/MIT6.858/tree/lab6) holds lab6

The latest commit of each branch holds the final solution of the lab. I skipped lab4 because it only involves writeups of theoretical exploits.

## Setup
The labs are run on the VM image provided on the course website. The VM can be run in many ways. For example, course suggests VMware.

I will be running the VM on Fedora Linux KVM/QEMU. This requires some dependencies that varies depending on your Linux distro, so look it up. The following details the rest of the setup.

First `cd` into the directory with the VM artifacts. To boot the VM
```
qemu-kvm -m 512 -net nic -net user,hostfwd=tcp:127.0.0.1:2222-:22,hostfwd=tcp:127.0.0.1:8080-:8080 vm-6858.vmdk -fsdev local,path=</path/to/host/folder>,security_model=none,id=fsdev0 -device virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=hostshare
```
This sets up port forwarding for ssh and the web server. It also sets up file sharing with the host OS, such that both the host and guest can access `</path/to/host/folder>`. This is optional, but is convenient for editing from a local text editor.

To ssh into the host
```
ssh -p 2222 httpd@localhost
```
And enter password `6858`.

Once in the guest, you can access the shared folder with
```
sudo mount -t 9p -o trans=virtio,version=9p2000.L hostshare <path/to/folder>
```
The shared folder will be visible at `<path/to/folder>`. Recommended path is `/home/httpd/lab`
