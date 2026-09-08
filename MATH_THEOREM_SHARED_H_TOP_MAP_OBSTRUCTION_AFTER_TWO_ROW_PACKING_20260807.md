# The shared-\(H\) top map is a sharp obstruction after complete two-row packing

**Date:** 2026-08-07  
**Input:**
`MATH_THEOREM_SINGLE_BULGE_FULL_BASE_SCD_EXTENSION_AND_FIRST_LITERAL_HALL_GATE_20260807.md`  
**Method:** inspect the terminal singleton menu of each bridge cube, then
embed an explicit two-ring collision whose complete first two rows remain
disjoint  
**Status:** theorem.  It proves that Theorem 4.5 cannot be extended through
all lower ranks merely by choosing endpointwise permutations of the shared
reset banks.  An additional top-map packing condition is necessary.  It
does not rule out a positive-density family chosen with that condition
from the outset.

## 1. The terminal bridge Hall row

For a low endpoint \(e\) in ring \(i\), write

\[
 A_e=P_i\cup I_e,
\tag{1.1}
\]

where \(I_e\) is its nonempty all-low private interval, and let \(H_i\)
be the common reset bank, \(|H_i|=d\).  Its bridge cube is

\[
                         [A_e,A_e\cup H_i].
\tag{1.2}
\]

At bridge offset \(r\), the endpointwise permutation chooses one member
of

\[
 \mathcal N_r(e)=
 \{A_e\cup J:J\subseteq H_i,\ |J|=r\}.
\tag{1.3}
\]

At the terminal offset there is no choice:

\[
                         \mathcal N_d(e)=\{A_e\cup H_i\}.
\tag{1.4}
\]

Define the **top map**

\[
                         \tau(e)=A_e\cup H_i.
\tag{1.5}
\]

### Proposition 1.1 (sharp terminal Hall condition)

The Hall inequalities (6.3) at \(r=d\) hold if and only if \(\tau\) is
injective on the endpoint family.

#### Proof

Every menu in (1.4) is a singleton.  Hence for
\(X\) endpoints,

\[
 \left|\bigcup_{e\in X}\mathcal N_d(e)\right|
   =|\tau(X)|.
\]

The Hall inequality \(|\tau(X)|\ge|X|\) for every \(X\) is exactly
injectivity. \(\square\)

This condition is independent of the endpointwise orders on \(H_i\).
Those orders control proper prefixes only; every permutation ends at the
same set (1.5).

## 2. Two-row disjointness does not imply top injectivity

We give an explicit two-ring obstruction.  Assume \(d\ge3\), \(s\ge2\),
and that the ambient ground set has enough additional coordinates to choose
two disjoint private banks of size \(3d-1\).  This holds throughout the
sufficiently large triangular regime.

Choose pairwise disjoint sets and labels

\[
 |R|=s-2,qquad |H_0|=d-2,qquad a,b,c,z,
\tag{2.1}
\]

and put

\[
 T=R\cup\{a,b,c,z\}\cup H_0.
\tag{2.2}
\]

Then \(|T|=s+d\).  Define two age-one bridge bases

\[
 \begin{aligned}
 A_1&=R\cup\{a,b\},
 &P_1&=R\cup\{a\},
 &H_1&=H_0\cup\{c,z\},\\
 A_2&=R\cup\{c,z\},
 &P_2&=R\cup\{c\},
 &H_2&=H_0\cup\{a,b\}.
 \end{aligned}
\tag{2.3}

Thus

\[
 A_1=P_1\cup\{b\},
 \qquad
 A_2=P_2\cup\{z\},
\tag{2.4}
\]

and

\[
                         A_1\cup H_1=T=A_2\cup H_2.
\tag{2.5}
\]

Choose disjoint fresh sets \(E_1,E_2\), each of size \(3d-1\), outside
\(T\), and put

\[
                         F_1=E_1\cup\{b\},
 \qquad                  F_2=E_2\cup\{z\}.
\tag{2.6}
\]

The pairs \((P_i,F_i,H_i)\) lift to literal length-\(3d\) single-bulge
rings.  Place \(b\), respectively \(z\), at an age-one low endpoint.

### Theorem 2.1 (complete-two-row counterexample)

The two rings can be ordered so that all their rank-\(s\) and
rank-\((s+1)\) marked and bridge targets are pairwise distinct, while the
two chosen age-one endpoints have the same terminal bridge target \(T\).
Consequently the two-row family has no collision-free full shared-\(H\)
extension.

#### Proof

First consider rank \(s\).  A cross-ring equality would have the form

\[
                         P_1\cup\{f\}=P_2\cup\{g\}.
\]

Since \(P_1=R+a\) and \(P_2=R+c\), equality forces
\(f=c\) and \(g=a\).  But

\[
                         c\notin F_1,
 \qquad                  a\notin F_2,
\]

so the two complete base stars are disjoint.

Every rank-\((s+1)\) target of ring \(i\) has the form

\[
                         P_i\cup\{u,v\}.
\tag{2.7}
\]

Marked targets use two private labels.  Bridge targets use one private
label and the first label in that endpoint's chosen permutation of
\(H_i\).

For the distinguished endpoint of ring 1, choose \(c\) first; its target
is

\[
                         B_1=R\cup\{a,b,c\}.
\tag{2.8}
\]

For the distinguished endpoint of ring 2, choose \(a\) first; its target
is

\[
                         B_2=R\cup\{a,c,z\}.
\tag{2.9}
\]

These are different.  At every other bridge endpoint choose a member of
\(H_0\) first.  Lemma 4.4 permits these endpoint-specific orders and
preserves within-ring collision freedom.

A cross-ring equality in (2.7) forces the left pair \(\{u,v\}\) to
contain \(c\), and the right pair to contain \(a\).  By construction, the
only rank-\((s+1)\) target of ring 1 containing \(c\) is \(B_1\), and the
only such target of ring 2 containing \(a\) is \(B_2\).  Equations
(2.8)--(2.9) show that these do not collide.  Hence the complete first two
rows are globally disjoint.

Finally, (2.5) says that the terminal menus of the distinguished
endpoints are both \(\{T\}\).  Proposition 1.1 gives a Hall deficiency of
one on this two-endpoint family.  No endpointwise permutation can alter
that terminal value. \(\square\)

The fresh private banks can be arranged in arbitrary remaining low/high
positions.  Their disjointness from \(T\) is exactly what ensures that no
additional cross-ring pair in (2.7) contains the required swapped labels
\(a,c\).

## 3. Exact consequence for an all-depth theorem

Theorem 4.5 closes the bottom two rows jointly, but it does not contain the
terminal Hall row even implicitly.  A positive all-depth extension theorem
must add at least the following requirement during selection:

\[
 \boxed{
  \{A_e\cup H_i:e\text{ selected}}
  \text{ is a family of distinct named targets}.}
\tag{3.1}
\]

Only after (3.1) is enforced do the nonterminal prefix menus become the
remaining shared-\(H\) problem.

There is a symmetric hierarchy near the top.  At offset \(d-j\), the
menu consists of the sets obtained from \(\tau(e)\) by deleting a
\(j\)-subset of \(H_i\).  Thus a bounded number of top rows can be packed
by a reverse version of the fixed-\(q\) tight-window argument, but an
all-depth theorem must correlate the bottom and top selections through the
same \(H_i\).

## 4. What is and is not obstructed

The theorem proves a sharp **logical obstruction**:

\[
 \text{complete rows }s,s+1
 \centernot\Longrightarrow
 \text{a shared-}H\text{ chain extension}.
\]

It does not prove that every two-row packing has a top collision, nor that
a theta-sized top-injective subfamily cannot be chosen.  The constructive
target is now more precise:

> **Two-ended hinge packing.**  Choose the base stars, low tight paths and
> reset banks jointly so that both the protected bottom-window rows and the
> terminal top map (3.1) are injective, then solve the intermediate nested
> prefix rows.

Endpoint-specific permutations solve ordering freedom inside each cube,
but they cannot repair a failed top map.  That is the first sharp
obstruction beyond Theorem 4.5.
