# Exact flag moments for the forced `k=11` prefix

## 1. Rank-five cut identity

Fix any rank-five mask `Q`.  Let `S_Q` be its six rank-six supersets.  All
fifteen Johnson edges internal to `S_Q` have lower intersection colour `Q`,
and every Johnson edge of lower colour `Q` is one of these internal edges.

In the canonical fixed-row path:

* if `Q=C0=31`, no internal edge of `S_Q` is selected;
* for every other rank-five `Q`, exactly one internal edge is selected.

Let `b_Q` be the number of selected real edges crossing from `S_Q` to its
complement, and let `e_Q` be the number of selected dummy endpoint edges
incident with `S_Q`.  Summing the selected degree-two equations over the six
vertices of `S_Q` gives

\[
  b_Q+e_Q+2i_Q=12,
\]

where `i_Q` is the number of selected internal edges.  Therefore

\[
 b_Q+e_Q=
 \begin{cases}
 12,&Q=C_0,\\
 10,&Q\ne C_0.
 \end{cases}                                      \tag{1}
\]

This is the rank-five specialization of the general flag-moment identity in
`K11_FLAG_MOMENT_CUT.md`.

## 2. Why prefix moments are cheap and useful

Once a canonical prefix

```text
E,F,G,H,I
```

has been fixed by the nested orbit settings, its adjacent intersections give
up to four explicit selected non-omitted lower colours

```text
E&F, F&G, G&H, H&I.
```

Equation (1) supplies one exact-10 cardinality for each of them.  Each support
contains exactly

```text
150 real cut edges + 6 dummy endpoint edges = 156 literals.
```

These constraints are redundant, but globally couple an early forced colour
to all possible occurrences of the other endpoint and all distant path edges.
They expose the sum of six vertex-degree equations directly instead of asking
CDCL resolution to reconstruct it through fifteen internal-colour clauses.

The cuts do not assume that either endpoint contains `Q`.  Endpoint incidence
is represented by the six dummy literals and counted exactly.

## 3. Implementation

Set

```text
RECOMBINE_PREFIX_MOMENTS=1
```

to add exact-10 counters for every adjacent lower colour in the currently
forced canonical prefix.  The prefix may have two through five vertices,
depending on whether the second-, third-, and fourth-orbit variables are
present.  Duplicate or omitted prefix colours are rejected defensively.

The option requires canonicalization, ordered orientation, `k=11`, and
`rank=6`.  It is independent of `RECOMBINE_C0_MOMENT=1`; enabling both gives
the exact-12 omitted-colour cut plus all available exact-10 prefix cuts.
