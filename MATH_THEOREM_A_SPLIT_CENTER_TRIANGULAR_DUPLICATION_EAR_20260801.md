# A split-center Pascal ear realizes the entire triangular reset-cut deficit

**Date:** 2026-08-01  
**Lane:** A, ambient duplicate bank / one-oriented reversal quotient  
**Status:** exact supplementary local construction and exact owner-neutral
integration criterion.  The ear supplies the previously isolated
\(\binom d2\) short subtriangle with no repeated packet owner, has simple
internal q1 palettes, and has a nonempty exact depth-\(d\) antecedent.
It is strictly weaker than
`MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md`,
whose two banks cover the complete two-triangle leave of size \(d(d+1)\).
The ear does not extract its owners from a global factor, preserve targets
displaced at their old occurrences, cover the extra rank row or the long
triangle, or solve the Catalan/compiler/regeneration gates.

## 0. Outcome

After the canonical owner-exact \(d\)-cell restitution tail, the forced
short residual of the opened reset-return packet is not an arbitrary family.
It is the Ferrers triangle

\[
 {\cal T}_d=
 \{T_{p,q}=B\cup U_p\cup V_q:
       0\le p\le d-2,\ 1\le q,\ p+q\le d-1\},             \tag{0.1}
\]

where \(|B|=r\), \(U_p=\{u_1,\ldots,u_p\}\), and
\(V_q=\{v_1,\ldots,v_q\}\).  Hence

\[
 \#\{T\in{\cal T}_d:|T|=r+s\}=s
       \quad(1\le s\le d-1),\qquad
 |{\cal T}_d|=\binom d2.                                  \tag{0.2}
\]

For every \(d\ge2\) there is an explicit simple Johnson path on exactly
\(2d-2\) rank-\(r\) owners such that every \(T_{p,q}\) is the union of one
contiguous owner interval.  The path has simple internal lower and upper
q1 palettes, is disjoint from the reset-return packet's owner set, and has
a nonempty flat depth-\(d\) source antecedent.  Thus each target in (0.1)
also has a literal contiguous source-word witness.

The owner count is neutral in the exact following sense: the ear uses
\(2d-2\) distinct ordinary middle owners and no stutter or nonowner.  If
their existing occurrences in a coefficient-one ambient factor are
extracted and rethreaded into this ear, the middle-owner multiset is
unchanged.  Constructing that global extraction while preserving the old
witnesses and q1 resources is a separate gate.

Only one orientation is needed.  Under the frozen global-reversal quotient,
the opposite ear, source, witnesses and compiler certificate are obtained
by reflecting the completed oriented child.

## 1. Exact form of the triangular residual

Use the four-block maximal-antecedent notation from
`MATH_THEOREM_RESET_RETURN_RAIL_LINEARIZATION_COLLATERAL_20260801.md`.
Allow an additional permanent core \(H\), and put

\[
 B=H\cup X\cup C\cup\{\delta\},\qquad |B|=r,              \tag{1.1}
\]

where

\[
 X=\{x_1,\ldots,x_d\},\qquad C=\{c_1,\ldots,c_d\}.        \tag{1.2}
\]

The first source block is

\[
 A_t=H\cup\{\delta\}\cup X[1,t]\cup C[t+1,d]
       \qquad(0\le t\le d),                               \tag{1.3}
\]

the next block begins with \(X\cup\{u_1\},X\cup\{u_2\},\ldots\),
and the final singleton block is

\[
                         H\cup C\cup\{y_1\},\ldots,
                         H\cup C\cup\{y_d\}.              \tag{1.4}
\]

Set

\[
 U_p=\{u_1,\ldots,u_p\},\qquad
 v_q=y_{d-q+1},\qquad V_q=\{v_1,\ldots,v_q\}.             \tag{1.5}
\]

### Proposition 1.1 (forced target formula)

The short targets still absent after appending
\(A_0,\ldots,A_{d-1}\) are precisely the family (0.1).

#### Proof

A missing crossing interval uses \(q\ge1\) final singleton cells and,
after the cut, the first \(d+p+1\) source cells, where

\[
                         p\ge0,\qquad p+q\le d-1.          \tag{1.6}
\]

The final \(q\) cells contribute \(H\cup C\cup V_q\).  The cells
\(A_0,\ldots,A_d\) contribute exactly \(B\), and the following \(p\)
singleton cells contribute \(U_p\).  Their union is therefore
\(B\cup U_p\cup V_q\).  Conversely every pair in (1.6) is one of the
unrestored crossing intervals counted by the exact tail formula
\(\binom d2\).  Distinctness follows from the disjoint labelled banks
\(U,V\).  This also proves (0.2). \(\square\)

## 2. Why direct continuation repeats an owner

The union of the appended cells \(A_0,\ldots,A_{d-1}\) is

\[
                         B-\{x_d\}.                        \tag{2.1}
\]

### Proposition 2.1 (first-owner obstruction)

Suppose one tries to repair (0.1) by continuing the canonical tail with a
new source cell \(G_0\), using the natural suffix--tail--continuation
witnesses and requiring the next depth-\(d\) owner to retain rank \(r\).
Restoring the smallest target

\[
                         T_{0,1}=B\cup\{v_1\}              \tag{2.2}
\]

without introducing an extraneous coordinate forces

\[
 (B-\{x_d\})\cup G_0=B.                                  \tag{2.3}
\]

But the left member of (2.3) is the first new depth-\(d\) owner window.
It therefore repeats the packet owner \(B\).  Hence no owner-exact direct
continuation of this natural form can realize even the first triangular
target.

#### Proof

The old crossing suffix already supplies \(v_1\).  The canonical tail
supplies exactly \(B-\{x_d\}\), so the continuation must add \(x_d\).
The next owner window contains the canonical tail and \(G_0\); flat rank
\(r\) forbids it from adding any coordinate outside \(B\).  This proves
(2.3), and the same \(d+1\) cells form that owner window. \(\square\)

For the literal cyclic continuation this repeated window is precisely
\(A_0\cup\cdots\cup A_d=B=T_0\).  The obstruction is only to that
specific one-sided continuation, not to an arbitrary flat continuation or
to an ambient bank at another owner occurrence.  The construction below
replaces the repeated central owner by two distinct facets of (2.2).

## 3. The split-center ear

Choose distinct \(a,b\in C\).  Choose

\[
 e_1,\ldots,e_{d-2},f_1,\ldots,f_{d-2}
       \in B-\{a,b,\delta\}                                \tag{3.1}
\]

pairwise distinct.  This is possible because \(|B|\ge2d+1\).  Put

\[
 E_p=\{e_1,\ldots,e_p\},\qquad
 F_t=\{f_1,\ldots,f_t\},                                  \tag{3.2}
\]

with \(E_0=F_0=\varnothing\), and define

\[
 L_p=(B-\{a\}-E_p)\cup\{v_1\}\cup U_p
       \qquad(0\le p\le d-2),                             \tag{3.3}
\]

\[
 R_q=(B-\{b\}-F_{q-1})\cup V_q
       \qquad(1\le q\le d-1).                             \tag{3.4}
\]

Read

\[
 \mathcal E_d=
 (L_{d-2},L_{d-3},\ldots,L_0,R_1,R_2,\ldots,R_{d-1}).     \tag{3.5}
\]

For \(d=2\), the two reservoir lists are empty and (3.5) is simply
\((L_0,R_1)\).

### Theorem 3.1 (literal triangular owner ear)

The list (3.5) is a simple rank-\(r\) Johnson path on \(2d-2\) owners.
Its internal lower and upper q1 colours are all distinct.  Moreover, for
every index pair in (0.1),

\[
             \bigcup [L_p,L_{p-1},\ldots,L_0,R_1,\ldots,R_q]
                   =T_{p,q}.                               \tag{3.6}
\]

#### Proof

Each \(L_p\) removes \(p+1\) elements of \(B\) and adds
\(p+1\); each \(R_q\) removes and adds \(q\).  Thus all have rank \(r\).
The successive exchanges are

\[
 L_p\longrightarrow L_{p-1}:u_p\mapsto e_p,qquad
 L_0\longrightarrow R_1:b\mapsto a,qquad
 R_q\longrightarrow R_{q+1}:f_q\mapsto v_{q+1}.           \tag{3.7}
\]

The labelled additions and pairwise-disjoint deletion prefixes make all
owners distinct.

For \(1\le p\le d-2\), the left lower/upper pair is

\[
 \begin{aligned}
 I^L_p&=(B-\{a\}-E_p)\cup\{v_1\}\cup U_{p-1},\\
 O^L_p&=(B-\{a\}-E_{p-1})\cup\{v_1\}\cup U_p.
 \end{aligned}                                            \tag{3.8}
\]

The central pair is

\[
 I^0=(B-\{a,b\})\cup\{v_1\},\qquad O^0=B\cup\{v_1\},  \tag{3.9}
\]

and, for \(1\le t\le d-2\), the right pair is

\[
 \begin{aligned}
 I^R_t&=(B-\{b\}-F_t)\cup V_t,\\
 O^R_t&=(B-\{b\}-F_{t-1})\cup V_{t+1}.
 \end{aligned}                                            \tag{3.10}
\]

The left families are distinguished by their \(U\)-prefixes, the right
families by their \(V-\{v_1\}\)-prefixes, and the two sides by these
disjoint marker banks.  At the marker-free boundary cases, pairwise
distinctness of \(a,b,e_1,f_1\) separates (3.8)--(3.10) when \(d\ge3\).
For \(d=2\) there is only the central edge.  Thus both q1 palettes are
simple.

Finally \(L_0\cup R_1=B\cup\{v_1\}\).  The left segment through \(L_p\)
adds exactly \(U_p\), and the right segment through \(R_q\) adds exactly
\(V_q\).  This proves (3.6). \(\square\)

### Proposition 3.2 (separation from the reset packet)

With \(a,b\in C\) and all reservoirs avoiding \(\delta\), no ear owner is
a reset-return packet owner.  Its internal q1 palettes are disjoint from
the surviving packet q1 palettes; the sole deliberate contact is

\[
                         O^0=B\cup\{v_1\},                 \tag{3.11}
\]

the omitted cut-edge upper colour.

#### Proof

Every ear owner contains \(v_1=y_d\), whereas reset-path owners contain no
\(y\)-coordinate.  A return \(P\)-owner contains \(\alpha\) and omits
\(\delta\), while every ear owner contains \(\delta\) and omits \(\alpha\).
A return \(Q\)-owner retains all of \(C\), whereas each left ear owner
omits \(a\in C\) and each right ear owner omits \(b\in C\).  This proves
owner separation.

The same membership markers separate all incident lower and upper colours,
except that the central upper colour retains all of \(B\) and adds only
\(y_d\).  This is exactly the upper colour of the deleted edge
\(Q_{d-1}E\).  All other ear colours omit \(a\) or \(b\), while surviving
\(Q\)-rail colours retain \(C\). \(\square\)

## 4. Exact flat source and literal OR witnesses

Let (3.5) be \(H_0,\ldots,H_{N-1}\), where \(N=2d-2\).  Define its
linear maximal depth-\(d\) antecedent on \(N+d=3d-2\) source positions by

\[
 S_t=\bigcap_{i=\max(0,t-d)}^{\min(N-1,t)}H_i
       \qquad(0\le t<N+d).                                \tag{4.1}
\]

### Theorem 4.1 (nonempty exact antecedent)

Every \(S_t\) is nonempty and

\[
                         D^dS=\mathcal E_d.                \tag{4.2}
\]

Every nonconstant coordinate trace on the owner path is a prefix or a
suffix.  Hence the ear has no short internal positive run at any depth;
all its residence obligations are clipped endpoint obligations.

#### Proof

Every owner in (3.5) contains \(\delta\) and \(v_1\), so (4.1) is
nonempty.  Because the deletion reservoirs are disjoint, the trace of
each \(u_i\) and of \(b\) is a prefix, while the trace of each \(v_j\),
\(j\ge2\), and of \(a\) is a suffix.  An \(e_i\)-coordinate has a suffix
trace and an \(f_i\)-coordinate has a prefix trace; every remaining
coordinate is constant.

For a binary prefix, suffix or constant owner trace, intersecting the
incident owner interval as in (4.1) and then taking each length-\(d+1\)
source union reproduces the trace exactly.  Applying this coordinatewise
proves (4.2).  The residence statement follows from the trace
classification. \(\square\)

### Corollary 4.2 (literal source witnesses)

If the owner interval in (3.6) occupies indices \([i,j]\), then

\[
                         T_{p,q}=\bigcup_{t=i}^{j+d}S_t.    \tag{4.3}
\]

Thus every forced triangular target has one contiguous source-word witness
inside the ear.

#### Proof

By (4.2), \(H_h=\bigcup_{t=h}^{h+d}S_t\).  Unioning this identity for
\(i\le h\le j\) gives (4.3), and Theorem 3.1 identifies its value. \(\square\)

## 5. Exact zero-owner-count scope

Let a coefficient-one ambient owner factor contain every rank-\(r\) owner
once.  Proposition 3.2 says the \(2d-2\) ear owners are distinct from the
packet owners, so they occur elsewhere in that factor.

### Theorem 5.1 (owner-neutral rethread criterion)

The triangular residual (0.1) is repaired with zero additional owner
occurrences if the ambient factor admits a rethread which:

1. extracts the existing occurrences of the \(2d-2\) owners in (3.5);
2. reconnects the holes left at their former locations;
3. orders the extracted owners as (3.5) with its internal q1 colours
   available; and
4. attaches the exact source (4.1) with legal endpoint ages.

Under these conditions the owner multiset is unchanged, every ear owner is
used once, and Corollary 4.2 supplies all \(\binom d2\) forced targets.
Conversely, any claimed use of this particular ear at zero owner count must
realize these four ledger conditions.

#### Proof

The operation is a permutation of existing owner occurrences.  Theorem 3.1
and Theorem 4.1 prove the internal chronology, palettes and source; the four
conditions are exactly the remaining exterior incidences. \(\square\)

This is a literal bank, not yet an unconditional global extraction theorem.
In particular, removing the old occurrences can destroy upper witnesses or
compiler cells elsewhere.  Those casualties must be protected or repaired
in the same global rethread.

## 6. Reversal quotient and remaining debt

Construct only the oriented ear above.  If it is part of one complete child
state, global reversal transports its owner path, source antecedent,
triangular witnesses, endpoint ages and occurrence-labelled compiler
matching bijectively.  Therefore no fixed-address intersection of the two
ear compiler graphs is required.  This uses
`MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md`.

The quotient does not make the ear an actuator and does not repair an
incomplete oriented child.  The exact remaining rows are:

1. prove the ambient extraction/rethread conditions of Theorem 5.1;
2. preserve every target displaced at the old ear-owner occurrences;
3. cover any additional long-interval cut losses beyond (0.1);
4. solve the still-joint fixed-\(M_0\) lower/root, other-head and graphic
   Catalan correlation; and
5. give one oriented complete compiler and regenerate the quotient state.

No theorem here uses the invalid arbitrary-second-facet shortcut: a tail
relative to fixed \(M_0\) still fixes its lower preimage and legal other
head.  No bare-cut \(O(1)\) conclusion or additive bound is claimed.
