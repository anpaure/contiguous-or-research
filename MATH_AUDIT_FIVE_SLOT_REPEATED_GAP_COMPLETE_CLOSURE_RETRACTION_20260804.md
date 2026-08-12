# Retraction audit: the proposed five-slot repeated-gap closure

**Date:** 2026-08-04  
**Method:** independent pure-mathematical implication audit.  
**Verdict:** **RETRACTED — DO NOT CITE AS A POSITIVITY THEOREM.**

## 1. Fatal direction error

The proposal uses the fact that every interior critical point of \(F_A\)
on \([0,A/2]\) is a strict local maximum.  The valid endpoint consequence
is

\[
 \boxed{
 F_A(u)\ge\min\{F_A(0),F_A(v)\}
 \qquad(0\le u\le v\le A/2).}                            \tag{1.1}
\]

Indeed, the minimum of \(F_A\) on \([0,v]\) occurs at one of the two
endpoints, so every interior value \(F_A(u)\) is at least their minimum.

The retracted note instead states

\[
 F_A(v)\ge\min\{F_A(0),F_A(u)\},                          \tag{1.2}
\]

which does not follow from the critical-point property.  It interchanges
the endpoint \(v\) and the interior point \(u\).

## 2. Both claimed margins use the invalid direction

For the short-singleton gate, the parameters satisfy

\[
                         0<u<y<A/2.
\]

The proposed estimate

\[
 F_A(y)-F_A(u)>C(A)-64/1000                               \tag{2.1}
\]

uses (1.2).  The valid relation (1.1) controls \(F_A(u)\) from below in
terms of \(F_A(y)\); it gives no lower bound of the form (2.1).
Removing (2.1) loses the \(C(A)>43/1000\) contribution on which the stated
\(9/10000\) margin depends.

For the long-singleton gate,

\[
                         0<v<a<u<2a<A/2.
\]

The two proposed estimates

\[
\begin{aligned}
F_A(2a)-F_A(u)&>C(A)-64/1000,\\
F_A(a)-F_A(v)&>C(A)-64/1000
\end{aligned}                                             \tag{2.2}
\]

again require (1.2).  The correct consequences point in the opposite
direction:

\[
\begin{aligned}
F_A(u)&\ge\min\{C(A),F_A(2a)\},\\
F_A(v)&\ge\min\{C(A),F_A(a)\}.
\end{aligned}
\]

Thus neither inequality in (2.2) is established.

## 3. Surviving statements

The following pieces remain valid in isolation:

1. the composite endpoint-descent lemma
   \[
   \sum_mK(V_m)\ge\sum_{i=0}^4F_E(V_i)
                 \ge\sum_{i=0}^4F_A(V_i);
   \]
2. the rational train bound
   \[
                         F_A(v)<64/1000
                         \qquad(0\le v\le A/2);
   \]
3. the identification of the two pure lattices with the exact
   superadditive three-denomination clocks
   \[
   (0,a,y,2y-a)
   \quad\text{and}\quad
   (0,a,2a,p).
   \]

These facts do not by themselves sign either reflected difference left in
Sections 3--4 of the retracted proof.

## 4. Correct status

The gates

\[
 \mathcal R(a,\beta)
 =\mathcal L_3(a+2\beta;a,a+\beta)
\]

and

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a)
\]

remain open on their stated interiors.  Consequently the retained-pulse
gate \(\mathcal H\), whose reduction depends on positivity of
\(\mathcal P\), also remains open.  No complete five-slot
size-three-efficient positivity theorem follows from the retracted note.

