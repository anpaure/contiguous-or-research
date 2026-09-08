# A linear literal PBBS cut seam via the dominance staircase

Date: 2026-07-25

> **Corrected global scope.** The \(4H-1\) one-cut theorem remains valid,
> but it does not close the coefficient-one gate. Under the corrected
> residence ledger \(J=\Omega(W/H)\), paying \(\Theta(H)\) independently
> at each cut costs \(\Theta(W)\). Cross-cut baseline recycling is required.
> See MATH_ATTACK_S_PBBS_CROSS_CUT_BASELINE_FUSION_20260725.md.

Pure mathematics only.  No computation, finite search, solver, or web
search is used.

## 0. Outcome

Let

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\}
\]

be a cyclic Johnson walk of rank \(m+1\), and cut it between
\(X_{-1}\) and \(X_0\).  Assume

\[
 1\le H,
 \qquad 2H\le m+1.                                \tag{0.1}
\]

There is an explicit nonzero literal word of length at most

\[
 \boxed{4H-1}                                      \tag{0.2}
\]

which represents every floor-correct lower intersection and every upper
union of at most \(H+1\) consecutive owners crossing this cut.

The upper chart is simply the \(2H\)-owner segment

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}.                  \tag{0.3}
\]

The lower chart has \(2H-1\) entries.  It is a monotone lattice staircase
of actual owner intersections through the Pareto-minimal left/right
positive-run extents at the cut.  The decisive fact is that floor
correctness forbids an extent point strictly southwest of the requested
depth pair.  This makes one contiguous staircase subpath union exactly to
the requested intersection.

Consequently the crossing-mask seam theorem \(\mathrm{CMS}(H)\) in
`MATH_ATTACK_AD15_DIRECT_PBBS_ALLQ_EROSION_AUDIT_20260725.md` is true with
the absolute constant

\[
 \boxed{C=5}                                       \tag{0.4}
\]

throughout (0.1).  If a projected PBBS cycle of length \(\ell\) is cut at
\(J\ge1\) edges meeting every positive residence interval of length at
most \(H\), its complete literal replacement has length at most

\[
 \boxed{\ell+(5H-1)J.}                             \tag{0.5}
\]

Thus the global deterministic transfer improves from the old quadratic
ledger to

\[
 \boxed{
 L_H\le
 W+2H B_m+2(5H-1)\nu_H(P_m),
 \qquad B_m=\operatorname{Cat}_m.}                \tag{0.6}
\]

In particular, the physical residence estimate

\[
 \nu_H(P_m)=O(B_m)                                 \tag{0.7}
\]

now suffices for a \(W+o(W)\) central-band word whenever \(H=o(m)\).
The formerly required little-oh \(o(B_m)\) was an artefact of literal
singleton repair at quadratic cost.  The separate Catalan residence
packing bound (0.7) remains unproved here.

## 1. Crossing intersections as two-dimensional dominance filters

Fix the cut between the adjacent rank-\((m+1)\) owners
\(X_{-1},X_0\).  Put

\[
 C=X_{-1}\cap X_0,
 \qquad |C|=m.                                    \tag{1.1}
\]

For \(1\le s,t\le H\), define the crossing intersection

\[
 \boxed{
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.}                \tag{1.2}
\]

It uses \(s+t\) owners and \(s+t-1\) Johnson transitions.  Every lower
crossing window of projected depth at most \(H\) has this form with

\[
 s+t-1\le H.                                      \tag{1.3}
\]

We construct the chart on the full square \([H]^2\), which is stronger
than needed.

For every \(x\in C\), let \(u_x\in[H]\) be its capped consecutive left
extent and \(v_x\in[H]\) its capped consecutive right extent:

\[
\begin{aligned}
 u_x&=\max\{u\in[H]:x\in X_{-u}\cap\cdots\cap X_{-1}\},\\
 v_x&=\max\{v\in[H]:x\in X_0\cap\cdots\cap X_{v-1}\}.
\end{aligned}                                     \tag{1.4}
\]

These maxima exist because \(x\in X_{-1}\cap X_0\).  Write

\[
 p_x=(u_x,v_x),
 \qquad
 \mathcal D=\{p_x:x\in C\}\subseteq[H]^2.        \tag{1.5}
\]

Multiplicity in \(\mathcal D\) is harmless; Pareto minima below are taken
from its set of distinct points.

### Lemma 1.1 (exact dominance formula)

For every \(q=(s,t)\in[H]^2\),

\[
 \boxed{
 P_{s,t}=\{x\in C:p_x\ge q\},}                   \tag{1.6}
\]

where inequalities are coordinatewise.

#### Proof

Every \(P_{s,t}\) contains both \(X_{-1}\) and \(X_0\) in its defining
intersection, so it is a subset of \(C\).  A coordinate \(x\in C\) lies
in every owner from \(-s\) through \(t-1\) exactly when its consecutive
positive run through the cut extends at least \(s\) owners left and at
least \(t\) owners right.  This is \(u_x\ge s,v_x\ge t\). \(\square\)

Thus the lower cut problem is a two-dimensional dominance problem, but
only its floor-correct queries have to be represented.

## 2. Floor correctness forbids a strict southwest point

Every intersection of \(L\) consecutive rank-\((m+1)\) Johnson owners has
size at least \(m+1-(L-1)\).  Call \(P_{s,t}\) **floor-correct** when

\[
 \boxed{
 |P_{s,t}|=m+2-s-t.}                              \tag{2.1}
\]

This is exactly the rank required of a correct lower projected mask.

### Lemma 2.1 (southwest exclusion)

If \(P_{s,t}\) is floor-correct, then

\[
 \boxed{
 \nexists x\in C:\quad u_x<s\text{ and }v_x<t.}  \tag{2.2}
\]

#### Proof

List the \(L=s+t\) owners in (1.2) as

\[
 Y_0=X_{-s},Y_1,\ldots,Y_{L-1}=X_{t-1}.
\]

For every coordinate of \(Y_0\) which is absent from the full
intersection, assign its first departure transition.  This is an injection
into the \(L-1\) internal transitions, because each Johnson transition
departs exactly one coordinate.

Suppose that \(x\in C\) has \(u_x<s,v_x<t\).  The first inequality says
that before reaching its positive run through the cut, \(x\) is absent at
some owner of the left part; hence there is an internal arrival of \(x\).
The second says that this arrival is followed by an internal departure of
\(x\) in the right part.

That later departure transition cannot be the first-departure image of a
new initial coordinate.  If \(x\notin Y_0\), it is not an initial
coordinate at all.  If \(x\in Y_0\), then it already departed before the
internal arrival, so the later departure is not its first.  This argument
also covers multiple positive runs of \(x\) inside the window.

Therefore at most \(L-2\) transitions are used by the first-departure
injection.  Hence

\[
 |P_{s,t}|\ge(m+1)-(L-2)=m+3-s-t,
\]

contradicting (2.1). \(\square\)

The strictness in (2.2) is essential.  Points directly west, south, or
northeast of \((s,t)\) are allowed.

## 3. The dominance staircase

Use the product order on \([H]^2\).  Let

\[
 d_1=(a_1,b_1),\ldots,d_r=(a_r,b_r)               \tag{3.1}
\]

be the distinct Pareto-minimal points of \(\mathcal D\), ordered by
increasing first coordinate.  Their second coordinates are then strictly
decreasing.  Augment this ordered list by
\[
 d_0=(1,H),\qquad d_{r+1}=(H,1),
\]
delete repetitions, and construct a unit lattice path \(\Gamma\) by
moving, between every successive pair in the augmented list, first east
and then south.

The path makes \(H-1\) east steps and \(H-1\) south steps.  Therefore its
number of vertices is exactly

\[
 \boxed{|\Gamma|=2H-1.}                            \tag{3.2}
\]

### Lemma 3.1 (staircase rectangle interception)

Let \(q\in[H]^2\) satisfy

\[
 \nexists d\in\mathcal D:\ d_1<q_1, d_2<q_2.    \tag{3.3}
\]

If \(p\in\mathcal D\) and \(p\ge q\), then

\[
 \boxed{
 \Gamma\cap[q,p]\ne\varnothing,}                \tag{3.4}
\]

where \([q,p]=\{z:q\le z\le p\}\).

#### Proof

Choose a Pareto-minimal \(d\in\mathcal D\) with \(d\le p\).  Such a point
exists by descending inside the finite nonempty set
\(\mathcal D\cap(-\infty,p]\).  The path \(\Gamma\) passes through \(d\).

If \(d\ge q\), take \(z=d\).  The excluded alternative
\(d_1<q_1,d_2<q_2\) leaves two one-sided cases.

Suppose first that \(d_1<q_1\) and \(d_2\ge q_2\).  Follow \(\Gamma\)
forward from \(d\).  Until its first coordinate reaches \(q_1\), every
Pareto minimum encountered still has second coordinate at least \(q_2\),
by (3.3).  Because each inter-minimum segment moves east before moving
south, the path therefore contains a point

\[
 z=(q_1,z_2),\qquad z_2\ge q_2.
\]

All second coordinates encountered forward from \(d\) are at most
\(d_2\le p_2\), and \(q_1\le p_1\).  Thus \(q\le z\le p\).

Suppose instead that \(d_1\ge q_1\) and \(d_2<q_2\).  Follow \(\Gamma\)
backward.  Until the second coordinate reaches \(q_2\), every Pareto
minimum encountered has first coordinate at least \(q_1\), again by
(3.3).  The vertical part of the first segment crossing height \(q_2\)
therefore contains

\[
 z=(z_1,q_2),\qquad z_1\ge q_1.
\]

Backward first coordinates are at most \(d_1\le p_1\), and
\(q_2\le p_2\).  Thus \(q\le z\le p\) here as well. \(\square\)

The east-before-south convention is used only in the two one-sided cases.

## 4. The linear lower crossing chart

For every staircase vertex \(z=(s,t)\in\Gamma\), form the actual
intersection letter

\[
 P_z=P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.             \tag{4.1}
\]

Emit these letters in their order along \(\Gamma\).

### Theorem 4.1 (all correct lower crossings in \(2H-1\) letters)

Every floor-correct \(P_q\), \(q=(s,t)\in[H]^2\), is represented by the
contiguous staircase interval

\[
 \boxed{
 P_q=\bigcup_{\substack{z\in\Gamma\\z\ge q}}P_z.} \tag{4.2}
\]

All \(2H-1\) emitted letters are nonempty under (0.1).

#### Proof

Along \(\Gamma\), first coordinates are nondecreasing and second
coordinates are nonincreasing.  Hence the vertices satisfying \(z\ge q\)
form one contiguous subpath: \(z_1\ge q_1\) is a suffix condition, while
\(z_2\ge q_2\) is a prefix condition.

If \(z\ge q\), the dominance formula (1.6) gives \(P_z\subseteq P_q\).
Conversely, let \(x\in P_q\).  Then \(p_x\ge q\).  Lemma 2.1 supplies
(3.3), and Lemma 3.1 gives a vertex

\[
 z\in\Gamma\cap[q,p_x].
\]

Since \(p_x\ge z\), equation (1.6) gives \(x\in P_z\).  This proves
(4.2).

Finally, a letter \(P_{s,t}\) intersects \(s+t\le2H\) consecutive
rank-\((m+1)\) owners.  Every transition can remove at most one coordinate
from the running intersection, so

\[
 |P_{s,t}|\ge(m+1)-(s+t-1)
              \ge m+2-2H\ge1.                   \tag{4.3}
\]

Thus every emitted letter is nonzero. \(\square\)

This theorem is deterministic and uses no PBBS-specific ordering of the
short runs.

## 5. Pascal interpretation and the exact short-run break

The staircase theorem is the integral form of the hinted Pascal identity.
For \(1\le s,t<H\), the two one-step extensions of \(P_{s,t}\) are

\[
 P_{s+1,t}=P_{s,t}\cap X_{-s-1},
 \qquad
 P_{s,t+1}=P_{s,t}\cap X_t.                       \tag{5.1}
\]

Put

\[
 R_{s,t}=
 P_{s,t}\setminus(P_{s+1,t}\cup P_{s,t+1}).      \tag{5.2}
\]

A coordinate lies in \(R_{s,t}\) exactly when its positive run through the
cut has capped extent pair \((s,t)\); equivalently, it is present
throughout \(X_{-s},\ldots,X_{t-1}\) and absent in both adjacent owners.
Therefore

\[
 \boxed{
 P_{s,t}=P_{s+1,t}\cup R_{s,t}\cup P_{s,t+1}.}   \tag{5.3}
\]

Thus \(R_{s,t}=\varnothing\) if and only if the two extension children
union to their parent.  Each child equals its parent or deletes one
coordinate.  If the pin is empty and both children are proper, they are
distinct facets; without the empty-pin hypothesis they can coincide.  A
short positive run is exactly a nonempty Pascal pin \(R_{s,t}\).  Literal
insertion of every broken parent separately pays the old triangular
\(H^2\) toll.  The dominance staircase shares all such pins at once.
Floor correctness, through Lemma 2.1, is precisely the condition which
makes the sharing safe.

In the equivalent deepest-erosion-row picture, a short run becomes a chord
which must be included exactly when the requested leaf interval contains
that chord.  An arbitrary chord family is genuinely two-dimensional.  The
new point is that floor-correct requests cannot strictly straddle a chord
at both ends; their safe dominance region is intercepted by the one
staircase \(\Gamma\).

## 6. Upper crossings and the exact per-cut cost

Emit, as a second local block, the \(2H\) owners

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}.                  \tag{6.1}
\]

Every upper crossing union of at most \(H+1\) owners is the union of its
literal contiguous owner subsegment in (6.1).  All owner letters are
nonzero.

Concatenate the lower staircase block and the upper owner block.  Target
witnesses stay wholly inside the relevant block, so concatenation creates
no constraint.  The total repair length is

\[
 (2H-1)+2H=4H-1,                                  \tag{6.2}
\]

proving (0.2).

## 7. Global PBBS cut repair

Let \(C\) be an active complement-projected PBBS cycle of length \(\ell\),
and let \(D_C\) be any nonempty set of \(J\) transition edges meeting every
positive coordinate residence interval of length at most \(H\).  Cutting
at \(D_C\) gives \(J\) linear owner paths with no internally bounded
positive run of length at most \(H\).

The endpoint-capped erosion word of Lemma 7.1 in
`MATH_ATTACK_AD15_DIRECT_PBBS_ALLQ_EROSION_AUDIT_20260725.md` costs

\[
 \ell+HJ                                                   \tag{7.1}
\]

and covers every correct window lying wholly inside a path.  Append the
\((4H-1)\)-letter chart of Sections 4 and 6 at every cut.  Every original
upper window, and every floor-correct lower intended window, of depth at
most \(H\) which was destroyed by cutting crosses at least one selected
cut and is represented inside that cut's chart.  This remains true when
one window crosses several nearby cuts; the chart uses the original cyclic
owners, not independently chosen endpoint dummies.

Hence the complete active-cycle word has length

\[
 \boxed{
 \ell+HJ+(4H-1)J=\ell+(5H-1)J,}                  \tag{7.2}
\]

which proves \(\mathrm{CMS}(H)\) with \(C=5\).

Every projected PBBS cycle has length at least \(2m+1\), so (0.1) ensures
that all local owner indices used by a chart lie in one unambiguous cyclic
neighbourhood.  The construction remains integral inside the original
factor and every displayed target is a literal contiguous OR in the new
word.

## 8. Global ledger and coefficient-one implication

Inactive cycles retain their cyclic erosion words, at overhead \(2H\) per
cycle.  Let \(c_2(P_m)\) be the number of projected step-two cycles.  On
each active cycle choose a minimum residence-interval transversal.  The
circular interval packing--transversal theorem gives

\[
 J_C=\tau_H(C)\le\nu_H(C)+1\le2\nu_H(C),          \tag{8.1}
\]

because an active cycle has \(\nu_H(C)\ge1\).  Summing (7.2) therefore
gives

\[
\begin{aligned}
 L_H
 &\le W+2Hc_2(P_m)+(5H-1)\sum_{C\text{ active}}J_C\\
 &\le W+2Hc_2(P_m)+2(5H-1)\nu_H(P_m)\\
 &\le \boxed{W+2HB_m+2(5H-1)\nu_H(P_m)},          \tag{8.2}
\end{aligned}
\]

using \(c_2(P_m)\le B_m\).  This is (0.6).

If \(\nu_H(P_m)\le K B_m\) for a fixed \(K\), then

\[
 \frac{L_H-W}{W}
 \le
 \frac{2H+2K(5H-1)}{2m+1}
 =O_K(H/m).                                       \tag{8.3}
\]

Thus every \(H=o(m)\) gives a \(W+o(W)\) central-band word.  Combining
this with the already proved outer-tail estimate under

\[
 \frac{m}{H}\exp\!\left(-\frac{H^2}{m+H}\right)\to0 \tag{8.4}
\]

gives the coefficient-one theorem conditionally on the Catalan physical
residence packing bound (0.7).  Equivalently, after the deck reduction and
negligible short quotient cycles, it is enough to prove

\[
 \overline\nu_H=O(B_m/(2m+1)).                    \tag{8.5}
\]

The deterministic cut-repair gate itself is closed.

There is also a fixed-window formulation which exactly replaces the old
little-oh hypothesis \((\mathrm{RP}_A)\).

### Corollary 8.1 (fixed-window big-O now suffices)

Assume that for every fixed \(A>0\) there is a constant \(K_A\) such that

\[
 \boxed{
 \nu_{\lceil A\sqrt m\rceil}(P_m)
 \le K_A B_m}                                     \tag{8.6}
\]

for all sufficiently large \(m\).  Then

\[
 \boxed{
 \nu(k)\le(1+o(1))
 \binom{k}{\lfloor k/2\rfloor}.}                 \tag{8.7}
\]

#### Proof

For fixed \(A\), put \(H=\lceil A\sqrt m\rceil\).  Equation (8.3), with
\(K=K_A\), makes the central-band excess \(o_A(W)\).  The proved
product-SCD outer tail has normalized cost

\[
 O\!\left((1+A^2)e^{-A^2+o(1)}\right).
\]

First let \(m\to\infty\) for fixed \(A\), and then let \(A\to\infty\).
Equivalently, choose an integer diagonal \(A=A(m)\to\infty\) slowly enough
that \(K_{A(m)}A(m)/\sqrt m\to0\).  The standard trimmed-coordinate lift
handles the opposite parity.  This proves (8.7). \(\square\)

By the deck theorem, after its negligible short-cycle term, (8.6) is
equivalent to the fixed-window quotient estimate

\[
 \boxed{
 \overline\nu_{\lceil A\sqrt m\rceil}
 =O_A(B_m/(2m+1)).}                               \tag{8.8}
\]

Thus the deterministic seam theorem changes the residence target from a
little-oh to the sharp constant-order Catalan packing bound.

## 9. Scope and audit boundary

What is proved:

* a \(2H-1\)-letter lower chart for every floor-correct crossing
  intersection at one arbitrary Johnson cut;
* a \(4H-1\) total literal crossing chart including upper unions;
* \(\mathrm{CMS}(H)\) with \(C=5\) for \(2H\le m+1\);
* compatibility with arbitrarily close cuts; and
* the exact global ledger (8.2).

No histogram cancellation, fractional factor mixing, common-owner
synchronization, or unlabelled-to-labelled implication is used.  The
helpers \(P_z\) are actual nonempty sets and every target is reconstructed
by one literal contiguous union.

What is not proved is the residence estimate (0.7).  The earlier scalar
peak-deletion induction does not establish it.  This report removes the
quadratic literal-repair loss; it does not claim coefficient one without
the separate Catalan packing input.
