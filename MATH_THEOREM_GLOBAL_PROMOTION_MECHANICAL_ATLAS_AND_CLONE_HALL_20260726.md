# Global promotion-ring resolution: a simultaneous mechanical atlas and exact clone Hall theorem

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Outcome

Put

\[
 V=[2m],\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H},
\tag{0.1}
\]

where

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 \theta=\frac{MN_H}{W}=1+o(1).
\tag{0.2}
\]

A root is \(A\in\binom V{m-H}\), its top is \(U=A^c\), and a cyclic
frame \(\pi\) on \(U\) has middle deck

\[
 \mathcal D(A,\pi)
 =\{A\cup I_\pi(i,H):i\in\mathbb Z_M\}.
\tag{0.3}
\]

Deleting one phase gives a repaired frame with \(M-1\) middle targets.

This note proves a positive global reduction which is not a local-block
construction.

1. Fix one balanced half \(P\in\binom Vm\). For every root there is an
   explicit cyclic mechanical \(0\)-\(1\) pattern such that every
   interval length is balanced simultaneously. Arbitrary labelings of
   its \(P\)- and \(P^c\)-positions remain legal tight Hamilton cycles.

2. One mechanical frame at every root has aggregate middle
   \(P\)-profile within \(o(W)\) of the complete middle layer. The same
   statement holds at every direct entrance length
   \[
                         r=m-q,\qquad q=o(\sqrt m).
   \tag{0.4}
   \]
   One deletion per root changes the combined discrepancy by only
   \(2N_H=o(W)\).

3. More strongly, after forgetting only the requirement that the
   \(M-1\) phase choices at one root come from one common labeling, the
   resulting literal source--target graph has an integral matching
   covering \(W-o(W)\) individual middle targets. It also has,
   separately, an integral matching covering \(N_q-o(W)\) individual
   entrance targets. These are exact Hall theorems inside the restricted
   mechanical support, not merely profile averages.

Thus neither a balanced-half Gaussian cut nor any raw one-row Hall cut
survives in this atlas. The only remaining condition is a common
permutation coupling:

> for each root, the middle and entrance targets assigned to all its
> phase clones must be the interval rows of one labelled cyclic order.

This common-order condition is root-local in form but cannot be rounded
rootwise. The block-factor hole theorem forces any successful rounding
law to correlate essentially the entire
\(\binom mH\)-root star of almost every middle target. Accordingly,
nothing below proposes independent blocks, bounded trades, or a product
of local resolutions.

No raw repaired-ring factor is constructed here. The advance is that the
global gate is reduced from arbitrary target Hall to a precise
**cross-root permutation-coupling problem over an explicitly
profile-correct support atlas**.

## 1. The exact repaired-resolution normal form

Let \(\mathscr H^-\) be the formal rooted repaired catalogue. A column is
a triple

\[
                         e=(A,\pi,s),
\tag{1.1}
\]

where \(\pi\) is an oriented cyclic order on \(U=A^c\), modulo rotation,
and \(s\in\mathbb Z_M\) is the deleted phase. It contains the root marker
\(A\) and the \(M-1\) middle targets

\[
                         A\cup I_\pi(i,H),\qquad i\ne s.
\tag{1.2}
\]

Columns are retained with multiplicity, as required for a resolution
colouring. Every root has degree

\[
                         Q=M(M-1)!=M!.
\tag{1.3}
\]

Every middle target has degree

\[
\begin{aligned}
 D^-_0
 &=\binom mH H!m!(M-1)\\
 &=Q\,\frac{(M-1)N_H}{W}.
\end{aligned}
\tag{1.4}
\]

Indeed, choose its root in \(\binom mH\) ways, order its prescribed
\(H\)-window in \(H!m!\) cyclic frames, and delete any of the other
\(M-1\) phases.

### Proposition 1.1 (resolution-colouring gate)

Suppose the packing-side calibration satisfies

\[
                         (M-1)N_H\le W.
\tag{1.5}
\]

A proper \(Q\)-edge-colouring of \(\mathscr H^-\), with conflicts on
roots and middle targets, is equivalent to a resolution into \(Q\)
classes such that every class

1. contains exactly one repaired frame at every root; and
2. repeats no middle target.

Every class then covers \((M-1)N_H\) targets and has

\[
                         W-(M-1)N_H=o(W)
\tag{1.6}
\]

middle holes.

#### Proof

The \(Q\) formal columns at a fixed root form a clique. In a proper
colouring with \(Q\) colours they therefore use every colour exactly
once. Hence every colour class contains one repaired frame at every
root. Properness on middle rows gives disjoint middle decks. The
converse is the same argument backwards. Equation (1.6) follows from
(0.2). \(\square\)

Proposition 1.1 is a sufficient exact global object, not a claim that
the colouring exists. It exposes why a resolvable design would solve the
middle gate and why the required correlation is catalogue-wide.

## 2. One cyclic pattern balances every interval length

### Lemma 2.1 (cyclic mechanical word)

For every \(0\le t\le M\), define the bi-infinite binary word

\[
 b_i=
 \left\lfloor\frac{(i+1)t}{M}\right\rfloor
 -\left\lfloor\frac{it}{M}\right\rfloor,
 \qquad i\in\mathbb Z.
\tag{2.1}
\]

It has period \(M\), exactly \(t\) ones in a period, and, for every
\(0\le s\le M\), every cyclic length-\(s\) interval has weight

\[
              \left\lfloor\frac{st}{M}\right\rfloor
 \quad\text{or}\quad
              \left\lceil\frac{st}{M}\right\rceil.
\tag{2.2}
\]

The number of intervals having the upper value is

\[
              st-M\left\lfloor\frac{st}{M}\right\rfloor.
\tag{2.3}
\]

#### Proof

Replacing \(i\) by \(i+M\) adds \(t\) to both floors, so the word is
periodic. Telescoping gives

\[
 \sum_{j=0}^{s-1}b_{i+j}
 =\left\lfloor\frac{(i+s)t}{M}\right\rfloor
  -\left\lfloor\frac{it}{M}\right\rfloor,
\tag{2.4}
\]

which is one of the two values in (2.2). Summing (2.4) over
\(i\pmod M\), every one is counted \(s\) times, so the total is \(st\).
This forces (2.3). \(\square\)

Fix \(P\in\binom Vm\). For a root \(A\), put \(U=A^c\) and

\[
                         t=|U\cap P|.
\tag{2.5}
\]

Place the labels of \(U\cap P\) bijectively in the one-positions of
(2.1), and the labels of \(U\setminus P\) in the zero-positions. The two
internal bijections are deliberately left free. Every placement is an
ordinary labelled cyclic frame on \(U\), so its \(H\)-windows form one
literal tight Hamilton cycle.

For a root-form middle target \(D=A\cup J\), Lemma 2.1 gives

\[
 |D\cap P|\in
 \left\{
 m-t+\left\lfloor\frac{Ht}{M}\right\rfloor,\,
 m-t+\left\lceil\frac{Ht}{M}\right\rceil
 \right\}.
\tag{2.6}
\]

For a direct interval target \(S=I_\pi(i,r)\), the same frame gives

\[
 |S\cap P|\in
 \left\{
 \left\lfloor\frac{rt}{M}\right\rfloor,\,
 \left\lceil\frac{rt}{M}\right\rceil
 \right\}.
\tag{2.7}
\]

The simultaneity in \(r\) is essential: middle and entrance have not
been encoded as independent rows.

## 3. Exact profile census and its asymptotics

There are exactly

\[
 n_t=\binom mt\binom m{t-H},
 \qquad H\le t\le m,
\tag{3.1}
\]

roots with \(|U\cap P|=t\). Put

\[
 k_t=m-t+\left\lfloor\frac{Ht}{M}\right\rfloor,\qquad
 u_t=Ht-M\left\lfloor\frac{Ht}{M}\right\rfloor.
\tag{3.2}
\]

The full-frame middle supply in \(P\)-profile \(k\) is exactly

\[
 S^{(0)}_k
 =\sum_{t=H}^m n_t
 \left((M-u_t)\mathbf1_{k=k_t}
             +u_t\mathbf1_{k=k_t+1}\right).
\tag{3.3}
\]

For direct interval length \(r\), put

\[
 a_{r,t}=\left\lfloor\frac{rt}{M}\right\rfloor,\qquad
 u_{r,t}=rt-Ma_{r,t}.
\tag{3.4}
\]

Then its exact profile supply is

\[
 S^{(r)}_k
 =\sum_{t=H}^m n_t
 \left((M-u_{r,t})\mathbf1_{k=a_{r,t}}
             +u_{r,t}\mathbf1_{k=a_{r,t}+1}\right).
\tag{3.5}
\]

The target profile sizes are

\[
 B^{(0)}_k=\binom mk^2
\tag{3.6}
\]

at the middle and

\[
 B^{(r)}_k=\binom mk\binom m{r-k}
\tag{3.7}
\]

at rank \(r\).

### Theorem 3.1 (simultaneous profile correctness)

Under (0.2),

\[
 \boxed{\sum_k|S^{(0)}_k-B^{(0)}_k|=o(W).}
\tag{3.8}
\]

If \(r=m-q\) and \(q=o(\sqrt m)\), then

\[
 \boxed{\sum_k|S^{(r)}_k-B^{(r)}_k|=o(W).}
\tag{3.9}
\]

Both conclusions remain true after deleting one arbitrary phase from
every root frame.

#### Proof

Choose a uniform root, equivalently a uniform \(M\)-set \(U\), and set
\(T=|U\cap P|\). This is hypergeometric, with

\[
 \mathbb ET=\frac M2,\qquad
 \operatorname{Var}T=\frac{M(m-H)}{4(2m-1)}.
\tag{3.10}
\]

After a uniform phase is chosen, (2.3) says that the middle profile is
the linear lattice interpolation of

\[
 \kappa_0(t)=m-t+\frac{Ht}{M}
             =m-\frac mM t.
\tag{3.11}
\]

It has mean \(m/2\), and its variance differs by \(O(1)\) from

\[
 \widetilde\sigma_0^2
 =\left(\frac mM\right)^2\operatorname{Var}T
 =\frac{m^2(m-H)}{4M(2m-1)}.
\tag{3.12}
\]

A uniform middle target has mean \(m/2\) and variance

\[
                         \sigma_0^2=\frac{m^2}{4(2m-1)}.
\tag{3.13}
\]

Therefore

\[
 \frac{\widetilde\sigma_0^2}{\sigma_0^2}
 =\frac{m-H}{m+H}=1-o(1).
\tag{3.14}
\]

Here is a direct total-variation justification. Uniformly on

\[
 |t-M/2|\le L_m\sqrt m,\qquad
 L_m\to\infty,\qquad
 L_m^4(H/m+m^{-1/2})\to0,
\tag{3.15}
\]

Stirling's formula applied to (3.1), (3.6), and their normalizing sums
gives their centered quadratic logarithms, with variances (3.10) and
(3.13), plus \(o(1)\). The affine interpolation (3.11) contributes the
Jacobian \(M/m=1+o(1)\). By (3.14), the two local masses have ratio
\(1+o(1)\) uniformly on (3.15). The mass outside (3.15) is \(o(1)\):
first use the same quadratic estimate outside a fixed central window,
then let that window grow. Hence the normalized laws in (3.3) and
(3.6) have total-variation distance \(o(1)\).

Their total masses are \(MN_H=\theta W\) and \(W\). Since
\(\theta=1+o(1)\), this proves (3.8).

For length \(r\), the interpolated map is

\[
                         \kappa_r(t)=\frac rM t.
\tag{3.16}
\]

Its variance differs by \(O(1)\) from

\[
 \widetilde\sigma_r^2
 =\frac{r^2(m-H)}{4M(2m-1)}.
\tag{3.17}
\]

A uniform rank-\(r\) target has variance

\[
                         \sigma_r^2=\frac{r(2m-r)}{4(2m-1)}.
\tag{3.18}
\]

For \(r=m-q\),

\[
 \frac{\widetilde\sigma_r^2}{\sigma_r^2}
 =\frac{(m-q)(m-H)}{(m+H)(m+q)}=1-o(1).
\tag{3.19}
\]

The same Stirling argument gives total-variation distance \(o(1)\)
between (3.5), normalized by \(MN_H\), and (3.7), normalized by
\(N_q=\binom{2m}{m-q}\). Moreover

\[
 \frac{MN_H}{N_q}
 =\theta\frac W{N_q}=1+o(1)
\tag{3.20}
\]

when \(q=o(\sqrt m)\). This proves (3.9).

Deleting one phase changes one coordinate of each supply vector for
every root. It changes each \(\ell^1\) comparison by at most
\(N_H=o(W)\). \(\square\)

### Corollary 3.2 (profile duals vanish)

Every bounded dual weight which is constant on the \(P\)-intersection
bins of the middle and a sub-Gaussian entrance layer evaluates the
mechanical supply--target discrepancy as \(o(W)\).

Thus the fixed-half Gaussian profile is not a statewise obstruction to
this atlas.

## 4. Exact cell biregularity

Root the cyclic positions, for example by the deleted phase. Fix a root
of type \(t\), a middle target \(D\supset A\), and put

\[
                         j=|(D\setminus A)\cap P|.
\tag{4.1}
\]

The target can occur in the mechanical catalogue if and only if

\[
 j\in
 \left\{
 \left\lfloor\frac{Ht}{M}\right\rfloor,\,
 \left\lceil\frac{Ht}{M}\right\rceil
 \right\}.
\tag{4.2}
\]

If \(c_{t,j}\) is the number of phase starts whose \(H\)-window has
exactly \(j\) one-positions, then the number of rooted label placements
realizing this occurrence is exactly

\[
 c_{t,j}\,j!(t-j)!(H-j)!(m-t+j)!.
\tag{4.3}
\]

Indeed, after choosing the start, assign independently the four label
classes inside and outside the window to their prescribed one- and
zero-positions. A prescribed proper window occurs at only one start in
a labelled cyclic order, so there is no overcount. By (2.3),

\[
\begin{aligned}
 c_{t,\lfloor Ht/M\rfloor}&=M-u_t,\\
 c_{t,\lceil Ht/M\rceil}&=u_t,
\end{aligned}
\tag{4.4}
\]

with the two values merged when \(u_t=0\).

The stabilizer \(S_P\times S_{P^c}\) is transitive on roots of a fixed
type and on targets of a fixed profile. Hence every ordered
source--target cell in (4.2) is biregular. The same assertion, with
\(H,j\) replaced by \(r,k\), holds for direct entrance intervals.

## 5. Integral Hall after phase cloning

The previous biregularity is strong enough to settle the raw one-row
Hall problem exactly.

For the middle row, make one left clone \((A,i)\) for every root and
phase. If the length-\(H\) binary interval at phase \(i\) has \(j\)
ones, join \((A,i)\) to every target

\[
                         D=A\cup J
\tag{5.1}
\]

where \(J\in\binom UH\) and \(|J\cap P|=j\). This edge means that some
label placement of the mechanical pattern makes phase \(i\) own \(D\).
No common placement is yet required for different phases.

Let \(\Gamma_0\) be this bipartite graph. Define \(\Gamma_r\) similarly:
clone \((A,i)\) is joined to every rank-\(r\) set \(S\subset U\) whose
\(P\)-count equals the binary weight of the length-\(r\) interval at
phase \(i\).

### Theorem 5.1 (exact clone Hall)

The graph \(\Gamma_0\) has a matching of size

\[
                         \sum_k\min(S^{(0)}_k,B^{(0)}_k)
                         =W-o(W).
\tag{5.2}
\]

For \(r=m-q\), \(q=o(\sqrt m)\), the graph \(\Gamma_r\) has a matching
of size

\[
                         \sum_k\min(S^{(r)}_k,B^{(r)}_k)
                         =N_q-o(W).
\tag{5.3}
\]

After deleting one prescribed phase at every root, the same conclusions
hold with \(o(W)\) changed only by an additional \(N_H=o(W)\).

#### Proof

Fix a target profile \(k\). Further fix a source type \(t\) and phase
\(i\) which maps to \(k\). On the left, take the clone \((A,i)\) for
every type-\(t\) root \(A\). On the right, take all targets of profile
\(k\). The action of \(S_P\times S_{P^c}\) is transitive on each shore
and preserves adjacency. This cell graph is therefore biregular.

Give every edge of a cell equal weight so that every left vertex has
weighted degree one. By biregularity, every right vertex then has the
same weighted degree. Summing all cells which map to profile \(k\), the
total left mass is \(S^{(0)}_k\), so every right vertex has weighted
degree

\[
                         \frac{S^{(0)}_k}{B^{(0)}_k}.
\tag{5.4}
\]

If \(S^{(0)}_k\le B^{(0)}_k\), this is a fractional matching saturating
all left clones in the profile. If \(S^{(0)}_k\ge B^{(0)}_k\), multiply
all its weights by \(B^{(0)}_k/S^{(0)}_k\); this is a fractional
matching saturating all right targets.

The bipartite matching polytope is integral. Hence there is an integral
matching of size \(\min(S^{(0)}_k,B^{(0)}_k)\). Different target
profiles have disjoint vertex sets, so these matchings may be united.
Finally,

\[
\begin{aligned}
 \sum_k\min(S^{(0)}_k,B^{(0)}_k)
 &=\frac12\left(
 MN_H+W-\sum_k|S^{(0)}_k-B^{(0)}_k|
 \right)\\
 &=W-o(W)
\end{aligned}
\tag{5.5}
\]

by (0.2) and Theorem 3.1.

The entrance proof is identical, using (3.5), (3.7), and (3.9). Since
the two total masses are \(MN_H=(1+o(1))W\) and
\(N_q=(1-o(1))W\), equation (5.3) follows. Removing one clone at every
root changes the relevant source total, and hence the displayed matching
lower bound, by at most \(N_H\). \(\square\)

### Corollary 5.2 (the exact grouping obstruction)

There are integral near-perfect assignments of individual middle phase
clones, and separately of individual entrance phase clones, entirely
inside the mechanical support atlas. Extend each matching arbitrarily on
its unmatched left clones. This assigns every retained clone and creates
at most \(o(W)\) additional repeat occurrences, because the number of
unmatched clones is \(o(W)\).

Such full phase assignments give a legal repaired frame selection if and
only if, for every root \(A\), there is one bijection

\[
                         \varphi_A:\mathbb Z_M\longrightarrow U
\tag{5.6}
\]

respecting the mechanical \(P/P^c\) positions such that every assigned
middle set and every assigned entrance set is the image under
\(\varphi_A\) of its prescribed cyclic interval.

This is the authoritative residual condition. Separate phase matchings
do not imply it: a middle deck of \(M-1\) windows reconstructs the cyclic
order and the missing phase up to dihedral symmetry, so almost all
phasewise freedom disappears when the clones are grouped.

The common-permutation condition has the following exact label form.

### Lemma 5.3 (lag-\(H\) rotor completion criterion)

Let \((J_i)_{i\in\mathbb Z_M}\) be \(H\)-subsets of one \(M\)-set \(U\).
Assume

\[
                         |J_i\cap J_{i+1}|=H-1
 \qquad(i\in\mathbb Z_M),
\tag{5.7}
\]

and write

\[
 x_i\ \text{for the unique element of }J_i\setminus J_{i+1}.
\tag{5.8}
\]

There is a labelled cyclic order

\[
                         (x_0,x_1,\ldots,x_{M-1})
\tag{5.9}
\]

whose length-\(H\) window at phase \(i\) is \(J_i\) if and only if

1. the labels \(x_0,\ldots,x_{M-1}\) are all distinct; and
2. the lag-\(H\) insertion identities
   \[
      J_{i+1}\setminus J_i=\{x_{i+H}\}
      \qquad(i\in\mathbb Z_M)
   \tag{5.10}
   \]
   hold.

Equivalently, the clone assignments must obey

\[
 J_{i+1}\setminus J_i
 =J_{i+H}\setminus J_{i+H+1}
 \qquad(i\in\mathbb Z_M),
\tag{5.11}
\]

and the singleton labels on the right of (5.11) must exhaust \(U\).

#### Proof

For a genuine cyclic order, shifting the \(H\)-window from phase \(i\)
to \(i+1\) deletes \(x_i\) and inserts \(x_{i+H}\). Thus (5.7)--(5.10)
are necessary.

Conversely, assume the two conditions. At transition \(i\), relation
(5.10) deletes \(x_i\) and inserts \(x_{i+H}\). Since the \(x_i\)'s are
all distinct, a label \(x_j\) is inserted exactly at transition \(j-H\)
and deleted exactly at transition \(j\). It is therefore present in
exactly the \(H\) successive states

\[
                         J_{j-H+1},\ldots,J_j.
\tag{5.12}
\]

Consequently

\[
                         J_i=\{x_i,x_{i+1},\ldots,x_{i+H-1}\}
\tag{5.13}
\]

for every \(i\), with indices modulo \(M\). This is precisely the window
deck of (5.9). \(\square\)

The mechanical binary pattern enforces only the \(P/P^c\)-counts of the
two sides of (5.10). The clone Hall theorem does not enforce equality of
the actual inserted label with the label deleted \(H\) phases later.
Thus (5.11) is a literal statewise obstruction to gluing arbitrary
phase matchings.

This failure occurs inside the mechanical support, not only in an
abstract clone graph. Take a root type with

\[
                         t\ge2H,\qquad M-t\ge2H,
\tag{5.14}
\]

and start from any genuinely labelled mechanical order
\((c_0,\ldots,c_{M-1})\). At one transition \(i\), replace the actual
inserted label \(c_{i+H}\) by a different label \(z\notin J_i\) from the
same one of \(P,P^c\), leaving all other phase assignments unchanged.
The modified phase \(J_{i+1}'=(J_i\setminus\{c_i\})\cup\{z\}\) has
exactly the prescribed mechanical profile and is individually adjacent
to its clone in \(\Gamma_0\). Nevertheless (5.10) at phase \(i\) would
require \(z=c_{i+H}\). Hence this phasewise legal state has no common
cyclic labeling. Condition (5.14) holds for all but exponentially few
root types.

For a repaired deck, one window is absent. The one-hole reconstruction
theorem supplies its unique cyclic completion up to reversal; Lemma 5.3
then applies to that completion. Once the middle order is completed, its
entrance row is no longer free:

\[
                         S_i=\{x_i,x_{i+1},\ldots,x_{i+r-1}\}
\tag{5.15}
\]

up to the fixed promotion-ring phase convention. Hence the surviving
global problem is to choose the middle clone matching so that (5.11)
holds at every root while the forced sets (5.14) have only \(o(W)\)
holes.

## 6. Alignment with the block-factor floor

Theorem 5.1 is not a forbidden local-block proposal.

1. The mechanical pattern only defines a globally symmetric support
   atlas. It does not select frames independently at different roots.

2. Clone Hall is an ungrouped transportation theorem. It deliberately
   stops before choosing one common labeling per root.

3. Any probability law used to round the clone assignments into frames
   must still obey the block-factor theorem. With
   \[
      p=\frac{M}{\binom MH},\qquad
      \frac1p=(1+o(1))\binom mH,
   \tag{6.1}
   \]
   a law supported on \(o(W)\)-hole selections cannot factor into
   independent correlation blocks of size \(o(1/p)\). In targetwise
   form, almost every middle target must see almost its whole root star
   inside one correlated component.

Thus the correct next object is not independent rounding of the
mechanical cells. It is a globally correlated permutation coupling of
the clone matchings, or an equivalent resolution colouring of the
restricted repaired catalogue.

The earlier restriction-confluent and small master-order library
obstructions remain in force, but they are not reproved here. The
mechanical atlas is intentionally nonconfluent and allows root-sensitive
label orders, so it does not fall into those already closed classes.

## 7. Exact boundary

Proved here:

1. the repaired catalogue's exact resolution-colouring normal form and
   degrees;
2. an explicit mechanical cyclic pattern balancing all interval lengths
   simultaneously;
3. exact profile census formulas (3.3) and (3.5);
4. \(o(W)\) middle and sub-Gaussian entrance discrepancy in every
   balanced-half profile, including one deletion per root;
5. exact biregularity in every surviving source--target profile cell;
6. the necessary-and-sufficient lag-\(H\) rotor completion equations;
   and
7. integral \(W-o(W)\) middle and \(N_q-o(W)\) entrance clone matchings
   inside the restricted atlas.

Not proved here:

1. a common permutation coupling of the two clone matchings;
2. a proper \(Q\)-colouring of the repaired catalogue;
3. one raw frame per root with \(o(W)\) combined middle/entrance defect;
   or
4. coefficient one.

The new information is sharp enough to move the gate. Potential
reachability, profile capacity, and literal one-row Hall all hold in one
explicit all-length support atlas. The unresolved issue is now exactly
whether those integral clone assignments can be coupled, across
\(\binom mH\)-scale root stars, into one cyclic labeling per root without
creating linear middle or entrance loss.

## 8. Dependency ledger

The correlation-scale audit used in Section 6 is
MATH_THEOREM_PROMOTION_RING_BLOCK_FACTOR_HOLE_FLOOR_20260726.md.
The one-hole rigidity invoked after Lemma 5.3 is proved in
MATH_AUDIT_CALIBRATED_FULL_TOP_PROMOTION_RING_SWITCHES_TAIL_AND_LOCALITY_20260726.md.
The already closed restriction-confluent and master-order routes are
recorded in
MATH_AUDIT_GLOBAL_RECURSIVE_SCD_TO_PROMOTION_RING_FACTORIZATION_20260726.md
and are not reproved here.

## 9. Root-intrinsic affine-syndrome continuation

The preceding clone Hall theorem suggests assigning a code to each root
and using that code to choose its two label permutations.  The first
genuinely root-star-coupled algebraic attempt is additive, not an ambient
master-order restriction.

Let \(G\) be a finite abelian group and fix coordinate weights

\[
                         w_x\in G\qquad(x\in V).
\tag{9.1}
\]

For every \(B\subseteq V\), put

\[
                         \sigma(B)=\sum_{x\in B}w_x.
\tag{9.2}
\]

Let \(L\in\operatorname {End}(G)\) and \(\beta\in G\).  The affine root
hash is

\[
                         h(A)=\beta+L\sigma(A).
\tag{9.3}
\]

The attractive identity is exact.  If \(D=A\sqcup J\), then

\[
 h(A)=\sigma(J)
 \quad\Longleftrightarrow\quad
 (I+L)\sigma(A)=\sigma(D)-\beta.
\tag{9.4}
\]

Thus, on the whole root star

\[
                         \mathcal R(D)=\binom D{m-H},
\tag{9.5}
\]

the target condition is one affine equation in the root syndrome.  If
the values \(\sigma(A)\), \(A\in\mathcal R(D)\), were nearly rainbow,
an affine line hash could in principle produce one hit rather than the
Poisson hole law of independent roots.  This is the correct reason to
test additive codes.

Call the decoder **syndrome-complete** when, for every root \(A\) and
every \(J\in\binom{U_A}H\),

\[
 J\text{ is a retained window of }\pi_A
 \quad\Longleftrightarrow\quad
 \sigma(J)=h(A).
\tag{9.4a}
\]

Thus the hash equality, rather than an additional unencoded chronology,
is the complete clone-owner assignment.  Since a repaired frame has
\(M-1\) windows, (9.4a) asks its syndrome fibre to have exactly that
size and to be one repaired cyclic deck.  The following theorem is the
exact local obstruction.  It also applies to the weaker one-way
requirement that every retained window lie in the hash fibre.

### Theorem 9.1 (repaired additive-syndrome holonomy)

Let

\[
 \pi=(x_0,x_1,\ldots,x_{M-1})
\tag{9.6}
\]

be a cyclic labeling of one top \(U\), and put

\[
 J_i=\{x_i,x_{i+1},\ldots,x_{i+H-1}\}.
\tag{9.7}
\]

Fix a deleted phase \(s\).  If

\[
                         \sigma(J_i)=z
            \qquad(i\ne s)
\tag{9.8}
\]

for some \(z\in G\), then the set of weights

\[
                         \{w_x:x\in U\}
\tag{9.9}
\]

has size at most

\[
                         g+2,
 \qquad g=\gcd(M,H)=\gcd(m,H).
\tag{9.10}
\]

For a full, undeleted ring the sharper bound is \(g\).

#### Proof

For every transition whose two endpoint phases are retained,

\[
\begin{aligned}
 0
 &=\sigma(J_{i+1})-\sigma(J_i)\\
 &=w_{x_{i+H}}-w_{x_i}.
\end{aligned}
\tag{9.11}
\]

Thus

\[
                         w_{x_{i+H}}=w_{x_i}
       \qquad(i\notin\{s-1,s\}).
\tag{9.12}
\]

The permutation \(i\mapsto i+H\) on \(\mathbb Z_M\) consists of exactly
\(g\) cycles.  Delete from those cycles the at most two edges indexed by
\(s-1,s\).  The resulting graph has at most \(g+2\) connected
components.  Equation (9.12) makes the weight constant on every
component, proving (9.10).  Without a deletion, no edge is removed and
there are exactly \(g\) components. \(\square\)

This is not a fixed-master-cycle statement.  The cyclic labeling in
Theorem 9.1 may be chosen separately and intrinsically at every root,
and its two shore permutations are arbitrary.

### Corollary 9.2 (global weight and code collapse)

Suppose that every root has a repaired frame satisfying (9.8), with the
same global coordinate weights (9.1), though with arbitrary root-dependent
label permutations, deleted phases, and syndrome values.  Then

\[
                         |\{w_x:x\in V\}|\le g+2.
\tag{9.13}
\]

Consequently the number of possible root syndromes is at most

\[
 \boxed{
 K_g=\binom{m-H+g+1}{g+1}.}
\tag{9.14}
\]

#### Proof

If \(g+3\) distinct coordinate weights existed, choose one coordinate of
each weight and extend those coordinates to an \(M\)-set \(U\).  This is
the top of the root \(A=V\setminus U\), contradicting Theorem 9.1.
Thus (9.13) holds.

Write a root by the numbers of its elements in the at most \(g+2\)
weight classes.  These nonnegative numbers sum to \(m-H\), so there are
at most the number of weak compositions in (9.14).  The group sum can
identify several compositions, but cannot create more values. \(\square\)

### Theorem 9.3 (entropy--holonomy dichotomy for the rainbow affine-star plan)

Let

\[
                         R=|\mathcal R(D)|=\binom mH.
\tag{9.15}
\]

Consider the **rainbow affine-star plan**, which requires the root
syndrome to be nearly rainbow on almost every middle root star:

\[
 |\sigma(\mathcal R(D))|=(1-o(1))R
                         \qquad\text{for almost every }D.
\tag{9.16}
\]

If every root also has a repaired constant-syndrome frame (9.8), then

\[
                         K_g\ge(1-o(1))R.
\tag{9.17}
\]

In particular, if \(g\) is a proper divisor of \(H\), then (9.17) is
false by an exponential factor:

\[
 \boxed{
 \frac{K_g}{R}
 \le
 \exp\left[-\left(\frac12+o(1)\right)
             H\log\frac mH\right]=o(1).}
\tag{9.18}
\]

Hence the rainbow affine-syndrome construction is impossible unless

\[
                         g=H,
 \quad\text{equivalently}\quad H\mid m.
\tag{9.19}
\]

#### Proof

Equations (9.14) and (9.16) immediately imply (9.17).  If \(g\) is a
proper divisor of \(H\), then \(g\le H/2\).  The standard product bounds
for binomial coefficients give

\[
\begin{aligned}
 \log K_g
 &\le (g+1)\log\frac{e(m-H+g+1)}{g+1}\\
 &\le\left(\frac12+o(1)\right)
                 H\log\frac mH,
\end{aligned}
\tag{9.20}
\]

whereas

\[
 \log R
 =H\log\frac mH+O(H).
\tag{9.21}
\]

Since \(m/H\to\infty\), subtraction proves (9.18).  Finally
\(g=\gcd(m,H)\) divides \(H\), so the only alternative to a proper
divisor is \(g=H\). \(\square\)

The hypothesis (9.16) is the defining entropy certificate of this
rainbow plan.  In (9.4), all roots with the same syndrome are
indistinguishable to the affine equation, and (9.4a) leaves no second
chronological filter: a selected root-star fibre of size \(r\) enters
as an \(r\)-fold collision.  Requiring all fibres to be almost
singletons is a clean sufficient way to eliminate that collision
mechanism, and Theorem 9.3 rules it out except at the arithmetic
alignment \(H\mid m\).

A logically weaker syndrome-complete design could try to arrange that
only one designated syndrome fibre is singleton for each target while
all other fibres are ignored.  Theorem 9.3 does not exclude that
selective-fibre possibility; it excludes the uniform rainbow
linearization that would have coupled the existing clone Hall theorem
without another target-dependent chronology.

The syndrome-complete condition itself is nevertheless impossible, by
combining holonomy with the one-hole reconstruction rigidity.

### Theorem 9.4 (equal-weight symmetry obstruction)

For all sufficiently large \(m\), there is no choice of a finite
abelian group \(G\), global coordinate weights \(w_x\), affine root hash
(9.3), and one repaired cyclic frame at every root satisfying the
syndrome-complete equivalence (9.4a).

This remains impossible when \(H\mid m\).

#### Proof

Suppose such a family exists.  Corollary 9.2 shows that the \(2m\)
coordinates occupy at most

\[
                         g+2\le H+2=o(m)
\tag{9.22}
\]

weight classes.  Therefore one global weight class contains at least

\[
                         \frac{2m}{g+2}>4
\tag{9.23}
\]

coordinates.  Choose four of them and extend them to an arbitrary
\(M\)-set \(U\).  Let \(A=V\setminus U\), and let
\(\mathcal W_A^-\) be its repaired deck.

Every permutation of the four equal-weight coordinates preserves
\(\sigma(J)\) for every \(J\in\binom UH\).  By syndrome completeness,

\[
 \mathcal W_A^-=
 \{J\in\tbinom UH:\sigma(J)=h(A)\}.
\tag{9.24}
\]

Hence all \(24\) permutations of those four coordinates preserve the
repaired deck.  Thus

\[
                         S_4\le\operatorname {Aut}(\mathcal W_A^-).
\tag{9.25}
\]

On the other hand, the one-hole reconstruction theorem says that
\(\mathcal W_A^-\) determines its missing window and its cyclic order
up to reversal.  Every deck automorphism must therefore be an
automorphism of that cycle, so

\[
                         \operatorname {Aut}(\mathcal W_A^-)
                         \le D_{2M}.
\tag{9.26}
\]

Every subgroup of a dihedral group has a cyclic subgroup of index at
most two.  The group \(S_4\) has no such subgroup: its cyclic subgroups
have order at most four and hence index at least six.  This contradicts
(9.25)--(9.26). \(\square\)

Theorem 9.4 is stronger than the rainbow entropy obstruction.  It rules
out the complete additive decoder even if one tries to exploit only a
single exceptional syndrome fibre on each target star.  A weaker
one-way use of (9.8), followed by another target-dependent chronological
filter, is not syndrome-complete and is not covered; that extra filter
is precisely the original permutation-coupling problem in new notation.

## 10. Exact owner ledger for the failed affine construction

For completeness, the physical middle load of any attempted
constant-syndrome realization is

\[
 \ell(D)=
 \sum_{A\in\binom D{m-H}}
 \mathbf1\{D\setminus A\text{ is a retained window of }\pi_A\}
 \mathbf1\{(I+L)\sigma(A)=\sigma(D)-\beta\}.
\tag{10.1}
\]

Under (9.8), the second indicator is forced by the first.  Under the
syndrome-complete condition (9.4a), the converse also holds, so (10.1)
is exactly the affine clone-owner rule rather than only a necessary
condition.  The total mass remains

\[
                         \sum_D\ell(D)=(M-1)N_H.
\tag{10.2}
\]

Thus the scalar middle load is exactly correct at the packing-side
calibration.  Nevertheless Theorem 9.4 forbids the syndrome equality
from being the complete physical owner rule.  The failure therefore
occurs before a useful entrance audit.  Keeping only the forward
implication in (9.8) leaves an unencoded window-membership decision,
which is the original common-order gate rather than a hash solution.

The same conclusion applies to the two label permutations of the
mechanical pattern.  Those permutations only choose the word
\((x_i)\) in (9.6); equation (9.11) holds after every such choice.  In
particular the balanced binary profile theorem and clone Hall theorem do
not weaken the holonomy.

## 11. Phase offsets and the exact surviving escape

The only immediate additive escape is to make the syndrome class depend
on phase.  Let \(\rho_i\in G\) and replace (9.8) by

\[
                         \sigma(J_i)=z+\rho_i.
\tag{11.1}
\]

Then the derivative is no longer zero but is exactly

\[
 \boxed{
 w_{x_{i+H}}-w_{x_i}=\rho_{i+1}-\rho_i.}
\tag{11.2}
\]

Following an orbit of the shift \(i\mapsto i+H\) gives the necessary
cycle condition

\[
 \boxed{
 \sum_{r=0}^{M/g-1}
   (\rho_{i+rH+1}-\rho_{i+rH})=0
 \qquad(i\in\mathbb Z_M).}
\tag{11.3}
\]

Conversely, (11.2), together with one initial window syndrome, implies
(11.1) at every phase.  Thus (11.2)--(11.3) are the exact inhomogeneous
lag-\(H\) rotor equations for an additive phase-offset construction.

They do not yet couple the clone Hall matching.  If the offsets are
chosen after the labeling, taking

\[
                         \rho_i=\sigma(J_i)-z
\tag{11.4}
\]

makes the equations tautological and merely re-encodes the original
permutation.

There is an even sharper all-depth audit.  For a length \(k\), write

\[
                         J_i^{(k)}=
 \{x_i,x_{i+1},\ldots,x_{i+k-1}\}.
\tag{11.5}
\]

Suppose consecutive lengths are encoded by

\[
 \sigma(J_i^{(k)})=z_k+\rho_{i,k},
 \qquad
 \sigma(J_i^{(k+1)})=z_{k+1}+\rho_{i,k+1}.
\tag{11.6}
\]

Then subtraction recovers the entering label weight exactly:

\[
 \boxed{
 w_{x_{i+k}}=(z_{k+1}-z_k)
             +(\rho_{i,k+1}-\rho_{i,k}).}
\tag{11.7}
\]

Consequently, if the coordinate weights are injective, the offset tables
at any two consecutive controlled lengths recover the whole labelled
cyclic order.  After the fixed harmless phase shifts in the promotion
convention, the lower and upper flags use the nested lengths
\(H-q,\ldots,H+q\).  Hence an all-depth phase-offset hash carries the
same information as the two original label permutations.  It is a valid
normal form, but not a compression or a rounding theorem.

## 12. Why “bounded degree” alone cannot be an obstruction

There is a formal issue with an unrestricted bounded-degree hash no-go.
Define the root incidence code

\[
                         \chi(A)=(\mathbf1_{x\in A})_{x\in V}.
\tag{12.1}
\]

Every coordinate of \(\chi\) is a polynomial of degree one in the root
indicators, and \(\chi\) is injective.  Therefore every possible
root-dependent pair of label permutations factors as

\[
 A\overset{\chi}{\longmapsto}\chi(A)
   \overset{\mathcal D}{\longmapsto}
   (\pi_A^P,\pi_A^{P^c})
\tag{12.2}
\]

for a suitable decoder \(\mathcal D\).  In particular, polynomial degree
without a bound on output dimension or decoder complexity places no
restriction at all on the frame assignment.

Thus a theorem excluding “all bounded-degree root hashes” would be
false as a complexity statement: degree-one codes already parameterize
the complete mechanical catalogue.  A meaningful algebraic no-go must
specify the decoder law.  Theorems 9.1--9.4 do so for the most direct
affine-syndrome decoder, and (11.2)--(11.7) characterize its only evident
phase-dependent escape.

## 13. Continuation boundary

Newly proved in Sections 9--12:

1. the exact affine identity (9.4) which makes additive root syndromes a
   genuine whole-star, non-Poisson candidate;
2. the repaired lag-\(H\) holonomy bound \(g+2\), valid for arbitrary
   root-intrinsic mechanical labelings;
3. the resulting global syndrome-alphabet bound (9.14);
4. an exponential entropy contradiction for every proper
   \(g=\gcd(m,H)<H\);
5. the equal-weight \(S_4\)-versus-dihedral obstruction, which rules out
   every syndrome-complete additive decoder, including \(H\mid m\);
6. the exact physical owner ledger and its correct total mass;
7. the inhomogeneous phase-offset rotor equations and orbit sums;
8. recovery of the full cyclic labeling from two consecutive nested
   offset layers; and
9. the universality of unrestricted degree-one root codes.

Still open:

1. a nonadditive, high-dimensional decoder whose output offsets are
   fixed before the cyclic labeling yet satisfy (11.2)--(11.3);
2. coupling such offsets to the clone Hall assignment with \(o(W)\)
   middle and two-sided entrance defects; and
3. coefficient one.

The constructive gate is now narrower.  A viable intrinsic code must
avoid constant syndrome fibres, and its phase offsets must solve a
global root-star assignment while already carrying essentially a full
permutation at consecutive nested depths.
