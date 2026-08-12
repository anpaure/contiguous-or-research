# Ordered-chain diagonal closure, the minimal cubic trade, and a protected all-depth absorber

**Date:** 2026-08-01  
**Status:** unconditional theorem in the complete local-order flag host.  It
proves that the determinant-two triangle from the multi-order selector can
never be isolated, constructs the smallest nontrivial integral chain trade,
lifts it coherently through every suffix rank, and gives a polynomially
spread protected absorber menu.  It does not prove that these flags survive
the physical turn, Euler, residence, or upper-shadow restrictions.

## 0. Outcome

Let the flag host consist of all deletion flags

\[
 q=T_0\supset T_1\supset\cdots\supset T_{d-1},
 \qquad |T_j|=m-j,                                             \tag{0.1}
\]

with one row class for every displayed rank.  The following facts hold.

1. Every determinant-two three-column triangle has a **diagonal flag**
   containing all three witness rows.  More generally, every pairwise
   co-flagged family of rows lies in one flag.  Thus an isolated triangle is
   impossible in the complete host.
2. There is no nontrivial two-against-two flag trade.  The smallest trade is
   a three-against-three Johnson-triangle trade.
3. That cubic trade has an exact all-depth lift: both sides use the same
   three roots and the same three named suffix targets at every rank.
4. Adding any core flag to one side of a private cubic trade gives a
   four-against-three absorber.  Its off state covers nine auxiliary rows
   per three consecutive levels (and, in the all-depth lift, three auxiliary
   rows at every level); its on state covers exactly the same auxiliary rows
   plus the complete core flag.
5. A fixed core flag has

   \[
   L_d=2\binom{m-1}3(m+1)_3(m-4)_{d-3}                         \tag{0.2}
   \]

   such rooted absorbers.  In the range \(d=O(\sqrt m)\), a fixed resource
   row occurs in at most

   \[
   M_d=2\binom{m-2}2(m+1)_3(m-4)_{d-3}                         \tag{0.3}
   \]

   candidates, so \(L_d/M_d=(m-1)/3\).  Consequently any fixed number of
   resource-disjoint core flags has pairwise compatible absorbers whenever

   \[
                         m-1>3b+9d(h-1),                       \tag{0.4}
   \]

   where \(b\) is an additional forbidden-row bank.

The determinant-two minor is therefore not the one-copy obstruction in the
complete local-order host.  The exact remaining issue is whether a
sufficient part of this cubic absorber menu survives the **physical**
structural zeros.

## 1. The complete ordered-chain host

Put \(n=2m+1\).  A depth-\(d\) flag is an ordered deletion word

\[
                 f=(q;a_1,a_2,\ldots,a_{d-1}),                 \tag{1.1}
\]

where \(q\in\binom{[n]}m\) and the \(a_i\) are distinct elements of \(q\).
Its rank-\((m-j)\) row is

\[
                 T_j(f)=q-\{a_1,\ldots,a_j\}.                  \tag{1.2}
\]

Every column of the incidence matrix is therefore a chain in the Boolean
lattice.

## 2. Every determinant-two triangle has a diagonal

### Theorem 2.1 (flag-diagonal closure)

Let \({\cal X}\) be a family of distinct set rows in the depth window
\(m-d+1,\ldots,m\).  If every pair of rows in \({\cal X}\) occurs together
in some flag, then the rows of \({\cal X}\) are nested and one flag contains
all of them.

#### Proof

Two rows occurring in one flag are comparable by inclusion.  Distinct rows
of the same rank cannot be comparable, so the ranks in \({\cal X}\) are
distinct.  Ordering by rank therefore orders the rows by strict inclusion.
Insert arbitrary intermediate sets between consecutive rows, and extend at
the top and bottom inside the depth window.  The resulting maximal chain is
a flag containing \({\cal X}\). \(\square\)

### Corollary 2.2 (no isolated determinant-two triangle)

Suppose three rows \(X_1,X_2,X_3\) and three flag columns have restricted
incidence matrix

\[
                 \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix}. \tag{2.1}
\]

Then a fourth flag column has restricted incidence vector

\[
                              (1,1,1)^{\mathsf T}.              \tag{2.2}
\]

#### Proof

Every pair of witness rows occurs in one of the three columns.  Apply
Theorem 2.1. \(\square\)

Thus the half-integral solution of the isolated \(3\times3\) submatrix is
not a local feasibility obstruction in the complete host: its three rows
are covered integrally by the diagonal flag.  Structural zeros can delete
that diagonal, but then the obstruction belongs to the restricted physical
support, not to the all-order chain geometry.

## 3. The smallest genuine flag trade

A flag trade is a pair \((M_0,M_1)\) of distinct flag matchings which cover
the same multiset of rows at every rank.

### Proposition 3.1 (no two-flag trade)

There is no nontrivial trade with \(|M_0|=|M_1|=2\).

#### Proof

It suffices to inspect two consecutive ranks.  Suppose two distinct
rank-\((r-1)\) rows \(A_1,A_2\) are reassigned between two distinct
rank-\(r\) rows \(B_1,B_2\).  A nontrivial swap requires

\[
                    A_1,A_2\subseteq B_1\cap B_2.              \tag{3.1}
\]

But two distinct rank-\(r\) sets have intersection of rank at most \(r-1\),
and if the intersection has rank \(r-1\), it contains exactly one
rank-\((r-1)\) set.  Thus (3.1) is impossible.  The same argument applies
to a swap at any adjacent pair of levels.  After cancelling common columns,
every nontrivial two-against-two trade would have such a first changed
adjacency. \(\square\)

### Theorem 3.2 (cubic Johnson-triangle trade)

Let \(Q\in\binom{[n]}m\), choose distinct
\(u_0,u_1,u_2\in Q\), and choose distinct labels
\(x_0,x_1,x_2\notin Q\).  Indices are read modulo three.  Put

\[
 \begin{aligned}
 R_i&=Q-\{u_i\}+\{x_i\},\\
 P_i&=Q-\{u_i\},\\
 S_i&=Q-\{u_i,u_{i+1}\}.
 \end{aligned}                                                 \tag{3.2}
\]

Then

\[
 M_0=\{(S_i\subset P_i\subset R_i):i\in\mathbb Z_3\},         \tag{3.3}
\]

and

\[
 M_1=\{(S_i\subset P_{i+1}\subset R_{i+1}):i\in\mathbb Z_3\} \tag{3.4}
\]

are two matchings with exactly the same bottom, middle, and root rows.

#### Proof

The three \(P_i\) are distinct facets of \(Q\), the three \(S_i\) are
their cyclic pairwise intersections, and the three \(R_i\) are distinct
roots.  Both (3.3) and (3.4) use every one of these rows exactly once.
All displayed containments are immediate from (3.2). \(\square\)

Proposition 3.1 and Theorem 3.2 show that cubic degree is minimal.

## 4. Coherent lift through every suffix rank

Assume \(d\ge3\).  Choose an ordered tuple

\[
 W=(w_3,w_4,\ldots,w_{d-1})                                    \tag{4.1}
\]

of distinct elements of \(Q-\{u_0,u_1,u_2\}\).  Replace (3.3)--(3.4) by
the full flags

\[
 f_i^0=(R_i;x_i,u_{i+1},w_3,\ldots,w_{d-1}),                   \tag{4.2}
\]

and

\[
 f_i^1=(R_{i+1};x_{i+1},u_i,w_3,\ldots,w_{d-1}).               \tag{4.3}
\]

### Theorem 4.1 (all-depth cubic trade)

The matchings

\[
                         M_0(W)=\{f_i^0:i\in\mathbb Z_3\},
 \qquad M_1(W)=\{f_i^1:i\in\mathbb Z_3\}                      \tag{4.4}
\]

cover the same three named rows at every rank
\(m,m-1,\ldots,m-d+1\).

#### Proof

The first deletion in (4.2) gives \(P_i\), while the first deletion in
(4.3) gives \(P_{i+1}\).  The second deletion in both flags indexed by
\(i\) gives the same set \(S_i\).  Every later deletion is the same prefix
of \(W\), so the two sides use the same continuation below each \(S_i\).

The three rows at every deeper rank remain distinct.  If
\(K=Q-\{u_0,u_1,u_2\}\), then \(S_i=K\cup\{u_{i+2}\}\).  Since \(W\subset
K\), every continuation below \(S_i\) retains its private marker
\(u_{i+2}\).  Hence each side is a matching, and their row multisets agree
at every rank. \(\square\)

This is the required coherent generalization: no independent rankwise
rounding is used.

## 5. A rooted four-versus-three absorber

Fix a core flag

\[
                  f_*=(Q;a_1,a_2,\ldots,a_{d-1}).               \tag{5.1}
\]

In Theorem 4.1 require

\[
 U=\{u_0,u_1,u_2\}\subset Q-\{a_1\},
 \qquad W\subset Q-(U\cup\{a_1\}).                             \tag{5.2}
\]

Then every auxiliary suffix row retains \(a_1\), whereas every proper
suffix row of \(f_*\) omits \(a_1\).  The auxiliary roots use an exterior
label and differ from \(Q\).  Thus the cubic trade is resource-disjoint
from the complete core flag.

Define

\[
                 A_{\rm off}=M_1(W),
 \qquad A_{\rm on}=M_0(W)\cup\{f_*\}.                           \tag{5.3}
\]

### Theorem 5.1 (rooted chain absorber)

The off state covers one common auxiliary bank of three rows at every
rank.  The on state covers exactly the same auxiliary bank and, in
addition, every row of \(f_*\).  Both states are matchings.

Hence (5.3) is a literal all-depth absorber for one complete flag.  Together
with Corollary 2.2, it absorbs the diagonal completion of every
determinant-two triangle without creating an unpriced suffix-rank marginal.

#### Proof

Theorem 4.1 gives equality of the auxiliary row multisets.  Condition (5.2)
gives disjointness from the core rows.  Adding \(f_*\) to the first side is
therefore legal and adds exactly the advertised core rows. \(\square\)

After cancelling common columns, a private-core absorber with \(t\) off
flags and \(t+1\) on flags contains a nontrivial \(t\)-against-\(t\) trade
on its auxiliary bank.  Proposition 3.1 forces \(t\ge3\).  Thus the
seven-column absorber (5.3) is minimal within this standard private-core
model.

## 6. Exact menu size and resource loads

Use \((z)_r=z(z-1)\cdots(z-r+1)\), with \((z)_0=1\).  Fix the core flag
\(f_*\).  Choose:

* a three-set \(U\subset Q-\{a_1\}\);
* one of the two cyclic orientations of \(U\);
* an injection \(U\to[n]-Q\), giving the three exterior labels \(x_i\);
* an ordered \((d-3)\)-tuple \(W\) from \(Q-(U\cup\{a_1\})\).

This gives exactly

\[
 L_d=2\binom{m-1}3(m+1)_3(m-4)_{d-3}                          \tag{6.1}
\]

labelled absorbers.

### Lemma 6.1 (one-row loads)

A fixed auxiliary middle row occurs in at most

\[
 M_d^{\rm mid}=2\binom{m-2}2(m+1)_3(m-4)_{d-3}                \tag{6.2}
\]

candidate absorbers.  A fixed auxiliary root row occurs in at most

\[
 M_d^{\rm root}=2\binom{m-2}2(m)_2(m-4)_{d-3}.                 \tag{6.3}
\]

For a fixed rank-\((m-j)\) suffix row, \(2\le j<d\), the load is at most

\[
 M_{d,j}^{\rm suf}
 \le
 3j!(m-j-1)(m-j-2)_{d-j-1}(m+1)_3.                            \tag{6.4}
\]

If \(d=O(\sqrt m)\), then for every sufficiently large \(m\),

\[
              M_d:=\max\left(M_d^{\rm mid},M_d^{\rm root},
                      \max_{2\le j<d}M_{d,j}^{\rm suf}\right)
                    =M_d^{\rm mid}.                            \tag{6.5}
\]

#### Proof

For (6.2), the omitted element \(u\) is determined; choose the other two
members of \(U\), its cyclic orientation, the exterior injection, and
\(W\).  For (6.3), both \(u\) and its exterior image are determined.

For (6.4), write the fixed suffix as \(Q-A\), \(|A|=j\).  Choose the
two-set \(A\cap U\), the third member of \(U\), the cyclic position and
orientation, the order of the remaining \(j-2\) elements of \(A\) in the
prefix of \(W\), the tail of \(W\), and the exterior injection.  This gives
the displayed upper bound.

Finally,

\[
 {M_{d,j}^{\rm suf}\over M_d^{\rm mid}}
 \le {3j!\over(m-2)_{j-1}},                                    \tag{6.6}
\]

which is at most one uniformly for \(2\le j<d=O(\sqrt m)\) and large
\(m\).  Equation (6.3) is smaller than (6.2). \(\square\)

In particular,

\[
                         {L_d\over M_d}={m-1\over3}.             \tag{6.7}
\]

## 7. Protected greedy packing

### Theorem 7.1 (bounded protected absorber bank)

Let \(f_1,\ldots,f_h\) be pairwise resource-disjoint core flags.  Besides
their own core rows, forbid a bank of at most \(b\) resource rows.  In the
range \(d=O(\sqrt m)\), the cores admit pairwise resource-disjoint rooted
absorbers whenever

\[
                         m-1>3b+9d(h-1).                        \tag{7.1}
\]

#### Proof

One forbidden row deletes at most \(M_d\) candidates from a menu.  The
auxiliary bank of one selected cubic trade contains exactly three rows at
each of the \(d\) ranks, and therefore deletes at most \(3dM_d\) candidates
from another menu.  Greedily selecting the absorbers leaves, at step
\(j<h\), at least

\[
                     L_d-(b+3dj)M_d                             \tag{7.2}
\]

options.  Equations (6.7) and (7.1) make this positive. \(\square\)

For fixed \(h\), \(b=O(hd)\), and \(d=O(\sqrt m)\), condition (7.1)
holds for all sufficiently large \(m\).  Thus the complete flag host has a
genuinely spread protected absorber atlas, not merely one formal cubic move.

## 8. What this removes, and what remains

The determinant-two minor from the flag-selector note no longer counts as
evidence for an intrinsic one-copy gap:

* its witness rows always have a diagonal flag;
* the full diagonal flag has a minimal all-depth absorber;
* any fixed protected bank of such absorbers can be planted with explicit
  list-to-conflict ratio \(\Theta(m/d)\).

The surviving issue is **structural-zero robustness**.  A physical
chronology may forbid the diagonal flag, one orientation of the cubic
trade, or the common continuation \(W\) because of turn compatibility,
Euler balance, residence, owner collisions, or upper witnesses.  None of
those rows is encoded in the complete local-order host.

The next exact lemma should therefore be stated as follows.

> **Physical cubic flag-lift lemma.**  After the prepared task roots and
> their turn guards are frozen, a positive \(\Omega(m^{-1})\) fraction of
> the rooted absorber menu (6.1) survives as literal safe chronology
> packets, with the same all-depth row identity.

By Theorem 7.1, that density is already enough for every fixed task bank.
The open theorem is physical lifting, not chain-marginal integrality.

