# Fourth-wave G: four-box endpoint null space and SCD gluing rigidity

## 0. Verdict

The endpoint-potential proof has an exact nonnegative slack decomposition.
Its one-partition equality patterns are completely rigid, and the coupled
two-partition word inequality has no equality case on any nontrivial band.

The rigidity survives four-block aggregation. Let \(W=W(N)\), \(R=\sqrt N\),
and take the positive-density family of four-chain product boxes whose first
three heights lie in \([0.1R,0.2R]\) and whose fourth height lies in
\([0.7R,0.8R]\). Define

\[
 \Gamma=\sum_{\mathcal B}
 \frac{w_{\mathcal B}H_{\mathcal B}}{s_{\mathcal B}},
 \qquad
 \mathcal S=\sum_{\mathcal B}
 \left[
 s_{\mathcal B}(\delta_L(\mathcal B)+\delta_R(\mathcal B))
 -w_{\mathcal B}H_{\mathcal B}
 \right].
 \tag{0.1}
\]

Here \(w_{\mathcal B}\) is the plateau width,
\(H_{\mathcal B}\) its height, \(s_{\mathcal B}\) its long side, and
\(\delta_L,\delta_R\) are the endpoint-class excesses above width. If a
universal word has length \(W+d\), and \(P_{\rm sh}\) counts physical
positions used in at least one orientation by two different product boxes,
then

\[
 \boxed{
 P_{\rm sh}\ge
 \frac{
 [H_{\min}(\Gamma-2d)-\mathcal S]_+
 }{4(H_{\max}+1)}.
 }
 \tag{0.2}
\]

For the displayed height windows,

\[
 \Gamma=\Theta(W),\qquad H_{\min},H_{\max}=\Theta(R).
 \tag{0.3}
\]

Consequently

\[
 d=o(W),\quad \mathcal S=o(RW)
 \quad\Longrightarrow\quad
 \boxed{P_{\rm sh}=\Omega(W)}.
 \tag{0.4}
\]

Thus, in a word of length \(W+o(W)\), endpoint equality or aggregate
near-equality at the natural \(R^4\) per-box slack scale cannot be fused
through \(o(W)\) shared positions. Conversely, an \(o(W)\)-portal
construction of length \(W+o(W)\) must satisfy

\[
 \boxed{\mathcal S=\Omega(RW),}
 \tag{0.5}
\]

so it must be macroscopically far from the endpoint-dual null space.

The phrase “\(o(W)\) global endpoints” cannot literally mean all endpoint
positions: the \(W\) middle-rank targets already require \(W\) distinct left
endpoints and \(W\) distinct right endpoints. Throughout this report it
means \(o(W)\) physical positions at which same-orientation cross-box
sharing occurs. It is not a claim about total endpoints or word-length
overhead.

This does not disprove the global contiguous-OR conjecture. A word of length
\(W+o(W)\) may use \(\Theta(W)\) already-existing positions as bounded-degree
portals. Alternatively, Section 7 shows that high degree is locally
realizable at \(\Theta(R)\) slack per served class. It does not construct the
aggregate \(\mathcal S=\Omega(RW)\) packing from (0.5). Both a baseline-wide
near-null braid and a coherent sparse high-slack chronology remain unproved.

All statements labelled theorem, lemma, proposition, or corollary are
unconditional. The three replacement lemmas in Section 9 are explicitly
**UNPROVED**.

---

## 1. Endpoint partitions

Let

\[
 Q(p,q,r,s)=[0,p]\times[0,q]\times[0,r]\times[0,s],
\]

put

\[
 P=p+q+r,\qquad V=(p+1)(q+1)(r+1),\qquad H=s-P,
 \tag{1.1}
\]

assume \(P>0\), and first take \(H\ge1\). The condition \(P>0\) ensures
that every selected plateau target is nonzero, as required by the
contiguous-OR convention. The plateau layers are

\[
 \Lambda_j=
 \{(x,y,z,P+j-x-y-z):0\le x\le p,\ 0\le y\le q,\ 0\le z\le r\},
 \qquad 0\le j\le H.
 \tag{1.2}
\]

Each layer has \(V\) targets. Use

\[
 \phi(x,y,z,w)=x+y+z,\qquad 0\le\phi\le P.
 \tag{1.3}
\]

Choose one literal witnessing interval for every selected target. Group the
targets by common left endpoint and, separately, by common right endpoint.
Each class is a coordinatewise chain. Moreover, a left class and a right
class meet in at most one target: two targets in their intersection would
have the same physical interval and hence the same union.

For one orientation \(\varepsilon\in\{L,R\}\), let
\(\mathscr C_\varepsilon\) be its nonempty endpoint classes restricted to
the plateau and write

\[
 C_\varepsilon=V+\delta_\varepsilon.
 \tag{1.4}
\]

Let \(A_j^\varepsilon\) be the classes meeting \(\Lambda_j\), and set

\[
 M_j^\varepsilon=\mathscr C_\varepsilon\setminus A_j^\varepsilon.
 \tag{1.5}
\]

A chain meets an antichain at most once, so

\[
 |A_j^\varepsilon|=V,\qquad
 |M_j^\varepsilon|=\delta_\varepsilon.
 \tag{1.6}
\]

All class minima and maxima below are taken inside the retained target
family.

---

## 2. Exact flat slack and equality

Suppress the orientation and define

\[
 \mathsf A=\sum_{j=0}^{H-1}|M_j\cap M_{j+1}|,
 \tag{2.1}
\]

\[
 \Phi=\sum_{K\in\mathscr C}
 \bigl(\phi(\max K)-\phi(\min K)\bigr).
 \tag{2.2}
\]

Let \(h\) and \(v\) be the numbers of transverse and fourth-coordinate
plateau covers, respectively, whose two targets lie in one endpoint class.
Put

\[
 \mathsf B=P\delta-\Phi,\qquad
 \mathsf G=\Phi-h,\qquad
 \sigma=\mathsf A+\mathsf B+\mathsf G.
 \tag{2.3}
\]

### Theorem 2.1 (exact one-partition ledger)

The three summands in (2.3) are nonnegative integers, and

\[
 \boxed{v=VH-s\delta+\sigma.}
 \tag{2.4}
\]

#### Proof

The missing-class formulation turns inclusion-exclusion into an identity:

\[
 \begin{aligned}
 |A_j\cap A_{j+1}|
 &=C-|M_j\cup M_{j+1}|\\
 &=V-\delta+|M_j\cap M_{j+1}|.
 \end{aligned}
 \tag{2.5}
\]

Comparable targets in adjacent ranks form a genuine cover. Summing (2.5),

\[
 h+v=H(V-\delta)+\mathsf A.
 \tag{2.6}
\]

Exactly \(\delta\) classes miss each boundary. The two boundary layers have
the same \(\phi\)-multiset, hence

\[
 \Phi=
 \sum_{K\in M_H}\phi(\max K)
 -\sum_{K\in M_0}\phi(\min K).
 \tag{2.7}
\]

Therefore

\[
 \mathsf B=
 \sum_{K\in M_H}(P-\phi(\max K))
 +\sum_{K\in M_0}\phi(\min K)\ge0.
 \tag{2.8}
\]

Every transverse adjacent cover contributes one to \(\Phi\). Every remaining
comparison between consecutive retained targets of a class has nonnegative
transverse gain, so \(\mathsf G=\Phi-h\ge0\). Substitute
\(h=P\delta-\mathsf B-\mathsf G\) into (2.6) and use \(s=P+H\).
\(\square\)

Let \(U\) be the number of the \(VH\) vertical plateau covers used by
neither endpoint partition. Orthogonality makes the two used vertical-edge
sets disjoint. Adding (2.4) gives

\[
 \boxed{
 s(\delta_L+\delta_R)-VH
 =U+\sigma_L+\sigma_R.
 }
 \tag{2.9}
\]

### Corollary 2.2 (formal equality classification)

Equality in the one-partition estimate \(v\ge VH-s\delta\) holds exactly
when:

1. no endpoint class misses two consecutive plateau layers;
2. every class missing the bottom starts at potential \(0\), and every class
   missing the top ends at potential \(P\);
3. every positive transverse gain occurs on an adjacent transverse cover,
   so every rank-skipping comparison has zero transverse gain.

Coupled equality additionally requires the two partitions to exhaust all
vertical plateau covers.

#### Proof

The three conditions are precisely
\(\mathsf A=\mathsf B=\mathsf G=0\); coupled equality also requires \(U=0\)
in (2.9). \(\square\)

This classification has a sharp entrance consequence. If \(\sigma=0\), a
bottom-missing class must appear in layer \(1\), since otherwise it belongs
to both \(M_0\) and \(M_1\). Its first target must have \(\phi=0\). There is
only one such target in layer \(1\), so

\[
 \boxed{\sigma=0\Longrightarrow\delta\le1.}
 \tag{2.10}
\]

The reflected exit statement is identical.

For \(p,q,r\ge1\), even coupled endpoint equality in (2.9) is impossible.
Indeed

\[
 (p+1)(q+1)(r+1)\ge2(p+q+r+1),
 \tag{2.11}
\]

with equality only at \(p=q=r=1\). Since \(H\ge1\),
\(VH/(P+H)\ge2\). Equations (2.9)--(2.10) leave only
\(p=q=r=H=1\) and \(\delta_L=\delta_R=1\). Then both bottom-missing
classes begin at the same layer-\(1\), potential-\(0\) target, so neither
partition uses the vertical edge entering it. This contradicts \(U=0\).

---

## 3. Empty two-sided word null space

Let the physical word have length \(n=V+D\) and put

\[
 e_L=n-C_L,\qquad e_R=n-C_R.
 \tag{3.1}
\]

Since \(\delta_\varepsilon=D-e_\varepsilon\), (2.9) becomes

\[
 \boxed{
 2sD-VH=s(e_L+e_R)+U+\sigma_L+\sigma_R.
 }
 \tag{3.2}
\]

### Theorem 3.1

For \(H\ge1\), equality in the unrounded word bound \(2sD\ge VH\) is
impossible.

#### Proof

If the right side of (3.2) vanished, then
\(e_L=e_R=U=\sigma_L=\sigma_R=0\). Hence
\(\delta_L=\delta_R=D\le1\) by (2.10).

If \(D=0\), (2.4) says that each partition uses all \(VH>0\) vertical
edges, contradicting orthogonality. If \(D=1\), both unique bottom-missing
classes start at the same layer-\(1\), potential-\(0\) target. The vertical
edge entering that target is used by neither partition, contradicting
\(U=0\). \(\square\)

Thus the literal coupled null space is empty. The useful object is the
asymptotic null space in which the right side of (3.2) is small compared
with its natural \(R^4\) edge scale.

---

## 4. Entrance energy and near-null geometry

An internal start at layer \(i\ge1\) and base point \(X=(x,y,z)\) has cost

\[
 c^-(i,X)=i-1+\phi(X).
 \tag{4.1}
\]

An internal end at layer \(j\le H-1\) has reflected cost

\[
 c^+(j,X)=H-j-1+P-\phi(X).
 \tag{4.2}
\]

Let \(\rho(d)\) be the sum of the \(d\) cheapest entrance costs, with
\(\rho(0)=0\).

### Lemma 4.1 (entrance energy)

For one endpoint partition,

\[
 \boxed{\sigma\ge2\rho(\delta).}
 \tag{4.3}
\]

#### Proof

If a class first appears in layer \(i\), its initial missing run contributes
at least \(i-1\) to \(\mathsf A\), and (2.8) contributes
\(\phi(\min K)\). The \(\delta\) starts are distinct targets, so their total
cost is at least \(\rho(\delta)\). Reversing layers and complementing the
three base coordinates gives the same bound for the \(\delta\) exits.
Prefix and suffix missing runs of a nonempty class are disjoint; internal
missing runs and \(\mathsf G\) are nonnegative. \(\square\)

Before any side truncation, cost \(c\) has multiplicity

\[
 \binom{c+3}{3}.
 \tag{4.4}
\]

Define \(\rho_4(0)=0\). For \(d\ge1\), choose \(h\) with

\[
 \binom{h+3}{4}<d\le\binom{h+4}{4},
\]

and set

\[
 \boxed{
 \rho_4(d)=
 4\binom{h+3}{5}
 +h\left(d-\binom{h+3}{4}\right).
 }
 \tag{4.5}
\]

This follows from

\[
 \sum_{c=0}^{h-1}\binom{c+3}{3}=\binom{h+3}{4},
 \qquad
 \sum_{c=0}^{h-1}c\binom{c+3}{3}=4\binom{h+3}{5}.
 \tag{4.6}
\]

Moreover,

\[
 \rho_4(d)=
 \left(\frac45\,24^{1/4}+o(1)\right)d^{5/4}.
 \tag{4.7}
\]

On a compact strict-dominant window

\[
 p,q,r,H,s\asymp R,
 \tag{4.8}
\]

put \(S_0=\delta_L+\delta_R\). If \(S_0>2VH/s\), the conclusion below is
already stronger than required. Otherwise \(S_0=O(R^3)\), and the first
\(S_0\) costs are untruncated because their largest cost is
\(O(R^{3/4})\). In this branch, (2.9), Lemma 4.1, and discrete convexity of
\(\rho_4\) give

\[
 sS_0-VH
 \ge2\rho_4(\delta_L)+2\rho_4(\delta_R).
 \tag{4.9}
\]

Since \(S_0\ge VH/s=\Theta(R^3)\), the right side in the second branch is
\(\Omega(R^{15/4})\). Uniformly across both branches,

\[
 \boxed{
 S_0\ge\frac{VH}{s}+\Omega(R^{11/4}),
 \qquad
 D\ge\frac{VH}{2s}+\Omega(R^{11/4}).
 }
 \tag{4.10}
\]

This is a subleading correction to the cubic local excess.

If

\[
 sS_0-VH=o(R^4),
 \tag{4.11}
\]

then for some \(\varepsilon_R\to0\), all but \(o(R^3)\) internal starts lie
in

\[
 (i-1)+\phi(X)\le\varepsilon_RR,
 \tag{4.12}
\]

and all but \(o(R^3)\) internal ends lie in the reflected corridor.
Furthermore, the total number of unused vertical edges, consecutive
double-misses, and units of transverse potential transported across rank
skips is \(o(R^4)\). These assertions follow termwise from (2.9) and
Markov's inequality applied to (4.1)--(4.2).

Thus a leading-scale near-null pattern almost two-colors the vertical band,
with chain births and deaths confined to sublinear corner corridors.

---

## 5. Exact sloped-band ledger

Assume \(s\ge P>0\). Fix

\[
 0\le k\le\min\{p,q,r\},
\]

retain every rank from \(P-k\) through \(s+k\), and put

\[
 J=s-P+2k,\qquad Q=J+P=s+2k,
 \tag{5.1}
\]

\[
 F=\binom{k+2}{3},\qquad
 E=\binom{k+3}{4},\qquad
 B_0=V-F,
 \tag{5.2}
\]

\[
 T=(J+1)V-2E,\qquad
 \Delta_\phi=PF-6\binom{k+2}{4}.
 \tag{5.3}
\]

Here \(T\) is the band population, \(B_0\) is either boundary size, and
\(\Delta_\phi\) is top boundary potential minus bottom boundary potential.
The band contains \(T-V\) vertical covers.

For one endpoint partition with \(C\) classes, let \(A_i\) and \(M_i\) be
its occupied and missing class sets in band layer \(i\). Put

\[
 d_0=C-B_0,\qquad
 \mathsf A=\sum_{i=0}^{J-1}|M_i\cap M_{i+1}|,
 \tag{5.4}
\]

\[
 \mathsf B=\Delta_\phi+Pd_0-\Phi,\qquad
 \mathsf G=\Phi-h,\qquad
 \sigma=\mathsf A+\mathsf B+\mathsf G.
 \tag{5.5}
\]

As in (2.8),

\[
 \mathsf B=
 \sum_{K\text{ misses top}}(P-\phi(\max K))
 +\sum_{K\text{ misses bottom}}\phi(\min K)\ge0.
 \tag{5.6}
\]

### Theorem 5.1

For one partition,

\[
 \boxed{
 v=2T-2B_0-\Delta_\phi+PB_0-QC+\sigma.
 }
 \tag{5.7}
\]

For a word of length \(n=V+D\), put \(e_L=n-C_L\),
\(e_R=n-C_R\), and

\[
 N_k=(s-P+2k)V
 +6\binom{k+2}{4}
 -(4P+2)\binom{k+2}{3}.
 \tag{5.8}
\]

If \(U_k\) is the number of vertical band covers used by neither endpoint
partition, then

\[
 \boxed{
 2QD-N_k=Q(e_L+e_R)+U_k+\sigma_L+\sigma_R.
 }
 \tag{5.9}
\]

#### Proof

For adjacent layer sizes \(m_i,m_{i+1}\),

\[
 |A_i\cap A_{i+1}|
 =m_i+m_{i+1}-C+|M_i\cap M_{i+1}|.
\]

After summation,

\[
 h+v=2T-2B_0-JC+\mathsf A.
\]

Substitute
\(h=\Delta_\phi+P(C-B_0)-\mathsf B-\mathsf G\) to obtain (5.7).
The two vertical-edge sets are disjoint and lie in an ambient set of size
\(T-V\). Add (5.7), substitute
\(C_\varepsilon=n-e_\varepsilon\), and simplify using (5.1)--(5.3).
\(\square\)

### Corollary 5.2 (empty sloped word null space)

For every nontrivial band \(J\ge1\), equality in \(2QD\ge N_k\) is
impossible.

#### Proof

If the right side of (5.9) vanished, then both partitions would have
\(e_L=e_R=0\) and \(\sigma=0\). Hence \(C_L=C_R=V+D\). A bottom-missing
class must begin in layer \(1\) at the unique potential-\(0\) target, so

\[
 C-B_0=D+F\le1.
 \tag{5.10}
\]

If \(D+F=0\), then \(D=F=0\) and this is the nontrivial flat case of
Theorem 3.1. If \(D+F=1\), the two unique bottom-missing classes begin at
the same layer-\(1\), potential-\(0\) target. The vertical edge entering it
is used by neither partition, so \(U_k\ge1\), a contradiction.
\(\square\)

There is also an unconditional quantitative sharpening. For
\(0\le c\le k-1\), the entrance-cost multiplicity is exactly (4.4), with no
side truncation. Since

\[
 F=\binom{k+2}{3}\le\binom{k+3}{4},
\]

the first \(F\) costs lie in this range. Each endpoint partition has at
least \(F\) internal starts and \(F\) internal ends. The entrance-energy
proof and the strict integrality from Corollary 5.2 therefore give, for
\(J\ge1\),

\[
 \boxed{
 2(s+2k)D\ge N_k+\max\{1,4\rho_4(F)\}.
 }
 \tag{5.11}
\]

For \(k=0\) or \(k=1\), \(\rho_4(F)=0\), so the new quantitative content
there is only the strict \(+1\). The entrance-energy term becomes nonzero
from \(k=2\) onward.

As \(k\to\infty\),

\[
 \rho_4(F)=
 \left(\frac{2\sqrt2}{15}+o(1)\right)k^{15/4}.
 \tag{5.12}
\]

Thus \(k\asymp R\) adds an \(\Omega(R^{11/4})\) word-length correction
beyond the leading cubic bound.

---

## 6. Four-block SCD gluing rigidity

Let \(N=4m\), with \(m\) even for convenience, split the coordinates into
four equal blocks, and fix arbitrary saturated SCDs in those blocks. Put

\[
 R=\sqrt N,\qquad W_t=\binom{t}{t/2}.
\]

The number of height-\(\ell\) chains in an SCD of \(B_m\) is

\[
 a_m(\ell)=
 \binom m{(m-\ell)/2}
 -\binom m{(m-\ell)/2-1}.
 \tag{6.1}
\]

For fixed \(0<u<v\), Stirling's formula and the parity-two Riemann sum give

\[
 \frac{\#\{C:uR\le\ell(C)\le vR\}}{W_m}
 \longrightarrow e^{-2u^2}-e^{-2v^2}>0.
 \tag{6.2}
\]

For all sufficiently large \(N\), let \(\mathscr D\) be the nonempty family
of product boxes with first three heights in
\([0.1R,0.2R]\) and fourth height in \([0.7R,0.8R]\). For
\(\mathcal B\in\mathscr D\),

\[
 w_{\mathcal B}=(p+1)(q+1)(r+1),\qquad
 H_{\mathcal B}=s-p-q-r,
 \tag{6.3}
\]

and

\[
 0.1R\le H_{\mathcal B}\le0.5R,\qquad
 s_{\mathcal B}\le0.8R,\qquad
 w_{\mathcal B}\ge0.001R^3.
 \tag{6.4}
\]

The family has positive density among the \(W_m^4\) product boxes. Central
binomial asymptotics give

\[
 W_m^4R^3=\Theta(W_N),
 \tag{6.5}
\]

so \(|\mathscr D|=\Theta(W_N/R^3)\). Define

\[
 \Gamma=\sum_{\mathcal B\in\mathscr D}
 \frac{w_{\mathcal B}H_{\mathcal B}}{s_{\mathcal B}}.
 \tag{6.6}
\]

Equations (6.2)--(6.5) imply

\[
 \boxed{\Gamma=\Theta(W_N).}
 \tag{6.7}
\]

The product boxes partition the global middle layer, hence

\[
 \sum_{\mathcal B}w_{\mathcal B}=W_N.
 \tag{6.8}
\]

Select witnesses for the full plateau in every box of \(\mathscr D\), and
only for the global-middle layer in every other product box. For
\(\mathcal B\in\mathscr D\), write

\[
 C_X(\mathcal B)=w_{\mathcal B}+\delta_X(\mathcal B),
 \qquad X\in\{L,R\},
 \tag{6.9}
\]

and define

\[
 \mathcal S_{\mathcal B}=
 s_{\mathcal B}(\delta_L+\delta_R)
 -w_{\mathcal B}H_{\mathcal B}.
 \tag{6.10}
\]

By (2.9),

\[
 \mathcal S_{\mathcal B}
 =U_{\mathcal B}+\sigma_L(\mathcal B)+\sigma_R(\mathcal B)\ge0.
 \tag{6.11}
\]

Put

\[
 \mathcal S=\sum_{\mathscr D}\mathcal S_{\mathcal B},\qquad
 H_{\min}=\min_{\mathscr D}H_{\mathcal B},\qquad
 H_{\max}=\max_{\mathscr D}H_{\mathcal B}.
 \tag{6.12}
\]

Let \(P_{\rm sh}\) count physical positions for which at least one
orientation is used by at least two selected product boxes. Boxes may be
dominant or nondominant, and witnesses may cross arbitrary seams.

### Theorem 6.1 (centered-plateau gluing rigidity)

For every universal word of length \(n=W_N+d\),

\[
 \boxed{
 P_{\rm sh}\ge
 \frac{
 [H_{\min}(\Gamma-2d)-\mathcal S]_+
 }{4(H_{\max}+1)}.
 }
 \tag{6.13}
\]

#### Proof

For an endpoint class \(K\) in a dominant box, let \(m(K)\) be the number
of plateau layers it meets, and let \(a(K)\) be the number of adjacent
layer pairs on which \(K\) misses both layers. A binary support of length
\(H+1\) with \(m\) occupied entries has at most \(m+1\) zero runs. Thus

\[
 \boxed{H_{\mathcal B}\le2m(K)+a(K).}
 \tag{6.14}
\]

Summing \(a(K)\) over all endpoint classes and both orientations gives the
\(\mathsf A_L+\mathsf A_R\) part of (6.11), so

\[
 \sum_{\mathcal B,K}a(K)\le\mathcal S.
 \tag{6.15}
\]

Form the incidence graph between product boxes and oriented physical
endpoint slots. A dominant box contributes

\[
 2w_{\mathcal B}+\delta_L(\mathcal B)+\delta_R(\mathcal B)
\]

edges, and every other box contributes at least twice its middle-layer
width. By (6.8), the graph has at least

\[
 2W_N+E,\qquad
 E:=\sum_{\mathscr D}(\delta_L+\delta_R)\ge\Gamma
 \tag{6.16}
\]

edges.

Delete one edge at every nonempty oriented physical slot, preferring a
nondominant edge when one is present. There is at most one nondominant edge
at a slot: all nondominant selected targets have rank \(N/2\), while
distinct targets with one fixed oriented endpoint form a strict chain and
therefore have distinct ranks. At most \(2n\) edges are deleted. Hence at
least

\[
 E-2d\ge\Gamma-2d
 \tag{6.17}
\]

edges remain, when this quantity is positive. Every remaining edge is
dominant and lies at a same-orientation shared slot. Call these edges
charged.

Apply (6.14) to the charged endpoint classes. By (6.15), their total target
mass is at least

\[
 \frac{H_{\min}(\Gamma-2d)-\mathcal S}{2}.
 \tag{6.18}
\]

All product-box plateaux are centered at global rank \(N/2\). At a fixed
oriented endpoint, all selected targets form a strict inclusion chain, so
there is at most one target of each rank. The union of the dominant plateau
rank intervals contains at most \(H_{\max}+1\) ranks. Thus one oriented
portal carries target mass at most \(H_{\max}+1\), and one physical position
carries at most twice that over the two orientations. Dividing (6.18) by
\(2(H_{\max}+1)\) proves (6.13). \(\square\)

### Corollary 6.2

If \(d=o(W_N)\) and \(\mathcal S=o(RW_N)\), then

\[
 \boxed{P_{\rm sh}=\Omega(W_N).}
 \tag{6.19}
\]

Equivalently, if \(d=o(W_N)\) and \(P_{\rm sh}=o(W_N)\), then

\[
 \boxed{\mathcal S=\Omega(RW_N).}
 \tag{6.20}
\]

#### Proof

Use (6.4), (6.7), and (6.13). \(\square\)

Formal exact equality, hypothetical integer-tight endpoint counts, and any
aggregate leading-scale near-null family satisfy the small-slack hypothesis.
For example, integer tightness would give
\(0\le\mathcal S_{\mathcal B}<s_{\mathcal B}=O(R)\), and hence total slack
\(O(W_N/R^2)=o(RW_N)\).

The benchmark obtained by summing the entrance-energy lower-bound scale is

\[
 (W_N/R^3)R^{15/4}
 =W_NR^{3/4}=o(RW_N).
 \tag{6.21}
\]

Thus that local estimate by itself is below the \(RW_N\) threshold. It does
not prove that actual local minimizers have small aggregate slack.
Theorem 6.1 says that every family which does have
\(\mathcal S=o(RW_N)\) requires a linear population of shared positions.

---

## 7. Degree-sharp high-slack portal

Theorem 6.1 genuinely uses small scalar slack. Rank and SCD geometry alone
permit high-degree physical portals.

Let the four block sizes be even \(m\), put \(r_0=\sqrt m\), and choose
constants

\[
 0<a<b<c<d,\qquad c>3b.
 \tag{7.1}
\]

Call factor chains of heights in \([ar_0,br_0]\) low and chains of heights
in \([cr_0,dr_0]\) high. Each window contains a fixed positive proportion
of factor chains. Let \(h\to\infty\) satisfy

\[
 h\le\min\{ar_0/4,(c-3b)r_0/4\}.
 \tag{7.2}
\]

### Lemma 7.1

There are nested sets

\[
 F_1\subset\cdots\subset F_D,\qquad D=\Theta(h),
 \tag{7.3}
\]

in \(h\) consecutive central ranks of block \(1\), lying in distinct low
SCD chains.

#### Proof

Choose a uniformly random maximal Boolean chain and inspect the \(h\)
central ranks. Every low SCD chain spans this band. At each rank, the chance
that the maximal-chain point lies in a low SCD chain is at least a fixed
\(\kappa+o(1)>0\), so the expected number of low hits is
\((\kappa+o(1))h\).

Let \(Y\) count pairs of inspected ranks whose points lie in the same SCD
chain. For ranks \(u<v\) with gap \(t\), the probability is at most

\[
 \binom{m-u}{t}^{-1}.
\]

Gap-one pairs contribute \(O(h/m)\); larger gaps contribute
\(O(h^2/m^2)\). Hence \(\mathbb EY=o(1)\). If \(X\) is the number of low
hits and \(D'\) their number of distinct SCD chains, then
\(D'\ge X-Y\), since \(q-1\le\binom q2\) for every hit multiplicity \(q\).
Some maximal chain therefore yields (7.3). \(\square\)

Choose central members \(U,U'\) of two distinct low chains in block \(2\),
a central member \(V_3\) of a low chain in block \(3\), and the central
member \(Z\) of a high chain in block \(4\). Put
\(E_i=F_i\setminus F_{i-1}\) for \(i\ge2\), and consider

\[
 E_D,\ldots,E_2,F_1\cup U\cup V_3
 \ \Vert\ Z\ \Vert\
 F_1\cup U'\cup V_3,E_2,\ldots,E_D.
 \tag{7.4}
\]

The position occupied by \(Z\) is a common right endpoint for suffix
witnesses of

\[
 T_i^-=F_i\cup U\cup V_3\cup Z,
 \tag{7.5}
\]

and a common left endpoint for prefix witnesses of

\[
 T_i^+=F_i\cup U'\cup V_3\cup Z.
 \tag{7.6}
\]

These \(2D\) targets lie in distinct strict-dominant product boxes and in
one common \(h\)-rank plateau band. Condition (7.2) guarantees the latter,
because the long height minus the sum of the three short heights is at least
\((c-3b)r_0\).

Every letter in (7.4) is nonempty. Append any universal word and choose all
other target witnesses wholly inside that appendage. The displayed
witnesses and their singleton hub classes are preserved. Thus the gadget is
literal, not fractional.

If \(r_Z\) and \(\ell_Z\) denote its right- and left-oriented box degrees,
then at the hub
\[
 r_Z=\ell_Z=D=\Theta(h),
\]
so the position supports \(2D=\Theta(h)\) oriented box roles in total. Each
served local endpoint class contains one strictly internal plateau target.
It contributes \(H_{\mathcal B}-2\) to the consecutive-miss term
\(\mathsf A\) and \(P_{\mathcal B}\), the sum of that box's three short
heights, to the boundary-potential term
\(\mathsf B\), hence \(s_{\mathcal B}-2=\Theta(r_0)\) to \(\sigma\).
The gadget buys high degree by paying this macroscopic per-class slack.

This is order-sharp local capacity, not a global fusion: it packs one hub,
not all endpoint incidences, and supplies no compatible near-width
chronology for every Boolean target.

---

## 8. Adversarial audit

The proof was checked against the following failure modes.

1. **Seam crossing.** No argument confines witnesses to boxwise subwords.
   Only the target and its actual physical endpoints are used.
2. **Unsaturated classes.** Missing layers remain explicitly in \(M_i\);
   (2.5) and its sloped analogue are identities.
3. **Rank skips.** Every positive skipped transverse gain is charged to
   \(\mathsf G\); a pure vertical skip correctly costs zero.
4. **Orthogonality.** A vertical target-poset cover cannot occur in both
   endpoint partitions, because that would put two targets in one left/right
   class intersection.
5. **Exact versus rounded equality.** Theorems 3.1 and 5.2 concern
   unrounded equality. Integer tightness creates less than one denominator
   of scalar slack and is covered by Corollary 6.2.
6. **Nondominant deletion.** A fixed oriented endpoint serves at most one
   selected nondominant middle target. Deleting it first makes every charged
   incidence in Theorem 6.1 dominant.
7. **Classes versus targets.** Inequality (6.14) converts charged classes
   into target mass before the rank-chain capacity is applied.
8. **Two orientations.** The denominator \(4(H_{\max}+1)\) records both the
   factor \(1/2\) in (6.14) and two orientations per physical position.
   Gadget (7.4) shows the orientation factor is real.
9. **SCD choice.** Height multiplicities are fixed for every SCD. Lemma 7.1
   also works for an arbitrary SCD.
10. **Scope.** \(P_{\rm sh}=\Omega(W)\) is a structural sharing conclusion,
    not a length lower bound beyond \(W\). The same \(W+o(W)\) positions may
    themselves be the portals.
11. **Sharpness.** Section 7 proves one-hub capacity only. It does not pack
    \(\Theta(W/R)\) hubs without chronology or contamination conflicts.

Independent proof audits reproduced the local slack identities, the
entrance-energy indexing, the charged-incidence deletion, the factor \(4\)
in (6.13), and the two-orientation literal hub. No finite or computational
search was used.

---

## 9. Smallest remaining replacement lemma

The equality-saturating \(o(W)\)-portal route is closed. Three clean
possibilities survive.

### Positive replacement A — UNPROVED

> **Baseline-wide near-null braid.** Construct a literal universal word of
> length \(W(N)+o(W(N))\) with
> \(P_{\rm sh}=\Theta(W(N))\) and \(\mathcal S=o(\sqrt N\,W(N))\), using
> the already unavoidable width-scale physical positions as bounded-degree
> portals while preserving all plateau witnesses.

This route is fully compatible with Theorem 6.1; the theorem says that a
near-null construction must be baseline-wide, not that it is impossible.

### Positive replacement B — UNPROVED

> **High-slack global braid.** Construct a literal universal word of length
> \(W(N)+o(W(N))\) whose four-block plateau witness system has
> \(P_{\rm sh}=o(W(N))\) and necessarily
> \(\mathcal S=\Omega(\sqrt N\,W(N))\), packing the resulting
> \(\Omega(W(N))\) extra endpoint-box incidences into high-degree portals
> while preserving all uncontaminated interval witnesses.

### Negative replacement — UNPROVED

> **Slack suppression or chronology obstruction.** Prove either that every
> width-plus-\(o(W)\) word admits a simultaneous selection of four-block
> plateau witnesses with \(\mathcal S=o(RW)\), or directly that scalar slack
> \(\Omega(RW)\) cannot be realized through \(o(W)\) shared positions under
> literal OR chronology and simultaneous left/right endpoint orders.

The degree-sharp gadget proves that rank support, SCD geometry, and arbitrary
seam crossing alone cannot establish the negative replacement. A further
ingredient must couple many hubs through time: opposite-endpoint
availability, letter contamination, or simultaneous orthogonal chain
packing.

The stable theorem-level conclusion is

\[
 \boxed{
\begin{gathered}
\text{in a word of length }W+o(W),\text{ the four-box endpoint-dual}\\
\text{equality null space cannot be fused through }o(W)
\text{ shared endpoint positions}.
\end{gathered}}
\]
