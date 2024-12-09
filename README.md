```
                __                 __    
  _____________/  |______ __  _  _|  | __
 /     \_  __ \   __\__  \\ \/ \/ /  |/ /
|  Y Y  \  | \/|  |  / __ \\     /|    < 
|__|_|  /__|   |__| (____  /\/\_/ |__|_ \
      \/                 \/            \/
```

## Setup
Install the `mrtawk` cli with pip inside this repository.\
For debugging and development purposes you can use `-e` to apply local code changes immediately.
```bash
pip3 install -e .
```

## Usage
`mrtawk` provides a CLI interface with some commands for querying MRT archives, initializing a new scenario, and appending MRTs to an existing scenario.\
All commands are chained commands, so you can append multiple commands to a single command.\
Also there are some global options that can be used with every command.
```
Options:
  -i, --mrt-input-path DIRECTORY
  -o, --scenario-output-path DIRECTORY
                                  [required]
```

### `mrtawk init`
To initialize a new scenario, you can use the `init` command.\
The command does not require any additional arguments.\
All necessary inputs are asked interactively.
```bash
mrtawk -o test_scenario_1 init
```

### `mrtawk append`
To append MRT archives to an existing scenario, you can use the `append` command.
```
Options:
  -s, --start-datetime [%Y-%m-%dT%H:%M:%S|%Y-%m-%dT%H:%M|%Y-%m-%d]
                                  [required]
  -e, --end-datetime [%Y-%m-%dT%H:%M:%S|%Y-%m-%dT%H:%M|%Y-%m-%d]
                                  [required]
  -v, --vendor [lw]               [default: lw; required]
  -p, --peer-name [amsix|decix|franceix|linx|marseix|mskix|nlix|swissix|chinatel|cogent|dtag|gtt|hurricane|level3|ntt|pccw|rostel|seabone|swisscom|telia]
                                  [default: decix; required]
  -b, --bgp-type [rib|update]     [default: update; required]

```

### `mrtawk query`
To query MRT archives, you can use the `query` command.
```
Options:
  -s, --start-datetime [%Y-%m-%dT%H:%M:%S|%Y-%m-%dT%H:%M|%Y-%m-%d]
                                  [required]
  -e, --end-datetime [%Y-%m-%dT%H:%M:%S|%Y-%m-%dT%H:%M|%Y-%m-%d]
                                  [required]
  -v, --vendor [lw]               [default: lw; required]
  -p, --peer-name [amsix|decix|franceix|linx|marseix|mskix|nlix|swissix|chinatel|cogent|dtag|gtt|hurricane|level3|ntt|pccw|rostel|seabone|swisscom|telia]
                                  [default: decix; required]
  -b, --bgp-type [rib|update]     [default: update; required]

```
