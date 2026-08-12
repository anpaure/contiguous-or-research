# Audit of the variable-support facet ring and a symmetric decorated rectangle circulation

**Date:** 2026-08-07  
**Object audited:** `MATH_THEOREM_VARIABLE_SUPPORT_FACET_RINGS_AND_LITERAL_RECTANGLE_FUSION_20260807.md`  
**Method:** direct index/rank reconstruction, complementation, and orbit counting  
**Verdict:** **PASS**, with one scope clarification.  The individual ring and
rectangle theorems are correct.  Moreover, all labelled forward rectangle
trades over a fixed core form an exact proper-target and immediate-upper
**multicover circulation**.  This does not yet give a sequence of trades in a
one-copy owner decomposition, because the rectangles overlap heavily.

## 1. Facet-ring audit

Let `n=2r-1`, `D=d+1`, `D+1<=ell<=r+1`, and `a=ell-D`.  The source letter at
phase `t` is

\[
 A_t=K\cup\{f_{t-a+1},\ldots,f_t\},
 \qquad |K|=r-\ell+1.
\]

The union of the `q` source letters ending at `t` is

\[
 Z_{t,q}=K\cup\{f_{t-q-a+2},\ldots,f_t\}.
\]

The private interval has length `a+q-1`.  Since `q<=D`,

\[
 1\le a+q-1\le a+D-1=\ell-1,
\]

so it neither empties nor covers the private cycle.  Hence

\[
 |Z_{t,q}|=(r-\ell+1)+(\ell-D+q-1)=r-D+q.
\]

At `q=D`, its first index is `t-ell+2`, so it contains every private label
except `f_(t+1)`.  Therefore

\[
 Z_{t,D}=(K\cup F)-\{f_{t+1}\}.
\]

These are all `ell` facets of the common `(r+1)`-set `K union F`, in a simple
Johnson cycle.  At a proper width, the nonempty proper cyclic private interval
recovers `t`; its length recovers `q`.  Thus all same-ring proper targets are
literal-distinct, including across widths.  Finally, any finite cyclic source
word gives a balanced state circulation: every occurrence of a length-`d`
state has one entering and one leaving transition, counted with multiplicity.

This proves all four rows of Theorem 2.1.

## 2. Pull-overlay audit

For the periodic schedule `L^j H`, with `j<=d=D-1`, every `D`-window contains
a high phase.  It therefore restores all of `K`; the private union is unchanged.
The owner inventory is consequently still exactly the facet cycle above.

A `q`-window omits `J` exactly when it lies inside a low run.  Per period this
happens `j-q+1` times for `q<=j`, and zero times for `q>j`.  Dividing by the
period `j+1` gives exactly `(j+1)^(-1) S_(delta,j)`.  Intersecting any emitted
target with `F` still recovers the private cyclic interval, hence the width and
phase, irrespective of whether `J` is present.  Theorem 3.1 and the compatible
length range

\[
 D+1\le\ell\le r+1,\qquad j+1\mid\ell
\]

are correct.

## 3. Rectangle fit, complementation, and component count

Complementing an original rank-`r` facet owner gives a rank-`(r-1)` star

\[
 G+f,\qquad |G|=r-2.
\]

For disjoint `S,A,B` of sizes `r-3,p,p+1`, respectively, the total number of
used ground labels is

\[
 (r-3)+p+(p+1)=r+2p-2.
\]

It fits in `n=2r-1` exactly when `2p<=r+1`.  The `B`-centred decomposition has
`p+1` stars of size `p`; the `A`-centred decomposition has `p` stars of size
`p+1`.  The hypotheses

\[
 D+1\le p<p+1\le r+1
\]

put both lengths in the literal facet-ring range.  Both shores cover the same
`p(p+1)` complemented owners, and replacing the first by the second reduces
the number of cyclic source components by exactly one.  Every ring is itself
state-balanced, so the disjoint union is balanced on either shore.

The word "owner" in this rectangle section is used in the complemented
rank-`(r-1)` model.  The literal source rings still have original rank-`r`
owner windows.  Making that convention explicit would remove a possible
reader ambiguity, but no formula depends on it.

## 4. Proper-target and upper-palette ledger

Put

\[
 C=[n]-(S\cup A\cup B),\qquad |C|=r-2p+1,
 \qquad a_0=p-D.
\]

For a `B`-centred star with centre `S+b` and private set `A`, the original
source core is

\[
 [n]-(S\cup\{b\}\cup A)=C\cup(B-\{b\}).
\]

Its width-`q` private interval has length `a_0+q-1`, which gives exactly (5.3).
For an `A`-centred star, the source core is `C union (A-{a})`, its private set
has size `p+1`, and the interval length is `a_0+q`; this gives exactly (5.4).

At `q<D`, those interval lengths lie in `[1,p-2]` and `[2,p-1]`, respectively
(with the evident shorter lower endpoints when `p>D+1`), so all cyclic
intervals are proper and phase-recovering.  Intersections with `A` and `B`
recover both the missing centre label and the cyclic interval.  Thus each
shore has `p(p+1)` distinct proper targets.

An old-shore target has `a_0+q-1` labels in `A` and `p` in `B`; a new-shore
target has `p-1` in `A` and `a_0+q` in `B`.  Equality forces
`a_0+q=p`, hence `q=D`, excluded.  The two proper families are disjoint.

The common `(r+1)`-owner union in the ring centred at `S+x` is
`[n]-(S+x)`.  It occurs once at each of the ring's cyclic owner edges.  Hence
the old shore has `p` copies for each `b in B`, and the new shore has `p+1`
copies for each `a in A`.  These named upper families are disjoint.  The
entire ledger in Theorem 5.1 is correct.

## 5. A new exact symmetric circulation

Although one rectangle is maximally visible, its signed damage has no global
linear obstruction.

Fix `S` and `p`, and put `U=[n]-S`, so `|U|=r+2`.  Let `mathscr R(S,p)` contain
every datum

\[
 (A,B,\alpha,\beta),
\]

where `A,B` are disjoint subsets of `U` of sizes `p,p+1`, and `alpha,beta`
are cyclic orders on `A,B`.  Orient every datum in the component-reducing
direction

\[
 \mathcal D_B\longrightarrow\mathcal D_A.
\]

### Theorem 5.1 (symmetric decorated rectangle circulation)

The sum of all oriented trades in `mathscr R(S,p)` has:

1. zero owner current;
2. zero immediate-upper current;
3. zero proper-target current at every width `1<=q<D`; and
4. formal component current `-|mathscr R(S,p)|`.

#### Proof

Owner current is zero separately for every rectangle.

For the upper row, identify the original upper colour `[n]-(S+x)` with
`x in U`.  The symmetric group on `U` acts transitively on these colours and
preserves the complete indexed family `mathscr R(S,p)`.  Therefore the total
old multiplicity is constant in `x`, and so is the total new multiplicity.
Each individual trade has `p(p+1)` upper occurrences on either shore.
The two constants consequently have equal total mass and are equal pointwise.

For a proper width `q`, put

\[
 h=D-q+1\in\{2,\ldots,D\}.
\]

Complement an emitted proper target.  On the new shore it has the form

\[
 S\cup\{a\}\cup J,
 \qquad a\in A,
 \quad J\text{ a cyclic }h\text{-interval of }B;
\]

on the old shore it has the form

\[
 S\cup\{b\}\cup I,
 \qquad b\in B,
 \quad I\text{ a cyclic }h\text{-interval of }A.
\]

Thus every complemented target has the form `S union T` with
`T subset U`, `|T|=h+1`.  Because all disjoint `(A,B)` and all cyclic orders
are included, `Sym(U)` acts transitively on the target family and preserves
each shore.  Hence each shore has a constant multiplicity on the
`binom(r+2,h+1)` possible targets.  Both shores have `p(p+1)` occurrences per
indexed rectangle, so the constants agree.  Complementing back proves exact
proper-target cancellation.

Finally, every oriented rectangle replaces `p+1` ring components by `p`, so
the summed formal component current is `-|mathscr R(S,p)|`.  \(\square\)

### Scope

This theorem is an exact positive multicover identity: it uses only forward,
component-reducing rectangles, not cancellation by inserting inverse trades.
It proves that owner, proper-target, and immediate-upper incidence vectors
contain no linear separator against component reduction.

It is **not** yet a legal sequence in a one-copy whole-layer factor.  The
rectangles in `mathscr R(S,p)` overlap on owner vertices, and their old shores
need not coexist in one current decomposition.  The remaining rounding theorem
must select a compatible sparse subfamily (or decompose a sufficiently regular
owner multicover) while retaining the orbit-balanced current.  No such
one-copy realization is asserted here.

## 6. A fixed-core owner-disjoint rounding obstruction

The preceding scope issue is substantive.  In the triangular regime, a
pointwise upper-neutral positive circulation cannot be made owner-disjoint
while keeping the core `S` fixed.

### Theorem 6.1

Let `mathscr F` be a family of forward rectangles `(S;A,B)` with one fixed
`S`, such that their owner edge sets `K_(A,B)` in the complete graph on
`U=[n]-S` are pairwise edge-disjoint.  If the total immediate-upper current
of `mathscr F` is zero and

\[
                         2p(p+1)>r+1,                 \tag{6.1}
\]

then `mathscr F` is empty.

#### Proof

For `x in U`, let `N_A(x)` and `N_B(x)` count the rectangles in which `x`
lies in the `A`- and `B`-shore, respectively.  The upper current at the colour
`[n]-(S+x)` is

\[
                 (p+1)N_A(x)-pN_B(x).
\]

Pointwise cancellation and `gcd(p,p+1)=1` imply

\[
                 N_A(x)=p k_x,\qquad
                 N_B(x)=(p+1)k_x
\]

for an integer `k_x>=0`.  Every occurrence of `x` in an `A`-shore uses
`p+1` owner edges incident with `x`; every occurrence in a `B`-shore uses
`p` such edges.  Edge-disjointness therefore uses

\[
 (p+1)N_A(x)+pN_B(x)=2p(p+1)k_x
\]

distinct edges at `x`.  But the complete graph on `U` has degree

\[
 |U|-1=(r+2)-1=r+1.
\]

Under (6.1), this forces `k_x=0` for every `x`, hence there is no rectangle.
\(\square\)

For the optimal triangular scale, `d^2~(pi/4)r` and every admissible
`p>=D+1=d+2`; therefore

\[
 2p(p+1)\ge2(d+2)(d+3)\sim {\pi\over2}r>r+1.
\]

Thus the symmetric multicover identity cannot be rounded by merely choosing
an owner-disjoint subfamily at one core.  A successful decorated circulation
must mix different `(r-3)`-cores (so the same upper colour can receive current
through different `(S,x)` presentations), use temporary overlap with a later
owner rerouting, or combine additional actuator types.
