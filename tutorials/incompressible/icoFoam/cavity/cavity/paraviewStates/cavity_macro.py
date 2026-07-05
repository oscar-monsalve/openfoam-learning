# state file generated using paraview version 6.1.0
import paraview
paraview.compatibility.major = 6
paraview.compatibility.minor = 1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.Set(
    ViewSize=[1496, 794],
    InteractionMode='2D',
    AxesGrid='Grid Axes 3D Actor',
    CenterOfRotation=[0.05000000074505806, 0.05000000074505806, 0.004999999888241291],
    CameraPosition=[0.05000000074505806, 0.05000000074505806, 0.27888724573938806],
    CameraFocalPoint=[0.05000000074505806, 0.05000000074505806, 0.004999999888241291],
    CameraParallelScale=0.07088723543695315,
    CameraParallelProjection=1,
    LegendGrid='Legend Grid Actor',
    PolarGrid='Polar Grid Actor',
)

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1496, 794)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Open FOAM Reader'
# cavityfoam = OpenFOAMReader(registrationName='cavity.foam', FileName='/home/om/OpenFOAM/om-v2512/run/openfoam-learning/tutorials/incompressible/icoFoam/cavity/cavity/cavity.foam')
# cavityfoam.Set(
#     MeshRegions=['internalMesh'],
#     CellArrays=['U', 'p'],
# )


# Added by Oscar to make the exported stated (.py) into a dynamic macro
# Get the dataset currently selected in the Pipeline Browser
cavityfoam = GetActiveSource()

# If nothing is selected, alert the user
if not cavityfoam:
    raise RuntimeError("Please select a data source in the Pipeline Browser before running this macro.")


# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=cavityfoam)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=cellDatatoPointData1)
slice1.Set(
    SliceType='Plane',
    SliceOffsetValues=[0.0],
    PointMergeMethod='Uniform Binning',
)

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Set(
    Origin=[0.05000000074505806, 0.05000000074505806, 0.004999999888241291],
    Normal=[0.0, 0.0, 1.0],
)

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.05000000074505806, 0.05000000074505806, 0.004999999888241291]

# create a new 'Contour'
velocityContour = Contour(registrationName='velocityContour', Input=slice1)
velocityContour.Set(
    ContourBy=['POINTS', 'U_Magnitude'],
    Isosurfaces=[0.0002091935394060598, 0.029581964479018678, 0.05895473541863129, 0.0883275063582439, 0.11770027729785652, 0.14707304823746914, 0.17644581917708177, 0.2058185901166944, 0.235191361056307, 0.2645641319959196, 0.2939369029355322, 0.32330967387514487, 0.35268244481475747, 0.38205521575437007, 0.41142798669398273, 0.44080075763359533, 0.47017352857320793, 0.49954629951282054, 0.5289190704524331, 0.5582918413920458, 0.5876646123316583, 0.617037383271271, 0.6464101542108837, 0.6757829251504962, 0.7051556960901089, 0.7345284670297215, 0.7639012379693341, 0.7932740089089467, 0.8226467798485594, 0.8520195507881719],
    PointMergeMethod='Uniform Binning',
)

# create a new 'Contour'
pressureContour = Contour(registrationName='pressureContour', Input=slice1)
pressureContour.Set(
    ContourBy=['POINTS', 'p'],
    Isosurfaces=[-4.366660118103027, -4.130372939965664, -3.8940857618283005, -3.657798583690937, -3.421511405553573, -3.1852242274162097, -2.9489370492788463, -2.7126498711414824, -2.476362693004119, -2.2400755148667555, -2.003788336729392, -1.7675011585920286, -1.5312139804546652, -1.2949268023173017, -1.0586396241799378, -0.8223524460425744, -0.586065267905211, -0.3497780897678471, -0.11349091163048364, 0.1227962665068798, 0.35908344464424324, 0.5953706227816067, 0.8316578009189701, 1.0679449790563336, 1.304232157193697, 1.5405193353310604, 1.7768065134684239, 2.013093691605788, 2.2493808697431517, 2.485668047880515, 2.7219552260178785, 2.958242404155242, 3.1945295822926054, 3.430816760429969, 3.667103938567333, 3.9033911167046966, 4.13967829484206, 4.3759654729794235, 4.612252651116787, 4.84853982925415],
    PointMergeMethod='Uniform Binning',
)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=cavityfoam,
    SeedType='Line')
streamTracer1.Set(
    Vectors=['CELLS', 'U'],
    InitialStepLength=0.01,
    MaximumStepLength=0.01,
    MaximumSteps=1500,
    MaximumStreamlineLength=0.5,
)

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Set(
    Point1=[0.05, 0.0, 0.005],
    Point2=[0.05, 0.1, 0.005],
    Resolution=21,
)

# create a new 'Cell Centers'
cellCenters1 = CellCenters(registrationName='CellCenters1', Input=cavityfoam)

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=cellCenters1,
    GlyphType='Arrow')
glyph1.Set(
    OrientationArray=['POINTS', 'U'],
    ScaleArray=['POINTS', 'No scale array'],
    ScaleFactor=0.005,
    GlyphTransform='Transform2',
    GlyphMode='All Points',
)

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Set(
    Scalars=['POINTS', 'AngularVelocity'],
    Vectors=['POINTS', 'Normals'],
    Radius=0.0003,
)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cavityfoam
cavityfoamDisplay = Show(cavityfoam, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.Set(
    RGBPoints=[
        # scalar, red, green, blue
        -4.366660118103027, 0.0, 0.0, 1.0,
        4.84853982925415, 1.0, 0.0, 0.0,
    ],
    ColorSpace='HSV',
    NanColor=[0.498039215686, 0.498039215686, 0.498039215686],
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
cavityfoamDisplay.Set(
    Representation='Outline',
    ColorArrayName=['CELLS', 'p'],
    LookupTable=pLUT,
    DisableLighting=1,
    Assembly='Hierarchy',
    DataAxesGrid='Grid Axes Representation',
    PolarAxes='Polar Axes Representation',
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
cavityfoamDisplay.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
cavityfoamDisplay.ScaleTransferFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
cavityfoamDisplay.OpacityTransferFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# show data from slice1
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'p'
pLUT_1 = GetColorTransferFunction('p')
pLUT_1.Set(
    RGBPoints=[
        # scalar, red, green, blue
        -4.36667013168335, 0.0, 0.0, 1.0,
        4.84853982925415, 1.0, 0.0, 0.0,
    ],
    ColorSpace='HSV',
    NanColor=[0.498039215686, 0.498039215686, 0.498039215686],
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
slice1Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'p'],
    LookupTable=pLUT_1,
    DisableLighting=1,
    Assembly='Hierarchy',
    DataAxesGrid='Grid Axes Representation',
    PolarAxes='Polar Axes Representation',
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# show data from pressureContour
pressureContourDisplay = Show(pressureContour, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
pressureContourDisplay.Set(
    Representation='Surface',
    AmbientColor=[0.0, 0.0, 0.0],
    ColorArrayName=['POINTS', ''],
    DiffuseColor=[0.0, 0.0, 0.0],
    Assembly='Hierarchy',
    DataAxesGrid='Grid Axes Representation',
    PolarAxes='Polar Axes Representation',
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
pressureContourDisplay.OSPRayScaleFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
pressureContourDisplay.ScaleTransferFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
pressureContourDisplay.OpacityTransferFunction.Points = [-4.36667013168335, 0.0, 0.5, 0.0, 4.848509788513184, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for pLUT_1 in view renderView1
pLUT_1ColorBar = GetScalarBar(pLUT_1, renderView1)
pLUT_1ColorBar.Set(
    AutoOrient=0,
    Orientation='Horizontal',
    WindowLocation='Lower Center',
    Title='Kinematic pressure, $p_{k}\\; (m^2 / s^2)$ ',
    ComponentTitle='',
    TitleFontFamily='Times',
    TitleFontSize=22,
    LabelFontFamily='Times',
    LabelFontSize=20,
    RangeLabelFormat='{:<#6.1f}',
)

# set color bar visibility
pLUT_1ColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Set(
    Points=[-4.366660118103027, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# get opacity transfer function/opacity map for 'p'
pPWF_1 = GetOpacityTransferFunction('p')
pPWF_1.Set(
    Points=[-4.36667013168335, 0.0, 0.5, 0.0, 4.84853982925415, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.Set(
    ViewModules=renderView1,
    Cues=timeAnimationCue1,
    AnimationTime=0.5,
    StartTime=0.1,
    EndTime=0.5,
    PlayMode='Snap To TimeSteps',
)

# initialize the animation scene

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/nightly/python/
##--------------------------------------------
