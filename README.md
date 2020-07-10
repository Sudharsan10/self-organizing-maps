<meta name="google-site-verification" content="anaQPdlDO5QzFwQQ6mpEFvfJXLj2Ue8-EFylgHd7JlU" />

<p align="center">
  <a href="https://github.com/Sudharsan10/self-organizing-maps">
    <img src=".\img\card.png" alt="Social-header">
  </a>  
</p>

<p align="center">
  13-D Wine data visualization & classification using 2D Self Organizing Maps.  
  <br>
    <a href=""><strong>Explore Self Organizing Maps docs »</strong></a>
    <br>
    <br>
    <a href="https://github.com/Sudharsan10/self-organizing-maps/issues/new">Report bug</a>
    ·
    <a href="https://github.com/Sudharsan10/self-organizing-maps/issues/new">Request feature</a>    
</p>


Self Organizing Map - An Unsupervised learning technique to visualize and classify 13 dimensional wine data by mapping  it to a 2D map.


## Table of contents
- [Quick start](#quick-start)
- [Pre-Requisites](#pre-requisites)
- [Run instructions](#run-instructions)
- [Status](#status)
- [What's included](#whats-included)
- [Documentation](#documentation)
- [Bugs and Feature requests](#bugs-and-feature-requests)
- [Creators](#creators)
- [Thanks](#thanks)

## Quick start
There are two ways to run this app: 
- [Download the latest Docker container.]() and run from the app in that container ( NOte: No Docker container at the moment)
- Clone the repo: 
    > ```shell script
    > git clone https://github.com/Sudharsan10/self-organizing-maps.git
    > ```
    
## Status
[![Documentation Status](https://img.shields.io/badge/Documentation-yes-e01563)](https://github.com/Sudharsan10/TilePuzzelSolver-App/tree/master/img/logo)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-e01563.svg)](https://github.com/Sudharsan10/TilePuzzelSolver-App/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Python%20Version-3.8.3-brightgreen)](https://www.python.org/)
[![pip-version](https://img.shields.io/badge/pip%20Version-20.0.2-brightgreen)](https://pip.pypa.io/en/stable/installing/)
[![pyqt-version](https://img.shields.io/badge/PyQt5%20Version-5.14.2-brightgreen)](https://pypi.org/project/PyQt5/)
[![numpy-version](https://img.shields.io/badge/numpy%20Version-1.18.1-brightgreen)](https://pypi.org/project/numpy/)
[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-0366d6.svg)](http://commonmark.org)
[![contributors](https://img.shields.io/badge/Contributors-01-0366d6)](https://github.com/Sudharsan10/TilePuzzelSolver-App/graphs/contributors)
[![Logo](https://img.shields.io/badge/Logo-Adobe%20Photoshop-20639B.svg)](https://github.com/Sudharsan10/TilePuzzelSolver-App/graphs/commit-activity)


## What's included
Within the download you'll find the following directories and files, logically grouping the modules in its own packages. 
You'll see something like this:

```text
Self Organizing Maps/   
├── data/
|   ├── Processed/...
|   └── Raw/...
├── docs/ ...
├── img/ ...
├── notebooks/
|   ├── __init__.py
|   ├── test_tile_puzzle_solver.py 
|   └── tile_puzzle_solver.py
├── src/
|   ├── handler/
|   |   ├── __init__.py
|   |   └── utility.py
|   └── som
|       ├── __init__.py
|       ├── som.py
|       └── som2d.py
├── Readme.md
├── main.py
└── setup.py
```
# ------>>> Rest of the content Under Progress <<<----

## Documentation
### Contents:
1. [How to use](#howtouse)
2. [Architecture](#architecture)
3. [Solver.py](#solver_py)
4. [Node obj Data structure](#node)
    
### 1 How to use <a id ='howtouse'></a>
Navigate to the project folder containing setup.py and run it. If using command line to run it, you can follow the command given below,
```shell script
python  setup.py
```
Enter the initial state of the puzzle and goal state of the puzzle as shown in the fig below.

Now you have three actions to perform in the form of three different button in the options section in the right side of the app.
They are,
1. [Find solution](#find-solution)
2. [Is solvable?](#is-solvable)
3. [Reset](#reset)

##### 1.2.1 Is solvable? <a id ='is-solvable'></a>
If you wish only to check for the solution feasibility for given state then you can use this button just to check the solution feasibility.

##### 1.2.2 Find solution <a id ='find-solution'></a>
This button triggers the autoSolve() function, which in checks for the solution feasibility if solution is feasible then 
it calls the method solve() from the TilePuzzleSolver class, upon completion of solve() method, backtrack() method is called.
Which returns the solution to the given puzzle states as a list of numpy array. This can be seen well in the flowchart below.

##### 1.2.3 Reset <a id ='reset'></a>
This button resets all the fields in the GUI by triggering the ClearAll() method.

If the Find Solution action is performed and upon success, a new button simulation will be visible in the options section 
and simulation section also becomes visible with four more action buttons and a simulation output area.

**Auto/Manual toggle Button:** Toggles visibility between start, stop button with manual navigation buttons - next, previous.

**Start/Pause buttons:** Starts and stops the simulation sates

**Next/Previous buttons:** use it to manually switch to the next/previous state in solution

**Reset button:** it reset the simulation output and toggles back to start/pause button.

<p align="center">
    <img src=".\img\htu01.png" width="100%" alt="how-to-use-01">
    .
    <img src=".\img\htu02.png" width="100%" alt="how-to-use-02">
    .
    <img src=".\img\htu03.png" width="100%" alt="how-to-use-03">
    .
    <img src=".\img\htu04.png" width="100%" alt="how-to-use-04">
    .
    <img src=".\img\htu05.png" width="100%" alt="how-to-use-05">
  </a>  
</p>

### 2 Architecture<a id='architecture'></a>
<img src=".\img\architecture.png" width="100%" />

### 3 solver.py<a id='sovler'></a>
<img src=".\img\solver.png" width="100%" />

### 4 Node obj Data Structure<a id='node'></a>
<img src=".\img\node.png" width="100%" />


## Bugs and feature requests
Have a bug or a feature request? Search for existing and closed issues, if your problem or idea is not addressed yet, 
[please open a new issue](https://github.com/Sudharsan10/TilePuzzelSolver-App/issues/new).

## Creators
**@Sudharsan** : <https://github.com/Sudharsan10>

<p align='center'>
    <a id='thanks'></a>
    Thank you for visiting our Repo!
</p>
