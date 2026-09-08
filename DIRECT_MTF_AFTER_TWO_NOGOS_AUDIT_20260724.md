# Audit of `DIRECT_MTF_AFTER_TWO_NOGOS_20260724.md`

Date: 2026-07-25

## Verdict

**FINAL PASS (the two scope repairs have been applied).**

The exact MTF reset and portal ledgers, the one-update criterion, the
Hamilton-path reformulation, the fixed-trace repair construction, the
functional \(\Phi_Z\), its rank-defect sandwich, the active-trace estimate,
the abstract Gaussian-window separation, and the implication
\(\mathrm{PTAD}_A\Rightarrow \nu(k)=(1+o(1))W(k)\) are all correct.

No coefficient-one estimate is used recursively in the trace cube.  The
only smaller-dimensional input is the already established unconditional
bound \(\nu(d)=O(W(d))\), for which the present
\((\sqrt2+o(1))W(d)\) theorem is sufficient.

The source now contains the following two corrections identified in the
first audit pass.

1. Theorem 4.1 says “for every \(Z\subseteq[2m]\),” whereas Section 3
   defined the construction only for a **proper** marked set.  Replace this
   by
   \[
   Z\subsetneq[2m],
   \]
   or explicitly introduce the harmless convention \(\nu(0)=0\).  All
   subsequent applications use \(|Z|=o(m)\), so this was only a boundary
   quantifier repair.  Theorem 4.1 now states the proper-set condition.
2. The abstract family in Section 7 proves that the **portal--trace ledger**
   is asymptotically strictly weaker than raw defect summability.  Because
   the note explicitly does not realize that family as the canonical defect
   of an adaptive MTF forest, it does not prove that the existential theorem
   \(\mathrm{PTAD}_A\) is strictly weaker on the restricted class of
   realizable adaptive-MTF data.  Statements that the “theorem” is strictly
   weaker should be replaced by: \(\mathrm{AD}_A\) implies
   \(\mathrm{PTAD}_A\), and the new numerical ledger is strictly weaker on
   abstract band-defect families; strict separation inside the realizable
   class remains open.  The status paragraph, Section 7 heading and
   conclusion, and final status now make exactly this distinction.

These applied repairs do not alter any displayed bound or the exact
remaining problem.

## 1. MTF reset and portal audit

For an ordered partition
\(\Sigma=(C_1,\ldots,C_r)\), the standard last-occurrence update is

\[
M_X(\Sigma)
=(X,C_1\setminus X,\ldots,C_r\setminus X),
\]

with empty residual blocks deleted.  Therefore:

* writing the pairwise disjoint target blocks in the order
  \(B_s,B_{s-1},\ldots,B_1\) makes their last occurrences occur in the
  order \(B_1,B_2,\ldots,B_s\), and erases every older residual piece;
* a one-update transition to \((B_1,\ldots,B_s)\) necessarily uses
  \(X=B_1\), and is possible exactly when
  \(D_{B_1}(\Sigma)=(B_2,\ldots,B_s)\);
* if the current state begins with the final \(\kappa\) target blocks,
  updating the remaining target blocks in reverse order preserves that
  leading target suffix and eliminates every residual piece in its
  complement.

This proves Lemmas 2.1--2.3 exactly.  In the case \(\kappa=s\), the
nonempty update \(B_1\) is idempotent, so the convention that every bridge
contains at least one nonzero letter is respected.  The full reverse reset
also proves

\[
1\le d_{\rm MTF}(\Sigma,\Pi)\le s.
\]

The imported adaptive construction needs exactly \(s=2H+2\) blocks only
for the **initial** state of each path: one lower core, \(H\) lower
singletons, \(H\) initially chosen upper singletons, and one nonempty
upper residual block.  Terminal states may have more blocks; this causes no
problem because the reverse-block reset cost is determined by the target
initial state, not by the number of source blocks.

## 2. Exact length and Hamilton-path functional

For paths with \(K_j\) middle vertices, the constructed word contains

\[
s+\sum_j(K_j-1)+\sum_{j=1}^{C-1}b_j
=W+(s-1)+\sum_{j=1}^{C-1}(b_j-1)
\]

letters.  There is no hidden seam letter: the last letter of a bridge
already creates the prescribed initial state of the following path, and
the next path then requires only its \(K_j-1\) internal updates.  Every
reset block, bridge mask, and path update is nonempty.

For fixed oriented pieces and fixed endpoint states, bridge minimization is
independent from seam to seam, since every chosen bridge ends in the exact
prescribed start state.  Hence minimizing over the order of the pieces is
precisely the directed Hamilton-path objective

\[
s-1+\min_{\sigma\in S_C}
\sum_{j=1}^{C-1}
\bigl(d_{\rm MTF}(\Pi^{\rm end}_{\sigma_j},
\Pi^{\rm start}_{\sigma_{j+1}})-1\bigr).
\]

Thus (2.7)--(2.13) are exact within the declared exact-state bridge model.
The word “exact” should not be read as a claim that no more global word
could merge a bridge with a different choice of adaptive endpoint data;
those data are part of the later joint existential optimization.

## 3. Fixed-trace repair

Let \(X=[n]\setminus Z\), \(|X|=d\ge1\), and let
\(V_1,\ldots,V_{\nu(d)}\) be a universal nonzero word on \(X\).

* For \(R=\varnothing\), every nonempty mask with trace \(R\) is a
  nonempty subset of \(X\), so the \(V\)-word covers it.
* For \(R\ne\varnothing\), the word
  \[
  R,\ R\cup V_1,\ldots,R\cup V_{\nu(d)}
  \]
  covers \(R\) literally, and an interval representing nonempty
  \(T\subseteq X\) lifts to an interval with union \(R\cup T\).

Thus the cylinder costs are exactly the advertised upper bounds

\[
\ell_R=\nu(d)+\mathbf1_{R\ne\varnothing}.
\]

For each trace one may choose either the \(h_R\) literal targets or the
cylinder word.  Concatenation cannot destroy any internal witness, proving

\[
L_{\rm repair}\le
\Phi_Z(\mathcal H)
=\sum_{R\subseteq Z}\min\{h_R,\ell_R\}.
\]

This is an exact explicit *upper ledger*, not a claim that \(\Phi_Z\) is
the optimal repair length.

## 4. The rank sandwich

For a fixed rank \(r\) and trace \(R\),

\[
h_{r,R}\le {d\choose r-|R|}
\le {d\choose\lfloor d/2\rfloor}
\le \nu(d)\le\ell_R.
\]

Also \(h_{r,R}\le h_R\).  Therefore

\[
h_{r,R}\le\min\{h_R,\ell_R\},
\]

and summing over traces gives \(M_r\le\Phi_Z(\mathcal H)\).  The reverse
upper bound follows termwise from
\(\min\{h_R,\ell_R\}\le h_R\).  Hence

\[
\max_r M_r\le\Phi_Z(\mathcal H)\le\sum_rM_r
\]

is valid, including for moving ranks in the declared band.  This also
confirms that trace compression cannot evade endpoint throughput at any
single rank.

## 5. Active-trace asymptotics and noncircularity

Under \(t=|Z|=o(m)\), put \(d=2m-t\).  Central-binomial asymptotics,
uniform because \(d\to\infty\), give

\[
\frac{W(d)}{W(2m)}
=(1+o(1))2^{-t}\sqrt{\frac{2m}{2m-t}}.
\]

The known unconditional global estimate \(\nu(d)=O(W(d))\) therefore
implies

\[
\ell_R=O(2^{-t}W+1)
\]

uniformly in the trace.  If \(J_Z\) traces are active, this yields

\[
\Phi_Z(\mathcal H)
\le O(J_Z2^{-t}W+J_Z).
\]

When \(J_Z=o(2^t)\), the first term is \(o(W)\); the second is also
\(o(W)\), since \(t=o(m)\) implies
\(2^t=\exp(o(m))=o(W(2m))\).  Corollary 6.1 is correct.

There is no circular appeal here.  The cylinder word needs only some
absolute-constant upper bound for \(\nu(d)/W(d)\).  The established
\(\sqrt2+o(1)\) upper bound supplies it before the present coefficient-one
problem is solved.

## 6. Abstract Gaussian-window separation

For

\[
t=2\left\lfloor\frac14\log_2m\right\rfloor,
\qquad d=2m-t,
\qquad |R|=t/2,
\]

a rank-\((m-q)\) set with trace \(R\) has
\(d/2-q\) unmarked coordinates.  Hence its count is exactly

\[
{d\choose d/2-q}.
\]

Uniform local central-binomial asymptotics for
\(1\le q\le A\sqrt m\) give

\[
\sum_{q=1}^{\lceil A\sqrt m\rceil}
{d\choose d/2-q}
=\Theta_A(\sqrt m\,W(d)).
\]

Here \(2^{-t}=\Theta(m^{-1/2})\), so
\(W(d)=\Theta(W/\sqrt m)\).  The raw sum is therefore
\(\Theta_A(W)\), while the single trace-cylinder word costs

\[
O(W(d))=O(W/\sqrt m)=o(W).
\]

Every individual rank defect is at most \(W(d)=o(W)\), as required by the
rank sandwich.  Section 7 is therefore a correct strict separation between
the two **numerical ledgers** at Gaussian depth.  As noted in the verdict,
realizability of this defect pattern by one adaptive forest is not proved.

## 7. Central-band and tail implication

The MTF word covers every designated canonical flag at its state endpoint.
Appending the trace-repair word covers every remaining mask in the declared
band, so, for proper \(Z\),

\[
L_{\rm band}
\le W+\mathfrak P_H+\Phi_Z(\mathcal H_H).
\]

The independently audited symmetric-chain-product tail has normalized
fixed-\(A\) cost

\[
\begin{aligned}
T(A)={}&4(A^2+\tfrac12)e^{-A^2}\operatorname{erf}(A)
+\frac{4A}{\sqrt\pi}e^{-2A^2}
+2\sqrt2\,\operatorname{erfc}(\sqrt2A)\\
={}&O((1+A^2)e^{-A^2})\longrightarrow0.
\end{aligned}
\]

Consequently \(\mathrm{PTAD}_A\), for fixed \(A\), gives

\[
\limsup_{m\to\infty}
\frac{\nu(2m)}{\binom{2m}{m}}
\le1+T(A).
\]

The order of limits in the source is correct: first \(m\to\infty\) with
\(A\) fixed, then \(A\to\infty\).  No uniformity in growing \(A\) is
needed.  Sperner supplies the matching lower bound.  Finally the valid
(slightly nonsharp but sufficient) lift

\[
\nu(2m+1)\le2\nu(2m)+1
\]

and

\[
\binom{2m+1}{m}
=\frac{2m+1}{m+1}\binom{2m}{m}
\]

transfer coefficient one to odd dimensions.  (The standard trimmed lift
in fact gives the marginally stronger \(\nu(2m+1)\le2\nu(2m)\), but the
extra \(+1\) is harmless.)

## 8. Relation to the old adaptive theorem

With independent resets,
\(\mathfrak P_H=(2H+1)(c+\rho_H)\).  The old adaptive hypothesis makes
this \(o(W)\), makes the first-band defect \(2(N_1-e)=o(W)\), and makes the
raw higher-depth defect sum \(o(W)\).  Since

\[
\Phi_Z(\mathcal A\sqcup\mathcal B)
\le |\mathcal A|+\Phi_Z(\mathcal B)
\]

trace by trace, the old hypothesis indeed implies the new one.  The
audited colour-preserving boundary choices recover the lower and upper
colours of cut forest edges, so no hidden first-shadow factorability or pin
cost is being reintroduced.

## Final status

After the two wording repairs, the note is a valid strict reduction of the
*ledger* governing the direct adaptive-MTF route.  Its exact remaining
positive theorem is still joint: the chronology, cuts, dummy departures,
initial upper partition, path order, exact bridges, and marked set must be
chosen together.  The note neither proves \(\mathrm{PTAD}_A\) nor invokes
the desired coefficient-one theorem in a smaller dimension.
