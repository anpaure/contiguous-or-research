# The actual BTK component quotient: explicit sink map and all-r connectedness

**Date:** 2026-08-13  
**Method:** Greene--Kleitman unmatched-position dynamics and a lexicographic
Dyck ascent  
**Status:** unconditional theorem for the quotient induced by the actual
BTK two-colour forest.  It proves the unique-sink map and weak
connectedness for every `r`.  It does not prove strong connectivity,
parent-component distinctness, a rainbow selector, or BTK pathization.

## 0. Correction and outcome

Let `F_BTK` be the oriented two-colour forest in
`MATH_THEOREM_BTK_TWO_COLOUR_CATALAN_FOREST_AND_LINEAR_PATHIZATION_GATE_20260813.md`.
Its components are rooted at the short Greene--Kleitman chains.

There is one literal correction to the quotient paragraph of that note:
a rank-`r-1` lower set on a `(2r-1)`-point ground has

\[
 (2r-1)-(r-1)=r
\tag{0.1}

\]

rank-`r` parents, not `r+1`.  One parent belongs to the component rooted
at the lower set itself.  Hence, if the other parents lie in distinct
components, the loopless quotient outdegree is `r-1`, not `r`.

This note proves, without that distinctness assumption:

1. an explicit Dyck-word formula for the sink component reached from every
   parent;
2. exactly one of the `r` parent incidences is a loop;
3. the underlying quotient multigraph is connected for every `r`.

The graph here is the **actual parent-to-BTK-component quotient**.  It is
different from the depth-two root graph in
`MATH_THEOREM_GK_DEPTH2_GRAPH_CONNECTIVITY_REGULARITY_AND_FREE_FUSION_LIMIT_20260807.md`.

## 1. Dyck convention for short chains

Use `0` for an opening step and `1` for a closing step.  Let

\[
 \mathcal D_r=\{D=d_0\cdots d_{2r-1}:D\text{ is a Dyck word}\}.
\tag{1.1}

\]

Every word in `D_r` ends in `1`.  Associate to it the rank-`r-1` set

\[
 L(D)=\{i<2r-1:d_i=1\}\subseteq[2r-1].
\tag{1.2}

\]

Because the prefix `d_0...d_(2r-2)` has `r-1` ones and every prefix of
`D` has at least as many zeros as ones, this prefix has no unmatched ones
under the ordinary left-to-right Greene--Kleitman matching.  It has one
unmatched zero.  Thus `L(D)` is exactly the bottom of a short central
chain.  Conversely every short-chain bottom arises uniquely this way.

For every zero position `x<2r-1`, the parent

\[
 A_x(D)=L(D)\cup\{x\}
\tag{1.3}

\]

is a rank-`r` owner.  These are all `r` parents of `L(D)`.

## 2. Exact parent-to-sink map

Given `D` and a zero position `x`, let `w_x` be the length-`2r-1` word
obtained from the prefix of `D` by changing `d_x=0` to `1`.  Match every
`1` in `w_x` to the rightmost earlier unmatched `0`.  Let

\[
 I_x=\{\text{unmatched one positions of }w_x\},
 \qquad
 Z_x=\{\text{unmatched zero positions of }w_x\}.
\tag{2.1}

\]

Since `w_x` has `r` ones and `r-1` zeros,

\[
 |I_x|=|Z_x|+1.
\tag{2.2}

\]

Define `Phi_x(D)` by simultaneously changing

\[
 1\to0\quad\text{at every position in }I_x,
 \qquad
 0\to1\quad\text{at every position in }Z_x,
\tag{2.3}

\]

and then appending the final `1`.

### Theorem 2.1 (explicit BTK sink formula)

The component of `F_BTK` containing the parent `A_x(D)` has short-chain
sink `L(Phi_x(D))`.  In particular, `Phi_x(D)` is a Dyck word.

#### Proof

In any binary word, delete all matched pairs.  The unmatched positions
have the form

\[
 1^a0^b.
\tag{2.4}

\]

The rank-`r` owner `A_x(D)` has `a=b+1` by `(2.2)`.  If `b=0`, it already
belongs to a short chain: its unique unmatched one is removed to obtain
the short-chain bottom.

If `b>0`, the oriented BTK forest edge from this owner changes the boundary
unmatched pattern

\[
 \cdots1\,0\cdots
 \quad\longmapsto\quad
 \cdots0\,1\cdots,
\tag{2.5}

\]

where the `1` is the last unmatched one and the `0` is the first unmatched
zero.  Those two positions become a new matched `01` pair and all previous
matched pairs remain fixed.  Hence one step decreases both `a` and `b` by
one.  Iterating `b` times changes every member of `Z_x` from zero to one
and changes all but one member of `I_x` from one to zero.  The final owner
has one unmatched one and no unmatched zero.  Removing that last unmatched
one produces precisely the prefix specified by `(2.3)`.

This is a short-chain bottom, so appending `1` gives a Dyck word, and the
unique sink theorem for `F_BTK` proves the claimed component identity.
\(\square\)

This is also a direct algorithm for the quotient; no recursive SCD
generation or forest traversal is needed.

## 3. The unique loop

Let `z(D)` be the unique unmatched zero of the prefix of `D`.

### Lemma 3.1

One has

\[
 \Phi_x(D)=D\quad\Longleftrightarrow\quad x=z(D).
\tag{3.1}

\]

#### Proof

If `x=z(D)`, changing that unmatched zero to one leaves one unmatched one
and no unmatched zero.  Removing the same position at the sink returns the
original prefix, so `Phi_x(D)=D`.

Conversely suppose `x!=z(D)`.  Then `x` was matched in the prefix of `D`.
Changing it from zero to one destroys its old pair.  The owner cannot
return to the same short-chain bottom, because every oriented BTK edge
strictly raises the bottom-rank potential until the unique sink and a
forest component contains only one short-chain sink.  Equivalently, in
the explicit formula `(2.3)`, the changed matched position cannot be the
single unmatched one deleted at the end without changing some other
matched position.  Thus `Phi_x(D)!=D`.  \(\square\)

Therefore the parent incidence quotient has one loop and `r-1` nonloop
arcs out of each Dyck root, counted with multiplicity.

## 4. A canonical Dyck ascent

Order binary words lexicographically with `0<1` and put

\[
 Z_r=(01)^r.
\tag{4.1}

\]

This is the lexicographically largest Dyck word in `D_r`.

If `D!=Z_r`, let `x(D)` be the second zero in the first occurrence of
`00` in `D`.  Such an occurrence exists: a Dyck word with no `00` must
alternate and hence equals `Z_r`.

### Lemma 4.1 (strict ascent)

For every `D!=Z_r`,

\[
 \Phi_{x(D)}(D)>_{lex}D.
\tag{4.2}

\]

#### Proof

Before `x=x(D)`, the Dyck word is a concatenation of singleton primitive
blocks `01`, followed by the first zero of the displayed `00`.  Thus the
prefix strictly before `x` is balanced and completely matched.

After changing `d_x` from zero to one, every position strictly before the
first zero in the displayed `00` remains matched exactly as before.  That
first zero is unmatched at the instant the scan reaches `x`, so the new
one at `x` matches it immediately.  Thus `x` belongs to a fixed matched
pair of `w_x`, not to `I_x` or `Z_x`.  Formula `(2.3)` leaves both that
pair and every earlier position unchanged.  In particular the short-root
output has bit `1` at `x`, whereas the original word has bit `0` there.
Hence the first differing bit changes from `0` to `1`, proving `(4.2)`.
\(\square\)

### Theorem 4.2 (all-r quotient connectedness)

Let `Q_r` be the directed multigraph on `D_r` with one arc

\[
 D\longrightarrow\Phi_x(D)
\tag{4.3}

\]

for every zero position `x<2r-1`, and delete its unique loop at every
vertex.  The underlying undirected graph of `Q_r` is connected for every
`r>=2`.  More precisely, every vertex has a directed path to `Z_r`.

#### Proof

At every nonterminal word choose the canonical arc from Lemma 4.1.
Lexicographic order increases strictly.  Since `D_r` is finite, the process
terminates, and its only possible terminal is the unique Dyck word without
`00`, namely `Z_r`.  This gives a directed path from every word to `Z_r`
and proves weak connectedness.  \(\square\)

The theorem proves neither reachability *from* `Z_r` nor strong
connectedness.  Finite replay through `r=9` finds strong connectivity and
finds the `r` parent sinks pairwise distinct, but those are separate open
statements.

## 5. Relation to degree-two pathization

Weak connectedness removes an abstract component barrier for endpoint
completion.  It does not choose physical BTK edges.  A quotient arc uses
an unused lower root `L(D)` and one parent owner `A_x(D)`; realizing a
sequence simultaneously must still preserve:

1. injectivity of the used lower roots;
2. owner degree at most two;
3. the selected upper colour of every BTK diamond; and
4. acyclicity of the resulting owner graph.

The lexicographic proof is therefore not yet a solution of BTK pathization.
Its significance is that the exact actual quotient has no disconnected
Catalan region: the remaining obstruction is coloured degree-reducing
selection, not component reachability.

## 6. Independent finite replay

Direct enumeration of `D_r` and formula `(2.3)` for `2<=r<=9` gives:

\[
\begin{array}{c|c|c|c}
r&|\mathcal D_r|&\text{loops}&\text{weak component size}\\ \hline
2&2&2&2\\
3&5&5&5\\
4&14&14&14\\
5&42&42&42\\
6&132&132&132\\
7&429&429&429\\
8&1430&1430&1430\\
9&4862&4862&4862
\end{array}
\tag{6.1}

\]

The replay is diagnostic only; Theorems 2.1 and 4.2 are solver-free and
hold for every `r`.
