# Independent cross-audit of the adaptive-MTF portal depletion obstruction

Date: 2026-07-25

Audited files:

* `ADAPTIVE_MTF_PORTAL_DEPLETION_OBSTRUCTION_20260725.md`;
* `ADAPTIVE_MTF_PORTAL_DEPLETION_OBSTRUCTION_SELF_AUDIT_20260725.md`.

## Verdict

**FAIL AS WRITTEN; PASS AFTER ONE REQUIRED DOMAIN CORRECTION.**

The exact bridge metric, portal ledger, residual recurrence, depletion
argument away from the singleton boundary, fresh-state one-update
classification, deepest-upper support ledger, strip and odd-cut
applications, relative-codegree estimate, and economical-cover ceiling all
check out.

There is, however, a real counterexample to Theorem 3.1 under the stated
global hypothesis (1\le H<m).  When

\[
m-H=1,
\]

the source first block, all intermediate blocks, and the target residual are
all singletons.  The proof's assertion that a target block of size (m-H)
can only come from the source first block is then false.  In fact a depleted
terminal canonical state can have a one-update portal to a fresh canonical
state, whereas (3.1) claims distance at least (2H+1).

The required correction is to assume

\[
\boxed{m-H\ge2}
\]

in Theorem 3.1 and in every result which invokes it: Corollary 3.2,
Theorems 4.1--4.2, and the unrestricted statement about odd-cut geodesics in
Section 6.  Equivalently, the note may impose (1\le H\le m-2) globally.
Theorem 3.3 already includes exactly this hypothesis.  The full-strip
application in Section 7 automatically satisfies it because
(H<\ell<m), and every fixed-Gaussian-window application satisfies it for
large (m).  Consequently this correction does not change the advertised
asymptotic architecture ceiling.

Subject to that explicit correction, I find no further mathematical error.

---

## 1. Exact bridge metric

After chronological updates (X_1,\ldots,X_k), the final ordered partition
is the nonempty list

\[
X_k,
X_{k-1}\setminus X_k,
\ldots,
X_1\setminus\bigcup_{j=2}^kX_j,
D_{\cup_jX_j}(\Sigma).
\]

The positive-last-occurrence blocks must be an initial block segment of the
target.  If that segment has (t) blocks, its union is (U_t), and the
untouched source part is exactly the target suffix.  Hence every nonempty
bridge has (k\ge t_*\).  Conversely the chronological word

\[
U_t,U_{t-1},\ldots,U_1
\]

peels (U_t) into (B_1,\ldots,B_t) in the correct order.  When (t=0),
the source already equals the target and updating (B_1) is idempotent.
Thus

\[
d^+_{\rm MTF}(\Sigma,\Pi)=\max\{1,t_*\}
\]

is exact.  No hidden assumption that the target suffix literally leads the
undeleted source is used; deletion before suffix comparison is essential
and is handled correctly.

Substituting (b_j=\max\{1,t_j\}) in the previously proved path-word
ledger gives

\[
(s-1)+\sum_j(b_j-1)
=(s-1)+\sum_j(t_j-1)_+.
\]

The first initialization and every seam have the correct off-by-one.

## 2. Canonical state and residual block counts

The canonical state has a first ((m-H))-block and (H) lower singleton
markers.  Initially its upper queue has (H) singleton markers and one
((m-H))-residual.  Under

\[
\Theta_{i+1}=(\{p_i\},\Theta_i\setminus\{q_i\}),
\]

an arrival extracted from a singleton deletes one singleton and the
prepended departure replaces it; an arrival extracted from the residual
shrinks that residual and increases the singleton count by one.  Hence the
only possible nonsingleton upper block is always the final block

\[
R_i=R_0\setminus\{q_j\in R_0:j<i\}.
\]

The terminal state need not retain exactly (2H) singleton blocks, and the
source note does not assume that it does in Theorem 3.1.  It correctly uses
only the facts that every intermediate block is a singleton and
(|R_i|\le m-H).  A non-consuming component does retain exactly (H)
upper singletons, because in that case every arrival is extracted from an
existing singleton.

## 3. The missing boundary hypothesis and explicit counterexample

Take

\[
m=2,\qquad H=1,\qquad n=4,\qquad s=4.
\]

Let the fresh initial canonical state be

\[
\Pi_0=(\{1\},\{2\},\{4\},\{3\}).
\]

This corresponds to (T_0=\{1,2\}), departure (p_0=2), terminal dummy
departure (p_1=1), arrival (q_0=3), upper singleton (4), and initial
residual (R_0=\{3\}).  The canonical update by the new lower core
\(\{3\}\) produces

\[
\Sigma=(\{3\},\{1\},\{2\},\{4\}),
\]

the terminal state over (T_1=\{1,3\}).  Its initial residual has been
consumed completely, so it is residual-consuming in the sense of (2.8).

Now take the fresh canonical target

\[
\Pi=(\{1\},\{3\},\{2\},\{4\}).
\]

The one-letter update (\{1\}) sends (\Sigma) to (\Pi).  Therefore

\[
d^+_{\rm MTF}(\Sigma,\Pi)=1<3=s-1,
\]

contradicting (3.1) under the note's stated domain.

For (m-H\ge2), the proof is valid.  A target suffix of length at least
two ends in a block of size (m-H\).  No source singleton and no depleted
source residual can supply it.  The only possible source is the first
block (A).  Retaining its full size forces deletion disjoint from (A),
so it is the first surviving source block and cannot be the last block of a
suffix of length at least two.  Hence (t_*\ge s-1).

The same size separation is needed in Corollary 3.2.  Once imposed, a
bridge of length at most (s-2) leaves a target suffix of length at least
two, and its final large block must be the full, untouched source residual;
therefore source and target residuals coincide.

The self-audit repeats the invalid sentence "no other source block is large
enough" without checking the (m-H=1) boundary.  This is the only
substantive omission I found in that audit.

## 4. Fresh-state one-update classification

Theorem 3.3 already assumes (m-H\ge2), and under that hypothesis its
classification is exact.  If (A') is the target first block, put

\[
k=|A'\cap\{x_i\}|,
\quad a_0=|A\setminus A'|,
\quad b_0=|B\setminus A'|.
\]

The target-size identity is

\[
a_0+b_0=m-H+k.
\]

The target suffix's last ((m-H))-block must be the old (B)-block, so
(b_0=m-H), (B'=B), and (a_0=k).  If (k=0), the state is unchanged.
If (k>0), the surviving (A\setminus A') must itself be one singleton,
and counting the target's (2H) singleton blocks gives

\[
1+(2H-k)=2H,
\]

so (k=1).  This yields exactly (3.6), including its singleton order.
Direct deletion verifies sufficiency.

The middle-mask interpretation also has the correct queue index: for
(j\le H) the target middle mask is unchanged, while for (j>H) it is

\[
T-\{x_H\}+\{x_j\}.
\]

Thus every one-update run of fresh states preserves its residual, and its
deepest canonical upper mask is (B^c).

## 5. Deepest-upper support and system ledgers

For (m-H\ge2), every depleted component except possibly the last has an
outgoing bridge of length at least (s-1), hence contributes at least
(s-2=2H) portal excess.  Together with the first initialization this gives

\[
\mathfrak P_H\ge2H+1+2H(D-1)_+.
\]

There is no double-counting: this inequality and the analogous (J)-bound
are two separate lower bounds on the same portal sum, not a claim that they
add.

For the (J)-bound, mark the first component carrying each distinct full
residual among the non-consuming components.  Except possibly at the first
component, each marked component has a distinct incoming seam.  Its source
is either depleted, invoking Theorem 3.1, or undepleted with a different
residual, invoking the contrapositive of Corollary 3.2.  Each marked seam
therefore contributes at least (2H) excess.  This proves

\[
D-1\le\frac{\mathfrak P_H-(2H+1)}{2H},
\qquad
J-1\le\frac{\mathfrak P_H-(2H+1)}{2H}.
\]

Every non-consuming residual value contributes exactly one possible
deepest-upper canonical label, while the consuming components contribute at
most one label per middle state.  Therefore

\[
|\mathcal S_H^+|\le K_D+J.
\]

With (M_H^+=o(W)), this implies (K_D\ge N_H-o(W)).  At
(H=A\sqrt m+o(\sqrt m)),

\[
N_H/W=e^{-A^2+o(1)},
\]

and the deductions (D,J=o(W/H)) and (K_D/D=\omega(H)) are correct.
The use of canonical support rather than incidental bridge witnesses is
explicitly disclosed in both the source and its self-audit.

## 6. Cyclic strips and complementary odd cuts

For a cyclic strip, the initial residual is

\[
R_0=D\cup\{z_\ell,\ldots,z_{2\ell-H-1}\},
\]

up to the cyclic indexing convention.  All (ell-H) displayed moving
coordinates arrive before the terminal state (i=2\ell-1), while no
coordinate of (D) arrives.  Hence (R_{\rm end}=D), of size
(m-\ell<m-H).  The terminal-index convention does not lose the final
needed arrival.

Thus all (p) selected strips are consuming and

\[
\mathfrak P_H\ge2H+1+2H(p-1)=2Hp+1.
\]

For disjoint middle rows with leave (u_0),
(p=(W-u_0)/(2\ell)), so (u_0=o(W)) and
\(\mathfrak P_H=o(W)) force (H/\ell\to0).  The comparison with
independent resets differs by only (p-1) letters and has no off-by-one
error.

For a complementary geodesic, all (m-H) coordinates in the initial
residual arrive during its (m) transitions, so its terminal residual is
empty.  The stated lower bound

\[
\mathfrak P_H\ge 2H\frac{W}{m+1}+1
\]

is correct whenever (m-H\ge2).  The note must either restrict this
statement accordingly or separately exclude the exceptional boundary
(H=m-1), where the general depletion theorem is false.

## 7. Relative codegree and the economical-cover ceiling

Fixing a middle mask (T), every strip through (T) contains exactly two
distinct depth-one lower masks which are facets of (T).  Therefore

\[
\sum_{S\subset T,\ |S|=m-1}\deg(T,S)=2D_0,
\]

and the maximum real codegree satisfies

\[
\Gamma\ge2D_0/m.
\]

The degree ratio is exactly

\[
\frac{D_{\max}}{D_0}
=\prod_{i=1}^H\left(1+\frac{H}{m-H+i}\right),
\]

so

\[
\Gamma/D_{\max}
\ge\frac2m\exp\!\left(-\frac{H^2}{m-H}\right).
\]

Dummy regularization cannot erase this real codegree.  Under the explicitly
assumed growing-uniformity hypothesis

\[
e^{2R_{\rm hyp}}\Gamma
=o(D_{\max}/\log D_{\max}),
\]

taking logarithms gives (7.8).  Since

\[
2R_{\rm hyp}=4\ell(2H+1)\ge8\ell H>8H^2
\]

and (H<\ell=o(m)), one first gets (H^2=O(\log m)).  Substitution then
gives

\[
\ell H\le(1/8+o(1))\log m.
\]

Combining this with the independently forced (H/\ell\to0) yields

\[
H^2=o(\log m).
\]

Every factor of two and the coefficient (1/8) are correct.

## 8. Exact corrections required in the source and self-audit

At minimum, make the following edits.

1. Replace the global parameter line by
   \[
   1\le H\le m-2
   \]
   if no (H=m-1) statement is needed.  This is the cleanest repair.

2. Alternatively, add (m-H\ge2) to Theorem 3.1 and Corollary 3.2, and
   propagate it explicitly to Theorems 4.1--4.2 and Section 6.

3. In both proofs of Theorem 3.1, replace the unqualified sentence that a
   block of size (m-H) can only come from (A) by the qualified sentence
   that this holds because (m-H\ge2), the intermediate blocks are
   singletons, and the depleted residual has size below (m-H).

4. Add the (m=2,H=1) example above, or at least state that the excluded
   boundary really is false rather than merely untreated.

After these changes, the main asymptotic conclusion remains:

\[
\boxed{H=o(\sqrt{\log m})}
\]

inside the full-strip, standard economical-cover, exact-canonical-portal
architecture.

---

## 9. Recheck after the domain patch

The source was subsequently patched to impose (m-H\ge2) in its setup,
Theorem 3.1, Corollary 3.2, Theorems 4.1--4.2, and the odd-cut application.
This repairs the counterexample above and correctly leaves the full-strip
and Gaussian conclusions unchanged.

**Final mathematical verdict after that patch: PASS.**

Only presentational cleanup remains.  The newly inserted theorem assumptions
currently appear as the literal text `Assume (m-H\ge2).` rather than as
LaTeX; they should read `Assume \(m-H\ge2\).`  Corollary 3.4 and Section 3
of the self-audit should also state explicitly that they inherit this
hypothesis.  These do not alter any corrected mathematical conclusion.
