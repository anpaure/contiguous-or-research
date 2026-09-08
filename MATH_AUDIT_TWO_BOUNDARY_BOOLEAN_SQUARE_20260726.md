# Two-boundary Boolean squares versus full-parent erasure

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The full-parent erasure theorem and the two-boundary theorem concern
different placements of the switches.

* If a size-\(s\) replacement fixes both complementary child ports and all
  its changed phases lie strictly between them, then every full-parent
  matched intersection forgets the replacement.
* If a replacement in a size-\((s+1)\) parent changes the two phases which
  are themselves the endpoints of the serviced child window, then those
  two choices can survive. With disjoint coordinate pairs they can give a
  literal Boolean square of four physical targets.

Thus the two-boundary mechanism genuinely evades strict-interior erasure
for the one window whose endpoints it changes. It does not yet prove PCap.
Four exact obstructions remain.

1. In the canonical Klein-four ownership overlay, the entire
   no-interior-return block is one component. Its four shores merely
   permute
   \[
   (C_s,C_{s-1},C_{s-1},C_{s-2}),
   \]
   so one cell always retains load (C_s>p). Thus the canonical coordinate
   implementation is ruled out throughout the whole early regime, not
   merely above a scalar threshold.
2. The four target cells have canonical auxiliary load. For the natural
   two-end leaf realization their target-orbit mass is at least
   \[
   M_s=\operatorname {Cat}_s+
       2\operatorname {Cat}_{s-1}+\operatorname {Cat}_{s-2}.
   \tag{0.1}
   \]
   This mass is invariant under the two endpoint transpositions. Hence
   four bins of cap \(p\) are impossible whenever \(M_s>4p\).
3. The complete elementary-rectangle families whose pointwise positive
   collision is proved below \(p\) move only
   \(O(\operatorname {Cat}_{s-2})\) source occurrences. That is collision
   safety, not a balanced four-cell construction.
4. The local collision estimate does not include pre-existing background
   load, collisions between different parent contexts, or the joint
   component constraint needed to choose both endpoint bits.

Put \(d=\operatorname {Cat}_s=\theta p\), where \(s\) is minimal with
\(d\ge p\). Then

\[
 \frac{M_s}{d}
 =\frac{5s(5s-7)}{4(2s-1)(2s-3)}
 =\frac{25}{16}+O(s^{-1}).
 \tag{0.2}
\]

Consequently even a hypothetical fragmentation which remains inside the
same four-cell coordinate orbit has the exact mass obstruction

\[
 \boxed{K_p\big|_{\square}\ge(M_s-4p)_+,}
 \tag{0.3}
\]

and cannot work when

\[
 \boxed{
 \theta>
 \theta_{\square}(s):=
 \frac{16(2s-1)(2s-3)}{5s(5s-7)}
 =\frac{64}{25}+O(s^{-1}).}
 \tag{0.4}
\]

The lower part \(1\le\theta\le64/25+o(1)\) is not refuted by the orbit
census alone. It *is* refuted for the canonical coordinate overlay by
component indivisibility: one shore always carries the entry (C_s>p).
What remains open is a genuinely non-coordinate packet or trade which
fragments or replaces this component, together with a balanced-contingency
and cross-context residual-capacity theorem.

## 1. Exact reconciliation of the two locality statements

Let

\[
 X_0,X_1,\ldots,X_{s+1}
 \tag{1.1}
\]

be a rooted parent trace. The distinguished size-\(s\) child window is a
consecutive subtrace. There are two cases.

### Case I: strict child substitution

The replacement fixes the two child boundary states

\[
                         P,\qquad J\setminus P.
 \tag{1.2}
\]

A parent window containing the complete child slab therefore has local
intersection contained in

\[
                         P\cap(J\setminus P)=\varnothing.
 \tag{1.3}
\]

Every switch strictly inside the child is erased. This is Theorem 3.1 of
MATH_THEOREM_EARLY_CATALAN_FOUR_BIN_ERASURE_20260726.md.

### Case II: endpoint-aligned parent substitution

The outer parent ports \(X_0,X_{s+1}\) remain fixed, but one changes the two
internal states which are the endpoints of the serviced child window.
The octahedral identity erases every changed phase strictly between those
endpoints, while the two endpoint states remain visible. Two disjoint
coordinate pairs can therefore give

\[
 T_{\epsilon,\eta}
 =K\cup\{x_L(\epsilon),x_R(\eta)\},
 \qquad(\epsilon,\eta)\in\{0,1\}^2.
 \tag{1.4}
\]

The four targets in (1.4) are distinct.

There is no contradiction: Case II is not a port-preserving substitution
of the child. It is a port-preserving substitution of its parent which
changes the child's exported entrance and exit states. This is exactly the
escape explicitly left open by the erasure theorem.

### Lemma 1.1 (required separation of affected phases)

The assertion that all nonendpoint switches erase by the local identity

\[
                         L\cap M\cap R
                       = L\cap M'\cap R
 \tag{1.5}
\]

is valid for a family of switches when the closed three-phase
neighbourhoods of its changed states are disjoint, or when a separate
multi-switch identity proves (1.5) after the neighbouring changes.
Merely saying that the changed phases are distinct is insufficient:
another switch may change \(L\) or \(R\).

#### Proof

The proof of (1.5) uses the actual neighbouring states \(L,R\). If they
are unchanged, the identity applies verbatim. If a second move changes
one of them, the old identity says nothing about the new triple. \(\square\)

The fixed-scale elementary rectangle atlas has disjoint affected edges,
so this caveat does not invalidate that atlas. It must be checked anew for
arbitrary nested collections.

## 2. The natural four-cell orbit already carries auxiliary mass

Take two disjoint endpoint coordinate pairs

\[
 \{\beta_L,\gamma_L\},\qquad
 \{\beta_R,\gamma_R\},
 \tag{2.1}
\]

and the four targets

\[
 T_{00}=K\cup\{\beta_L,\beta_R\},\quad
 T_{10}=K\cup\{\gamma_L,\beta_R\},\quad
 T_{01}=K\cup\{\beta_L,\gamma_R\},\quad
 T_{11}=K\cup\{\gamma_L,\gamma_R\}.
 \tag{2.2}
\]

For the standard two-end MSW leaf realization, the canonical rooted
occurrences contributing to these cells are respectively indexed by

\[
\begin{array}{c|c|c}
\text{cell}&\text{Dyck-root condition}&\text{count}\\ \hline
00&x\in\mathcal D_s& C_s,\\
10&x=10u,\ u\in\mathcal D_{s-1}& C_{s-1},\\
01&x=u10,\ u\in\mathcal D_{s-1}& C_{s-1},\\
11&x=10u10,\ u\in\mathcal D_{s-2}& C_{s-2}.
\end{array}
\tag{2.3}
\]

The endpoint-window formulas identify the four physical targets in (2.3)
with (2.2). For the obstruction below, equality is not needed: the
displayed occurrences already give the lower bound

\[
 \sum_{\epsilon,\eta}\mu(T_{\epsilon,\eta})\ge M_s.
\tag{2.4}
\]

There is a stronger fact for the canonical implementation.  In the parent
factor (F_{s+1}), the no-interior-return roots split as

\[
 \{1u0:u\in\mathcal D_s\}\ \dot\cup\
 \{10\,1v0:v\in\mathcal D_{s-1}\}\ \dot\cup\
 \{1v0\,10:v\in\mathcal D_{s-1}\}\ \dot\cup\
 \{10\,1w0\,10:w\in\mathcal D_{s-2}\}.
\tag{2.5}
\]

The exact one-end ownership theorem and its right-end mirror join all four
families in (2.5) into one component of the four-factor overlay
(F_{s+1},LF_{s+1},RF_{s+1},LRF_{s+1}).  Both endpoint relations preserve
all interior return cuts, so this component cannot mix with any other
root type.  On its four shores the distinguished-window load vector is
only permuted:

\[
                 (C_s,C_{s-1},C_{s-1},C_{s-2}).
\tag{2.6}
\]

### Corollary 2.1 (canonical component no-go)

Every legal shore choice in the canonical Klein-four overlay leaves one
of the four cells with load at least (C_s).  Hence, whenever (C_s>p),
the canonical coordinate Boolean square fails even inside one parent
context.

This is stronger than the orbit-total inequality below.  The latter is
still useful because it survives a hypothetical fragmentation into
smaller coordinate components.

### Theorem 2.2 (four-orbit cap floor)

Along every sequence of component switches generated by the two endpoint
coordinate transpositions, the total load on the four-set orbit (2.2) is
invariant. Therefore

\[
 \sum_{\epsilon,\eta}
   (\mu(T_{\epsilon,\eta})-p)_+
 \ge (M_s-4p)_+.
\tag{2.5}
\]

#### Proof

Each row replacement is a coordinate image under the group generated by
the two disjoint transpositions. Summing a row's target incidence over a
group orbit is coordinate-invariant. Hence the orbit total is invariant.
For four nonnegative loads of total at least \(M_s\),

\[
 \sum_{i=1}^4(x_i-p)_+\ge\left(\sum_{i=1}^4x_i-4p\right)_+.
\]

This proves (2.5). \(\square\)

The exact Catalan ratios are

\[
 \frac{C_{s-1}}{C_s}
 =\frac{s+1}{2(2s-1)},\qquad
 \frac{C_{s-2}}{C_s}
 =\frac{s(s+1)}{4(2s-1)(2s-3)}.
\tag{2.6}
\]

Thus

\[
\begin{aligned}
\frac{M_s}{C_s}
&=1+\frac{s+1}{2s-1}
  +\frac{s(s+1)}{4(2s-1)(2s-3)}\\
&=\frac{5s(5s-7)}{4(2s-1)(2s-3)},
\end{aligned}
\tag{2.7}
\]

which gives (0.2)--(0.4).

## 3. The proved elementary-arm bound is not a four-cell realization

At the early scale, one complete elementary boundary family has

\[
                         f=C_{s-2}
\tag{3.1}
\]

row-disjoint rectangles. Two boundary families can therefore move at
most \(2f\) distinguished source occurrences. To lower a source cell of
load \(d=C_s\) to cap \(p=d/\theta\), at least

\[
                         d-p
\tag{3.2}
\]

source occurrences must leave it.

### Proposition 3.1 (elementary supply threshold)

The two complete elementary boundary families can have enough
distinguished source action only if

\[
 2C_{s-2}\ge C_s-p,
\tag{3.3}
\]

equivalently

\[
 \boxed{
 \theta\le
 \frac1{1-2C_{s-2}/C_s}
 =\frac87+O(s^{-1}).}
\tag{3.4}
\]

#### Proof

Each elementary rectangle has one distinguished negative source arm.
There are \(f\) rectangles at each endpoint. This proves the upper bound
\(2f\). Rearranging (3.3) and using (2.6) gives (3.4). \(\square\)

Therefore the pointwise estimate

\[
                         2C_{s-2}<p
\tag{3.5}
\]

has the following exact meaning: even if all positive arms from the two
families collide, their new mass fits below an empty cap-\(p\) target.
It does not say that enough old source mass moves, and it does not produce
the four cell counts \(n_{00},n_{01},n_{10},n_{11}\).

Larger ownership components can move more source mass, but then their two
boundary component partitions cross rather than refine one another. Their
joint four-cell table remains an unproved signed-discrepancy problem.

## 4. Audit of the full affected profiles

For one elementary rectangle, the complete fixed-depth signed vector is

\[
\begin{aligned}
d_q={}&
 \partial\operatorname {suf}_{\ell}(\mathsf O)
+\partial\operatorname {suf}_{\ell}(\mathsf E)\\
&-\partial\operatorname {pre}_{\ell}(\mathsf E)
-\partial\operatorname {pre}_{\ell}(\mathsf O).
\end{aligned}
\tag{4.1}
\]

At an internal rank the four positive targets and four negative targets
are distinct. Hence, for one additive family of \(f\) rectangles in one
parent,

\[
 \left\|\sum_{e\in\mathcal E}(d_{q,e})_+\right\|_\infty
 \le f,
\tag{4.2}
\]

and for two additive boundary families the crude bound is \(2f<p\).
This verifies the new-positive-arm part of the one-parent claim under
the affected-neighbourhood hypothesis of Lemma 1.1.

It does not verify cap safety. The exact hinge sees the residual capacity

\[
                         c_\beta(S)=(p-\beta(S))_+,
\tag{4.3}
\]

where \(\beta(S)\) includes every canonical occurrence and every other
context. The required condition is

\[
 \sum_C u^+_C(S)\le c_\beta(S)
 \qquad\text{for every physical target }S,
\tag{4.4}
\]

not merely \(\sum_Cu^+_C(S)<p\) for one parent.

There are four remaining failures of inference.

1. Old load: a target with fewer than \(p\) new occurrences may already
   have background load close to or above \(p\).
2. Negative placement: pointwise control of positive arms says nothing
   about whether the negative arms actually leave overloaded targets.
3. Joint endpoint choice: the two component partitions are nonlaminar.
   Choosing each marginal does not realize a balanced \(2\times2\)
   contingency table.
4. Nonadditive overlap: if the two endpoint families change adjacent
   states or share rows in overlapping slabs, (4.1) cannot simply be
   summed. They must be treated as one joint ownership atom.

Thus the complete four-arm formula is necessary and useful, but the
one-parent estimate proves only an \(L^\infty\) bound on fresh positive
arms.

## 5. Cross-context collisions

For one exterior core \(E\), the four targets in (2.2) are distinct.
For two different parent contexts \(C,C'\), nothing in the Boolean-square
lemma excludes

\[
 E_C\cup K_C\cup\{x_L,x_R\}
 =
 E_{C'}\cup K_{C'}\cup\{x'_L,x'_R\}.
\tag{5.1}
\]

Consequently the one-parent estimate does not tensor over an aligned
atlas. The exact global pointwise quantity is

\[
 \boxed{\max_S\sum_C u^+_{C,G_C,q}(S),}
\tag{5.2}
\]

or, with background included, the residual hinge in (4.4).

If two contexts have disjoint phase slabs but their targets coincide, their
histograms add and may cross the cap. If their phase slabs overlap, they
must first be grouped into one joint atom; independent component choices
are then unavailable. A common exterior set preserves four labels inside
one context, but supplies no marker distinguishing two contexts.

No cross-context injectivity or bounded-congestion theorem is proved in the
two-boundary note. The canonical plateau construction itself is a warning:
many distinct rooted occurrences and, potentially, several aligned context
groups may have one physical target.

## 6. Exact remaining region

The canonical two-boundary coordinate construction is ruled out for every

\[
                         \theta>1
\tag{6.1}
\]

because its principal no-interior-return block is one component and every
shore retains a cell of load (C_s). Even a hypothetical coordinate
fragmentation of that block would remain ruled out by the four-orbit
census when

\[
                         \theta>\frac{64}{25}+o(1).
\tag{6.2}
\]

Independently, the certified elementary family is too sparse already for

\[
                         \theta>\frac87+o(1).
\tag{6.3}
\]

Thus the only surviving version is a genuinely non-coordinate packet or
trade which fragments or replaces the principal block. Such a proof still
needs:

1. a joint legal two-boundary component selection whose four cell counts
   are at most the residual capacities, not merely \(p\);
2. the full four-arm hinge inequality at every protected depth;
3. a cross-context marker or congestion theorem; and
4. an atomwise multiplicity bound after all overlapping contexts are
   grouped.

Accordingly:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
The two-boundary construction genuinely escapes strict-interior erasure
for an endpoint-aligned window, so the erasure theorem does not refute the
four-bin idea. However, the canonical Klein-four ownership component only
permutes \((C_s,C_{s-1},C_{s-1},C_{s-2})\), and therefore fails for every
\(C_s>p\). The weaker total-mass floor gives the threshold
\(64/25+o(1)\) even after hypothetical coordinate fragmentation. A
non-coordinate packet/trade, balanced joint realizability, and
cross-context residual capacity are all still open.
\end{minipage}}
\tag{6.4}
\]
