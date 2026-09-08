# Audit of common-cap Cartesian Hall and a valid all-dimensional existence criterion

Date: 2026-07-31  
Scope: audit of
`MATH_THEOREM_R_MAXIMAL_COMMON_CAP_INTERVAL_CEGAR_AND_CARTESIAN_HALL_20260731.md`
and
`MATH_THEOREM_R_K16_COMMON_Q_INTERVAL_CONFLICT_CLUTTER_AND_CARTESIAN_HALL_20260731.md`.

## 1. Verdict on the exact finite mathematics

The following statements in the two source notes are correct.

1. For a fixed target-to-cell matching (M), the maximal common cap

   \[
   K_p(M)=E_p\cap\bigcap_{(S,C)\in M:p\in C}S
   \]

   is the unique maximal possible physical word.  The matching is realizable
   if and only if this word is nonempty, preserves every prescribed middle
   row, and realizes every selected lower cell.
2. The coordinatewise cover formulation through the blocker unions (Z_b)
   is equivalent to the maximal-cap criterion.
3. The three exact obstruction types—empty position, lost middle bit, and
   lost selected-lower bit—form a complete conflict clutter.
4. For row width at most (D) and lower-cell length at most (d), minimal
   conflicts have the stated bounded ranks and spans.  In particular, for
   (D=d+1), rank is at most

   \[
   \max\{d(d+1)/2,d+1\}
   \]

   and physical span is at most (3d-1).
5. Integral matching plus all conflict-clutter inequalities is an exact
   integer formulation, and the bounded-rank CEGAR separation procedure is
   finite, sound, and complete.
6. The binary trace lift is exact: existential guard positions replace every
   high-arity conflict by trace-versus-selected-edge incompatibilities.
7. The Cartesian-*guarded* Hall theorem in the first note is a valid
   deterministic sufficient criterion.

None of these conclusions uses randomness, total unimodularity, PBBS, or a
Pascal recursion.

## 2. Two corrections of interpretation

### 2.1 Strong Cartesian Hall is an exact restatement, not an existence theorem

The second note calls a whole edge subgraph (H) Cartesian when the single
maximal word (K(H)) realizes every edge of (H) simultaneously.  The
result

> a compiler exists iff a Cartesian (H) contains a lower-perfect matching

is correct, but it is nearly tautological: from a solution take (H=M).
Moreover, if (H) is Cartesian and contains two edges ((S,C)) and
((T,C)) on the same physical cell, then

\[
\bigcup_{p\in C}K_p(H)=S=T.
\]

Thus one cell cannot support two distinct target labels in a Cartesian
subgraph.  Once every target has at least one edge in (H), distinct-cell
selection is automatic; the global Hall inequalities add no further work.

This does not invalidate the theorem.  It means that the strong definition
has already hidden the simultaneous compiler inside the premise.  The useful
positive object is instead the first note's **Cartesian-guarded** graph:
guards are checked only against co-selectable edges, so the graph need not be
simultaneously realizable in its entirety, yet *every matching it contains*
is realizable.

The sentence identifying universal trace guards with a strong Cartesian
subgraph needs this distinction.  They are equivalent only if guards protect
against every edge of (H), including pairs which no matching can select
together.  With the co-selectable-pair test, they certify the weaker and more
useful guarded property.

### 2.2 The c7be open-gate statements are superseded

The exact (k=16) construction now uses the same endpoint-rerooted target
order `c7beccc3...`, the pinned singleton `0x8000`, and schedule

\[
X=\{12870,12871,12872\},\qquad Y=\{0,1,6388\}.
\]

It supplies a simultaneous common-cap matching and a literal word of length
12,873.  Therefore statements that no compatible matching, integral clutter
solution, or common cap has been exhibited for this frozen fibre are stale.
The abstract counterexamples and all general theorems remain valid.

The positive certificate is
`MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`.

## 3. A deterministic all-dimensional sufficient theorem

The guarded theorem becomes a genuine existence result once Hall is supplied
by an explicit fractional flow rather than assumed as another black box.

### Theorem 3.1 (guarded fractional-Hall compiler)

Use the general interval compiler system of the source notes.  Suppose a
candidate subgraph (G') is Cartesian guarded in the sense of the first
note.  Suppose there are nonnegative weights (x_e) such that

\[
\sum_{e\in G'(S)}x_e=1\quad(S\in\mathcal L),\qquad
\sum_{e\in G'(C)}x_e\le1\quad(C\in\mathcal C).          \tag{3.1}
\]

Then one nonempty literal source simultaneously preserves every prescribed
middle row and realizes every lower target.

If, in addition, every required upper target is the union of a consecutive
block of middle rows whose physical row intervals have interval union, then
the same source realizes all required lower, middle, and upper targets.

#### Proof

For any target set \(\mathcal A\subseteq\mathcal L\), (3.1) gives

\[
|\mathcal A|
=\sum_{S\in\mathcal A}\sum_{e\in G'(S)}x_e
\le\sum_{C\in N(\mathcal A)}\sum_{e\in G'(C)}x_e
\le|N(\mathcal A)|.
\]

Thus Hall holds.  The Cartesian-guarded Hall theorem supplies a realizable
matching and its maximal common-cap word.  The upper-target conclusion is
the consecutive-block argument from the second source note.  \(\square\)

### Corollary 3.2 (guarded normalized-load test)

It is enough that every target has positive guarded degree and

\[
\sum_{(S,C)\in G'}\frac1{\deg_{G'}(S)}\le1
\quad\text{for every fixed cell }C.                    \tag{3.2}
\]

Indeed take (x_{S,C}=1/\deg_{G'}(S)).  A cruder sufficient condition is

\[
\min_S\deg_{G'}(S)\ge\max_C\deg_{G'}(C).              \tag{3.3}
\]

The content needed from an all-(k) construction is now explicit: install
the guards while retaining the normalized load bound.  This is stronger
than merely retaining many candidates on average and weaker than explicitly
constructing an integral compiler.

## 4. A rigorous probabilistic sufficient theorem

Bounded conflict rank and span do not by themselves imply existence.  They
do, however, make the exact bad-event family finite and bounded-arity.  The
following theorem states precisely the extra local-pressure inequality an
LLL proof would have to verify.

For each lower target (S), let

\[
V_S=\{(S,C)\in G\}
\]

be its nonempty candidate part.  Independently choose one \(X_S\in V_S\)
with distribution \(\pi_S\).  Use two kinds of atomic bad events.

1. For distinct targets, selecting two candidates with the same cell.
2. Selecting every edge of one member of the exact conflict clutter.

After exact unary propagation, all remaining bad events have at least two
vertices and use at most one candidate from each target part.

For a bad event (B), let

\[
p_B=\prod_{e\in B}\pi(e).
\]

For a candidate \(e\in V_S\), let \(\mathcal A(e)\) be the bad events which
prescribe some *different* candidate in \(V_S\setminus\{e\}\).

### Theorem 4.1 (atomic lopsided common-cap criterion)

Suppose numbers (c_e\ge1) and (0\le y_B<1) satisfy

\[
p_B\le\frac{y_B}{\prod_{e\in B}c_e}                  \tag{4.1}
\]

for every bad event, and

\[
\prod_{B\in\mathcal A(e)}(1-y_B)\ge c_e^{-1}         \tag{4.2}
\]

for every positive-probability candidate (e).  Then a simultaneous
common-cap matching exists.

With the same upper consecutive-block hypothesis as Theorem 3.1, its maximal
common cap is a full literal compiler word.

#### Proof

Atomic events are joined in the lopsided dependency graph only when they
prescribe different values of a common target variable.  Events which agree
where their target variables overlap are legitimate lopsided nonneighbors:
after outside variables are fixed, avoiding all such compatible events is a
coordinatewise nonincreasing function of the indicators of the assignments
prescribed by the conditioned event.  This is the standard atomic
negative-dependency argument.

Every lopsided neighbor of (B) belongs to (mathcal A(e)) for at least one
(e\in B).  Repeating factors in ((0,1]) only decreases their product, so

\[
\prod_{B'\sim B}(1-y_{B'})
\ge\prod_{e\in B}\prod_{B'\in\mathcal A(e)}(1-y_{B'})
\ge\prod_{e\in B}c_e^{-1}.
\]

Equations (4.1)--(4.2) are therefore the asymmetric lopsided-LLL
inequalities.  An outcome avoiding all bad events chooses one candidate per
target, has no repeated cell, and contains no member of the exact conflict
clutter.  The conflict-clutter theorem then gives a common cap.  \(\square\)

### Corollary 4.2 (uniform list/profile criterion)

Suppose every residual target has at least (M) candidates, choose uniformly,
and let (widetilde D_j(e)) count size-(j) bad events which prescribe an
alternative candidate in the target part of (e).  If some (1<c<M)
satisfies

\[
\prod_{j\ge2}\left(1-(c/M)^j\right)^{\widetilde D_j(e)}
\ge\frac1c\qquad\text{for every candidate }e,          \tag{4.3}
\]

then a simultaneous common-cap matching exists.  The additive sufficient
condition is

\[
\sum_{j\ge2}\widetilde D_j(e)
\frac{(c/M)^j}{1-(c/M)^j}\le\log c.                   \tag{4.4}
\]

This is the valid route from bounded local conflict clutter to an existence
theorem.  It still requires a quantitative alternative-choice profile.

## 5. What the exact K16 result does and does not generalize

For (k=16), the final common-cap model supplies the integral selector
directly.  Consequently it also supplies, after the fact:

- a strong Cartesian subgraph (H=M);
- compatible trace guards;
- a feasible fractional flow (the incidence vector of (M)); and
- zero probability for every bad event under the Dirac distribution on the
  selected candidates.

These are consistency checks, not independent existence proofs.  In
particular, the fact that Kissat found the model at zero conflicts does not
show that the same CNF is forced, propagation-complete, or satisfiable in
other dimensions.

To prove the exact formula in every dimension by this route, it is sufficient
to construct, for each (k), an upper-complete middle chronology and a
depth-(d(k)) candidate system satisfying either:

1. the guarded normalized-load condition (3.2); or
2. the atomic lopsided pressure condition (4.1)--(4.2), equivalently a
   checkable specialization such as (4.3)--(4.4).

Together with the monotone-deadline lower bound, either construction proves

\[
\nu(k)=\binom{k}{\lceil k/2\rceil}+d(k).
\]

No known PBBS or Pascal family has yet been proved to satisfy either
condition uniformly in (k).

## 6. Explicit warnings

1. **Bounded rank is not bounded dependency.**  Although each conflict uses
   (O(d^2)) selected candidates and lies in an (O(d))-position window, one
   target variable can have candidates in many distant windows.  The atomic
   event dependency or lopsided alternative-choice pressure can therefore
   grow with the whole chronology.
2. **Interval locality is not an LLL proof.**  One must specify the random
   variables, include same-cell collision events, and verify (4.1)--(4.2) or
   another valid local-lemma criterion.  A calculation using only conflict
   span omits dependencies through common target choices.
3. **Marginal Hall is insufficient.**  The exact rank-two c7be conflict and
   the nested-singleton example in the source note disprove this.
4. **Laminarity is insufficient.**  Nested cells can erase a common physical
   coordinate, and the augmented conflict LP can have the determinant-two
   half-integral vertex displayed in the source note.
5. **Strong Cartesianity cannot be assumed from pairwise cell geometry.**
   It is already simultaneous realizability of the retained edge family.
6. **An LLL selector need not be a matching unless collision events are part
   of the bad-event family.**
7. **Neither theorem is currently an unconditional all-(k) construction.**
   Their value is an exact deterministic/probabilistic target for the missing
   design theorem.
