<div align="center">
  <div>
    <img src="LOGO.png" width="900" height="200"/>
  </div>
</a>

# QA

<em>Design, monitor and price your own exotic financial derivatives contracts.</em>

</div>

## 🍺 Project Status

<table class="no-border">
  <tr>
    <td><a href="https://github.com/matt-charr/qa-demo/stargazers">
    <img src="https://img.shields.io/github/stars/matt-charr/qa-demo?style=social"></td>
    <td><a href="https://github.com/matt-charr/qa-demo/network/members">
    <img src="https://img.shields.io/github/forks/matt-charr/qa-demo?style=social"></td>
    <td><a href="https://github.com/matt-charr/qa-demo/watchers">
    <img src="https://img.shields.io/github/watchers/matt-charr/qa-demo?style=social"></td>
  <tr>
    <td><a href="https://twitter.com/matt_charr" alt="twitter"><img src="https://img.shields.io/twitter/follow/matt-charr?style=social" alt="twitter"></a></td>
    <td><a href="https://www.youtube.com/c/qacom" alt="youtube"><img src="https://img.shields.io/badge/youtube-d95652.svg?style=flat-square&logo=youtube" alt="youtube"></a></td>
    <td><a href="https://www.twitch.tv/mattcharr" alt="twitch"><img src="https://img.shields.io/badge/twitch-d51561.svg?style=flat-square&logo=twitch" alt="twitch"></a></td>
    <td><a href="https://www.linkedin.com/in/matthieu-charrier-080820134/" alt="linkedin"><img src="https://img.shields.io/badge/linkedin-d00.svg?style=flat-square&logo=linkedin" alt="linkedin"></a></td>
  <tr>
  <tr>
    <td><img src="https://img.shields.io/badge/Solution-C++17-blue.svg?style=flat&logo=c%2B%2B&logoColor=b0c0c0&labelColor=363D44" alt="C++ solution"/></td>
    <td><img src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20Mac-blue??style=flat&logo=Linux&logoColor=b0c0c0&labelColor=363D44" alt="Operating systems"/></td>
  </tr>
</table>

⭐ Star the project on GitHub increases its visibility and helps it to progress

<td>
<h3>📰 Latest news (as of 2023-11-11) </h3>
<ul>
    <li>🔔(<strong>Release</strong>) <a href="https://github.com/matt-charr/qa-demo/releases/tag/v0.1.0">qa-v0.1.0</a> is out 🚀</li>
</ul>
</td>

<td>
<h3>👷 Current work (as of 2023-11-11) </h3>
<ul>
    <li>📗(<strong>Project</strong>) Handling early exercise feature. </li>
    <li>📙(<strong>Feature</strong>) Making PDE pricer framework.</li>
    <li>📘(<strong>Misc</strong>) Handling intraday fixings/payments/exercises.</li>
    <li>📕(<strong>Issue</strong>)</li>
</ul>
</td>

## 🤖 Introduction

`QA-Quantitative Analytics` is a simple cross-platform GUI desktop application to design, inspect and price your own exotic financial derivatives contract. The project is an ecosystem of the following repositories:

### qa-dev (*private*)

This is the core repository of the project, its access is restricted to our developpers only.
`qa-dev` is a repo that contains:

- **qalib** -- A library which handles modeling and pricing.

- **qapp** -- A front-end library through which the user can send requests to `qa` and have a nice view on the outputs.

- **qalgebra** -- `qa` uses the power of algebraic contract description to build a contract. `qalgebra` is a library that implements a custom language easily understandable to `qa` and the users to describe step by step and block by block all the events that occurs during the contract lifetime. 

### qa-data (*private*)

coming soon

### [qa-payoff](https://github.com/matt-charr/qa-payoff) (*public*)

For the users to benefit `qalgebra` technology and price their own contracts, our developpers created `qa-payoff`, a friendly factory where all programmer enthusiasts can use and contribute its favorite observable/payoff functions to eventually load, monitor, inspect and price it from `qapp`. This game room is yours, feel free to populate and use it at your convenience.

# ⚡️ Quick Start

- Download the [latest release](https://github.com/matt-charr/qa-demo/releases) and select the package corresponding to your configuration, the package name should looks like: <br> <br> `QA-{MAJOR}.{MINOR}.{PATCH}_{OS}_{COMPILER}-{MAJOR}.{MINOR}.{PATCH}_{BUILD_TYPE}` <br>
<ins>ex</ins>: <em>QA-0.1.0_Windows_GNU-13.1.0_Release</em>

# 🙌 Contributions

1. [Fork](https://github.com/matt-charr/qa-payoff) the master branch of `qa-payoff`.
2. Clone the repo.
```bash
git clone https://github.com/{my_github_username}/qa-payoff
```
1. Add your files if any and commit your change.
```bash
git add {my_file}
git commit -am "{my_commit_message}"
```
1. Push your commit.
```bash
git push origin master
```
1. Submit your [pull request](https://github.com/matt-charr/qa-payoff).

> [!IMPORTANT]  
> If possible you can kindly add a contract cpp file that uses your new feature.

> [!NOTE]  
> Review + Validation + Merge <= 1w

# 💻 Insights

## 🍏 Build

We are using [CMake](https://cmake.org/) as a build system and our code base is located on a private repository which access is restricted to our developers only. <br> 
After cloning the project for the first time, we configure and build an embedded CMake project that uses superbuild feature of CMake to clone, build and install all the dependencies that `qa` needs into a dedicated folder. <br>

It is to the following projects that we owe our heartfelt thanks for their generous contribution.

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

## 🍊 Tests

Once an issue, feature or project is sorted, a new unit test is required to be submitted to the test suite together with a contract source code that replicates the expected behavior of the code change. To ensure that the code change effect is not broken by any subsequent modifications, We use the service of [GoogleTest]() as a testing framework.

## 🍈 Continuous Integration

`qa` embbeds a custom GitHub action that runs at each pull requests. Once triggered, build and tests are running on Windows, Linux and MacOS remote machines in Debug/Release mode with the following configurations:

| Name                          | OS             | CMake         | Generator             | Architecture | Build Type | Compiler            | Status |
| ----------------------------- | -------------- | ------------- | --------------------- | ------------ | ---------- | ------------------  | --- |
| Windows-Release               | windows-latest | CMake-v3.27.2 | MinGW Makefiles       |              | Release    | GCC-13.2.0          | ✅  |
| Windows-Debug                 | windows-latest | CMake-v3.27.2 | Visual Studio 17 2022 | x64         | Debug      | MSVC-v19.30.30709.0 | ✅  |
| Linux-Release                 | ubuntu-latest  | CMake-v3.27.2 | Unix Makefiles        |              | Release    | GCC-v13.2.0         | ✅  |
| Linux-Debug                   | ubuntu-latest  | CMake-v3.27.2 | Unix Makefiles        |              | Debug      | GCC-v13.2.0         | ✅  |
| MacOS-Release                 | macos-latest   | CMake-v3.27.2 | Unix Makefiles        |              | Release    |                     | ✅  |
| MacOS-Debug                   | macos-latest   | CMake-v3.27.2 | Xcode                 |              | Debug      |                     | ✅  |

A dev branch is merged if and only if all builds and tests passed on all configurations.

## 🍇 Continuous Delivery

Our team delivers a release or a patch once a week, and strives to respect as closely as possible the [semantic versioning](https://semver.org/).
To publish a new release on each OS, we execute a shell script hosted on `qa-release` a remote repository that installs `qapp` executable, `qalgebra` library and `qa` runtime dependencies to a specific folder and push it to [qa-demo](https://github.com/matt-charr/qa-demo) repository.

> [!NOTE]
> `qa` has subscribed to a remote VPS (KVM2 plan - 100Go) provided by [Hostinger](https://www.hostinger.fr) to run builds and tests on Linux OS.

> [!IMPORTANT]
> We are far from being CD experts and know that our solution looks like a rush, better ways of releasing probably exist such as deploying binaries to a more convenient location than GitHub or building on a dedicated production environement. You are more than welcome to suggest improvements or just simply share your CD work styles. 

# 🌴 Features

## 📝 List of available features

Coming soon ...

## 🤝 Missing a specific feature ?

The project is very far from being complete (and will probably never be ...) and a loads of features are still missing. This is why our developpers are working continuously to enrich the list of functionalities. Feel free to share your idea. We are happy to discuss with you about your personnal needs and the feasibility of your project.

> [!NOTE]
> If your idea is considered as doable by our team, be sure that your request will be added to our stack. But please kindly understand that we cannot give any ETA since our developers are working for `qa` as volunteers aside their job and our backlog is already populated by a thousand of new fields to explore.

## 🔎 Found a bug ?

Feel free to report your issue with a respective title and an understandable description here [issues](https://github.com/matt-charr/qa-demo/issues). For any questions, you can always reach out to us directly via our [twitter](https://twitter.com/matt_charr) or post your question on [QuantStackExchange](https://quant.stackexchange.com/questions/tagged/qa) with the official `qa` tag.

> [!IMPORTANT]
> `qa` embbeds a mecanism to save and open your current mock-up for further usage. If possible please attach your [mock-up](video youtube) file together with the relevant data json files and contract cpp files in your issue, it helps our developpers to reproduce the bug and increase the chances for us to be sort it quickly.

# 📜 Licence

```text
Copyright (C) 2023 Matthieu Charrier <matthieu.charrier.pro@gmail.com>.
All rights reserved.
This GitHub repository is part of the project QA - Quantitative Analytics.
Hence the latter remains the exclusive property of its author.
Accordingly, no part of this document may be used in any form for professional or commercial purposes without the express permission of Matthieu Charrier.
```