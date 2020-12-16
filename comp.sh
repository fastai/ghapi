#!/bin/zsh
_do_ghapi_completions()
{ 
    COMP="$(completion-ghapi "${COMP_WORDS[1]}")"
    COMPREPLY=($COMP)
}

complete -F _do_ghapi_completions ghapi
