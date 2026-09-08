# Independent audit of the all-width common-mate `C8` spanning phased host

**Date:** 2026-08-12
**Primary source:**
`MATH_THEOREM_COMMON_MATE_C8_ALLWIDTH_COLLAR_SPANNING_PHASED_HOST_20260812.md`
**Companion reduction:**
`MATH_REDUCTION_COMMON_MATE_C8_ALLWIDTH_COLLAR_EXACT_ORE_GATE_AND_SELF_AUDIT_20260812.md`
**Audited input SHA256:** primary
`1c625076ac21b591a1ced44b19979e566071180c26c899f8a9aa61e6e6316e3f`;
companion
`d54d9578940692355183b68a0dcfd44f86b805089bea2e941e4f8b20ff6577d1`
**Verdict:** **PASS.**  No mathematical patch is required.  The local
two-transition closure, exposure bounds, Ore localization, partial-shadow
thresholds, numerical induction, phased two-factor completion, and switch
legality all verify under the stated `m>=12` hypothesis.

## 1. Literal two-transition closure

The fixed sets have

\[
 |C|=m-3,\qquad |Q|=4,\qquad t_i\in C,\qquad d_i\notin C\cup Q.
\]

Therefore

\[
 H_i=(C-t_i)\cup Q
\]

has rank `m`.  The four `H_i` are pairwise distinct because `H_i` omits
`t_i` and contains every other `t_j`.

Using

\[
 F_i=(C-t_i)\cup(Q-q_i)\cup\{d_i\},qquad
 R_i=C\cup(Q-q_{i+3}),
\]

one has

\[
 F_i-d_i+q_i=H_i,qquad H_i-q_{i+3}+t_i=R_i.
\]

Thus `F_i-H_i-R_i` is exactly a two-step Johnson path.  Its two lower
colours are

\[
 J_i^0=(C-t_i)\cup(Q-q_i),qquad
 J_i^1=(C-t_i)\cup(Q-q_{i+3}).
\]

They are distinct for fixed `i`, and different missing-core labels separate
different `i`.  Every old bridge lower colour with missing core `t_i`
contains a `Z` label, whereas `J_i^0,J_i^1` use only `Q` outside the core.
Every neutral lower colour contains the full core.  Hence the closure adds
no lower-colour collision.  The same signatures show that no `H_i` is an
old owner.

The old path has `2m+2` incidence edges.  Beginning at `R_i` in phase zero,
it consequently ends at `F_i` in phase one.  The four closure incidences

\[
 F_i-J_i^0-H_i-J_i^1-R_i
\]

may therefore be coloured `0,1,0,1`; both joins alternate correctly.  Each
old path becomes one properly phased incidence cycle, and the four cycles
are vertex-disjoint.

The counts are exact.  Before closure one path has `m+2` owners, `m+1`
lower colours, and `2m+2` incidences.  Closure adds one owner, two lower
colours, and four incidences.  Hence four closed cycles have

\[
 |\mathcal U(P^\circ)|=4m+12,qquad
 |Z(P^\circ)|=4m+12,qquad
 |E(P^\circ)|=8m+24.
\]

All protected vertices on both shores have degree two.

## 2. All-width transparency survives closure

The switch changes only the incoming incidences `R_iL_i`.  Before a
crossing owner interval reaches `F_i`, Theorem 7.1 gives equal cumulative
unions in the old and switched phases.  At `F_i` that cumulative union is
the full ground set `[2m-1]`.  Appending `H_i`, `R_i`, or any later owner
cannot change it.  Thus intervals ending before `F_i` retain the prefix
identity, intervals extending through the closure are full in both phases,
and noncrossing intervals are copied literally.  No new width exception is
introduced.

## 3. Exposure audit

Write

\[
 D=[2m-1]\setminus C=Q\cup\{c\}\cup Z.
\]

### 3.1 The `beta` bound

The protected lower colours containing the full core correspond to edges
of the graph on `D` formed by:

* the four cyclic edges of `Q`;
* the four edges `cq`, `q in Q`; and
* the edges `qz_j`, `q in Q`, `1<=j<H`.

An owner containing `C` is `C` plus a three-set in `D`, which spans at most
three of these edges.  It can also contain missing-core protected colours
only when its outside triple equals their outside triple.  A nonrepeated
triple contributes at most one such colour.  The only repeated triples are
the four active triples `Q-q_j`, each occurring in the two closure rows;
such a triple spans exactly two cyclic edges and contributes exactly two
missing-core colours.  Thus the total is at most four.

An owner missing exactly `t_i` can contain only the five missing-`t_i`
protected lower colours.  Their outside triples are the three consecutive
bridge triples and the two closure triples.  Direct union inspection shows
that no four-set contains more than two of them.  An owner missing two or
more core labels contains none.  Therefore

\[
 \beta(P^\circ)\le4.
\]

### 3.2 The `alpha` bound

An unused lower vertex containing `C` is `C` plus a pair in `D`.  Every
pair occurs in at most four protected full-core owner triples; the extremal
case is a consecutive neutral pair `z_(j-1)z_j`, including `z_0=c`, which
occurs once for each active `q`.

An unused lower vertex missing exactly `t_i` lies under at most two of the
four missing-`t_i` protected owners and under at most one full-core owner.
If it misses two core labels, it lies under at most one protected owner on
each corresponding path; the only repeated outside four-set is `Q`, in the
owners `H_i`.  Missing three core labels is impossible below a protected
owner.  Hence

\[
 \alpha(P^\circ)\le4.
\]

No omitted closure colour or owner raises either exposure.

## 4. Exact applicability of the cited Ore theorems

The protected near-shadow theorem assumes only a subgraph of `ML_m` with
maximum degree at most two.  The closed bank satisfies this exactly.  For a
failed shore it gives, with `e=|E(P^circ)|`,

\[
 \min\{|A|,W-|A|\}
 <\frac{m(m-1)}{2m-1}e.
\]

The sublinear-exposure note is introduced using an owner-path forest, but
the proofs of its two threshold results use only:

1. every used lower vertex has protected degree two;
2. every unused lower vertex has residual demand two;
3. every protected owner has degree at most two; and
4. the literal exposure bounds `alpha,beta`.

They do not use acyclicity.  Therefore they apply unchanged to the four
closed cycles.  Since `m>=12` and `alpha,beta<=4`, their hypotheses
`alpha,beta<=m-3` and `D>=2` hold.  They yield

\[
 |A|\ge K(m-5),qquad
 |B|\ge K(m-5)+1,qquad
 K(D)={2D-1\choose D},
\]

where `B=(L\setminus Z(P^circ))\setminus A`.  The optional-complement
identity is exact because every protected lower vertex is saturated and
the total residual demand equals total residual owner capacity.

## 5. Numerical separation

Here

\[
 e=8m+24,qquad
 T_m=\frac{m(m-1)}{2m-1}(8m+24).
\]

At `m=12`,

\[
 K(m-5)=K(7)={13\choose7}=1716,qquad
 T_{12}=\frac{15840}{23}<689.
\]

Furthermore

\[
 \frac{K(m-4)}{K(m-5)}
 =\frac{(2m-9)(2m-10)}{(m-4)(m-5)}>3
\]

for `m>=12`, while direct cancellation gives

\[
 \frac{T_{m+1}}{T_m}
 =\frac{(m+1)(m+4)(2m-1)}{(m-1)(m+3)(2m+1)}<2.
\]

Thus `K(m-5)>T_m` for every `m>=12`.

If localization selects the small side, `|A|<T_m` contradicts the first
threshold.  If it selects the co-small side, then

\[
 |B|=W-|Z(P^\circ)|-|A|<W-|A|<T_m,
\]

contradicting the optional threshold.  Hence no residual Ore cut fails.

## 6. Ordered phases and switch legality

Ore--Ryser supplies a spanning two-factor containing `P^circ`.  Since every
vertex of each protected cycle is already saturated, each remains an entire
factor component.  Its prescribed alternating colouring is therefore
independent of the colouring choices on all other cycles.  The two colour
classes are ordered perfect matchings `M_0,M_1`.

Every `L_i` is already incident in `P^circ` with its prescribed old
phase-zero edge `L_iR_i` and its phase-one edge `L_iU_i`.  Hence no proposed
new incidence `L_iR_(i-1)` occurs in the containing factor.  The four new
incidences are genuine containment edges, pairwise distinct, and replacing

\[
 L_iR_i\longmapsto L_iR_{i-1}
\]

permutes the four phase-zero partners.  Thus `M_0` remains a perfect
matching and `M_1` is unchanged.  The switched object is another ordered
two-SDR.  The all-width current is zero and the socket action is the odd
cycle `i->i+1` by the audited local collar theorem.

The conclusion is exactly a spanning phased two-factor host.  It does not
assert one factor cycle, upper-surjectivity, residence, inherited MNW socket
identification, or lower/common-cap compilation.

## 7. Companion reduction

The unclosed-bank reduction is internally consistent:

* its shore and edge counts `4m+4`, `4m`, `8`, and `8m+8` are exact;
* its residual capacities are `0,1,2` on internal, endpoint, and unused
  owners;
* equations (2.3) and (2.5) are the exact capacitated Hall/Ore--Ryser
  criterion; and
* the complement overflow equation (3.6) follows by comparing against the
  full residual cut.

The companion reduction does not by itself prove the unclosed bank
extendable.  The spanning-host theorem proves that the stronger closed bank
is contained in a factor.  That same factor already contains the original
unclosed protected paths, so the reduction's criterion follows a
posteriori; no deletion from the factor is required.
