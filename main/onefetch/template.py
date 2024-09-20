pkgname = "onefetch"
pkgver = "2.22.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "rust-std",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["bash", "git"]
pkgdesc = "Displays project information and code statistics"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://onefetch.dev"
source = f"https://github.com/o2sh/onefetch/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1741516c628bb70b432285aa78439c4acfeb5df19e48b8d85dba5f71336e190b"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"onefetch.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/onefetch",
                "--generate",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_man("docs/onefetch.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"onefetch.{shell}", shell)