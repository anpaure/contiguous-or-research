# Self-audit of the adaptive-MTF portal depletion obstruction

Date: 2026-07-25

Audited source:
`ADAPTIVE_MTF_PORTAL_DEPLETION_OBSTRUCTION_20260725.md`.

## Verdict

**INTERNAL PASS, pending an independent cross-audit.**

The bridge metric, residual invariant, depletion lower bound, fresh-state
one-update classification, cyclic-strip and odd-cut applications, system
ledger, relative-codegree lower bound, and architecture ceiling have each
been reconstructed independently below.  No computation, search, or
external result beyond the matching hypothesis explicitly assumed in the
source is used.

The principal scope boundary is important: the depletion theorem is a lower
bound for bridges which end at the **exact full canonical initial state**,
including its final residual block.  It does not rule out a weaker bridge
which recreates only the prefix through rank \(m+H\) and leaves the later
tail arbitrarily partitioned.  This agrees with the scope of the exact-state
portal functional in `DIRECT_MTF_AFTER_TWO_NOGOS_20260724.md`.

## 1. Exact bridge metric

After chronological updates \(X_1,\ldots,X_k\), a coordinate is classified
by its last positive update time, or by its old source block if it was never
updated.  Therefore the final partition is exactly
\[
X_k,
X_{k-1}\setminus X_k,
\ldots,
X_1\setminus\bigcup_{j>1}X_j,
D_{\cup_jX_j}(\Sigma),
\]
with empty blocks deleted.  If the final target prefix contains \(t\)
positive-time blocks, their union is exactly \(U_t\), so the untouched
source residual is the target suffix.  This proves the lower bound
\(k\ge t_*\).

Conversely, the chronological word
\[
U_t,U_{t-1},\ldots,U_1
\]
successively splits
\(U_t=B_1\sqcup\cdots\sqcup B_t\) into the target block order.  This proves
the upper bound.  When \(t=0\), updating the existing first block is
idempotent, so the nonempty-distance convention gives \(1\).  Thus
\[
d^+_{\rm MTF}=\max\{1,t_*\}
\]
is exact.

Substitution into the already-audited portal length
\((s-1)+\sum(b_j-1)\) gives (1.11)--(1.12) without an off-by-one error.

## 2. Residual evolution

Initially the upper tail consists of \(H\) singleton blocks and one residual
\(R_0\) of size \(m-H\).  The recurrence
\[
\Theta_{i+1}=(\{p_i\},\Theta_i\setminus\{q_i\})
\]
only prepends a singleton and deletes \(q_i\) from its existing block.  It
never merges a departed coordinate back into \(R_0\).  Therefore the unique
possible nonsingleton upper-tail block at time \(i\) is precisely \(R_0\)
minus the initial-residual coordinates which have already arrived.  Equations
(2.6)--(2.8) are exact.

## 3. Depletion lower bound

Assume \(m-H\ge2\), as in the corrected source theorem.

A terminal canonical state has one first block of size \(m-H\), singleton
intermediate blocks, and a last residual of size strictly below \(m-H\) when
depleted.  A fresh exact target has a last block of size \(m-H\).

If the deletion-suffix overlap left two or more target blocks, that last
large block would have to arise from the source first block; no other source
block is large enough.  But deletion preserves source block order, so a
surviving first source block cannot be the last of a suffix with at least two
blocks.  Hence at most one target suffix block can survive and
\(t_*\ge s-1\).  This proves the bridge lower bound \(2H+1\).

If a bridge has length at most \(s-2\), the same argument forces the last
source residual to retain full size \(m-H\) and to equal the target residual.
The claimed common-residual invariant is therefore necessary.

The sharpness example has no terminal residual and leaves the source first
block as the sole target suffix block.  The depletion theorem excludes
shorter bridges, so its distance is exactly \(s-1\).

## 4. Fresh one-update classification

For
\[
\Sigma=(A,x_1,\ldots,x_{2H},B)
\]
and target first block \(A'\), let
\[
k=|A'\cap\{x_i\}|,
\quad a_0=|A\setminus A'|,
\quad b_0=|B\setminus A'|.
\]
The target-size equation is
\[
a_0+b_0=m-H+k.
\]
Because the target suffix ends in its unique block of size \(m-H\ge2\),
source order forces that block to be \(B\), hence \(b_0=m-H\) and
\(a_0=k\).  For \(k=0\) the state is unchanged.  For \(k>0\), the residual
source-first block contributes one target singleton while \(k\) source
singletons disappear, so
\[
1+2H-k=2H.
\]
Thus \(k=1\), giving exactly (3.6).  Direct deletion proves sufficiency.

For \(j\le H\), the entering singleton remains in the middle via the new
core and the ejected core point replaces it in the lower singleton queue, so
the middle set is unchanged.  For \(j>H\), the queue loses \(x_H\) and the
core gains \(x_j\), giving (3.11).  The middle-layer interpretation is
correct.

For a fresh state with residual \(B\), the deepest upper prefix contains
every block except \(B\), so it is exactly \(B^c\).  Hence \(M\) distinct
deepest-upper canonical masks require \(M\) distinct residual values.  A
linear ordering which visits \(M\) residual values has at least \(M-1\)
residual-changing seams, and Corollary 3.2 charges \(2H\) excess to each.
This verifies (3.12)--(3.13).  The argument counts canonical support only,
as the source explicitly states.

## 5. System ledger and the two canonical atom families

Among \(D\) depleted components, at most one can be last.  Each of the other
\(D-1\) outgoing seams contributes at least
\((2H+1)-1=2H\) excess letters, in addition to the first initialization
\(2H+1\).  This is exactly (4.1).

For a cyclic strip, its initial moving complement has \(\ell\) coordinates.
Only \(H\) are removed from the initial residual into singleton upper blocks;
the other \(\ell-H\) all arrive during the cut path.  The fixed opposite core
never arrives, so under the audited cyclic initialization the terminal
residual is exactly that core, of size \(m-\ell<m-H\).

For a complementary geodesic, every one of the \(m\) initial-complement
coordinates arrives.  The initial residual contains \(m-H\) of them, so it
is empty at the terminal state.  Thus both applications of Theorem 4.1 are
valid.

With \(p=(W-u_0)/(2\ell)\), (4.1) gives
\[
\mathfrak P_H/W\ge(1-u_0/W)H/\ell+1/W.
\]
For \(u_0=o(W)\), portal excess \(o(W)\) therefore forces
\(H/\ell\to0\).

If a component never consumes its residual \(B\), its complement tail has
total size \(m\), of which \(B\) already occupies \(m-H\).  Hence there are
exactly \(H\) singleton upper blocks at every state, and the deepest upper
prefix is \(B^c\).  This verifies (4.3).

Consuming components contribute at most one deepest-upper support label per
middle state, while non-consuming components contribute at most one per
distinct residual.  Thus \(|\mathcal S_H^+|\le K_D+J\).  Every first visit
to a new full residual value, except possibly at the initial component, has
an incoming seam from either a depleted source or a different undepleted
residual.  Theorems 3.1 and 3.2 charge \(2H\) excess in the two cases.
This proves both inequalities in (4.5).  The Gaussian conclusions follow
from \(N_H/W=e^{-A^2+o(1)}\).  No support multiplicity is mistaken for
support size in this argument.

## 6. Codegree and economical-cover ceiling

For a fixed middle strip mask, exactly two lower-row strip masks are its
facets.  Double counting over its \(m\) facets gives
\[
\Gamma\ge2D_0/m.
\]
Also
\[
\frac{D_{\max}}{D_0}
=\prod_{i=1}^H
\left(1+\frac H{m-H+i}\right),
\]
so
\[
\log(D_{\max}/D_0)\le H^2/(m-H).
\]
The relative-codegree lower bound (7.6) follows.

Under the explicitly assumed standard hypothesis
\[
e^{2R_{\rm hyp}}\Gamma=o(D_{\max}/\log D_{\max}),
\]
taking logarithms gives (7.8).  Since
\(2R_{\rm hyp}\ge8\ell H\), \(H<\ell=o(m)\), this first gives
\(H^2=O(\log m)\), and then
\[
\ell H\le(1/8+o(1))\log m.
\]
Combining with \(H/\ell\to0\) gives
\(H^2=o(\log m)\).  The constant and every factor of two have been checked.

## 7. Scope audit

The source does not claim:

* a lower bound for prefix-equivalent rather than exact-state bridges;
* a lower bound on trace repair;
* an obstruction to residual-preserving adaptive components;
* a global obstruction to PTAD or coefficient one;
* necessity of the economical-cover hypothesis for some different matching
  method.

Accordingly, the final conclusion is correctly limited to the full-strip,
standard-matching, exact-state-portal architecture.
