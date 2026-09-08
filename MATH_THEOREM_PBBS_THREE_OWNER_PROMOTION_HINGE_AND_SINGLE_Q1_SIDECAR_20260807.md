# A three-owner PBBS hinge promotes a saturated upper flag with one sharp q1 sidecar

**Date:** 2026-08-07  \
**Status:** unconditional literal local promotion theorem.  It supplies the
promotion ticket missing from the native dense delayed-atom row.  Its only
local immediate-palette defect is one explicitly named predecessor lower
colour; global planting, sidecar routing, upper completion, and common-cap
compatibility remain open.

## 1. Parameters

Let \(d\ge2\), put \(q=d+1\), and choose pairwise disjoint data

\[
 M,\quad \{u,v\},\quad B^-\cup B
\]

such that

\[
 |M|=m-d-2,\qquad |B^-|=|B|=q,\qquad
 |B^-\cap B|=q-1=d.
\tag{1.1}
\]

Put

\[
 U=M\cup\{u\},\qquad
 Y=M\cup B,\qquad
 T=M\cup\{u\}\cup B.
\tag{1.2}
\]

Thus

\[
 |M|=m-d-2,\quad |U|=m-d-1,\quad |Y|=m-1,\quad |T|=m.
\]

Assume \(|M|\ge d-1\), which holds for all sufficiently large optimal
parameters.  Choose nonempty sets

\[
 K_1,\ldots,K_{d-1}\subseteq M,\qquad
 \bigcup_{i=1}^{d-1}K_i=M.
\tag{1.3}
\]

## 2. Literal source block

On positions \(-d-1,-d,\ldots,-1,0,1\), define

\[
 A_{-d-1}=B^-,
 \qquad A_{-d}=\{u\},
 \qquad A_{-d+i}=K_i\ (1\le i\le d-1),
\]

\[
 A_0=B,\qquad A_1=\{v\}.
\tag{2.1}
\]

For \(j\ge1\), write

\[
 Z_{e,j}=A_{e-j+1}\cup\cdots\cup A_e.
\tag{2.2}
\]

### Theorem 2.1 (exact promotion hinge)

The block (2.1) satisfies

\[
 \boxed{
 Z_{-1,d-1}=M,\quad
 Z_{-1,d}=U,\quad
 Z_{0,d}=Y,\quad
 Z_{0,d+1}=T.}
\tag{2.3}
\]

Its three consecutive length-\((d+1)\) owner windows are

\[
 T_-:=Z_{-1,d+1}=M\cup\{u\}\cup B^-,
\]

\[
 T_0:=Z_{0,d+1}=M\cup\{u\}\cup B,
\]

\[
 T_+:=Z_{1,d+1}=M\cup B\cup\{v\}.
\tag{2.4}
\]

They are distinct rank-\(m\) sets forming a simple Johnson path

\[
 T_-\longrightarrow T_0\longrightarrow T_+.
\tag{2.5}
\]

In particular, the middle occurrence realizes the saturated PBBS flag
\(M\subset U\), its successor coatom \(Y\), and its owner \(T\) in one
literal history.

#### Proof

Equations (2.3) follow immediately from (1.3) and (2.1).  Each set in
(2.4) has rank

\[
 (m-d-2)+1+(d+1)=m.
\]

The first step replaces the unique member of \(B^-\setminus B\) by the
unique member of \(B\setminus B^-\); the second replaces \(u\) by \(v\).
Thus both are Johnson edges, and disjointness of the displayed roles makes
the three owners distinct.  \(\square\)

### Corollary 2.2 (the whole saturated SCD piece is literal)

Let

\[
 L_1\subsetneq L_2\subsetneq\cdots\subsetneq L_{d-1}=M
\tag{2.6}
\]

be any strict chain.  Put \(L_0=\varnothing\) and choose

\[
 K_{d-\ell}=L_\ell\setminus L_{\ell-1}
 \qquad(1\le\ell\le d-1).
\tag{2.7}
\]

Then every \(K_i\) is nonempty, they have union \(M\), and

\[
 \boxed{Z_{-1,\ell}=L_\ell\qquad(1\le\ell\le d-1).}
\tag{2.8}
\]

Together with \(Z_{-1,d}=U\), the hinge realizes the entire saturated
length-\(d\) endpoint chain in one common source history.

#### Proof

The last \(\ell\) internal letters are

\[
 K_{d-\ell},K_{d-\ell+1},\ldots,K_{d-1}.
\]

Their differences telescope to \(L_\ell\).  The final statement is
Theorem 2.1.  \(\square\)

## 3. Exact immediate palettes

The set-theoretic lower and upper colours are

\[
 I_-:=T_-\cap T_0
   =M\cup\{u\}\cup(B^-\cap B),
\]

\[
 I_+:=T_0\cap T_+
   =M\cup B=Y,
\tag{3.1}
\]

and

\[
 J_-:=T_-\cup T_0
   =M\cup\{u\}\cup(B^-\cup B),
\]

\[
 J_+:=T_0\cup T_+
   =M\cup B\cup\{u,v\}.
\tag{3.2}
\]

All have the required ranks \(m-1,m+1\), respectively, and the two values
on each shore are distinct.

The native shared source cells are

\[
 C_-:=A_{-d}\cup\cdots\cup A_{-1}=U,
\qquad
 C_+:=A_{-d+1}\cup\cdots\cup A_0=Y.
\tag{3.3}
\]

Hence the successor edge is literally q1-tight:

\[
 C_+=I_+.
\tag{3.4}
\]

The predecessor edge has exactly one named sidecar:

\[
 I_-\setminus C_-=B^-\cap B,
\qquad |I_-\setminus C_-|=d.
\tag{3.5}
\]

### Theorem 3.1 (sharpness of the predecessor sidecar)

Suppose two distinct rank-\(m\) Johnson neighbours \(V_-,V_0\) share a
length-\(d\) source cell of value \(U\), where \(|U|=m-d-1\).  Then that
shared cell cannot equal \(V_-\cap V_0\).

More precisely,

\[
 |(V_-\cap V_0)\setminus U|=d.
\tag{3.6}
\]

#### Proof

Johnson neighbours of rank \(m\) have intersection rank \(m-1\).  The
shared source value \(U\) is contained in both owners and has rank
\(m-d-1\).  Subtraction gives (3.6).  Since \(d>0\), native q1 tightness is
impossible.  \(\square\)

Thus (3.5) is not a defect of the chosen banks.  Every saturated flag
transition of this form must export one predecessor lower-colour ticket.

## 4. Residence interface

Inside the three-owner path:

* every coordinate of \(M\) occurs in all three owners;
* \(u\) occurs in \(T_-,T_0\) and exits at the right boundary;
* \(v\) enters at the right boundary;
* the \(d\) coordinates in \(B^-\cap B\) occur in all three owners;
* the unique coordinate in \(B^-\setminus B\) occurs only at the left
  boundary; and
* the unique coordinate in \(B\setminus B^-\) occurs in \(T_0,T_+\) and
  exits through the right boundary of the displayed block.

Consequently every positive run shorter than \(d+1\) is clipped by one of
the two displayed boundaries.  There is no wholly internal short positive
run.  Extending the clipped runs is a collar obligation, not a local
residence obstruction.

The complete coordinate support has size

\[
 |M|+2+|B^-\cup B|=m+2,
\tag{4.1}
\]

so there is ample ambient coordinate room in \([2m+1]\).

## 5. Exact global interface

The hinge supplies one occurrence-labelled packet containing:

1. the saturated upper flag \(M\subset U\);
2. its fresh exterior \(B\);
3. the forced coatom--owner edge \(Y\subset T\);
4. a two-edge simple owner path with distinct set-theoretic q1 palettes;
5. a literal successor lower colour \(Y\); and
6. one named predecessor lower-colour sidecar \(I_-\).

A joint orbit/factor theorem may therefore start from this template rather
than from the native dense queue, whose compatible flag degree is zero.
The required global theorem must:

* plant a target-disjoint family of hinges;
* route every sidecar \(I_-\) to a separate legal occurrence;
* extend all clipped residence runs;
* complete the named upper decks and topology; and
* preserve one common lower compiler/cap.

The scalar reset bank has much more capacity than the rephased flag count,
but that scalar inequality does not prove the occurrence-labelled sidecar
matching.  This theorem proves the missing local promotion ticket, not the
global PBBS factor or \(\nu(k)\le B(k)+O(1)\).

## 6. One-longer-cell refinement: the sidecar becomes literal

The predecessor sidecar is forced only if every displayed owner occurrence
is restricted to source length \(d+1\).  Allowing the predecessor occurrence
to have source length \(d+2\) admits the following exact refinement.

Write

\[
 B^-=C\mathbin{\dot\cup}\{b^-\},\qquad
 B=C\mathbin{\dot\cup}\{b\},
\qquad |C|=d,
\tag{6.1}
\]

with \(b^-\ne b\).  Replace the first letter \(B^-\) of (2.1) by the two
consecutive letters

\[
 A_{-d-2}=\{b^-\},\qquad A_{-d-1}=C,
\tag{6.2}
\]

and retain

\[
 A_{-d}=\{u\},\quad
 A_{-d+i}=K_i\ (1\le i\le d-1),\quad
 A_0=B,\quad A_1=\{v\}.
\tag{6.3}
\]

### Theorem 6.1 (exact promotion staircase with one longer predecessor)

The source (6.2)--(6.3) has the following literal interval table:

\[
\begin{array}{c|c|c}
\text{interval}&\text{value}&\text{rank}\\ \hline
[-d-2,-1]&M\cup\{u\}\cup C\cup\{b^-\}=T_-&m\\
[-d-1,-1]&M\cup\{u\}\cup C=I_-&m-1\\
[-d,-1]&M\cup\{u\}=U&m-d-1\\
[-d+1,-1]&M&m-d-2\\
[-d+1,0]&M\cup C\cup\{b\}=Y&m-1\\
[-d,0]&M\cup\{u\}\cup C\cup\{b\}=T_0&m\\
[-d+1,1]&M\cup C\cup\{b,v\}=T_+&m.
\end{array}
\tag{6.4}
\]

Moreover,

\[
 T_-\cap T_0=I_-,
\qquad
 T_0\cap T_+=Y,
\tag{6.5}
\]

and both intersections occur at the displayed literal intervals.  The
two upper colours are also literal:

\[
 T_-\cup T_0=M\cup\{u\}\cup C\cup\{b^-,b\}
\]

on \([-d-2,0]\), and

\[
 T_0\cup T_+=M\cup C\cup\{b,u,v\}
\]

on \([-d,1]\).

Thus the packet simultaneously realizes:

* the saturated flag \(M\subset U\);
* the successor coatom--owner edge \(Y\subset T_0\);
* three simple rank-\(m\) owner witnesses;
* both rank-\((m-1)\) q1 colours; and
* both rank-\((m+1)\) q1 colours.

Its only nonstandard central cell is the predecessor owner \(T_-\), whose
source length is \(d+2\).  Every other displayed central or flag interval
has length at most \(d+1\).

#### Proof

Every row of (6.4) follows by taking the union of the displayed source
letters and using \(\bigcup_iK_i=M\).  Equations (6.5) follow from

\[
 T_-=M\cup\{u\}\cup C\cup\{b^-\},
\quad
 T_0=M\cup\{u\}\cup C\cup\{b\},
\]

\[
 T_+=M\cup C\cup\{b,v\}.
\]

Hence \(T_-\to T_0\) exchanges \(b^-\) for \(b\), while
\(T_0\to T_+\) exchanges \(u\) for \(v\).  The spanning interval of two
overlapping witnesses has union equal to the union of their values, which
gives the two upper rows.  \(\square\)

### Corollary 6.2 (exact scope of the longer predecessor)

The native maximal delayed-atom row cannot realize a saturated penultimate
flag, and a length-\((d+1)\)-only promotion hinge necessarily exports the
predecessor q1 sidecar by Theorem 3.1.  A length-\((d+2)\) predecessor
removes that sidecar completely through Theorem 6.1.

This does **not** by itself charge one extra physical word position.  At
length \(B(k)\), the rank-slack theorem restricts the selected
one-per-target middle witnesses to length at most \(d+1\); it does not
forbid incidental longer rank-\(m\) intervals.  Therefore Theorem 6.1 is
compatible with an exact-\(B(k)\) architecture if \(T_-\) is a reset or
duplicate occurrence whose target has another admissible selected witness.
If \(T_-\) must itself be the selected unique witness, then the longer
cell needs a separately priced slack mechanism.

The remaining task is global: plant a large occurrence-disjoint family of
these staircases, price or duplicate their \(T_-\) occurrences, extend the
clipped residence collars, and complete the upper/common-cap rows.
