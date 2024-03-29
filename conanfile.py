from conans import ConanFile, CMake, tools


class MultiformatsConan(ConanFile):
    name = "multiformats"
    version = "0.1"
    license = "MIT"
    author = "Matthew Knight mgk1795@gmail.com"
    url = "https://github.com/matt1795/multiformats"
    description = "C++"
    homepage = "https://multiformats.io/"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    requires = "OpenSSL/1.1.1b@conan/stable"
    generators = "cmake_find_package", "cmake"
    exports_sources = "*"

    def configure(self):
        if self.settings.compiler in ["gcc", "clang"] and self.settings.compiler.libcxx != "libstdc++11":
            raise Exception("need to use libstdc++11 for compiler.libcxx")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_folder)
        cmake.build()

    def package(self):
        self.copy("include/*.hpp", dst=".")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["multiformats"]
