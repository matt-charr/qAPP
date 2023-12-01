# 📺 How can I build my contract ?

1. Please ensure you have a C++ compiler (MSBuild, g++, Clang, ...) and a recent CMake version installed in your machine.

```bash
# Ensure you have a C++ compiler installed in your machine!
g++ --version

# Ensure you have a recent CMake version installed in your machine!
cmake --version
```

2. Go to <em>factory</em> directory and if not already created, create a new cpp file in <em>examples</em> named <em>autocall.cpp</em>. Open it with your favorite editor to have a nice overview of what the language looks like and how to use it to build your own contract. The syntax is intuitive enought not to provide any more explanations for it.

```bash

# go to factory.
cd factory &&

# create examples/autocall.cpp.
touch examples/autocall.cpp &&

# let's see how it looks like.
vim examples/autocall.cpp
```

3. You can then generate your contract json file by running the following commands:

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
> If you are more familiar with vscode or msvc, you can open `factory` inside your favorite IDE. We dropped some specific configurations file into it for you to use your best environement at your advantage. Your configuration file for your IDE is missing ? [Ask for it!](https://GitHub/matt-charr/qa-demo/issues)

> [!NOTE]
> The users familiar with CMake can update the CMakeLists.txt at their advantage, include other source files, use their own CMake generator or C++ compiler or even add libraries to link their code with external resources.
