```mermaid
 classDiagram
    GameLoop "1" --> "1" Tetris
    GameLoop "1" --> "1" Renderer
    GameLoop "1" --> "1" EventQueue
    GameLoop "1" --> "1" Clock
    Renderer "1" --> "1" Tetris
    Tetris "1" --> "1" Block
```