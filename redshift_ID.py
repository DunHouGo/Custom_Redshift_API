#  Last Update 2022 08 20
#
#  Easy to Use Redshift ID 
# 
#  Cinema 4D build S26.107 @Redshift 3.5.06
#
#  Autor: DunHou
#
#  Only For Redshift Node Materials
#
#  To be Continue
#
import maxon
RS_SHADER_PREFIX = "com.redshift3d.redshift4c4d.nodes.core."
RS_STANDARD_SURFACE_PREFIX = "com.redshift3d.redshift4c4d.nodes.core.standardmaterial."

#=============================================
#                   Node
#=============================================


# Shader Asset ID Strings ==> commonly used
class ShaderStr():    
    # main 
    Output = "com.redshift3d.redshift4c4d.node.output" # Output node
    StandardMaterial = RS_SHADER_PREFIX + "standardmaterial"  # Standard Surface node
    # basic
    Incandescent = RS_SHADER_PREFIX + "incandescent" # Incandescent node
    Sprite = RS_SHADER_PREFIX + "sprite" # Sprite node
    Volume = RS_SHADER_PREFIX + "volume" # Volume node
    MaterialBlender = RS_SHADER_PREFIX + "materialblender" # Material Blender node
    MaterialLayer = RS_SHADER_PREFIX + "materiallayer" # Material Layer node
    # not recommend to use (out of date)
    Material = RS_SHADER_PREFIX + "material" # Old Material node

    # Color Nodes
    Color = "net.maxon.asset.utility.color" # C4D node
    AbsColor = RS_SHADER_PREFIX + "rsmathabscolor" # Abs Color node

    ColorRange = RS_SHADER_PREFIX + "rscolorrange" # Color Range node
    Colorlayer = RS_SHADER_PREFIX + "rscolorlayer" # Color Layer node

    ColorInvert = RS_SHADER_PREFIX + "rsmathinvcolor" # Color Invert node
    ColorMul = RS_SHADER_PREFIX + "rsmathmul" # Color Mutiply node
    ColorMix = RS_SHADER_PREFIX + "rscolormix" # Color Mix node
    ColorAdd = RS_SHADER_PREFIX + "rsmathadd" # Color Add node
    # Texture
    Texture = RS_SHADER_PREFIX + "texturesampler" # Texture
    Ramp = RS_SHADER_PREFIX + "rsramp" # Ramp
    ScalarRamp = RS_SHADER_PREFIX + "rsscalarramp" # Scalar Ramp
    MaxonNoise = RS_SHADER_PREFIX + "maxonnoise" # Maxon Noise
    Fresnel = RS_SHADER_PREFIX + "fresnel" # Fresnel
    Curvature = RS_SHADER_PREFIX + "curvature" # Curvature
    AO = RS_SHADER_PREFIX + "ambientocclusion" # AO
    WireFrame = RS_SHADER_PREFIX + "wireframe" # Wire Frame
    # Unity
    OSLShader = RS_SHADER_PREFIX + "osl" # OSL
    Triplanar = RS_SHADER_PREFIX + "triplanar" # Triplanar
    UVProjection = RS_SHADER_PREFIX + "uvprojection" # UV Projection
    StoreColorToAOV = RS_SHADER_PREFIX + "storecolortoaov" # Store Color To AOV
    RaySwitch = RS_SHADER_PREFIX + "rayswitch" # Ray Switch
    ShaderSwitch = RS_SHADER_PREFIX + "rsshaderswitch" # Shader Switch
    # Bump and Dispplacement
    BumpMap = RS_SHADER_PREFIX + "bumpmap" # Bump Map
    BumpBlender = RS_SHADER_PREFIX + "bumpblender" # Bump Blender
    Displacement = RS_SHADER_PREFIX + "displacement" # Displacement
    DisplacementBlender = RS_SHADER_PREFIX + "displacementblender" # Displacement Blender
    RoundCorners = RS_SHADER_PREFIX + "roundcorners" # Round Corners
    # Attributes
    State = RS_SHADER_PREFIX + "state" # State
    VertexAttribute = RS_SHADER_PREFIX + "vertexattributelookup" # Vertex Attribute
    PointAttribute = RS_SHADER_PREFIX + "particleattributelookup" # Point Attribute
    ColorUserData = RS_SHADER_PREFIX + "rsuserdatacolor" # 
    IntegerUserData = RS_SHADER_PREFIX + "rsuserdatainteger" # 
    ScalarUserData = RS_SHADER_PREFIX + "rsuserdatascalar" # 
    StringUserData = RS_SHADER_PREFIX + "rsuserdatastring" # 
    VectorUserData = RS_SHADER_PREFIX + "rsuserdatavector" # 

# Shader Asset IDs ==> commonly used
class ShaderID():
    Output = maxon.Id(ShaderStr.Output) # Output node
    StandardMaterial = maxon.Id(ShaderStr.StandardMaterial) # Standard Surface node
    # basic
    Incandescent = maxon.Id(ShaderStr.Incandescent) # Incandescent node
    Sprite = maxon.Id(ShaderStr.Sprite) # Sprite node
    Volume = maxon.Id(ShaderStr.Volume) # Volume node
    MaterialBlender = maxon.Id(ShaderStr.MaterialBlender) # Material Blender node
    MaterialLayer = maxon.Id(ShaderStr.MaterialLayer) # Material Layer node
    # not recommend to use (out of date)
    Material = maxon.Id(ShaderStr.Material) # Old Material node

    # Color Nodes
    Color = maxon.Id(ShaderStr.Color) # C4D node
    AbsColor = maxon.Id(ShaderStr.AbsColor) # Abs Color node

    ColorRange = maxon.Id(ShaderStr.ColorRange) # Color Range node
    Colorlayer = maxon.Id(ShaderStr.Colorlayer) # Color Layer node

    ColorInvert = maxon.Id(ShaderStr.ColorInvert) # Color Invert node
    ColorMul = maxon.Id(ShaderStr.ColorMul) # Color Mutiply node
    ColorMix = maxon.Id(ShaderStr.ColorMix) # Color Mix node
    ColorAdd = maxon.Id(ShaderStr.ColorAdd) # Color Add node

    # Texture
    Texture = maxon.Id(ShaderStr.Texture) # Texture
    Ramp = maxon.Id(ShaderStr.Ramp) # Ramp
    MaxonNoise = maxon.Id(ShaderStr.MaxonNoise) # Maxon Noise
    Fresnel = maxon.Id(ShaderStr.Fresnel) # Fresnel
    Curvature = maxon.Id(ShaderStr.Curvature) # Curvature
    AO = maxon.Id(ShaderStr.AO) # AO
    WireFrame = maxon.Id(ShaderStr.WireFrame) # Wire Frame

    # Unity
    OSLShader = maxon.Id(ShaderStr.OSLShader) # OSL
    Triplanar = maxon.Id(ShaderStr.Triplanar) # Triplanar
    UVProjection = maxon.Id(ShaderStr.UVProjection) # UV Projection
    StoreColorToAOV = maxon.Id(ShaderStr.StoreColorToAOV) # Store Color To AOV
    RaySwitch = maxon.Id(ShaderStr.RaySwitch) # Ray Switch
    ShaderSwitch = maxon.Id(ShaderStr.ShaderSwitch) # Shader Switch
    # Bump and Dispplacement
    BumpMap = maxon.Id(ShaderStr.BumpMap) # Bump Map
    BumpBlender = maxon.Id(ShaderStr.BumpBlender) # Bump Blender
    Displacement = maxon.Id(ShaderStr.Displacement) # Displacement
    DisplacementBlender = maxon.Id(ShaderStr.DisplacementBlender) # Displacement Blender
    RoundCorners = maxon.Id(ShaderStr.RoundCorners) # Round Corners
    # Attributes
    State = maxon.Id(ShaderStr.State) # State
    VertexAttribute = maxon.Id(ShaderStr.VertexAttribute) # Vertex Attribute
    PointAttribute = maxon.Id(ShaderStr.PointAttribute) # Point Attribute
    ColorUserData = maxon.Id(ShaderStr.ColorUserData) # 
    IntegerUserData = maxon.Id(ShaderStr.IntegerUserData) # 
    ScalarUserData = maxon.Id(ShaderStr.ScalarUserData) # 
    StringUserData = maxon.Id(ShaderStr.StringUserData) # 
    VectorUserData = maxon.Id(ShaderStr.VectorUserData) # 

#=============================================
#                   Port
#=============================================

# Port ID Strings ==> most commonly used
class PortStr():
    # output port
    Output_Surface = "com.redshift3d.redshift4c4d.node.output.surface"
    Output_Displacement = "com.redshift3d.redshift4c4d.node.output.displacement"
    Output_Volume = "com.redshift3d.redshift4c4d.node.output.volume"
    Output_Environment = "com.redshift3d.redshift4c4d.node.output.environment"
    Output_Light = "com.redshift3d.redshift4c4d.node.output.light"

    # standard surface port

    # output
    standard_outcolor =  RS_STANDARD_SURFACE_PREFIX + "outcolor"
    # base 
    base_color = RS_STANDARD_SURFACE_PREFIX + "base_color"
    base_color_weight = RS_STANDARD_SURFACE_PREFIX + "base_color_weight"
    diffuse_roughness = RS_STANDARD_SURFACE_PREFIX + "diffuse_roughness"
    metalness = RS_STANDARD_SURFACE_PREFIX + "metalness"
    # reflection
    refl_color = RS_STANDARD_SURFACE_PREFIX + "refl_color"
    refl_weight = RS_STANDARD_SURFACE_PREFIX + "refl_weight"
    refl_roughness = RS_STANDARD_SURFACE_PREFIX + "refl_roughness"
    refl_ior = RS_STANDARD_SURFACE_PREFIX + "refl_ior"
    refl_aniso = RS_STANDARD_SURFACE_PREFIX + "refl_aniso"
    refl_aniso_rotation = RS_STANDARD_SURFACE_PREFIX + "refl_aniso_rotation"
    refl_samples = RS_STANDARD_SURFACE_PREFIX + "refl_samples"
    refl_isglossiness = RS_STANDARD_SURFACE_PREFIX + "refl_isglossiness" # bool port
    # transmission
    refr_color = RS_STANDARD_SURFACE_PREFIX + "refr_color"
    refr_weight = RS_STANDARD_SURFACE_PREFIX + "refr_weight"
    refr_roughness = RS_STANDARD_SURFACE_PREFIX + "refr_roughness"
    refr_samples = RS_STANDARD_SURFACE_PREFIX + "refr_samples"
    ss_depth = RS_STANDARD_SURFACE_PREFIX + "ss_depth"
    ss_scatter_color = RS_STANDARD_SURFACE_PREFIX + "ss_scatter_color"
    ss_phase = RS_STANDARD_SURFACE_PREFIX + "ss_phase"
    ss_samples = RS_STANDARD_SURFACE_PREFIX + "ss_samples"
    refr_abbe = RS_STANDARD_SURFACE_PREFIX + "refr_abbe"
    # sss
    sss_color = RS_STANDARD_SURFACE_PREFIX + "ms_color"
    sss_weight = RS_STANDARD_SURFACE_PREFIX + "ms_amount"
    sss_radius = RS_STANDARD_SURFACE_PREFIX + "ms_radius"
    sss_scale = RS_STANDARD_SURFACE_PREFIX + "ms_radius_scale"
    sss_phase = RS_STANDARD_SURFACE_PREFIX + "ms_phase"
    sss_mode = RS_STANDARD_SURFACE_PREFIX + "ms_mode"
    sss_samples = RS_STANDARD_SURFACE_PREFIX + "ms_samples"
    # sheen
    sheen_color = RS_STANDARD_SURFACE_PREFIX + "sheen_color"
    sheen_weight = RS_STANDARD_SURFACE_PREFIX + "sheen_weight"
    sheen_roughness = RS_STANDARD_SURFACE_PREFIX + "sheen_roughness"
    sheen_samples = RS_STANDARD_SURFACE_PREFIX + "sheen_samples"
    # thin film
    thinfilm_thickness = RS_STANDARD_SURFACE_PREFIX + "thinfilm_thickness"
    thinfilm_ior = RS_STANDARD_SURFACE_PREFIX + "thinfilm_ior"
    # coat
    coat_color = RS_STANDARD_SURFACE_PREFIX + "coat_color"
    coat_weight = RS_STANDARD_SURFACE_PREFIX + "coat_weight"
    coat_roughness = RS_STANDARD_SURFACE_PREFIX + "coat_roughness"
    coat_ior = RS_STANDARD_SURFACE_PREFIX + "coat_ior"
    coat_aniso = RS_STANDARD_SURFACE_PREFIX + "coat_aniso"
    coat_aniso_rotation = RS_STANDARD_SURFACE_PREFIX + "coat_aniso_rotation"
    coat_samples = RS_STANDARD_SURFACE_PREFIX + "coat_samples"
    coat_bump_input = RS_STANDARD_SURFACE_PREFIX + "coat_bump_input"
    # emission
    emission_color = RS_STANDARD_SURFACE_PREFIX + "emission_color"
    emission_weight = RS_STANDARD_SURFACE_PREFIX + "emission_weight"
    # geo
    opacity_color = RS_STANDARD_SURFACE_PREFIX + "opacity_color"
    bump_input = RS_STANDARD_SURFACE_PREFIX + "bump_input"

# Port IDs ==> most commonly used
class PortID():
    # output
    Output_Surface = maxon.Id(PortStr.Output_Surface)
    Output_Displacement = maxon.Id(PortStr.Output_Displacement)
    Output_Volume = maxon.Id(PortStr.Output_Volume)
    Output_Environment = maxon.Id(PortStr.Output_Environment)
    Output_Light = maxon.Id(PortStr.Output_Light)

    # standard surface port

    # output
    standard_outcolor =  maxon.Id(PortStr.standard_outcolor)
    # base 
    base_color = maxon.Id(PortStr.base_color)
    base_color_weight = maxon.Id(PortStr.base_color_weight)
    diffuse_roughness = maxon.Id(PortStr.diffuse_roughness)
    metalness = maxon.Id(PortStr.metalness)
    # reflection
    refl_color = maxon.Id(PortStr.refl_color)
    refl_weight = maxon.Id(PortStr.refl_weight)
    refl_roughness = maxon.Id(PortStr.refl_roughness)
    refl_ior = maxon.Id(PortStr.refl_ior)
    refl_aniso = maxon.Id(PortStr.refl_aniso)
    refl_aniso_rotation = maxon.Id(PortStr.refl_aniso_rotation)
    refl_samples = maxon.Id(PortStr.refl_samples)
    refl_isglossiness = maxon.Id(PortStr.refl_isglossiness)
    # transmission
    refr_color = maxon.Id(PortStr.refr_color)
    refr_weight = maxon.Id(PortStr.refr_weight)
    refr_roughness = maxon.Id(PortStr.refr_roughness)
    refr_samples = maxon.Id(PortStr.refr_samples)
    ss_depth = maxon.Id(PortStr.ss_depth)
    ss_scatter_color = maxon.Id(PortStr.ss_scatter_color)
    ss_phase = maxon.Id(PortStr.ss_phase)
    ss_samples = maxon.Id(PortStr.ss_samples)
    refr_abbe = maxon.Id(PortStr.refr_abbe)
    # sss
    sss_color = maxon.Id(PortStr.sss_color)
    sss_weight = maxon.Id(PortStr.sss_weight)
    sss_radius = maxon.Id(PortStr.sss_radius)
    sss_scale = maxon.Id(PortStr.sss_scale)
    sss_phase = maxon.Id(PortStr.sss_phase)
    sss_mode = maxon.Id(PortStr.sss_mode)
    sss_samples = maxon.Id(PortStr.sss_samples)
    # sheen
    sheen_color = maxon.Id(PortStr.sheen_color)
    sheen_weight = maxon.Id(PortStr.sheen_weight)
    sheen_roughness = maxon.Id(PortStr.sheen_roughness)
    sheen_samples = maxon.Id(PortStr.sheen_samples)
    # thin film
    thinfilm_thickness = maxon.Id(PortStr.thinfilm_thickness)
    thinfilm_ior = maxon.Id(PortStr.thinfilm_ior)
    # coat
    coat_color = maxon.Id(PortStr.coat_color)
    coat_weight = maxon.Id(PortStr.coat_weight)
    coat_roughness = maxon.Id(PortStr.coat_roughness)
    coat_ior = maxon.Id(PortStr.thinfilm_ior)
    coat_aniso = maxon.Id(PortStr.coat_aniso)
    coat_aniso_rotation = maxon.Id(PortStr.coat_aniso_rotation)
    coat_samples = maxon.Id(PortStr.coat_samples)
    coat_bump_input = maxon.Id(PortStr.coat_bump_input)
    # emission
    emission_color = maxon.Id(PortStr.emission_color)
    emission_weight = maxon.Id(PortStr.emission_weight)
    # geo
    opacity_color = maxon.Id(PortStr.opacity_color)
    bump_input = maxon.Id(PortStr.bump_input)

#=============================================
#          Simplyfy Redshift ID
#=============================================
# Str of node ID
def StrNodeID(node_name):
    redshift_pre = "com.redshift3d.redshift4c4d.nodes.core."
    realID = redshift_pre + node_name
    return realID
# Str of port ID
def StrPortID(node_name, port_name):
    redshift_pre = "com.redshift3d.redshift4c4d.nodes.core."
    realID = redshift_pre + node_name +  '.' + port_name
    return realID
# Make a str to maxon ID
def StrtoMaxonID(ID_string):
    realID = maxon.Id(str(ID_string))
    return realID