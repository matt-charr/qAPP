<h1 align="center">
<img src="img/logo.png" width="900" height="300"/>
</h1><br>

<tr>
  <td><a href="https://github.com/matt-charr/qa-demo/stargazers">
  <img src="https://img.shields.io/github/stars/matt-charr/qa-demo?style=social"></td>
  <td><a href="https://github.com/matt-charr/qa-demo/network/members">
  <img src="https://img.shields.io/github/forks/matt-charr/qa-demo?style=social"></td>
  <td><a href="https://github.com/matt-charr/qa-demo/watchers">
  <img src="https://img.shields.io/github/watchers/matt-charr/qa-demo?style=social"></td>
  <td><a href="https://github.com/matt-charr/qa-demo/issues">
  <img src="https://img.shields.io/github/issues/matt-charr/qa-demo?style=social"></td>
</tr>
<br>
<tr>
  <td><a href="https://twitter.com/matt_charr" alt="twitter"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a></td>
  <td><a href="https://www.twitch.tv/mattcharr" alt="twitch"><img src="https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white" alt="Twitch"></a></td>
  <td><a href="https://www.linkedin.com/in/matthieu-charrier-080820134/" alt="linkedin"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin"></a></td>
  <td><a href="https://github.com/matt-charr/" alt="GitHub"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a></td>
</tr>
<br>
<tr>
  <td><a href="" alt="C"><img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" alt="C"/></a></td>
  <td><a href="" alt="C++"><img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++"/></a></td>
  <td><a href="" alt="MariaDB"><img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="MariaDB"/></a></td>
</tr>
<br>
<tr>
  <td><a href="" alt="Windows"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows"/></a></td>
  <td><a href="" alt="Linux"><img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/></a></td>
  <td><a href="" alt="MacOS"><img src="https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white" alt="MacOS"/></a></td>
</tr>
<br>
<tr>
  <td><a href="" alt="GitHubActions"><img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHubActions"/></a></td>
  <td><a href="" alt="Hostinger"><img src="https://img.shields.io/badge/Linode-00A95C?style=for-the-badge&logo=Linode&logoColor=white" alt="Hostinger"/></a></td>
</tr>

# 🍺 Project Status

⭐ Star the project on GitHub helps it to progress.

<td>
<h3>📰 Latest news </h3>
<ul>
  <li> <ins>2024-03-25</ins>
<ul>
    <li> 🔔(<strong>Release</strong>) <a href="https://github.com/matt-charr/qa-demo/releases">qa-v0.3.1</a> is out 🚀</li>
</ul>
</ul>
</td>

<td>
<h3>👷 Current work </h3>
<ul>
<li> <ins>2024-03-25</ins>
<ul>
    <li>📗(<strong>Long Term Project</strong>) Implementing Longstaff-Schwartz algorithm. </li>
    <li>📙(<strong>Short Term Project</strong>) Making templates for some standard contracts</li>
    <li>📕(<strong>Issue</strong>) Fixing stack overflow at deep contract motion time</li> 
    <li>📘(<strong>Misc</strong>) Computing delta (sticky delta) and cega with AAD</li>
</ul>
</ul>
</td>

<td>
<h3>🏆 Achievements </h3>
<ul>
<li> <ins>2024-01-11</ins>
<ul>
    <li>📗(<strong>Long Term Project</strong>) Generic PDE pricer handles choosing style features.</li>
    <li>📙(<strong>Short Term Project</strong>) Released the C API</li>
    <li>📕(<strong>Issue</strong>) Set MacOS release package</li>
    <li>📘(<strong>Misc</strong>) Implemented qapy, a python project to design and generate your contract.</li>
</ul>
</ul>
</td>

## 📋 Table of Contents

1. 💥 [Genesis](#genesis)
2. ⚡️ [Quick Start](#quick-start)
3. 🌴 [Features](#features)
   1. 📝 [List of features](#list-of-features)
   2. 🤝 [Missing a specific feature ?](#missing-a-specific-feature-?)
   3. 🔎 [Found a bug ?](#found-a-bug-?)
4. 🙌 [How can I contribute ?](#how-can-i-contribute-?)
5. 💻 [Insights](#insights)
   1. 🍯 [Developement](#developement)
   2. 🍏 [Build](#build)
   3. 🍊 [Tests](#tests)
   4. 🍈 [Continuous Integration](#continuous-integration)
   5. 🍇 [Continuous Delivery](#continuous-delivery)
6. 📜 [Licence](#licence)

# <a name="genesis">Genesis</a>

<div align="center">
<em>"Design, price and monitor your own exotic financial derivatives contracts"</em>
</div> <br>

🎮 `𝐪𝐀𝐏𝐏` (Quantitative Analytics Application) is a simple ecosystem of devices that helps the users to 𝑏𝑢𝑖𝑙𝑑, 𝑝𝑟𝑖𝑐𝑒 and 𝑎𝑛𝑎𝑙𝑦𝑠𝑒 customized financial derivatives contracts.

✍🏻 This flowcharts shows the architecture of the project together with which components the user can consume.

⏩ **𝑞𝐶𝑂𝑅𝐸** (<em>private</em>) is the aggregation of embedded private libraries in charge of implementing 𝘤𝘰𝘯𝘵𝘳𝘢𝘤𝘵, 𝘥𝘢𝘵𝘢, 𝘮𝘰𝘥𝘦𝘭 and 𝘱𝘳𝘪𝘤𝘦𝘳 architectures. Its codebase is hosted on a private GitHub repository which access is restricted to our developpers only.

⏩ **𝑞𝐴𝑃𝐼** (<em>public</em>) is the shared object that the user can plug into his or her personal project. A library of functions that request the core to perform generic actions such as getting contract information, getting price and greeks ...

⏩ **𝑞𝐿𝐴𝑁𝐺** (<em>public</em>) is the internal contract description that uses the power of domain-specific language. A language easily understandable by human and machine to design your contract from a self-explanatory script. The whole ecosystem is built around this.

⏩ **𝑞𝐺𝑈𝐼** (<em>public</em>) is the up and running GUI desktop application from which the user requests the API and visualize the results through a modern graphical interface.

![Architecture](https://github.com/matt-charr/qa-demo/assets/68332647/9282f0f0-2023-4d25-9ba6-aef13b857a2d)

# <a name="quick-start">⚡️ Quick Start</a>

To download the latest version of our application, go to [Releases](https://github.com/matt-charr/qa-demo/releases) and download the asset that corresponds to your operating system. After extracting all the files into a nice location of your machine, you are falling onto a folder that contains `qAPP` directory. Open the `qGUI` executable located at <em>qa/bin</em> and you arrive to the main page. 

On the left hand side of the screen is located a logger that displays the messages that `qCORE` returns after each actions.

Each action triggers by `qGUI` - typically pressing a button - throws <FONT COLOR="BLUE"><em>information</em></FONT>, <FONT COLOR="GREEN"><em>warnings</em></FONT>, <FONT COLOR="ORANGE"><em>errors</em></FONT> and/or <FONT COLOR="RED"><em>exceptions</em></FONT>.
- If an <FONT COLOR="RED"><em>exception</em></FONT> is thrown, it means something went wrong dev side. In that case please [report your issue](https://github.com/matt-charr/qa-demo/issues) by dropping your `mockup` file together with your contract and data json files if any (see [How can I report my issue](features/how-can-i-report-my-issue/doc.md)).
- If an <FONT COLOR="ORANGE"><em>error</em></font> is thrown, it means that something went wrong user side and `qCORE` did not manage to perform your request. In that case you need to check the log and correct your request accordingly.
- If a <FONT COLOR="GREEN"><em>warning</em></font> is thrown, it means that something went wrong user side but `qCORE` managed to perform the request.
At inception, an action always thrown an <FONT COLOR="BLUE"><em>information</em></FONT> message to the user such as "Pricing contract...", the goal is to inform what action `qGUI` is performing.
When the action is over, a <FONT COLOR="YELLOW"><em>success</em></font> is thrown if an only if no error or exception occured during the action lifetime.

# <a name="features"> 🌴 Features</a>

## <a name="list-of-features">📝 List of features</a>

1. 📺 [Dictionary](doc/dictionary.md)
2. 📺 [How can I design my contract ?](doc/how_can_i_design_my_contract.md)

## <a name="missing-a-specific-feature-?">🤝 Missing a specific feature ?</a>

The project is very far from being complete (and will probably never be ...) and a loads of features are still missing. This is why our developpers are working continuously to enrich the list of available functionalities. Feel free to [share your ideas](https://github.com/matt-charr/qa-demo/issues) under the tag <em>features</em> ! We are happy to discuss with you about your personnal needs and the feasibility of your project.

> [!NOTE]
> If your idea is considered as doable by our team, be sure that your request will be added to our stack. But please kindly understand that we cannot give any ETA since our developers are working for `qAPP` as volunteers aside their job and our backlog is already populated by a thousand of new fields to explore.

## <a name="found-a-bug-?">🔎 Found a bug ?</a>

Feel free to [report your issue](https://github.com/matt-charr/qa-demo/issues) (see [How can I report my issue](features/how-can-i-report-my-issue/doc.md)) with a respective title and an understandable description. For any questions, you can always reach out to us directly via our [twitter](https://twitter.com/matt_charr) or post your question on [QuantStackExchange](https://quant.stackexchange.com/questions/tagged/qa) with the official `qAPP` tag.

> [!IMPORTANT]
> `qAPP` embbeds a mecanism to save and open your current `mockup` for further usage. If possible please attach your `mockup` file together with the relevant data json and contract external files in your issue, it helps our developpers to reproduce the bug and increase the chances for us to sort it quickly. See [How can I report my issue](features/how-can-i-report-my-issue/doc.md) for further details on how to proceed.

# <a name = "how-can-i-contribute-?"> 🙌 How can I contribute ?</a>

We are building a payoff base to:
- Challenge our tool and push it to its limits.
- Enhance our unit and integration tests.

We propose to every structured products and programmer enthusiasts to contribute its favorite payoff within a shared folder. Here is the process to follow:

- Design your contract (see [How can I design my contract](doc/how_can_i_design_my_contract.md))

- Fork and clone this repository.

```bash
git clone https://github.com/matt-charr/qa-demo.git
```

- Drop your contract python file(s) into <em>qa-demo/factory</em> folder.

```bash
mv my_contract.py qa-demo/factory/my_contract.py
```

- Commit, push and pull request.

```bash
cd qa-demo 
git commit -am "Added my contract"
git push origin master
```

# <a name="work-style">💻 Insights</a>

## <a name="developement"> 🍯 Developement</a>

Once a bug or a feature is submitted, an issue is created with the corresponding flag (<em>bug</em>, <em>feature</em>, <em>short project</em>, <em>long project</em>, <em>misc</em>). Once picked from the stack, a dev branch is created, comes down locally to the developper machine and this is where the fun begins 😃

## <a name="build"> 🍏 Build</a>

`qAPP` uses [CMake](https://cmake.org/) as a build system and has its main code base located on a private repository which access is restricted to our developers only. Besides, it relies on a bunch of repository dependencies that are required at `qAPP` build time. <br> 
It is to the following projects that we owe our heartfelt thanks for their generous open source contribution.

- [ImGui](https://github.com/matt-charr/imgui-for-qa)
- [ImPlot](https://github.com/matt-charr/implot-for-qa)
- [ImFileBrowser](https://github.com/matt-charr/imfilebrowser-for-qa)
- [MariaDB](https://github.com/matt-charr/mariadb-for-qa)
- [Curl](https://github.com/matt-charr/curl-for-qa)
- [OpenSSL](https://github.com/matt-charr/ssl-for-qa)
- [Glfw](https://github.com/matt-charr/glfw-for-qa)
- [JsonCpp](https://github.com/matt-charr/jsoncpp-for-qa)
- [Eigen](https://github.com/matt-charr/eigen-for-qa)

To load the below dependencies, `qAPP` uses the power of [superbuild](https://cmake.org/cmake/help/latest/module/ExternalProject.html) feature from CMake. For that purpose, an embedded CMake project is in charge of cloning, building and installing all the dependencies that `qAPP` requires into a specific folder. That's pretty cool, isn't it ? 😃

## <a name="tests"> 🍊 Tests</a>

In order to ensure that the code change effect is not broken by any subsequent modifications, at the end of each dev session, a new unit test is required to be submitted to the test suite together with a contract file that replicates the expected behavior of the code change.

## <a name = "continuous-integration">🍈 Continuous Integration</a>

`qAPP` embbeds a custom GitHub action that runs at each pull requests. Once a pull request is submitted, build and tests are triggered on our Windows, Linux and MacOS self-hosted runners in Debug/Release mode with the below configurations. A dev branch is merged if and only if all builds and tests passed on all tested configurations.

| Name        | OS           | Provider                              | RAM      | CMake        | CMake Generator       | Build Type      | Compiler           | Build Status |
| ----------- | ------------ | ------------------------------------  | -------- |------------- | --------------------- | --------------- | ------------------ | ------------ | 
| Win32-MinGW | Windows 10   | -                                     | 16.00 GB | CMake-3.28.3 | MinGW Makefiles       | Release & Debug | GCC-13.2.0         | ✅           |
| Win32-MSVC  | Windows 10   | -                                     | 16.00 GB | CMake-3.28.3 | Visual Studio 17 2022 | Release & Debug | MSVC-19.30.30709.0 | ✅           |
| Linux       | Ubuntu 22.04 | [Hostinger](https://www.hostinger.fr) |  8.00 GB | CMake-3.22.1 | Unix Makefiles        | Release & Debug | GCC-11.4.0         | ✅           |
| MacOS       | Sonoma 14.4  | [UltaHost](https://ultahost.com)      |  2.00 GB | CMake-3.28.3 | Unix Makefiles        | Release & Debug | CLANG-1500.3.9.4   | ✅           |

<h1 align="left">
<img src="img/build.png" width="300" height="250"/>
</h1><br>

## <a name="continuous-delivery">🍇 Continuous Delivery</a>

Our team delivers a release on a weekly basis:

- ~One <strong>major</strong> release per year (coming out with the current <em>long project</em>)
- ~One <strong>minor</strong> release per month (coming out with the current <em>short project</em>)
- ~One <strong>patch</strong> release per week (coming out with the current <em>issue</em>)
   
To publish a new release, each tag created on our developement repository triggers a github actions that for each OS supported will create and upload the package to [qa-demo](https://github.com/matt-charr/qa-demo).

<h1 align="left">
<img src="img/release.png" width="300" height="200"/>
</h1><br>

> [!IMPORTANT]
> We are far from being CD experts and know that our solution looks like a rush, better ways of releasing probably exist such as deploying binaries to a more convenient location than GitHub or building on a dedicated production environement. You are more than welcome to suggest improvements or just simply share your CD work styles. 

# <a name="licence">📜 Licence</a>

```text
Copyright © 2023 QA - Quantitative Analytics. All rights reserved.
This file is part of the project QA - Quantitative Analytics. 
Hence the latter remains the exclusive property of its author. 
Accordingly, no part of this document may be used or transmitted 
in any form for professional, educational or commercial purposes 
without the express permission of Matthieu Charrier.
```
