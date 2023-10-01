This project is pretty stable so there is not much to say.

## Making a new release

I am writing this down because otherwise I am going to forget how to
do it.

* Edit the changelog to change the `Unreleased` section to a new tag.
  Use semver to decide the new version number.
* Change the version number to the new version in the `version`
  subcommand output in the Python script `bin/wdx`.
* Push the commit and tag.
* Create a GitHub Release for the new tag and copy the relevant
  changelog section into its text. Reformat it so that the line breaks
  are okay.
* Push a new commit adding `-devel` to the `version` subcommand
  output.
