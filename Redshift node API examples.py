#=============================================
#                   Libs
#=============================================
from typing import Optional
import c4d
import os
import sys
import maxon
# import custom redshift node material API
path = r"K:\MyAPI" # custom path for api lib
if path not in sys.path:
    sys.path.append(path)
import redshift_node as rs
import redshift_ID as rsID
#=============================================
#           ID (auto completion)
#=============================================
StandardOutputPortString = rsID.PortStr.standard_outcolor
OutputSurfacePortString = rsID.PortStr.Output_Surface
roughness = rsID.PortStr.refl_roughness
base_color = rsID.PortStr.base_color
mix_input1 = rsID.StrPortID("rscolormix","input1")
mix_input2 = rsID.StrPortID("rscolormix","input2")
curvature_out = rsID.StrPortID("curvature", "out")                      # "com.redshift3d.redshift4c4d.nodes.core.curvature.out"
noise_out = rsID.StrPortID("maxonnoise", "outcolor")                    # "com.redshift3d.redshift4c4d.nodes.core.maxonnoise.outcolor"
color_correct_input = rsID.StrPortID("rscolorcorrection", "input")      # "com.redshift3d.redshift4c4d.nodes.core.rscolorcorrection.input"
doc = c4d.documents.GetActiveDocument()
#=============================================
#                  Examples
#=============================================
if rs.RedshiftNodeBased(): # 检测是否为Redshift Node Base

    #---------------------------------------------------------
    # Example 01
    # 创建材质
    # Standard Surface
    #---------------------------------------------------------

    def CreateStandard(name):
        # 创建Standard Surface材质
        redshiftMaterial = rs.CreateStandardSurface(name)
        # 将Standard Surface材质引入当前Document
        doc.InsertMaterial(redshiftMaterial.material)
        # 将Standard Surface材质设置为激活材质
        doc.SetActiveMaterial(redshiftMaterial.material)


    #---------------------------------------------------------
    # Example 02
    # 新建节点 修改属性
    # Modify Standard Surface
    #---------------------------------------------------------
    
    def AddandModify(name):

        redshiftMaterial = rs.CreateStandardSurface(name)
        
        # modification has to be done within a transaction
        with rs.RSMaterialTransaction(redshiftMaterial) as transaction:

            # find brdf node (in this case : standard surface)
            # 查找Standard Surface节点
            standard_surface = redshiftMaterial.GetRootBRDF()

            # change a shader name
            # 更改Standard Surface节点名称
            redshiftMaterial.SetShaderName(standard_surface,'Changed Name')

            # add a new shader to gragh and connect to some port
            # 添加shader
            noise_node = redshiftMaterial.AddShader("maxonnoise")
            color_mix_node = redshiftMaterial.AddShaderTo("rscolormix", rsID.StrPortID("rscolormix","outcolor"), standard_surface, base_color)
            ramp_node = redshiftMaterial.AddRamp()
            cc_node = redshiftMaterial.AddColorCorrectTo(color_mix_node,mix_input1)
            # connect a shader's port to another shader's port
            # 添加链接
            redshiftMaterial.AddConnection(noise_node, noise_out, color_mix_node, mix_input2)

            # get data type
            # 获取端口类型
            print("roughness port type = {0}".format(redshiftMaterial.GetParamDataType(standard_surface,roughness)))
            # set shader value < date type >
            # 设置端口属性
            redshiftMaterial.SetShaderValue(standard_surface,roughness,maxon.Float64(1))
            # get connections
            # 获取链接
            connectioninfo = redshiftMaterial.GetAllConnections()
            # get some info
            # 查看属性
            print("standard_surface AssetID = {0}".format(redshiftMaterial.GetAssetId(standard_surface)))
            print("standard_surface ShaderID = {0}".format(redshiftMaterial.GetShaderId(standard_surface)))
            print("roughness Value = {0}".format(redshiftMaterial.GetShaderValue(standard_surface,roughness)))            
            print("Connections Num = {0}".format(len(connectioninfo)))
            for i, element in enumerate(connectioninfo):
                print(("Connections" + str(i) + "= {0}".format(connectioninfo[i])))

        # add the material to the scene
        # 将Standard Surface材质引入当前Document
        doc.InsertMaterial(redshiftMaterial.material)
        doc.SetActiveMaterial(redshiftMaterial.material)
        return redshiftMaterial


    if __name__ == '__main__':
        # --- 1 --- #
        CreateStandard("1.Standard Surface")
        # --- 2 --- #
        example2 = AddandModify("2.Modify Material")
        
    c4d.EventAdd()
    
else:
    c4d.gui.MessageDialog("Redshift Node Material is not Valuable")