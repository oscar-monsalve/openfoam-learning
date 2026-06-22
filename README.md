# OpenFOAM directories and Git workflow

## OpenFOAM environment

OpenFOAM is not loaded automatically in every terminal session. Before working with OpenFOAM cases, load the OpenFOAM environment manually with:

```bash
of
```

This command activates OpenFOAM v2512 for the current terminal session by defining variables such as `$WM_PROJECT_DIR`, `$FOAM_TUTORIALS`, and `$FOAM_RUN` (these environment variables are explain in the next section), and by making commands such as `blockMesh`, `checkMesh`, `icoFoam`, and `paraFoam` available.

I intentionally run `of` only when I am going to work with OpenFOAM, instead of loading it automatically in every terminal. This keeps the normal shell environment cleaner for unrelated tasks such as Git, Python, Neovim configuration, or general Linux work.

To verify that OpenFOAM is loaded:

```bash
echo "$WM_PROJECT_VERSION"
command -v blockMesh
```

Expected version:

```text
v2512
```

## OpenFOAM environment variables

After loading OpenFOAM with:

```bash
of
```

the shell defines several useful environment variables.

## `WM_PROJECT`

```bash
echo "$WM_PROJECT"
```

Example:

```text
OpenFOAM
```

This identifies the active OpenFOAM distribution.

## `WM_PROJECT_VERSION`

```bash
echo "$WM_PROJECT_VERSION"
```

Example:

```text
v2512
```

This tells which OpenFOAM version is currently active. This is important because tutorials, solvers, dictionaries, boundary conditions, and utilities can differ between OpenFOAM versions.

## `WM_PROJECT_DIR`

```bash
echo "$WM_PROJECT_DIR"
```

Example:

```text
/opt/OpenFOAM/OpenFOAM-v2512
```

This is the OpenFOAM installation directory.

This directory contains OpenFOAM itself: solvers, utilities, libraries, source code, configuration files, and official tutorials.

Do not store personal cases here. Treat this directory as read-only during normal work.

## `FOAM_TUTORIALS`

```bash
echo "$FOAM_TUTORIALS"
```

Example:

```text
/opt/OpenFOAM/OpenFOAM-v2512/tutorials
```

This is where the official installed tutorial cases are located.

Do not run or modify tutorials directly inside this directory. Instead, copy them to a personal working directory before running them.

Example:

```bash
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" "$FOAM_RUN/tutorials/cavity"
```

## `FOAM_RUN`

```bash
echo "$FOAM_RUN"
```

Example:

```text
/home/om/OpenFOAM/om-v2512/run
```

This is the personal OpenFOAM working directory.

This is the correct place for copied tutorials, learning cases, and personal simulation cases.

Recommended structure:

```text
/home/om/OpenFOAM/om-v2512/run/
├── tutorials/
├── learning/
├── projects/
└── openfoam-learning/
```

## Standard OpenFOAM case structure

A typical OpenFOAM case has this structure:

```text
caseName/
├── 0/
├── constant/
└── system/
```

Meaning:

```text
0/          Initial and boundary conditions
constant/   Physical properties and mesh data
system/     Control, numerical schemes, solver settings, and mesh dictionaries
```

Important files commonly found in `system/`:

```text
controlDict
fvSchemes
fvSolution
blockMeshDict
```

Important files commonly found in `constant/`:

```text
transportProperties
turbulenceProperties
polyMesh/
```

## Recommended Git repository location

Create the Git repository as a subdirectory of `$FOAM_RUN`, not inside the OpenFOAM installation directory.

Recommended location:

```text
$FOAM_RUN/openfoam-learning
```

Equivalent full path on this machine:

```text
/home/om/OpenFOAM/om-v2512/run/openfoam-learning
```

This keeps the repository close to the OpenFOAM working directory while avoiding changes to the installed package files.

Suggested repository structure:

```text
openfoam-learning/
├── README.md
├── .gitignore
├── notes/
├── scripts/
└── cases/
    ├── cavity/
    ├── pipe_laminar/
    └── blockMesh_basics/
```

## What should be committed to Git?

Commit files that define the case and document the learning process:

```text
README.md
notes/
scripts/
cases/*/0/
cases/*/constant/
cases/*/system/
Allrun
Allclean
```

Commit OpenFOAM dictionaries such as:

```text
controlDict
fvSchemes
fvSolution
blockMeshDict
transportProperties
turbulenceProperties
snappyHexMeshDict
decomposeParDict
```

## What should not be committed?

Do not commit heavy generated files:

```text
Result time directories
Generated meshes
Parallel processor directories
VTK exports
postProcessing output
Large log files
ParaView temporary files
```

Examples of generated directories:

```text
0.1/
0.2/
0.5/
1/
2/
10/
constant/polyMesh/
processor0/
processor1/
postProcessing/
VTK/
```

## Recommended workflow

Copy official tutorials into the repository only when working on them:

```bash
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cases/cavity
```

Run the case:

```bash
cd cases/cavity
blockMesh
checkMesh
icoFoam
paraFoam
```
