# Independent audit of the PBBS dominance-staircase seam

Date: 2026-07-25

Audited source:
`MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md`.

## Verdict

**PASS.**  The \(2H-1\) lower staircase, \(4H-1\) complete one-cut chart,
\(\ell+(5H-1)J\) component ledger, and the conditional
\((CP_A)\Rightarrow\) coefficient-one theorem are correct as stated.

No PBBS return classification is used.  The argument applies to every
rank-\((m+1)\) Johnson collar satisfying \(2H\le m+1\), and only claims
lower targets whose intersection has the floor rank.

## Checks

1. **Dominance coordinates.**  A crossing owner window contains the
   central core \(C=X_{-1}\cap X_0\).  A coordinate \(x\in C\) survives
   \(P_{s,t}\) exactly when its maximal run through the cut has extents
   \(u_x\ge s,v_x\ge t\).  Capping at \(H\) does not affect any query in
   \([H]^2\).

2. **Floor-correct southwest exclusion.**  If a run point is strictly
   southwest of \((s,t)\), the coordinate has an internal arrival and a
   later internal departure in the query window.  Map each initial
   coordinate missing from the intersection to its first departure.  The
   later departure is unused, including when the coordinate was initially
   present (it then had an earlier first departure before its reentry).
   Thus at most \(s+t-2\) of the \(s+t-1\) transitions are images, making
   the intersection at least one larger than floor rank.  All off-by-one
   cases pass.

3. **Pareto interception.**  Pareto minima have increasing first and
   strictly decreasing second coordinate.  East-before-south motion is
   essential.  In the west/north case it reaches the query's vertical line
   before descending below its height; otherwise the next Pareto minimum
   would be strictly southwest.  The reverse argument is north-before-west.
   The constructed vertex lies between query and containing run point in
   both coordinates.

4. **Physical OR order.**  Along the staircase, \(z_1\ge s\) is a suffix
   condition and \(z_2\ge t\) is a prefix condition.  Their intersection is
   one contiguous subpath.  Every letter \(P_z\) is a subset of the target;
   rectangle interception supplies a letter containing each target
   coordinate.  Therefore the OR is exact, not merely a cover.

5. **Nonzero letters.**  Every staircase vertex indexes at most \(2H\)
   owners.  One coordinate is lost per transition, giving rank at least
   \(m+2-2H\ge1\).

6. **Upper chart and several cuts.**  The owner segment
   \(X_{-H},\ldots,X_{H-1}\) literally contains every crossing upper owner
   window.  A target crossing several cuts is represented in the chart of
   any one of them because every chart uses the original cyclic owners, not
   endpoint dummies.

7. **Ledger.**  Endpoint-capped erosion costs \(\ell+HJ\); charts cost
   \((4H-1)J\), giving \(\ell+(5H-1)J\).  A minimum circular transversal
   on an active cycle is at most \(2\nu_H(C)\), while inactive cycles cost
   at most \(2H\) each.  Hence

   \[
    L_H\le W+2HB_m+2(5H-1)\nu_H(P_m).
   \]

8. **Asymptotics.**  Under \(\nu_{A\sqrt m}=O_A(B_m)\), the normalized
   central excess is \(O_{A,K_A}(m^{-1/2})\).  Constants may depend
   arbitrarily on fixed \(A\); the displayed diagonal thresholds absorb
   them, and the product-SCD tail then vanishes as \(A\to\infty\).

## Scope warning

The theorem does not prove \((CP_A)\).  It changes the packing gate from
the old little-oh Catalan physical scale to the big-oh Catalan scale,
equivalently

\[
 \overline\nu_{A\sqrt m}=O_A(B_m/(2m+1))
\]

on the quotient.  The best current unconditional quotient bound remains
larger by \(\Theta(\sqrt{m\log m})\).

