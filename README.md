# Kubernetes Nodes condition

This check will provide health information for every node condition.

## Installation

Make sure that kubernetes for python is installed.


```
pip install kubernetes
```

Copy the file to your plugin directory in Icinga 2 or Nagios.

```
cp check_kubernetes_nodes_condition.py /usr/lib/nagios/plugins/
```

Add CheckCommand definition:

```
object CheckCommand "kubernetes_nodes_condition" {
  command = [ PluginDir + "/check_kubernetes_nodes_condition.py" ]

  arguments = {
    "--kube-config" = {
      "value" = "$kubernetes_nodes_condition_kubeconfig$"
    }
  }
}
```

### Example:

```
/usr/lib/nagios/plugins/check_kubernetes_nodes_condition.py --kube-config /etc/icinga2/kubeconfig.yml
Node: shoot--dk8sl1kzom--test-worker-yzhj-z1-dsm2-jhpq8
  [OK] FrequentUnregisterNetDevice: node is functioning properly
  [OK] FrequentKubeletRestart: kubelet is functioning properly
  [OK] FrequentDockerRestart: docker is functioning properly
  [OK] FrequentContainerdRestart: containerd is functioning properly
  [OK] KernelDeadlock: kernel has no deadlock
  [OK] ReadonlyFilesystem: Filesystem is not read-only
  [OK] CorruptDockerOverlay2: docker overlay2 is functioning properly
  [OK] NetworkUnavailable: Calico is running on this node
  [OK] MemoryPressure: kubelet has sufficient memory available
  [OK] DiskPressure: kubelet has no disk pressure
  [OK] PIDPressure: kubelet has sufficient PID available
  [OK] Ready: kubelet is posting ready status
```
