function {
    emulate -LR zsh

    if (( ! ${path[(I)${0:A:h}/bin]} )); then
        path+=(${0:A:h}/bin)
    fi

    local code='
function wdx {
    emulate -LR zsh
    local output
    output="$(WDX --shell "$@")" || return $?
    eval "$output"
}'
    eval ${code//WDX/${(q)0:A:h}/bin/wdx}
}
