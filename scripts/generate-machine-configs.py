# import yaml and jinja
import yaml
import os
from jinja2 import Template

print(os.getcwd())
with open(os.getcwd() + "/cluster/main/machines.yaml") as file:
    machines = yaml.safe_load(file)

with open(os.getcwd() + "/cluster/main/network.yaml") as file:
    network = yaml.safe_load(file)

# read your jinja template file
with open(os.getcwd() + "/cluster/main/controlplane.yaml.j2") as file:
    template = Template(file.read())

# iterate over the devices described in your yaml file
# and use jinja to render your configuration
for machine in machines["machines"]:
    print(
        template.render(
            machine=machine["name"],
            network=network["general"],
            dns=network["dns"],
        )
    )
