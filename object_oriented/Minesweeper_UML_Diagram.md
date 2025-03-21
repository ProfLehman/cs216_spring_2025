# Minesweeper

```mermaid
classDiagram
    class Minesweeper {
        %% === Fields ===
        - int _rows
        - int _cols
        - int[][] _mines
        - int[][] _tiles
        - string _status
        - int _num_mines

        %% === Public Methods ===
        + __init__(rows, cols)
        + get_status() str
        + get_rows() int
        + get_cols() int
        + mark_tile(r, c, tile_type)
        + to_string_mines() str
        + to_string_tiles() str
        + to_string_board() str
        + game_won() bool

        %% === Private/Internal Helpers ===
        - _place_mines()
        - _calculate_clues()
        - _is_valid_index(r, c) bool
        - _open_adjacent_blanks(r, c)
    }
