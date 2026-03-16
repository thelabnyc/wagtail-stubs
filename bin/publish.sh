#!/usr/bin/env bash

set -euxo pipefail

# Check git status
git fetch --all
CURRENT_BRANCH=$(git branch --show-current)
if [[ "$CURRENT_BRANCH" != "master" && ! "$CURRENT_BRANCH" =~ ^wagtail- ]]; then
    echo "This script must be run from master or a wagtail-* branch, but the current branch is ${CURRENT_BRANCH}. Abort!"
    exit 1
fi

NUM_BEHIND=$(git log ..origin/"$CURRENT_BRANCH" | wc -l | awk '{print $1}')
if [ "$NUM_BEHIND" == "0" ]; then
    echo ""
else
    echo "Your branch is NOT up to date with origin/${CURRENT_BRANCH}. Abort! Please fetch and rebase first."
    exit 1
fi

# Update version and publish via commitizen
cz bump "$@"
