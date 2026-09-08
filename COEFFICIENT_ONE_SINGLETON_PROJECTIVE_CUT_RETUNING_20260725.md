# Corrected pruning scale resurrects the singleton projective-plane cut

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The pointwise correction in
`ISOLATED_PRUNING_FRACTIONAL_OVERLOAD_THEOREM_20260725.md`, Section 2.1,
is coefficient-accurate.  With

\[
 \delta=m^{-2/3},\qquad
 L=Qm^{2/3}\log m,
\]

it gives a rational fractional matching (x) with target loads at most
one and average tag deficit

\[
 \beta={1\over T}\sum_U\left(1-
              \sum_{e:\tau(e)=U}x_e\right)=o(1/Q).
\tag{0.1}
\]

If a fractional colour cover of the denominator-cleared point has cost
at most ((1+\varepsilon)D), exact averaging gives a colour missing at
most

\[
 {\varepsilon+\beta\over1+\varepsilon}T
\tag{0.2}
\]

tags.  Thus the literal repair ledger requires

\[
 \varepsilon+\beta=o(1/Q),
\tag{0.3}
\]

unless a separate chain-aligned reserve is proved.

The singleton/projective-plane cut is not removed by the corrected
pruning statistics.  In fact, the correction changes the natural tag
degree from the formerly used (m^{5/2-o(1)}) to

\[
 D\asymp\mu=m^{11/6-o(1)}.
\tag{0.4}
\]

At this scale there is an exact abstract rational multicover with all of
the following properties:

* every tag has degree exactly (D);
* every target has degree between (D/2) and (D);
* every two distinct protected supports meet in at most one target;
* every two-target codegree is at most one;
* the corrected atom size is exactly (1/D);
* the chronology-style one-star hitting ratio is
  (m^{-5/6+o(1)}=o(m^{-1/2+o(1)}));
* nevertheless its fractional and integral chromatic indices are at
  least (m^{1/6+o(1)}D).

The obstruction is a projective plane whose low-load point stars are
completed by nonincident private filler edges.  It has tag deficit zero.
Consequently pointwise capacity, diffuseness, width one, pair codegree,
the centered exponential moment, and the present one-star estimate do
not imply the weighted matching-cover inequality, let alone the
(1+o(1/Q)) version required by (0.3).

This is a no-go for colouring or decomposing the **whole** rational point
from the presently recorded parameters.  It is not a no-go for a direct
one-colour theorem: the example deliberately has a perfect matching made
of filler edges.  The exact positive alternatives are therefore:

1. prove a genuinely global weighted dispersal inequality for the actual
   Boolean chronology; or
2. bypass full colouring and construct one matching missing (o(T/Q))
   tags directly.

No coefficient-one conclusion is claimed.

## 1. Coefficient-accurate extraction

For completeness, let

\[
 s_U=\sum_{e:\tau(e)=U}x_e\le1,
 \qquad
 \ell_v=\sum_{e:v\in C(e)}x_e\le1,
 \qquad
 \sum_U(1-s_U)=\beta T.
\tag{1.1}
\]

Choose a common denominator (D_0) and give edge type (e) multiplicity
(D_0x_e).  The total number of occurrence edges is exactly

\[
 D_0\sum_Us_U=D_0(1-\beta)T.
\tag{1.2}
\]

Suppose a rational fractional edge-colour cover has cost
(C\le(1+\varepsilon)D_0).  Clear the denominators of its matching
coefficients by an integer (b), and delete surplus occurrences from
matching copies.  This gives an exact colouring of the (b)-fold demand
using (bC) colours.  Some colour therefore contains at least

\[
 {bD_0(1-\beta)T\over bC}
 \ge {1-\beta\over1+\varepsilon}T
\tag{1.3}
\]

edges.  Since a colour is a matching, these lie on distinct tags, and
(0.2) follows exactly.

If a missing tag costs at most

\[
 K\le(2Q+1)g,
 \qquad gT=(1+o(1))W,
\tag{1.4}
\]

then the literal repair cost supplied by (0.2) is at most

\[
 (2Q+1)(1+o(1))
 {\varepsilon+\beta\over1+\varepsilon}W.
\tag{1.5}
\]

This proves (0.3).  Notice that (arepsilon=o(1)) alone gives only
(o(T)) missed tags and is not coefficient-safe.

## 2. What changes under the new pruning scale

In the protected window,

\[
 Q=m^{1/2+o(1)},\qquad
 g=m^{1/2+o(1)},\qquad
 K=m^{1+o(1)}.
\tag{2.1}
\]

The corrected choice of (L) gives

\[
 \mu=m^{11/6-o(1)}.
\tag{2.2}
\]

Consequently

\[
 {K^2\over\mu}=m^{1/6+o(1)},
\tag{2.3}
\]

not (o(1)).  Thus the elementary bound

\[
 |\mathcal F|\le K^2-K+1
\tag{2.4}
\]

for a linear pairwise-intersecting family no longer puts
(|\mathcal F|) below the colour scale.  A projective plane essentially
attains (2.4).

The separate one-star estimate is not lost by this retuning.  Its raw
tolerance is

\[
 \varepsilon_1=m^{-1/2+o(1)},
\tag{2.5}
\]

and the relevant Chernoff exponent after the corrected pruning is

\[
 \mu\varepsilon_1=m^{4/3-o(1)}\gg m.
\tag{2.6}
\]

Hence its union bound over (exp(O(m))) target--strip pairs still has
room.  The construction below therefore satisfies the one-star estimate
rather than evading it through a failed preservation argument.

By contrast, the old simultaneous all-pair-codegree union bound does
fail after retuning.  A raw relative pair degree (m^{-1+o(1)}) has
marked mean only

\[
 \mu m^{-1+o(1)}=m^{5/6+o(1)},
\tag{2.7}
\]

whose Chernoff tail cannot be union-bounded over (exp(\Theta(m)))
pairs.  The construction below is stronger: its denominator-cleared
two-target codegrees are already at most one.

## 3. An exact calibrated projective-plane multicover

### Theorem 3.1

Let (q) be a prime power, put

\[
 k=q+1,
 \qquad n=q^2+q+1,
\tag{3.1}
\]

and let (D) be an even integer satisfying

\[
 2k<D<n.
\tag{3.2}
\]

There is a finite rational tag--target hypergraph ((\mathcal H,x)) with
(n) tags and maximum protected rank (k) such that:

1. every tag has (D) support edges, each of weight (1/D);
2. every target has (x)-load in ([1/2,1]);
3. any two distinct support edges have protected intersection at most
   one, and every two-target weighted codegree is at most (1/D);
4. for

   \[
    \Gamma_v(E)=\{P:v\in C(P),\ C(P)\cap C(E)\ne\varnothing\},
   \]

   one has, whenever (v\notin C(E)),

   \[
    x(\Gamma_v(E))
    \le \zeta:=\max\left\{{k\over D},{1\over q},{2\over D}\right\};
   \tag{3.3}
   \]

5. the (n) distinguished core edges are pairwise intersecting, and

   \[
    \chi_f'(x)\ge {n\over D},
    \qquad
    \chi'(\mathcal H_D)\ge n,
   \tag{3.4}
   \]

   where (mathcal H_D) is the denominator-cleared multihypergraph;
6. nevertheless (mathcal H) has a matching meeting every tag.

#### Proof

Let (Pi) be a projective plane of order (q), with point set
(\mathcal P) and line set (\mathcal L).  Both have cardinality (n).
Use one tag (	au_L) for every (L\in\mathcal L), and one private
target (z_L) for every tag.

Consider the bipartite nonincidence graph between (\mathcal L) and
(\mathcal P): (L) is adjacent to (p) precisely when (p\notin L).
It is (q^2)-regular.  A regular bipartite graph decomposes into perfect
matchings, so fix a decomposition

\[
 \mathcal N=M_1\dot\cup\cdots\dot\cup M_{q^2}.
\tag{3.5}
\]

Put

\[
 b={D\over2}-k.
\tag{3.6}
\]

Thus (1\le b<q^2).  We claim that (b) of the perfect matchings in
(3.5) may be selected so that, for every two lines (L,R), the number
of selected matchings which send (L) to a point of (R) is at most

\[
 {2b\over q}.
\tag{3.7}
\]

If (R=L), this number is zero.  If (R\ne L), exactly (q) points of
(R) are nonincident with (L), and each occurs in exactly one factor
of (3.5) at (L).  A uniformly random (b)-subset of the (q^2)
factors therefore gives a hypergeometric variable of mean (b/q).
The usual sampling-without-replacement Chernoff bound gives failure
probability at most

\[
 \exp(-b/(3q))
\tag{3.8}
\]

for one ordered pair.  Whenever (b/q\gg\log q), the union bound over
fewer than (4q^4) ordered pairs proves the claim.  This is the only
regime used below.  For the finitely many remaining parameter values one
may replace the right side of (3.7) by its trivial value (b); none of
the asymptotic conclusions uses them.

For every tag (L), create the following (D) support edges.

* One **core edge** (P_L) with protected set (L\subseteq\mathcal P).
* For each of the selected (b) perfect matchings (M_i), one assigned
  filler (F_{L,i}) with protected set

  \[
   \{z_L,M_i(L)\}.
  \tag{3.9}
  \]

* (D-1-b) further labelled fillers, each with protected set
  \({z_L}\).

Give every support edge weight (1/D).

Every tag has total weight one.  A projective point (p) belongs to
exactly (k) core lines.  Every selected perfect matching uses (p)
once, so (p) belongs to exactly (b) assigned fillers.  Therefore

\[
 \ell(p)={k+b\over D}={1\over2}.
\tag{3.10}
\]

The private target (z_L) belongs to all (D-1) fillers at its tag, so

\[
 \ell(z_L)={D-1\over D}\in[1/2,1].
\tag{3.11}
\]

Two core edges meet in their unique projective-plane point.  Two fillers
on different tags can meet only in their assigned projective point; two
fillers on one tag meet only in (z_L).  A core edge (P_L) is disjoint
from every assigned filler on its own tag because all assignments use
nonincidences, and it meets a filler on another tag in at most the
filler's assigned point.  Thus every intersection has size at most one.

The same description proves the two-target codegree assertion.  A pair
of projective points lies on one core line; a pair ({z_L,p}) occurs
in at most one assigned filler because the factors in (3.5) partition
the edges of the nonincidence graph; all other target pairs occur in no
support edge.

We next prove (3.3).  There are two target types.

* Let (v=p\in\mathcal P).  If (E=P_R) is a core line not through
  (p), the only members of (Gamma_p(E)) are the (k) core lines
  through (p), so their mass is (k/D).  If (E) is a filler not
  containing (p), at most one core line through (p) meets its
  assigned point, and at most one filler containing (p) shares the
  private target of (E).  Its mass is therefore at most (2/D).
* Let (v=z_L).  A core edge (P_R) meets precisely those fillers at
  (L) whose assigned point lies on (R).  By (3.7), their mass is at
  most (2b/(qD)\le1/q).  A filler on another tag meets at most one
  filler at (L), giving mass at most (1/D).  A filler on tag (L)
  contains (z_L) and is excluded by the hypothesis on (E).

This proves (3.3).

The core family

\[
 \mathcal F=\{P_L:L\in\mathcal L\}
\tag{3.12}
\]

is pairwise intersecting.  In the point-specific fractional-colouring
dual, take (y_P=1) on (mathcal F) and zero elsewhere.  Its numerator
is (n/D), while every matching has supported weight at most one.  This
proves the first inequality in (3.4).  After denominator clearing, the
same (n) core occurrence edges form a clique, proving the second.

Finally, (D-1-b=D/2+k-1>0).  Choose one unassigned filler at every tag.
Its protected set is ({z_L}), and these targets are different for
different tags.  The chosen edges form a matching meeting all (n)
tags.  This proves the theorem. \(\square\)

## 4. Corrected asymptotics

For every large (m), choose a power of two (q) with

\[
 {m\over2}<q\le m
\tag{4.1}
\]

and an even integer

\[
 D=m^{11/6-o(1)}.
\tag{4.2}
\]

Then (2(q+1)<D<q^2+q+1), and (b/q=m^{5/6-o(1)}\gg\log m), so the
discrepancy selection in Theorem 3.1 applies.  Moreover

\[
 {n\over D}=m^{1/6+o(1)},
\tag{4.3}
\]

while

\[
 \zeta
 =O\left({m\over m^{11/6-o(1)}}+{1\over m}\right)
 =m^{-5/6+o(1)}
 =o(m^{-1/2+o(1)}).
\tag{4.4}
\]

Thus the construction obeys a one-star inequality strictly stronger than
the current protected-strip estimate.  Its maximum atom and normalized
two-target codegree are respectively

\[
 \|x\|_\infty={1\over D}=m^{-11/6+o(1)},
 \qquad
 \Delta_2^x\le {1\over D}=m^{-11/6+o(1)}.
\tag{4.5}
\]

All centered nonlinear intersection moments vanish identically, because
distinct supports intersect in zero or one target.  Target degrees after
clearing are exactly (D/2) on projective targets and (D-1) on private
targets.  There are no exceptional tags or targets and (eta=0).

Disjoint replication gives the same obstruction on any multiple of
(n) tags without changing (4.3)--(4.5).  Since (k=q+1=m^{1+o(1)}),
the rank is in the intended growing-(K) range.

## 5. Exact boundary after the singleton cut

Theorem 3.1 proves that the following implication is false, even with
the corrected scale and with no exceptional ledger:

\[
\begin{gathered}
 d(\text{tag})=D,\quad D/2\le d(\text{target})\le D,\quad
 |C(E)\cap C(F)|\le1,\\
 \Delta_2\le1,\quad \|x\|_\infty=1/D,\quad
 \sup_{v\notin C(E)}x(\Gamma_v(E))
      =o(m^{-1/2+o(1)})
\end{gathered}
\]

\[
 \not\Longrightarrow\qquad
 \chi_f'(x)\le1+o(1/Q).
\tag{5.1}
\]

In particular, neither a heat-bath argument based only on these local
loads nor an entropy-compression theorem based only on width and the
centered moment can prove the desired decomposition.

For the actual Boolean-geodesic point, the exact full-colouring gate is

\[
 \sum_e x_ey_e
 \le\bigl(1+o(1/Q)\bigr)
       \max_{M\text{ matching}}\sum_{e\in M}y_e
 \qquad(y\ge0).
\tag{5.2}
\]

Already on singleton-intersecting subfamilies it requires

\[
 x(\mathcal F)\le1+o(1/Q)
\tag{5.3}
\]

for every pairwise-intersecting (mathcal F) with no common target.
The one-star theorem does not imply (5.3) after the corrected retuning:
it permits (K^2) lines, each of mass (1/D), whose total mass is
(K^2/D=m^{1/6+o(1)}).

Condition (5.3) is necessary but not sufficient for (5.2), since general
weighted matching-polytope facets need not be cliques.  Thus the exact
remaining structural theorem is (5.2), or a chronology-specific
substitute strong enough to imply it.  If one only seeks coefficient one,
Theorem 3.1 also shows why it may be preferable to bypass (5.2): a direct
near-perfect matching can exist even when full fractional colouring is
off by an unbounded factor.

