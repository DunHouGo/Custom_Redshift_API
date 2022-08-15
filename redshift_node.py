# Last Update 2022 08 11
#
# Custom Redshift API for Cinema 4D build S26.107 @Redshift 3.5.04
# 
#  on devlepment
#
#  Autor: DunHou


#=============================================
#                   Libs
#=============================================
import c4d
import maxon
import maxon.frameworks.nodespace
import maxon.frameworks.nodes
import maxon.frameworks.graph
#import os
#import sys
import redshift_ID as rsID # Commonly Used IDs for Redshift
#=============================================
#                   ID
#=============================================
StandardMaterialAssetID = rsID.ShaderID.StandardMaterial # maxon.Id("com.redshift3d.redshift4c4d.nodes.core.standardmaterial") # standard surface node
StandardOutputPortID = rsID.PortID.standard_outcolor # maxon.Id("com.redshift3d.redshift4c4d.nodes.core.standardmaterial.outcolor") # standard surface output
OutputMaterialAssetID = rsID.ShaderID.Output # maxon.Id("com.redshift3d.redshift4c4d.node.output") # Output node
OutputSurfacePortID = rsID.PortID.Output_Surface # maxon.Id("com.redshift3d.redshift4c4d.node.output.surface") # Output node surface
OutDisplacementPortID = rsID.PortID.Output_Displacement # maxon.Id("com.redshift3d.redshift4c4d.node.output.displacement") # Output node displacement

# not done yet in redshift_ID
ImageNodeID = maxon.Id("com.redshift3d.redshift4c4d.nodes.core.texturesampler") # texture node
ColorCorrectionNodeID = maxon.Id("com.redshift3d.redshift4c4d.nodes.core.rscolorcorrection") # color correct



VectorColorDataType = "net.maxon.parametrictype.col<3,float64>"
StandardOutputPort ="com.redshift3d.redshift4c4d.nodes.core.standardmaterial.outcolor"
OutputSurfacePort = "com.redshift3d.redshift4c4d.node.output.surface"

RS_NODESPACE = "com.redshift3d.redshift4c4d.class.nodespace" # node space
RS_MATERIAL_END_NODE = "com.autodesk.Redshift.material"
RS_SHADER_PREFIX = "com.redshift3d.redshift4c4d.nodes.core."

ID_PREFERENCES_NODE = 465001632 # Prefs ID
ID_REDSHIFT = 1036219 # Redshift

#=============================================
#              RedshiftMaterial
#=============================================
# 确认当前渲染器是Redshift 
# 且首选项设置为Node材质
doc = c4d.documents.GetActiveDocument()
def RedshiftNodeBased():
    """
    1.Check current Render Engine is Redshift
    2.Pereference Redshift material type is Node 

    Returns:
        Tuer: True
    """
    doc = c4d.documents.GetActiveDocument()
    RenderEngine = doc.GetActiveRenderData()[c4d.RDATA_RENDERENGINE]


    prefs = c4d.plugins.FindPlugin(ID_PREFERENCES_NODE)
    
    if not isinstance(prefs, c4d.BaseList2D):
        raise RuntimeError("Could not access preferences node.")

    # Redshift Node
    if RenderEngine == ID_REDSHIFT:        
        descIdSettings = c4d.DescID(
        c4d.DescLevel(1036220, 1, 465001632), # pref ID Redshift
        c4d.DescLevel(888, 133, 465001632)
        )
        # Set
        prefsset = prefs[descIdSettings]

        if prefsset[c4d.PREFS_REDSHIFT_USE_NODE_MATERIALS] == False: # Legacy
            #isNode = False
            return False

        elif prefsset[c4d.PREFS_REDSHIFT_USE_NODE_MATERIALS] == True: # Node
            #isNode = True
            return True

def RedshiftMaterial(material):
    """
    Creates an Redshift Material instance based on the type of the given BaseMaterial.

    Parameters
    ----------
    material : c4d.BaseMaterial
        BaseMaterial instance from the C4D document.
    """
    if material is None:
        return None

    if RedshiftNodeBased() == True:
        return RedshiftNodeMaterial(material)

    print("[WARNING] Material '%s' is not a Redshift Node Material" % material.GetName())
    return None

def GetActiveGraphModelRef() -> maxon.NodesGraphModelRef:
    """Returns the Nodes graph of the active document.
    """
    # Get the scene nodes scene hook.
    sceneNodesHook = doc.FindSceneHook(c4d.SCENENODES_IDS_SCENEHOOK_ID)
    if not sceneNodesHook:
        raise RuntimeError("Could not retrieve Scene Nodes scene hook.")

    # Get the scene nodes graph from the hook.
    sceneNodesHook.Message(maxon.neutron.MSG_CREATE_IF_REQUIRED)
    sceneNodes = sceneNodesHook.GetNimbusRef(maxon.neutron.NODESPACE)
    if not sceneNodes:
        raise RuntimeError("Could not retrieve Scene Nodes graph model.")

    graph = sceneNodes.GetGraph()
    if graph.IsReadOnly():
        raise RuntimeError("Scene Nodes graph is read only.")

    return graph

def GetActiveNodeGraph(dispaly=False):
    mat = doc.GetActiveMaterial()
    if mat is None:
        raise ValueError("Cannot get a Material")

    # Retrieve the reference of the material as a node Material.
    nodeMaterial = mat.GetNodeMaterialReference()
    if nodeMaterial is None:
        raise ValueError("Cannot retrieve nodeMaterial reference")

    nimbusRef = mat.GetNimbusRef(RS_NODESPACE)
    # print("nimbusRef " + str(nimbusRef))
    if nimbusRef is None:
        raise ValueError("Cannot retrieve the nimbus ref for that node space")

    # Retrieve the graph corresponding to that node space.
    graph = nimbusRef.GetGraph()
    if dispaly == True:
        print("graph " + str(graph))
        if graph is None:
            raise ValueError("Cannot retrieve the graph of this nimbus ref")
    return graph

# 创建Standard Surface
def CreateStandardSurface(name):
    """
    Creates a new Redshift Starndard Surface Material with a NAME.

    Args:
        name (str): Name of the Material

    Returns:
        Material: Redshift Material instance
    """
    #doc = c4d.documents.GetActiveDocument()
    standardMaterial = RedshiftNodeMaterial.Create(name)
    if standardMaterial is None or standardMaterial.material is None:
        raise Exception("Failed to create Redshift Standard Surface Material")

    with RSMaterialTransaction(standardMaterial) as transaction:
        oldrs = standardMaterial.GetRootBRDF()
        output = standardMaterial.GetRSOutput()
        standardMaterial.RemoveShader(oldrs)
        standard_surface = standardMaterial.AddShader("standardmaterial")
        standardMaterial.AddConnection(standard_surface,rsID.PortStr.standard_outcolor, output, rsID.PortStr.Output_Surface)
        
    #doc.InsertMaterial(standardMaterial.material)
    #doc.SetActiveMaterial(standardMaterial.material)
    return standardMaterial   

#=============================================
#          Simplyfy Redshift ID
#=============================================
# Str of node ID
# def StrNodeID(node_name):
#     redshift_pre = "com.redshift3d.redshift4c4d.nodes.core."
#     realID = redshift_pre + node_name
#     return realID
# # Str of port ID
# def StrPortID(node_name, port_name):
#     redshift_pre = "com.redshift3d.redshift4c4d.nodes.core"
#     realID = redshift_pre + node_name +  '.' + port_name
#     return realID
# # Make a str to maxon ID
# def StrtoMaxonID(ID_string):
#     realID = maxon.Id(str(ID_string))
#     return realID

#=============================================
#           Redshift Node Material
#=============================================

class RedshiftNodeMaterial:
    # 初始化 ==> OK
    def __init__(self, material):
        self.material = material
        self.graph = None
        self.nimbusRef = self.material.GetNimbusRef(RS_NODESPACE)
        #self.node = maxon.GraphNode # Type of 5 :[true node,  input port, output port, input port list, output port list]
        if self.material is not None:
            nodeMaterial = self.material.GetNodeMaterialReference()
            self.graph = nodeMaterial.GetGraph(RS_NODESPACE)
            if self.graph is None:
                print("[WARNING] Node space is not found in Node Material: %s" % self.material.GetName())

#===========================
#           新建
#===========================

    # 创建材质 ==> OK
    def Create(name):
        """
        Creates a new Redshift Node Material with a NAME.

        Parameters
        ----------
        name : str
            The Material entry name.

        """
        # Retrieve the selected baseMaterial
        material = c4d.BaseMaterial(c4d.Mmaterial)
        if material is None:
            raise ValueError("Cannot create a BaseMaterial")            
        material.SetName(name)
        # Retrieve the reference of the material as a node Material.
        nodeMaterial = material.GetNodeMaterialReference()
        if nodeMaterial is None:
            raise ValueError("Cannot retrieve nodeMaterial reference")
        # Add a graph for the redshift node space
        nodeMaterial.AddGraph(RS_NODESPACE)
        # Return a redshift node material
        return RedshiftNodeMaterial(material)
    # 创建Shader ==> OK 
    def AddShader(self, nodeId):
        """
        Adds a new shader to the graph.

        Parameters
        ----------
        nodeId : str
            The Redshift node entry name.
        name : str
            Name of the shader node.
        """
        if self.graph is None:
            return None

        shader = self.graph.AddChild("", "com.redshift3d.redshift4c4d.nodes.core." + nodeId, maxon.DataDictionary())

        return shader   
    # 创建Shader并连接到 ==> TO DO
    def AddShaderTo(self, shader_Id, source_port, target_node, target_port):
        
        """
        Adds a new shader to the given port of given node.

        Parameters
        ----------
        nodeId : str
            The Redshift node entry name.
        name : str
            Name of the shader node.
        """
        soure_node = self.AddShader(self, shader_Id)
        self.AddConnection(self, soure_node, source_port, target_node, target_port)
      # 创建Shader到连接线 ==> TO DO
    def AddShadertoConnection(slef, shader_id, in_port, out_port, connection):
        # to do
        pass  
    # ----- 常用shader ----- #
    # 创建Texture ==> TO DO
    def AddTexture(self,node_name,tex_path,color_space):
        # to do
        pass
    # 创建Texture并连接到 ==> TO DO
    def AddTextureTo(self, node_name, tex_path, color_space, target_node, target_port):

        # to do
        pass
    
    # 
    # 创建color correct ==> OK
    def AddColorCorrect(self):
        """
        Adds a new color correct shader to the graph.

        """
        if self.graph is None:
            return None
        nodeId = "rscolorcorrection"
        shader = self.graph.AddChild("", "com.redshift3d.redshift4c4d.nodes.core." + nodeId, maxon.DataDictionary())

        return shader 
    # 创建color correct并且链接到指定节点的指定端口 ==> OK
    def AddColorCorrectTo(self, targret_shader, targrt_port):
        node = self.AddColorCorrect()
        outPort = "com.redshift3d.redshift4c4d.nodes.core.rscolorcorrection.outcolor"
        return node,self.AddConnection(node, outPort, targret_shader, targrt_port) is not None
    def AddColorCorrectToConnection(self, targret_shader, targrt_port):
        node = self.AddColorCorrect()
        inPort = "com.redshift3d.redshift4c4d.nodes.core.rscolorcorrection.input"
        outPort = "com.redshift3d.redshift4c4d.nodes.core.rscolorcorrection.outcolor"
        return self.AddConnection(node, outPort, targret_shader, targrt_port) is not None
        
        pass
      
    # 创建ramp
    def AddRamp(self):
        """
        Adds a new ramp shader to the graph.

        """
        if self.graph is None:
            return None
        nodeId = "rsramp"
        shader = self.graph.AddChild("", "com.redshift3d.redshift4c4d.nodes.core." + nodeId, maxon.DataDictionary())

        return shader   
    # 创建maxon noise
    def AddMaxonNoise(self):
        """
        Adds a new maxonnoise shader to the graph.

        """
        if self.graph is None:
            return None
        nodeId = "maxonnoise"
        shader = self.graph.AddChild("", "com.redshift3d.redshift4c4d.nodes.core." + nodeId, maxon.DataDictionary())

        return shader   

    # 创建displacement
    def AddDisplacement(self):
        """
        Adds a new displacement shader to the graph.

        """
        if self.graph is None:
            return None
        nodeId = "displacement"
        shader = self.graph.AddChild("", "com.redshift3d.redshift4c4d.nodes.core." + nodeId, maxon.DataDictionary())

        return shader   
    # 创建texture 并通过displacement node链接到output的置换端口
    def AddTextureToDisplacement():
        pass



#===========================
#           获取
#===========================
    def GetPort(self):
        if self.graph is None:
            return None
        #port = self.graph.GetInputs().FindChild(real_port_name)


    # 获取端口
    def GetShaderPort(self, shader, port_name):
        """
        Adds a new shader to the graph.

        Parameters
        ----------
        shader : node
            The shader .
        port_name : str
            Name of the shader node.
        """
        if self.graph is None:
            return None

        real_port_name = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial." + port_name

        if isinstance(port_name, str):            
            port = shader.GetOutputs().FindChild(real_port_name)
            if not self.IsPortValid(real_port_name):
                print("[WARNING] Output port '%s' is not found on shader '%r'" % (port_name, shader))
                return

        real_port_name = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial." + port_name
        port = shader.GetInputs().FindChild(real_port_name)
        return port


    # 是否NodeBase
    def IsNodeBased(self):
        return True    
    # 端口合法 ==> OK
    def IsPortValid(self, port):
        """
        Checks if the FieldOutputBlock instance allocations and sizes are valid.
        """
        try:
            return port.IsValid()
        except Exception as e:
            return False 
    # 获取名称 ： 
    def GetNodeName(self, node, display=False):
        """
        Retrieve the displayed name of a node.
        Args:
            node: (maxon.GraphNode): The node to retrieve the name from.
            display: print info when display is True
        Returns:
            Optional[str]: The node name, or None if the Node name can't be retrieved.
        """
        if node is None:
            return None

        nodeName = node.GetValue(maxon.NODE.BASE.NAME)

        if nodeName is None:
            nodeName = node.GetValue(maxon.EffectiveName)

        if nodeName is None:
            nodeName = str(node)
        if display ==True :
            print(nodeName)
        return nodeName
    # 获取资产ID ==> OK tip:只有node有asset id
    def GetAssetId(self, shader, display=False):
        """
        Returns the asset id of the given shader.

        Parameters
        ----------
        shader : maxon.frameworks.graph.GraphNode
            The shader node.
        display: print info when display is True
        """
        res = shader.GetValue("net.maxon.node.attribute.assetid")
        assetId = ("%r"%res)[1:].split(",")[0]
        if display == True:
            print("AssetID = " + ("%r"%res)[1:].split(",")[0])
        return assetId
    # 获取ShaderID ==> OK  
    def GetShaderId(self, shader):
        """
        Returns the  node id of the given shader.

        Parameters
        ----------
        shader : maxon.frameworks.graph.GraphNode
            The shader node.
        """
        if shader is None:
            return None
    
        assetId = self.GetAssetId(shader,False)
        if assetId.startswith(RS_SHADER_PREFIX):
            return assetId[len(RS_SHADER_PREFIX):]
    
        return ""
    # 获取port数据类型 ==> OK
    def GetParamDataType(self, shader, paramId, display=False):
        """
        Returns the data type id of the given port.

        Parameters
        ----------
        shader : maxon.frameworks.graph.GraphNode
            The shader node.
        paramId : int
            Id of the parameter.
        display: print info when display is True
        """
        if shader is None or paramId is None:
            return None

        port = shader.GetInputs().FindChild(paramId)
        if not self.IsPortValid(port):
            return None   
        if display == True:
            print(port.GetDefaultValue().GetType().GetId())     
        return port.GetDefaultValue().GetType().GetId()
    # 获取属性 ==> OK  
    def GetShaderValue(self, shader, paramId, display=False):
        """
        Returns the value stored in the given shader parameter.

        Parameters
        ----------
        shader : maxon.frameworks.graph.GraphNode
            The shader node.
        paramId : int
            Id of the parameter.
        display: print info when display is True
        """
        if shader is None or paramId is None:
            return None

        # col<3,float64> data type
        # if self.GetParamDataType(shader, paramId) == VectorColorDataType:
        #     return shader.GetDefaultValue()

        # standard data type
        port = shader.GetInputs().FindChild(paramId)
        if not self.IsPortValid(port):
            print("[WARNING] Input port '%s' is not found on shader '%r'" % (paramId, shader))
            return None
        if display == True:
            print(port.GetDefaultValue()) 
        return port.GetDefaultValue()
    # 获取shader所有端口属性 
    def GetShaderValues(self, shader, paramId, display=False):
        # to do
        pass
    # 获取Output Surface ==> OK 
    def GetRSOutput(self):
        """
        Returns the Redshift material end node.
        """
        if self.graph is None:
            return None
        try:
            endNodePath = self.nimbusRef.GetPath(maxon.NIMBUS_PATH.MATERIALENDNODE)
            shader = self.graph.GetNode(endNodePath)
            return shader
        finally:
            for shader in self.GetShaders(False):
                if self.GetAssetId(shader) == OutputMaterialAssetID:
                    return shader
            return None    
    # 获取Output置换 
    def GetDisplacementRoot(self):
        """
        Returns the shader (maxon.frameworks.graph.GraphNode)
        connected to 'displacement' root port.
        """
        #return self.GetRootShader("displacement")
        if self.graph is None:
            return None

        endNode = self.GetRSOutput()
        root_port = endNode.GetInputs().FindChild(OutDisplacementPortID)
        if endNode is None:
            print("[WARNING] End node is not found in Node Material: %s" % self.material.GetName())
            return None
        for c in root_port.GetConnections(maxon.frameworks.misc.PORT_DIR.INPUT):
            outPort = c[0]
            src = outPort.GetAncestor(maxon.frameworks.graph.NODE_KIND.NODE)
            return src

        return None        
    # 获取Root BRDF ==> OK  BRDF:standard surface / rs material 
    def GetRootBRDF(self):
        """
        Returns the shader (maxon.frameworks.graph.GraphNode)
        connected to given root port.

        Parameters
        ----------
        rootPortId : int or str
            The root port id.
        """
        if self.graph is None:
            return None

        endNode = self.GetRSOutput()
        if endNode is None:
            print("[WARNING] End node is not found in Node Material: %s" % self.material.GetName())
            return None
        
        predecessor = list()
        maxon.GraphModelHelper.GetDirectPredecessors(endNode, maxon.NODE_KIND.NODE, predecessor)
        rootshader = predecessor[0] 
        if rootshader is None and not rootshader.IsValid() :
            raise ValueError("Cannot retrieve the inputs list of the bsdfNode node")
        #print(rootshader)
        return rootshader
    # 获取Shader贴图路径
    def GetShaderTexture(self):
        # to do
        pass
    # 获取选择node的子集
    def GetSelectNodeChildren():

        # Get the Active Material
        # ISSUE: It's possible to have the node editor editing a material even if its not active/selected (Asset Mode, Lock mode, etc)
        mat = doc.GetActiveMaterial()
        if mat is None:
            raise ValueError("There is no selected BaseMaterial")

        # Retrieve the reference of the material as a node Material.
        nodeMaterial = mat.GetNodeMaterialReference()
        if nodeMaterial is None:
            raise ValueError("Can't retrieve nodeMaterial reference")

        # Retrieve the graph corresponding to that nodeSpace.
        graph = nodeMaterial.GetGraph(RS_NODESPACE)
        if graph is None:
            raise ValueError("Can't retrieve the graph of this nimbus ref")

        with RSMaterialTransaction() as transaction:
            selected_nodes = []
            maxon.GraphModelHelper.GetSelectedNodes(graph, maxon.NODE_KIND.NODE, selected_nodes)
            predecessors = []
            for node in selected_nodes:
                maxon.GraphModelHelper.GetAllPredecessors(node, maxon.NODE_KIND.NODE, predecessors)
            for predecessor in predecessors:
                maxon.GraphModelHelper.SelectNode(predecessor)

        # Pushes an update event to Cinema 4D
        c4d.EventAdd()

#===========================
#           设置
#===========================

    # 设置节点名 ==> OK
    def SetShaderName(self,shader,name):
        """
        Set the name of the shader.

        Parameters
        ----------
        shader : maxon.frameworks.graph.GraphNode
            The shader node.
        name : name str
        """
        if shader is None:
            return None
        shadername = maxon.String(name)   
        shader.SetValue(maxon.NODE.BASE.NAME, shadername)
        shader.SetValue(maxon.EffectiveName, shadername)
    # 设置属性 ==> OK 注意数据类型 ： maxon.Float64(0.2) / maxon.Color64(1,0,0)
    # TO DO ： 增加判定，根据shader数据类型，标准化输入数据类型(maxon.type)
    def SetShaderValue(self, shader, paramId, value):
        """
        Sets the value stored in the given shader parameter.

        Parameters
        ----------
        shader : maxon.frameworks.graph.GraphNode
            The shader node.
        paramId : int
            Id of the parameter.
        value : [depends on the parameter]
            Parameter value.
        """
        if shader is None or paramId is None:
            return None

        # # vcolor custom data type
        # if self.GetParamDataType(shader, paramId) == VectorColorDataType:
        #     return shader.SetVColor(shader, paramId, value)

        # standard data type
        port = shader.GetInputs().FindChild(paramId)
        if not self.IsPortValid(port):
            print("[WARNING] Input port '%s' is not found on shader '%r'" % (paramId, shader))
            return None
    
        port.SetDefaultValue(value)

#===========================
#           操作
#===========================  
    # [private] shader list
    def _CollectShaders(self, node, shaders):
        """
        Private function to collect shaders from the graph.

        Parameters
        ----------
        node : maxon.frameworks.graph.GraphNode
            Graph node.
        shaders : list
            List of shaders.
        """
        if node.GetKind() != maxon.frameworks.graph.NODE_KIND.NODE:
            return

        if self.GetAssetId(node) == "net.maxon.node.group":
            for node in root.GetChildren():
                self._CollectShaders(node, shaders)
            return

        shaders.append(node)
    # 遍历shader ==> OK 
    def GetShaders(self,display=False):
        if self.graph is None:
            return []

        shaders = []

        root = self.graph.GetRoot()
        for node in root.GetChildren():   
            self._CollectShaders(node, shaders) 
            #shaders.append(node)
        #print(shaders)
        if display == True:
            print("Shaders Num : " + str(len(shaders)-2))
        return shaders
    # 删除Shader ==> OK 
    def RemoveShader(self, shader):
        """
        Removes the given shader from the graph.

        Parameters
        ----------
        shader : maxon.frameworks.graph.GraphNode
            The shader node.
        display: print info when display is True
        """
        if self.graph is None:
            return

        if shader is None:
            return

        shader.Remove()
    # 隐藏节点预览 ==> TO DO
    def MutePreview(ON=True):
        # to do
        pass
    # 暴露接口 ==> TO DO
    def ExposePort(On=True):
        pass

#===========================
#          连接线
#===========================  

    # 获取所有连接线 ==> OK 
    def GetConnections(self):
        """
        Returns the list of connections within this shader graph.
        A connection is a tuple of:
            source shader node : maxon.frameworks.graph.GraphNode
            source shader output port id : str
            target shader node : maxon.frameworks.graph.GraphNode
            target shader input port id : str
        """
        if self.graph is None:
            return []

        connections = []

        for shader in self.GetShaders():
            for inPort in shader.GetInputs().GetChildren():
                for c in inPort.GetConnections(maxon.frameworks.misc.PORT_DIR.INPUT):
                    outPort = c[0]
                    src = outPort.GetAncestor(maxon.frameworks.graph.NODE_KIND.NODE)
                    connections.append((src, outPort, shader, inPort))

        return connections
    # 获取当前node连接线 
    # 修改时使用，添加连接线后，需要在第二个RSMaterialTransaction获取
    def GetShaderConnection(self,shader):
        """
        Returns the list of connections of this shader.
        A connection is a tuple of:
            source shader node : maxon.frameworks.graph.GraphNode
            source shader output port id : str
            target shader node : maxon.frameworks.graph.GraphNode
            target shader input port id : str
        """
        if self.graph is None:
            return []

        connections = []
        
        for inPort in shader.GetInputs().GetChildren():
            for c in inPort.GetConnections(maxon.frameworks.misc.PORT_DIR.INPUT):
                outPort = c[0]
                src = outPort.GetAncestor(maxon.frameworks.graph.NODE_KIND.NODE)
                connections.append((src, outPort, shader, inPort))

        return connections
    # 获取当前port连接线 
    # 修改时使用，添加连接线后，需要在第二个RSMaterialTransaction获取
    def GetPortConnection(self,port):
        """
        Returns the list of connections of this shader.
        A connection is a tuple of:
            source shader node : maxon.frameworks.graph.GraphNode
            source shader output port id : str
            target shader node : maxon.frameworks.graph.GraphNode
            target shader input port id : str
        """
        if self.graph is None:
            return []

        connections = []        
        
        for c in port.GetConnections(maxon.frameworks.misc.PORT_DIR.INPUT):
            connections.append(c)
        return connections
    # 添加连接线 ==> OK 
    def AddConnection(self, soure_node, outPort, target_node, inPort):
        """
        Connects the given shaders in the graph.

        Parameters
        ----------
        src : maxon.frameworks.graph.GraphNode
            The source shader node.
        outPort : str
            Output port id of the source shader node.
        dst : maxon.frameworks.graph.GraphNode
            The target shader node.
        inPort : str
            Input port id of the target shader node.
        """
        if self.graph is None:
            return None

        if soure_node is None or target_node is None:
            return None

        if outPort is None or outPort == "":
            outPort = "output"

        if isinstance(outPort, str):
            outPort_name = outPort
            outPort = soure_node.GetOutputs().FindChild(outPort_name)
            if not self.IsPortValid(outPort):
                print("[WARNING] Output port '%s' is not found on shader '%r'" % (outPort_name, soure_node))
                outPort = None

        if isinstance(inPort, str):
            inPort_name = inPort
            inPort = target_node.GetInputs().FindChild(inPort_name)
            if not self.IsPortValid(inPort):
                print("[WARNING] Input port '%s' is not found on shader '%r'" % (inPort_name, target_node))
                inPort = None

        if outPort is None or inPort is None:
            return None

        outPort.Connect(inPort)
        return (soure_node, outPort, target_node, inPort)
    # 添加Output连接线 
    # to fix : TypeError: target should be a GraphNode
    def AddtoOutput(self, src, outPort):
        """
        Connects the given shader to the given root port.

        Parameters
        ----------
        src : maxon.frameworks.graph.GraphNode
            The source shader node.
        outPort : str
            Output port id of the source shader node.
        rootPortId : int or str
            The root port id.
        """
        endNode = self.GetRSOutput()        
        return self.AddConnection(src, outPort, endNode, OutputSurfacePortID) is not None
    # 添加Output连接线 
    # to fix : TypeError: target should be a GraphNode
    def AddtoDisplacement(self, src, outPort):
        """
        Connects the given shader to the given root port.

        Parameters
        ----------
        src : maxon.frameworks.graph.GraphNode
            The source shader node.
        outPort : str
            Output port id of the source shader node.
        rootPortId : int or str
            The root port id.
        """
        endNode = self.GetRSOutput()        
        return self.AddConnection(src, outPort, endNode, OutDisplacementPortID) is not None
    # 删除连接线
    def RemoveConnection(self, target_node, inPort):
        """
        Disconnects the given shader input.

        Parameters
        ----------
        dst : maxon.frameworks.graph.GraphNode
            The target shader node.
        inPort : str
            Input port id of the target shader node.
        """
        if self.graph is None:
            return None

        if target_node is None:
            return None

        if isinstance(inPort, str):
            inPort_name = inPort
            inPort = target_node.GetInputs().FindChild(inPort_name)
            if not self.IsPortValid(inPort):
                print("[WARNING] Input port '%s' is not found on shader '%r'" % (inPort_name, target_node))
                inPort = None

        if inPort is None:
            return None

        mask = maxon.frameworks.graph.Wires(maxon.frameworks.graph.WIRE_MODE.NORMAL)
        inPort.RemoveConnections(maxon.frameworks.misc.PORT_DIR.INPUT, mask)
    # 禁用连接线
    def MuteConnection(self, source_port, target_port, connection):
        def mute():
            if connection[maxon.Wires.INHIBIT] == maxon.WIRE_MODE.NORMAL:
                # Unmute the wire.
                connection[maxon.Wires.INHIBIT] = maxon.WIRE_MODE.REMOVE
            else:
                # Mute the wire.
                connection[maxon.Wires.INHIBIT] = maxon.WIRE_MODE.NORMAL
            source_port.Connect(target_port, modes=connection)
            return True
        with RSMaterialTransaction() as transaction:
            maxon.GraphModelHelper.GetSelectedConnections(self.graph, mute)
            transaction.Commit()
            c4d.EventAdd()

#=============================================
#           Redshift Transaction
#=============================================

# Transaction
class RSMaterialTransaction:
    """
    A class used to represent a transaction in an Redshift Node Material.
    Use it in a with statement.
    """

    def __init__(self, redshiftMaterial):
        self.redshiftMaterial = redshiftMaterial
        self.transaction = None

    def __enter__(self):
        if self.redshiftMaterial is not None and self.redshiftMaterial.graph is not None:
            self.transaction = self.redshiftMaterial.graph.BeginTransaction()
        return self

    def __exit__(self, type, value, traceback):
        if self.transaction is not None:
            self.transaction.Commit()



