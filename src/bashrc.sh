if [ -z "$PYPCG_PYTHON_PATH" ]
then
    export PYPCG_PYTHON_PATH=$PYPCG_SOURCE_DIR/
    export PYTHONPATH=$PYPCG_PYTHON_PATH:$PYTHONPATH
fi

function pcg-image-cairo-lines()
{
    python3 -m pcg.image.cairo_lines_001
}

alias pcg-image-random-color="python3 -m pcg.image.color.gen_color_image"
alias pcg-image-color-palette="python3 -m pcg.image.color.gen_color_palette_image"