# The CCTPF full-history polytope has a literal odd-port obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

This note formulates the exact single full-history selection problem behind
CCTPF and proves that the common-core degree caps do **not** make its natural
flow relaxation integral.

For every sufficiently large calibrated pair \((m,H)\), there is a physical
three-top, two-option-per-top subcatalogue with all of the following
properties.

1. Every option is one literal core-safe tail order with one exact nested
   CCTPF tag profile.
2. In the induced three-root subsystem, every middle or active signed target
   occurs in at most two of the six options.  Consequently weight \(1/2\) on
   every option is an exact root-saturating fractional full-history solution
   respecting every target capacity of that subsystem.
3. The compatible-top degree inside that subsystem is at most two, hence is
   below every active common-core cap.  Moreover, the three prescribed cores
   extend to a core assignment on all tops satisfying the full global caps.
4. For each bit \(b\in\{0,1\}\), three literal lower depth-one targets give
   the matrix

   \[
   \begin{pmatrix}
   1&1&0\\
   0&1&1\\
   1&0&1
   \end{pmatrix},                                             \tag{0.1}
   \]

   of determinant \(2\).  Any integral root selection would have to
   properly two-colour a triangle, which is impossible.

Thus the exact local tail-order DAGs are integral, but coupling them by
physical target capacities is an unsplittable multicommodity path problem,
not a one-commodity network flow.  The missing inequalities are genuine
odd-set/port inequalities.

This is a no-go for total unimodularity, and for an integrality theorem that
uses only the already proved common-core caps and target rows.  It is
**not** a counterexample to CCTPF for the complete physical catalogue: each
top there has many options outside the six used below.  The half vector is
root-saturating only on the induced three-root subsystem.  A positive proof
must show that complete root fibres globally destroy or absorb every odd
port mesh.

## 1. Exact full-history formulation

Retain the CCTPF notation

\[
M=m+H,\qquad s=m-H,\qquad L=m-3H+1,
\tag{1.1}
\]

and the nonincreasing quota profile

\[
b_0=L\ge b_1\ge\cdots\ge b_{H-1}\ge b_H=0.
\tag{1.2}
\]

For a fixed top \(U\) and fixed core \(Q_U\), let \(\Omega_U\) be the set
of pairs \(\omega=(w,d)\), where

* \(w\) is a permutation of \(S_U=U\setminus Q_U\); and
* \(d:[L]\to\{0,\ldots,H-1\}\) satisfies

  \[
  |\{j:d(j)\ge q\}|=b_q\qquad(0\le q<H).
  \tag{1.3}
  \]

For \(1\le j\le L\) and \(0\le\ell\le2H\), write

\[
R_{j,\ell}=\{j+2H-\ell,\ldots,j+2H-1\}\subseteq[s].
\tag{1.4}
\]

If \(w=(w_1,\ldots,w_s)\), the physical target in this cell is

\[
T_{j,\ell}(w)=U\setminus\{w_t:t\in R_{j,\ell}\}.
\tag{1.5}
\]

The middle target has \(\ell=H\).  At signed depth \(q\), the upper and
lower targets have deletion lengths \(H-q\) and \(H+q\), respectively,
and are active precisely when \(d(j)\ge q\).

Let \({\cal T}\) consist of the middle layer and all active internal signed
layers.  Put

\[
a_{T,\omega}=
\begin{cases}
1,&\text{if the history \(\omega\) uses \(T\),}\\
0,&\text{otherwise.}
\end{cases}
\tag{1.6}
\]

The exact CCTPF selection system is

\[
\sum_{\omega\in\Omega_U}x_{U,\omega}=1
\qquad(U\in\tbinom{[2m]}M),                                  \tag{1.7}
\]

\[
\sum_U\sum_{\omega\in\Omega_U}a_{T,\omega}x_{U,\omega}\le1
\qquad(T\in{\cal T}),                                        \tag{1.8}
\]

\[
x_{U,\omega}\in\{0,1\}.                                    \tag{1.9}
\]

Each \(\Omega_U\) is the source--sink path set of a finite acyclic state
graph: the state remembers the exposed prefix of the permutation and the
remaining tag census.  Hence the convex hull for one root is a network-flow
polytope.  The difficulty in (1.7)--(1.9) is entirely in the shared resource
rows (1.8).

If one identifies target occurrences by a common capacity-one network arc,
flow may enter that arc carrying the prefix state of one root and leave it
through the continuation port of another root.  Such a splice need not obey
the diagonal/diamond identities of one tail order.  Keeping the root and
prefix state on both sides prevents the splice, but then the common target
capacity is a side constraint coupling distinct commodities.  The theorem
below makes this failure integral and physical.

The paired quotient-chain theorem does not remove this coupling.  That
theorem starts with a core of occurrences whose paired maps

\[
\Theta_q=(T^-_q,T^+_q)
\tag{1.10}
\]

already have coordinate-injective projections and already coarsen with
depth.  It then chooses nested representatives inside that core.  In CCTPF,
choosing one history per root while making those coordinate projections
injective is the selection problem itself.  Applying paired quotient-chain
integrality before solving (1.7)--(1.9) would therefore assume the decisive
premise.  The obstruction below occurs exactly when the first lower
coordinate projection is formed.

## 2. A two-port tail-order lemma

We first isolate the only word construction needed in the obstruction.

### Lemma 2.1 (one hidden entrance and one interior port)

Suppose \(m\ge11H+4\) and \(H\ge2\).  Let

\[
S=P\mathbin{\dot\cup}E^{\rm L}\mathbin{\dot\cup}E^{\rm I},
\qquad |S|=s,qquad |E^{\rm L}|=|E^{\rm I}|=H,
\tag{2.1}
\]

where \(|P|=m-3H\).  For \(b\in\{0,1\}\), prescribe distinct markers

\[
x_{\rm L}^b,x_{\rm I}^b\in P.
\tag{2.2}
\]

There are two permutations \(w^0,w^1\) of \(S\) such that:

1. in \(w^b\), positions \(H,\ldots,2H-1\) are the elements of
   \(E^{\rm L}\), and position \(2H\) is \(x_{\rm L}^b\);
2. putting \(p=5H-1\), positions \(p,\ldots,p+H-1\) are the elements of
   \(E^{\rm I}\), and position \(p+H\) is \(x_{\rm I}^b\);
3. for \(E=E^{\rm L}\) and for \(E=E^{\rm I}\), no interval of length
   \(H+q\), \(1\le q<H\), in \(w^0\) which contains \(E\) has the same
   underlying set as an interval of that length in \(w^1\) which contains
   \(E\);
4. \(E^{\rm L}\) is not an eligible middle deletion interval, while
   \(E^{\rm I}\) is one.

Moreover, both displayed \((H+1)\)-intervals are eligible lower-depth-one
deletion intervals.  Their phase indices are \(1\) and \(4H\).

#### Proof

For each \(E\in\{E^{\rm L},E^{\rm I}\}\) and bit \(b\), choose a collar

\[
D_{E,b}=D^-_{E,b}\mathbin{\dot\cup}D^+_{E,b}\subset P,
\qquad |D^-_{E,b}|=H-1,\quad |D^+_{E,b}|=H,                 \tag{2.3}
\]

so that the four collars are pairwise disjoint and the appropriate marker
is in \(D^+_{E,b}\).  This is possible because

\[
|P|=m-3H\ge8H-4.                                             \tag{2.4}
\]

In \(w^b\), place

\[
D^-_{E^{\rm L},b},\ E^{\rm L},\ D^+_{E^{\rm L},b}
\tag{2.5}
\]

in positions \(1,\ldots,3H-1\), ordering the right collar so that
\(x_{\rm L}^b\) is first.  Put arbitrary unused letters in positions
\(3H,\ldots,4H-1\).  Place

\[
D^-_{E^{\rm I},b},\ E^{\rm I},\ D^+_{E^{\rm I},b}
\tag{2.6}
\]

in positions \(4H,\ldots,7H-2\), again putting
\(x_{\rm I}^b\) first in the right collar.  Fill every remaining position
arbitrarily with the unused letters.  The numerical hypothesis ensures
that all displayed positions exist.

An interval of length \(H+q\), \(1\le q<H\), which contains all \(H\)
consecutive positions occupied by \(E\), uses exactly \(q\) additional
positions, all in the adjacent collar \(D_{E,b}\).  Thus its underlying
set is

\[
E\mathbin{\dot\cup}Z_b,qquad
\varnothing\ne Z_b\subseteq D_{E,b}.                         \tag{2.7}
\]

The bit-zero and bit-one collars are disjoint, so the two sets in (2.7)
cannot agree.  This proves Item 3.

By (1.4), eligible middle \(H\)-intervals start in positions

\[
H+1,H+2,\ldots,s-H+1.                                       \tag{2.8}
\]

The block \(E^{\rm L}\) starts at position \(H\), so it is hidden just
outside the middle entrance port.  The block \(E^{\rm I}\) starts at
\(p=5H-1\), which lies in (2.8).  Eligible \((H+1)\)-intervals start in

\[
H,H+1,\ldots,s-H.                                            \tag{2.9}
\]

Hence \(E^{\rm L}\cup\{x_{\rm L}^b\}\) and
\(E^{\rm I}\cup\{x_{\rm I}^b\}\) are eligible.  Solving
\(j+H-1=H\) and \(j+H-1=p\) gives phase indices \(1\) and \(4H\).
\(\square\)

The hidden middle interval in Item 4 is the literal entrance-port effect.
It is why a cyclic orientation of three ports below avoids an unintended
middle target of fractional load two.

## 3. The physical odd-port construction

### Theorem 3.1 (six literal histories with fractional value three and
integral value at most two)

For every sufficiently large calibrated \((m,H)\), there are three
rank-\(M\) tops \(U_1,U_2,U_3\), one fixed \(2H\)-core in each top, and two
literal tagged core-safe histories \(P_i^0,P_i^1\) at every top, such that:

1. the six histories admit a root-saturating fractional selection obeying
   all physical target capacities;
2. no collision-free integral selection can choose one history at every
   root; and
3. the common-core compatible-target degree caps hold.

#### Proof

All indices below are read modulo three.  Choose pairwise disjoint sets

\[
|C|=m-H,qquad |A_1|=|A_2|=|A_3|=H,                          \tag{3.1}
\]

and put

\[
U_i=C\cup A_i\cup A_{i+1}.                                  \tag{3.2}
\]

Their union has size \(m+2H\le2m\), so the construction embeds in
\([2m]\).  We have

\[
|U_i|=m+H=M,                                                  \tag{3.3}
\]

\[
U_i\cap U_{i+1}=C\cup A_{i+1}=:K_i,qquad |K_i|=m,            \tag{3.4}
\]

and

\[
U_1\cap U_2\cap U_3=C,qquad |C|=m-H.                        \tag{3.5}
\]

For each edge \(i(i+1)\) and bit \(b\), choose six globally distinct
points

\[
x_i^b\in C.                                                   \tag{3.6}
\]

Choose one common set

\[
Q\in\binom{C\setminus\{x_i^b:i\in\mathbb Z_3, b\in\{0,1\}\}}{2H}
\tag{3.7}
\]

and use \(Q_{U_i}=Q\) for all three tops.

Define the six desired lower depth-one targets

\[
R_i^b=K_i\setminus\{x_i^b\}.                                 \tag{3.8}
\]

At the endpoint \(U_i\), the deletion set producing \(R_i^b\) is

\[
U_i\setminus R_i^b=A_i\cup\{x_i^b\};                        \tag{3.9}
\]

at the other endpoint \(U_{i+1}\), it is

\[
U_{i+1}\setminus R_i^b=A_{i+2}\cup\{x_i^b\}.                \tag{3.10}
\]

Fix a root \(U_i\).  In Lemma 2.1 take

\[
E^{\rm L}=A_i,qquad E^{\rm I}=A_{i+1},qquad P=C\setminus Q,
\tag{3.11}
\]

with markers

\[
x_{\rm L}^b=x_i^b,qquad x_{\rm I}^b=x_{i-1}^b.              \tag{3.12}
\]

The collar sets required for this root can be chosen inside \(C\setminus
Q\), independently of the choices at the other roots.  Complete the two
permutations from Lemma 2.1 and order \(Q\) arbitrarily.  This gives two
literal core-safe tail orders \(P_i^0,P_i^1\).

For sufficiently large \(m\), the calibrated CCTPF profile satisfies

\[
b_1=L-1.                                                      \tag{3.13}
\]

Indeed \(N_1/N_H=(m/(m+1))\Lambda\) and
\(\Lambda\ge L+c_0H\).  In particular, the two phase indices \(1\) and
\(4H\) may both be made active at depth one.  Since the sequence \(b_q\)
is nonincreasing, choose nested active phase sets of sizes \(b_q\) which
contain both phases at depth one, and define their stopping tags by last
membership.  This supplies an exact admissible tag profile on every one of
the six histories.

Equations (3.9)--(3.12) and Lemma 2.1 show that

\[
R_i^b\in P_i^b\cap P_{i+1}^b                              \tag{3.14}
\]

as an active lower depth-one target.  Therefore, for each fixed bit \(b\),
the three target rows \(R_1^b,R_2^b,R_3^b\) and history columns
\(P_1^b,P_2^b,P_3^b\) contain the incidence matrix (0.1).

We next audit every other target row.  A target common to histories on two
different roots \(U_i,U_j\) must be contained in \(U_i\cap U_j\), which
has size \(m\).

* At an upper rank \(m+q\), \(q>0\), this is impossible.
* At the middle rank it must equal \(K_i=U_i\cap U_{i+1}\).  At the
  cyclically designated endpoint \(U_i\), producing \(K_i\) would require
  the middle deletion interval \(A_i\).  This is the hidden left block of
  Lemma 2.1 and is not eligible.  Hence no middle target occurs on both
  endpoints of an edge.  The interior endpoint may use it in both of its
  bit options, giving multiplicity exactly two but no more.
* At a lower rank \(m-q\), \(1\le q<H\), a target shared across the edge
  \(i(i+1)\) forces the deletion interval at each endpoint to contain that
  endpoint's exclusive \(H\)-set.  Lemma 2.1(3) says that the two bit
  options at a fixed endpoint cannot have the same such deletion interval.
  Thus at most one bit option per endpoint can use the target.

Finally, no internal lower target can belong to all three roots, because

\[
m-q>m-H=|U_1\cap U_2\cap U_3|\qquad(q<H).                    \tag{3.15}
\]

Within one literal history, targets at a fixed rank are distinct.  It
follows that **every** middle or active signed target occurs in at most two
of the six histories.  Consequently

\[
x(P_i^b)=\frac12\qquad(i\in\mathbb Z_3, b\in\{0,1\})        \tag{3.16}
\]

satisfies each root equation and every target capacity inequality.

On the other hand, an integral root-saturating selection chooses a bit
\(b_i\) at root \(i\).  By (3.14), collision-freeness on edge \(i(i+1)\)
requires

\[
b_i\ne b_{i+1}.                                               \tag{3.17}
\]

The three inequalities (3.17) would be a proper two-colouring of an odd
cycle, impossible.  Hence the maximum number of roots simultaneously
saturated by these six histories is at most two.

It remains to check the advertised caps.  In this three-root instance, a
compatible internal target belongs to at most two tops by (3.4)--(3.5).
For the middle rank,

\[
\frac{\binom{s}{H}}L\longrightarrow\infty.                  \tag{3.18}
\]

For the lower sign, \(\binom{s}{H+q}/b_q\to\infty\) uniformly whenever
\(b_q>0\).  For the upper sign, put \(k=H-q\).  If \(b_q>0\), then
\(N_q/N_H\ge2\).  Since \(H=o(m)\),

\[
\log\frac{N_q}{N_H}
=\sum_{t=q+1}^{H}\log\frac{m+t}{m-t+1}
\le \frac{3H(H-q)}m                                           \tag{3.19}
\]

for all sufficiently large \(m\).  Therefore

\[
k=H-q\ge\frac{(\log2)m}{3H}\longrightarrow\infty.           \tag{3.20}
\]

As \(b_q\le L<s\), this gives

\[
\frac{d_q}{b_q}
=\frac{\binom{s}{H-q}}{b_q}\longrightarrow\infty.           \tag{3.21}
\]

Indeed \(\binom{s}{k}\ge(s/k)^k\), while
\(k\ge(\log2)m/(3H)\to\infty\) and \(k\le H=o(s)\).

Thus the compatible degree two is below every active cap
\(d_r/b_{|r|}\) for sufficiently large \(m\).  This proves all three
claims. \(\square\)

### Proposition 3.2 (the three prescribed cores coexist with the global
caps)

The three core prescriptions in Theorem 3.1 can be extended to a core
assignment on **every** rank-\(M\) top satisfying all of the audited
common-core maximum-degree caps.

#### Proof

Fix the three displayed cores and choose the core of every other top
independently and uniformly.  For a target \(Y\) at any protected rank,
its deterministic contribution from the three exceptional tops is at most
three.  The remaining random degree is bounded by the same binomial variable
used in the random-core cap theorem, with mean at most

\[
\mu_r=\frac{d_r}{\Lambda_r}.                                 \tag{3.22}
\]

At the middle rank, the additive gap between the cap and the mean is

\[
\frac{d_0}{L}-\frac{d_0}{\Lambda}
=\frac{d_0(\Lambda-L)}{L\Lambda}\longrightarrow\infty.       \tag{3.23}
\]

At a signed rank with \(b_{|r|}>0\), it is

\[
\frac{d_r}{b_{|r|}}-\frac{d_r}{\Lambda_r}
=\frac{d_r(\Lambda_r-b_{|r|})}
       {b_{|r|}\Lambda_r}\longrightarrow\infty.             \tag{3.24}
\]

The last divergence, uniformly over the protected ranks, is contained in
the audited estimate \(d_r/\Lambda_r^3\gg m\); in particular subtracting
three from every cap preserves at least half of the original Chernoff
margin for large \(m\).  The Chernoff exponents therefore change only by an
absolute factor and remain \(\gg m\).  The same union bound over all targets
and ranks succeeds.  Adding back the at most three prescribed contributions
gives the original caps. \(\square\)

Consequently the determinant-two minor below occurs inside a fixed-core
physical catalogue whose cores satisfy the full global cap theorem, not
merely in an isolated choice of three cores.

## 4. The exact odd-set and determinant certificates

For fixed \(b\), the three configurations \(P_1^b,P_2^b,P_3^b\) are
pairwise conflicting.  Hence every integral solution satisfies the valid
odd-clique inequality

\[
\boxed{\sum_{i=1}^3x(P_i^b)\le1.}                            \tag{4.1}
\]

The three pairwise target rows imply only

\[
2\sum_{i=1}^3x(P_i^b)\le3,                                  \tag{4.2}
\]

which admits the half vector.  Summing (4.1) over \(b=0,1\) gives at most
two selected histories, whereas the three root equations demand three.

Algebraically, (0.1) has determinant

\[
1(1)-1(-1)=2.                                                 \tag{4.3}
\]

Thus the physical target--history matrix is not totally unimodular even
after fixing all cores, restricting to literal tail orders, imposing the
exact tag census, and keeping every target row at degree at most two.

The obstruction is a port obstruction, not a scalar Hall cut.  Each
individual root path polytope is integral; each individual target has ample
common-core capacity; and the displayed half point passes every nonnegative
target-capacity inequality.  What fails is the parity of simultaneously
choosing compatible entrance/continuation ports around an odd mesh.

## 5. Precise boundary for CCTPF

Theorem 3.1 proves the following no-go statement.

> The common-core maximum-degree caps and target-capacity rows do not make
> the literal full-history matrix totally unimodular.  Even a root-saturating
> fractional distribution on a physical restricted subcatalogue need not
> round inside that subcatalogue.  In particular, CCTPF cannot follow from a
> totally-unimodular one-commodity flow whose only coupling constraints are
> physical target capacities.

It does not prove that the complete CCTPF catalogue is infeasible.  The
unrestricted catalogue may route each of the three roots through a third
tail order and escape the six-column face.  A positive CCTPF proof must
therefore establish at least one genuinely global assertion of the
following kind:

1. every physical odd port mesh has an alternating augmentation through
   options outside the mesh;
2. the aggregate deficiency of unaugmentable odd meshes is \(o(W)\); or
3. a stronger integral polytope including the required odd-set/blossom
   inequalities still has a root-saturating point.

Separate signed Hall theorems, the common fractional point, local Birkhoff
integrality of each tail order, and the common-core degree caps do not supply
any of these statements.
