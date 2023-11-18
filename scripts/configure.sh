cmake -S . -B ./build -G "MinGW Makefiles" \
    -DCMAKE_BUILD_TYPE=Release \
    -DLIB_NAME="my_qalgebra" \
    -DCMAKE_PREFIX_PATH="" \
    -DCMAKE_INSTALL_PREFIX="" \