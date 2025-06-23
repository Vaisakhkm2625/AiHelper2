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
        };
      });
      
      packages = forEachSupportedSystem ({ pkgs, system }: {
        default = pkgs.writeShellScriptBin "aihelper" ''
          export PATH="${pkgs.python312Full}/bin:${pkgs.python312Packages.pynput}/bin:$PATH"
          export PYTHONPATH="${pkgs.python312Packages.pynput}/${pkgs.python312.sitePackages}:${pkgs.python312Packages.pillow}/${pkgs.python312.sitePackages}:${pkgs.python312Packages.openai}/${pkgs.python312.sitePackages}:${pkgs.python312Packages.platformdirs}/${pkgs.python312.sitePackages}:${pkgs.python312Packages.pystray}/${pkgs.python312.sitePackages}:${pkgs.python312Packages.copykitten}/${pkgs.python312.sitePackages}:$PYTHONPATH"
          export LD_LIBRARY_PATH="${pkgs.xorg.libX11}/lib:${pkgs.xorg.xrandr}/lib:$LD_LIBRARY_PATH"
          cd ${./.}
          exec ${pkgs.python312Full}/bin/python main.py "$@"
        '';
      });
      
      apps = forEachSupportedSystem ({ pkgs, system }: {
        default = {
          type = "app";
          program = "${self.packages.${system}.default}/bin/aihelper";
        };
      });
    };
}
