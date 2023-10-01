# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog].

## 2.1.1 (released 2023-09-30)
### Bugs fixed
* The autopushd setting is now respected if set in your Zsh
  configuration ([#5]).

[#5]: https://github.com/radian-software/wdx/issues/5

## 2.1.0 (released 2022-03-10)
### Enhancements
* Zsh completions are now available.

## 2.0.1 (released 2019-02-12)
### Bugs fixed
* If `~/.config/wdx/points` was a symlink, `wdx` previously replaced
  it with a regular file when writing it. This behavior has been
  fixed.

## 2.0 (released 2018-06-26)
### Breaking changes
* The `WDX_NAME` environment variable no longer affects the operation
  of `wdx.zsh`. If you wish to use `wdx` by another name, define an
  alias.
* Handling of command-line arguments and options is now much more
  consistent and robust. In particular, all arguments starting with a
  hyphen are now considered to be options, and are validated. The
  `--`, `--help`, and `--version` options (and similar) are accepted
  globally.

### New features
* Added a `wdx ls` command for listing warp points. This should be
  especially useful in scripts.

### Enhancements
* The command-line help is now much more sophisticated, and includes
  explanations of each subcommand as well as `wdx` as a whole.
* The Python script can now be used independently of the shell
  wrapper. This may be useful in scripting.
* Error messages have been rewritten.

### Bugs fixed
* `wdx` will now create parent directories of the warp point file if
  they are missing.

## 1.0 (released 2017-08-24)
### Added
* `wdx.py` script providing core functionality.
* `wdx.zsh` wrapper that can be used in Zsh via [zplug].
* Subcommands `go`, `show`, `set`, `rm`, `version`, `help`.
* MIT license and documentation.

[keep a changelog]: http://keepachangelog.com/
[zplug]: https://github.com/zplug/zplug
