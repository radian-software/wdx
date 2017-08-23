function wdx {
    emulate -LR zsh
    local -a output
    output=("${(@f)$(${${functions_source[wdx]}:A:h}/wdx.py wdx $@)}") || return $?
    if [[ $output[1] == cd ]]; then
        cd $output[2]
    elif [[ $output[1] == echo ]]; then
        for line in ${output[2,-1]}; do
            echo $line
        done
    elif [[ $output[1] != nop ]]; then
        echo "wdx: Internal error: Unexpected protocol" 1>&2
        return 1
    fi
}
