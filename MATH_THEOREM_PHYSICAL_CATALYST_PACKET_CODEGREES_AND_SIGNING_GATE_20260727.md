# Physical three-top catalyst packets: exact degrees, critical codegrees, and the signing gate

Date: 2026-07-27

## 0. Outcome

Let

\[
 n=2m,\qquad M=m+H,\qquad s=m-H,\qquad
 R=\binom{2m}M,\qquad W=\binom{2m}m,
\]

and use the packing-side height, so

\[
 \lambda_H=\frac WR=M(1+O(H/m)).
\]

Form the **formal physical packet hypergraph** \(\mathcal K\):

* its top vertices are the \(R\) rank-\(M\) tops;
* its owner vertices are the \(W\) middle \(m\)-sets;
* a formal edge is one role-labelled three-top/two-base conveyor;
* the edge contains its three tops and its common squarefree support of
  \(3M\) middle owners.

Thus \(\mathcal K\) is \(k=3M+3\)-uniform.  Retaining role labels makes
it a multihypergraph; quotienting packet symmetries divides all relevant
degrees together.

This note proves:

1. exact top and owner degrees
   \[
   \boxed{
   D_T=3sM!,\qquad
   D_O=\frac{3M(m!)^2}{(s-1)!},\qquad
   \frac{D_O}{D_T}=\frac M{\lambda_H}=1-O(H/m);}
   \tag{0.1}
   \]
2. exact top--top and top--owner pair profiles, and an exact
   distance-enumerator formula for owner pairs;
3. the sharp order
   \[
   \boxed{\Delta_2(\mathcal K)=\Theta(D_T/m^2);}
   \tag{0.2}
   \]
4. an exact critical obstruction to every audited growing-rank nibble:
   \[
   \boxed{
   \frac{k\Delta_2\log(W+R)}{D_T}
   \ge12\log2-o(1),}
   \tag{0.3}
   \]
   rather than \(o(1)\);
5. fixed-rank contraction packs the three-top supports almost perfectly,
   but random decoration has linear expected owner-pair collisions;
   obtaining \(o(W)\) repeated middle incidence is equivalent to the
   original near-owner-factor problem, not a consequence of the
   contraction; and
6. after such a packet selection, the remaining all-depth choice is an
   explicit signed quadratic (Ising/discrepancy) problem whose
   interaction matrix is the overlap Gram matrix of the \(16q\)-sparse
   trace derivatives.

This is a sharp critical boundary, not a coefficient-one proof.

## 1. Formal packet count and exact degrees

Fix one canonical conveyor template with \(M+1\) active roles: the
\(M-2\) ordered common-core positions and the three roles \(x,a,y\).
A formal packet is an injection of those roles into \([2m]\). Hence

\[
 |E(\mathcal K)|=(n)_{M+1}=\frac{n!}{(s-1)!}.
\tag{1.1}
\]

Every packet contains three tops and \(3M\) owners. The symmetric group
is transitive on each vertex orbit, so incidence counting gives

\[
 RD_T=3|E(\mathcal K)|,\qquad
 WD_O=3M|E(\mathcal K)|.
\]

Using

\[
 R=\frac{n!}{M!s!},\qquad
 W=\frac{n!}{(m!)^2}
\]

gives (0.1).

Equivalently, a fixed unordered three-top support has
\[
 6(M-2)!
\]
formal decorations: order the three omitted endpoint roles and biject
the \(M-2\) core roles with their labels.

## 2. Exact pair profiles

### 2.1 Two tops

Two packet tops are always distinct \(M\)-subsets of a common
\((M+1)\)-set. Therefore

\[
 \boxed{
 d(U,V)=
 \begin{cases}
 6(M-1)!,&|U\cap V|=M-1,\\
 0,&\text{otherwise}.
 \end{cases}}
\tag{2.1}
\]

Indeed, for adjacent \(U,V\), their union is forced; choose the third
omitted endpoint in \(M-1\) ways and then one of \(6(M-2)!\)
decorations. Consequently

\[
 \frac{C_{TT}}{D_T}=\frac2{sM}.
\tag{2.2}
\]

### 2.2 One top and one owner

For a packet owner \(X\) and packet top \(U\), necessarily
\(|X\setminus U|\in\{0,1\}\).  Relative to each one of the three
canonical tops, exactly \(2m\) of the packet's \(3M\) owners contain
the endpoint omitted from that top: each of the other two cyclic frames
has exactly \(m\) windows through that endpoint.  Hence the exact
codegrees are

\[
\boxed{
d(U,X)=
\begin{cases}
3s(3M-2m)m!H!,&X\subseteq U,\\[1mm]
6m(m-1)!(H+1)!,&|X\setminus U|=1,\\
0,&|X\setminus U|>1.
\end{cases}}
\tag{2.3}
\]

For example, in the contained case there are
\(3(3M-2m)\) canonical top--owner incidence patterns.  For each,
the owner roles map to \(X\) in \(m!\) ways, the remaining top roles in
\(H!\) ways, and the omitted active role has \(s\) possible images
outside \(U\).  The one-outside case is analogous.

Both values in (2.3) are exponentially smaller than \(D_T/m^2\), since
their normalizations contain \(\binom MH^{-1}\) or
\(\binom M{H+1}^{-1}\).

### 2.3 Two owners

Let

\[
 A_d=\#\{\{P,Q\}:P,Q\text{ are distinct canonical packet owners and }
                 d_J(P,Q)=d\}.
\tag{2.4}
\]

This is a finite, exact distance enumerator of the displayed canonical
three-frame support.  If fixed owners \(X,Y\) have Johnson distance
\(d\), then

\[
\boxed{
d(X,Y)=
\begin{cases}
A_d\,\dfrac{(d!)^2(m-d)!^2}{(s-1)!},
   &1\le d\le H+1,\\[3mm]
0,&d>H+1.
\end{cases}}
\tag{2.5}
\]

To see this, fix one canonical owner pair of distance \(d\).  Map its
intersection, its two differences, and the unused active roles.  The
numbers of choices are respectively
\[
(m-d)!,\quad d!,\quad d!,\quad
(m-d)_{H+1-d}=\frac{(m-d)!}{(s-1)!}.
\]

The distance-one enumerator satisfies

\[
 3M\le A_1\le15M.
\tag{2.6}
\]

The lower bound consists of the \(M\) consecutive-window pairs inside
each of the three cyclic decks.  For the upper bound, a fixed owner has
two distance-one neighbors in its own deck and at most four in either
other deck, by the cyclic one-zero lemma.  Sum degrees and divide by
two.

Put
\[
 F_d=\frac{(d!)^2(m-d)!^2}{(s-1)!}.
\]
Then
\[
 \frac{F_1}{D_T}=\frac1{3m^2\lambda_H},
\qquad
 \frac{F_{d+1}}{F_d}
 =\left(\frac{d+1}{m-d}\right)^2.
\tag{2.7}
\]

Since \(A_d<\frac92M^2\), (2.6)--(2.7) show

\[
 \frac{M}{m^2\lambda_H}
 \le\frac{d_{OO}(1)}{D_T}
 \le\frac{5M}{m^2\lambda_H},
\tag{2.8}
\]

while every \(d\ge2\) contributes only \(O(D_T/m^3)\). Together with
(2.2), this proves (0.2).

## 3. The exact nibble boundary

The degree discrepancy is only \(O(H/m)\), and the maximum codegree is
\(\Theta(D_T/m^2)\), but the uniformity is \(k=3M+3\).  Already the
top--top codegree forces

\[
\begin{aligned}
\frac{k\Delta_2\log(W+R)}{D_T}
&\ge
(3M+3)\frac2{sM}(2m\log2+o(m))\\
&=12\log2+o(1).
\end{aligned}
\tag{3.1}
\]

Thus the explicit variable-rank condition
\(k\Delta_2\log|V|/D=o(1)\) fails at a nonzero constant.  Classical and
modern fixed-rank nibble theorems do not diagonalize because
\(k\to\infty\).  The physical packet catalogue is on the same critical
surface as the repaired-ring catalogue, with a larger constant.

## 4. What fixed-rank contraction does and does not give

Project a packet to its three tops.  The resulting 3-uniform
hypergraph is regular with

\[
d_{\rm top}=s\binom M2,\qquad
\Delta_{2,\rm top}=M-1,\qquad
\frac{\Delta_{2,\rm top}}{d_{\rm top}}=\frac2{sM}=o(1).
\]

Pippenger--Spencer therefore gives a matching of top triples covering
all but \(o(R)\) tops.  This is a valid fixed-rank contraction.

However a family of

\[
r=(1-o(1))R/3
\]

packets has
\[
3Mr=(1-o(1))MR=(1-o(1))W
\tag{4.1}
\]
middle incidences.  If \(\mu(X)\) is its owner load, put
\[
\operatorname{col}=\sum_X(\mu(X)-1)_+.
\]
Then
\[
\operatorname{col}=3Mr-|\{X:\mu(X)>0\}|.
\tag{4.2}
\]

Consequently \(\operatorname{col}=o(W)\) is equivalent to covering
\(W-o(W)\) distinct owners.  The contraction has not weakened the
owner-factor requirement; it has only separated its top part.

The independent benchmark confirms the scale. Two independent uniform formal
packets have expected owner intersection
\[
\frac{(3M)^2}{W}.
\]
For \(r\sim R/3\) independent packets, the expected pair-collision
ledger is
\[
\binom r2\frac{9M^2}{W}
=\left(\frac12+o(1)\right)W
\tag{4.3}
\]
because \(MR/W=M/\lambda_H=1+o(1)\).  Conditioning only on distinct
top triples is not analyzed by this calculation; the fixed-rank
contraction may introduce useful correlations, but none are supplied by
its theorem.

### Proposition 4.1 (rigorous slow first bite)

For every \(\varepsilon=o(1)\) with
\(\varepsilon R\to\infty\), there is a top-disjoint packet family of
size
\[
 \left(\frac{\varepsilon}{3}-O(\varepsilon^2)\right)R
\]
whose owner pair-collision ledger
\[
 \sum_X\binom{\mu(X)}2
\]
is \(O(\varepsilon^2W)\).

#### Proof

Select every formal packet independently with probability
\(p=\varepsilon/D_T\). The expected number selected is
\[
p|E(\mathcal K)|=\varepsilon R/3.
\]
The expected number of selected pairs sharing a top is at most
\[
R\binom{D_T}2p^2=O(\varepsilon^2R).
\]
Delete one packet from every such conflicting pair. This leaves a
top-disjoint family and costs at most the number of conflict pairs.

Before deletion, the expected owner pair-collision ledger is
\[
W\binom{D_O}2p^2=O(\varepsilon^2W)
\]
because \(D_O/D_T=1+o(1)\). Deletion only decreases it.  Averaging
and Markov give constant-probability bounds
\(O(\varepsilon^2R)\) and \(O(\varepsilon^2W)\) for the two collision
ledgers, while Chernoff gives
\((1+o(1))\varepsilon R/3\) selected packets with probability tending
to one.  Taking fixed sufficiently large constants in the two Markov
bounds makes the three events intersect with positive probability.
The same deletion then gives both asserted bounds. \(\square\)

Thus a slow first bite with \(\varepsilon=o(1)\) has \(o(W)\)
collisions, but covers only \(o(R)\) tops. Iterating independent bites
until \(1-o(1)\) total density restores the linear benchmark. Avoiding
that restoration requires correlations not present in the first-bite
argument; this is precisely the growing-rank matching problem exposed
by (3.1).

## 5. Residual all-depth signing problem

Assume a family \(\mathcal P\) of top-disjoint packets has been selected
and that its common middle supports have only \(o(W)\) repeated
incidence.  For packet \(P\) and depth \(q\), let

\[
\delta_{P,q}=\Gamma^1_{P,q}-\Gamma^0_{P,q}.
\]

Then
\[
\sum_T\delta_{P,q}(T)=0,\qquad
|\operatorname{supp}\delta_{P,q}|
=\|\delta_{P,q}\|_2^2=16q.
\tag{5.1}
\]

Choose a shore sign \(\varepsilon_P\in\{-1,+1\}\), and put
\[
A_{P,q}=\frac12(\Gamma^0_{P,q}+\Gamma^1_{P,q}),\qquad
B_q=R_q+\sum_{P\in\mathcal P}A_{P,q}.
\]

The resulting load is
\[
L_q(\varepsilon)
=B_q+\frac12\sum_P\varepsilon_P\delta_{P,q}.
\tag{5.2}
\]

For nonnegative depth weights \(w_q\), the sign-dependent part of the
weighted floor energy is exactly
\[
\boxed{
\mathcal F(\varepsilon)
=\sum_P b_P\varepsilon_P
 \sum_{P<Q}J_{PQ}\varepsilon_P\varepsilon_Q,}
\tag{5.3}
\]
where
\[
b_P=\frac12\sum_qw_q\langle B_q,\delta_{P,q}\rangle,
\qquad
J_{PQ}=\frac14\sum_qw_q
       \langle\delta_{P,q},\delta_{Q,q}\rangle.
\tag{5.4}
\]

The diagonal term
\[
\frac18\sum_{P,q}w_q\|\delta_{P,q}\|_2^2
\]
is independent of the signs.  This is the multi-packet form of the
single-packet no-self-toll identity.

If derivative supports of different packets were disjoint, then
\(J_{PQ}=0\) and every sign could be chosen independently against
\(b_P\).  With overlap, (5.3) is an Ising/discrepancy problem on the
packet conflict graph.  A sufficient next theorem would bound its
weighted interaction degree
\[
\max_P\sum_{Q\ne P}|J_{PQ}|
\]
by a strict fraction of the available linear charge
\(\sum_P|b_P|\), simultaneously for all controlled depths.  Top
disjointness alone gives no such bound because rank-\((m-q)\) targets
can occur in packets on many different tops.

Thus the two residual gates are now separated exactly:

1. **physical packet selection:** near-perfect top coverage with
   \(o(W)\) repeated middle incidence;
2. **trace signing:** minimize the explicit quadratic form (5.3).

Neither follows from the fixed-rank top contraction.
