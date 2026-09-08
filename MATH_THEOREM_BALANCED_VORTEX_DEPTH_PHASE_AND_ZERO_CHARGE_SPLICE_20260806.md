# Balanced-vortex depth phase and the exact zero-charge splice gate

## Status

This note resolves the scalar part of length-neutral balanced-vortex
recursion and isolates its sharp literal boundary condition.

Write

\[
 W_s=\binom{2s-1}{s},\qquad H_s=4^{s-1}-1,
 \qquad T_t=\binom{t+1}{2},
\]

and

\[
 D_s=\min\{t\geq0:tW_s+T_t\geq H_s\}.
 \tag{0.1}
\]

Thus $D_s=d(2s-1)$.  At the critical balanced-vortex step put

\[
 a=\left\lfloor {\log _2s\over4}\right\rfloor,
 \qquad q=s-a.
 \tag{0.2}
\]

For all sufficiently large $s$,

\[
 \boxed{D_s-D_q\in\{0,1\}.}
 \tag{0.3}
\]

There is an exact test for which value occurs.  A zero cost at a single
step is therefore arithmetically possible, but it is not automatic: when
the difference is one, the child must be supplied in the lower (root)
phase.  An ordinary owner-phase child has a rank obstruction.

The second theorem below gives a necessary-and-sufficient boundary-tensor
criterion for joining two cyclic source components without adding a
letter.  Equality of one complete oriented port state is a useful sharp
context-free sufficient condition.

These results do **not** construct the required two-phase decorated child.
They show exactly what a recursive construction must export and why paying
one position at each depth jump would accumulate rather than give an
additive constant.

## 1. Exact ambient versus intrinsic depth

### Theorem 1.1 (critical-step depth dichotomy)

Let $q$ be given by (0.2).  For all sufficiently large $s$,

\[
 0\leq D_s-D_q\leq1.
 \tag{1.1}
\]

Moreover, once (1.1) holds, the value is determined exactly by

\[
 D_s-D_q=
 \begin{cases}
 0,&D_qW_s+T_{D_q}\geq H_s,\\
 1,&D_qW_s+T_{D_q}<H_s.
 \end{cases}
 \tag{1.2}
\]

#### Proof

First, (D_s) is nondecreasing in (s).  Indeed,

\[
 W_{s+1}=c_sW_s,\qquad
 c_s={2(2s+1)\over s+1}<4,qquad
 H_{s+1}=4H_s+3.
\]

For fixed (t), put

\[
 g_s(t)={H_s-T_t\over W_s}.
\]

A direct subtraction gives

\[
 g_{s+1}(t)-g_s(t)
 ={(4-c_s)H_s+3+(c_s-1)T_t\over c_sW_s}>0.
 \tag{1.3}
\]

Since (t) is feasible in (0.1) exactly when (t\geq g_s(t)), every
integer feasible at (s+1) is feasible at (s).  Hence
(D_{s+1}\geq D_s), and in particular (D_s\geq D_q).

Now put (x_s=H_s/W_s).  Stirling's formula gives

\[
 x_s={\sqrt{\pi s}\over2}+O(s^{-1/2}).
 \tag{1.4}
\]

Also (D_s\leq\lceil x_s\rceil).  Consequently

\[
 {T_{D_s}\over W_s}
 \leq {T_{\lceil x_s\rceil}\over W_s}=o(1),
\]

and the defining inequality gives

\[
 x_s-o(1)\leq D_s<x_s+1.
 \tag{1.5}
\]

Uniformly for (q=s-O(\log s)),

\[
 x_s-x_q
 ={\sqrt\pi\over2}(\sqrt s-\sqrt q)+O(q^{-1/2})
 =O\left({\log s\over\sqrt s}\right)=o(1).
 \tag{1.6}
\]

Equations (1.5)--(1.6) imply (D_s-D_q<2) for all sufficiently large
(s).  The difference is a nonnegative integer, proving (1.1).

Finally, (D_s=D_q) precisely when the integer (D_q) is feasible in
(0.1) at (s).  If it is not feasible, (1.1) forces (D_s=D_q+1).
This is exactly (1.2).  \(\square\)

### Corollary 1.2 (unit charges accumulate)

Let

\[
 s_{i+1}=s_i-\left\lfloor{\log_2s_i\over4}\right\rfloor
\]

until a fixed terminal value (s_m=s_*) is reached.  Then

\[
 \sum_{i=0}^{m-1}(D_{s_i}-D_{s_{i+1}})
 =D_{s_0}-D_{s_*}=\Theta(\sqrt{s_0}).
 \tag{1.7}
\]

Thus a recursion which spends one physical position whenever the intrinsic
deadline drops cannot prove (B(k)+O(1)).

#### Proof

The sum telescopes.  Equation (1.4), together with (1.5), gives
(D_s=\frac12\sqrt{\pi s}+O(1)).  \(\square\)

## 2. The phase required at a one-level drop

For a cyclic word (C=(C_i)_{i\in\mathbb Z/N\mathbb Z}), define its
union derivative by

\[
 (\mathsf UC)_i=C_i\cup C_{i+1}.
\]

Associativity and idempotence of union give

\[
 (\mathsf U^hC)_i=\bigcup_{j=0}^h C_{i+j}.
 \tag{2.1}
\]

Let $A$ be a fixed set, disjoint from the moving ground set $R$, and put
$\widehat C_i=A\cup C_i$.

### Theorem 2.1 (zero-length phase-lift criterion)

Let $e=D_q$, $D=D_s$, and $\epsilon=D-e\in\{0,1\}$.  Put

\[
 Z=\mathsf U^eC.
\]

The word \(\widehat C\), with exactly the same number of cyclic source
positions as $C$, has ambient owner row equal to a prescribed ordering
$(A\cup X_i)$ of the balanced owner slice if and only if

\[
 \boxed{\mathsf U^\epsilon Z=(X_i).}
 \tag{2.2}
\]

In particular:

1. if $\epsilon=0$, $Z$ must be the owner-phase ordering itself;
2. if \(\epsilon=1\), an ordinary simple owner-phase ordering cannot
   work: two distinct rank-(q) sets have union of rank at least (q+1);
3. in the flat one-copy root phase, (2.2) is equivalent to a cyclic
   ordering (Q_i\) of all rank-((q-1)) roots such that

   \[
   Q_i\cup Q_{i+1}=X_i
   \tag{2.3}
   \]

   enumerates every rank-(q) owner once.  Equivalently, the alternating
   sequence

   \[
   Q_0,X_0,Q_1,X_1,\ldots
   \]

   is a Hamilton cycle in the middle-levels graph.

#### Proof

Because (A) occurs in every source letter,

\[
 \mathsf U^D\widehat C
 =A\cup\mathsf U^{e+\epsilon}C
 =A\cup\mathsf U^\epsilon Z.
\]

This proves the equivalence (2.2) and Item 1.  For Item 2, if consecutive
rank-(q) terms of (Z) are distinct, their union has rank at least
(q+1); if they are equal throughout, they cannot enumerate the owner
slice.  For Item 3, consecutive distinct rank-((q-1)) sets have a
rank-(q) union exactly when they differ by one element.  Since both the
root and owner shores have cardinality (W_q), the two one-copy
conditions are precisely the alternating Hamilton-cycle condition.
\(\square\)

The Middle Levels Theorem supplies the central root/owner phase in Item 3.
It does **not** supply an (e)-fold literal antecedent (C), the lower
chain tickets, upper witnesses, residence, or compiler data.  Those are
the genuine decorated two-phase gate.

### Proposition 2.2 (complementary root phase)

Let $O_0,\ldots,O_{W_q-1}$ be a cyclic permutation of all rank-$q$
sets in $R$, and suppose

\[
                         P_i=O_i\cap O_{i+1}             \tag{2.4}
\]

is a permutation of all rank-$(q-1)$ sets.  Put

\[
                         Q_i=R-O_i.
\]

Then $Q_i$ is a permutation of all roots and

\[
 Q_i\cup Q_{i+1}=R-P_i                                \tag{2.5}
\]

is a permutation of all owners.  Thus every doubly-rainbow owner cycle
already contains the required root phase, by complementation.

Moreover, if every coordinate of $O$ has both its positive runs and its
zero runs of length at least $e+1$, then both $O$ and $Q$ satisfy the
coordinatewise depth-$e$ antecedent criterion.  Hence the scalar phase
choice in Theorem 2.1 costs no positions at the Boolean-factorization
level.

#### Proof

Complementation bijects the rank-(q) and rank-((q-1)) shores of a
((2q-1))-set, and De Morgan's law gives (2.5).  A coordinate is present
in $Q_i$ exactly when it is absent from $O_i$, so the positive runs of
$Q$ are the zero runs of $O$.  The standard cyclic sliding-OR inverse
criterion says that a binary target trace has a depth-$e$ antecedent
exactly when every nonconstant positive run has length at least $e+1$
(with the constant trace handled separately).  Apply it to $O$ and to
$Q$.  \(\square\)

This proposition does not assert that the coordinatewise antecedent can be
chosen with every source letter nonempty, nor that the two phases have a
common compiler.  Those are literal pin/common-cap conditions rather than
deadline conditions.

### Corollary 2.3 (bounded rethreading cannot repair the wrong phase)

Suppose $\epsilon=1$ and $\mathsf U^eC$ is a simple cyclic permutation
of the rank-$q$ owners.  Alter the cyclic order by cutting and rejoining
$h$ source arcs, without changing the source letters.  If the resulting
depth-$(e+1)$ row has rank $q$ everywhere, then

\[
                         h(e+1)\geq W_q.                \tag{2.6}
\]

In particular, no bounded number of state splices repairs an owner-phase
child at a one-level deadline drop.

#### Proof

Before rethreading, every depth-$(e+1)$ cell is the union of two
consecutive, distinct rank-$q$ terms of $\mathsf U^eC$, and hence has
rank at least $q+1$.  A changed source arc can affect only the
$e+1$ windows of length $e+2$ which cross that arc.  Thus at most
$h(e+1)$ of the $W_q$ bad cells can change.  All of them must change
in a rank-$q$ final row, proving (2.6).  \(\square\)

## 3. Exact zero-charge two-cut splicing

Cut a cyclic source word (C) immediately before (C_0).  For
(i,j\geq0), define the left and right cumulative boundary unions

\[
 L_i(C)=\bigcup_{h=1}^iC_{-h},\qquad
 R_j(C)=\bigcup_{h=0}^{j-1}C_h,
 \tag{3.1}
\]

with (L_0=R_0=\varnothing).  A crossing interval using (i) letters
from the left and (j) from the right has value

\[
                         L_i(C)\cup R_j(C).             \tag{3.2}
\]

Fix a maximum relevant width $G$.  Let $C,E$ be two cyclic components,
each opened at a cut and each of length at least $G$.  Cross-splice
them by replacing the two old successor arcs by the two crossed successor
arcs.  No source position is inserted or deleted.

### Theorem 3.1 (sharp boundary-tensor criterion)

The cross-splice preserves the complete occurrence-labelled boundary OR
deck through width $G$ if and only if, for every $i,j\geq1$ with
$i+j\leq G$, the two new cells can be
matched to the two old cells with the same values and the same carried
tickets.  After forgetting ticket names, the exact value condition is

\[
 \boxed{
 \begin{aligned}
 &\{\!\{L_i(C)\cup R_j(C),\ L_i(E)\cup R_j(E)\}\!\}\\
 &\qquad=
 \{\!\{L_i(C)\cup R_j(E),\ L_i(E)\cup R_j(C)\}\!\}.
 \end{aligned}}
 \tag{3.3}
\]

For preservation of the depth-(D) derivative and all shorter compiler
cells, take (G=D+1).  A full arbitrary-width upper deck requires either
the same test through the largest protected crossing-witness width, or a
choice of upper witnesses disjoint from the two cuts.  In addition, the
splice is residence-safe if and only if every positive (and, when in
scope, negative) run assembled across either new seam passes the required
length threshold.  This is decided exactly by the two capped head/tail age
states at the cuts, including the constant-coordinate flags.

Therefore (3.3), the occurrence-ticket matching, and the capped-age test
are together necessary and sufficient for a literal zero-charge splice.

#### Proof

Every interval not crossing an altered successor arc is literally
unchanged.  For fixed (i,j), the two old crossing values are the left
side of (3.3), while the two new crossing values are the right side.
Hence (3.3), refined by the occurrence-ticket labels, is necessary and
sufficient for all affected OR cells.

Likewise, every run not crossing a changed arc is unchanged.  A changed
run is obtained by concatenating one trailing boundary run with one leading
boundary run.  Its legality is therefore determined exactly by the capped
head/tail ages and the constant-coordinate flag.  No other cell or run can
change.  \(\square\)

### Corollary 3.2 (state-equality splice)

If the two cuts have identical oriented right states through width (G),
namely

\[
 R_j(C)=R_j(E)\qquad(1\leq j\leq G),                  \tag{3.4}
\]

with identical right-side ticket and capped-age data, then the cross-splice
is zero-charge.  The analogous statement holds with left states.

Moreover, equality of the complete oriented state is the sharp
**context-free** rule: if (3.4) fails, some exterior left collar which does
not already contain a coordinate in the symmetric difference detects the
failure in a crossing union.  Thus no weaker right-state summary guarantees
transparent splicing against every admissible exterior.

#### Proof

Substituting (3.4) into (3.3) preserves each old cell individually rather
than merely as a two-cell multiset.  Identical ticket and age data gives the
remaining assertions of Theorem 3.1.  For sharpness, choose a coordinate in
the first unequal cumulative union and an exterior left collar avoiding it;
the corresponding crossing unions differ.  \(\square\)

## 4. Recursive consequence and obstruction

The scalar deadline mismatch of a critical balanced vortex is not itself
an additive-length obstruction: Theorem 2.1 shows how a one-level mismatch
can be absorbed by changing from owner phase to root phase without adding a
source position.  The central middle-levels cycle supplies exactly the
required root/owner incidence.

However, the following stronger recursive state is necessary.

> **Two-phase regenerative vortex state.**  At each critical step, export a
> cyclic literal antecedent in the phase \(\epsilon=D_s-D_q\), together with
> all lower-chain, upper, residence, and compiler tickets, and expose a cut
> whose complete ambient boundary tensor satisfies Theorem 3.1 with the
> complement component.  After splicing, the same kind of state must be
> available for the next step.

An owner-phase-only induction fails at every step with \(\epsilon=1\) by
the rank obstruction in Theorem 2.1.  Paying one new position to repair
each such failure costs \(\Theta(\sqrt s)\) over a full recursion by
Corollary 1.2.  Thus the balanced-subcube vortex can be recursively
decorated with no accumulating additive length **if and only if** the
phase-adaptive decorated antecedent and zero-charge boundary state can be
regenerated.  The Middle Levels Theorem proves only its undecorated central
projection.
