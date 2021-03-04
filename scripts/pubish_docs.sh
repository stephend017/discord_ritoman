#!/bin/bash

# CONSTANTS
DOC_NAME="API Utils"
DOC_SOURCE="discord_ritoman.utils"
WIKI_FOLDER="wiki"
WIKI_REPO="https://github.com/stephend017/discord_ritoman.wiki.git"

# setup wiki repo
if [[ ! -d "./$WIKI_FOLDER" ]]; then
    git clone "$WIKI_REPO" "$WIKI_FOLDER"
fi

git submodule update "$WIKI_FOLDER"
env/bin/pydoc-markdown -I . -m "$DOC_SOURCE" '{
    renderer: {
      type: markdown,
      descriptive_class_title: false,
      render_toc: true,
      use_fixed_header_levels: true,
      header_level_by_type: {
          "Module": 1,
          "Class": 2,
          "Method": 3,
          "Function": 2,
          "Data": 2,
      }
    }
  }' > "./$WIKI_FOLDER/$DOC_NAME.md"
cd "$WIKI_FOLDER"
git checkout master
git add "./$DOC_NAME.md"
git commit -m "Updated Documentation"
git push
