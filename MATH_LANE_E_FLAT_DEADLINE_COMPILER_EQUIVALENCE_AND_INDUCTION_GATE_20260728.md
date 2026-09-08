# Lane E: the flat deadline compiler equivalence and the exact induction gate

Date: 2026-07-28

Method: pure mathematics only.  No computation, search, or probabilistic
existence argument is used.

## 0. Outcome

Let

\[
 r=\left\lceil\frac{k}{2}\right\rceil,\qquad
 W=\binom{k}{r},\qquad
 \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},
\]

and let \(d=d(k)\) be least with

\[
 \Lambda\le dW+\binom{d+1}{2}.
\tag{0.1}
\]

Thus the monotone-deadline theorem gives

\[
\nu(k)\ge B(k):=W+d.
\tag{0.2}
\]

We assume \(d\ge1\).  The cases \(d=0\) are the immediate middle-layer
cases and require no short-band compiler.

This note gives an exact deterministic upper compiler in the flat-central
normal form.  It is stronger than a sufficient Hall formulation: it is an
if and only if statement, and after its finite datum is supplied the word is
given by one explicit coordinatewise formula.

The datum consists of

1. an order \(T_0,\ldots,T_{W-1}\) of the rank-\(r\) layer; and
2. an injective assignment of every strict lower target to one physical
   interval of length at most \(d\).

There are three coordinatewise interval-hitting conditions and one upper
window condition.  They are necessary and sufficient for a length-\(B(k)\)
universal word with

\[
                         D^dA=T.
\tag{0.3}
\]

All exact certificates for \(11\le k\le14\) lie in this class.  The theorem
therefore captures their common deterministic architecture without imposing
Johnson adjacency, cyclic symmetry, cap two, rank-by-rank grading, or a
particular hitting core.

No all-\(k\) construction of the required datum is proved here.  Two naive
inductions fail for exact reasons:

* odd-to-even lifting can lower the deadline, so the old lower compiler
  cannot be duplicated;
* a single cyclic element order whose \(r\)-windows enumerate the middle
  layer requires \(k\mid W\), already false at \(k=14\).

The remaining equality theorem is consequently the banded pin-extension
statement BPE stated in Section 7.  Proving BPE in every dimension gives
\(\nu(k)=B(k)\) by an explicit compiler; disproving it would refute the
flat-central route, but not the unrestricted equality conjecture because
central flattening is not known to be forced at positive slack.

## 1. The short physical band

Put

\[
                         L=W+d
\]

and index word positions by \([0,L-1]\).  For a set word \(A\), write

\[
                         (D^sA)_j
 =\bigcup_{h=0}^{s}A_{j+h}.
\tag{1.0}
\]

A cell

\[
                         (s,j),\qquad
 0\le s<d,\quad 0\le j<L-s,
\]

denotes the physical interval

\[
                         I(s,j)=[j,j+s].
\]

Let

\[
 {\cal B}_{L,d}
 =\{(s,j):0\le s<d,\ 0\le j<L-s\}.
\tag{1.1}
\]

Its exact size is

\[
 \begin{aligned}
 |{\cal B}_{L,d}|
 &=\sum_{s=0}^{d-1}(L-s)\\
 &=dL-\binom d2\\
 &=dW+\binom{d+1}{2}\\
 &=\Lambda+\sigma,
 \end{aligned}
\tag{1.2}
\]

where

\[
                         \sigma
 =dW+\binom{d+1}{2}-\Lambda
\tag{1.3}
\]

is precisely the monotone-deadline slack.

The central row consists of the \(W\) intervals

\[
                         J_i=[i,i+d],
 \qquad 0\le i<W.
\tag{1.4}
\]

Every interval of length at most \(d\) is contained in some \(J_i\).
Every interval of length at least \(d+1\) contains some \(J_i\).  Both
statements include the two boundaries because \(L=W+d\).

## 2. Flat deadline data

Let

\[
 {\cal L}_{<r}
 =\{S\subseteq[k]:1\le |S|<r\}.
\]

A flat deadline datum is a pair \((T,\phi)\) with the following properties.

First,

\[
 T=(T_0,\ldots,T_{W-1})
\tag{2.1}
\]

is a permutation of \(\binom{[k]}r\).

Second,

\[
 \phi:{\cal L}_{<r}\longrightarrow{\cal B}_{L,d}
\tag{2.2}
\]

is injective.  Write

\[
 \phi(S)=(s_S,j_S),\qquad I_S=[j_S,j_S+s_S].
\tag{2.3}
\]

For a coordinate \(x\in[k]\), define its maximal legal position set

\[
 \boxed{
 Q_x(T,\phi)
 =[0,L-1]\setminus
 \left(
   \bigcup_{i:\,x\notin T_i}J_i
   \ \cup\
   \bigcup_{S:\,x\notin S}I_S
 \right).}
\tag{2.4}
\]

Thus a position is legal for \(x\) exactly when putting \(x\) there violates
neither a central equality nor an assigned lower equality.

The datum is called feasible when it satisfies:

\[
 J_i\cap Q_x\ne\varnothing
 \qquad(0\le i<W,\ x\in T_i);
\tag{F1}
\]

\[
 I_S\cap Q_x\ne\varnothing
 \qquad(S\in{\cal L}_{<r},\ x\in S);
\tag{F2}
\]

\[
 \bigcup_{x=1}^{k}Q_x=[0,L-1];
\tag{F3}
\]

and the upper-window condition

\[
 \left\{
   \bigcup_{h=a}^{b}T_h:
   0\le a\le b<W
 \right\}
 \supseteq
 \{U\subseteq[k]:|U|>r\}.
\tag{F4}
\]

Conditions (F1)--(F3) are coordinatewise and integral.  There is no
fractional assignment, rounding, or probabilistic choice hidden in them.

## 3. The exact compiler

### Theorem 3.1 (flat deadline compiler equivalence)

Fix a permutation \(T\) of the middle layer.

There is a nonzero word \(A=(A_0,\ldots,A_{L-1})\) such that

\[
                         (D^dA)_i=T_i
 \qquad(0\le i<W)
\tag{3.1}
\]

and every member of \({\cal L}_{<r}\) occurs as a short cell of \(A\) if
and only if there is an injective map \(\phi\) satisfying
(F1)--(F3).

When the datum is feasible, one valid word is the entrywise maximal word

\[
 \boxed{
                         A_p^{\max}
 =\{x\in[k]:p\in Q_x(T,\phi)\}.}
\tag{3.2}
\]

This word is universal if and only if (F4) also holds.  Consequently

\[
 \boxed{
 \text{a feasible datum satisfying (F4)}
 \quad\Longrightarrow\quad
 \nu(k)=B(k).}
\tag{3.3}
\]

Conversely, every universal word of length \(B(k)\) whose \(d\)-th row is a
permutation of the middle layer supplies such a feasible datum.

#### Proof

Assume first that \((T,\phi)\) satisfies (F1)--(F3), and define \(A\) by
(3.2).  Condition (F3) makes every entry nonempty.

Fix a central interval \(J_i\).  If \(x\notin T_i\), definition (2.4)
forbids \(x\) at every position of \(J_i\).  If \(x\in T_i\), (F1) puts
\(x\) at some legal position of \(J_i\).  Therefore

\[
                         \bigcup_{p\in J_i}A_p=T_i.
\tag{3.4}
\]

The same argument with \(I_S\) and (F2) gives

\[
                         \bigcup_{p\in I_S}A_p=S
 \qquad(S\in{\cal L}_{<r}).
\tag{3.5}
\]

Thus (3.1) holds and all lower targets occur.

For every \(q\ge0\) and \(0\le i<W-q\), associativity of union gives

\[
 \begin{aligned}
 (D^{d+q}A)_i
 &=D^q(D^dA)_i\\
 &=\bigcup_{h=0}^{q}T_{i+h}.
 \end{aligned}
\tag{3.6}
\]

Hence (F4) supplies every upper target, proving sufficiency and (3.3).

Conversely, suppose \(A\) is nonzero, satisfies (3.1), and covers every
lower target.  A lower target cannot have a witness interval of length
at least \(d+1\), because such an interval contains a central interval
\(J_i\), whose union has rank \(r\).  Choose one short witness \(I_S\) for
every lower \(S\).  Distinct targets have distinct witness cells, so these
choices define an injection \(\phi\).

Let

\[
                         H_x=\{p:x\in A_p\}.
\]

Every negative central or lower pin excludes \(H_x\) from its interval.
Thus

\[
                         H_x\subseteq Q_x(T,\phi).
\tag{3.7}
\]

Every positive pin is hit by \(H_x\), which proves (F1) and (F2).
Since the word is nonzero, \(\bigcup_xH_x=[0,L-1]\); (3.7) proves (F3).

Finally, a target of rank greater than \(r\) cannot occur in an interval of
length at most \(d\), because that interval is contained in a central
\(J_i\).  Every longer interval has the form used on the left side of
(3.6), so universality forces (F4).  This proves necessity. \(\square\)

### Corollary 3.2 (no separate residence or Hall ambiguity)

For a fixed \((T,\phi)\), conditions (F1)--(F3) are the complete physical
compatibility test.

In particular:

* (F1) includes the usual \(d\)-residence/factorability condition and also
  detects residence destroyed by lower pins;
* (F2) is the exact simultaneous positive-pin test, not a collection of
  one-target tests;
* (F3) is exactly the nonzero-entry condition.

An ordinary candidate graph or fractional Hall check is insufficient unless
it is proved to produce an injective \(\phi\) satisfying these three
conditions.  Conversely, once such a \(\phi\) is known, formula (3.2) is a
deterministic integral compiler.

## 4. Equality capacity is now literal

The injection \(\phi\) occupies exactly \(\Lambda\) cells of the band
\({\cal B}_{L,d}\).  By (1.2), exactly \(\sigma\) cells remain unused.
Thus the lower-bound slack identity is not merely a scalar check inside this
normal form: it is the exact omitted-cell ledger of the compiler.

No rank ordering of the occupied cells is assumed.  A rank-\(s\) target may
be assigned at any depth below \(d\) allowed by (F1)--(F3).  This is essential:
the exact \(k=11\) multirow word has eight rank-three targets in \(DA\),
and positive slack does not force a graded tableau.

The theorem also clarifies the role of the PCSH and sandwich-Hall
formulations.  They are useful sufficient ways of manufacturing a feasible
\(\phi\).  The object that is actually necessary and sufficient is the
finished injective pin table together with (F1)--(F3).

## 5. Audit against the exact cases \(k=11,12,13,14\)

The four recent exact words all have a flat central row, so Theorem 3.1
applies in both directions.

\[
\begin{array}{c|c|c|c|c|c}
k&r&W&d&\Lambda&\sigma\\ \hline
11&6&462&3&1023&369\\
12&6&924&2&1585&266\\
13&7&1716&3&4095&1059\\
14&7&3432&2&6475&392
\end{array}
\tag{5.1}
\]

For \(k=11\), \(D^3A\) is the complete rank-six layer.  One
translation-equivariant resident cycle, one safe cut, and the multirow
compiler give a feasible \(\phi\).

For \(k=12\), the stored length-926 word has \(D^2A\) equal to all 924
rank-six masks.  Its short rows cover the complete lower ideal, and its
longer rows cover the upper ideal.

For \(k=13\), two resident all-shadow cycles are cut and joined by one
shadow-safe seam.  The resulting \(D^3A\) is the complete rank-seven path,
and the flexible lower compiler supplies \(\phi\).

For \(k=14\), the six-piece two-shore braid produces the complete rank-seven
path with exact depth-two residence and all upper shadows.  The all-rank
lower compiler supplies \(\phi\).

Thus the common invariant is not a common cyclic factor or a common
rank-by-rank word profile.  It is exactly the existence of the datum
\((T,\phi)\).

## 6. Exact audit of direct induction

### 6.1 Odd to even: the two shores

Let \(k=2m+1\), \(r=m+1\), and adjoin a new coordinate \(x\).  The
rank-\(r\) layer on \([k]\cup\{x\}\) splits into two equal shores

\[
 {\cal A}=\binom{[k]}r,
\qquad
 {\cal B}=
 \left\{\{x\}\cup([k]\setminus P):
              P\in\binom{[k]}r\right\}.
\tag{6.1}
\]

Indeed,

\[
 W(k+1)=\binom{2m+2}{m+1}=2\binom{2m+1}{m+1}=2W(k).
\tag{6.2}
\]

Write

\[
 A(P)=P,\qquad B(Q)=\{x\}\cup([k]\setminus Q).
\]

The exact cross-shore formulas are

\[
 A(P)\cap B(Q)=P\setminus Q,
\tag{6.3}
\]

\[
A(P)\cup B(Q)
 =\{x\}\cup P\cup([k]\setminus Q).
\tag{6.4}
\]

More generally, an arbitrary window crossing from an \(A\)-segment
\(P_{-u},\ldots,P_0\) into a \(B\)-segment \(Q_1,\ldots,Q_v\) has the exact
port signatures

\[
 \begin{aligned}
 &\bigcup_{i=-u}^{0}A(P_i)
 \ \cup\
 \bigcup_{j=1}^{v}B(Q_j)\\
 &\qquad
 =\{x\}\cup
   \left(\bigcup_{i=-u}^{0}P_i\right)
   \cup
   \left([k]\setminus\bigcap_{j=1}^{v}Q_j\right),
 \end{aligned}
\tag{6.4a}
\]

and

\[
 \bigcap_{i=-u}^{0}A(P_i)
 \ \cap\
 \bigcap_{j=1}^{v}B(Q_j)
 =
 \left(\bigcap_{i=-u}^{0}P_i\right)
 \setminus
 \left(\bigcup_{j=1}^{v}Q_j\right).
\tag{6.4b}
\]

The reverse \(B\)-to-\(A\) formulas are identical after reversing the two
lists.  Hence every all-depth shadow created or destroyed by a shore braid
is determined by its finite prefix/suffix port tables.

In particular, a cross-shore seam is a Johnson edge precisely when

\[
 |P\cap Q|=1.
\tag{6.5}
\]

Thus every cross port obeys (6.3)--(6.4).  If the lifted chronology is
required to remain a Johnson path, its cross ports must additionally satisfy
(6.5).  Johnson adjacency is not a hypothesis of Theorem 3.1: a more general
induction may instead use a non-Johnson seam provided it retains (F1) and
(F4), and then constructs a new lower injection satisfying (F2)--(F3).
The \(k=14\) six-piece braid succeeds inside the stronger Johnson class.

The old lower compiler cannot simply be copied.  The deadline changes with
dimension and can decrease:

\[
 d(11)=3,\quad d(12)=2,\qquad
 d(13)=3,\quad d(14)=2.
\tag{6.6}
\]

An old assigned cell of depth two is legal at deadline three but is outside
the new short band when the deadline becomes two.  Therefore shore
duplication does not even define a candidate \(\phi\) in these two exact
lifts.  The lower pins must be reassigned after the braid.

This failure is forced by capacity, not by the displayed representatives.
At \(k=11\), the depth-zero and depth-one rows contain only

\[
                         465+464=929
\]

cells for 1,023 lower targets, so every \(\phi\) uses at least 94 depth-two
cells.  At \(k=13\), those two rows contain

\[
                         1719+1718=3437
\]

cells for 4,095 lower targets, so every \(\phi\) uses at least 658
depth-two cells.  Both populations become illegal after a literal
deadline-\(3\) to deadline-\(2\) copy.

### 6.2 Even to odd: no two-copy width identity

For \(k=2m\),

\[
 W(k+1)
 =\binom{2m+1}{m+1}
 =\frac{2m+1}{m+1}\binom{2m}{m}.
\tag{6.7}
\]

The multiplier is strictly between one and two and is not a two-shore
duplication.  A uniform induction must therefore use a genuine refinement or
quotient decomposition rather than concatenating two old central
chronologies.

### 6.3 No-go for one master cyclic element order

Consider the particularly attractive algebraic family

\[
 T_i=\{z_i,z_{i+1},\ldots,z_{i+r-1}\},
 \qquad i\in{\mathbb Z}_W,
\tag{6.8}
\]

where every displayed window has \(r\) distinct symbols and the \(T_i\)
enumerate \(\binom{[k]}r\).

### Proposition 6.1 (divisibility obstruction)

Any family (6.8) requires

\[
                         k\mid W.
\tag{6.9}
\]

#### Proof

Let \(n_x\) be the number of occurrences of coordinate \(x\) in the cyclic
word \(z\).  Every occurrence lies in exactly \(r\) of the windows (6.8).
On the other hand, \(x\) belongs to exactly

\[
                         \binom{k-1}{r-1}
                         =\frac{rW}{k}
\]

members of the middle layer.  Hence

\[
                         rn_x=\frac{rW}{k},
\qquad n_x=\frac Wk.
\]

This is integral for every \(x\), proving (6.9). \(\square\)

At \(k=14\),

\[
                         W=3432,\qquad 14\nmid3432.
\]

Therefore no single sliding master order can underlie an all-\(k\)
construction, even though such orders remain plausible on selected odd
dimensions.  The multi-piece \(k=14\) braid is not cosmetic: it leaves this
algebraic family.

## 7. The isolated all-\(k\) theorem

Define BPE\(_k\), the banded pin-extension statement, as follows.

> There is a permutation \(T\) of \(\binom{[k]}r\) and an injection
> \(\phi:{\cal L}_{<r}\to{\cal B}_{B(k),d(k)}\) satisfying
> (F1)--(F4).

### Theorem 7.1 (exact status of BPE)

\[
 \boxed{
 \mathrm{BPE}_k
 \quad\Longleftrightarrow\quad
 \begin{array}{c}
 \text{there is a universal word of length }B(k)\\
 \text{whose }d(k)\text{-th row is the middle layer}
 \end{array}.}
\tag{7.1}
\]

In particular,

\[
                         \mathrm{BPE}_k
 \quad\Longrightarrow\quad
                         \nu(k)=B(k).
\tag{7.2}
\]

#### Proof

This is exactly Theorem 3.1 with \(d=d(k)\), followed by the monotone-deadline
lower bound. \(\square\)

The implication cannot presently be reversed from the bare equality
\(\nu(k)=B(k)\), because positive slack does not force central flattening.
Thus BPE is the precise theorem for the direct OR-compiler lane, not a
restatement of the unrestricted conjecture.

An induction proof of BPE must preserve four named resources:

1. central ownership, namely that \(T\) is a permutation;
2. negative-pin legality, encoded in the sets \(Q_x\);
3. every positive central and lower hit, (F1)--(F2), plus nonzero positions
   (F3);
4. all upper consecutive-window targets, (F4).

The exact \(k=13\) and \(k=14\) certificates show that this interface permits
multiple carrier components, nontrivial splicing, and multi-piece shore
braids.  They do not yield a dimension-free rule producing the next
\(\phi\).  That pin-extension step is the first unresolved induction
interface.

## 8. Net lane-E conclusion

There is now a deterministic equality compiler with no rounding gap:

\[
                         (T,\phi)
 \longmapsto
                         A_p=\{x:p\in Q_x(T,\phi)\}.
\]

The lower-bound slack is exactly the number of unassigned short cells, and
upper coverage is exactly a consecutive-window property of \(T\).  The
general construction problem is therefore not to guess word entries.  It is
to construct one middle order and one band injection obeying four explicit
conditions.

The audited certificates prove BPE for \(k=11,12,13,14\).  A general proof
of BPE, possibly by a recursive two-shore braid followed by a fresh
pin-extension theorem, would prove \(\nu(k)=B(k)\).  The current mathematics
does not yet supply that extension theorem.
