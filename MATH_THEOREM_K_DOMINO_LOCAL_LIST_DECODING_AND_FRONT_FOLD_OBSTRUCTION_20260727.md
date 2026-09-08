# Domino-cell local list decoding: the isolated \(1/3\) theorem and the hereditary \(1/2\) front-fold obstruction

Date: 2026-07-27

Method: pure mathematics only. No web search, computation, finite search,
solver, or probabilistic black box is used.

## 0. Outcome

Put

\[
n=2m,\qquad R=2r+1,\qquad h=m-2r>0,\qquad K=4m.
\tag{0.1}
\]

All finite statements below assume \(2\le r<m/2\). In the asymptotic
annular statements we additionally have \(h=o(m)\), so
\(r=(1/2-o(1))m\).

A simple domino-twin packet is encoded by a cyclic list of unordered
dominoes \(B_i\), \(i\in\mathbb Z_m\). Its support is the disjoint union
of the four-target cells

\[
\mathcal S_i
=\{A_i\cup\{x\}:x\in B_{i-1}\cup B_{i+r}\},
\qquad
A_i=\bigcup_{j=i}^{i+r-1}B_j.
\tag{0.2}
\]

The proposed hereditary local-list estimate with exponent \(c\le1/3\)
is false. The exact conclusions are these.

1. A genuine star-to-top shared edge is not the obstruction at close
   overlap. If one \(F\)-cell has a two-target intersection split across
   two owner cells of a \(G\)-top, then

   \[
   |F\setminus G|\ge4r=2(R-1).
   \tag{0.3}
   \]

   Thus, in the annular regime, no such split occurs when
   \(|F\setminus G|=o(m)\).

2. For one isolated contiguous segment, the desired \(1/3\) decoder is
   valid. If \(G\) is obtained by repartitioning the fixed labels in one
   segment and fixing every outside domino, then, in the close regime,

   \[
   \#\{G:|F\setminus G|\le s\}
   \le
   2^\ell\,{(2\lfloor s/6\rfloor+2)!\over
                    2^{\lfloor s/6\rfloor+1}}
   \le \exp(O(m))\,n^{s/3}.
   \tag{0.4}
   \]

   The two fronts of each nontrivial prefix discrepancy pay six missing
   targets.

3. The isolated theorem is not hereditary. Choose two length-\(\ell\)
   segments at displacement \(r\), and independently repartition their
   two fixed label pools. If

   \[
   h\le\ell,\qquad \ell+h<r,
   \tag{0.5}
   \]

   then every resulting packet satisfies

   \[
   |F\setminus G|\le8\ell+4h,
   \tag{0.6}
   \]

   while the number of distinct simple supports is at least

   \[
   {1\over2m}\left({(2\ell)!\over2^\ell}\right)^2.
   \tag{0.7}
   \]

   More strongly, one fixed exact missing-target trace is shared by at
   least

   \[
   \left\lfloor
   {1\over 2m\,2^{\,4(2\ell+h)}}
   \left({(2\ell)!\over2^\ell}\right)^2
   \right\rfloor
   \tag{0.8}
   \]

   distinct packets.

4. If \(h=o(\ell)\), \(\ell=o(m)\),
   \(m=o(\ell\log m)\), and
   \(\log\ell/\log m\to1\), then (0.6)--(0.8) force every uniform bound

   \[
   \#\{G:|F\cap G|\ge K-s\}
   \le \exp(O(m))\,n^{cs}
   \tag{0.9}
   \]

   to have

   \[
   \boxed{c\ge\frac12.}
   \tag{0.10}
   \]

   In the Gaussian and one-baseline annular regimes one may take
   \(\ell=\lfloor m/\sqrt{\log m}\rfloor\).

The reason is exact. Two independently free domino positions carry two
\(\log n\)-scale label choices each: pairing and ordering. Four missing
targets per free domino therefore pay exponent \(1/2\), not \(1/3\).
The \(1/3\) target would require six separately charged missing targets
per freely repartitioned domino. At displacement \(r\), the required
fronts are the same physical cells.

## 1. Intrinsic cell recovery

The normal form (0.2) has two facts used below.

We also use the audited intrinsic clique classification: every Johnson
edge and triangle induced by a simple domino packet lies in a canonical
star quartet or a canonical top quartet.

### Lemma 1.1 (support recovery)

The simple support determines its unordered domino partition and its
cyclic domino order up to one global rotation or reflection. Thus a
simple support has at most \(2m\) anchored domino-list presentations.

#### Proof

The exact clique classification distinguishes the canonical star
\(K_4\)'s from the canonical top \(K_4\)'s: a star cell has intersection
of size \(R-1\) and union of size \(R+3\), whereas a top has union of
size \(R+1\). Hence the \(m\) cores \(A_i\) are intrinsic.

Because \(r<m/2\), two cores have symmetric difference four exactly
when their indices are adjacent in the cyclic core order. This recovers
the core cycle up to dihedral symmetry. Once it is oriented,

\[
B_i=A_i\setminus A_{i+1}.
\tag{1.1}
\]

Thus the unordered blocks and their cyclic order are recovered. There
are at most \(2m\) choices of anchor and orientation. \(\square\)

### Lemma 1.2 (cell intersection types)

Let

\[
S(A,Q)=\{A+x:x\in Q\}
\]

be a star cell. Two common vertices of \(S(A,Q)\) and another star
force the two star cores to be equal. A top

\[
T(U,P)=\{U-y:y\in P\}
\]

meets \(S(A,Q)\) in at most two vertices. Equality two holds precisely
when

\[
A\subset U,\qquad
U\setminus A=\{x,y\}\subseteq Q\cap P.
\tag{1.2}
\]

Three vertices of one star can never form a top triangle.

#### Proof

Two distinct vertices \(A+x,A+y\) have intersection \(A\), so if they
belong to one other star its core is \(A\). If both equal top vertices,
say \(U-u,U-v\), their intersection is \(U\setminus\{u,v\}\), proving
(1.2); a third top vertex has a different triple intersection.
Equivalently, a star triangle has intersection size \(R-1\) and union
size \(R+2\), whereas a top triangle has intersection size \(R-2\) and
union size \(R+1\). \(\square\)

## 2. Split star-to-top edges are necessarily macroscopic

Write the dominoes of \(G\) as \(C_j\), and put

\[
d_i=4-|\mathcal S_i(F)\cap G|,
\qquad
s=\sum_i d_i=|F\setminus G|.
\tag{2.1}
\]

### Theorem 2.1 (split-top quarantine)

If some \(F\)-cell has two common targets lying in two distinct
\(G\)-star owner cells of one canonical \(G\)-top, then

\[
s\ge4r.
\tag{2.2}
\]

#### Proof

Write that top as

\[
U_j=C_j\cup C_{j+1}\cup\cdots\cup C_{j+r}.
\]

By Lemma 1.2 the split \(F\)-core has the form

\[
A_i^F=U_j\setminus\{x,y\},
\qquad x\in C_j,\quad y\in C_{j+r}.
\tag{2.3}
\]

Thus it contains all \(r-1\) internal \(G\)-dominoes and one singleton
from each endpoint domino.

Every \(F\)-cell with \(d_k\le1\) contains a common star triangle.
By Lemma 1.2 it lies in one \(G\)-star cell, whose core is \(A_k^F\).
Distinct \(F\)-cells give distinct \(G\)-star cells, since the
\(F\)-cells are disjoint and two disjoint triples cannot lie in one
four-set.

Now \(A_i^F\cap A_k^F\) has even size because both sets are unions of
\(F\)-dominoes. On the other hand, \(A_k^F\) is a length-\(r\) window
of \(G\)-dominoes. In its intersection with (2.3), every internal
\(G\)-domino contributes zero modulo two, while each included endpoint
domino contributes one. A length-\(r\) block window cannot contain both
\(C_j\) and \(C_{j+r}\). Even parity therefore forces it to contain
neither.

Each fixed \(G\)-domino belongs to exactly \(r\) length-\(r\) windows,
and no such window contains both endpoint dominoes. Exactly

\[
m-2r=h
\tag{2.4}
\]

windows avoid both. Hence at most \(h\) cells have \(d_k\le1\). The
other \(m-h=2r\) cells have \(d_k\ge2\), and (2.2) follows. \(\square\)

In the annular regime \(h=o(m)\), split-top ambiguity is absent whenever
\(s=o(m)\).
After the existing global dihedral alignment, every cell having at
least two survivors is then a same-core star cell. This validates the
ordinary two-front decoder locally; it does not validate hereditary
addition of its two charges.

### Lemma 2.2 (generic \(r\)-paired bad-set constraint)

Assume the complete common cells have been globally aligned. Let

\[
J=\{i:\mathcal S_i(F)\text{ is not a complete common cell}\},
\qquad
Q=\{j:B_j(F)\ne B_j(G)\}.
\tag{2.5}
\]

Then

\[
\boxed{
Q\subseteq
(J\cup(J-1))\cap(J+r\cup(J+r-1)).
}
\tag{2.6}
\]

Thus a changed domino position must be covered by two bad-cell collars,
one near that position and one near its translate by \(-r\). Moreover
\(|J|\le |F\setminus G|\), since every index in \(J\) has positive
cell deficit.

#### Proof

If cells \(j,j+1\) are both complete and common, equality of their cores
recovers

\[
B_j=A_j\setminus A_{j+1}.
\]

Hence a changed \(B_j\) forces \(j\in J\) or \(j+1\in J\), which is the
first factor on the right of (2.6). Likewise, if cells
\(j-r,j-r+1\) are both complete and common, then

\[
B_j=A_{j-r+1}\setminus A_{j-r}.
\]

Thus a changed \(B_j\) also forces \(j-r\in J\) or
\(j-r+1\in J\), giving the second factor. \(\square\)

### Sharpness at macroscopic deficiency

The quarantine scale is asymptotically sharp. Let

\[
C_i=\{a_i,b_i\},
\qquad
B_i=\{b_i,a_{i+1}\}
\tag{2.7}
\]

with cyclic indices. Then

\[
A_i^F
=\{b_i\}\cup\bigcup_{t=i+1}^{i+r-1}C_t
\cup\{a_{i+r}\}.
\tag{2.8}
\]

Of the four targets in the \(i\)-th \(F\)-cell, exactly

\[
A_i^F+a_i=U_i^G-b_{i+r},
\qquad
A_i^F+b_{i+r}=U_i^G-a_i
\tag{2.9}
\]

belong to \(G\). Each of the other two has \(r-1\) full
\(G\)-dominoes and three singleton \(G\)-dominoes, so it is not in the
domino-cell normal form. Therefore

\[
|F\cap G|=2m,\qquad |F\setminus G|=2m,
\tag{2.10}
\]

and all \(m\) dominoes are changed. Thus an unconditional
four-missing-target charge is itself false; the close-regime quarantine
in Theorem 2.1 is essential.

## 3. Exact normal form for one contiguous bad segment

Fix a segment

\[
I_a=\{a,a+1,\ldots,a+\ell-1\},
\qquad \ell<r,
\tag{3.1}
\]

and repartition its fixed \(2\ell\)-label union into an ordered list of
\(\ell\) unordered dominoes. Every outside domino remains fixed.

For \(1\le t\le\ell-1\), let \(P_t\) and \(P'_t\) be the unions of the
first \(t\) old and new dominoes of the segment, and put

\[
D=\{t:P_t\ne P'_t\}.
\tag{3.2}
\]

### Lemma 3.1 (two fronts and two collars)

The core-mismatch starts are exactly

\[
(a+D)\,\dot\cup\,(a-r+D).
\tag{3.3}
\]

All possibly changed cells lie in

\[
T_a=[a+1,a+\ell]\cup[a-r,a+\ell-1-r].
\tag{3.4}
\]

The open parts of the two intervals in (3.4) are the two core fronts;
the extra endpoints \(a+\ell\) and \(a-r\) are the two boundary
collars.

#### Proof

The core starting at \(a+t\) contains the suffix of the segment after
cut \(t\), while the core starting at \(a-r+t\) contains its prefix.
Since the full segment union is fixed, either core is unchanged exactly
when \(P_t=P'_t\). Every other core contains the entire segment or
avoids it. A cell with such an unchanged core can still change only
when one of its boundary dominoes is an endpoint domino of the segment,
which gives precisely \(a+\ell\) and \(a-r\). \(\square\)

### Theorem 3.2 (isolated \(1/3\) list decoder)

Assume \(s<4r\). Among the packets obtained by the one-segment operation,

\[
\#\{G:|F\setminus G|\le s\}
\le
2^{\ell-1}N_{\lfloor s/6\rfloor+1},
\qquad
N_u:={(2u)!\over2^u}.
\tag{3.5}
\]

Consequently this class satisfies an inverse bound with exponent
\(c=1/3\), up to an \(\exp(O(m))\) prefactor.

#### Proof

By Theorem 2.1 no shared pair of vertices is a split top. In this
one-segment class, an \(F\)-core which is also a \(G\)-core has the same
cyclic index. Indeed, the symmetric difference of two distinct
length-\(r\) position windows cannot be contained in a contiguous
segment of length \(\ell<r\): if the windows overlap, their two boundary
difference intervals contain a pair of positions at cyclic distance
\(r\); if they are disjoint, the difference contains a whole
length-\(r\) window. At least one outside fixed domino would therefore
have opposite membership in the two cores, and its two labels cannot be
supplied by the disjoint segment pool. Hence every core mismatch in
(3.3) leaves at most one target of its \(F\)-cell in \(G\). The two
front sets are disjoint, so

\[
|F\setminus G|\ge6|D|.
\tag{3.6}
\]

It remains to count the repartitions with \(|D|=u\). The equality cuts
\(P_t=P'_t\), together with the two endpoint cuts, split the segment
into blocks. If the non-singleton block lengths are
\(L_1,\ldots,L_b\ge2\), then

\[
\sum_{j=1}^b(L_j-1)=u.
\tag{3.7}
\]

For fixed equality cuts there are at most
\(\prod_jN_{L_j}\) ordered pairings. For \(a,b\ge2\),

\[
{N_{a+b-1}\over N_aN_b}
={2(2a+2b-2)!\over(2a)!(2b)!}\ge1;
\tag{3.8}
\]

the ratio is minimized at \(a=b=2\), where it is \(5/2\), and increases
in either variable. Repeated merging in (3.8) gives

\[
\prod_jN_{L_j}\le N_{u+1}.
\tag{3.9}
\]

There are at most \(2^{\ell-1}\) choices of equality cuts. Combining
(3.6)--(3.9) proves (3.5). Finally

\[
N_{\lfloor s/6\rfloor+1}
\le (2m)^{\,2\lfloor s/6\rfloor+2},
\]

and the additive power two is absorbed by \(\exp(O(m))\), proving the
\(1/3\) statement. \(\square\)

This theorem identifies exactly why the original \(1/3\) argument looked
available: each nontrivial prefix cut has two physically distinct
fronts, and each mismatched-core cell loses at least three targets.

## 4. Two segments fold four fronts into two

Now choose

\[
I_0=[0,\ell-1],
\qquad
I_r=[r,r+\ell-1],
\tag{4.1}
\]

under (0.5), and repartition the two label pools independently.

For a segment \(I_a\), Lemma 3.1 gives the fixed incidence quarantine

\[
T_a=[a+1,a+\ell]\cup[a-r,a+\ell-1-r].
\tag{4.2}
\]

Using \(m=2r+h\),

\[
T_0=[1,\ell]\cup[r+h,r+h+\ell-1],
\tag{4.3}
\]

\[
T_r=[r+1,r+\ell]\cup[0,\ell-1].
\tag{4.4}
\]

Since \(\ell\ge h\), the two remote intervals overlap, and (0.5) keeps
the following two pieces disjoint and away from wraparound:

\[
T_0\cup T_r
=[0,\ell]\,\dot\cup\,[r+1,r+h+\ell-1].
\tag{4.5}
\]

Therefore

\[
|T_0\cup T_r|=2\ell+h.
\tag{4.6}
\]

One nominal front is identical in the two segments. The remaining two
fronts are shifted by only \(h=m-2r\) and overlap in all but an
\(h\)-collar.

### Theorem 4.1 (exact-trace front-fold obstruction)

There are at least (0.7) distinct simple packets \(G\) satisfying
(0.6). Moreover there is one fixed set \(Z\subseteq F\),
\(|Z|\le8\ell+4h\), for which at least (0.8) of these packets satisfy

\[
F\setminus G=Z.
\tag{4.7}
\]

#### Proof

Every cell outside (4.5) is literally unchanged: its core contains all
or none of each modified label pool and its two boundary dominoes are
fixed. Since the \(F\)-cells are disjoint,

\[
|F\setminus G|
\le4|T_0\cup T_r|=8\ell+4h.
\tag{4.8}
\]

One segment has exactly

\[
N_\ell={(2\ell)!\over2^\ell}
\tag{4.9}
\]

ordered lists of unordered pairs. The two choices are independent.
Lemma 1.1 shows that at most \(2m\) presentations yield one simple
support, proving (0.7).

All missing targets lie in the fixed union of the \(2\ell+h\) cells in
(4.5), which contains \(4(2\ell+h)\) targets. Hence there are at most
\(2^{4(2\ell+h)}\) exact missing-target traces. Pigeonholing the
distinct supports proves (0.8). \(\square\)

The conditioning in (4.7) is stronger than knowledge of the maximal
bad segments, the survivor counts in each cell, or the two fixed label
pools. Thus this is a literal local-list obstruction, not merely a
large coarse conflict neighbourhood.

## 5. Entropy normalization and the exponent \(1/2\)

The one-segment factor has the exact decomposition

\[
{(2\ell)!\over2^\ell}
=(2\ell-1)!!\,\ell!.
\tag{5.1}
\]

The perfect-matching/repartition term and the ordering term each
contribute

\[
(1+o(1))\ell\log\ell.
\tag{5.2}
\]

Internal orientations have already been quotiented. Thus two segments
have entropy

\[
\log\left[{1\over2m}
\left({(2\ell)!\over2^\ell}\right)^2\right]
=4\ell\log\ell+O(\ell+\log m).
\tag{5.3}
\]

The exact-trace pigeonhole in (0.8) subtracts only \(O(\ell+h)\), so it
has the same leading entropy.

Suppose

\[
h=o(\ell),\qquad \ell=o(m),\qquad
m=o(\ell\log m),\qquad
{\log\ell\over\log m}\longrightarrow1.
\tag{5.4}
\]

Then \(s=8\ell+4h=o(m)\), while

\[
\log |\mathcal L_s(F)|=(4+o(1))\ell\log m,
\qquad
s\log n=(8+o(1))\ell\log m.
\tag{5.5}
\]

The term \(O(m)\) in (0.9) is negligible by (5.4). Dividing (0.9) by
\(\ell\log m\) gives \(4\le8c\), proving (0.10).

For example, if \(h=O(\sqrt{m\log m})\), take

\[
\ell=\left\lfloor {m\over\sqrt{\log m}}\right\rfloor.
\tag{5.6}
\]

All hypotheses hold.

Equivalently, the family has \(f=2\ell\) freely repartitioned domino
positions,

\[
|F\setminus G|\le(4+o(1))f,
\qquad
\log\#G=(2+o(1))f\log n.
\tag{5.7}
\]

Thus a four-hole charge pays \(2/4=1/2\). A \(1/3\) list exponent would
need a six-hole charge, exactly the charge supplied by Theorem 3.2
before the two fronts are folded together.

## 6. Correction to the earlier effective-coefficient formula

The long-segment obstruction in
MATH_OBSTRUCTION_GLOBALLY_ALIGNED_DOUBLE_SEGMENT_DOMINO_ENTROPY_20260727.md
is sound. Its displayed effective coefficient omits one normalization
factor away from the long regime. For segment length \(\ell\), the
coefficient relative to a bound with base \(m\) is

\[
c_{\ell,m}
= {\log\ell\over\log m}\,
  {1\over 2+\min\{1,h/\ell\}}+o(1),
\tag{6.1}
\]

not merely the second factor. Consequently a short segment
\(\ell=m^{\alpha+o(1)}\le h\) gives the lower calibration
\(\alpha/3\), not \(1/3\). For the decisive choice (5.6), however,
\(\log\ell/\log m\to1\), so the conclusion \(c\ge1/2\) is unchanged.

## 7. Exact implication boundary

Proved:

1. the exact star/star versus star/top cell-intersection classification;
2. the macroscopic lower bound \(s\ge4r\) for any genuine split-top
   coincidence;
3. the exact core-mismatch two-front/two-collar normal form for one
   contiguous segment;
4. a literal \(c=1/3\) list decoder for one isolated segment;
5. the exact \(r\)-displaced front-fold identity
   \(|T_0\cup T_r|=2\ell+h\);
6. a two-segment family of size (0.7) with deficiency (0.6);
7. the stronger exact-missing-trace list lower bound (0.8); and
8. failure of every uniform static inverse estimate with \(c<1/2\),
   including the proposed \(c\le1/3\) theorem.

Not proved or refuted:

1. a trajectory-dependent theorem showing that the two independent
   segment repartitions cannot survive simultaneously in the same
   stopped residual link;
2. a terminal-scale estimate at one fixed \(s=Cm/\log m\) with its
   additive exponential constant made explicit; or
3. a joint colouring/quotient which treats each \(r\)-paired front-fold
   cluster as one object rather than paying for its packets separately.

Hence the static local-list lane is closed at the survivor threshold.
The remaining annular escape must use dynamic trajectory information or
cluster the \(r\)-paired front folds; removing star-to-top coincidences
does not restore a strict exponent below \(1/2\).
