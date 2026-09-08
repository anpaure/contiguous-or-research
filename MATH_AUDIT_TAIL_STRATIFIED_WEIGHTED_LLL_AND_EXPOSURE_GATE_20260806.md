# Audit of the stratified tail weighted-LLL argument

**Date:** 2026-08-06  
**Method:** direct quantifier audit, factorial-moment witness events, and the
sharp protected-matching scale  
**Status:** the external coarea and bottom-fibre estimates are sound after
the correction below.  The global-exposure LLL and the final component
claim in the first draft are not sound as written.  A witness-event LLL
repairs the former.  The latter remains a genuine central-plus-tail
topology gate.  No `B(k)+O(1)` conclusion is made.

## 1. What survives the audit

The singleton exclusion is necessary.  Protecting all owners
`K union {e}` gives exposure `m` at the common lower facet `K`, so the
complement-paired low family must begin at rank two.

The external coarea calculation also survives, with one wording
correction.  If a labelled role has deterministic external rank `s`, then

\[
 \sum_{T\in\binom E q}
   \Pr(\operatorname{tr}_E X_T=S)
       ={\binom m q\over\binom m s}.                 \tag{1.1}
\]

If the rank of the role is random and one merely retains the part with
rank `s`, the right statement is the upper bound

\[
 \sum_{T\in\binom E q}
   \Pr(\operatorname{tr}_E X_T=S, |\operatorname{tr}_E X_T|=s)
       \le {\binom m q\over\binom m s}.              \tag{1.2}
\]

Both follow from `Sym(E)` invariance.  Equality in (1.1) uses total mass
`binom(m,q)`; the subprobability in (1.2) has no larger total mass.

Conditional `Sym(K)` invariance gives the exact fibre sizes

\[
 \binom{m-1}s,qquad \binom{m-1}{s-1},qquad
 \binom{m-1}{s-2}                                  \tag{1.3}
\]

for lower, owner, and upper roles having external rank `s`.  The only
zero-dimensional base fibre is the rank-two upper role.  It is the named
upper target of its unique rank-two tail witness and must be treated as an
intended reservation, not as a random collision event.

For the other base roles, the direct collar coarea gives a total
per-macro collision charge `O(1/m)` at the bottom; all balanced-high and
connector roles whose external rank is at least `d-O(1)` contribute
`m^{-omega(1)}`.  To use this conclusion one must state separately that:

1. every low collar visits each small external rank only `O(1)` times; and
2. the residence-constrained connector type word remains inside the band
   `[q,m-q]` (or inside a band with the same `d-O(1)` distance from the
   ends after its bounded forced prefix and suffix).

The first assertion follows from monotonicity of a collar.  The second is
an additional scheduling row and was only implicit in the first draft.

## 2. The first-draft global-event LLL is invalid

Let `B_e` be the local role-collision events.  For one macro the sum of
probabilities of incident collision events is `O(1/m)`.  This is enough
for the local collision LLL.

An event of the form

\[
 G_x=\{\text{exposure at }x>m/3\}                   \tag{2.1}
\]

depends, however, on every macro which can hit `x`.  Hence it is adjacent
not only to all other exposure events but also to all local collision
events meeting any of those macros.  The latter total charge can be
`2^{o(m)}`.  The estimate

\[
 \Pr(G_x)=\exp\{-\Omega(m\log m)\}                  \tag{2.2}
\]

does not by itself compensate for a product factor of the form
`exp(-2^{o(m)})`.  Therefore the displayed LLL argument in the first draft
does not prove simultaneous privacy and sub-half exposure.

## 3. A correct repair: minimal exposure witnesses

The obstruction in Section 2 is an artefact of using one global bad event.
It disappears after replacing it by its minimal many-macro witnesses.

### Theorem 3.1 (finite-range witness-event LLL)

Let `J` be a family of independent macro seeds.  Suppose every physical
object uses the seeds in a set of size at most `a`, and the intersection
graph of these seed sets has maximum degree `Delta`, where `a,Delta` are
absolute constants.  Assume:

1. every local collision event uses at most `a_0` object neighbourhoods;
2. for every object neighbourhood `j`,
   \[
      \sum_{B_e:\ e\text{ meets }j}\Pr(B_e)\le {C_0\over m}; \tag{3.1}
   \]
3. for every exposure vertex `v`, the contribution `Y_{jv}` of one object
   is in `{0,...,b}`, with `b=O(1)`, and
   \[
      \sum_j\mathbb E Y_{jv}\le M                 \tag{3.2}
   \]
   for an absolute `M`; and
4. one fixed object can contribute to only `m^{O(1)}` different exposure
   vertices.

Then, for every fixed `theta>0`, the object seeds can be selected so that
no local collision occurs and

\[
                         \sum_jY_{jv}\le\theta m    \tag{3.3}
\]

for every exposure vertex `v`, once `m` is sufficiently large.

#### Proof

Colour the object-intersection graph with `h=Delta+1` colours.  Split
`Y_{jv}` into the `b` indicators `1_{Y_{jv}\ge l}`.  If (3.3) fails, then
for some colour and some `l` at least

\[
                         t=\left\lceil{\theta m\over hb}\right\rceil
                                                               \tag{3.4}
\]

independent object indicators are one.  For every such `t`-set make a
witness bad event.

For fixed `v`, colour and `l`, if the indicator probabilities are `p_j`,
then `sum p_j<=M`; hence the sum of the probabilities of all its witness
events is at most

\[
             \sum_{|S|=t}\prod_{j\in S}p_j
             \le {M^t\over t!}
             \le\left({eM\over t}\right)^t
             =\exp\{-\Omega(m\log m)\}.             \tag{3.5}
\]

There are only `2^{O(m)}` exposure vertices, so the total witness-event
mass is `o(1)`.

More importantly, the witness mass adjacent to one fixed object is also
`o(1)`.  For fixed `v` its value is at most

\[
        p_j{M^{t-1}\over(t-1)!},                    \tag{3.6}
\]

summed over a bounded seed neighbourhood.  Summing (3.6) over `v` costs
only `m^{O(1)}` by hypothesis 4 and is still
`exp(-Omega(m log m))`.

A local event therefore sees local-event charge `O(1/m)` and
witness-event charge `o(1)`.  A witness event uses `t=Theta(m)` objects,
so it sees local-event charge at most `t C_1/m=O(1)` and witness charge
`o(1)`.  Give local events weight `2 Pr(B_e)` and witness events weight
`A Pr(W)` for one fixed constant `A` larger than the exponential of that
`O(1)` charge.  The asymmetric local-lemma inequalities then hold for both
event classes.  Avoiding every witness gives (3.3).  `square`

For the tail chronology, a monotone piece contributes to a fixed exposure
vertex at most twice, and each tail macro has only a bounded number of
pieces.  The coarea calculation with one marked facet or cofacet gives
(3.2).  Thus Theorem 3.1 is the correct route to direct all-occurrence
exposure.  It does not require full pairwise Ore-halo disjointness at the
bottom layer.

## 4. A second correction: tail-only completion is not joint completion

After opening one nonpayload connector transition, the packed tail cycle
is a protected path forest of size `2^{o(m)}`.  Applying the
subexponential Hamilton-anchored completion theorem to this forest alone
does produce a spanning cycle cover with `2^{o(m)}` components.

That factor need not contain the already constructed central protected
bank.  Therefore it cannot be cited as a completion of the full
construction.

There is nevertheless a useful exact factor consequence.  Let `F_i^0` be
the two alternating matching classes of the central protected bank.  The
existing construction has

\[
 |F_i^0|\le 2^{m+o(m)},\qquad
 \widehat\alpha(F_i^0),\widehat\beta(F_i^0)\le10.  \tag{4.1}
\]

If a resource-disjoint tail forest `F_i^t` satisfies

\[
 |F_i^t|=2^{o(m)},\qquad
 \widehat\alpha(F_i^t),\widehat\beta(F_i^t)\le m/3, \tag{4.2}
\]

then the union has size `2^{m+o(m)}` and both exposure deficits obey

\[
 D_\alpha,D_\beta\ge {2m\over3}-O(1).              \tag{4.3}
\]

Consequently

\[
 m|F_i^0\cup F_i^t|=2^{m+o(m)}
   =o\left(\binom{2D_\alpha-1}{D_\alpha}ight)
   =o\left(\binom{2D_\beta-1}{D_\beta}ight).     \tag{4.4}
\]

The sharp protected-matching theorem therefore extends each combined
matching class to a perfect matching.  This gives an exact common
owner/lower-`q1` two-factor **conditional on the resource-disjoint tail
packing**.

The Hamilton-damage estimate cannot be applied to the combined bank to
deduce `2^{o(m)}` components: the central bank has `2^{m+o(m)}` protected
edges.  Bounded or subexponential topology of the combined completion
remains open.

## 5. The exact remaining tail-packing statement

To turn the draft into an unconditional theorem it remains to prove one
joint selection statement.

> **Tail boundary/co-selection lemma.**  Select the low collars, balanced
> high witnesses, residence-constrained connectors, and the polynomial
> co-singleton seasoning bank so that:
>
> 1. the connector external-rank band used in Section 1 is respected;
> 2. an explicit local fork table excludes every same-seam owner/lower/
>    upper equality;
> 3. every new base role is disjoint from the already protected central,
>    rolling, and hinge banks, including the small `s=3` boundary fibres;
> 4. the per-object collision charge is `O(1/m)`; and
> 5. the hypotheses of Theorem 3.1 hold for both alternating classes.

The first-draft point-load calculation proves the bulk part of item 4.
It does not prove item 3: polynomial external-trace load alone is
insufficient at the smallest `K` fibres.  Those boundary roles require an
explicit reservation/co-selection argument.

Once this lemma is proved, Theorem 3.1 and (4.4) close the complete
owner/lower-`q1` factor row.  They still do not fuse the residual
central-plus-tail factor into a resident bounded-component chronology,
install the PBBS arbitrary-width bank, or transport the terminal cap.
