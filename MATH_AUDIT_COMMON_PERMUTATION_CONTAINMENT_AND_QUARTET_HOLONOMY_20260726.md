# Audit: common-permutation containment cut versus quartet holonomy

Date: 2026-07-26

Files audited:

* `MATH_THEOREM_PROMOTION_CLONE_COMMON_PERMUTATION_TOP_HARMONIC_CONTAINMENT_CUT_20260726.md`;
* `MATH_THEOREM_PROMOTION_RING_QUARTET_HOLONOMY_EXCHANGE_20260726.md`.

## 0. Verdict

Both main theorems are valid.  One endpoint caveat in the quartet note
was corrected during this audit: Lemma 3.1 is false for singleton
windows, because the deck of all singleton labels is permutation
invariant.  Its hypothesis is now \(2\le h<M/2\).  Every application has
\(h=H+q\ge2\), so no later result changes.

The scopes are complementary.

1. The clone-containment theorem is a sharp **negative composition
   theorem**.  Separate near-perfect Hall matchings at the middle and an
   entrance rank can be conjugated so that \(W-o(W)\) paired clone
   incidences violate the literal nesting required by every common cyclic
   order.  It disproves composition of independent marginal matchings;
   it does not obstruct a jointly designed nested matching.
2. The quartet theorem is a genuine **positive exact move theorem**.
   Four actual cyclic frames admit a phasewise, all-length compound
   exchange inside the common-permutation space.  It also proves that
   local top-degree energy and permutation parity are not absolute
   obstructions.  But the move is load-neutral, and no connectivity or
   energy descent is proved.  Thus it is a real algebraic generator, not
   yet a rounding route.

The strongest positive audited statement is the phasewise identity

\[
 \sum_{i,j}(-1)^{i+j}
 \bigl(v_{ij}^{+}(s,\ell)-v_{ij}^{-}(s,\ell)\bigr)=0
\]

for every phase and every proper interval length, together with its
literal four-frame exchange.  The strongest negative audited statement
is the \(W-o(W)\) common-permutation edit-distance example for two
separately exact clone Hall matchings.

## 1. Clone containment audit

### 1.1 Physical nesting

For one top \(U\), common owner start \(a\), and lower displacement
\(q\), the omitted middle set and the entrance complement are

\[
 J_a=I(a+m,H),\qquad C_a=I(a+m,H+q).
\]

Therefore \(J_a\subseteq C_a\) literally.  Rotation and reversal change
both intervals coherently, so this is convention-independent.

### 1.2 Conditional probability

Conditioning a shore-preserving relabelling on \(gB=A\) makes \(gC\)
uniform among \((H+q)\)-sets in \(U_A\) with its prescribed shore
profile.  Hence

\[
 \Pr(J\subseteq gC\mid gB=A)
 =\frac{(c)_j}{(t)_j}
   \frac{(H+q-c)_{H-j}}{(M-t)_{H-j}}.
\]

For \(M/4\le t\le3M/4\), mechanical profile rounding gives both ratios
at most \((H+q+4)/M\), so the probability is at most

\[
 \left({H+q+4\over M}\right)^H
 =\exp(-(1/2+o(1))H\log m).
\]

The extreme-type mass is exponentially small by the stated
hypergeometric estimate.

### 1.3 Uniformity over phase alignments

The proof correctly counts all \(M\) possible entrance phases against
each middle clone before selecting the conjugating \(g\).  Therefore the
single selected \(g\) works for every rootwise phase bijection, rather
than only for a fixed alignment.  Since each marginal domain has size
\(T-o(W)\) in a common universe of size \(T\), their domains overlap in
\(T-o(W)\) clones under every alignment.  Only \(o(W)\) of all possible
phase pairs satisfy containment, proving the claimed incidence edit
distance.

This is an adversarial-pair theorem.  Conjugation deliberately produces
an incompatible pair from any two supplied marginals.  It does not say
that every pair is incompatible, and it leaves the jointly nested atom
space \((J,C)\), \(J\subset C\), completely open.

### 1.4 Harmonic formula

For the \(H\)-by-\((H+q)\) inclusion matrix, the Johnson eigenvalue on
degree \(j\) is

\[
 \binom{H+q-j}{H-j}
 \binom{M-H-j}{q}.
\]

At \(j=H\) this is \(\binom{M-2H}{q}>0\).  Transitivity of columns and
the trace identity give the displayed top-harmonic norm exactly.  Thus
the containment cut genuinely lives in growing degree \(H\); it is not
one of the already-cleared bounded-character constraints.

## 2. Quartet audit

### 2.1 Exact exchange

For a fixed positional interval, there are four cases.  If it contains
zero or two placeholders, the plus and minus sets agree.  If it contains
only \(A\), its checkerboard contribution is

\[
 \sum_{i,j}(-1)^{i+j}
 (e_{K\cup\{a_i\}}-e_{K\cup\{b_j\}})=0,
\]

and the only-\(B\) case is its negative.  This proves the identity
phase-by-phase and length-by-length.  Arbitrary common phase weights,
one common deleted phase, and common phase-to-depth schedules follow by
linear summation.

The result is stronger than an abstract column relation: both sides of
the exchange contain one literal cyclic frame on every touched top.

### 2.2 Action formula and correction

The two-position action formula was brute-checked for
\(7\le M\le21\), all \(2\le h<M/2\), and all allowed cyclic distances.
It is correct in that range and has the stated elementary proof.  For
\(h=1\), however, the deck is the complete singleton layer and its
action is zero, not \(4\).  The note now explicitly excludes this case.

For the application, complementation replaces length \(m-q\) by
\(H+q\), and a positional distance greater than \(2H\) gives exact
action \(4(H+q)\) at every \(q\le H\).  The checkerboard identity makes
the cross-top Gram terms cancel the entire diagonal action.

### 2.3 High harmonic and parity

The transposition-Laplacian average correctly yields a far positional
pair whose sub-top-degree action is \(O(H^2/m)=o(H)\).  Hence its local
degree-\(H\) action is \(4H-O(H^2/m)\), while the four-top aggregate is
zero.

The rectangle-annihilator proof over \(\mathbb F_2\) is also correct.
Every invariant is affine on the top:

\[
 w(U)=\alpha_0+\sum_{x\in U}\alpha_x,
\]

and the function space has dimension \(n\), because the \(n+1\)
generators have exactly one slice relation.  At most \(n\) exceptional
one-top sign changes repair these syndromes, at polynomial incidence
cost \(o(W)\).

### 2.4 Exact limitation

Every quartet exchange preserves every common scheduled interval load.
It therefore cannot lower a hole, collision, or overload objective that
depends only on those loads.  Its possible use is subtler: it may connect
different literal cyclic-frame realizations inside one load fibre, which
could permit a later noncommuting move or establish an integral
connectivity theorem.  Neither fact is currently proved.

## 3. Combined frontier

The clone theorem says that independently solved marginals can be
linearly far from the common-permutation space.  The quartet theorem says
that this space nevertheless has nontrivial exact cross-top motions and
that neither its first growing local harmonic nor its parity quotient is
the final obstruction.

Accordingly, neither note proves a global chronology construction.  The
quartet identity is a genuine positive ingredient, but the present net
result is still a reduction to the following gate:

> Prove that quartet and related higher exchanges connect enough of the
> jointly nested common-permutation fibre to reach a balanced integral
> point, or exhibit a nonabelian/odd-set invariant that they cannot
> change.

This is strictly narrower than the earlier unrestricted clone-Hall
problem, but it is not routine and contains the remaining integral
content.
