#!/usr/bin/env zsh

# Boilerplate.
setopt err_return
setopt pipe_fail

# Configure environment correctly so wd is usable.
cd $0:A:h
path=(${PWD:A:h} $path)
source ../wd.zsh

# Configure wd.
export WD_SAVE_FILE=${PWD:A}/points

# Create a convenient function for testing some basic functionality on
# a weird warp-point name.
function test_roundtrip {
    rm -f $WD_SAVE_FILE
    echo "testing 'wd set'"
    wd set $1 $2
    echo "  ok"
    echo "checking save file"
    [[ $(< $WD_SAVE_FILE) == "$1|$2" ]]
    echo "  ok"
    echo "testing 'wd rm'"
    wd rm $1
    echo "  ok"
    echo "checking save file"
    [[ -z $(< $WD_SAVE_FILE) ]]
    echo "  ok"
}

point_names=(
    'foo'
    'bar'
    'baz quux'
    '!' '@' '#' '$' '%' '^' '&' '*' '(' ')' '[' ']' '{' '}'
    '-' '_' '=' '+' "\\" '"' "'" ';' ':' ',' '.' '<' '>'
    '?' '/' '`' '~' '1' '2' '3' '0' '${' ')(' '()' '[]' ']['
    '{}' '}{' $'\t' $'\0' "\n" "\t" "\0" $'\a' $'\b'
    '$WD_SAVE_FILE'
)

fail=
for point in $point_names; do
    echo '  testing'
    if test_roundtrip $point; then
        echo true
    else
        echo false
    fi
    echo '  finished'
    # if ! result="$(test_roundtrip $point)"; then
    #     echo -E "Failed roundtrip for point name ${(q-)point}:" 1>&2
    #     echo -E $result
    #     fail=yes
    # fi
done

if [[ -n $fail ]]; then
    exit 1
fi
