# The whole-job price inequality closes through depth three; Pascal induction exits the middle strip

**Date:** 2026-08-07  
**Status:** unconditional exact tail reduction, unconditional Pascal
recurrence, and unconditional proof of \(FC_D\) for every actual binomial
instance with \(D\le3\).  No all-depth \(FC_D\) theorem and no actual
binomial counterexample are claimed.

## 1. Exact retained histogram and price margin

Let

\[
 W={k\choose r},\qquad t=r-D,
 \tag{1.1}
\]

where \(r\) is the chosen middle owner rank.  Let \(\beta_s\) targets be
deleted at rank \(s<t\), and put

\[
 n_s={k\choose s}-\beta_s,qquad n_0=0.
 \tag{1.2}
\]

Assume \((n_s)_{1\le s<t}\) is nondecreasing.  Its canonical horizontal
jobs born at rank \(b\) have length \(t-b\) and multiplicity

\[
                         j_{t-b}=n_b-n_{b-1}.
 \tag{1.3}
\]

The old collar tails are

\[
 K_q=W-{k\choose t+q-1}\quad(1\le q\le D),
 \qquad K_q=0\quad(q>D).
 \tag{1.4}
\]

For a nonnegative tail-price vector \(\lambda\), put

\[
 c_u=\sum_{q=1}^u\lambda_q
 \tag{1.5}
\]

and let \(\psi(L)\) be the minimum cost of partitioning a length-\(L\)
job into positive pieces of size at most \(D\), with a size-\(u\) piece
costing \(c_u\).  Thus \(\psi(0)=0\), \(\psi\) is nondecreasing and
subadditive, and

\[
                         a_q:=\psi(q)-\psi(q-1)\ge0.
 \tag{1.6}
\]

Replacing the raw table \((c_u)\) by its covering closure
\((\psi(u))_{u\le D}\) leaves every job cost unchanged and can only lower
the supply price.  It is therefore enough to test closed tables.

### Proposition 1.1 (exact signed-tail form)

The supply price minus the cheapest whole-job price is

\[
 \boxed{
 \mathfrak F_{k,r,t,\beta}(\psi)
 =\sum_{q\ge1}\Gamma_{k,r,t,\beta}(q)a_q,}
 \tag{1.7}
\]

where

\[
 \Gamma_{k,r,t,\beta}(q)
 =K_q-n_{t-q}
 =\mathbf1_{q\le D}
    \left(W-{k\choose t+q-1}\right)
   -{k\choose t-q}+\beta_{t-q}.
 \tag{1.8}
\]

Binomial coefficients and \(\beta_s\) outside their declared ranges are
zero.  In particular

\[
 \boxed{
 \mathfrak F_{\beta}(\psi)
 =\mathfrak F_{0}(\psi)
   +\sum_{s<t}\beta_s
       \bigl(\psi(t-s)-\psi(t-s-1)\bigr).}
 \tag{1.9}
\]

Thus every boundary deletion weakly improves every fixed covering-price
inequality.  Its **rank profile**, not its target names, determines the
amount of improvement.

#### Proof

The number of canonical jobs of length at least \(q\) is the height of
column \(t-q\), namely \(n_{t-q}\).  Summation by parts gives

\[
 \sum_Lj_L\psi(L)=\sum_{q\ge1}n_{t-q}a_q.
 \tag{1.10}
\]

Likewise, the number of sockets of capacity at least \(q\) is \(K_q\), so
their price is \(\sum_qK_qa_q\).  Subtraction proves (1.7)--(1.8), and
isolating \(\beta_{t-q}\) gives (1.9).  \(\square\)

For the packet boundary, \(\sum_s\beta_s=h\) and
\(\beta_s=0\) above \(D\).  Formula (1.9) explains exactly why target-level
arbitrary-deletion uniformity does not itself prove \(FC_D\): the repair is
weighted by selected long-distance increments \(a_{t-s}\), not merely by
the scalar \(h\).

## 2. Exact Pascal recurrence and its closure failure

Suppress \(\beta\) temporarily and write

\[
 \Gamma^{(k,r,t)}(q)=
 \mathbf1_{q\le r-t}
 \left({k\choose r}-{k\choose t+q-1}\right)
 -{k\choose t-q}.
 \tag{2.1}
\]

### Theorem 2.1 (Pascal splitting)

For every \(k,r,t,q\),

\[
 \boxed{
 \Gamma^{(k,r,t)}(q)
 =\Gamma^{(k-1,r,t)}(q)
  +\Gamma^{(k-1,r-1,t-1)}(q).}
 \tag{2.2}
\]

Both children have the same formal depth \(D=r-t\).  Consequently, for
every fixed price \(\psi\), the complete-histogram dual margin has the same
additive recurrence.

If a named deletion family is split according as its members avoid or
contain the last coordinate, so that

\[
                         \beta_s=\beta^0_s+\beta^1_{s-1},
 \tag{2.3}
\]

then the retained margins satisfy the identical recurrence with
\(\beta^0\) and \(\beta^1\) on the two children.

#### Proof

For \(q\le D\), apply Pascal separately to the owner, upper-collar, and
job binomial coefficients:

\[
\begin{aligned}
 {k\choose r}&={k-1\choose r}+{k-1\choose r-1},\\
 {k\choose t+q-1}
  &={k-1\choose t+q-1}+{k-1\choose t+q-2},\\
 {k\choose t-q}
  &={k-1\choose t-q}+{k-1\choose t-q-1}.
\end{aligned}
 \tag{2.4}
\]

These are exactly the two terms in (2.2).  For \(q>D\), every socket term
is zero and the last identity alone proves the recurrence.  Equation (2.3)
does the same for the deletion correction.  \(\square\)

This is a genuine Pascal induction, but the physical middle-rank class is
not closed under repeated descent.  Starting with an odd upper-middle
instance

\[
 k=2m+1,\qquad r=m+1,qquad t=r-D,
 \tag{2.5}
\]

the first child in (2.2) has parameters \((2m,m+1,t)\).  Its formal last
socket tail is

\[
 {2m\choose m+1}-{2m\choose t+D-1}
 ={2m\choose m+1}-{2m\choose m}<0.
 \tag{2.6}
\]

It is therefore not a physical collar instance.  A one-line induction
which proves both children separately cannot work.  Any successful Pascal
proof must keep the off-middle children coupled so that their negative
terminal rows cancel; (2.2) identifies that exact missing coupled
invariant.

## 3. Covering prices at depths one and two

At depth one, every closed price is a multiple of the linear volume price.
At depth two, write the closed table as

\[
 (c_1,c_2)=(a,a+b),
 \qquad a\ge0,\quad0\le b\le a.
 \tag{3.1}
\]

For every job length, the same min-plus formula is linear on this cone.
The cone has the two rays

\[
 (a,b)=(1,0),\qquad(1,1),
 \tag{3.2}
\]

whose covering closures are respectively

\[
                         \left\lceil{L\over2}\right\rceil,
 \qquad L.
 \tag{3.3}
\]

Thus \(FC_2\) is equivalent to the minimum-piece and volume inequalities.

For the actual optimal-depth instances, their exact margins are:

\[
\begin{array}{c|rrrrrrr}
 k&5&7&8&9&10&12&14\\ \hline
 \lceil L/2\rceil&5&7&34&7&87&197&338\\
 L&5&7&48&0&119&263&389
\end{array}
 \tag{3.4}
\]

The optimal-depth lists here are

\[
 D=1:\ \{3,4,6\},
 \qquad
 D=2:\ \{5,7,8,9,10,12,14\}.
 \tag{3.5}
\]

Here and below an entry is supply price minus job price.  The positive
boundary at \(k=9\) uses the left-filled profile
\((\beta_1,\beta_2)=(2,1)\).  Depth one is immediate from volume; at its
only positive boundary, \(k=6\), both sides equal five.

## 4. Complete depth-three price fan

Let a closed depth-three price table have successive increments

\[
 (c_1,c_2,c_3)=(a,a+b,a+b+c).
 \tag{4.1}
\]

Closedness is exactly

\[
                         a\ge0,qquad0\le b\le a,
                         \qquad0\le c\le a.
 \tag{4.2}
\]

Indeed, these are monotonicity together with
\(c_2\le2c_1\) and \(c_3\le c_1+c_2\).

There are three min-plus regions.

1. If \(c\le b\), size three is the cheapest density and a residue one is
   paid by one singleton.
2. If \(b\le c\le(a+b)/2\), size three is still cheapest, but a residue
   one is paid by two size-two pieces.
3. If \(2c\ge a+b\), size two is cheapest, and every odd length at least
   three uses one size-three piece.

In each region every \(\psi(L)\) is linear in \((a,b,c)\).  The respective
cones have extreme rays

\[
\begin{array}{c|c}
 c\le b&(1,0,0),(1,1,0),(1,1,1)\\
 b\le c\le(a+b)/2&(1,0,0),(2,0,1),(1,1,1)\\
 2c\ge a+b&(2,0,1),(1,0,1),(1,1,1).
\end{array}
 \tag{4.3}
\]

For example, the middle-cone decomposition is

\[
 (a,b,c)=(a-2c+b)(1,0,0)
          +(c-b)(2,0,1)+b(1,1,1),
 \tag{4.4}
\]

and the coefficients are nonnegative precisely on that cone.  The other
two decompositions are equally immediate:

\[
\begin{aligned}
 (a,b,c)&=(a-b)(1,0,0)+(b-c)(1,1,0)+c(1,1,1),\\
 (a,b,c)&=(a-c)(2,0,1)+(2c-a-b)(1,0,1)
                         +b(1,1,1).
\end{aligned}
 \tag{4.5}
\]

The five distinct rays in (4.3) have the following closed job prices:

\[
\begin{array}{c|c|c}
 (a,b,c)&(c_1,c_2,c_3)&\psi(L)\\ \hline
 (1,0,0)&(1,1,1)&\lceil L/3\rceil\\
 (1,1,0)&(1,2,2)&\lceil2L/3\rceil\\
 (1,0,1)&(1,1,2)&\lceil L/2\rceil\\
 (1,1,1)&(1,2,3)&L\\
 (2,0,1)&(2,2,3)&2\ (L=1),\quad L\ (L\ge2).
\end{array}
 \tag{4.6}
\]

This proves that checking these five rays is necessary and sufficient for
\(FC_3\).  Notice that the fifth ray is a genuine mixed min-plus ray; it
is not removed by merely naming the three ceiling tests.

#### Justification of the three regions

The size-two and size-three densities compare by

\[
 {a+b\over2}\lesseqgtr{a+b+c\over3}
 \quad\Longleftrightarrow\quad
                         a+b\lesseqgtr2c.
 \tag{4.7}
\]

In the size-three region, a residue-one choice compares
\(c_3+c_1\) with \(2c_2\); their difference is \(c-b\).
In the size-two region, \(c_3\le c_2+c_1\), so one size-three piece pays
every odd residue at least three.  In the size-three region the reductions

\[
 1+1\to2,qquad1+2\to3,qquad
 2+2+2\to3+3
 \tag{4.8}
\]

put every partition into the asserted normal form without increasing cost.
In the size-two region use instead

\[
 1+1\to2,\qquad1+2\to3,\qquad
 3+3\to2+2+2,\qquad1+3\to2+2.
 \tag{4.9}
\]

The four cost comparisons are respectively \(b\le a\), \(c\le a\),
\(2c\ge a+b\), and \(c\ge b\).  This proves both the formulas and
linearity used above.

## 5. Exact binomial verification at depth three

The three ceiling-ray margins are as follows:

\[
\begin{array}{c|r|r|r}
 k&\lceil L/3\rceil&\lceil2L/3\rceil&\lceil L/2\rceil\\ \hline
11&242&363&242\\
13&715&1066&702\\
15&2052&3027&1962\\
16&6666&10968&7992\\
17&5610&8075&5049\\
18&21335&35053&25516\\
19&13889&18886&10811\\
20&67336&110428&80237\\
21&26940&30132&11246\\
22&207781&339640&246008\\
24&618401&1004547&723695\\
26&1731485&2777545&1981009\\
28&4314767&6722696&4688052\\
30&8001129&11250549&7202294
\end{array}
 \tag{5.1}
\]

Every entry is obtained directly from

\[
 \sum_{u=1}^3H_{t+u}\psi(u)
 -\sum_{b=1}^{t-1}\widetilde H_b\psi(t-b),
 \tag{5.2}
\]

where

\[
 H_s={k\choose s}-{k\choose s-1},
 \qquad \widetilde H_1={k\choose1},
 \qquad \widetilde H_b=H_b\quad(b\ge2).
 \tag{5.2a}
\]

The tilde is the nonempty-ideal convention: after deleting the empty set,
its old symmetric chain merges into the rank-one birth class.

The volume ray has margin

\[
                         3W-\Lambda+h\ge0.
 \tag{5.3}
\]

For the mixed ray in (4.6), the margin is the volume margin plus

\[
                         H_{t+1}-H_{t-1}.
 \tag{5.4}
\]

This difference is positive on every row of (5.1).  It can be checked
without the table.  In even dimension \(k=2r\), \(t=r-3\),

\[
 {H_{r-2}\over H_{r-4}}
 ={5(r+4)(r+5)\over9(r-3)(r-2)}\ge1
 \tag{5.5}
\]

through the relevant range \(8\le r\le15\).  In odd dimension
\(k=2m+1\), \(t=m-2\),

\[
 {H_{m-1}\over H_{m-3}}
 ={(m+4)(m+5)\over2(m-2)(m-1)}\ge1
 \tag{5.6}
\]

through the relevant range \(5\le m\le10\).

The optimal-depth definition gives \(D=3\) exactly for

\[
 \{11,13,15,16,17,18,19,20,21,22,24,26,28,30\}.
 \tag{5.7}
\]

This is a finite substitution in

\[
 (D-1)W+{D\choose2}<\Lambda
 \le DW+{D+1\choose2}.
 \tag{5.8}
\]

There are no later depth-three values.  To see the monotonicity directly,
put

\[
 A_m={4^m\over2{2m\choose m}}.
 \tag{5.9}
\]

The two parity quotients are \(A_m-1/W\) and
\(A_m-1/2-1/W\), respectively, and

\[
 {A_{m+1}\over A_m}={2(m+1)\over2m+1}>1.
 \tag{5.10}
\]

Also \(W\) increases.  Hence each parity quotient is increasing.  At
\(k=31,32\) it already exceeds \(3+6/W\), so (5.8) forces every later
depth to be at least four.  Equations (4.3)--(5.10) therefore prove every
depth-three instance.

### Theorem 5.1 (exact finite closure)

For every Boolean coefficient-one instance with optimal depth \(D\le3\),
including the positive left-filled boundary instances \(k=6,9\), the
whole-job configuration LP \(FC_D\) is feasible.

#### Proof

Depth one is the volume inequality.  At depth two, (3.1)--(3.3) reduce all
prices to the two rows of (3.4).  At depth three, Section 4 reduces all
prices to the five rays in (4.6); the three ceiling rays pass by (5.1),
the volume ray by (5.3), and the mixed ray by (5.3)--(5.6).  The exact
configuration-price separation theorem then gives fractional feasibility.
\(\square\)

## 6. Remaining all-depth obstruction

There is no counterexample in the depth-three price fan.  The first finite
covering-price cone known not to be generated by concave and pure ceiling
rays occurs at capacity five, for example the closed table

\[
                         (1,2,2,2,3).
 \tag{6.1}
\]

Theorem 5.1 does not control that ray or its higher-depth analogues.  The
all-depth alternatives are now exact:

1. keep the off-middle Pascal children coupled and prove their total
   margin is nonnegative for every min-plus price; or
2. classify/control the genuinely mixed extreme shortest-path rays; or
3. exhibit one such ray with negative margin on the actual binomial data.

No theorem here decides among these alternatives.
