# Exact overlap hierarchy for H's deterministic rainbow catalogue

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Outcome

This note audits the overlap geometry of the deterministic gap-permutation
catalogue in
`MATH_ATTACK_H_DETERMINISTIC_CARRIER_ROTOR_TRAJECTORIES_20260725.md`.
It proves four facts.

1. There is an exact membership-atom formula for every multiple codegree.
   The common priority order factors completely from the coordinate
   labelling.
2. Same-phase vertical ladders have an exact factorial codegree formula.
3. If the gap permutation has displacement at most a fixed (D) from the
   ordinary cyclic schedule (in particular, for H's adjacent-switch cube,
   (D=1)), then the complete pair-overlap mass is (O_D(\sqrt m)), and
   the nested (k)-overlap mass is
   
   \[
      O_D(m^{5/2-k}).
   \]
   
   The corresponding exponentially weighted nested hierarchy is summable.
   Thus the adjacent vertical codegree (1/m) is not by itself a
   higher-overlap obstruction.
4. This raw hierarchy is not hereditary under target deletion. At depth
   one every decorated path leaves at most two phases unclaimed. Hence
   three forbidden depth-one phases annihilate every priority decoration
   of a fixed base path. No priority phase code can remove this obstruction
   while retaining the calibrated depth-one quota.

The conclusion is precise. Bounded-displacement pruning closes the **raw
nested-overlap** gate. The remaining common-matching theorem must control
the residual distribution of whole base paths; it cannot be deduced from
raw overlap moments plus reprioritization.

## 1. Catalogue notation

Put

\[
 n=2m,\qquad M=m+H,\qquad
 N=\binom{2m}{M},\qquad W=\binom{2m}{m}.
\tag{1.1}
\]

For a signed depth (d\in[-Q,Q]), write

\[
 r_d=m+d,\qquad c(d)=c_{|d|},
\tag{1.2}
\]

where

\[
 c_0=M,\qquad
 c_q=\min\left\{M,\left\lfloor
 {\binom{2m}{m-q}\over N}\right\rfloor\right\}.
\tag{1.3}
\]

Fix a nonempty family \(\mathfrak R\) of admissible gap permutations.
Above every carrier (U\in\binom{[2m]}M), the catalogue contains:

* every \(\rho\in\mathfrak R\);
* every bijective phase labelling \(\phi:\mathbb Z_M\to U\); and
* every priority permutation \(\pi\in S_M\).

The rank-(r_d) flag at phase (t) is denoted (F_d^\rho(t)). It is
claimed exactly when

\[
 \pi(t)\le c(d).
\tag{1.4}
\]

Every row is internally injective. Let (A) be the number of decorated
catalogue paths over one carrier. The tag degree is (A), and the degree
of a fixed rank-(r_d) target is

\[
 D_d=A,{c(d)N\over\binom{2m}{r_d}}\le A.
\tag{1.5}
\]

## 2. Exact master formula for every multiple codegree

Take fixed targets

\[
 \mathbf S=(S_1,\ldots,S_k),\qquad |S_i|=r_{d_i}.
\]

Fix a schedule \(\rho\) and a phase assignment

\[
 \mathbf t=(t_1,\ldots,t_k)\in\mathbb Z_M^k.
\]

Let (A_i\subseteq\mathbb Z_M) be the phase-label template of
\(F_{d_i}^\rho(t_i)\). For each nonempty
\(J\subseteq[k]\), define the domain and target membership atoms

\[
 a_J=\#\{x\in\mathbb Z_M:\{i:x\in A_i\}=J\},
\tag{2.1}
\]

\[
 s_J=\#\{x\in[2m]:\{i:x\in S_i\}=J\}.
\tag{2.2}
\]

Put (u=|\bigcup_iA_i|). Choosing a uniform carrier and a uniform
labelling is the same as choosing a uniform injection

\[
 f:\mathbb Z_M\hookrightarrow[2m].
\]

### Theorem 2.1 (labelling factor)

For the fixed template assignment,

\[
 \Pr\bigl(f(A_i)=S_i\ (1\le i\le k)\bigr)=0
\]

unless (a_J=s_J) for every nonempty (J\). When all atoms agree, the
probability is exactly

\[
 \boxed{
 p_{\rm lab}(\mathbf A,\mathbf S)
 ={\displaystyle\left(\prod_{\varnothing\ne J\subseteq[k]}a_J!\right)
 (2m-u)_{M-u}
 \over (2m)_M}.}
\tag{2.3}
\]

#### Proof

Every nonempty membership atom must be mapped bijectively onto the
corresponding target atom, giving the factorial product in (2.3). The
remaining (M-u) phase labels may be injected arbitrarily into the
(2m-u) coordinates outside the target union. Divide by the total number
((2m)_M) of injections. \(\square\)

Now group the distinct phases among (t_1,\ldots,t_k) as
\(\tau_1,\ldots,\tau_\ell\). The threshold attached to \(\tau_j\) is

\[
 b_j=\min\{c(d_i):t_i=\tau_j\}.
\tag{2.4}
\]

Let (b_{(1)}\le\cdots\le b_{(\ell)}) be their increasing rearrangement.

### Theorem 2.2 (priority factor)

The exact probability that every requested flag is claimed equals

\[
 \boxed{
 p_{\rm pr}(b_1,\ldots,b_\ell)
 ={\prod_{j=1}^{\ell}(b_{(j)}-j+1)\over(M)_\ell},}
\tag{2.5}
\]

with the product interpreted as zero if a factor is nonpositive.

#### Proof

Assign distinct priority ranks in increasing order of the thresholds.
The first phase has (b_{(1)}) choices, the next has
(b_{(2)}-1), and so on. Divide by the ((M)_\ell) possible ordered
distinct ranks. \(\square\)

Combining the two independent decorations gives the exact master identity

\[
 \boxed{
 {\deg(\mathbf S)\over A}
 =N\,{1\over|\mathfrak R|}
 \sum_{\rho\in\mathfrak R}
 \sum_{\mathbf t\in\mathbb Z_M^k}
 p_{\rm pr}(\mathbf t)\,
 p_{\rm lab}(\mathbf A^{\rho,\mathbf t},\mathbf S).}
\tag{2.6}
\]

Internal row injectivity makes the realized phase assignments disjoint, so
there is no multiplicity correction in (2.6).

## 3. Exact same-phase ladder distribution

Let

\[
 -Q\le d_1<\cdots<d_k\le Q,
 \qquad r_i=m+d_i,
\]

and let

\[
 S_1\subset\cdots\subset S_k,
 \qquad |S_i|=r_i.
\tag{3.1}
\]

Put

\[
 q_*=\max_i|d_i|,\qquad c_*=c_{q_*}.
\]

The number of ambient chains with these ranks is

\[
 \mathscr C(\mathbf r)
 ={(2m)!\over
 r_1!\,(2m-r_k)!\,
 \prod_{i=1}^{k-1}(r_{i+1}-r_i)!}.
\tag{3.2}
\]

### Theorem 3.1 (same-phase chain codegree)

The degree of the specified chain occurring in one common phase is

\[
 \boxed{
 {D_{\rm col}(S_1,\ldots,S_k)\over A}
 ={Nc_*\over\mathscr C(\mathbf r)}.}
\tag{3.3}
\]

If (S_j) is used as the anchor, then

\[
 \boxed{
 {D_{\rm col}(S_1,\ldots,S_k)\over D_{d_j}}
 ={c_*\over c(d_j)}\,{1\over\mathscr N_j(\mathbf r)},}
\tag{3.4}
\]

where the exact number of such chains containing a fixed (S_j) is

\[
 \mathscr N_j(\mathbf r)=
 {r_j!\over r_1!\prod_{i<j}(r_{i+1}-r_i)!}
 { (2m-r_j)!\over
 (2m-r_k)!\prod_{i\ge j}(r_{i+1}-r_i)!}.
\tag{3.5}
\]

#### Proof

In every decorated path, precisely the first (c_*) priority phases claim
the entire displayed subchain. Thus the total number of
edge--same-phase-chain incidences is (NAc_*). Coordinate symmetry is
transitive on the \(\mathscr C(\mathbf r)\) chains, proving (3.3).
Divide by (1.5), and use
\(\mathscr C(\mathbf r)=\binom{2m}{r_j}\mathscr N_j(\mathbf r)\), to get
(3.4). \(\square\)

For example, a complete consecutive double flag from lower depth (a) to
upper depth (b), anchored at its owner, has relative degree

\[
 {c_{\max(a,b)}\over M}
 {1\over(m)_a(m)_b}.
\tag{3.6}
\]

Thus every extra consecutive member of a vertical ladder costs another
factor (m^{-1+o(1)}).

## 4. Bounded-displacement phase geometry

Assume now that every schedule is (D)-banded as in Corollary 3.1 of H's
deterministic catalogue note. Thus, after using the departure labelling as
the cyclic phase order,

\[
 d_J(F_d(t),I_{m+d}(t))\le D
\tag{4.1}
\]

for the ordinary cyclic interval (I_{m+d}(t)).

The adjacent-switch cube has (D=1), so all estimates below already hold
on an exponentially large, fully labelled subcatalogue.

### Lemma 4.1 (near-interval defect count)

Let (r\le r+h<M), and let (A_t,B_s) have sizes (r,r+h) with

\[
 d_J(A_t,I_r(t))\le D,\qquad
 d_J(B_s,I_{r+h}(s))\le D.
\]

For fixed (t), the number of phases (s) satisfying

\[
 |A_t\setminus B_s|=d
\]

is at most

\[
 \boxed{L_D(h,d):=\min\{M,h+2d+4D+1\}.}
\tag{4.2}
\]

#### Proof

Put

\[
 f(s)=|I_r(t)\setminus I_{r+h}(s)|.
\]

The two Johnson-distance bounds imply

\[
 |f(s)-d|\le2D.
\tag{4.3}
\]

For cyclic intervals, (f=0) at exactly (h+1) starts. Away from that
containment interval, each positive value of (f) occurs at at most two
starts, one at each boundary. Hence the number of starts with
\(f\le d+2D\) is at most

\[
 h+1+2(d+2D).
\]

This is (4.2). \(\square\)

The complement lengths in the calibrated band are (H+O(Q)\gg D), so
for fixed (D) the truncation by (M) is never relevant in the dominant
small-defect cases.

## 5. Exact pair distribution and its total mass

Let (r\le r+h), and take fixed targets (S,T) with

\[
 |S|=r,\qquad |T|=r+h,\qquad |S\setminus T|=d.
\tag{5.1}
\]

For a decorated path (E), let (J_{r,h,d}(E)) be the number of ordered
claimed phase pairs producing this rank and defect profile. Let
\(\overline J_{r,h,d}\) denote the catalogue average.

### Theorem 5.1 (exact pair codegree)

\[
 \boxed{
 {\deg(S,T)\over A}
 ={N\over\binom{2m}{r}}
 {\overline J_{r,h,d}\over
 \binom rd\binom{2m-r}{h+d}}.}
\tag{5.2}
\]

Equivalently, relative to the degree of (S),

\[
 \boxed{
 {\deg(S,T)\over\deg(S)}
 ={\overline J_{r,h,d}\over
 c(r)\binom rd\binom{2m-r}{h+d}},}
\tag{5.3}
\]

where (c(r)=c_{|r-m|}).

Moreover, on the (D)-banded subcatalogue,

\[
 \boxed{
 \overline J_{r,h,d}
 \le\min\{c(r),c(r+h)\}L_D(h,d).}
\tag{5.4}
\]

#### Proof

There are

\[
 \binom{2m}{r}\binom rd\binom{2m-r}{h+d}
\]

ordered ambient pairs with profile (5.1). The total number of incidences
over all decorated paths is (NA\overline J_{r,h,d}). Coordinate symmetry
proves (5.2), and division by (1.5) proves (5.3).

Fixing a claimed rank-(r) phase, Lemma 4.1 leaves at most
\(L_D(h,d)\) possible phases in the other row. Reverse the two roles and
take the smaller of the two claimed-phase counts to get (5.4). \(\square\)

For a path (P), define its ordinary pair-overlap mass

\[
 \Xi_2(P)=
 {1\over A}
 \sum_{E:\operatorname{tag}(E)\ne\operatorname{tag}(P)}
 \binom{|E\cap P|}{2}.
\tag{5.5}
\]

Equivalently, it is the sum of \(\deg\{v,w\}/A\) over pairs of protected
targets in (P), with same-tag competitors deleted.

### Theorem 5.2 (sharp total pair mass)

For fixed (D), uniformly over every path in the (D)-banded catalogue,

\[
 \boxed{\Xi_2(P)=O_D(\sqrt m).}
\tag{5.6}

For the full priority decoration there is also the matching lower bound

\[
 \boxed{\Xi_2(P)\ge(\sqrt\pi-o(1))\sqrt m}
\tag{5.7}

before deleting the negligible same-tag contribution. Thus the order
\(\sqrt m\) is exact.

#### Proof

A pair in one carrier has union size at most (M), so in (5.1)

\[
 d\le M-r-h=O(H+Q)=o(m).
\tag{5.8}
\]

Put (a=m-Q). Equations (5.2)--(5.4), (1.5), and another application of
Lemma 4.1 to the fixed path give

\[
 \Xi_2(P)
 \le\sum_r c(r)
 \sum_{\substack{h,d\ge0\\(h,d)\ne(0,0)}}
 {L_D(h,d)^2\over\binom ad\binom a{h+d}}.
\tag{5.9}
\]

The inner sum is (O_D(1/m)). Its leading term is (h=1,d=0); every
term with (h+d\ge2), or with (d\ge1), gains at least one further
factor (m^{-1+o(1)}). A ratio comparison using
\(H+Q=o(m)\) makes this uniform through the range (5.8). Finally,

\[
 \sum_{r=m-Q}^{m+Q}c(r)
 =M+2\sum_{q=1}^Qc_q
 =(\sqrt\pi+o(1))m^{3/2}.
\tag{5.10}
\]

This proves (5.6).

For (5.7), keep only same-phase adjacent pairs in the two vertical
ladders. At signed distance (q\ge1), there are (c_q) such pairs, and
Theorem 3.1 gives their degree as

\[
 {A(1-o(1))\over m+O(Q)}.
\]

Both sides together contribute

\[
 (2-o(1)){1\over m}\sum_{q=1}^Qc_q
 =(\sqrt\pi-o(1))\sqrt m.
\]

Same-tag competitors form a vanishing fraction of these global degrees.
\(\square\)

The important comparison is

\[
 \Xi_2(P)=\Theta(\sqrt m),\qquad
 |P|=(\sqrt\pi+o(1))m^{3/2}.
\tag{5.11}
\]

Thus pair-neighbourhood overlap is only an (O(1/m)) fraction of the
single-conflict mass. Vertical pairs do **not** collapse the
\(m^{3/2}\) target neighbourhoods into a small number of identical
clusters.

## 6. The full nested higher-overlap hierarchy

Let \(\Xi_k^{\rm nest}(P)\) be the contribution to

\[
 {1\over A}\sum_E\binom{|E\cap P|}{k}
\]

from (k)-sets of targets in (P) which form a strict inclusion chain.

### Theorem 6.1 (nested hereditary overlap bound)

For fixed (D), uniformly for (k\ge2),

\[
 \boxed{
 \Xi_k^{\rm nest}(P)
 \le
 2\left(\sum_{q=0}^Qc_q\right)
 \left({C_D\over m}\right)^{k-1},}
\tag{6.1}
\]

where (C_D<\infty) depends only on (D). In particular, for fixed (k),

\[
 \boxed{
 \Xi_k^{\rm nest}(P)=O_D(m^{5/2-k}).}
\tag{6.2}
\]

#### Proof

Fix a rank profile

\[
 r_1<\cdots<r_k,qquad h_i=r_{i+1}-r_i.
\]

Anchor at the endpoint whose signed depth has largest absolute value, and
write (c_*=c_{q_*}). Given its phase, Lemma 4.1 gives at most

\[
 \prod_{i=1}^{k-1}(h_i+4D+1)
\tag{6.3}
\]

phase tuples producing a nested chain. Since the anchor must be one of the
first (c_*) priority phases, both the fixed path and the catalogue
average contain at most (c_*) times (6.3) such chains.

Starting from a fixed endpoint target, the number of ambient completions
is at least

\[
 \prod_{i=1}^{k-1}\binom{m-Q}{h_i}.
\tag{6.4}
\]

Also (Nc_*\le\binom{2m}{m-q_*}). Double counting exactly as in
Theorem 5.1 therefore bounds the contribution of this rank profile by

\[
 c_*\prod_{i=1}^{k-1}
 {(h_i+4D+1)^2\over\binom{m-Q}{h_i}}.
\tag{6.5}
\]

There are two choices for the extreme endpoint. Dropping the restriction
on the total rank span and summing the gaps independently gives

\[
 \Xi_k^{\rm nest}(P)
 \le2\left(\sum_{q=0}^Qc_q\right)
 \left(
 \sum_{h\ge1}{(h+4D+1)^2\over\binom{m-Q}{h}}
 \right)^{k-1}.
\tag{6.6}
\]

Because (Q=o(m)), the last sum is (O_D(1/m)), dominated by (h=1).
This proves (6.1), and (5.10) gives (6.2). \(\square\)

For every fixed (B<\infty) and every (z\ge1/\log m), Theorem 6.1
immediately gives

\[
 \boxed{
 \sum_{k=2}^{2Q+1}
 \Xi_k^{\rm nest}(P)\left({B\over z}\right)^{k-2}
 =O_D(\sqrt m).}
\tag{6.7}
\]

Indeed the ratio after the (k=2) term is

\[
 O_D\left({B\log m\over m}\right)=o(1).
\]

Normalized by the augmented edge size, (6.7) is (O_D(1/m)). This is the
desired exponentially weighted hierarchy for every vertically nested
collection, including collections whose members occur at different
phases.

## 7. The depth-one hereditary obstruction

The preceding estimates concern the undeleted symmetric catalogue. They
do not survive target deletion merely by changing the priority order.

Put

\[
 d_1=M-c_1.
\tag{7.1}
\]

For the even middle layer,

\[
 \lambda_1={W\over\binom{2m}{m-1}}={m+1\over m}.
\]

At the first crossing, \(\lambda_H\ge M\), and therefore

\[
 c_1
 =\min\left\{M,\left\lfloor{\lambda_H\over\lambda_1}\right\rfloor\right\}
 \ge
 \left\lfloor{Mm\over m+1}\right\rfloor
 \ge M-2.
\tag{7.2}
\]

Hence

\[
 \boxed{d_1\in\{0,1,2\}.}
\tag{7.3}
\]

### Theorem 7.1 (priority coding cannot give hereditary survival)

Fix one undecorated exactly-rainbow base trajectory. Let \(B\) be the set
of its phases at which at least one forbidden depth-one target occurs.
There exists a calibrated priority decoration avoiding every forbidden
depth-one target if and only if

\[
 \boxed{|B|\le d_1.}
\tag{7.4}
\]

In particular, three bad phases annihilate every priority decoration of
the base trajectory.

#### Proof

Depth one claims precisely the first (c_1=M-d_1) phases. Every bad
phase must therefore occupy one of the (d_1) unclaimed priority slots.
This is possible exactly when (7.4) holds. \(\square\)

For example, under independent depth-one deletion with density \(\delta\),
the survival probability of a fixed base path is at most

\[
 \sum_{j=0}^{2}\binom Mj\delta^j(1-\delta)^{M-j}.
\tag{7.5}
\]

It is exponentially small as soon as \(\delta\) is a fixed positive
constant, and tends to zero whenever \(M\delta\to\infty\).

This does not disprove a one-shot common matching: the catalogue contains
enormously many different base trajectories, and a successful selection
may correlate them globally with the residual rows. It proves the exact
narrower statement needed for the audit:

\[
 \boxed{
 \text{raw overlap summability plus priority reprioritization is not a
 hereditary nibble theorem.}}
\tag{7.6}
\]

Any iterative proof must show that, after each round, almost every
remaining carrier still has many **different base trajectories** meeting
the hard depth-one support condition. Moments of the undeleted decorated
hypergraph do not imply that statement.

## 8. Exact frontier

The bounded-displacement adjacent-switch catalogue now has the following
audited properties.

* It is literal and exactly rainbow in every protected row.
* It retains all calibrated tag and target degrees.
* Every multiple codegree has the exact formula (2.6).
* Its complete pair mass is sharply \(\Theta(\sqrt m)\), only an
  (O(1/m)) fraction of the single-conflict mass.
* Every nested higher-overlap series is exponentially summable by (6.7).

Thus a proposed common matching cannot be rejected merely because the
adjacent owner--facet codegree is (1/m). The correct remaining issue is
residual base-path support.

A theorem sufficient for the deterministic catalogue route would be:

> **Residual D-banded path theorem.** At every stage down to
> (R=o(N)) unused carrier tags, every residual carrier family admits a
> near-regular subcatalogue of (D=1) base trajectories having at most two
> forbidden depth-one phases and satisfying the membership-atom overlap
> hierarchy (2.6) after conditioning.

Together with an average-overlap/column nibble, this would yield the
partial common matching required by H's flagged-reserve theorem.

What remains unproved is precisely the conditioned statement. The raw
vertical overlap hierarchy itself is no longer the obstruction.

## 9. Monotone geodesic chunks: the crossing-rectangle obstruction

The preceding nested theorem does not control crossing collections. For
the monotone geodesic chunk catalogue, those collections have an exact
two-dimensional description which produces a sharp obstruction.

Write (g=\ell-1), and parameterize one oriented geodesic by

\[
 U=C\,\dot\cup\,
 \{a_1,\ldots,a_g\}\,\dot\cup\,
 \{b_1,\ldots,b_g\}\,\dot\cup R.
\tag{9.1}
\]

Define the full grid

\[
 \boxed{
 G_{i,j}=C\cup\{a_{i+1},\ldots,a_g\}
          \cup\{b_1,\ldots,b_j\},
 \qquad 0\le i,j\le g.}
\tag{9.2}
\]

Then

\[
 X_t=G_{t,t},\qquad
 L_q(t)=G_{t+q,t},\qquad
 U_q(t)=G_{t-q,t}.
\tag{9.3}
\]

Thus all protected flags form a priority-thinned diagonal strip of one
product grid. The lattice operations are literal Boolean operations:

\[
 G_{i,j}\cap G_{i',j'}=G_{\max(i,i'),\min(j,j')},
\tag{9.4}
\]

\[
 G_{i,j}\cup G_{i',j'}=G_{\min(i,i'),\max(j,j')}.
\tag{9.5}
\]

### 9.1 Exact square orbit count

Fix (s\le Q) and an interior diagonal position (t). The (s\)-square

\[
 \mathcal R_s(t)=
 \{G_{t+p,t+q}:0\le p,q\le s\}
\tag{9.6}
\]

contains

\[
 L_s=(s+1)^2
\tag{9.7}
\]

distinct Boolean targets. Its bottom has size (m-s), its top has size
(m+s), and the family records two ordered strings of (s) singleton
increments. Consequently the number of oriented ambient (s\)-squares is

\[
 \boxed{
 \mathscr R_s
 =\binom{2m}{m-s}(m+s)_s(m)_s
 ={(2m)!\over(m-s)!^2}
 =W(m)_s^2.}
\tag{9.8}
\]

Forgetting which of the two axes is called (a) changes this by at most a
factor two, irrelevant below.

The priority decoration does not sparsify polylogarithmic squares. Indeed,

\[
 c_s\ge\left\lfloor{M\over\lambda_s}\right\rfloor,
\]

so, uniformly for (s=o(m^{2/3})),

\[
 d_s:=M-c_s=O(s^2+s+1).
\tag{9.9}
\]

Every square in (9.6) is claimed whenever its (s+1) physical columns
all lie in the first (c_s) priority positions. Hence every decorated
chunk contains at least

\[
 \ell-s-(s+1)d_s=\ell-O(s^3)
\tag{9.10}
\]

claimed central (s\)-squares.

There are

\[
 B=\left\lfloor{M\over\ell}\right\rfloor N
 =(1-o(1)){W\over\ell}
\tag{9.11}
\]

carrier-copy tags. Double counting (9.6), using (9.8)--(9.11), shows that
a fixed central (s\)-square has relative degree

\[
 {\deg(\mathcal R_s)\over A}
 \ge {1-o(1)\over(m)_s^2}.
\tag{9.12}
\]

The number of host tags is

\[
 \left\lfloor{M\over\ell}\right\rfloor
 \binom{m-s}{H-s}\longrightarrow\infty,
\]

so deleting same-tag competitors changes (9.12) by (o(1)).

### Theorem 9.1 (ordinary exponential overlap hierarchy fails)

For every fixed (B_0>0), put

\[
 \mathcal K_z(P)=
 \sum_{k\ge2}\Xi_k(P)(B_0/z)^{k-2}.
\]

At (z=1/\log m), the geodesic grid catalogue satisfies

\[
 \boxed{\sup_P\mathcal K_z(P)\to\infty}
\tag{9.13}
\]

superpolynomially. More precisely, for every

\[
 s=\left\lfloor(2+\varepsilon){\log m\over\log\log m}\right\rfloor
\tag{9.14}
\]

with fixed \(\varepsilon>0\),

\[
 \boxed{
 \Xi_{(s+1)^2}(P)
 \ge(1-o(1)){\ell\over(m)_s^2},}
\tag{9.15}
\]

and therefore

\[
 \log\left[
 \Xi_{(s+1)^2}(P)(B_0\log m)^{(s+1)^2-2}
 \right]
 \ge
 (2\varepsilon+\varepsilon^2+o(1))
 { (\log m)^2\over\log\log m}.
\tag{9.16}
\]

#### Proof

A fixed path contains \((1-o(1))\ell\) squares by (9.10), and every one
has the relative degree (9.12). This proves (9.15). Since
\(\log(m)_s=s\log m+o(s\log m)\), substitution of (9.14) gives (9.16).
\(\square\)

Thus Theorem 6.1 is genuinely a **nested** theorem. Crossing grid
rectangles make the unrestricted higher-overlap hierarchy false.

For a Bernoulli deleted-target density (f), the same calculation enters
the normalized second moment with weight

\[
 (1-f)^{-(s+1)^2}.
\]

It becomes obstructive once

\[
 -\log(1-f)\gg{\log m\over Q},
\tag{9.17}
\]

but not at a single owner-scale bite (f=O(1/M)). Hence the square is a
cumulative/hereditary obstruction, not a first-bite obstruction.

## 10. A cheap width-three conflict removes every dangerous square

The grid also supplies a promising exact pruning mechanism.

Order grid cells by Boolean inclusion. In the coordinates of (9.2), an
antichain is a sequence

\[
 i_1<\cdots<i_s,qquad j_1<\cdots<j_s.
\tag{10.1}
\]

Each full grid is a sublattice of the Boolean lattice by (9.4)--(9.5), so
the intersection of two full grids is again a sublattice. An (s\)-element
antichain in that intersection generates the compressed (s\times s)
subgrid

\[
 \{G_{i_p,j_q}:1\le p,q\le s\}.
\tag{10.2}
\]

In particular, forbidding a shared three-antichain forbids every shared
square of side at least two and leaves full-grid intersections of width at
most two.

### Theorem 10.1 (relative degree of the three-antichain conflict)

Join two catalogue chunks on distinct tags when their **full** geodesic
grids share a three-element antichain. If \(\Delta_{\rm bad}\) is the
maximum degree of this graph, then

\[
 \boxed{
 {\Delta_{\rm bad}\over A}
 \le m^{-3+o(1)}.}
\tag{10.3}

The same estimate with the protected strip in place of the full grid is

\[
 O\left({\ell Q\over m^4}\right).
\tag{10.4}
\]

#### Proof

Take three antichain cells with successive positive coordinate gaps

\[
 \alpha_1,\alpha_2\ge1,qquad
 \beta_1,\beta_2\ge1.
\]

Conditioned on the first target, the other two targets prescribe four
disjoint coordinate blocks. Full coordinate symmetry gives relative
degree at most a constant times

\[
 {1\over
 \binom{m-g}{\alpha_1,\alpha_2}
 \binom{m-g}{\beta_1,\beta_2}}.
\tag{10.5}
\]

For a fixed starting cell, summing all positive gaps in (10.5) is
\(O(m^{-4})\), dominated by four unit gaps. There are (O(\ell Q))
starting cells in the protected strip, proving (10.4).

For the full grid, sum by its rank diagonal. A rank-(m+d) target has
normalized load (O(\lambda_d)), where

\[
 \lambda_d={W\over\binom{2m}{m-d}}
 =\exp(d^2/m+o(1))
\]

uniformly for \(|d|\le g=o(m^{2/3})\). Therefore

\[
 {\Delta_{\rm bad}\over A}
 \le
 O\left({\ell\over m^4}
 \sum_{|d|\le g}\lambda_d\right)
 \le {\ell g\over m^4}\exp(g^2/m+o(1)).
\tag{10.6}
\]

For (g\sim\sqrt{QH}\), one has
\(\ell g=m^{1+o(1)}\) and
\(\exp(g^2/m)=m^{o(1)}\). This proves (10.3). \(\square\)

The estimate is strong enough for a direct independent thinning.

In the normalization of
`RECTANGLE_BAD_GRAPH_BALANCED_PRUNING_LEMMA_20260725.md`, all calibrated
tag and protected-target fibres have minimum degree

\[
 d=(1-o(1))A.
\]

Thus Theorem 10.1 gives the exact relative bad-degree estimate

\[
 \boxed{
 \xi_3:={\Delta_{\rm bad}+1\over d}=m^{-3+o(1)}.}
\tag{10.6a}
\]

Taking

\[
 L=Q\log m
\]

in that balanced pruning lemma gives

\[
 {L\over Q}\to\infty,
 \qquad
 {1\over L\xi_3}=m^{5/2-o(1)}\gg\log Q.
\tag{10.6b}
\]

Consequently its exceptional weighted fibre mass is (o(W)), and every
good retained fibre has degree (m^{5/2-o(1)}). This is larger than the
square of the protected chunk size (m^{1+o(1)}).

### Proposition 10.2 (part-balanced square-free thinning)

Put

\[
 \varepsilon=m^{-3+o(1)},\qquad L=Q\log m,
 \qquad p={1\over \varepsilon A L}.
\tag{10.7}
\]

Mark every catalogue chunk independently with probability (p), and
delete each marked chunk having a marked bad neighbour. The retained
catalogue has no pair sharing a three-antichain. Moreover, for all but an
\(O(1/L)\) fraction of carrier-tag groups and protected-target groups, its
degree is at least

\[
 \boxed{
 \mu/4,\qquad
 \mu={1\over\varepsilon L}=m^{5/2-o(1)}.}
\tag{10.8}
\]

#### Proof

Every relevant group has size \(\Theta(A)\). Its marked count has mean
\(\Theta(\mu)\) and is below half its mean with probability
\(e^{-\Omega(\mu)}\). The expected number of its marked vertices deleted
because of a marked bad neighbour is at most

\[
 O(Ap^2\Delta_{\rm bad})=O(\mu/L).
\]

Markov's inequality shows that only an (O(1/L)) fraction of groups can
lose more than one quarter of their expected marked degree. Average over
all groups and fix one outcome. \(\square\)

For two retained chunks, their full-grid intersection is a sublattice of
width at most two. By Dilworth and the fact that a product grid has height
\(2g+1\),

\[
 \boxed{|\mathcal G(P)\cap\mathcal G(P')|\le4g+2.}
\tag{10.9}

This pruning leaves polynomial degree (m^{5/2-o(1)}), comfortably larger
than the square of the protected chunk size (m^{1+o(1)}).

The remaining mathematical gate is now much narrower:

> **Width-two grid-overlap theorem.** Prove that, after the thinning in
> Proposition 10.2, intersections which are width-two sublattices satisfy
> the exponentially weighted overlap/concentration estimates required by
> a column nibble.

The expected bound is favorable: a width-two sublattice spanning (a)
steps in the (a)-direction and (b) steps in the (b)-direction has at
most (2(a+b+1)) cells, whereas sharing it costs the two ordered blocks
roughly ((m)_a^{-1}(m)_b^{-1}). At weight (O(\log m)), each extra span
then carries ratio (O((\log m)^2/m)=o(1)). A complete uniform count of
all width-two sublattice shapes is still required.

This width-two theorem, rather than the false unrestricted hierarchy in
Theorem 9.1, is the next grid-aware overlap problem.

## 11. The width-two census is summable

The remaining census in fact has a clean raw bound.

Let (P,E) be two full geodesic grids surviving the three-antichain
conflict. Put

\[
 \mathcal L=\mathcal G(P)\cap\mathcal G(E).
\]

If \(|\mathcal L|\ge2\), let (I=\bigcap\mathcal L),
\(J=\bigcup\mathcal L), and put

\[
 t=|J\setminus I|.
\tag{11.1}
\]

### Lemma 11.1 (width-two shape count)

For every such intersection,

\[
 \boxed{|\mathcal L|\le2(t+1).}
\tag{11.2}
\]

For a fixed grid (P), the number of width-two sublattices with parameter
(t) is at most

\[
 \boxed{8\ell^2(t+1)16^t.}
\tag{11.3}
\]

#### Proof

The interval from (I) to (J) has height at most (t+1). Dilworth's
theorem and width at most two give (11.2).

In the coordinates of (P), write the two coordinate spans as (a,b),
so (a+b=t). There are at most \(\ell^2(t+1)\) choices of a bounding box.
Every width-two set is the union of two chains. A chain in an
\(a\)-by-\(b\) box is contained in a monotone lattice path; there are at
most (2^t) such paths and at most (2^{t+1}) subsets of one path. Thus
there are at most (2\cdot4^t) chains and at most (4\cdot16^t) ordered
pairs of chains. This proves (11.3), with slack for duplicate
representations. \(\square\)

### Lemma 11.2 (span codegree)

Uniformly for (1\le t\le2g\), a fixed width-two sublattice of span (t)
has raw relative degree at most

\[
 \boxed{
 m^{o(1)}{t+1\over\binom{m-g}{t}}.}
\tag{11.4}
\]

#### Proof

Every competitor containing the sublattice contains its meet (I) and
join (J). Given an occurrence of (I), a geodesic grid has at most
(t+1) cell displacements which can produce the prescribed nested
rank-(t) extension. The prescribed difference (J\setminus I) is one
of at least \(\binom{m-g}{t}\) possible coordinate blocks.

The normalized degree of a full-grid target of rank (m+d),
\(|d|\le g\), is at most

\[
 O(\lambda_d)\le\exp(g^2/m+o(1))=m^{o(1)}.
\]

Multiplying these two bounds proves (11.4). \(\square\)

For (w\ge1), define the raw exponential intersection excess

\[
 \mathfrak M_w(P)
 ={1\over A}\sum_{E:\operatorname{tag}(E)\ne\operatorname{tag}(P)}
 \left(w^{|\mathcal G(P)\cap\mathcal G(E)|}
       -1-(w-1)|\mathcal G(P)\cap\mathcal G(E)|\right).
\tag{11.5}
\]

### Theorem 11.3 (width-two exponential census)

After forbidding shared three-antichains, uniformly for

\[
 1\le w\le C\log m
\]

with fixed (C),

\[
 \boxed{\sup_P\mathfrak M_w(P)=m^{o(1)}.}
\tag{11.6}

The same bound holds, a fortiori, for the priority-claimed protected
intersection.

#### Proof

Use (11.2)--(11.4) and sum over all possible intersection sublattices:

\[
 \mathfrak M_w(P)
 \le
 m^{o(1)}\ell^2
 \sum_{t=1}^{2g}
 { (t+1)^2 16^t w^{2(t+1)}
  \over\binom{m-g}{t}}.
\tag{11.7}
\]

The ratio of consecutive summands is at most

\[
 O\left(w^2{g\over m-g}\right)
 =m^{-1/2+o(1)}.
\tag{11.8}
\]

Thus the (t=1) term dominates. Since
\(\ell^2/m=QH/m=m^{o(1)}\) and (w=m^{o(1)}), the right side of
(11.7) is (m^{o(1)}). \(\square\)

This closes the **raw shape census** left open after Proposition 10.2.
It also explains why width three is the correct cutoff:

* unrestricted intersections contain square area (s^2) at perimeter
  cost (2s), causing Theorem 9.1;
* width-two intersections have area at most twice their span, so every
  extra span costs (m^{1-o(1)}) and gains only (O(\log^2m)) in the
  exponential weight.

The independent thinning can preserve this census in weighted average.
Conditioned on one chunk being marked, its expected marked width-two
intersection excess is (pA\,m^{o(1)}). Summing over chunks and applying
Markov simultaneously with Proposition 10.2 gives an outcome in which:

1. all shared three-antichains are absent;
2. all but (o(W)) weighted tag/target fibres have degree
   (m^{5/2-o(1)}) when (L=Q\log m); and
3. all but an (o(1)) weighted fraction of retained candidates have
   normalized width-two exponential excess (m^{o(1)}).

What is still not automatic is hereditary propagation through all matching
bites. The new reduced gate is no longer an overlap enumeration problem;
it is a residual-degree theorem for this width-two-pruned catalogue.
