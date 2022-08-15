from typing import Optional
import c4d
import os
import sys
import maxon
# import custom redshift node material API
path = r"D:\MyAPI"
if path not in sys.path:
    sys.path.append(path)
import redshift_node as rs
import redshift_ID as rsID

StandardOutputPortString = rsID.PortStr.standard_outcolor
OutputSurfacePortString = rsID.PortStr.Output_Surface
roughness = rsID.PortStr.refl_roughness
base_color = rsID.PortStr.base_color
curvature_out = rsID.StrPortID("curvature", "out") # "com.redshift3d.redshift4c4d.nodes.core.curvature.out"
noise_out = rsID.StrPortID("maxonnoise", "outcolor") # "com.redshift3d.redshift4c4d.nodes.core.maxonnoise.outcolor"
color_correct_input = rsID.StrPortID("rscolorcorrection", "input") # "com.redshift3d.redshift4c4d.nodes.core.rscolorcorrection.input"
doc = c4d.documents.GetActiveDocument()

if rs.RedshiftNodeBased():

    #---------------------------------------------------------
    # Example 01
    # 创建材质
    # Standard Surface
    #---------------------------------------------------------

    def CreateStandard(name):
        redshiftMaterial = rs.CreateStandardSurface(name)
        doc.InsertMaterial(redshiftMaterial.material)
        doc.SetActiveMaterial(redshiftMaterial.material)


    #---------------------------------------------------------
    # Example 02
    # 新建节点 修改属性
    # Standard Surface
    #---------------------------------------------------------
    def AddandModify(name):

        redshiftMaterial = rs.CreateStandardSurface(name)

        # create the shader graph
        # modification has to be done within a transaction
        with rs.RSMaterialTransaction(redshiftMaterial) as transaction:

            # find brdf node (in this case : standard surface)
            standard_surface = redshiftMaterial.GetRootBRDF()

            # change a shader name
            redshiftMaterial.SetShaderName(standard_surface,'Changed Name')

            # add a new shader to gragh and connect to some port
            noise_node = redshiftMaterial.AddShader("maxonnoise")
            ramp_node = redshiftMaterial.AddRamp()
            cc_node = redshiftMaterial.AddColorCorrectTo(standard_surface,base_color)
            # connect a shader's port to another shader's port
            # AddConnection()[0] return node , [1] return True
            redshiftMaterial.AddConnection(noise_node, noise_out, cc_node[0], color_correct_input)

            # get data type
            print("roughness port type = {0}".format(redshiftMaterial.GetParamDataType(standard_surface,roughness)))
            # set shader value < date type >
            redshiftMaterial.SetShaderValue(standard_surface,roughness,maxon.Float64(1))

            #arnoldMaterial.AddtoDisplacement(standard_surface,StandardOutputPortID)

            # get some info
            print("standard_surface AssetID = {0}".format(redshiftMaterial.GetAssetId(standard_surface)))
            print("standard_surface ShaderID = {0}".format(redshiftMaterial.GetShaderId(standard_surface)))
            print("roughness Value = {0}".format(redshiftMaterial.GetShaderValue(standard_surface,roughness)))
            #connectioninfo = redshiftMaterial.GetConnections()
            #print("Connections = {0}".format(a))

            # change roughness value to 1
            port = standard_surface.GetInputs().FindChild(roughness)
            port.SetDefaultValue(maxon.Float64(1))


        # add the material to the scene
        doc.InsertMaterial(redshiftMaterial.material)
        doc.SetActiveMaterial(redshiftMaterial.material)
        return redshiftMaterial

    def ReadInfo(redshiftMaterial):
        # list connections
        print(" -------------------------")
        connections = redshiftMaterial.GetConnections()
        print(" number of connections: %d" % len(connections))





    if __name__ == '__main__':
        # --- 1 --- #
        CreateStandard("1.Standard Surface")
        # --- 2 --- #
        example2 = AddandModify("2.Modify Material")
        # --- 3 --- #
        #ReadInfo(example2)


    c4d.EventAdd()
else:
    c4d.gui.MessageDialog("Redshift Node Material is not Valuable")