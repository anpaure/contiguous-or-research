# Octahedral rectangle positivity: interior connectivity and a sharp quadratic metric obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

Let \(V\) be a finite set, let \(2\le r\le |V|-2\), and let
\(\mu,\nu\in\mathbb Z_{\ge0}^{\binom Vr}\) have equal point marginals.
A unit rank-\(r\) square is

\[
 \omega(K;a,b,c,d)
 =e_{Kbc}+e_{Kad}-e_{Kac}-e_{Kbd},
 \tag{0.1}
\]

where \(|K|=r-2\) and \(a,b,c,d\) are distinct points outside \(K\).
A support-feasible square path is a sequence of nonnegative load vectors
whose successive differences are \(\pm\omega\).

The requested dimension-free bound

\[
 \text{path length}=O(\|\mu-\nu\|_1)
 \tag{0.2}
\]

cannot follow from any arbitrary uniform common lower bound or slack
assumption, even for exact floor/ceiling-balanced loads.

The obstruction is a quadratic pair-cut potential. For \(A\subseteq V\),
put

\[
 \Phi_A(x)
 =\sum_{S\in\binom Vr}\binom{|S\cap A|}{2}x(S).
 \tag{0.3}
\]

Every unit square changes \(\Phi_A\) by at most one. Nevertheless, for
every \(r\ge2\) and \(|V|\ge2r\), there are strictly positive load vectors
\(\mu,\nu\), with equal point marginals and

\[
 \|\mu-\nu\|_1=4,
 \qquad
 |\Phi_A(\mu)-\Phi_A(\nu)|
 =\left\lfloor {r^2\over4}\right\rfloor.
 \tag{0.4}
\]

Thus every signed square word, even before positivity is imposed, has
length at least \(\lfloor r^2/4\rfloor\).

The same abstract rank, total-mass, and floor/ceiling parameters occur in
the first lower central band. For

\[
 V=[2m],\qquad r=m-1,\qquad
 W=\binom{2m}{m},\qquad N=\binom{2m}{m-1},
\]

there are two load vectors of total mass exactly \(W\), every entry equal
to one or two, with equal point marginals and \(\ell_1\)-distance four,
whose square distance is at least

\[
 \boxed{\left\lfloor{(m-1)^2\over4}\right\rfloor.}
 \tag{0.5}
\]

So the failure is not caused by a sparse boundary point.

There is also a positive theorem at the correct scale. If

\[
 \min\{\mu(S),\nu(S)\}\ge1
 \qquad(S\in\binom Vr),
 \tag{0.6}
\]

then a support-feasible square path always exists, and one may take

\[
 \boxed{
 T\le {s(s-1)\over2}\,\|\mu-\nu\|_1,
 \qquad s=\min\{r,|V|-r\}.}
 \tag{0.7}
\]

The lower example has an explicit positive path of
\(O(r^2)\) moves, so the quadratic dependence on \(r\) is order-sharp.
Full common support therefore removes the positivity obstruction but not
the metric obstruction.

For calibrated packet absorption, equal point marginals are consequently
insufficient. Any \(O(\ell_1)\)-capacity theorem must at least control all
pair-cut discrepancies \(\Phi_A(\mu)-\Phi_A(\nu)\), or must allow larger
higher-order circuits whose action on (0.3) is of order \(r^2\) per
physical move.

## 1. Square paths and the pair-cut potential

For a load vector \(x\), define its point-margin vector by

\[
 (\partial_1x)(v)=\sum_{S\ni v}x(S).
 \tag{1.1}
\]

Every square (0.1) lies in \(\ker\partial_1\). The previously proved
octahedral saturation theorem says that these squares generate the whole
integer kernel. That theorem is a signed lattice statement and gives no
word-length or positivity bound.

The potential (0.3) has the equivalent pair-margin form

\[
 \Phi_A(x)
 =\sum_{\{u,v\}\in\binom A2}
   \sum_{S\supseteq\{u,v\}}x(S).
 \tag{1.2}
\]

Thus equal point marginals fix the first moments but do not fix
\(\Phi_A\), which is a sum of second moments.

Define the complete rank-two shadow

\[
 (\Gamma_2x)(\{u,v\})
 =\sum_{S\supseteq\{u,v\}}x(S).
 \tag{1.2a}
\]

For the square (0.1), all pairs meeting the common core cancel and

\[
 \Gamma_2\omega
 =e_{\{b,c\}}+e_{\{a,d\}}
  -e_{\{a,c\}}-e_{\{b,d\}}.
 \tag{1.2b}
\]

Consequently

\[
 \|\Gamma_2\omega\|_1=4.
 \tag{1.2c}
\]

This gives the primal version of the same slow mode:

\[
 \boxed{
 T\ge {1\over4}\|\Gamma_2(\mu-\nu)\|_1.}
 \tag{1.2d}
\]

Indeed the triangle inequality applied to the \(T\) square images proves
(1.2d). The scalar potential \(\Phi_A\) is obtained by summing the
coordinates of \(\Gamma_2x\) over \(\binom A2\).

### Lemma 1.1 (unit octahedral curvature)

For every \(A\subseteq V\) and every square (0.1),

\[
 \boxed{
 \Phi_A(\omega)
 =(\mathbf1_A(b)-\mathbf1_A(a))
  (\mathbf1_A(c)-\mathbf1_A(d)).}
 \tag{1.3}
\]

In particular,

\[
 |\Phi_A(\omega)|\le1.
 \tag{1.4}
\]

#### Proof

Put \(k=|K\cap A|\) and \(\epsilon_x=\mathbf1_A(x)\). For
\(h(t)=\binom t2\), the left side of (1.3) is

\[
 h(k+\epsilon_b+\epsilon_c)
 +h(k+\epsilon_a+\epsilon_d)
 -h(k+\epsilon_a+\epsilon_c)
 -h(k+\epsilon_b+\epsilon_d).
\]

The affine part of \(h\) cancels, and its mixed second difference is

\[
 (\epsilon_b-\epsilon_a)(\epsilon_c-\epsilon_d).
\]

This proves (1.3)--(1.4). \(\square\)

### Corollary 1.2 (metric lower bound)

Every signed or support-feasible square path from \(\mu\) to \(\nu\) has
length

\[
 \boxed{
 T\ge
 \max_{A\subseteq V}|\Phi_A(\mu)-\Phi_A(\nu)|.}
 \tag{1.5}
\]

#### Proof

Sum (1.4) along the path. \(\square\)

This is a word-metric obstruction, not a new lattice invariant:
\(\Phi_A\) may change, but only one unit per installed rectangle.

## 2. A four-support obstruction with arbitrary common slack

Choose disjoint \(r\)-sets \(P,Q\subseteq V\). Let

\[
 s=\lfloor r/2\rfloor.
\]

Partition

\[
 P=P_0\mathbin{\dot\cup}P_1,\qquad
 Q=Q_0\mathbin{\dot\cup}Q_1
\]

so that

\[
 |P_0|=|Q_1|=s,\qquad
 |P_1|=|Q_0|=r-s.
\]

Put

\[
 C=P_0\cup Q_0,\qquad D=P_1\cup Q_1.
 \tag{2.1}
\]

Then \(C,D\) are disjoint \(r\)-sets and

\[
 P\mathbin{\dot\cup}Q=C\mathbin{\dot\cup}D.
 \tag{2.2}
\]

Let \(u\) be any nonnegative common load vector, and set

\[
 \mu=u+e_P+e_Q,\qquad
 \nu=u+e_C+e_D.
 \tag{2.3}
\]

### Theorem 2.1 (quadratic distance at \(\ell_1=4\))

The vectors in (2.3) have equal point marginals and

\[
 \|\mu-\nu\|_1=4.
 \tag{2.4}
\]

With the potential indexed by \(A=P\),

\[
 \boxed{
 \Phi_P(\mu)-\Phi_P(\nu)
 =s(r-s)=\left\lfloor{r^2\over4}\right\rfloor.}
 \tag{2.5}
\]

Consequently every square path from \(\mu\) to \(\nu\) has at least the
number of moves in (2.5).

#### Proof

Equation (2.2) says that the two extra pairs in (2.3) have the same point
incidence, so the point margins agree. The four displayed \(r\)-sets are
distinct, giving (2.4).

At rank two, the changed pair coordinates form four disjoint complete
bipartite blocks:

\[
 +\,P_0\times P_1,\qquad +\,Q_0\times Q_1,\qquad
 -\,P_0\times Q_0,\qquad -\,P_1\times Q_1.
\]

Consequently

\[
 \|\Gamma_2(\mu-\nu)\|_1=4s(r-s).
 \tag{2.4a}
\]

Their intersections with \(P\) have sizes

\[
 r,\quad0,\quad s,\quad r-s.
\]

Therefore

\[
 \begin{aligned}
 \Phi_P(\mu)-\Phi_P(\nu)
 &=\binom r2-\binom s2-\binom{r-s}2\\
 &=s(r-s).
 \end{aligned}
\]

Apply Corollary 1.2. \(\square\)

Taking \(u\equiv L\) for an arbitrary \(L\ge1\) shows that no amount of
uniform pointwise slack repairs the linear-distance claim. The loads may
be \(L\) or \(L+1\) everywhere.

If \(|V|=2r\) and \(P\dot\cup Q=V\), these endpoints also have exactly
uniform point marginals: the uniform baseline contributes equally at every
point and each extra complementary pair contributes one. Thus point
regularity does not remove the obstruction.

### Theorem 2.2 (the distance is exactly quadratic)

If \(u(S)\ge1\) for every rank-\(r\) set, the support-feasible square
distance between the two vectors in (2.3) is exactly

\[
 \boxed{s(r-s).}
 \tag{2.6}
\]

#### Proof

The lower bound is Theorem 2.1. For the upper bound, put

\[
 P=P_0,\quad Q=P_1,\quad R=Q_0,\quad T=Q_1
\]

temporarily, so the four disjoint blocks have sizes

\[
 |P|=|T|=s,\qquad |Q|=|R|=r-s.
\]

Choose bijections \(P\leftrightarrow T\) and \(Q\leftrightarrow R\).
For \(0\le i\le s\), let \(P_i\) be obtained from \(P\) by replacing its
first \(i\) elements by their partners in \(T\). For
\(0\le j\le r-s\), define \(Q_j\) analogously by replacing elements of
\(Q\) by their partners in \(R\), and put

\[
 S_{ij}=P_i\cup Q_j.
\]

The four corners are

\[
 S_{00}=P\cup Q,\quad
 S_{s,r-s}=R\cup T,\quad
 S_{0,r-s}=P\cup R,\quad
 S_{s,0}=Q\cup T.
\]

For every grid cell define

\[
 q_{ij}
 =e_{S_{ij}}+e_{S_{i+1,j+1}}
  -e_{S_{i+1,j}}-e_{S_{i,j+1}}.
 \tag{2.7}
\]

The four sets in (2.7) share the \(r-2\) labels unaffected by that cell,
so \(q_{ij}\) is one elementary octahedron. Double telescoping gives

\[
 \sum_{i=0}^{s-1}\sum_{j=0}^{r-s-1}q_{ij}
 =e_{P\cup Q}+e_{R\cup T}
  -e_{P\cup R}-e_{Q\cup T}.
 \tag{2.8}
\]

Apply the negative cells \(-q_{ij}\) in row-major order. The partial
telescoping formula is explicit. After rows \(0,\ldots,i-1\) and the first
\(j\) cells of row \(i\), the load is

\[
 u+e_{S_{s,r-s}}+e_{S_{0,r-s}}
   -e_{S_{i,r-s}}+e_{S_{ij}}
   +e_{S_{i+1,0}}-e_{S_{i+1,j}}.
 \tag{2.9}
\]

Coincident terms in (2.9) cancel. The grid vertices are distinct: the
intersection of \(S_{ij}\) with \(P\cup T\) determines \(i\), and its
intersection with \(Q\cup R\) determines \(j\). Hence the remaining
negative coefficients occur on at most two coordinates/grid vertices and equal
\(-1\). The common load \(u\ge1\) supplies those temporary donors.
At \(j=r-s\), the formula becomes the corresponding row-start formula
with \(i\) replaced by \(i+1\), so the borrowed cells are restored as the
front advances. At the final corner it is

\[
 u+e_{S_{0,r-s}}+e_{S_{s,0}}.
\]

Thus every intermediate load is nonnegative. There are exactly
\(s(r-s)\) cells. \(\square\)

In particular the obstruction is a genuine long positive path, not a
disconnected-fibre example.

## 3. Exact floor/ceiling-balanced obstruction at rank \(m-1\)

Now put

\[
 V=[2m],\qquad r=m-1,\qquad
 N=\binom{2m}{m-1}.
 \tag{3.1}
\]

The exact arithmetic is

\[
 N={m\over m+1}W,\qquad
 W-N={W\over m+1}=\operatorname {Cat}_m=:B.
 \tag{3.2}
\]

Hence a floor/ceiling-balanced rank-\((m-1)\) load vector of total mass
\(W\) has exactly \(B\) entries equal to two and every other entry equal
to one.

For \(m\ge3\), choose disjoint \((m-1)\)-sets \(P,Q\), form \(C,D\) as in
Section 2, and choose a family

\[
 \mathcal R\subseteq\binom V{m-1}
 \setminus\{P,Q,C,D\},
 \qquad |\mathcal R|=B-2.
 \tag{3.3}
\]

Such a family exists because

\[
 N-4-(B-2)=(m-1)B-2\ge0
\]

for \(m\ge3\).

Put

\[
 u=\mathbf1+\sum_{S\in\mathcal R}e_S
 \tag{3.4}
\]

and define \(\mu,\nu\) by (2.3).

### Theorem 3.1 (calibrated first-band no-go)

Both \(\mu\) and \(\nu\) have total mass exactly \(W\); every load is one
or two; their point marginals are equal; and

\[
 \|\mu-\nu\|_1=4.
 \tag{3.5}
\]

Their abstract support-feasible unit-square distance is exactly

\[
 \boxed{\left\lfloor{(m-1)^2\over4}\right\rfloor.}
 \tag{3.6}
\]

The same number remains a lower bound even if arbitrary signed
intermediate vectors are allowed. A shortest nonnegative path may leave
the balanced box.

#### Proof

The common load (3.4) has \(B-2\) entries at two. Adding \(P,Q\), or
adding \(C,D\), gives exactly \(B\) entries at two. Equations
(3.2)--(3.4) prove the mass and balance claims. Equal point marginals and
(3.5) follow from Theorem 2.1. Equation (3.6) follows from
Theorems 2.1--2.2 with \(r=m-1\). The lower bound used no condition on
intermediate vectors, while the grid path is support-feasible because the
common load is at least one. \(\square\)

Every rank-\((m-1)\) square uses only \(m+1\) points. It therefore embeds
inside a calibrated top of size \(M=m+H\) whenever \(1\le H\le m\).
Restricting to top-local squares actually installed by a packet absorber
can only increase the distance in (3.6), provided each charged physical
selector projects to one unit elementary octahedron. A batched nonlocal
circuit is a different move model and can evade this unit-word metric.

This is an abstract load-fibre obstruction with exactly the calibrated
rank, mass, balance, and singleton-margin hypotheses. It is not proved
that both endpoints arise from actual calibrated packet selections with
their fixed segment-stitching baselines. Accordingly it refutes any
absorber theorem deduced from those coarse hypotheses alone, not every
more structured packet-residual theorem.

There is also a prescribed-repair version. Choose a new family
\(\mathcal R\) disjoint from \(\{P,Q,C,D\}\), with
\(|\mathcal R|=B-4\), and put

\[
 b=\mathbf1+\mathbf1_{\mathcal R}+e_P+e_Q,\qquad
 \mu'=b+e_P+e_Q,\qquad
 \nu'=b+e_C+e_D.
 \tag{3.7}
\]

Here \(B=\operatorname{Cat}_m\ge5\) and \(N-4\ge B-4\), so the required
family exists for \(m\ge3\).

Then \(\mu'\) has only two overload units above the balanced cap two,
whereas \(\nu'\) is exactly floor/ceiling balanced. They have equal point
margins, \(\ell_1\)-distance four, and the same exact quadratic square
distance. This obstructs transport to that prescribed balanced quota
vector. It does not rule out the possibility that some other balanced
endpoint is much closer to \(\mu'\).

## 4. A support-feasible implementation of one general exchange

The preceding obstruction does not mean that full-support fibres are
disconnected. A common unit reservoir implements every ordinary two-row
incidence exchange.

Let \(P,Q\) be \(r\)-sets, let

\[
 a\in P\setminus Q,\qquad b\in Q\setminus P,
\]

and put \(d=|P\setminus Q|\). The desired symmetric exchange is

\[
 P'=P-a+b,\qquad Q'=Q-b+a.
 \tag{4.1}
\]

If \(d=1\), the unordered pair \(\{P',Q'\}\) equals \(\{P,Q\}\), so no
load move is needed. Assume \(d\ge2\). Enumerate

\[
 (P\setminus Q)\setminus\{a\}=\{p_1,\ldots,p_{d-1}\},
\]

\[
 (Q\setminus P)\setminus\{b\}=\{q_1,\ldots,q_{d-1}\}.
\]

For \(0\le i\le d-1\), put

\[
 P_i=P-\{p_1,\ldots,p_i\}+\{q_1,\ldots,q_i\},
\qquad
 P_i'=P_i-a+b.
 \tag{4.2}
\]

Then

\[
 P_0=P,\qquad P_0'=P',\qquad
 P_{d-1}=Q',\qquad P_{d-1}'=Q.
 \tag{4.3}
\]

For \(0\le i<d-1\), define

\[
 \Delta_i
 =e_{P_i'}+e_{P_{i+1}}
  -e_{P_i}-e_{P_{i+1}'}.
 \tag{4.4}
\]

### Lemma 4.1 (positive exchange simulation)

Every \(\Delta_i\) in (4.4) is one octahedral square. If
\(u(S)\ge1\) for every \(r\)-set \(S\), then applying
\(\Delta_0,\Delta_1,\ldots,\Delta_{d-2}\) in this order gives a
support-feasible path

\[
 u+e_P+e_Q\longrightarrow u+e_{P'}+e_{Q'}
 \tag{4.5}
\]

of exactly \(d-1\) square moves. All helper loads are restored at the end.

#### Proof

The four sets in (4.4) share the core

\[
 P_i\setminus\{a,p_{i+1}\}
\]

and use the four distinct outside points

\[
 a,\ p_{i+1},\ b,\ q_{i+1}.
\]

Thus (4.4) is a square.

After applying the moves through index \(i<d-2\), the current vector is

\[
 u+e_Q+e_{P_0'}+e_{P_{i+1}}-e_{P_{i+1}'}.
 \tag{4.6}
\]

It is nonnegative because \(u(P_{i+1}')\ge1\). The next move consumes
\(P_{i+1}\) and the next common helper \(P_{i+2}'\), restores
\(P_{i+1}'\), and creates \(P_{i+2}\). At the last move,
\(P_{d-1}'=Q\), so the extra copy of \(Q\) is consumed and the final
vector is \(u+e_{P_0'}+e_{P_{d-1}}\). Use (4.3). \(\square\)

The proof uses common slack only on the helper cells

\[
 P_1',P_2',\ldots,P_{d-2}'.
\]

Thus a chosen sequence of ordinary symmetric exchanges is positively
implementable whenever all helper cells in its chains have one common
unit of load. Full support (5.1) is a convenient uniform sufficient
condition, not a necessary condition for an individual instance. This
helper-reservoir formulation is the weakest support hypothesis used by the
construction.

## 5. Interior connectivity at the correct quadratic scale

We use the elementary binary-interchange lemma.

### Lemma 5.1 (binary incidence interchanges)

Let \(M,N\) be \(k\times v\) zero-one matrices with the same row sums
\(r\) and the same column sums. Then \(M\) can be transformed into \(N\)
by at most \(rk\) ordinary \(2\times2\) interchanges.

#### Proof

We first prove an occupancy-cycle lemma independent of the target matrix.
In any binary matrix, suppose a simple row--column cycle has occupied
edges

\[
 i_jc_j\qquad(1\le j\le\ell)
\]

and vacant edges

\[
 i_{j+1}c_j\qquad(1\le j\le\ell),
\]

with cyclic row indices. In current row \(i_1\), let \(t\) be the least
index \(2\le t\le\ell\) for which the entry at \(c_t\) is zero. Such a
\(t\) exists because \(i_1c_\ell\) is the closing vacant cycle edge.

For \(h=t,t-1,\ldots,2\), interchange rows \(i_1,i_h\) and columns
\(c_{h-1},c_h\). At that moment their \(2\times2\) pattern is

\[
 \begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

Indeed the zero in pivot row \(i_1\) moves one column left at every step,
while \(i_hc_{h-1}\) and \(i_hc_h\) are the untouched vacant and occupied
cycle edges. The intermediate pivot-row entries
\(c_2,\ldots,c_{t-1}\) are restored as the zero moves left.

If \(t=\ell\), these \(t-1\) switches reverse the whole cycle. If
\(t<\ell\), the newly occupied chord \(i_1c_t\), together with the
remaining cycle entries, is another occupied/vacant cycle with
\(\ell-t+1\) occupied edges. Induction toggles it in at most
\(\ell-t\) further switches. Thus the original cycle costs at most
\(\ell-1\), and every entry off that cycle, including the temporary chord,
returns to its initial value.

Now colour the entries in \(M-N\): a \(+1\) entry is red and a \(-1\)
entry is blue. Orient red edges from rows to columns and blue edges from
columns to rows. Equal row and column sums make this directed bipartite
difference Eulerian, so it decomposes into edge-disjoint directed simple
alternating cycles. Apply the occupancy-cycle lemma to each one.

Processing the edge-disjoint cycles sequentially costs at most the total
number of red entries, which is at most \(rk\). \(\square\)

### Theorem 5.2 (positive interior Markov theorem)

Suppose

\[
 \mu(S)\ge1,\qquad \nu(S)\ge1
 \qquad(S\in\binom Vr)
 \tag{5.1}
\]

and \(\partial_1\mu=\partial_1\nu\). Then there is a support-feasible
sequence of unit octahedral squares from \(\mu\) to \(\nu\) of length at
most

\[
 \boxed{
 T\le {s(s-1)\over2}\|\mu-\nu\|_1,
 \qquad s=\min\{r,|V|-r\}.}
 \tag{5.2}
\]

#### Proof

Complement every set first if \(r>|V|/2\). Equal point margins imply
equal total mass. Hence the complemented signed difference still has zero
point margins, because

\[
 \sum_{T\ni x}(\mu-\nu)(V\setminus T)
 =\sum_S(\mu-\nu)(S)-\sum_{S\ni x}(\mu-\nu)(S)=0.
\]

Complementation also preserves nonnegativity, \(\ell_1\)-distance, and
elementary octahedral moves. Explicitly, with

\[
 E=V\setminus(K\cup\{a,b,c,d\}),
\]

the complement of \(\omega(K;a,b,c,d)\) is, up to the same harmless sign
convention, \(\omega(E;a,b,c,d)\), and
\(|E|=(|V|-r)-2\). We may therefore assume
\(r=s\le |V|/2\).

Remove the common load

\[
 u(S)=\min\{\mu(S),\nu(S)\}.
\]

The positive and negative residual multisets each contain

\[
 k={1\over2}\|\mu-\nu\|_1
\tag{5.3}
\]

rank-\(r\) sets. Label their copies and form their \(k\times |V|\)
incidence matrices. Equal point margins give equal column sums; every row
has sum \(r\). Lemma 5.1 supplies at most \(rk\) ordinary binary
interchanges.

One interchange acts on two current \(r\)-sets \(P,Q\) by the symmetric
exchange (4.1). If \(d=|P\setminus Q|=1\), it only permutes the two
unlabelled row sets and costs no load move; relabel the two residual copies
before continuing. If \(d\ge2\), Lemma 4.1
implements it with \(d-1\le r-1\) octahedral squares. Hypothesis (5.1)
gives \(u(S)\ge1\) for every helper cell, and every helper is restored
before the next matrix interchange.

Thus the whole sequence stays nonnegative and has length at most

\[
 s k(s-1)
 ={s(s-1)\over2}\|\mu-\nu\|_1.
\]

At the end the residual multiset is the negative residual multiset, so the
load vector is \(\nu\). \(\square\)

Theorem 2.2 is sharper on the four-support witness: its exact positive
distance is \(\lfloor r^2/4\rfloor\). Thus the quadratic scale in
Theorem 5.2 is genuine, not an artifact of an unreachable pair.

## 6. Consequences for calibrated rectangle absorbers

Theorem 5.2 gives the weakest simple density hypothesis presently proved:
one common unit in every rank-\(r\) cell. This hypothesis is compatible
with central floor/ceiling loads, whose floor is at least one. It removes
the old sparse obstruction

\[
 e_{123}+e_{456}\not\longrightarrow
 e_{234}+e_{156}
\]

by supplying the helper cells used in Lemma 4.1.

It does **not** give the coefficient-safe bound requested by a final
absorber. Theorem 3.1 shows that even exact \(1/2\)-balanced loads can
require \(\Theta(m^2)\) unit target-rank octahedra to move four units of
\(\ell_1\)-mass, and hence the same number of installed rectangle bits
under one-bit/one-square charging. Increasing every load by an arbitrary
common constant does not alter this lower bound.

Therefore any theorem of the form

\[
 T\le C\|\mu-\nu\|_1
\tag{6.1}
\]

with \(C\) uniform in the growing rank must assume more than:

* nonnegativity;
* exact floor/ceiling balance;
* equality of total mass;
* equality of all point marginals; and
* arbitrary uniform pointwise slack.

A necessary additional condition is the pair-cut bound

\[
 \boxed{
 |\Phi_A(\mu)-\Phi_A(\nu)|
 \le C\|\mu-\nu\|_1
 \quad\text{for every }A\subseteq V.}
 \tag{6.2}
\]

This condition is not asserted sufficient. It is the first explicit slow
mode missed by point calibration. In dual language, a linear square-word
bound must control every load potential whose octahedral second difference
is bounded; (0.3) supplies a concrete sharp family.

There is a full shadow hierarchy behind this warning. For
\(2\le j\le r\), let

\[
 (\Gamma_jx)(T)=\sum_{S\supseteq T}x(S),
 \qquad T\in\binom Vj.
\]

One elementary square has exactly

\[
 4\binom{r-2}{j-2}
\]

nonzero \(j\)-shadow coordinates, each equal to \(1\) or \(-1\): choose
\(j-2\) points of the common core and one of the four signed tip-pairs.
All subsets using at most one tip cancel, and no edge contains three tips.
Hence
every square path also obeys

\[
 T\ge
 {\|\Gamma_j(\mu-\nu)\|_1
  \over4\binom{r-2}{j-2}}.
 \tag{6.3}
\]

Pair-shadow control is therefore necessary but need not exhaust the slow
metric modes.

There are three honest escapes for the packet programme.

1. Build the calibrated near-factor so that its residual already obeys
   pair-cut bounds such as (6.2), in addition to point marginals.
2. Allow higher-order support-feasible circuits which change
   \(\Phi_A\) by \(\Theta(r^2)\) in one physically charged move.
3. Budget the proved worst-case
   \(O(r^2\|\mu-\nu\|_1)\) abstract square-distance bound. At
   \(r\asymp m\), this is too large for the proposed one-bit-per-top final
   absorber unless the residual is smaller by a corresponding \(m^2\)
   factor.

The obstruction concerns transport to a **prescribed** near-balanced
vector. It does not refute an adaptive absorber which may choose whichever
balanced endpoint lies in the starting vector's short square-metric
neighborhood. Such an adaptive theorem would need to be stated and proved
with that weaker quantifier.

## 7. Audit ledger

### Proved

1. The pair-cut potential is one-Lipschitz under every unit octahedral
   square.
2. Strictly positive, arbitrarily slack, equal-margin loads at
   \(\ell_1\)-distance four can have square distance
   \(\lfloor r^2/4\rfloor\).
3. The same obstruction occurs for exact total-\(W\), floor/ceiling
   \(1/2\)-balanced loads at rank \(m-1\) on \([2m]\).
4. One common unit in every cell makes every ordinary symmetric exchange
   support-feasible in \(d-1\) squares.
5. Full common support connects any two vectors in the strictly positive
   part of a point-margin fibre in at most
   \(\frac12s(s-1)\|\mu-\nu\|_1\) square moves, where
   \(s=\min(r,|V|-r)\).
6. The quadratic rank dependence is order-sharp.

### Not proved

1. Pair-cut balance (6.2) is not proved sufficient for linear square
   distance.
2. The support-feasible square path is an abstract load path. Assigning
   every used square injectively to an actually installed calibrated top
   and segment pair is an additional availability problem.
3. No adaptive short-endpoint theorem is proved.

The positivity gate is therefore resolved for the strictly positive
abstract load fibre: full common support gives connectivity, but the
desired \(O(\ell_1)\) unit-square length is impossible. Sparse fibres and
physical top/segment availability remain separate. The decisive
obstruction here is quadratic square-word geometry, not nonnegativity or
the integer lattice.
