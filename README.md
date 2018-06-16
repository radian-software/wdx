**`wdx`**: like [`wd`][wd] but different.

## Summary

`wdx` is a Zsh plugin which allows you to designate directories with
abbreviations, and later use those abbreviations to jump to the
directories.

## Installing

The easiest way to install `wdx` is using [zplug]:

    $ zplug raxod502/wdx

Otherwise, you can install `wdx` manually:

* Clone the `wdx` source repository.
* Add the `bin` subdirectory to your PATH.
* Source the file `wdx.zsh` in your `~/.zshrc`.

## Basic usage

Here is the command syntax:

    usage: wdx [-s | --shell] <subcommand>

    subcommands:
      wdx [go] <point>
      wdx show <point>
      wdx set [<point> [<target>]] [-f | --force]
      wdx rm [<point>]
      wdx ls
      wdx help [<subcommand>]
      wdx version

The subcommands are as follows:

* The `go` subcommand is used to `cd` to a target directory. If you
  don't give any subcommand, then `wdx` assumes you meant `go`.
* The `show` subcommand is used to print a target directory.
* The `set` subcommand is used to set a warp point. The `-f` or
  `--force` option allows you to overwrite an existing warp point by
  the same name.
* The `rm` subcommand is used to remove a warp point.
* The `ls` subcommand is used to print a list of all the defined warp
  point names. If you want to see the paths as well, you can just
  inspect the save file (see below).

Ambiguities are resolved like so:

* If the warp point name is omitted in the `set` or `rm` subcommands,
  then it defaults to the basename of the current directory
  (`/foo/bar` becomes `bar`).
* If the target directory is omitted in the `set` subcommand, then it
  defaults to the current directory.
* You must use `wdx go` explicitly in order to go to a warp point
  whose name is also a `wdx` subcommand.
* To deal with warp points and directories whose names begin with a
  hyphen, you can use the `--` argument to prevent following arguments
  from being interpreted as options.

The `-s`, `--shell` option causes `wdx` to print shell code to stdout
instead of performing the action directly. This feature is used
implicitly by the shell wrapper defined in `wdx.zsh`, so that the `go`
subcommand can actually change the working directory of your shell. It
is probably not much use to the end user, unless you are bypassing the
shell wrapper and working directly with the `wdx` script in the `bin`
subdirectory.

## Save file format

Your warp points are put in `$XDG_CONFIG_HOME/wdx/points`, or by
default `~/.config/wdx/points`.

The file format is plain-text. Lines alternate between warp point
names and target directories. Any characters except newlines are
allowed in point names and target paths. In particular, empty strings
are allowed. Points are sorted first by target path, and then by point
name.

Editing the save file by hand is encouraged if you rename a parent
directory, which will otherwise break your warp points.

Note that warp point targets need not be absolute paths. They are not
resolved at any time, but are saved and passed to `cd` unmodified.

## Tips

You can use `wdx` with the name `wd` instead, simply by defining

    alias wd=wdx

in your `.zshrc`.

## Why?

Because I thought the command-line interface of [`wd`][wd] was a bit
messy, and it didn't allow for arbitrary warp point names.

[wd]: https://github.com/mfaerevaag/wd
[zplug]: https://github.com/zplug/zplug
