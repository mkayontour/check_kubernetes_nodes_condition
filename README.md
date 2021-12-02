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
object CheckCommand "kubernetes_node_conditions" {
  command = [ PluginDir + "/check_node_conditions.py" ]

  arguments = {
    "--kube-config" = {
      "value" = "$kubernetes_node_conditions_kubeconfig$"
    }
  }
}
```
