function {
    emulate -LR zsh
    local code='
function WDX {
    emulate -LR zsh
    local -a output
    output=("${(@f)$(${${functions_source[WDX]}:A:h}/wdx.py WDX $@)}") || return $?
    if [[ $output[1] == cd ]]; then
        cd -- $output[2]
    elif [[ $output[1] == echo ]]; then
        for line in ${output[2,-1]}; do
            echo $line
        done
    elif [[ $output[1] != nop ]]; then
        echo "WDX: Internal error: Unexpected protocol" 1>&2
        return 1
    fi
}'
    eval ${code//WDX/${WDX_NAME:-wdx}}
}
