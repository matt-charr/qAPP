<div align="center">
  <div>
    <img src="LOGO.jpg" width="900" height="600"/>
  </div>
</a>

# QA

<em>Design, monitor and price your own financial contracts.</em>

</div>

# 🍺 Project Status

<table class="no-border">
  <tr>
    <td><a href="https://github.com/matt-charr/qa-demo/stargazers">
    <img src="https://img.shields.io/github/stars/matt-charr/qa-demo?style=social"></td>
    <td><a href="https://github.com/matt-charr/qa-demo/network/members">
    <img src="https://img.shields.io/github/forks/matt-charr/qa-demo?style=social"></td>
    <td><a href="https://github.com/matt-charr/qa-demo/watchers">
    <img src="https://img.shields.io/github/watchers/matt-charr/qa-demo?style=social"></td>
    <td><a href="https://github.com/matt-charr/qa-demo/issues">
    <img src="https://img.shields.io/github/issues/matt-charr/qa-demo?style=social"></td>
  <tr>
    <td><a href="https://twitter.com/matt_charr" alt="twitter"><img src="https://img.shields.io/twitter/follow/matt-charr?style=social" alt="twitter"></a></td>
    <td><a href="https://www.twitch.tv/mattcharr" alt="twitch"><img src="https://img.shields.io/badge/twitch-d51561.svg?style=flat-square&logo=twitch" alt="twitch"></a></td>
    <td><a href="https://www.linkedin.com/in/matthieu-charrier-080820134/" alt="linkedin"><img src="https://img.shields.io/badge/linkedin-d00.svg?style=flat-square&logo=linkedin" alt="linkedin"></a></td>
    <td><a href="https://github.com/matt-charr/" alt="GitHub"><img src="https://img.shields.io/badge/GitHub-d1014.svg?style=flat-square&logo=GitHub" alt="GitHub"></a></td>
  <tr>
  <tr>
    <td><img src="https://img.shields.io/badge/Solution-C++17-blue.svg?style=flat&logo=c%2B%2B&logoColor=b0c0c0&labelColor=363D44" alt="C++ solution"/></td>
    <td><img src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20Mac-blue??style=flat&logo=Linux&logoColor=b0c0c0&labelColor=363D44" alt="Operating systems"/></td>
  </tr>
</table>

⭐ Star the project on GitHub helps it to progress.

<td>
<h3>📰 Latest news </h3>
<ul>
  <li> <ins>2023-11-18</ins>
<ul>
    <li> 🔔(<strong>Release</strong>) <a href="https://github.com/matt-charr/qa-demo/releases/tag/v0.1.0">qa-v0.1.0</a> is out 🚀</li>
</ul>
</ul>
</td>

<td>
<h3>👷 Current work </h3>
<ul>
<li> <ins>2023-11-18</ins>
<ul>
    <li>📗(<strong>Project</strong>) Handle early exercise feature. </li>
    <li>📙(<strong>Feature</strong>) Make PDE pricer framework.</li>
    <li>📘(<strong>Misc</strong>) Handle intraday fixings/payments/exercises.</li>
    <li>📕(<strong>Issue</strong>)</li>
</ul>
</ul>
</td>

## 📋 Table of Contents

1. 🤖 [Introduction](#introduction)
2. ⚡️ [Quick Start](#quick-start)
3. 🙌 [Contributions](#contributions)
4. 💻 [Insights](#insights)
   1. 🍯 [Developement](#developement)
   2. 🍏 [Build](#build)
   3. 🍊 [Tests](#tests)
   4. 🍈 [Continuous Integration](#continuous-integration)
   5. 🍇 [Continuous Delivery](#continuous-delivery)
5. 🌴 [Features](#features)
   1. 📝 [List of features](#list-of-features)
   2. 🤝 [Missing a specific feature ?](#missing-a-specific-feature-?)
   3. 🔎 [Found a bug ?](#found-a-bug-?)
6. 📜 [Licence](#licence)

# <a name="introduction">🤖 Introduction</a>

`QA-Quantitative Analytics` is an ecosystem of components that help you with designing, monitoring and pricing your own financial derivatives.

- **qacore** (<em>private</em>) -- The core library of the project that is the agregation of embedded libraries in charge of implementing contract, data, modeling and pricing engine.

- **qapp** (<em>public</em>) -- The GUI desktop application through which the user can interact with `qacore` and send all kind of request such as pricing a contract, feed a database, see model calibration results, inspect the contract lifetime events and much more.

- **qalgebra** (<em>private</em>) -- `qacore` uses the power of algebraic contract description and `qalgebra` is the library that implements it: A customized language easily understandable by human and machine to design your contract with a self-explanatory script. Thanks to qalgebra, The user can write down a contract using this simple language and send it to qa for it to run a bunch of actions such as pricing, monitoring and much more. The whole `qa` ecosystem is built arround `qalgebra` device.

- **qafactory** (<em>public</em>) -- For the users to benefit `qalgebra` technology and price their own contracts, our developpers created `qafactory`, a friendly factory where all programmer enthusiasts can use and contribute its favorite payoff functions to eventually inspect it from `qapp`. This game room is yours, feel free to populate and use it at your convenience.

# <a name="quick-start">⚡️ Quick Start</a>

To download the latest version of our application, go to [Releases](https://github.com/matt-charr/qa-demo/releases/tag) and download the asset that corresponds to your operating system.

<div align="left">
  <div>
    <img src="capture/Capture.PNG" width="500" height="200"/>
  </div>
</div>

After extracting all the files into a nice location of your machine, you are falling onto a folder that contains `qa` directory. 

<div align="left">
  <div>
    <img src="capture/Capture2.PNG" width="500" height="200"/>
  </div>
</div>

Open the `qapp` executable located at <em>qa/bin</em>, you arrive to the main page which is a logger frame that displays the messages that `qacore` returns after each actions.

<div align="left">
  <div>
    <img src="capture/Capture3.PNG" width="500" height="200"/>
  </div>
</div>

Each action triggers by `qapp` - typically pressing a button - throws <FONT COLOR="BLUE"><em>information</em></FONT>, <FONT COLOR="GREEN"><em>warnings</em></FONT>, <FONT COLOR="ORANGE"><em>errors</em></FONT> and/or <FONT COLOR="RED"><em>exceptions</em></FONT>.
- If an <FONT COLOR="RED"><em>exception</em></FONT> is thrown, it means something went wrong dev side. In that case please [report your issue](https://github.com/matt-charr/qa-demo/issues) by dropping your mockup file together with your contract and data files if any.
- If an <FONT COLOR="ORANGE"><em>error</em></font> is thrown, it means that something went wrong user side and `qacore` did not manage to perform your request. In that case you need to check the log and correct your request accordingly.
- If an <FONT COLOR="GREEN"><em>warning</em></font> is thrown, it means that something went wrong user side but `qacore` managed to perform the request.
At inception, an action always thrown an <FONT COLOR="BLUE"><em>information</em></FONT> message to the user such as "Pricing contract...", the goal is to inform what action `qapp` is performing.
When the action is over, a <FONT COLOR="YELLOW"><em>success</em></font> is thrown if an only if no error or exception occured during the action lifetime.

# <a name = "contributions"> 🙌 Contributions</a>

Coming soon ...

# <a name="work-style">💻 Insights</a>

## <a name="developement"> 🍯 Developement</a>

Once a bug or a new feature is submitted, an issue is created with the corresponding flag (bug, feature, project, creation). 
Once picked from the stack, a dev branch is created, comes down locally to the developper machine and this is where the fun begins 😃

## <a name="build"> 🍏 Build</a>

`qa` uses [CMake](https://cmake.org/) as a build system and has its main code base located on a private repository which access is restricted to our developers only. Besides, it relies on a bunch of repository dependencies that are required at `qa` developpement/build time. <br> 
It is to the following projects that we owe our heartfelt thanks for their generous Open Source contribution.

- [ImGui]()
- [ImPlot]()
- [ImFileBrowser]()
- [MariaDB]()
- [Curl]()
- [OpenGL]()
- [Glfw]()
- [JsonCpp]()
- [GTest]()
- [Eigen]()

To load the below dependencies, `qa` uses the power of [superbuild](https://cmake.org/cmake/help/latest/module/ExternalProject.html) feature from CMake. For that purpose, an embedded CMake project is in charge of cloning, building and installing all the dependencies that `qa` requires into a specific folder. That's pretty cool, isn't it ? 😃

## <a name="tests"> 🍊 Tests</a>

At the end of each dev session, a new unit test is required to be submitted to the test suite together with a contract json file that replicates the expected behavior of the code change. To ensure that the code change effect is not broken by any subsequent modifications, we use the service of [GTest]() as a testing framework.

## <a name = "continuous-integration">🍈 Continuous Integration</a>

`qa` embbeds a custom GitHub action that runs at each pull requests. Once a pull request is submitted, build and tests are triggered on our Windows and Linux self-hosted runners in Debug/Release mode with the below configurations. A dev branch is merged if and only if all builds and tests passed on all configurations.

| Name                          | OS             | CMake        | Generator             | Architecture | Build Type | Compiler            | Status  |
| ----------------------------- | -------------- | -------------------- | --------------------- | ------------ | ---------- | ------------------  | ------- |
| Windows-Release               | windows-latest | CMake-3.27.2 | MinGW Makefiles       |x64              | Release    | GCC-13.2.0          | ✅     |
| Windows-Debug                 | windows-latest | CMake-3.27.2 | Visual Studio 17 2022 | x64          | Debug      | MSVC-19.30.30709.0  | ✅     |
| Linux-Release                 | ubuntu-latest  | CMake-3.22.1 | Unix Makefiles        |x64              | Release    | GCC-11.4.0          | ✅     |
| Linux-Debug                   | ubuntu-latest  | CMake-3.22.1 | Unix Makefiles        |x64              | Debug      | GCC-11.4.0          | ✅     |
| MacOS-Release                 | macos-latest   |  | Unix Makefiles        |x64              | Release    |                     | ❌     |
| MacOS-Debug                   | macos-latest   |  | Xcode                 |x64              | Debug      |                     | ❌     |

> [!NOTE]
> `qa` has subscribed to a remote VPS (KVM2 plan - 100Go) provided by [Hostinger](https://www.hostinger.fr) to run builds, tests and deployment on Linux. We could not find any server providers to run our builds and tests on MacOS and are listening to any suggestions 😃.

## <a name="continuous-delivery">🍇 Continuous Delivery</a>

Our team delivers a release or a patch on a regular basis, and strives to respect as closely as possible the [semantic versioning](https://semver.org/). To publish a new release, each tag created on our developement repository triggers a github actions that for each OS supported will create and upload the package to [qa-demo](https://github.com/matt-charr/qa-demo). Here are the configurations on which we deploy our package:

| Name                          | OS             | CMake        | Generator             | Architecture | Build Type | Compiler            | Status  |
| ----------------------------- | -------------- | -------------------- | --------------------- | ------------ | ---------- | ------------------  | ------- |
| Windows-Release               | windows-latest | CMake-3.27.2 | MinGW Makefiles       |x64              | Release    | GCC-13.2.0          | ✅     |
| Linux-Release                 | ubuntu-latest  | CMake-3.22.1 | Unix Makefiles        |x64              | Release    | GCC-11.4.0          | ✅     |
| MacOS-Release                 | macos-latest   |  | Unix Makefiles        |x64              | Release    |                     | ❌     |

> [!IMPORTANT]
> We are far from being CD experts and know that our solution looks like a rush, better ways of releasing probably exist such as deploying binaries to a more convenient location than GitHub or building on a dedicated production environement. You are more than welcome to suggest improvements or just simply share your CD work styles. 

# <a name="features"> 🌴 Features</a>

## <a name="list-of-features">📝 List of features</a>

1. [How can I report my issue ?](#how-can-i-report-my-issue-?)
2. [How can I build my contract ?](#how-can-i-build-my-contract-?)
3. [How can I load my contract ?](#how-can-i-load-my-contract-?)
4. [How can I move my contract ?](#how-can-i-move-my-contract-?)
5. [How can I edit my fixings ?](#how-can-i-edit-my-fixings-?)

### <a name="how-can-i-report-my-issue-?">📺 How can I report my issue ?</a>
### <a name="how-can-i-build-my-contract-?">📺 How can I build my contract ?</a>

1. Please ensure you have a C++ compiler (MSBuild, g++, Clang, ...) and a recent CMake version installed in your machine.

```bash
# Ensure you have a C++ compiler installed in your machine!
g++ --version

# Ensure you have a recent CMake version installed in your machine!
cmake --version
```

2. Go to <em>factory</em> directory and if not already created, create a new cpp file in <em>examples</em> named <em>autocall.cpp</em>. Open it with your favorite editor to have a nice overview of what the language looks like and how to use it to build your own contract.

```bash

# go to factory.
cd factory &&

# create autocall.cpp.
touch examples/autocall.cpp &&

# let's see how it looks like.
vim examples/autocall.cpp
```

3. You can create your contract json file by running the following commands:

```bash

# configure.
cmake -S . -B ./build -G "MinGW Makefiles" -DMAIN="examples/autocall.cpp" &&

# build.
cmake --build ./build &&

# run.
./bin/run
```

or execute the shell:

```bash
# configure, build and run.
./scripts/build.sh examples/autocall.cpp
```

4. Check that the contract json file has been create with success.

```bash
# check that json file exists.
vim examples/autocall.json
```

Congratulations! You built your first contract.
Once you are familiar enough with the syntax, feel free to update it at your convenience or even create your own designed contract cpp files and generate their respective contract json file!

> [!NOTE]
> If you are more familiar with vscode or msvc, you can open `factory` inside your favorite IDE. We dropped some specific configurations file into it for you to use your best environement at your adavantage.

> [!NOTE]
> The users familiar with CMake can update the CMakeLists.txt at their advantage, include other source files, use their own CMake generator or C++ compiler or even add external libraries ...

### <a name="how-can-i-load-my-contract-?">📺 How can I load my contract ?</a>

<div align="left">
  <div>
    <img src="capture/Capture5.PNG" width="700" height="1000"/>
  </div>
</div>

### <a name="how-can-i-move-my-contract-?">📺 How can I move my contract ?</a>
### <a name="how-can-i-edit-my-fixings-?">📺 How can I edit my fixings ?</a>

## <a name="missing-a-specific-feature-?">🤝 Missing a specific feature ?</a>

The project is very far from being complete (and will probably never be ...) and a loads of features are still missing. This is why our developpers are working continuously to enrich the list of available functionalities. Feel free to share your ideas! We are happy to discuss with you about your personnal needs and the feasibility of your project.

> [!NOTE]
> If your idea is considered as doable by our team, be sure that your request will be added to our stack. But please kindly understand that we cannot give any ETA since our developers are working for `qa` as volunteers aside their job and our backlog is already populated by a thousand of new fields to explore.

## <a name="found-a-bug-?">🔎 Found a bug ?</a>

Feel free to report your issue with a respective title and an understandable description here [issues](https://github.com/matt-charr/qa-demo/issues). For any questions, you can always reach out to us directly via our [twitter](https://twitter.com/matt_charr) or post your question on [QuantStackExchange](https://quant.stackexchange.com/questions/tagged/qa) with the official `qa` tag.

> [!IMPORTANT]
> `qa` embbeds a mecanism to save and open your current mockup for further usage. If possible please attach your mockup file together with the relevant data json files and contract cpp/json files in your issue, it helps our developpers to reproduce the bug and increase the chances for us to be sort it quickly.

# <a name="licence">📜 Licence</a>

```text
Copyright (C) 2023 Matthieu Charrier. All rights reserved.
This file is part of the project QA - Quantitative Analytics.
Hence the latter remains the exclusive property of its author.
Accordingly, no part of this document may be used in any form for professional or commercial purposes
without the express permission of Matthieu Charrier.
```