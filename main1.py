import yaml
with open("yamfile1.yml", "r") as f:
    var_yamlfile = yaml.load(f, Loader=yaml.SafeLoader)
    print(var_yamlfile)