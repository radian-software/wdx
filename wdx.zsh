typeset wdx_dir
wdx_dir=${0:A:h}

function {
    emulate -LR zsh

    if (( ! ${path[(I)$wdx_dir]} )); then
        path+=($wdx_dir/bin)
    fi

    function wdx {
        emulate -LR zsh
        local output
        output="$(command wdx --shell "$@")" || return $?
        eval "$output"
    }
}
