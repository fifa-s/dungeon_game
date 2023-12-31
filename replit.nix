{ pkgs }: {
	deps = [
		pkgs.nodePackages.prettier
    pkgs.python310Full
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
	];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath ([
      # Neded for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
    ] ++ (with pkgs.xorg; [ libX11 libXext libXinerama libXcursor libXrandr libXi libXxf86vm ]));
    PYTHONHOME = "${pkgs.python310Full}";
    PYTHONBIN = "${pkgs.python310Full}/bin/python3.10";
    LANG = "en_US.UTF-8";
    STDERREDBIN = "${pkgs.replitPackages.stderred}/bin/stderred";
    PRYBAR_PYTHON_BIN = "${pkgs.replitPackages.prybar-python310}/bin/prybar-python310";
  };
}