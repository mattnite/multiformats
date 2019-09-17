import os

from conans import ConanFile, CMake, tools


class MultiformatsTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "gtest/1.8.1@bincrafters/stable", "multiformats/0.1@matt1795/testing"
    def configure(self):
        self.options["gtest"].build_gmock = False

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(source_folder=self.source_folder)
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            self.run("bin%sMultiformatsTests --gtest_output=\"xml:results.xml\"" % os.sep)
