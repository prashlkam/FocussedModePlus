# flake.nix

{
  description = "My Nix Flake for installing FocussedModePlus on linux...";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      pythonVersion = "3.11.5";
      pyqtVersion = "5.15.10";
      pygameVersion = "2.4.0";
      pkgs = import nixpkgs {};
    in
    {
      packages = pkgs.mkShell {
        buildInputs = [
          (pkgs.python37.override { version = pythonVersion; })
          (pkgs.pyqt5.override { version = pyqtVersion; })
          (pkgs.python37Packages.pygame.override { version = pygameVersion; })
        ];
      };
    };
}

