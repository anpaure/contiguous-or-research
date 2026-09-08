# Phase-directed adjacent skeletons

Date: 2026-09-07.  This note records a positive fixed-uniformity
construction and two exact limitations of phase labels.  It concerns the
three central ranks.  It does not give the Gaussian-width square cover or
prove the full-cube coefficient-one conjecture.

Put

\[
 \Omega=P\mathbin{\dot\cup}Q,\qquad |P|=|Q|=b,
 \qquad W={2b\choose b}.
\]

For a middle set `S`, call a Johnson move phase-forward if it deletes an
element of `P` and inserts an element of `Q`.  Every path consisting only
of phase-forward moves is geodesic: a deleted coordinate can never be
inserted later, and an inserted coordinate can never be deleted later.

The purpose of the first construction is to put this observation directly
inside the four-uniform adjacent-skeleton matching.

## 1. A directed four-uniform hypergraph

Let `[S]={S,S^c}` be an antipodal middle pair.  Whenever
`|S cap Q|<b/2`, the orbit has a unique representative of smaller
`Q`-weight; call it `S^downarrow` and put

\[
 q([S])=|S^\downarrow\cap Q|.
\]

Choose a real sequence `a_b -> infinity` with `a_b=o(sqrt b)`, and put

\[
 q_0=\left\lceil {b\over2}-a_b\sqrt b\right\rceil,
 \qquad q_1=\left\lfloor {b-3\over2}\right\rfloor,
 \qquad I_b=\{q_0,\ldots,q_1\}.                       \tag{1}
\]

The harmless removal of the top one or two levels ensures that every
orbit used below has a unique low representative.

Define a four-uniform hypergraph `H_b(P,Q)` as follows.  It has:

* every lower target `L in binom(Omega,b-1)` satisfying

  \[
    \min(|L\cap Q|,b-1-|L\cap Q|)\in I_b;             \tag{2}
  \]

* an out-slot `([S],out)` for every orbit of level `q in I_b`;
* an in-slot `([T],in)` for every orbit of level `q+1`, `q in I_b`.

For a low representative `S` of level `q in I_b`, choose

\[
 p\in S\cap P,\qquad x\in Q\setminus S,
 \qquad T=S-p+x.
\]

Insert the hyperedge

\[
 \{S-p,\ (S\cup\{x\})^c,\ ([S],out),\ ([T],in)\}.   \tag{3}
\]

The first two entries are precisely the two lower colours of the folded
Johnson edge `[S][T]`.

For later orientation, if `c_q=binom(b,q)`, the four vertex classes used
by the level-`q` edges have exact sizes

\[
 c_qc_{q+1},\quad c_qc_{q+1},\quad c_q^2,\quad
 c_{q+1}^2,                                      \tag{3a}
\]

in the order lower-low-out-in.  Their ratios tend uniformly to one on
`I_b`.  The hypergraph is the disjoint union of these level strata as a
matching problem, while the selected out-edge in stratum `q` and in-edge
in stratum `q-1` can join at the same folded middle target.

### Degree and codegree calculation

If a lower vertex in (2) has low parameter `q`, its degree is

\[
                         (q+1)(b-q).                 \tag{4}
\]

An out-slot at level `q` has degree `(b-q)^2`, and an in-slot at level
`q+1` has degree `(q+1)^2`.  Therefore, uniformly over all vertices,

\[
 d(v)=(1+o(1)){b^2\over4}.                           \tag{5}
\]

Two lower vertices determine at most one edge, as do two middle slots.
A lower vertex and a middle slot lie together in at most `2b` edges.
Consequently

\[
 \Delta_2(H_b(P,Q))\le 2b=o(b^2).                   \tag{6}
\]

The rank-`b` and rank-`b-1` hypergeometric distributions have variance
`Theta(b)`.  Chebyshev (or the elementary binomial-product tail bound),
together with the fact that one central level has size `O(W/sqrt b)`,
shows that the vertices retained in (1)--(2) comprise

\[
 (1-o(1))W\quad\hbox{lower vertices},\qquad
 (1-o(1))W\quad\hbox{middle slots}.                  \tag{7}
\]

Thus `|V(H_b)|=(2-o(1))W`.  Equations (5)--(6) verify literally the
hypotheses of the fixed-uniformity Pippenger near-perfect-matching theorem.
There is a matching `M_b` leaving `o(W)` vertices uncovered, and hence

\[
                         |M_b|=(1-o(1)){W\over2}.    \tag{8}
\]

No growing-uniformity theorem is used.

## 2. The selected graph is a union of geodesic paths

Direct every folded Johnson edge selected by (3) from `[S]` to `[T]`.
The matching condition gives indegree and outdegree at most one.  Along an
edge the level `q` increases by one, so there is no directed cycle.
Every nontrivial component is therefore a directed path.

The unique low representatives along such a component form a geodesic in
`J(2b,b)`: every move removes a `P`-coordinate and adds a `Q`-coordinate.
Its length is at most `q_1+1-q_0<b`, so it determines a legal centered
square pair.

Let `E=|M_b|`, and let `t` be the number of nontrivial path components.
Every path source either lies in the bottom level `q_0`, or has an
unmatched in-slot.  The bottom level has `O(W/sqrt b)=o(W)` vertices, and
the matching leaves `o(W)` slots unmatched.  Hence

\[
                              t=o(W).                \tag{9}
\]

Coalesce all the side-two squares along each directed path.  The all-rank
geodesic merge lemma preserves every target of the selected side-two
squares.  A path of `e` edges becomes one side-`e+1` square and has
principal charge `2(e+1)`.  The total principal charge is therefore

\[
                    2E+2t=(1+o(1))W.                \tag{10}
\]

The matching uses every retained lower target at most once and misses only
`o(W)` of all lower targets.  The same is true at rank `b+1` by
complementation.  All but `o(W)` folded middle targets are incident with a
selected edge: an omitted orbit lies in a discarded boundary/tail level or
accounts for an unmatched slot.  Thus the coalesced family misses only
`o(W)` targets in each of the three central ranks.

Compiling each coalesced square independently with band width `H=1` costs

\[
 2E+4t=(1+o(1))W,                                    \tag{11}
\]

and the remaining three-rank holes cost `o(W)` singleton patches.  This is
an alternative unconditional proof of

\[
             \nu_1(2b)=(1+o(1)){2b\choose b}.        \tag{12}
\]

More structurally, (8)--(9) imply that the selected edges have diverging
average geodesic run length.  For a suitable `r_b -> infinity`, all but
`o(W)` selected edges lie in components with at least `r_b` edges.

## 3. A fixed-phase square-root ceiling

The preceding runs cannot reach the scale needed by the current
Gaussian-band interface.

**Fixed-phase width lemma.**  Suppose a family of phase-forward geodesic
paths for one balanced split `P dotcup Q` covers `W-o(W)` middle sets
(multiplicity is irrelevant).  If `t` is its number of paths, then

\[
                         t=\Omega(W/\sqrt b).        \tag{13}
\]

Consequently its average number of covered middle vertices per path is
`O(sqrt b)`.

Proof.  For fixed sufficiently large `C`, a positive constant fraction of
all middle sets have

\[
        \bigl||S\cap Q|-b/2\bigr|\le C\sqrt b.       \tag{14}
\]

There are `O(sqrt b)` integer levels in (14), and a phase-forward
geodesic contains at most one vertex in each level.  If
`t=o(W/sqrt b)`, all paths together cover only `o(W)` vertices in (14),
contradicting the assumed `W-o(W)` total coverage. `square`

In particular, if the independent square compiler is run at a width
`H/sqrt b -> infinity`, its component overhead obeys

\[
                         2Ht=\omega(W).              \tag{14a}
\]

Thus the fixed phase fails the Gaussian-band interface for a direct and
quantitative reason, even though it is asymptotically optimal for the
three central ranks.

The same conclusion holds for any fixed catalogue of `r` balanced-split
phases, even if each path may choose its phase and the targets are assigned
adversarially among phases.  Indeed, choose `C=C(r)` large.  By Chebyshev
and a union bound, a positive fraction of all middle sets simultaneously
satisfy (14) for every one of the `r` splits.  One phase owns a positive
fraction (depending only on `r`) of those assigned targets; its paths again
have only `O(sqrt b)` available levels.  Hence

\[
                         t=\Omega_r(W/\sqrt b).      \tag{15}
\]

Thus a bounded phase catalogue cannot produce average side
`omega(sqrt b)`.  This is a width obstruction for this phase mechanism,
not for unrestricted geodesic square covers.

## 4. Two capacity slots cannot enforce a phase catalogue

There is a separate, purely local obstruction to putting many phases into
the original two middle-capacity slots.

At one folded middle target, give every incident half-edge an arbitrary
deterministic label in `{0,1}`.  Two incidences can coexist in a hypergraph
matching exactly when their labels differ.  Thus the complete local
compatibility graph is a complete bipartite graph between the two label
classes.

If one phase admits any through-pair, its half-edges meet both label
classes.  If a second phase also admits a through-pair, take a label-zero
half-edge from the first phase and a label-one half-edge from the second.
They form an allowed cross-phase pair.  Therefore two slots cannot allow
through-pairs in two phases while forbidding every phase switch.  This
argument permits the slot label to depend on the entire incident edge, not
only on its direction.

For the more restrictive phase/direction-only proposal, the failure is
even more transparent.  Rejecting every pair of entering incidences makes
all entering types use one common label `c`; rejecting every pair of
leaving incidences makes all leaving types use one common label `d`.
Allowing a directed through-pair forces `c != d`, after which an entering
edge of every phase is compatible with a leaving edge of every other
phase.  The desired same-phase relation is a disjoint union of phase
edges, whereas binary-slot compatibility is complete bipartite.

Hence merely relabelling the two slots in the four-uniform skeleton cannot
both choose among several phases and force a component to retain one
phase.  Phase-specific copies of slots remove the actual degree-two
capacity constraint unless an additional coupling gadget is introduced.
Such a gadget, a path-level macroedge, or a genuinely dynamic extension
procedure is extra structure beyond the present four-uniform matching.

## 5. Exact scope

The positive theorem supplies a phase-coherent, globally integral
three-rank skeleton at asymptotically optimal principal charge.  It is
strictly stronger than degree two alone because every component is
geodesic and can be coalesced.

It does **not** reach the required `omega(sqrt b)` side lengths: (13)--(15)
show that one or finitely many balanced-split phases cannot do so.  It also
does not assert small aggregate holes at depths at least two.  The next
mechanism must therefore use an unbounded, coherently coupled phase family
or abandon fixed-split monotonicity; static direction labels on the two
existing slots are insufficient.
