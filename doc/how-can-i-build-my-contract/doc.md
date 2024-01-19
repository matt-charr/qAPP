# 📺 How can I build my contract ?

> [!NOTE]
> <strong>You need to have any kind of C++ compiler together with a recent CMake version installed in your machine to perform the following actions.</strong>
>```bash
># Ensure you have a C++ compiler installed in your machine!
>g++ --version
>
># Ensure you have a recent CMake version installed in your machine!
>cmake --version
>```

1. Open your terminal and go to <em>qa/factory</em> directory, take a first look at the file <em>qa/factory/examples/autocall.cpp</em> and take your time to observe what the language looks like and how to use it to build your own contract. The syntax is intuitive enought not to provide any more explanations for it.

```bash

# go to factory.
cd factory 

# let's see how it looks like.
vim examples/autocall.cpp
```

2. Once your contract cpp file is ready, you can generate your contract json file by running the following commands:

```bash

# configure.
cmake -S . -B ./build -G "MinGW Makefiles" -DMAIN="examples/autocall.cpp"

# build.
cmake --build ./build

# run.
./bin/run
```

or just by executing the shell:

```bash

# configure, build and run.
./scripts/build.sh examples/autocall.cpp

```

> [!NOTE] 
> If you are in the <em>Code</em> team, you can just 
> open the <em>factory</em> folder with <em>Code</em>, go to your cpp file > (<em>Ctrl+P</em>), hit <em>ctrl+F5</em> and select the action <em>build</em>.

> [!NOTE] 
> If you are in the <em>Visual Studio</em> team, you can 
> open the <em>factory</em> folder with <em>Visual Studio</em>, build the solution and execute the target <em>run.exe</em>.

3. You can now check that the contract json file has been create with success.

```bash
# check that json file exists.
vim examples/autocall.json
```

Congratulations! You built your first contract.
Once you are familiar enough with the syntax, feel free to update your contract cpp file at your convenience or even create your own designed contract cpp files and generate their respective contract json file!

> [!NOTE]
> Your configuration file for your IDE is missing ? [Ask for it!](https://GitHub/matt-charr/qa-demo/issues)

> [!NOTE]
> The users familiar with CMake can update the <em>qa/factory/CMakeLists.txt</em> at their advantage, include other source files, use their own CMake generator or C++ compiler or even add libraries to link their code with external resources.
