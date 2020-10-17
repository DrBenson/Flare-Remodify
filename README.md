
**Flare** engind **_Remodify_** project.
```
┎──────────────────────────────────────┒
┃       Remodify version: 1.1.0        ┃
┠──────────────────────────────────────┨
┃     This remodify based on Flare     ┃
┃(Free Libre Action Roleplaying Engine)┃
┖──────────────────────────────────────┛
```
  This is re-modify engine of flare game engine. Most are based on flare-engine source code.

** Folder description **
```
Flare-Remodify -------------------> This project home.
━┓
 ┣━┓flare ------------------------> Flare core and game mod.
 ┃ ┗━━━━┓
 ┃      ┣━┓android ---------------> Android package files.
 ┃      ┃ ┗━━━━━━━ Flare-*.apk ---> Flare core package.
 ┃      ┃
 ┃      ┗━┓bin -------------------> Executable binary files.
 ┃        ┗━━━┳━ Flare -----------> Executable binary for Linux.
 ┃            ┣━ Flare-i686 ------> Executable binary for Linux i686.
 ┃            ┣━ Flare-x64.exe ---> Executable binary for Windows.
 ┃            ┣━ Flare-mac-x64 ---> Executable binary for macOS x86_64.
 ┃            ┣━ Flare-win32.exe -> Executable binary for Windows win32.
 ┃            ┣━ lib -------------> SDL2 Library for Linux i686.
 ┃            ┣━ lib64 -----------> SDL2 Library for Linux.
 ┃            ┣━ libSDL2-win-x86 -> SDL2 Library for Windows.
 ┃            ┣━ libSDL2-win-x64 -> SDL2 Library for Windows win32.
 ┃            ┗━ libSDL2-mac -----> SDL2 Library for macOS i686.
 ┃
 ┗━┓dev --------------------------> Development source folder.
   ┗━━┳━ flare-engine ------------> Flare Action Roleplaying Engine(engine source code only).
      ┣━ empyrean_itemdef --------> Item generation script for Flare's Empyrean mod
      ┣━ flare_map_traverse ------> Map drawer/traversal for flare-game
      ┗━ tilesetdef-generator ----> Tool to convert tilesets embedded in a TMX to Flare's tileset format.
```
## Copyright and License

Most of Flare is Copyright © 2010-2013 Clint Bellanger.
Contributors retain copyrights to their original contributions.

Flare's source code is released under the GNU GPL v3. Later versions are permitted.

Flare's default mod (includes engine translations) is released under GNU GPL v3 and CC-BY-SA 3.0.
Later versions are permitted.

The default mod contains the Liberation Sans font which is released under the SIL Open Font License, Version 1.1.

The GNU Unifont font is released under GPL v2, with the exception that embedding the font in a document does not in itself bind that document to the terms of the GPL.

# Flare-Remodify 1.1.0

The Flare Game [Re-Modify](https://github.com/DrBenson/Flare-Remodify) Based on [Flare](http://flarerpg.org) Fantasycore and Empyrean Campaign Engine v1.1.61.

## Command-line Options

| Command           | Description
|-------------------|----------------
| `--help`          | Prints the list of command-line flags.
| `--version`       | Prints the release version.
| `--data-path`     | Specifies an exact path to look for mod data.
| `--debug-event`   | Prints verbose hardware input information.
| `--renderer`      | Specifies the rendering backend to use. The default is 'sdl\_hardware'. Also available is 'sdl', which is a software-based renderer.
| `--no-audio`      | Disables sound effects and music.
| `--mods`          | Starts the game with only these mods enabled.
| `--load-slot`     | Loads a save slot by numerical index.
| `--load-script`   | Execute's a script upon loading a saved game. The script path is mod-relative.
| `--safe-video`    | Launches with the minimum video settings.

## Links

The following links are specific to the original engine

* [Flare-Remodify](https://github.com/DrBenson/Flare-Remodify) --> https://github.com/DrBenson/Flare-Remodify
* [Homepage](http://flarerpg.org) --> http://flarerpg.org
* [Source](https://github.com/flareteam/flare-engine) ----> https://github.com/flareteam/flare-engine
* [Forums](http://opengameart.org/forums/flare) ----> http://opengameart.org/forums/flare
