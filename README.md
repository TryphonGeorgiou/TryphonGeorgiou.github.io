# Website of Tryphon T. Georgiou

Published by GitHub Pages at https://tryphongeorgiou.github.io

- Each page is a Markdown file: `index.md`, `publications.md`, `bio.md`, `students.md`, ...
- The left menu is in `_data/menu.yml`.
- The look is in `assets/style.css`; the page frame in `_layouts/default.html`.
- To update the CV, replace `Vitae_online.pdf`.

Markdown cheat sheet (jemdoc equivalent in parentheses):

    ## Heading                      (== Heading)
    - list item                     (- list item)
    [link text](https://...)        ([https://... link text])
    **bold**                        (*bold*)
    line ending in \\ breaks line   (line ending in \n)

Photo with text beside it:

    <div class="fig" markdown="1">
    ![](images/name.jpg){: width="270"}

    **Caption**\\
    More text
    </div>

GitHub rebuilds the site about a minute after each change.
