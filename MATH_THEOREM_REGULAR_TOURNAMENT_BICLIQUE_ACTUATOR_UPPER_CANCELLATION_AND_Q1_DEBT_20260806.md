# Regular-tournament biclique actuators: exact upper cancellation and the q1-lower debt

## Status

This note gives a literal state-balanced trade on a large owner subset of one
ambient `(r+2)`-set.  The two phases have:

* exactly the same one-copy owner set;
* exactly the same immediate-upper multiset, with multiplicity;
* an identical protected named lower bank at every source depth; and
* an explicit inventory of all uncommitted source occurrences.

The trade is not q1-lower neutral.  Its old and new immediate-lower root
families are disjoint, with exact debt `L^2` per biclique.  Thus this note
does not prove an all-owner factor or an upper bound for `nu(k)`.  It isolates
the one remaining palette row which a C6-type completion must supply.

## 1. Parameters and the tournament bank

Let

\[
                    n=2r-1,\qquad d\ge2\text{ even},
                    \qquad L=d+2.                            \tag{1.1}
\]

Fix an `(r-3)`-set `S` and put

\[
                    R=[n]-S,\qquad |R|=r+2.                 \tag{1.2}
\]

Choose an odd integer `g>=3` satisfying

\[
                           gL\le r+2,                        \tag{1.3}
\]

and disjoint ordered banks

\[
 G_i=\{x_{i,0},\ldots,x_{i,L-1}\}\subset R,
                  \qquad i\in\mathbb Z_g.                  \tag{1.4}
\]

Put

\[
                  D=R-\bigcup_iG_i,qquad h=|D|=r+2-gL.     \tag{1.5}
\]

Let `mathcal T` be a regular tournament on the `g` group indices.  Thus

\[
              d^+_{\mathcal T}(i)=d^-_{\mathcal T}(i)
                         ={g-1\over2}.                       \tag{1.6}
\]

For an unordered group pair `{i,j}`, the complemented owner grid is

\[
 \mathcal X_{ij}
   =\{S\cup\{u,v\}:u\in G_i,\ v\in G_j\}.                  \tag{1.7}
\]

In the original owner layer it is

\[
 \overline{\mathcal X}_{ij}
   =\{R-\{u,v\}:u\in G_i,\ v\in G_j\}.                    \tag{1.8}
\]

The grids for distinct unordered pairs are disjoint.

## 2. The two literal phases

Fix a tournament arc `i -> j`, and put

\[
                         C_{ij}=R-(G_i\cup G_j).             \tag{2.1}
\]

For every centre `x_(i,s) in G_i`, define the phase-zero cyclic source word

\[
 X^{0;i\to j,s}_t
   =C_{ij}\cup
      \bigl(\{x_{i,t},x_{i,t+1}\}-\{x_{i,s}\}\bigr)
        \cup\{x_{j,t}\},
       \qquad t\in\mathbb Z_L.                             \tag{2.2}
\]

For every centre `x_(j,s) in G_j`, define the transposed phase-one word

\[
 X^{1;i\to j,s}_t
   =C_{ij}\cup
      \bigl(\{x_{j,t},x_{j,t+1}\}-\{x_{j,s}\}\bigr)
        \cup\{x_{i,t}\}.
                                                                    \tag{2.3}
\]

The whole phase is the disjoint collection of these rings over all arcs of
`mathcal T` and all centres in the tail, respectively head, group.

### Lemma 2.1 (literal state balance)

Every word in (2.2)--(2.3) is a legal depth-`d`, state-balanced pull ring.
Its `L` owner windows are

\[
                         R-\{x_{i,s},x_{j,u}\},
                         \qquad u\in\mathbb Z_L,             \tag{2.4}
\]

in phase zero, and the same sets with the two group roles transposed in
phase one.

#### Proof

In (2.2), a core coordinate `x_(i,a) != x_(i,s)` appears only at source
phases `a-1,a`.  Its omission set is therefore one cyclic interval of
length

\[
                              L-2=d.                         \tag{2.5}
\]

The coordinates of `C_(ij)` are never omitted, and `x_(j,t)` is the
private phase label.  This is exactly the pull overlay of an all-high ring.
Any length-`L-1=d+1` window misses only one phase, so it contains both the
whole allowed core and all but one private label.  This proves (2.4).

The ring length `L` is even.  The even-start two-step macros therefore give
one balanced cyclic state component, as in the pull-overlay theorem.  The
transpose is identical. `square`

## 3. Owner equality and the protected all-depth bank

### Theorem 3.1 (one-copy owners)

Both phases use exactly once every owner in

\[
 \boxed{
   \mathcal O_{\rm cross}
     =\{R-\{u,v\}:u\in G_i,v\in G_j, i<j\}.}               \tag{3.1}
\]

Thus

\[
                         |\mathcal O_{\rm cross}|
                           =\binom g2L^2.                    \tag{3.2}
\]

#### Proof

For one group pair, (2.4) is the row decomposition of the complete
bipartite grid in phase zero and the column decomposition in phase one.
Both enumerate its `L^2` owners once.  Different group pairs have different
two-group support in the omitted pair, so their grids are disjoint. `square`

For `1<=q<=d`, write

\[
 I_i(q,t)=\{x_{i,t},x_{i,t+1},\ldots,x_{i,t+q-1}\}.        \tag{3.3}
\]

### Theorem 3.2 (identical protected lower bank)

For every unordered pair `{i,j}`, every `1<=q<=d`, and every
`t in Z_L`, both phases contain the named target

\[
 \boxed{
      P_{ij;q,t}=C_{ij}\cup I_i(q,t)\cup I_j(q,t).}         \tag{3.4}
\]

On the orientation `i -> j`, it occurs in the phase-zero ring centred at
`x_(i,t+q)` and the phase-one ring centred at `x_(j,t+q)`.

All targets in (3.4), over every pair, depth, and phase, are distinct.
Hence the common protected bank has cardinality

\[
 \boxed{
                         \binom g2Ld.}                       \tag{3.5}
\]

#### Proof

A width-`q` interval beginning at `t` in (2.2) has private contribution
`I_j(q,t)`.  Its `G_i` contribution is

\[
       \{x_{i,t},\ldots,x_{i,t+q}\}-\{x_{i,s}\}.           \tag{3.6}
\]

Putting `s=t+q` gives (3.4).  Equation (2.3) gives the same target after
transposition.

Different values of `q` have different target ranks

\[
                         |P_{ij;q,t}|=r+2-2L+2q.             \tag{3.7}
\]

At fixed `q`, the complement of (3.4) inside `R` is supported on exactly
the two groups `G_i,G_j`, with `L-q>=2` omitted elements in each.  It
therefore recovers the unordered group pair.  The proper cyclic interval in
either recovered group then recovers `t`.  This proves distinctness and
(3.5). `square`

## 4. Exact immediate-upper cancellation

Consecutive owners in a phase-zero ring centred at `u in G_i` have union

\[
                              R-\{u\}.                       \tag{4.1}
\]

The same statement holds in phase one with the head group as centre.

### Theorem 4.1 (upper multiset equality)

The complete immediate-upper multisets of phases zero and one are equal.
For every `u in G_i`, the target `R-{u}` has multiplicity

\[
 \boxed{
                         L{g-1\over2}}                       \tag{4.2}
\]

in each phase.

#### Proof

For every outgoing tournament arc `i -> j`, phase zero has one ring centred
at `u`; its `L` cyclic owner transitions all have union `R-{u}`.  Thus the
phase-zero multiplicity is `L d^+(i)`.  In phase one, `u` is a centre once
for every incoming arc, giving `L d^-(i)`.  Equation (1.6) makes these
equal and proves (4.2). `square`

This is an exact occurrence-multiset statement, not merely coverage or
equality after averaging.

## 5. The uncancelled immediate-lower row

Consecutive phase-zero owners on an arc `i -> j` have intersection

\[
 Q^0_{ij;s,t}
    =R-\{x_{i,s},x_{j,t},x_{j,t+1}\}.                      \tag{5.1}
\]

The phase-one roots are

\[
 Q^1_{ij;s,t}
    =R-\{x_{j,s},x_{i,t},x_{i,t+1}\}.                      \tag{5.2}
\]

### Theorem 5.1 (sharp q1-lower debt)

For every group pair, each family in (5.1)--(5.2) has exactly `L^2`
distinct targets, and the two families are disjoint.  Root families from
different group pairs are also disjoint.  Consequently the switch loses

\[
 \boxed{
                           \binom g2L^2}                     \tag{5.3}
\]

old immediate-lower targets and gains the same number of new ones.  Its
immediate-lower symmetric difference is twice (5.3).

#### Proof

In (5.1), the omitted triple has one element in `G_i` and one cyclically
adjacent pair in `G_j`.  Since `L>=4`, the `L` adjacent pairs are distinct;
the omitted triple recovers both `s` and `t`.  Formula (5.2) has the
multiplicities two and one on the two groups, so it cannot equal a member of
(5.1).  A target from another group pair has a different two-group support
in its omitted triple. `square`

Thus regular-tournament balancing removes the q1-upper polarization exactly,
but it cannot cancel q1-lower roots.  A separate incidence-C6 or root-bank
completion is genuinely necessary.

## 6. The explicitly uncommitted occurrence inventory

For one group pair and one proper width `q`, each phase has `L` rings and
`L` starts per ring, hence `L^2` literal source occurrences.  Theorem 3.2
commits exactly `L` of them.  Therefore the number of uncommitted occurrence
slots is exactly

\[
 \boxed{
     \binom g2(L^2-L)d}                                     \tag{6.1}
\]

per phase over all proper widths.

These are real literal cells, but (6.1) is only an occurrence count.  Their
named values may collide, and no matching of exterior demands into them is
claimed.  The q1-lower roots in Section 5 are a separate owner-incidence row
and are not silently charged to (6.1).

## 7. A sharp local leave bound inside one ambient top

The owner facets associated with the ambient set `R` are indexed by the
edges of the complete graph on `R`: the edge `{u,v}` represents
`R-{u,v}`.  The tournament bank covers exactly the cross-group edges.
Its uncovered owner count is

\[
 \boxed{
   g\binom L2+h(gL)+\binom h2,\qquad h=r+2-gL.}             \tag{7.1}
\]

Choose `g` to be the largest odd integer with `gL<=r+2`.  Then

\[
                             0\le h<2L,                     \tag{7.2}
\]

and (7.1) is `O(rL)=O(r^(3/2))`, whereas the complete ambient owner bank
has `binom(r+2,2)=Theta(r^2)` members.

Thus one ambient top admits an exactly upper-balanced, state-balanced
actuator on all but `O(rL)` of its owner facets.  This is a local statement:
different ambient tops overlap in owners, so it is not yet a global owner
decomposition.

## 8. Divisibility and unequal groups

No divisibility hypothesis `L | (r+2)` is required.  The odd group count
and the remainder bank `D` absorb that scalar mismatch, with the sharp
remainder estimate (7.2).  If `(r+2)/L` is an odd integer then `h=0`; if it
is even, taking one fewer group leaves exactly one `L`-bank.

Equal group size is essential to the literal theorem as stated.  The
owner-only `K_(L,L+1)` trade exchanges `L+1` size-`L` stars with `L`
size-`(L+1)` stars, but its state-balanced all-depth decoration has not been
authenticated.  No unequal-group extension is asserted here.

## 9. Exact remaining gate

The tournament construction closes the upper-polarization problem proposed
for the complete-bipartite absorber.  The surviving local theorem is now:

> **Root-completion lemma.**  Add a resource-disjoint bounded-state
> incidence circuit to each tournament bank so that the old and new root
> families (5.1)--(5.2) are matched into one common q1-lower palette, while
> retaining the owner set, the upper multiset (4.2), and the protected
> all-depth bank (3.4).

After that local lemma, a global proof would still need to select
owner-disjoint ambient banks and route the uncommitted occurrences (6.1)
to the remaining named lower targets.  Those are separate global
cover-down and Hall problems.
