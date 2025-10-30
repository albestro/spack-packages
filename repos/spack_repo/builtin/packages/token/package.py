# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install token
#
# You can edit this file again by typing:
#
#     spack edit token
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Token(CMakePackage):
    """Utilities for string tokenization"""

    homepage = "https://gitlab.kitware.com/utils/token"
    git = "https://gitlab.kitware.com/utils/token.git"

    license("BSD-3-Clause", checked_by="albestro")

    version("master")

    depends_on("nlohmann-json")

    def cmake_args(self):
        args = []
        return args
