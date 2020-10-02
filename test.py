import yaml
import pprint

with open('anchors_references.yml') as f:
    pprint.pprint(yaml.load(f, Loader=yaml.FullLoader))
