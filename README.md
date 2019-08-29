# bloodstained-castle-graph
NetworkX-based graph of the Bloodstained Castle movement requirements.

# Description:
This script attempts to generate a configuration of important progression shards/items by modeling the entire castle and requirements to move from one space to another.
The script randomly assigns the progression-important items/shards to different locations and repeatedly runs a breadt-first search on the graph to either determine that the configuration allows reaching the final boss or not.  Sounds silly but usually finds a solution with 1-5 attempts.

The graph uses nodes to represent different locations and edges to represent moving from one location to the next.  Nodes have data attached related to what is at that location, ie chests and mobs.  Edges have a boolean expression dictating what item(s) or shard(s) are required to make that transition.

This is very much incomplete!  Especially mob and chest data.  I've got 80% of the map done but will be making major tweaks as I find better ways to express the constraints within networkx.

# Usage:

```
python main.py  -h
usage: main.py

main.py

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Increase output verbosity
```

# Typical output:

Non-verbose:
```
Castle has 334 nodes
{'ENT19': 'Passplate', 'LIB13_1': 'CW', 'ICE10': 'DS', 'JPN14': 'INV', 'ENT3': 'BS', 'SAN7': 'RS', 'TAR7': 'ZANGETSUTO', 'GND2_L': 'DJ', 'KNG13': 'SILVER_BROMIDE', 'ARC2': 'HJ', 'ENT15': 'AP', 'KNG3': 'RR', 'TWR13': 'ACC'}
```

Verbose prints much more data about what progression keys are being considered and what nodes are visited in what order.
