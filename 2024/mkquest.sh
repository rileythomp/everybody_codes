#!/bin/sh

_mkquest() {
    local year_dir quest_dir
    case "${2-}" in
        ''|*[!0-9]*)
            printf '%s\n' 'Usage: source mkquest.sh <quest-number>' >&2
            return 1
            ;;
    esac

    year_dir=$(CDPATH= cd -- "$(dirname -- "$1")" && pwd) || return
    quest_dir="$year_dir/quests/$2"

    mkdir "$quest_dir" || return
    touch "$quest_dir/1.in" "$quest_dir/2.in" "$quest_dir/3.in" || return
    cp "$year_dir/quests/1/main.py" "$quest_dir/main.py" || return
    cd "$quest_dir"
}

# Both shells expose the sourced file's path differently; $0 is the shell itself.
if [ -n "${ZSH_VERSION-}" ]; then
    eval '_mkquest "${(%):-%x}" "$@"'
else
    _mkquest "${BASH_SOURCE:-$0}" "$@"
fi
