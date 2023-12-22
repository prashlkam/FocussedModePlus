# flake.nix

{
  description = "My Python Flake with PyQt5 and pygame";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixpkgs-unstable;
  };

  outputs = { self, nixpkgs }:
    let
      pythonVersion = "3.11";
    in
    nixpkgs.legacyPackages.${pythonVersion}.mkPython {
      pname = "my-python-environment";
      version = "1.0";

      nativeBuildInputs = [ nixpkgs.pyqt5 nixpkgs.pygame ];

      meta = with nixpkgs.lib; {
        description = "My Python Environment";
        license = licenses.mit;
      };
    };
}

