let
   nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
   pkgs = import nixpkgs {config = {}; overlays = [];};
in

pkgs.mkShell {
  packages = with pkgs; [
  python3
  python311Packages.pygame
  python311Packages.pyqt5
  git
  ];
}
