{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system:
        let
          pkgs = import nixpkgs {
            inherit system;
            config.allowUnfree = true;
          };
        in
        f { inherit pkgs system; }
      );
    in
    {
      devShells = forEachSupportedSystem ({ pkgs, system }: {
        default = pkgs.mkShell {
          venvDir = ".venv";

          packages = with pkgs; [
            python312Full
            xorg.libX11
            xorg.xrandr
          ] ++ (with pkgs.python312Packages; [
            pynput
            pillow
            pip
            openai
            platformdirs
            pystray
            copykitten
            venvShellHook
          ]);

          # venvShellHook = ''
          #   echo "Setting up Python virtual environment in .venv"
          #   pip install --upgrade pip
          #   pip install copykitten
          # '';
        };
      });
    };
}
