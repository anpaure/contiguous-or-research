# Independent audit: Pascal port rank aperture and regenerative chain

**Date:** 2026-08-02  
**Scope:** solver-free replay of
`MATH_THEOREM_K_PASCAL_PORT_RANK_APERTURE_AND_ONE_CREDIT_REGENERATIVE_CHAIN_20260802.md`.
No claim about a complete canonical table, upper shadows, residence, exterior
windows, or compiler matching is audited here.

## 1. Common-intersection replay

Let `R` be the union of the common ordered rail and let `c_0,c_1` be the
two predecessor leading blocks.  Each closing owner contains `R`.  Old and
crossed legality give

\[
 c_0,c_1\subseteq T_0,qquad c_0,c_1\subseteq T_1.
\]

Therefore

\[
 (R\cup c_0)\cup(R\cup c_1)\subseteq T_0\cap T_1.
\]

This proves the claimed support inclusion without using ranks, Hall, or
chronology.

For distinct rank-`r` owners, the intersection has size at most `r-1`.
Two contained rank-`(r-1)` supports must both equal that intersection.  The
strict one-copy obstruction follows.

## 2. Defect arithmetic

Write `Q_e=R union c_e` and `|Q_e|=r-1-e_e`.  Then

\[
\begin{aligned}
 |Q_0\triangle Q_1|
 &=2|Q_0\cup Q_1|-|Q_0|-|Q_1|\\
 &\le2(r-1)-(r-1-e_0)-(r-1-e_1)\\
 &=e_0+e_1.
\end{aligned}
\]

There is no reversed inequality hidden here.  Equality is possible for
`Q_0 subset Q_1`, `|Q_1-Q_0|=1`, with defects `(1,0)`.

## 3. Literal smallest calibration

Take `r=4,d=2`,

\[
 R=\{0\},\quad b=1,
 \quad a_0=2,\ a_1=3,\ a_2=4,
 \quad w=(\{0\}).
\]

The aperture and ordinary predecessor heads are

\[
 h_{p_*}=(\{1\},\{0\}),
 \qquad h_{p_1}=(\{1,3\},\{0\}).
\]

The closing heads and owners are

\[
 h_{g_0}=(\{0\},\{2,3\}),
 \quad T_0=\{0,1,2,3\},
\]

\[
 h_{g_1}=(\{0\},\{3,4\}),
 \quad T_1=\{0,1,3,4\}.
\]

Both caps have lower endpoint `{1}`.  The old assignments are legal, and
the crossed leading blocks `{1,3}` and `{1}` are legal for `g_0` and `g_1`
respectively.  The supports are

\[
 Q_*=\{0,1\},\quad Q_1=\{0,1,3\},
 \quad U_0=\{0,2,3\},\quad U_1=\{0,3,4\}.
\]

Thus the only noncentral support is `Q_*`, and the symmetric-difference
bound is attained with value one.

## 4. General chain replay

For the general construction,

\[
 P_j=T_j\setminus U_j=\{b\}.
\]

At step `j`, the new leading block `{b,a_j}` is contained in

\[
 T_{j-1}=R\cup\{b,a_{j-1},a_j\},
\]

while the anchor `{b}` is contained in `T_j`.  These are exactly the two
crossed cap tests.  The selected matching switch leaves the same physical
anchor token on the new closing role, so no new aperture token is created.

Pairwise distinctness follows from the visible signatures:

* owners are labelled by consecutive pairs `{a_j,a_(j+1)}` plus `b`;
* closing-head supports have the same pairs but omit `b`;
* ordinary predecessor supports contain `b` and one `a_j`; and
* the aperture contains `b` and no `a_j`.

The audit therefore confirms the local one-copy ledger stated in the
theorem.  It does not promote the deficient aperture to a central target.

## 5. Suspension replay

Adding a fresh `z` to one rail block adds it to every `R`, `Q`, and `U`,
and adding it to every owner gives

\[
 (T_j+z)\setminus(U_j+z)=T_j\setminus U_j=\{b\}.
\]

All old and crossed cap tests are unchanged.  Owner and support ranks each
increase by one, so the defect vector stays `(1,0,...,0)`.

## 6. Verdict

The rank-aperture obstruction, defect inequality, anchored recurrence,
explicit one-aperture chain, and rank suspension all pass independently.
The sharp unresolved row is exactly the global repayment/embedding of the
one deficient head occurrence.  No downstream gate follows from this
audit.

