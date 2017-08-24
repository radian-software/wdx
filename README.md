**`wdx`**: like [`wd`] but different.

## Summary

`wdx` allows you to designate directories with abbreviations, and
later use those abbreviations to jump to the directories.

## Installing

I recommend using [zplug]:

    $ zplug raxod502/wdx

Else you can clone this repository and source `wdx.zsh` in your
`.zshrc`. There is only support for Zsh at the moment, but that is
easy to change.

If you export `WDX_NAME` before sourcing `wdx.zsh`, then the function
is defined with that name, rather than `wdx`. Example:

    $ export WDX_NAME=wd

`wdx` doesn't need `WDX_NAME` to be defined after you've sourced
`wdx.zsh`.

## Usage

Set a warp point to the current directory, using the basename of the
directory as the point name:

    $ wdx set

Use an alternative point name:

    $ wdx set <name>

Set a warp point to a particular directory:

    $ wdx set <name> <target-directory>

The command will abort if the warp point already exists and it points
to a different directory. Override that:

    $ wdx set -f

If `-f` is present, it's assumed to be a flag. `-f` may be repeated,
with no special effect. To override this, everything after a `--` is
taken literally.

Jump to a warp point:

    $ wdx go <point>

Shorthand, if the point name is not also a `wdx` subcommand:

    $ wdx <point>

Show the target of a warp point:

    $ wdx show <point>

Delete a warp point (defaults to basename of current directory):

    $ wdx rm [<point>]

Misc:

    $ wdx help [<subcommand>]
    $ wdx version

## Protips

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

## Why?

Because I thought the command-line interface of [`wd`] was a bit
messy, and it didn't allow for arbitrary warp point names.

[wd]: https://github.com/mfaerevaag/wd
[zplug]: https://github.com/zplug/zplug
