# Calibrated top-fibre packets: exact overlap and codegree audit

Date: 2026-07-25

Pure mathematics only.  No computation, search, solver, or web input is
used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q=\frac{W}{N_q},
\]

and let \(H\) be the **least** positive integer for which

\[
 \lambda_H\ge M:=m+H.                                      \tag{0.1}
\]

For every top \(U\in\binom{[2m]}M\), choose a directed cyclic order of
\(U\).  Its \(M\) cyclic \(m\)-intervals form its middle packet, and its
cyclic \((m\pm q)\)-intervals are its flags at depth \(q<H\).

The exact audit gives the following conclusions.

1. The calibration is scalar-perfect up to \(o(W)\): if
   \(S=MN_H\), then

   \[
    0\le W-S<\frac{2(H-1)}{M-1}W=o(W),                    \tag{0.2}
   \]

   and the sum, over every controlled rank, of the slot shortages forced
   before any packet is chosen is

   \[
    (W-S)+2\sum_{q=1}^{H-1}(N_q-S)_+
      =O\!\left(\frac{H^{3/2}}mW\right)=o(W).              \tag{0.3}
   \]

2. Two packets whose tops are at Johnson distance \(t\) have at most

   \[
    H-t+1                                                     \tag{0.4}
   \]

   common middle owners (and none if \(t>H\)).  This bound is sharp.

3. The hypergraph whose edge is one top together with the \(M\) middle
   owners of one packet is nearly regular and has excellent owner
   codegrees.  If \(R=(M-1)!\) is the number of directed cyclic orders of
   one top and \(d\) is the owner degree, then

   \[
    d=\frac{(m!)^2}{(m-H)!}=\frac{M}{\lambda_H}R,            \tag{0.5}
   \]

   while two owners at Johnson distance \(1\le s<H\) have exact
   codegree

   \[
    d_s=\frac{2d}{\binom ms^2}.                              \tag{0.6}
   \]

   The boundary value at \(s=H\) is

   \[
    d_H=H!^2(m-H+1)!,\qquad
    \frac{d_H}{d}=\frac{m-H+1}{\binom mH^2}.                \tag{0.7}
   \]

   Hence the maximum distinct-owner codegree is \(2d/m^2\) for all
   sufficiently large \(m\).  There is no middle-only overlap obstruction.

4. This good codegree does **not** survive the addition of all flag rows.
   A target of size \(m\pm q\) has degree \(\lambda_qd\), and two targets
   in the same rank and at Johnson distance \(s\) have normalized
   codegree

   \[
    \frac{2}{\binom{m-q}s\binom{m+q}s}                      \tag{0.8}
   \]

   in the overlapping-complement range.  In contrast, for nested targets
   \(A\subset B\), \(|B|-|A|=c\), the exact ratios are

   \[
    \frac{\deg(A,B)}{\deg(A)}
      =\frac{c+1}{\binom{2m-|A|}c},\qquad
    \frac{\deg(A,B)}{\deg(B)}
      =\frac{c+1}{\binom{|B|}c}.                           \tag{0.9}
   \]

   At adjacent central ranks this is \(2/m+O(m^{-2})\), not
   \(O(m^{-2})\).  It is forced by an exact \(2M\)-cycle of inclusions
   between consecutive interval ranks in every packet.

5. Even exact disjointness of all selected middle packets implies only

   \[
    (q+1)\operatorname{mult}(T)\le\binom{m+q}q              \tag{0.10}
   \]

   for a repeated rank-\((m-q)\) or rank-\((m+q)\) flag \(T\).  At
   \(q=1\) this allows multiplicity \(\lfloor(m+1)/2\rfloor\), and the
   bound is locally sharp.  Thus a near-perfect middle matching, by
   itself, gives no \(o(W)\) shallow-hole theorem.

The precise proved boundary is therefore positive for the middle-only
packet matching and negative for any argument which tries to infer the
flag support from that matching without using the nested interval
structure.  No obstruction to a correlated all-rank packet selection is
proved here.

## 1. The calibrated scalar window

The consecutive ratio is

\[
 \frac{\lambda_q}{\lambda_{q-1}}
   =\frac{m+q}{m-q+1}.                                      \tag{1.1}
\]

Minimality in (0.1) gives \(\lambda_{H-1}<M-1\), and therefore

\[
 M\le\lambda_H
 <(M-1)\frac{M}{m-H+1}.                                    \tag{1.2}
\]

Write

\[
 \mu=\frac{S}{W}=\frac{M}{\lambda_H},\qquad \delta=1-\mu.
\]

Then (1.2) gives the exact bounds

\[
 0\le\delta<1-\frac{m-H+1}{M-1}
 =\frac{2H-2}{M-1}.                                        \tag{1.3}
\]

This proves (0.2).  The standard expansion

\[
 \log\lambda_h=\frac{h^2}{m}
   +O\!\left(\frac hm+\frac{h^3}{m^2}\right)
\]

shows

\[
 H=(1+o(1))\sqrt{m\log m}.                                 \tag{1.4}
\]

### Proposition 1.1 (aggregate forced slot deficit)

With \(S=MN_H\), equation (0.3) holds.

#### Proof

For every \(q\ge1\),

\[
 \begin{split}
 \log\lambda_q
 &=\sum_{i=0}^{q-1}
   \log\left(1+\frac{2i+1}{m-i}\right)\\
 &\ge\sum_{i=0}^{q-1}\frac{2i+1}{m+i+1}
 \ge\frac{q^2}{m+q}.                                      \tag{1.5}
 \end{split}
\]

Here \(\log(1+x)\ge x/(1+x)\) was used in the first inequality.
If \(N_q>S\), then \(1/\lambda_q>\mu=1-\delta\).  For sufficiently
large \(m\), (1.3) gives \(\delta<1/2\), so (1.5) yields

\[
 \frac{q^2}{m+q}< -\log(1-\delta)\le2\delta.               \tag{1.6}
\]

Since \(q\le H=o(m)\), this implies \(q<2\sqrt{\delta m}\).  Moreover

\[
 0<N_q-S\le W-S=\delta W.                                  \tag{1.7}
\]

Consequently

\[
 \sum_{q=1}^{H-1}(N_q-S)_+
 \le2\delta^{3/2}\sqrt m\,W
 =O\!\left(\frac{H^{3/2}}mW\right).                        \tag{1.8}
\]

Add the middle deficit \(\delta W\), double for the lower and upper
ranks, and use (1.4).  Since

\[
 \frac{H^{3/2}}m
 =m^{-1/4}(\log m)^{3/4+o(1)}=o(1),
\]

the result follows. \(\square\)

At upper depth \(H\), a packet's flag is its top \(U\), not \(M\)
distinct masks.  Choosing one packet at every top covers that rank
exactly.

There is also no hidden singleton-incidence divisibility.  At any proper
interval size \(k<M\), a coordinate of a fixed top belongs to exactly
\(k\) of its \(M\) cyclic \(k\)-intervals.  Hence, after choosing one
packet at every top, the number of rank-\(k\) flag occurrences containing
any fixed coordinate \(x\) is the order-independent integer

\[
 k\binom{2m-1}{M-1}=\frac{kS}{2m}.                         \tag{1.9}
\]

Thus the first point marginals are already exact before the cyclic orders
are chosen.  Pair and higher marginals, unlike (1.9), depend on those
orders.

### Proposition 1.2 (exact unstructured Hall allocation)

Ignoring the requirement that the \(M\) owners assigned to one top be the
cyclic intervals of one order, there is an exact choice of \(M\) distinct
middle owners inside every top, with no owner chosen twice globally.

More generally, at every proper rank \(k\) for which

\[
 \binom{2m}{k}\ge S,                                       \tag{1.10}
\]

one can assign \(M\) distinct rank-\(k\) subsets to every top, with no
rank-\(k\) target assigned to two tops.

#### Proof

Consider the inclusion graph between the \(N_H\) tops and the rank-\(k\)
targets.  Its top and target degrees are

\[
 B_k=\binom Mk,qquad A_k=\binom{2m-k}{M-k},
\]

and double counting gives

\[
 N_HB_k=\binom{2m}{k}A_k.                                \tag{1.11}
\]

For a family \(\mathcal A\) of tops, all \(B_k|\mathcal A|\) incident
edges land in its neighbourhood, while a target receives at most \(A_k\)
of them.  Therefore

\[
 |N(\mathcal A)|\ge
 \frac{B_k}{A_k}|\mathcal A|
 =\frac{\binom{2m}{k}}{N_H}|\mathcal A|
 \ge M|\mathcal A|.                                       \tag{1.12}
\]

Replace every top by \(M\) identical demand clones.  Equation (1.12) is
Hall's condition for a matching saturating all clones, and matching uses
distinct target vertices.  At \(k=m\), condition (1.10) is exactly
\(W\ge S\), already guaranteed by calibration. \(\square\)

Thus even exact integral owner allocation and all capacity-rich rankwise
allocations are settled before chronology is imposed.  The missing
integrality is specifically the demand that the allocations at all ranks
come from one cyclic order in each top.

## 2. Exact intersection of two fixed packets

For a cyclic order \(\pi\) of a top \(U\), denote its middle packet by
\(\mathcal P(U,\pi)\).  Let

\[
 t=|U\setminus V|=|V\setminus U|.
\]

### Theorem 2.1 (sharp top-distance intersection bound)

If \(U\ne V\), then

\[
 |\mathcal P(U,\pi)\cap\mathcal P(V,\rho)|
 \le(H-t+1)_+.                                             \tag{2.1}
\]

For every \(1\le t\le H\), equality is attainable.

#### Proof

A common owner \(X\) must lie in \(U\cap V\).  In the first top its
complement

\[
 Q=U\setminus X
\]

is a cyclic \(H\)-interval containing the fixed \(t\)-set
\(A=U\setminus V\).  In a circle of length \(M\), the number of cyclic
\(H\)-intervals containing a fixed \(t\)-set is at most \(H-t+1\): after
unwrapping any one containing interval, its first point can move through
at most \(H-t+1\) positions.  If no containing interval exists, the
number is zero.  This proves the upper bound.  If \(t>H\), the same fact
also follows from \(|U\cap V|=M-t<m\).

For sharpness, put the elements of \(A=U\setminus V\) consecutively in
\(\pi\), put the elements of \(B=V\setminus U\) in the corresponding
block of \(\rho\), and give the common coordinates the same cyclic order
outside those blocks.  Replacing the block \(A\) by \(B\) bijects the
\(H-t+1\) intervals containing the whole block.  Their complementary
owners are identical in the two packets. \(\square\)

Thus a pair of nearby tops can share \(\Theta(H)\) owners, but only an
\(O(H/M)=o(1)\) fraction of either packet.

The identical argument gives every other proper interval rank.

### Corollary 2.2 (sharp flag-packet intersection bound)

Let \(1\le k<M\), put \(h=M-k\), and let
\(\mathcal I_k(U,\pi)\) be the packet's family of cyclic \(k\)-intervals.
For tops at distance \(t\),

\[
 |\mathcal I_k(U,\pi)\cap\mathcal I_k(V,\rho)|
 \le(h-t+1)_+.                                             \tag{2.2}
\]

For every \(1\le t\le h\), equality is attainable by the same block-
replacement construction.

Indeed, the complement in \(U\) of a common \(k\)-interval is an
\(h\)-interval containing \(U\setminus V\).  Conversely, replace that
fixed \(t\)-block by \(V\setminus U\).  In particular, at lower depth
\(q\) the bound is \((H+q-t+1)_+\), while at upper depth \(q\) it is
\((H-q-t+1)_+\).

## 3. Exact middle degrees and codegrees

Retain directed cyclic orders modulo rotation, so one top has

\[
 R=(M-1)!                                                     \tag{3.1}
\]

candidate packets.  Reversal merely duplicates a support with the reverse
chronology; quotienting by reversal divides every count below by two and
does not change a ratio.

A fixed owner \(X\) lies in \(\binom mH\) tops.  In one containing top,
the number of cyclic orders in which \(X\) is an interval is

\[
 m!H!.                                                        \tag{3.2}
\]

Indeed, \(X\) and its complement are the two cyclic blocks.  Therefore

\[
 d=\binom mH m!H!=\frac{(m!)^2}{(m-H)!}.                     \tag{3.3}
\]

Since

\[
 \binom{M}{m}=\frac{M!}{m!H!},\qquad
 \frac{\binom mH}{\binom Mm}=\frac1{\lambda_H},
\]

(3.3) also gives (0.5).

### Theorem 3.1 (owner-pair codegree)

Let \(X,Y\) be distinct middle owners at Johnson distance
\(s=|X\setminus Y|\).

* If \(s>H\), their codegree is zero.
* If \(1\le s<H\), their codegree is

  \[
   d_s=\binom{m-s}{H-s}
       2(s!)^2(H-s)!(m-s)!
      =\frac{2d}{\binom ms^2}.                            \tag{3.4}
  \]

* If \(s=H\), their codegree is (0.7).

#### Proof

A common top contains \(X\cup Y\), and there are
\(\binom{m-s}{H-s}\) such tops.  Fix one.  The complements

\[
 Q=U\setminus X,\qquad Q'=U\setminus Y
\]

are \(H\)-sets at distance \(s\).  When \(s<H\), a cyclic order in which
both are intervals has, up to the two directions, the four consecutive
blocks

\[
 Q\setminus Q',\quad Q\cap Q',\quad Q'\setminus Q,\quad
 U\setminus(Q\cup Q').
\]

Their sizes are \(s,H-s,s,m-s\), giving exactly

\[
 2(s!)^2(H-s)!(m-s)!                                       \tag{3.5}
\]

orders.  Multiplication and cancellation prove (3.4).

When \(s=H\), the complements are disjoint.  Contract them to two blocks.
Together with the \(m-H\) remaining singleton coordinates there are
\(m-H+2\) cyclic units, giving

\[
 H!^2(m-H+1)!                                               \tag{3.6}
\]

orders.  The common top is forced. \(\square\)

For \(H\ge2\), the boundary ratio in (0.7) is smaller than \(2/m^2\)
for all sufficiently large \(m\).  Hence (0.6) at \(s=1\) is the maximum.

There is a useful independent audit of every factor in Theorem 3.1.  A
packet containing a fixed owner has exactly \(M-1\) other owners, so its
pair codegrees must satisfy

\[
 \sum_{Y\ne X}\deg(X,Y)=d(M-1).                            \tag{3.7}
\]

At each distance \(1\le s<H\) there are \(\binom ms^2\) choices of
\(Y\), and (3.4) contributes exactly \(2d\).  At distance \(H\), (0.7)
contributes exactly \(d(m-H+1)\).  Therefore the left side of (3.7) is

\[
 2d(H-1)+d(m-H+1)=d(m+H-1)=d(M-1),
\]

as required.

If one adjoins the top itself as one more vertex of every packet edge,
then top degree is \(R\), top--top codegree is zero, and top--owner
codegree is \(m!H!\) when the owner is contained in the top.  Its ratio to
\(R\) is

\[
 \frac{m!H!}{(M-1)!}=\frac{M}{\binom Mm},                   \tag{3.8}
\]

which is superpolynomially small at (1.4).  Equations (0.5)--(0.7) make
the augmented middle hypergraph nearly regular with maximum normalized
codegree \(2/m^2\).  Any failure of a near-perfect middle packet matching
therefore cannot be blamed on a positive-density pair overlap.

## 4. Same-rank flag degrees and codegrees

Let \(T\) have size \(k\), where \(1\le k<M\).  It lies in
\(\binom{2m-k}{M-k}\) tops.  In any one containing top, exactly

\[
 k!(M-k)!                                                     \tag{4.1}
\]

directed cyclic orders make \(T\) an interval.  Hence

\[
 d_k=\binom{2m-k}{M-k}k!(M-k)!
 =\frac{k!(2m-k)!}{(m-H)!}.                                 \tag{4.2}
\]

For \(k=m\pm q\), this becomes

\[
 d_{m\pm q}=\lambda_qd.                                    \tag{4.3}
\]

Suppose two \(k\)-targets are at Johnson distance \(s\), and put
\(h=M-k\).  In the range \(1\le s<h\), their complements in a common
top are overlapping \(h\)-intervals.  The same four-block count as in
Section 3 gives

\[
 d_{k,s}
 =\frac{2(s!)^2(k-s)!(2m-k-s)!}{(m-H)!},                    \tag{4.4}
\]

and therefore

\[
 \frac{d_{k,s}}{d_k}
 =\frac{2}{\binom ks\binom{2m-k}s}.                         \tag{4.5}
\]

For \(k=m\pm q\), equation (4.5) is (0.8).  In every shallow rank
\(q=o(m)\), its maximum is \((2+o(1))/m^2\).

There is a boundary exception when \(s=h\): the two complements are
disjoint, and the per-top count is

\[
 h!^2(M-2h+1)!.                                             \tag{4.6}
\]

For \(h=1\), the normalized codegree is \(1/(m-H+1)\).  This is benign:
rank \(M-1\) consists of the sets \(U-x\), and every packet in top \(U\)
contains all of them, independently of its cyclic order.  That upper rank
is automatically covered when every top is used.

The same row-sum audit verifies (4.4)--(4.6).  For fixed \(T\), every one
of its incident packets contains \(M-1\) other targets in the same rank.
Each distance \(1\le s<h\) contributes \(2d_k\) after summing (4.5) over
the \(\binom ks\binom{2m-k}s\) targets at that distance.  The disjoint-
complement boundary contributes \((M-2h+1)d_k\).  Their sum is

\[
 2(h-1)d_k+(M-2h+1)d_k=(M-1)d_k,
\]

which is the required total.

## 5. The nested cross-rank obstruction

The preceding \(O(m^{-2})\) same-rank codegrees might suggest applying a
generic matching theorem simultaneously to many ranks.  The following
exact count rules that inference out.

### Theorem 5.1 (nested interval codegree)

Let \(A\subset B\subsetneq U\) have sizes \(a,b\), and put \(c=b-a\).
Across all tops and cyclic orders, the number of packets in which both
\(A\) and \(B\) are intervals is

\[
 d(A,B)=\frac{a!(c+1)!(2m-b)!}{(m-H)!}.                    \tag{5.1}
\]

Consequently (0.9) holds.

#### Proof

There are \(\binom{2m-b}{M-b}\) tops containing \(B\).  In a fixed top,
first choose the offset of the interval \(A\) inside the interval \(B\).
There are \(c+1\) offsets.  The elements of \(A\), of \(B\setminus A\),
and of \(U\setminus B\) can then be ordered in

\[
 a!\,c!\,(M-b)!
\]

ways.  Thus the per-top count is
\((c+1)!a!(M-b)!\).  Multiplication by the number of tops gives (5.1).
Dividing by (4.2) for \(a\) and for \(b\) proves (0.9). \(\square\)

For \(c=1\), \(a=m-1\), and \(b=m\), the ratio to the owner degree is
exactly

\[
 \frac{d(A,B)}{d_m}=\frac2m.                              \tag{5.2}
\]

This factor has a direct packet interpretation.  If

\[
 I_i^k=\{u_i,u_{i+1},\ldots,u_{i+k-1}\}
\]

are the \(k\)-intervals of one cyclic order, then \(I_i^k\) is contained
in exactly

\[
 I_i^{k+1}\quad\text{and}\quad I_{i-1}^{k+1}.              \tag{5.3}
\]

The inclusion graph between the packet's \(k\)- and \((k+1)\)-intervals
is therefore one alternating cycle of length \(2M\).  Adjacent flag ranks
come in indivisible cycle bundles; they are not independent low-codegree
rows.

In particular, if one tries to enforce \(Q\) shallow ranks by replacing a
packet with the union of all its target vertices, the edge size is
\(\Theta(MQ)\), while (5.2) leaves normalized codegree \(\Theta(1/m)\).
Thus the usual hypothesis ``edge size times normalized codegree tends to
zero'' fails already for a growing \(Q\).  This is an obstruction to that
black-box route, not to a structure-aware packet theorem.

## 6. Middle disjointness does not force flag coverage

### Proposition 6.1 (sharp local multiplicity ceiling)

Assume a family of selected packets has pairwise disjoint middle owner
sets.  Let \(T\) be a rank-\((m-q)\) lower target or a rank-\((m+q)\)
upper target, with \(1\le q<H\).  If \(T\) occurs as an interval in
\(c_T\) selected packets, then

\[
 (q+1)c_T\le\binom{m+q}q.                                 \tag{6.1}
\]

#### Proof

If \(|T|=m-q\), then in every packet containing \(T\) as an interval,
exactly \(q+1\) of that packet's middle intervals contain \(T\).  Across
middle-disjoint packets these are distinct members of the family of all
middle supersets of \(T\), whose size is \(\binom{m+q}q\).

If \(|T|=m+q\), exactly \(q+1\) of the packet's middle intervals are
contained in \(T\).  There are again \(\binom{m+q}q\) possible middle
subsets.  This proves (6.1). \(\square\)

At \(q=1\), (6.1) reads

\[
 c_T\le\left\lfloor\frac{m+1}{2}\right\rfloor.             \tag{6.2}
\]

It is locally sharp.  For a fixed \((m-1)\)-set \(T\), pair disjointly
as many as possible of the \(m+1\) coordinates outside \(T\).  For every
pair \(\{x,y\}\), choose a top containing \(T+x+y\) and a cyclic order
with the consecutive block

\[
 x,\quad T\text{ in any order},\quad y.
\]

Then \(T\) is an interval, and the two middle intervals of that packet
containing it are exactly \(T+x\) and \(T+y\).  These owner pairs are
disjoint over the chosen coordinate pairs.  This does not assert that all
other owners in those packets are mutually disjoint; it proves that no
stronger per-target multiplicity conclusion follows from middle
disjointness alone.

The crude support consequence of (6.2) is only \(\Omega(W/m)\), far below
the \(W-o(W)\) shallow support required.  A separate correlated all-rank
argument is indispensable.

## 7. Independent orders and the exact remaining gate

For a target of size \(k=m\pm q<M\), the number of containing tops and the
per-top interval probability are

\[
 A_k=\binom{2m-k}{M-k},\qquad
 p_k=\frac{M}{\binom Mk}.                                  \tag{7.1}
\]

If the cyclic orders are chosen independently and uniformly at all tops,
then

\[
 A_kp_k=\frac{S}{N_q}=\frac{M\lambda_q}{\lambda_H}.          \tag{7.2}
\]

The expected number of holes in that rank is exactly

\[
 N_q(1-p_k)^{A_k}.                                          \tag{7.3}
\]

At the middle rank, \(p_m\to0\) and \(A_mp_m=\mu\to1\), so (7.3) is

\[
 (e^{-1}+o(1))W.                                            \tag{7.4}
\]

The same conclusion holds for every \(q=o(\sqrt m)\).  Thus independent
topwise selection fails linearly even though the deterministic capacity
defect (0.3) is \(o(W)\).

Combining all sections, the calibrated problem has the following exact
boundary.

* Scalar capacity, top divisibility, packet-pair overlap, and the
  middle-only degree/codegree ledger all support an integral near-packing.
* Independent orders fail by (7.4).
* A middle near-packing cannot be promoted formally to shallow flag
  coverage, by Proposition 6.1.
* A generic all-layer low-codegree matching theorem cannot be invoked,
  because Theorem 5.1 gives the sharp adjacent-rank ratio \(2/m\) and the
  packet carries whole inclusion cycles.

The unresolved positive theorem must round the nested \(2M\)-cycle bundles
themselves, or exploit an exact switch/absorption operation which preserves
middle disjointness while repairing their flag supports.  No no-go for
such a correlated construction is proved in this audit.
