# Audit of isolated-pruning fractional overload, and the exact rounding gate

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The abstract theorem in
`ISOLATED_PRUNING_FRACTIONAL_OVERLOAD_THEOREM_20260725.md` is correct.
In particular, the random isolated pruning contains strictly more
information than the weighted lower-fibre conclusion of the earlier
balanced-pruning lemma: after normalizing separately in every surviving
tag fibre, its aggregate denominator deviations give a tag-saturating
fractional point of total capacity-one overload (o(W)).

There is one error in the geodesic application, but it does not invalidate
the conclusion.  The sentence saying that every integer floor leaves less
than (T) uncovered targets is false at a shallow **capped** row, where

\[
 c_q^{(g)}=g<\left\lfloor {R_q\over T}\right\rfloor.
\]

The correct capped-row ledger is

\[
 \sum_{q:\,c_q^{(g)}=g}(R_q-gT)
 =O\left({WH^{3/2}\over m}\right)=o(W).
\]

Together with the noncapped floor loss (O(QT)=o(W)), the already proved
deadline-enlargement loss (o(W)), and the middle remainder (W-gT=o(W)),
this repairs the underload paragraph exactly.

The Bernoulli argument admits a useful strengthening.  After discarding
only (o(T)) tags, all target loads can be made at most (1+o(1))
**pointwise**, not merely in aggregate.  Scaling then gives a genuine
fractional matching in the tag--target hypergraph of total mass
((1-o(1))T).

This does not by itself give the required integral family.  The remaining
problem is a partitioned maximum-coverage/integral-matching problem.  The
width-two pair-intersection census controls repeated intersections of a
fixed pair of paths, but is blind to a projective-plane type family in
which every pair meets in one different target.  Thus a new transversal
expansion or hereditary aligned-rounding theorem is still required.

## 1. Abstract theorem: line-by-line verification

There are (T) tags, (A) candidates over every tag, (K) claims per
candidate, target universe (V), target degrees (d_v\le A), and a bad
graph of maximum degree \(\Delta\).  Put

\[
 p={1\over L(\Delta+1)},\qquad \mu=pA.
\]

Mark candidates independently with probability (p), and retain a
marked candidate if it has no marked bad neighbour.  For a tag (U),
write

\[
 Y_U=\#\{\hbox{marked candidates over }U\},\qquad
 Z_U=\#\{\hbox{marked candidates over }U\hbox{ deleted}\},
\]

and (A'_U=Y_U-Z_U).

### 1.1 Tag deviations

Exactly,

\[
 Y_U\sim\operatorname{Bin}(A,p),\qquad \mathbb EY_U=\mu.
\]

For one candidate (P), the probability that (P) is marked and at
least one bad neighbour is marked is at most

\[
 p\deg_B(P)p\le p^2\Delta.
\]

Consequently

\[
 \mathbb EZ_U\le Ap^2\Delta
 =\mu p\Delta\le {\mu\over L}.
\]

If (A'_U<\mu/2), then either (Y_U<3\mu/4) or
(Z_U>\mu/4).  Chernoff and Markov therefore give

\[
 \Pr(A'_U<\mu/2)
 \le e^{-\mu/32}+{4\over L}.
\]

Also

\[
 \mathbb E|A'_U-\mu|
 \le \mathbb E|Y_U-\mu|+\mathbb EZ_U
 \le \sqrt\mu+{\mu\over L}.
\]

No independence between (Y_U) and (Z_U) is used here.

### 1.2 Target deviation and denominator identity

Let (Y_v) count all marked candidates claiming (v).  Since markings
are independent,

\[
 Y_v\sim\operatorname{Bin}(d_v,p).
\]

Let (n_{Uv}) count retained candidates over a good tag (U) which
claim (v), and put (n_v=\sum_U n_{Uv}).  Deletion and removal of bad
tags only decrease counts, so (n_v\le Y_v).

With the fibre-uniform weights (x_P=1/A'_U),

\[
\begin{aligned}
 \ell(v)
 &=\sum_U{n_{Uv}\over A'_U}\\
 &\le {n_v\over\mu}
  +\sum_U n_{Uv}\left|{1\over A'_U}-{1\over\mu}\right|.
\end{aligned}
\]

The calibration gives

\[
 {pd_v\over\mu}={d_v\over A}\le1.
\]

It follows that

\[
 (\ell(v)-1)_+
 \le {(Y_v-pd_v)_+\over\mu}
 +\sum_U n_{Uv}\left|{1\over A'_U}-{1\over\mu}\right|.
\]

The first term has expectation at most (1/\sqrt\mu), since

\[
 \mathbb E(Y_v-pd_v)_+
 \le\mathbb E|Y_v-pd_v|
 \le\sqrt{pd_v}\le\sqrt\mu.
\]

For the second term, the exact fixed-claim identity is

\[
\begin{aligned}
 &\sum_v\sum_U n_{Uv}
 \left|{1\over A'_U}-{1\over\mu}\right|\\
 &=K\sum_U A'_U
 \left|{1\over A'_U}-{1\over\mu}\right|\\
 &={K\over\mu}\sum_U|A'_U-\mu|.
\end{aligned}
\]

Thus

\[
 \mathbb E\sum_v(\ell(v)-1)_+
 \le {|V|\over\sqrt\mu}
 +KT\left({1\over\sqrt\mu}+{1\over L}\right).
\]

Combining this random variable with the bad-tag count by the elementary
two-object averaging used in the note gives the displayed factor (2)
in both final bounds.  This part of the proof is valid.

## 2. Exact geodesic normalizations

For the length-(g) chunk catalogue, let (T) denote the tag count.
Every decorated path claims

\[
 K=g+2\sum_{q=1}^Q \widetilde c_q\le(2Q+1)g,
\]

where \(\widetilde c_q\le c_q^{(g)}\le g\) is the possibly
deadline-enlarged claim count.  Coordinate symmetry and double counting
give the exact normalized degrees

\[
 {d_X\over A}={Tg\over W}\le1
 \quad (X\hbox{ a middle owner}),
\]

and

\[
 {d_S\over A}={T\widetilde c_q\over R_q}\le1
 \quad (S\hbox{ in either signed depth-}q\hbox{ row}).
\]

The last inequality follows from

\[
 \widetilde c_q\le c_q^{(g)}
 =\min\left\{g,\left\lfloor{R_q\over T}\right\rfloor\right\}.
\]

The target and claim counts obey

\[
 |V|\le(2Q+1)W,
\]

and, more sharply than is needed,

\[
 KT=Tg+2T\sum_q\widetilde c_q
 \le W+2\sum_qR_q\le(2Q+1)W.
\]

For protected three-antichain pruning,

\[
 {\Delta+1\over A}=m^{-3+o(1)}.
\]

With (L=Q\log m),

\[
 \mu={A\over L(\Delta+1)}=m^{5/2-o(1)},
\]

and therefore

\[
 {|V|\over\sqrt\mu}
 +KT\left({1\over\sqrt\mu}+{1\over L}\right)
 =O\left(QW(\mu^{-1/2}+L^{-1})\right)=o(W).
\]

The number of discarded tags is (O(T/L)+o(T)), hence their middle
owner loss is

\[
 O(gT/L)+o(gT)=O(W/L)+o(W).
\]

Their signed claim loss is

\[
 O(KT/L)+o(KT)=O(QW/L)+o(W)=o(W).
\]

These normalizations are all correct.

## 3. Correction to the floor ledger

Put

\[
 c_q^{(g)}=\min\left\{g,\left\lfloor{R_q\over T}\right\rfloor\right\}.
\]

If the cap does not bind, then

\[
 0\le R_q-Tc_q^{(g)}<T.
\]

If the cap binds, this conclusion is false.  Instead,

\[
 0\le R_q-gT\le W-gT.
\]

The chunk construction gives

\[
 W-gT=O\left({W(H+g)\over m}\right)=O\left({WH\over m}\right).
\]

The cap can bind only when (R_q\ge gT).  The central-binomial estimate

\[
 W-R_q=\Theta\left({Wq^2\over m}\right)
\]

in the relevant range then forces (q=O(\sqrt H)).  Hence

\[
 \sum_{q:\,c_q^{(g)}=g}(R_q-gT)
 =O\left({WH^{3/2}\over m}\right)=o(W),
\]

because (H=(1+o(1))\sqrt{m\log m}).  At the noncapped rows,

\[
 \sum_q(R_q-Tc_q^{(g)})=O(QT)=O(QW/g)=o(W)
\]

because (Q=o(g)).  Finally the known deadline enlargement satisfies

\[
 2T\sum_q(c_q^{(g)}-\widetilde c_q)=o(W).
\]

These terms, together with (W-gT=o(W)), are the complete pre-pruning
scalar underload ledger.  For any row, the identity

\[
 \sum_v(1-\ell(v))_+-\sum_v(\ell(v)-1)_+
 =|V_q|-\sum_v\ell(v)
\]

then converts the (o(W)) overload theorem into (o(W)) total
underload as claimed.

## 4. Stronger pointwise fractional-matching theorem

The aggregate estimate is enough to close the weighted-cut dual.  The
same experiment gives a stronger conclusion useful for rounding.

### Theorem 4.1 (pointwise isolated-pruning fractional point)

In the abstract catalogue, assume

\[
 \log(T+|V|)=o(\mu),\qquad L\to\infty.
\]

Then there is an isolated pruning and a retained tag family
(\mathcal T'\) such that

\[
 T-|\mathcal T'|
 =O\left({T\over\sqrt L}\right),
\]

and the fibre-uniform weights satisfy

\[
 \ell(v)\le1+\varepsilon\qquad(v\in V),
\]

where

\[
 \varepsilon
 =O\left(\sqrt{{\log(T+|V|)\over\mu}}+{1\over\sqrt L}\right)=o(1).
\]

Consequently, (y_P=x_P/(1+\varepsilon)) is a feasible fractional
matching in the hypergraph whose vertices are the tags and targets and
whose edge (P) contains its tag and its (K) claims.  Its total mass is

\[
 \sum_Py_P={|\mathcal T'|\over1+\varepsilon}=(1-o(1))T.
\]

#### Proof

Put (S=T+|V|), and choose

\[
 \zeta=C\sqrt{{\log(4S)\over\mu}}
\]

with a sufficiently large absolute constant (C).  Standard binomial
Chernoff bounds and a union bound give, with probability (1-o(1)),

\[
 Y_U\ge(1-\zeta)\mu\quad(U\hbox{ any tag})
\]

and

\[
 Y_v\le pd_v+\zeta\mu\quad(v\in V).
\]

For the second inequality one uses (pd_v\le\mu); its upper-tail
exponent is \(\Omega(\zeta^2\mu)\).

Put \(\delta=L^{-1/2}\), and call a tag deletion-bad when
(Z_U>\delta\mu).  Since \(\mathbb EZ_U\le\mu/L\),

\[
 \mathbb E\#\{U:Z_U>\delta\mu\}
 \le {T\over L\delta}={T\over\sqrt L}.
\]

Markov's inequality with a fixed constant factor, intersected with the
simultaneous binomial event above, produces an outcome with
(O(T/\sqrt L)) deletion-bad tags.  Retain all other tags.  On a retained
tag,

\[
 A'_U=Y_U-Z_U\ge(1-\zeta-\delta)\mu.
\]

Therefore

\[
\begin{aligned}
 \ell(v)
 &=\sum_U{n_{Uv}\over A'_U}\\
 &\le {Y_v\over(1-\zeta-\delta)\mu}\\
 &\le {1+\zeta\over1-\zeta-\delta}
 =1+O(\zeta+\delta).
\end{aligned}
\]

Scaling proves the final assertion. \(\square\)

In the protected geodesic application,

\[
 \log(T+|V|)=O(m),\quad
 \mu=m^{5/2-o(1)},\quad
 L=Q\log m=m^{1/2+o(1)}.
\]

Thus

\[
 \varepsilon=m^{-1/4+o(1)},\qquad
 T-|\mathcal T'|=m^{-1/4+o(1)}T,
\]

and the retained tag--target hypergraph has a fractional matching of mass
((1-m^{-1/4+o(1)})T).

This last statement is a fractional-matching strengthening, not by itself
a literal coefficient-one conclusion.  The discarded fraction
(m^{-1/4+o(1)}) is (o(1)), so its middle-owner mass is (o(W)), but
literal repair of all its signed claims would multiply it by (Q).  The
exact colour/reserve tradeoff is recorded in
`RATIONAL_MULTICOVER_COLOR_REDUCTION_AND_BERGE_CUT_20260725.md`.

## 5. What integral rounding must prove

For an integral choice (P_U) from each retained tag, let

\[
 r_v=\#\{U:v\in C(P_U)\}.
\]

Its duplicate ledger is

\[
 \operatorname{Dup}(P_\bullet)
 =\sum_v(r_v-1)_+
 =K|\mathcal T'|-\left|\bigcup_U C(P_U)\right|.
\]

Thus the remaining task is exactly a partitioned maximum-coverage
rounding theorem:

\[
 \boxed{\text{choose one legal path per almost every tag with }
 \operatorname{Dup}=o(W).}
\]

Equivalently, it is enough to find a target-disjoint matching covering
((1-o(1))T) tags, because the omitted tags cost only (g\,o(T)=o(W))
middle owners.

Independent rounding does not suffice.  If (p_{Uv}) is the probability
that the selected path over tag (U) claims (v), then

\[
 \mathbb E\operatorname{Dup}
 =\sum_v\left(\ell(v)-1+\prod_U(1-p_{Uv})\right),
\]

which is of Poisson order when many loads are near one.  Pointwise
fractional feasibility alone therefore does not preserve the coefficient.

Nor does the width-two pair-intersection census, by itself, imply an
integral matching theorem.  It only penalizes intersections of size at
least two in its nonlinear overlap moment.  A projective plane already
shows the missing phenomenon: its lines have pairwise intersection one,
so every nonlinear width-two overlap moment vanishes, while the line
family is globally intersecting.  The geodesic catalogue has additional
ordered and inclusion structure, so this is not a counterexample to the
actual construction; it is a proof that the presently recorded abstract
hypotheses do not logically imply the desired rounding.

The exact new gate is therefore one of the following equivalent-strength
forms.

1. **Near-perfect transversal theorem.**  Prove that the isolated
   protected-strip catalogue contains a target-disjoint selection on
   ((1-o(1))T) tag fibres.
2. **Coefficient-safe coverage rounding.**  Round the point of Theorem
   4.1 to one path on almost every tag with duplicate ledger (o(W)).
3. **Hereditary aligned expansion.**  Prove a Hall/Aharoni--Haxell type
   expansion for every residual tag family, using the actual geodesic
   phase order, not merely pairwise width-two intersection counts.

At the fractional level, the horizontal path-start ratio remains
(1/g=o(1/Q)), exactly as in the earlier dual audit.  Hence the unresolved
horizontal cost is part of this same integral transversal theorem, not a
second fractional obstruction.
