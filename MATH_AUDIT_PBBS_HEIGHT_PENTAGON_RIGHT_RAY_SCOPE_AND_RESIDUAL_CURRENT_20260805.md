# Audit of the PBBS height-pentagon `q1` and right-ray theorem

**Date:** 2026-08-05  
**Method:** cyclic-parenthesis normalization and literal set algebra; no
search or computation  
**Audited file:**
`MATH_THEOREM_PBBS_HEIGHT_PENTAGON_FORCED_Q1_AND_RIGHT_RAY_REGENERATION_20260805.md`

## 0. Verdict

The two substantive identities in the audited theorem are correct:

\[
 P_i\cup Q_{i+1}=P_{i+1}\cup Q_{i+1}\qquad(h\ge4),       \tag{0.1}
\]

and consequently

\[
 P_i\cup B_{i+1}(v)=P_{i+1}\cup B_{i+1}(v)               \tag{0.2}
\]

for every prefix of the **retained cut arc** beginning at `Q_(i+1)`.
For the distinguished arrow `0 -> 1`, both identities hold already for
every `h>=2`.

There are two scope corrections.

1.  Equation (0.2) gives a value- and width-preserving **bijection between
    old and new occurrence addresses**.  It does not fix the physical
    occurrence address: `(i+1,1,v)` moves to `(i,1,v)`.
2.  It closes the right-ray sector only.  The one-cut residual contains
    every cell with incoming penetration `u>=2`, including the left-ray
    boundary `v=1`.  In addition, every interval traversing two or more
    rethreaded edges belongs to a separate path-state current.  Thus the
    residual must not be described merely as intervals having nontrivial
    penetration beyond the endpoint on both sides.

With those corrections, the theorem is proof-safe.  In particular, it
does prove complete high-pentagon `q1` regeneration and an injective
transport of all high-pentagon right-ray occurrences.

## 1. Literal normalization and the common deletion coordinate

Put `t=r-h-1`.  The five states from the pentagon theorem, rooted at their
forward-unmatched zero and with that root removed, are

\[
\begin{aligned}
 D_h^0&=1^h0^{h-1}(10)^{r-h}0,\\
 D_h^1&=1^{h+1}0^{h+1}(10)^t,\\
 D_h^2&=(10)^t1101^{h-1}0^h,\\
 D_h^3&=1(10)^t0101^{h-1}0^{h-1},\\
 D_h^4&=1^{h-1}0^{h-1}11(10)^t00.
\end{aligned}                                             \tag{1.1}
\]

This follows directly from the physical words in (3.4) of
`MATH_THEOREM_PBBS_AH_LADDER_PENTAGON_RETURN_20260805.md` and the forward
survivors

\[
 z_1,z_0,z_2,a,c.                                        \tag{1.2}
\]

The first up-step reaching the global maximum is the physical coordinate

\[
 p=h+1                                                       \tag{1.3}
\]

for `D_h^0,D_h^1,D_h^2` at every `h>=2`, and for all five rows when
`h>=4`.  In the final row at `h=4`, the initial height-three peak occurs
before any later tie, so the same first-maximum rule still selects `p`.

There is one harmless low-height correction to the displayed maximum
table in the audited theorem.  For `D_h^4` the exact maximum is

\[
 \max\{h-1,\ 2+\mathbf 1_{t>0}\},                         \tag{1.4}
\]

not always `max{h-1,3}`.  At `(h,r)=(3,4)` the exact maximum is two, not
three.  This does not affect any claim using all five common deletions,
because those claims begin at `h=4`; nor does it affect the distinguished
`0 -> 1` arrow.

The coordinate `p` lies in the common core `L_h`, whereas every pentagon
deletion and insertion belongs to

\[
 \{z_0,z_1,c,a,z_2\}.                                    \tag{1.5}
\]

Hence, writing `r_i=p_+(Z_i)` and
`Z_(i+1)=Z_i-{d_i}+{r_i}`, the distinguished-deletion PBBS formula is

\[
 g(Z_i)=Z_i-\{p\}+\{r_i\}                                \tag{1.6}
\]

for every role when `h>=4`.  The three labels `p,d_i,r_i` are distinct.

## 2. Exact `q1` regeneration

Recall

\[
 Q_i=[n]\setminus Z_i,\qquad
 P_i=[n]\setminus g(Z_i).                                \tag{2.1}
\]

The old edge at role `i` is `P_i Q_i`, and the new edge at role `i` is
`P_i Q_(i+1)`.  Taking complements and applying (1.6),

\[
\begin{aligned}
 (P_i\cup Q_{i+1})^c
   &=g(Z_i)\cap Z_{i+1}\\
   &=(Z_i-\{p\}+\{r_i\})
        \cap(Z_i-\{d_i\}+\{r_i\})\\
   &=Z_{i+1}-\{p\}.                                     \tag{2.2}
\end{aligned}
\]

At the next role,

\[
 (P_{i+1}\cup Q_{i+1})^c
   =g(Z_{i+1})\cap Z_{i+1}=Z_{i+1}-\{p\}.                \tag{2.3}
\]

Equations (2.2)--(2.3) prove (0.1).  The cyclic shift `i+1 -> i` is a
bijection on the five roles, so the complete old and new upper-`q1`
palettes agree as multisets, including multiplicities.

For `i=0`, only the first two normalized roots are needed.  They have the
same physical deletion `p=h+1` for every `h>=2`, and their root insertions
are respectively `z_1,z_0`.  Thus

\[
 P_0\cup Q_1=P_1\cup Q_1                                \tag{2.4}
\]

at every height.  This is exactly the old selected `q1` value whose
deficit-three core has gap vector `(0,0,3)`.  The gap theorem makes its old
corrected occurrence unique, but (2.4) supplies a new occurrence, so
uniqueness of the old occurrence does not create a hole.

## 3. Exact occurrence-labelled right-ray map

Delete all chosen old matching edges and orient every retained arc.  For a
cut role `j`, let `B_j(v)` be the union of the first `v` owners of the
retained arc beginning at `Q_j`, stopping no later than the tail immediately
before the next deleted edge.  Thus

\[
 Q_j\subseteq B_j(v).                                    \tag{3.1}
\]

For a high pentagon define

\[
 \Psi_h:(j,1,v)_{\rm old}\longmapsto(j-1,1,v)_{\rm new}
 \qquad(j\in\mathbb Z_5),                               \tag{3.2}
\]

where `u=1` means that the interval uses only the endpoint owner on its
incoming side.  The old and new values are respectively

\[
 P_j\cup B_j(v),\qquad P_{j-1}\cup B_j(v).               \tag{3.3}
\]

Using (0.1) with `i=j-1` and then (3.1),

\[
\begin{aligned}
 P_j\cup B_j(v)
   &=(P_j\cup Q_j)\cup B_j(v)\\
   &=(P_{j-1}\cup Q_j)\cup B_j(v)\\
   &=P_{j-1}\cup B_j(v).                                \tag{3.4}
\end{aligned}
\]

Both occurrences have the same width.  Map (3.2) is injective on complete
occurrence addresses: cyclic role shift is injective, distinct prefix
lengths remain distinct, and pentagons at different heights have disjoint
new first edges.  It is therefore legitimate to transport a declared
upper witness through `Psi_h`.

What is preserved is the target value and a declared occurrence matching,
not the literal address itself.  In particular, an occurrence-sensitive
cap may be transported only if its additional type and capacity data are
also mapped; (3.4) alone does not prove such a cap isomorphism.

At heights two and three, the same argument gives only the distinguished
map

\[
 (1,1,v)_{\rm old}\longmapsto(0,1,v)_{\rm new}.          \tag{3.5}
\]

No all-role assertion at those heights follows from the common-deletion
calculation.

The phrase "every exterior prefix" must mean every prefix of one retained
arc as above.  Once an interval crosses a second deleted/rethreaded edge,
its subsequent arc word depends on the splice permutation and is not
covered by (3.4).

## 4. The exact one-cut residual

Let `A_i(u)` be the union of the last `u` owners of the retained incoming
arc ending at `P_i`, with `A_i(1)=P_i`; let `B_i(1)=Q_i`.  For a single
pentagon put

\[
\begin{aligned}
 J^-_{i;u,v}&=[i,u,v;\ A_i(u)\cup B_i(v)],\\
 J^+_{i;u,v}&=[i,u,v;\ A_i(u)\cup B_{i+1}(v)].           \tag{4.1}
\end{aligned}
\]

The full one-cut occurrence current is

\[
 \partial_h^{(1)}=\sum_{i,u,v}J^+_{i;u,v}
                    -\sum_{i,u,v}J^-_{i;u,v}.            \tag{4.2}
\]

For `h>=4`, Section 3 supplies the complete occurrence matching

\[
 J^-_{i+1;1,v}\longleftrightarrow J^+_{i;1,v}            \tag{4.3}
\]

with equal values.  After removing these matched demand--supply pairs, the
exact one-cut residual is

\[
 \boxed{
 \partial_{h,\rm res}^{(1)}
   =\sum_{i,\,u\ge2,\,v}J^+_{i;u,v}
    -\sum_{i,\,u\ge2,\,v}J^-_{i;u,v}.}                  \tag{4.4}
\]

Formula (4.4) is an occurrence current.  Forgetting addresses gives the
corresponding target-value current used for support domination.

Crucially, (4.4) contains the sector `u>=2,v=1`.  These are left-ray
occurrences: they penetrate the incoming arc beyond `P_i` but use only
`Q_i` on the outgoing side.  They have not been regenerated.  Thus the
remaining one-cut problem is "nonminimal incoming penetration", not only
"nonminimal penetration on both sides".

At `h=2,3`, subtract only the matched family (3.5) from (4.2); all other
one-cut terms remain in the proof-safe residual.

## 5. The complete multi-cut path-state current

For completeness, delete the entire simultaneous ladder cut set and let
`C_a` (`a` in `mathcal A`) be the resulting oriented retained arc words.
Write `H_a` and `T_a` for the first and last owners of `C_a`.  The old and
new matchings induce splice bijections `s_0,s_1` on `mathcal A`: after
reaching `T_a`, the next retained arc is `C_(s_epsilon(a))` in phase
`epsilon in {0,1}`.

For every admissible address `(a,t,u,v)` with `t>=1`, put

\[
\begin{aligned}
 V_\epsilon(a,t,u,v)
  ={}&\operatorname {Suf}_u(C_a)\\
    &\cup\bigcup_{j=1}^{t-1} C_{s_\epsilon^j(a)}
     \cup\operatorname {Pre}_v(C_{s_\epsilon^t(a)}).
                                                               \tag{5.1}
\end{aligned}
\]

Here admissibility means that the address describes a proper contiguous
interval in the chosen linear opening (or a non-full interval in a cyclic
component), so duplicate full-cycle descriptions are omitted.  The exact
complete exterior current is

\[
 \partial_{\rm ext}
 =\sum_{a,t,u,v}[+,a,t,u,v;V_1(a,t,u,v)]
  -\sum_{a,t,u,v}[-,a,t,u,v;V_0(a,t,u,v)].               \tag{5.2}
\]

Its `t=1` part is (4.2), after translating arc and cut-role indices.  The
right-ray theorem removes exactly the eligible `t=1,u=1` pairs described
in Section 3.  Therefore, for high pentagons, the unresolved tensor is

\[
 \boxed{
 \partial_{\mathrm{ext}}^{\mathrm{res}}
   =\partial_{\ge2\ \text{ cuts}}
     +\partial_{1\ \text{ cut},\ u\ge2},}              \tag{5.3}
\]

together with the unpaired bottom-height terms and any independent typed
cap or zero-gap seam state.  No identity in the audited theorem cancels
the `t>=2` part: after the next splice, the old and new arc itineraries may
already differ.

Equation (5.3), rather than a generic "two-sided target" phrase, is the
exact remaining upper-current gate.

## 6. Proof-safe consequences

The audited theorem establishes all of the following.

1.  The forced selected `q1` occurrence at every ladder height is recreated.
2.  Every height `h>=4` pentagon preserves its complete upper-`q1` palette
    as a multiset.
3.  Every high-pentagon right-ray occurrence within one retained cut arc
    has an injectively matched new occurrence of the same value and width.
4.  These maps remain injective across the simultaneous height ladder.

It does **not** establish any of the following.

1.  preservation of left rays (`u>=2,v=1`);
2.  preservation of arbitrary multi-cut intervals;
3.  pointwise fixation of physical occurrence addresses;
4.  transport of phase flags, shared cap resources, or zero-gap seam data;
5.  bounded support of (5.3).

Accordingly the next PBBS theorem must control the complete residual
path-state current (5.3), or provide independent alternate witnesses for
its negative support.  Re-proving `q1` or right-ray coverage cannot close
that remaining row.
