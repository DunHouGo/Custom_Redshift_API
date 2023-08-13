# Redshift-custom-API-for-Cinema-4D（Deprecated）
> This library has been discontinued for maintenance. Please skip to the latest version on [renderEngine](https://github.com/DunHouGo/renderEngine)

Custom API for Redshift in Cinema 4D

[Cinema 4D SDK Reference](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/index.html)

## Authors
- [DunHou](https://github.com/DunHouGo) - Original Author
- [HerzogVonWiesel](https://github.com/HerzogVonWiesel) (Jérôme Stephan)

## Files
  
### `Redshift IDs`
Makes it easier to reference Maxon Asset IDs for Redshift nodes and ports


### `Redshift Nodes`
Custom Functions to modify Redshift shader nodes in Node Editor more easily


### `Redshift API Examples`
Some examples showing how to use this custom API


## Important Notes
- ### This API is designed to be used only with Redshift Node Materials.

## Getting Started
- Download the repository and place its files in your Cinema 4D python library folder.
  - Windows: `C:\Users\USERNAME\AppData\Roaming\MAXON\CINEMA 4D VERSION\python310\libs\`
  - Mac: `/Users/USERNAME/Library/Preferences/MAXON/CINEMA 4D VERSION/python310/libs/`
- You can then use it by calling the modules in your python scripts.
  - `import redshift_node as rs`
  - `import redshift_ID as rsID`
- Every modification has to be done within a transaction
  - `with rs.MaterialTransaction(redshiftMaterial) as transaction:`
- Often you will need the Node ID of a given node. You can either use the Redshift IDs file or get it manually by searching for the node in the commander, showing its details, and copying the ID from the upper right "#" of the details window.
- Often you will need the Port ID of a port on a given node. For the Standard Material they can also be found in the Redshift IDs file. To get them for other nodes you can use the `.GetInputPortNames(node)` and `.GetOutputPortNames(node)` functions.
- I strongly recommend looking at the examples to get a better understanding of how to use this API, as well as my `import_textures.py` and `import_textures_from_base.py` scripts in my [CG_Scripts](https://github.com/HerzogVonWiesel/CG_Scripts) repository which depend heavily on this API to get a more in-depth look at how to use it.
