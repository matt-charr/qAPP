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
    <td><img src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux-blue??style=flat&logo=Linux&logoColor=b0c0c0&labelColor=363D44" alt="Operating systems"/></td>
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

# 🙌 Contributions

Coming soon ...

# 💻 Insights

## 🍯 Work Style

Once a bug or a new feature is submitted, an issue is created with the corresponding flag (bug, feature, project, creation). 
Once picked from the stack, a dev branch is created, comes down locally to the developper machine and this is where the fun begins 😃

## 🍏 Build

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

## 🍊 Tests

At the end of each dev session, a new unit test is required to be submitted to the test suite together with a contract file that replicates the expected behavior of the code change. To ensure that the code change effect is not broken by any subsequent modifications, we use the service of [GTest]() as a testing framework.

## 🍈 Continuous Integration

`qa` embbeds a custom GitHub action that runs at each pull requests. Once a pull request is submitted, build and tests are triggered on our Windows and Linux self-hosted runners in Debug/Release mode with the below configurations. A dev branch is merged if and only if all builds and tests passed on all configurations.

| Name                          | OS             | CMake         | Generator             | Architecture | Build Type | Compiler            | Status  |
| ----------------------------- | -------------- | ------------- | --------------------- | ------------ | ---------- | ------------------  | ------- |
| Windows-Release               | windows-latest | CMake-v3.27.2 | MinGW Makefiles       |              | Release    | GCC-13.2.0          | ✅     |
| Windows-Debug                 | windows-latest | CMake-v3.27.2 | Visual Studio 17 2022 | x64          | Debug      | MSVC-19.30.30709.0  | ✅     |
| Linux-Release                 | ubuntu-latest  | CMake-v3.27.2 | Unix Makefiles        |              | Release    | GCC-11.4.0          | ✅     |
| Linux-Debug                   | ubuntu-latest  | CMake-v3.27.2 | Unix Makefiles        |              | Debug      | GCC-11.4.0          | ✅     |
| MacOS-Release                 | macos-latest   | CMake-v3.27.2 | Unix Makefiles        |              | Release    |                     | ❌     |
| MacOS-Debug                   | macos-latest   | CMake-v3.27.2 | Xcode                 |              | Debug      |                     | ❌     |

> [!NOTE]
> `qa` has subscribed to a remote VPS (KVM2 plan - 100Go) provided by [Hostinger](https://www.hostinger.fr) to run builds, tests and deployment on Linux. We could not find any server providers to run our builds and tests on MacOS and are listening to any suggestions 😃.

## 🍇 Continuous Delivery

Our team delivers a release or a patch on a regular basis, and strives to respect as closely as possible the [semantic versioning](https://semver.org/).
To publish a new release, each tag created on our developement repository triggers a github actions that for each OS supported will create and upload the package to [qa-demo](https://github.com/matt-charr/qa-demo).

> [!IMPORTANT]
> We are far from being CD experts and know that our solution looks like a rush, better ways of releasing probably exist such as deploying binaries to a more convenient location than GitHub or building on a dedicated production environement. You are more than welcome to suggest improvements or just simply share your CD work styles. 

# 🌴 Features

## 📝 List of available features

### 📺 How can I build my contract ?

- Create a new cpp file into `factory` directory:

```cd qalgebra```
```touch my_contract.cpp```

### 📺 How can I report my issue ?

## 🤝 Missing a specific feature ?

The project is very far from being complete (and will probably never be ...) and a loads of features are still missing. This is why our developpers are working continuously to enrich the list of available functionalities. Feel free to share your ideas! We are happy to discuss with you about your personnal needs and the feasibility of your project.

> [!NOTE]
> If your idea is considered as doable by our team, be sure that your request will be added to our stack. But please kindly understand that we cannot give any ETA since our developers are working for `qa` as volunteers aside their job and our backlog is already populated by a thousand of new fields to explore.

## 🔎 Found a bug ?

Feel free to report your issue with a respective title and an understandable description here [issues](https://github.com/matt-charr/qa-demo/issues). For any questions, you can always reach out to us directly via our [twitter](https://twitter.com/matt_charr) or post your question on [QuantStackExchange](https://quant.stackexchange.com/questions/tagged/qa) with the official `qa` tag.

> [!IMPORTANT]
> `qa` embbeds a mecanism to save and open your current mockup for further usage. If possible please attach your mockup file together with the relevant data json files and contract cpp/json files in your issue, it helps our developpers to reproduce the bug and increase the chances for us to be sort it quickly.

# 📜 Licence

```text
Copyright (C) 2023 Matthieu Charrier. All rights reserved.
This file is part of the project QA - Quantitative Analytics.
Hence the latter remains the exclusive property of its author.
Accordingly, no part of this document may be used in any form for professional or commercial purposes
without the express permission of Matthieu Charrier.
```