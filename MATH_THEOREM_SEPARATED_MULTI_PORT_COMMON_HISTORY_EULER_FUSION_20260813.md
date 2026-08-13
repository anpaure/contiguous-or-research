# Separated multi-port common histories fuse a connected family of resident source circuits

**Date:** 2026-08-13  
**Method:** coordinatewise bounded-gap antecedents and an occurrence-labelled
order-`d` de Bruijn multigraph  
**Status:** unconditional at the stated port-packing hypotheses.  This note
does not prove that the canonical MSW components possess a spanning family
of separated compatible ports, nor does it protect source intervals longer
than `d+1`.

## 1. Simultaneous freedom at separated source blocks

Let

\[
                 T=(T_i)_{i\in\mathbb Z_L}
\]

be a cyclic simple Johnson trace whose nonconstant positive coordinate
runs have length at least `d+1`, and assume `1<=d<r` and `L>=d+1`.  Put

\[
 P_j=\bigcap_{h=0}^{d}T_{j-h},
 \qquad
 F_j=\{D_j,I_{j-d-1}\},                            \tag{1.1}
\]

with the event notation
`T_(i+1)=T_i-{D_i}+{I_i}`.  Thus `P` is the maximal depth-`d`
antecedent and every depth-`d` antecedent letter at `j` must contain
`F_j`.

Let `B` be a subset of the cyclic position set `Z_L`.  Assume every
cyclic connected component of `B` has at most `d` positions.  At every
`j in B`, choose a nonempty letter `H_j` satisfying

\[
                         F_j\subseteq H_j\subseteq P_j.       \tag{1.2}
\]

Define

\[
 A_j=\begin{cases}
       H_j,&j\in B,\\
       P_j,&j\notin B.
     \end{cases}                                             \tag{1.3}
\]

### Theorem 1.1 (separated multi-block freedom)

The simultaneous alteration (1.3) remains an antecedent of `T`:

\[
                              D^dA=T.                         \tag{1.4}
\]

### Proof

Fix a nonconstant coordinate `x`, and unwrap one positive owner run as
`[a,b]`.  In the maximal antecedent its allowed carrier is

\[
                              E_x=[a+d,b].                    \tag{1.5}
\]

The two endpoints of `E_x` are forced positions, so (1.2) retains them
whenever they belong to `B`.  Every position of `E_x` outside `B` is also
retained, by (1.3).  Consequently each run of carrier positions from which
`x` is removed is contained in one connected component of `B` and has
length at most `d`.  The distance between consecutive retained carrier
positions is therefore at most `d+1`.  The exact bounded-gap
characterization of an antecedent supplies `x` to every owner in `[a,b]`.

For a constant-one coordinate, the carrier is the whole cyclic position
set.  Its deleted runs are again contained in components of `B` of length
at most `d`; hence its retained support cyclically hits every interval of
`d+1` source positions.  Constant-zero coordinates never occur.  Applying
the argument independently to every coordinate proves (1.4).  \(\square\)

In particular, any family of length-`d` port blocks which are pairwise
disjoint and separated cyclically by at least one unaltered position meets
the hypothesis.  One component of length `L` can therefore expose at least

\[
                         \left\lfloor{L\over d+1}\right\rfloor           \tag{1.6}
\]

independent length-`d` ports.

## 2. A port-labelled component tree

Let `G=(V,E)` be a connected graph.  For every `v in V`, let `T^v` be a
cyclic trace as in Section 1, with maximal and forced letters
`P^v_j,F^v_j`.  Choose one global traversal orientation for each component
`v`.  For every incidence `(v,e)`, choose a cyclic length-`d` port, read in
that same component orientation,

\[
                  B_{v,e}=(b_{v,e},\ldots,b_{v,e}+d-1).        \tag{2.1}
\]

Assume the incidence ports at a fixed `v` are pairwise disjoint and have
at least one unaltered position between consecutive ports.  For every edge
`e=uv`, align its two oriented ports and assume

\[
 F^u_{b_{u,e}+j}\cup F^v_{b_{v,e}+j}
 \subseteq
 P^u_{b_{u,e}+j}\cap P^v_{b_{v,e}+j}
 \qquad(0\le j<d).                                  \tag{2.2}
\]

Define the common literal history

\[
 H^e_j=F^u_{b_{u,e}+j}\cup F^v_{b_{v,e}+j}.          \tag{2.3}
\]

On component `v`, simultaneously replace the maximal letters on every
incident port by the appropriate word `H^e`.  Theorem 1.1 proves that the
resulting cyclic word `A^v` still induces precisely `T^v`, while (2.3)
makes the two words incident with `e` visit the same literal order-`d`
history vertex.

### Theorem 2.1 (connected multi-port Euler fusion)

Under (2.1)--(2.3), the source circuits `A^v` serialize into one cyclic
source word `A` with the following properties.

1. `|A|=sum_(v in V)|A^v|`; no source position is added.
2. Every based source subword of every length at most `d+1` is preserved
   literally, with the label of its old terminal order-`d` de Bruijn edge,
   and every such occurrence in `A` has exactly one old preimage.
3. In particular, the complete owner occurrence ledger and every
   occurrence-labelled strict-lower compiler using cells of width at most
   `d` transport verbatim.

### Proof

Regard each cyclic word `A^v` as a closed directed walk in the order-`d`
de Bruijn multigraph on literal source letters.  Distinguish parallel
edges by their old component and position labels.  Equation (2.3) says
that the two walks incident with every edge `e of G` share a vertex.
Because `G` is connected, the union of all walks is a connected balanced
directed multigraph.  It therefore has an Euler circuit.  Spell that Euler
circuit to obtain `A`.  It uses every labelled de Bruijn edge once, proving
item 1.

A labelled order-`d` de Bruijn edge records its literal `(d+1)`-letter
window.  Hence the Euler circuit has exactly the old multiset of based
length-`d+1` windows.  For `1<=ell<=d`, assign a based length-`ell`
occurrence to the labelled edge ending at its final letter; it is the
literal length-`ell` suffix of that edge's `(d+1)`-window.  This gives a
label-preserving bijection at every shorter width and proves item 2.
Taking unions of the preserved literal words gives item 3.  \(\square\)

Here the transported occurrence label is the terminal old de Bruijn-edge
(equivalently old owner-window) label.  The theorem does not claim that the
individual source-position labels appearing inside a crossing interval
remain consecutive after the splice; only their literal letter word and
the canonical terminal-edge occurrence label are preserved.

The theorem permits different edges incident with one component to use
different history states.  What is load-bearing is not a single fixed
state but the separated-port condition, which makes all those local
antecedent alterations coexist on one source circuit.

## 3. Exact remaining MSW gate

For a canonical odd MSW owner factor, every component has length
`L=2m+1`.  Thus the present theorem gives the following proof-safe
sufficient gate for zero-charge short-deck fusion:

> Select a connected graph on the `Cat_m` tight MSW components and, at
> every component, assign its incident edges to pairwise separated
> compatible length-`d` histories, with degree at most
> `floor((2m+1)/(d+1))`.

The exact pairwise compatibility relation is (2.2).  H100 audits show that
its transposition graph, and even the subgraph in which the two forced-pair
histories are literally equal, is connected in the first asymptotic test
range.  Connectivity alone is not enough: the separated incidence-port
assignment above is a sufficient global quantifier.  It is not necessary:
several circuits may meet at one shared literal history, and overlapping
alterations can sometimes coexist under the sharper coordinatewise
bounded-gap characterization even when the simple separation rule fails.

Even after that gate is closed, Theorem 2.1 controls only source widths at
most `d+1`.  Proper upper witnesses use longer intervals and require a
separate support-preserving tree choice, rematerialization bank, or
all-width actuator.  The theorem makes no claim about that long deck or
about opening the final cyclic word with a bounded cap.
