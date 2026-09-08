# A depth-raised PBBS promotion edge is locally complete at (B+2)

**Date:** 2026-08-07  
**Status:** local algebra PASS, but the displayed packet is **mass-dead**.
Its first source letter in the right owner is redundant, so every copy
consumes an unused selected-owner start; at length (B+2) there are only
(d+2) such starts.  The later clean lag-two packet in
`MATH_AUDIT_PBBS_LAG2_BPLUS2_ZERO_SIDECAR_ORBIT_AND_DYNAMIC_CACHE_GATE_20260807.md`
repairs this defect.  The conditional middle-levels reduction below
remains correct, but this particular packet does not prove its hypothesis.

## 1. Parameters

Put

\[
 n=2m+1,\qquad L=d+2.
\]

Choose pairwise disjoint sets and labels

\[
 K,\quad A=\{a_0,a_1,\ldots,a_{d-1}\},\quad C,
 \quad \{u,b^-,b\},
\]

with

\[
 |A|=|C|=d,qquad |K|=m-2d-2.
 \tag{1.1}
\]

Thus, for

\[
 M:=K\mathbin{\dot\cup}A,
 \tag{1.2}
\]

we have

\[
 |M|=m-d-2.
 \tag{1.3}
\]

The construction applies whenever \(m\ge2d+2\), hence for all
sufficiently large optimal parameters.

## 2. Literal source packet

On positions \(0,1,\ldots,d+2\), define

\[
 A_0=C\cup\{b^-\},
 \qquad
 A_1=C\cup\{a_0\},
 \qquad
 A_2=K\cup\{a_0,u\},
 \tag{2.1}
\]

\[
 A_{i+2}=K\cup\{a_0,a_i\}
 \quad(1\le i\le d-1),
 \qquad
 A_{d+2}=C\cup\{b\}.
 \tag{2.2}
\]

The notation reuses \(A\) for the toggle set and \(A_j\) for source
letters; the meaning is unambiguous from the subscript.

Define

\[
 T^-:=\bigcup_{j=0}^{d+1}A_j,
 \qquad
 T^+:=\bigcup_{j=1}^{d+2}A_j,
 \tag{2.3}
\]

and

\[
 I:=\bigcup_{j=1}^{d+1}A_j,
 \qquad
 J:=\bigcup_{j=0}^{d+2}A_j.
 \tag{2.4}

### Theorem 2.1 (depth-raised promotion edge)

The packet (2.1)--(2.2) satisfies

\[
 \boxed{
 T^-=M\cup C\cup\{u,b^-\},\qquad
 T^+=M\cup C\cup\{u,b\}.}
 \tag{2.5}
\]

Hence \(T^-,T^+\) are rank-\(m\) Johnson neighbours, each witnessed by
an interval of length

\[
 L=d+2.
\]

Their lower and upper colours are both literal:

\[
 \boxed{
 I=T^-\cap T^+=M\cup C\cup\{u\},\qquad |I|=m-1,}
 \tag{2.6}
\]

on the length-\((L-1)=d+1\) overlap, and

\[
 \boxed{
 J=T^-\cup T^+=M\cup C\cup\{u,b^-,b\},\qquad |J|=m+1,}
 \tag{2.7}
\]

on the length-\((L+1)=d+3\) span.

At the endpoint \(d+1\), the final \(d-1\) and \(d\) source intervals
have values

\[
 \bigcup_{j=3}^{d+1}A_j=M,
 \qquad
 \bigcup_{j=2}^{d+1}A_j=U:=M\cup\{u\},
 \tag{2.8}
\]

while at the next endpoint \(d+2\), the final \(d\) source interval has
value

\[
 \bigcup_{j=3}^{d+2}A_j
 =Y:=M\cup C\cup\{b\}.
 \tag{2.9}
\]

Thus one literal history simultaneously supplies

\[
 M\subset U,qquad Y\subset T^+,
 \tag{2.10}
\]

the two adjacent rank-\(m\) owners, their exact rank-\((m-1)\)
intersection, and their exact rank-\((m+1)\) union.  It has no immediate
palette sidecar.

#### Proof

The source letters at positions \(3,\ldots,d+1\) have union

\[
 K\cup\{a_0,a_1,\ldots,a_{d-1}\}=M.
\]

Adding position \(2\) adds precisely \(u\), proving (2.8); replacing it
by the final position adds \(C\cup\{b\}\), proving (2.9).

The left length-\(L\) window contains \(K,C,A,u,b^-\), and the right one
contains \(K,C,A,u,b\), which proves (2.5).  Their overlap omits only
\(b^-\) and \(b\), while their span contains both.  Equations
(2.6)--(2.7) and the rank assertions follow. \(\square\)

### Corollary 2.2 (complete saturated lower piece)

For \(1\le\ell\le d-1\), the last \(\ell\) source letters ending at
position \(d+1\) have values

\[
 K\cup\{a_0,a_{d-\ell+1},\ldots,a_{d-1}\}.
 \tag{2.11}
\]

They form a strict saturated chain ending at \(M\).  Thus the packet
realizes one whole rephased SCD endpoint piece, not only its final flag.

## 3. The packet cannot occur at positive density

Let

\[
 W={2m+1\choose m}={2m+1\choose m+1}.
\]

A word of length

\[
 N=W+d+2
 \tag{3.1}
\]

has

\[
 N-(d+2)+1=W+1
 \tag{3.2}
\]

intervals of length \(d+2\), and exactly

\[
 N-(d+3)+1=W
 \tag{3.3}
\]

intervals of length \(d+3\).

The row counts show why a globally shifted architecture is numerically
possible, but the displayed packet has an additional local obstruction.
In its right owner, the first letter (C+a_0) is contained in the union
of the remaining (d+1) letters: (C) reappears in the terminal
(C+b), and (a_0) reappears in every internal letter.  Consequently
the length-\((d+2)\) windows starting at the first and second right-owner
positions have the same rank-(m) value.  They cannot witness two distinct
middle targets.

Selected incomparable rank-(m) witnesses in a length-(W+d+2) word use
(W) distinct left endpoints, leaving only (d+2) unused starts.  Every
occurrence-disjoint copy of this packet forces one such unused start.
Hence this exact packet can occur at most (d+2) times and cannot serve a
positive-density task bank.

The clean lag-two packet repairs the problem by making the coordinate
deleted at the next owner transition occur in a unique source position.

## 4. Exact middle-levels interpretation

Let

\[
 T_0,T_1,\ldots,T_W
 \tag{4.1}
\]

be the consecutive length-\((d+2)\) window values of a source word of
length \(N\).  Suppose that every \(T_i\) has rank \(m\), that

\[
 T_W=T_0,
 \tag{4.2}
\]

and that \(T_0,\ldots,T_{W-1}\) are all the rank-\(m\) sets exactly once.
Then the length-\((d+3)\) windows are

\[
 J_i=T_{i-1}\cup T_i\qquad(1\le i\le W).
 \tag{4.3}
\]

They are all the rank-\((m+1)\) sets exactly once precisely when

\[
 T_0,J_1,T_1,J_2,\ldots,J_W,T_W=T_0
 \tag{4.4}
\]

is a Hamilton cycle of the middle-levels incidence graph

\[
 { [2m+1]\choose m} cup { [2m+1]\choose m+1}.
\]

Thus the abstract middle/upper chronology required at \(B+2\) exists for
every \(m\) by the Middle Levels Theorem.  The missing assertion is that
one can choose such a Hamilton cycle with a literal depth-\((d+1)\)
antecedent containing the required promotion packets and lower compiler.

## 5. Conditional (B+2) theorem

### Theorem 5.1 (decorated resident middle-levels reduction)

Assume that a middle-levels Hamilton cycle (4.4) admits a linear opening
\(T_0,\ldots,T_W\) and a source word \(A\) of length \(W+d+2\) such
that:

1. its consecutive length-\((d+2)\) unions are exactly
   \(T_0,\ldots,T_W\);
2. its consecutive length-\((d+3)\) unions are exactly
   \(J_1,\ldots,J_W\);
3. its intervals of length at most \(d+1\) contain every nonempty target
   of rank below \(m\); and
4. its remaining intervals contain every target of rank above \(m+1\);
   and
5. the opened endpoints retain any required boundary witnesses.

Then

\[
 \boxed{\nu(2m+1)\le B(2m+1)+2.}
 \tag{5.1}
\]

#### Proof

Conditions 1--2 cover the entire two middle levels, condition 3 covers
every strict lower target, and condition 4 covers every remaining target.
The source length is \(W+d+2=B+2\). \(\square\)

Condition 4 is substantive: an ordinary middle-levels Hamilton cycle
alone controls only rank \(m+1\).  The complete decorated theorem must
preserve all higher interval unions as well.

## 6. Remaining theorem

The additive-constant problem is reduced, along this route, to a
**depth-raised decorated middle-levels theorem**:

> choose a middle-levels Hamilton cycle whose rank-\(m\) shore has a
> literal width-\((d+2)\) factor; plant the required positive-density bank
> of packets from Theorem 2.1 in that factor; cover the entire strict lower
> ideal on the shorter suffix cells; and retain all higher interval-union
> witnesses.

Theorem 2.1 is a correct local interval identity but is not the mass-scale
packet.  The corrected lag-two packet removes the local common-history,
q1-sidecar, immediate-upper-sidecar, and blocked-start obstructions.  Its
remaining condition is the global dynamic-cache/factor theorem stated in
the cited audit.
