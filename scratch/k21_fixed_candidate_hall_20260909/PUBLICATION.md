# Published Hall certificate contents

The source, input word, graph data, feasible flow, Hall set, complete
neighbor list, reports, build commands and execution logs are retained.
The generated executable `checker.bin` is intentionally excluded from Git;
it can be rebuilt from `checker.cpp` using the saved command. Its executed
hash remains in the original run metadata.

The original remote manifests describe the complete executed directory,
including that executable. They are preserved byte for byte rather than
rewritten to pretend the executable is part of this source publication.
`graph_rows.bin` is finite certificate data, not executable code, and is
included explicitly despite the repository's general binary-file ignore.
