# A polynomial-component simple factor has a sub-half repair-root transversal

**Date:** 2026-08-06  
**Method:** independent random representatives on small cycles, Chernoff,
and greedy avoidance on large cycles using the minimum vertex cover of an
even cycle; no computation or search  
**Status:** unconditional graph theorem.  Every simple spanning two-factor
of the Middle Levels incidence graph with polynomially many components has
one selected incidence per component whose two endpoint banks satisfy a
fixed all-occurrence sub-half exposure cap.  The theorem does not cover
coloured common-edge two-cycles, prescribed root submenus, or the subsequent
root-to-code arms.

## 1. Setting

Let

\[
 {cal L}={ [2r-1]\choose r-1},\qquad
 {cal U}={ [2r-1]\choose r},                       \tag{1.1}
\]

and let `G` be their inclusion graph.  Every vertex has degree `r`.
Let `K` be a **simple** spanning two-factor of `G`, with component set
`C`.  Write

\[
                         q=|{\cal C}|\le r^A           \tag{1.2}
\]

for one fixed `A`.

For a selected incidence `e_C=z_C y_C` in each component, define

\[
 \alpha=\max_{x\in{cal L}}
   |\{C:x\subset y_C\}|,\qquad
 \beta=\max_{U\in{cal U}}
   |\{C:z_C\subset U\}|.                              \tag{1.3}
\]

These are exactly the all-occurrence endpoint exposures of the selected
root matching.

The Middle Levels incidence graph has no four-cycle: two distinct rank-`r`
sets have at most one common rank-`r-1` subset.  Hence every simple factor
component has at least six incidence edges, or at least three vertices on
each shore.

## 2. The theorem

### Theorem 2.1 (sub-half root transversal)

Fix

\[
                         0<\varepsilon<1/12.           \tag{2.1}
\]

For all sufficiently large `r`, every factor `K` satisfying (1.2) has a
choice of one incidence `e_C` per component for which

\[
 \boxed{
 \alpha,\beta\le\left\lfloor(1/2-\varepsilon)r\right\rfloor.}
                                                               \tag{2.2}
\]

The selected incidences form a matching because different factor
components are vertex-disjoint.

#### Proof

Put

\[
 K_* =\left\lfloor(1/2-\varepsilon)r\right\rfloor,
 \qquad
 K_0 =\left\lfloor(1/2-2\varepsilon)r\right\rfloor.   \tag{2.3}
\]

For a component `C`, let `ell_C` be its number of vertices on either
shore.  Call `C` small when

\[
                         \ell_C\le 7rq,               \tag{2.4}
\]

and large otherwise.

### Small components

Choose one incidence edge independently and uniformly from every small
cycle.  Its upper endpoint is uniform on the `ell_C` upper vertices of the
cycle, since every upper vertex is incident with two cycle edges.  Its
lower endpoint is uniform on the lower shore for the same reason.

Fix `x in L`.  Let `a_C(x)` be the number of upper vertices of `C`
containing `x`.  The number of selected upper roots containing `x` is a sum
of independent Bernoulli variables and has mean

\[
 \mu_x=\sum_{C\text{ small}}{a_C(x)\over\ell_C}
 \le {1\over3}\sum_Ca_C(x)
 \le r/3.                                             \tag{2.5}
\]

Here `ell_C>=3`, while `x` has exactly `r` upper neighbours in the whole
graph.  Dually, for every fixed `U in U`, the expected number of selected
lower roots contained in `U` is at most `r/3`.

Because (2.1) makes

\[
                         (1/2-2\varepsilon)r>r/3,     \tag{2.6}
\]

the Chernoff bound gives, for some `c_epsilon>0`,

\[
 \Pr[X_x>K_0]\le e^{-c_\varepsilon r},\qquad
 \Pr[Y_U>K_0]\le e^{-c_\varepsilon r}.              \tag{2.7}
\]

Only polynomially many rows can receive nonzero load from the small
components.  Indeed there are at most `7rq^2` small vertices on either
shore, and every one lies in exactly `r` opposite-shore stars.  Thus there
are at most `7r^2q^2` relevant rows on either side.  By (1.2), this is
polynomial in `r`.  A union bound in (2.7) is therefore less than one for
all sufficiently large `r`.  Fix a realization in which every small-cycle
root load is at most `K_0` on both shores.

### Large components

Process the large components one at a time.  At any stage call a lower row
`x` saturated when its current upper-root load is `K_*`, and call an upper
row `U` saturated when its current lower-root load is `K_*`.  Let these two
sets be `A` and `B`.

After at most `q` roots have been chosen, the sum of all upper-root loads
over lower rows is at most `rq`: one selected rank-`r` owner belongs to
exactly `r` lower stars.  Therefore

\[
                         |A|K_*\le rq.               \tag{2.8}
\]

For fixed `epsilon<1/12` and sufficiently large `r`, (2.8) gives

\[
                         |A|<3q.                    \tag{2.9}
\]

The same argument gives `|B|<3q`.

An upper vertex is forbidden when it contains a saturated member of `A`.
There are fewer than

\[
                         r|A|<3rq                   \tag{2.10}
\]

such upper vertices.  A lower vertex is forbidden when it is contained in
a saturated member of `B`; there are fewer than `3rq` of those.

Consider the next large factor cycle `C`.  If every incidence edge of `C`
had a forbidden endpoint, the forbidden vertices on `C` would form a
vertex cover of that even cycle.  A cycle with `ell_C` vertices on each
shore has minimum vertex-cover size `ell_C`.  But (2.10) gives fewer than
`6rq` forbidden vertices in the entire graph, whereas

\[
                         \ell_C>7rq.                 \tag{2.11}
\]

This is impossible.  Choose an edge of `C` with neither endpoint
forbidden.

Its upper endpoint belongs to no saturated lower star, and its lower
endpoint belongs to no saturated upper star.  Adding this root therefore
keeps every load at most `K_*`.  The initial small-cycle loads were at most
`K_0<K_*` for sufficiently large `r`, so induction processes all large
cycles and proves (2.2). \(\square\)

## 3. Why simplicity is load-bearing

### Proposition 3.1 (common-edge two-cycle obstruction)

Theorem 2.1 is false for a coloured union of two perfect matchings if
common incidences are retained as two-cycle components.

#### Proof

Fix one lower facet `x`.  Choose more than
`(1/2-epsilon)r` of its `r` upper neighbours and make each chosen incidence
a common edge of the two colour matchings.  Every such coloured two-cycle
has only that one upper root.  Any one-root-per-component selection has
upper endpoint load greater than `(1/2-epsilon)r` at `x`. \(\square\)

Thus a polynomial bound on the **number** of common edges does not imply a
sub-half root bank.  The common edges must first be removed/detoured, or
their endpoint bank must separately satisfy the exposure cap.

There is no contradiction with Theorem 2.1: a simple incidence factor has
girth at least six, which supplied the strict expectation gap `r/3<r/2` in
(2.5).

## 4. Protected-root and arm scope

The theorem chooses an arbitrary incidence of each simple component.  If a
later application restricts component `C` to a prescribed root menu
`E_C`, then the proof remains valid only after the following two properties
are re-established for those menus:

1. on the small-cycle bank, the random representative law has expected
   load strictly below `r/2` in every row; and
2. on a large cycle, no union of fewer than `6rq` saturated-star vertices
   covers every eligible root edge.

Neither follows from nonemptiness of `E_C`.  In particular, saying merely
that every component contains one polynomial-damage edge is insufficient.

The theorem also selects roots but does not route them to coded ports.  It
does, however, establish the exact necessary starting margin for such an
arm theorem.  Combined with a simple polynomial-component completion, the
formerly impossible arbitrary-root problem becomes:

\[
 \boxed{
 \text{sub-half root matching}
 \longrightarrow
 \text{low-increment root-to-code arms}.}
\]

## 5. PBBS consequence

The Hamilton-anchored completion theorem currently gives polynomially many
components but allows polynomially many common-edge two-cycles.  The
ordinary protected-factor theorem gives a simple factor but does not bound
its component count.  Theorem 2.1 shows that the exact graph-side synthesis
needed between them is now:

> construct a **simple** polynomial-component completion (or eliminate the
> common-edge bank from the Hamilton-anchored completion) while retaining
> the protected PBBS paths.

Once that is done, one repair root per component can be chosen with a fixed
linear all-occurrence exposure margin; no separate arbitrary-root
assumption is required.
