# Short mandatory-core gaps carry arbitrary payload words with private interval addresses

**Date:** 2026-08-05  
**Method:** the short-gap mandatory-core theorem and literal marker
projection; no computation or search  
**Status:** unconditional local theorem. Inside any good free block, the
constant core of the existing triangular chart may be replaced by an
arbitrary payload word on the common core. Every payload interval union is
then lifted by a private forced-marker address, with no collision and no
owner damage. This is an exact local Pascal recursion, not a global target
cover.

## 1. Set-up

Let

\[
                         P=(P_i)_{i\in\mathbb Z_W}               \tag{1.1}
\]

be a cyclic simple rank-\(t\) Johnson trace,

\[
 P_{i+1}=P_i-\{\delta_i\}+\{\iota_{i+1}\}.                      \tag{1.2}
\]

Assume \(P\) is the maximal depth-\(d\) antecedent of a resident rank-
\(r=t+d\) owner trace. Put

\[
 F_i=(P_i\setminus P_{i-1})\cup(P_i\setminus P_{i+1})
     =\{\iota_i,\delta_i\}.                                     \tag{1.3}
\]

Let \(G=[a,b]\) be a cyclic interval of length \(g\le d\). Assume

\[
 U_G=\{\iota_i:i\in G\}
\]

has \(g\) distinct elements and

\[
                         F_i\cap U_G=\{\iota_i\}
                         \qquad(i\in G).                         \tag{1.4}
\]

Define the boundary-free common core

\[
 C_G=\left(\bigcap_{i\in G}P_i\right)
       \setminus\bigcup_{i\in G}F_i.                            \tag{1.5}
\]

Choose an arbitrary payload word

\[
                         H_i\subseteq C_G
                         \qquad(i\in G),                         \tag{1.6}
\]

and define

\[
 A_i=
 \begin{cases}
   H_i\cup F_i,&i\in G,\\
   P_i,&i\notin G.
 \end{cases}                                                    \tag{1.7}
\]

## 2. Exact payload lift

### Theorem 2.1 (arbitrary-payload marker recursion)

The word \(A\) satisfies

\[
                         D^dA=T.                                \tag{2.1}
\]

For every nonempty interval \(I\subseteq G\),

\[
 \boxed{
 \bigcup_{i\in I}A_i
   =\left(\bigcup_{i\in I}H_i\right)
      \cup\left(\bigcup_{i\in I}F_i\right).}                    \tag{2.2}
\]

Moreover,

\[
 \boxed{
 \left(\bigcup_{i\in I}A_i\right)\cap U_G
       =\{\iota_i:i\in I\}.}                                    \tag{2.3}
\]

Consequently the \(g(g+1)/2\) interval values in (2.2) are pairwise
distinct, independently of repetitions among the payload interval unions.

#### Proof

For \(i\in G\),
\[
 F_i\subseteq A_i\subseteq P_i.
\]
Outside \(G\), equality \(A_i=P_i\) holds. Since the only modified cyclic
gap has length at most \(d\), the short-gap mandatory-core theorem gives
\(D^dA=T\).

Taking unions gives (2.2). By (1.5)--(1.6), every payload letter is
disjoint from \(U_G\). Equation (1.4) says that the only incoming marker
contributed by \(F_i\) is \(\iota_i\). This proves (2.3).

Two proper cyclic intervals of length at most \(g<W\) have different sets
of positions. The incoming markers are distinct, so their right sides in
(2.3) differ. Hence their complete values differ. \(\square\)

### Corollary 2.2 (rank control)

If the deletion labels across \(G\) are distinct, then

\[
                         |C_G|\ge t-g-1.                        \tag{2.4}
\]

If

\[
 \left|\bigcup_{i\in G}H_i\right|\le t-2g-1,                   \tag{2.5}
\]

then every interval value in (2.2) has rank below \(t\).

#### Proof

The intersection of \(g\) consecutive rank-\(t\) Johnson states loses at
most \(g-1\) coordinates. Among all mandatory labels, only the incoming
label at the left boundary and the outgoing label at the right boundary
can remain in every state. Removing those two possible labels proves
(2.4).

For \(I\subseteq G\),
\[
 \left|\bigcup_{i\in I}A_i\right|
 \le\left|\bigcup_{i\in G}H_i\right|+\sum_{i\in I}|F_i|
 \le(t-2g-1)+2g=t-1.
\]
\(\square\)

## 3. Exact recursion interpretation

Let

\[
                         Y(I)=\bigcup_{i\in I}H_i.               \tag{3.1}
\]

The payload word may be chosen by any smaller construction on the ground
set \(C_G\). The outer owner trace does not see its internal details:
every payload interval value \(Y(I)\) is transformed into

\[
                         Y(I)\cup F(I),
 \qquad
                         F(I)=\bigcup_{i\in I}F_i,               \tag{3.2}
\]

and the private address in (2.3) remembers \(I\) exactly. Thus collisions
in the payload deck do not create collisions in the lifted chart.

The constant-core chart is the special case \(H_i=K\) for all \(i\).
The new freedom is the whole interval deck of an arbitrary word \(H\), not
just one common value.

This is a literal local Pascal recursion, but it is not an exact cover
theorem. A prescribed target \(S\) can use interval \(I\) only if

\[
                         F(I)\subseteq S
\]

and the residual value \(S\setminus F(I)\) is supplied by the payload
interval inside \(C_G\). Choosing many blocks and payloads so that every
named target is supplied once remains the global coordinate-value atlas
problem.

## 4. Scope

The short-gap owner-safety theorem used above is

MATH_THEOREM_PBBS_SHORT_GAP_MANDATORY_CORE_LOCALIZATION_AND_BLOCK_TEMPLATE_20260805.md.

This theorem proves no placement of the free blocks, no complete cover of
the lower Boolean ideal, no typed common-cap route, and no universal OR
word.
