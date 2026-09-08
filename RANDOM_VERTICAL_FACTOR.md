# Random vertical shadows: the exact benchmark and the conditioning barrier

This note isolates what randomness would have to prove after the middle layer
has been partitioned into geodesic blocks.  It has three conclusions.

1.  In the independent-wreath benchmark, the number of missed targets has an
    exact binomial mean and is sharply concentrated.  The threshold for an
    `o(W)` *total* repair over all deeper ranks is

    \[
      q_*^2/m=\log\log m-\log 2+o(1),
    \]

    whereas the threshold for literally missing no target in one rank is
    `q^2/m=log m+O(1)`.
2.  Conditioning the wreaths to partition the middle layer is not a harmless
    technicality.  Exactness, full coordinate symmetry, and even the correct
    mean target multiplicity do not imply the independent miss exponent.
3.  For the uniform exact-factor model, the missing statement is precisely a
    robust perfect-matching count.  A concrete switching inequality which
    would imply the desired exponent is given in Section 7.

The note treats odd dimension because a wreath has the cleanest formulation
there.  The same one-target calculation applies to any transitive family of
geodesic blocks: replace the wreath length `n` by the block length `R`.

## 1. Parameters and one random wreath

Put

\[
 n=2m+1,\qquad
 W=\binom{n}{m},\qquad
 B=\frac{W}{n},
\]

and, for `0<=q<m`, put

\[
 r=m-q,\qquad
 N_q=\binom{n}{r},\qquad
 \rho_q=\frac{N_q}{W},\qquad
 \mu_q=\frac1{\rho_q}=\frac{W}{N_q}.                 \tag{1.1}
\]

A uniformly random wreath is obtained from a uniformly random cyclic order of
`[n]`, modulo reversal.  Its depth-`q` lower shadows are the `n` cyclic
intervals of length `r`.  Consequently, for a fixed rank-`r` target `S`,

\[
 p_q:=\Pr(S\text{ occurs in one wreath})
      =\frac{n}{N_q}.                                  \tag{1.2}
\]

Take `B` independent uniformly random wreaths, with replacement.  This is only
the benchmark model; their middle layers do not form a partition.  If `X_S`
is the number of wreaths containing `S`, then

\[
 X_S\sim\operatorname{Bin}(B,p_q),\qquad
 \mathbb E X_S=Bp_q=\mu_q,                              \tag{1.3}
\]

and hence

\[
 \Pr(X_S=0)=(1-p_q)^B
 =\exp(-\mu_q+o(1))                                    \tag{1.4}
\]

uniformly whenever `q=o(m)` and `rho_q=exp(-o(m))`.  Indeed,

\[
 Bp_q^2=\frac{nW}{N_q^2}=\frac{n}{\rho_q^2W}=o(1).      \tag{1.5}
\]

The exact ratio

\[
 \rho_q=\prod_{j=0}^{q-1}\frac{m-j}{m+2+j}             \tag{1.6}
\]

gives, for `q=o(m^(2/3))`,

\[
 \log\mu_q=\frac{q(q+1)}m+O\!\left(\frac{q^3}{m^2}
                                      +\frac{q}{m^2}\right). \tag{1.7}
\]

Thus the natural occurrence mean is `exp(q^2/m+o(1))`.

## 2. Exact two-target probability in one wreath

The dependence between different target shadows can also be computed exactly.
Let `S,T` be distinct rank-`r` sets, put

\[
 c=|S\cap T|,\qquad a=r-c,\qquad d=n-r=m+q+1.
\]

Condition on `S` being a cyclic interval.  The elements of `S` occur in a
uniform linear order, followed by the elements of its complement in an
independent uniform linear order.  Therefore

\[
 \theta_c:=\Pr(T\text{ is an interval}\mid S\text{ is an interval})
 =
 \begin{cases}
 \displaystyle
 \frac{d-r+1}{\binom d r},&c=0,\\[8pt]
 \displaystyle
 \frac{2}{\binom r c\binom d{r-c}},&0<c<r.
 \end{cases}                                           \tag{2.1}
\]

Indeed, in the second case `T` must cross exactly one of the two boundaries of
the `S` block.  Its `c` elements in `S` must occupy the appropriate end of
that block and its `a` outside elements the adjacent end of the complement
block.  In the disjoint case, `T` must occupy one of the `d-r+1` linear
length-`r` intervals wholly inside the complement block.

It follows that

\[
 \Pr(S,T\text{ both occur in one wreath})=p_q\theta_c. \tag{2.2}
\]

For `1<=q<=H=o(m)`, uniformly over distinct `S,T`,

\[
 \boxed{\theta_c\le\frac{2+o(1)}{m^2}.}                \tag{2.3}
\]

For `0<c<r`, both nontrivial binomial coefficients in (2.1) are at least
`r` and `d`.  For `c=0`, use

\[
 \frac{2q+2}{\binom{m+q+1}{2q+1}}
 =O(H/m^3)=o(m^{-2}),                                  \tag{2.4}
\]

where `2q+1<(m+q+1)/2` for all sufficiently large `m`.

## 3. Concentration of the ideal missing count

Let `M_q` be the number of rank-`m-q` targets absent from all `B` independent
wreaths.  From (1.4),

\[
 \mathbb E M_q
 =N_q\exp(-\mu_q+o(1)).                                \tag{3.1}
\]

There is also a useful second-moment statement.

### Theorem 1 (ideal-model concentration)

Uniformly for `1<=q<=H=o(m)`, if `mu_q=o(m^2)` and the right side of (3.1)
tends to infinity, then

\[
 \frac{M_q}{\mathbb E M_q}\longrightarrow1
 \qquad\text{in probability}.                          \tag{3.2}
\]

More quantitatively,

\[
 \frac{\operatorname{Var}M_q}{(\mathbb E M_q)^2}
 \le \frac{1+o(1)}{\mathbb E M_q}
       +O\!\left(\frac{\mu_q}{m^2}\right).             \tag{3.3}
\]

### Proof

Write `I_S=1_(X_S=0)` and `a_q=(1-p_q)^B`.  For distinct `S,T`, (2.2) gives

\[
 \mathbb E(I_SI_T)=(1-2p_q+p_q\theta_c)^B.             \tag{3.4}
\]

Using (1.5) and (2.3),

\[
 \log\frac{\mathbb E(I_SI_T)}{a_q^2}
 \le Bp_q\theta_c+O(Bp_q^2)
 =O(\mu_q/m^2)+o(1).                                   \tag{3.5}
\]

Summing the diagonal variances and the upper bound (3.5) for all ordered
distinct pairs proves (3.3).  Chebyshev proves (3.2).  QED.

This calculation is stronger than a heuristic Poisson statement: throughout
the useful band, the ideal number of absent targets is itself sharply
predictable.

## 4. Two different thresholds

The distinction between `o(W)` repair and literal complete coverage is
important.

### 4.1 The threshold for no missing target in one rank

The union bound and (1.4) show that every target at depth `q` is covered with
probability tending to one if

\[
 \mu_q-\log N_q\longrightarrow+\infty.                 \tag{4.1}
\]

Conversely, if

\[
 \mu_q\le(1-\varepsilon)\log N_q,                       \tag{4.2}
\]

then (3.1)--(3.3) imply that a target is missing with probability tending to
one.  Since `log N_q=(log 4+o(1))m` in the relevant range, the sharp first
order location is

\[
 \boxed{q^2/m=\log m+\log\log4+o(1).}                  \tag{4.3}
\]

Thus a claim that *every* deeper central target appears already at
`sqrt(m log log m)` is false even in the independent ideal model.

### 4.2 The threshold for `o(W)` total repair

For the OR application it is enough that the sum of all missing targets be
`o(W)`, since they may then be appended literally.  By (3.1), the normalized
expected contribution at depth `q` is

\[
 \frac{\mathbb E M_q}{W}
 =\rho_qe^{-1/\rho_q+o(1)}
 =\frac{e^{-\mu_q+o(1)}}{\mu_q}.                       \tag{4.4}
\]

Let `H=sqrt(m omega_m)`, where `omega_m=o(log m)` and `H>=q_0`; for the
eventual split one may take `omega_m/log log m->infinity`.  Let `q_0` be such
that `mu_(q_0)=mu_0`.  Since

\[
 \log\frac{\mu_{q+1}}{\mu_q}
 =\frac{2q+2}{m}+O(q^2/m^2),                            \tag{4.5}
\]

comparison with an integral gives

\[
 \sum_{q=q_0}^{H}\frac{\mathbb E M_q}{W}
 \le (1+o(1))\frac{m}{2q_0}
          \frac{e^{-\mu_0}}{\mu_0^2}
       +\frac{e^{-\mu_0}}{\mu_0}.                      \tag{4.6}
\]

Consequently the whole outer part of the central band has `o(W)` omissions,
for example, as soon as

\[
 \mu_0\ge(1/2+\varepsilon)\log m.                       \tag{4.7}
\]

Markov then gives one realization with `o(W)` total repair.

The actual one-sided transition window follows by taking logarithms in (4.6).
Define

\[
 \mu_c=\frac12\log m-2\log\log m
       -\frac12\log\log\log m+\log2+o(1).              \tag{4.8}
\]

Then the main term in (4.6) is `exp(-(mu_0-mu_c)+o(1))`.  For both the lower
and complementary upper layers, (4.6) is multiplied by two, so the corresponding
critical value has `2 log 2` in place of the final `log 2` in (4.8).  Thus
`mu_0-mu_c->+infinity` makes the expected total `o(W)`.  If
`mu_0-mu_c->-infinity`, restrict to the successive depths for which
`mu_q in [mu_0,mu_0+1]`.  The reverse integral comparison and the simultaneous
concentration (3.3) show that their total omissions divided by `W` tend to
infinity in probability.  Hence `mu_c` is the sharp ideal-model transition
window up to an additive `O(1)` in `mu`.

In particular, the leading constant can also be stated more simply: if

\[
 \mu_0\le(1/2-\varepsilon)\log m,                       \tag{4.9}
\]

take `Theta(m/q_0)` successive depths for which `mu_q` remains within a fixed
factor of `mu_0`.  Equations (3.2)--(3.3), simultaneously over these depths,
show with probability tending to one that their total omissions are not
`o(W)`.  The union of the Chebyshev failure probabilities is `o(1)` because
there are only `O(H)` depths and `mu_H=m^{o(1)}`.

Combining (1.7)--(4.9), the ideal structured/random transition is

\[
 \boxed{
 q_*^2/m=\log\log m-\log2+o(1).
 }                                                        \tag{4.10}
\]

In particular `q_*=(1+o(1))sqrt(m log log m)`, but (4.10) records the sharper
constant hidden in the earlier `Theta` statement.

## 5. What exact-factor symmetry does prove

Let `mathcal H_m` be the wreath hypergraph on the middle layer and let
`mathscr F_m` be any coordinate-permutation-invariant probability distribution
on its exact factors.  For a rank-`m-q` target `S`, let `X_S(F)` count the
wreaths of `F` whose depth-`q` shadow contains `S`.

Every factor has exactly `Bn=W` depth-`q` slots.  Coordinate transitivity
therefore gives the exact identity

\[
 \boxed{\mathbb E_{F\sim\mathscr F_m}X_S(F)=W/N_q=\mu_q.} \tag{5.1}
\]

This is all that symmetry alone gives.  It supplies no useful upper bound on
`Pr(X_S=0)`, because the positive multiplicities can be arbitrarily
heavy-tailed.

For the uniform distribution on all exact wreath factors, write
`PM(mathcal H_m)` for their number and let `mathcal H_m(S,q)` be the family of
wreaths whose depth-`q` shadow contains `S`.  Then exactly

\[
 \Pr(X_S=0)
 =\frac{PM(mathcal H_m\setminus\mathcal H_m(S,q))}
        {PM(mathcal H_m)}.                                  \tag{5.2}
\]

Thus transferring (1.4) to exact factors is the robust counting assertion

\[
 \log PM(mathcal H_m\setminus\mathcal H_m(S,q))
 -\log PM(mathcal H_m)
 \le-(1-o(1))\mu_q.                                      \tag{5.3}
\]

Neither existence of one factor nor ordinary degree/codegree estimates prove
(5.3).

## 6. A sharp symmetric obstruction

There is an explicit reason not to treat (5.3) as an automatic consequence of
conditioning.

Tile every sufficiently split orientation cube of one fixed perfect matching
of the `2m` coordinates with geodesic pair-flip cycles, and retain the
exceptional `o(W)` middle vertices as singleton blocks.  This is an exact
partition of the middle layer; it has `W-o(W)` geodesic depth-`q` slots in the
range below.  Randomly relabel all coordinates by one uniform permutation.  The
resulting distribution has all of the following properties:

* it is fully `Sym(2m)`-invariant;
* every realization partitions the middle layer exactly;
* every nontrivial depth-`q` block window is geodesic for `q<ell`; and
* the even-dimensional analogue of (5.1) holds up to a `1+o(1)` factor.

Nevertheless, if

\[
 q/\sqrt m\longrightarrow\infty,qquad
 q=o(ell),\qquad ell=o(m),                               \tag{6.1}
\]

then a fixed rank-`m-q` target is missed with probability `1-o(1)`.

Here is the short calculation.  Relative to the coordinate matching, a
typical target has

\[
 f=\frac{(m-q)^2}{4m}+O_p(\sqrt m)                       \tag{6.2}
\]

full pairs.  The total physical depth-`q` capacity available per target of
this type is at most

\[
 \lambda_{f,q}
 =\frac{2^q\binom{f+q}{q}}{\binom{m-2f}{q}},             \tag{6.3}
\]

and uniformly in the typical window,

\[
 \log\lambda_{f,q}=-(1+o(1))q^2/m.                      \tag{6.4}
\]

Thus `lambda_(f,q)=o(1)` on a family containing `1-o(1)` of the targets.
Even an optimal tiling can cover only a `lambda_(f,q)` fraction of that type,
so the missing fraction is `1-o(1)`.  Random global relabelling turns this
missing fraction into the miss probability of every fixed target.

At the same time, slot counting says that the mean multiplicity is
`(1-o(1))mu_q=exp((1+o(1))q^2/m)`, where here
`mu_q=binom(2m,m)/binom(2m,m-q)`.  Hence this invariant exact-partition
distribution has

\[
 \Pr(X_S=0)=1-o(1),\qquad \mathbb E X_S\to\infty.        \tag{6.5}
\]

The mean is carried by an extremely small favourable-type tail.  By
Cauchy--Schwarz,

\[
 \frac{\mathbb E X_S^2}{(\mathbb E X_S)^2}
 \ge\frac1{\Pr(X_S>0)}\longrightarrow\infty.            \tag{6.6}
\]

This proves a precise obstruction:

> Exact middle coverage, coordinate symmetry, and the correct normalized
> target degree do not even imply bounded relative second moment, let alone
> the Poisson miss exponent.

Different coordinate architectures must be mixed *inside* the selected
factor; randomizing one complete factor by a global automorphism cannot work.

## 7. An exact switching target for uniform wreath factors

There is a structural warning before setting up the switching count.  Given an
exact wreath factor `F`, define its **interaction multigraph** `Gamma_F` as
follows.  Its vertices are the `B` wreaths of `F`; for every odd-graph edge
whose endpoints lie in two different wreaths, insert an edge between the
corresponding vertices of `Gamma_F`.

### Lemma 2 (trade-support obstruction)

The interaction multigraph is exactly `n(m-1)`-regular.  Moreover, if a
nonempty family `Q` of old wreaths can be replaced by a different family of
wreaths on exactly the same middle vertices, then `Gamma_F[Q]` contains a
cycle, where two parallel edges count as a cycle of length two.

### Proof

Every middle vertex has `m+1` odd-graph neighbours.  Exactly two are its
neighbours in its own wreath, so every old wreath has `n(m-1)` external edge
ends.

The subgraph of the odd graph induced by the vertices of one wreath is exactly
its `C_n`: two length-`m` cyclic intervals are disjoint only at the two
minimum-cycle offsets.  Hence a new wreath wholly inside one old block is the
old wreath itself.  Any genuinely new wreath must cross between old blocks.
Contract its maximal segments inside the old blocks.  Its cross edges become
a closed trail in `Gamma_F[Q]`.  A closed trail using at least one edge
contains a multigraph cycle.  QED.

Thus constant-size factor trades are not automatic.  They exist only near
short cycles of `Gamma_F`.  If `Gamma_F` is simple, the Moore bound guarantees
only

\[
 \operatorname{girth}(\Gamma_F)
 =O\!\left(\frac{\log B}{\log(m^2)}\right)
 =O(m/\log m),                                          \tag{7.1}
\]

and even an interaction cycle is only a necessary, not sufficient, condition
for a wreath trade.  A successful switching proof may therefore require
mesoscopic trades, or it may first cut wreaths into long geodesic paths so
that exact `C_n` component lengths no longer have to be preserved.

The ratio (5.2) nevertheless suggests a clean counting target.  Put

\[
 \mathscr F_j(S,q)=\{F:X_S(F)=j\}.
\]

Suppose one defines factor-preserving trades and can prove that, for
`0<=j<=J`, every factor in `mathscr F_j` has at least `A_j` directed trades
to `mathscr F_(j+1)`, while every factor in `mathscr F_(j+1)` has at most
`B_(j+1)` reverse trades, with

\[
 \frac{A_j}{B_{j+1}}
 \ge(1-o(1))\frac{\mu_q}{j+1}.                         \tag{7.2}
\]

Double counting the directed trades gives

\[
 \frac{|\mathscr F_{j+1}|}{|\mathscr F_j|}
 \ge(1-o(1))\frac{\mu_q}{j+1}.                         \tag{7.3}
\]

If (7.3) holds through `J=(1+o(1))mu_q` with uniform accumulated error
`o(mu_q)`, then

\[
 \frac{|\mathscr F_0|}{|\mathscr F_m|}
 \le\left(\sum_{j=0}^{J}\frac{((1-o(1))\mu_q)^j}{j!}
     \right)^{-1}
 \le\exp(-(1-o(1))\mu_q).                              \tag{7.4}
\]

This is exactly the miss estimate required by Section 4.  It is substantially
weaker than proving that a switch chain mixes in total variation: only the
one-dimensional count `X_S` must have the correct upward/downward switching
ratios.

The unresolved combinatorial task is therefore:

> Construct controlled-complexity trades among exact wreaths (or among long
> geodesic path blocks after cutting the wreaths) which insert one prescribed
> depth-`q` interval shadow and satisfy (7.2), uniformly for
> `q>=q_*`.

The fixed-pair obstruction shows that the trades must change coordinate
pairing/type architecture, not merely rotate, reverse, or relabel blocks
inside one architecture.

## 8. Consequence for the global program

The mathematically correct multiscale split is now:

1. resolve all depths `q<q_*` by a structured two-sided construction;
2. prove the switching/counting estimate (7.4) for `q_*<=q<=H`;
3. append the resulting `o(W)` missed masks;
4. use the width-order tail construction outside the central band.

Here

\[
 q_*^2/m=\log\log m-\log2+o(1),\qquad
 H=\sqrt{m\,\omega_m},\quad
 \log\log m\ll\omega_m\ll\log m
\]

with `omega_m=o(log m)` chosen slowly.  The outer random stage is therefore
quantitatively much shallower than the literal-tail scale
`sqrt(m log m)`, but it is not automatic under exact-factor conditioning.
The missing theorem is the robust factor-count (5.3), for which (7.2) is an
explicit local-switching route.

## 9. Comparison with the collision-energy target

There are two inequivalent notions of collision energy.  This distinction is
essential for deciding where random switching can help.

For one sign and depth, write `d_S=X_S(F)` and define

\[
 C_q=\sum_S\binom{d_S}{2},\qquad
 D_q=\sum_S(d_S-1)_+.                                  \tag{9.1}
\]

The quadratic energy `C_q` penalizes every pair of occurrences.  The linear
duplicate energy `D_q` only records how many slots remain after retaining one
copy of every covered target.  Since there are `W` slots,

\[
 \boxed{D_q-(W-N_q)=M_q.}                              \tag{9.2}
\]

Thus (9.2), not quadratic collision energy, is the exact objective for the OR
problem.

The stronger quadratic target becomes arithmetically impossible at deeper
ranks.  If `W=aN_q+b`, where `a=floor(mu_q)` and `0<=b<N_q`, convexity shows
that the least possible value of `C_q` is

\[
 C_q^{\min}=N_q\binom a2+ab.                            \tag{9.3}
\]

Consequently

\[
 C_q^{\min}-(W-N_q)
 =N_q\frac{(a-1)(a-2)}2+b(a-1).                        \tag{9.4}
\]

When `mu_q->infinity`, (9.4) is `(1/2+o(1))W mu_q`, not `o(W)`.
In particular, a requirement of the form

\[
 \sum_{q\le H}\bigl(C_q-(W-N_q)\bigr)=o(W)             \tag{9.5}
\]

cannot hold for a band with `H^2/m->infinity`.  This corrects the previously
suggested all-depth low-pair-collision target: it over-penalizes unavoidable
triple and higher multiplicities.

The independent-wreath benchmark makes the same point probabilistically.  A
pair of independent wreaths has expected depth-`q` shadow intersection
`n^2/N_q`, so

\[
 \mathbb E C_q
 =\binom B2\frac{n^2}{N_q}
 =(1+o(1))\frac{W\mu_q}{2}.                            \tag{9.6}
\]

This energy is huge in the outer band even though Sections 3--4 show that its
missing count is small enough to repair.

At depth one the situation is the opposite.  Here

\[
 \mu_1=\frac{m+2}{m}=1+O(1/m).                         \tag{9.7}
\]

The ideal random factor misses `(e^{-1}+o(1))N_1=Theta(W)` targets, while the
arithmetic minimum quadratic excess is only `O(W/m)`.  Therefore `q=1` (and,
more generally, every `q=o(sqrt m)`) must be handled by a deliberately
near-rainbow, two-sided design.  No switching theorem whose conclusion is
merely Poisson-like can solve that range: its occurrence mean stays bounded.

The correct strategic division is consequently:

* **shallow depths:** construct near-rainbow shadows, measuring actual
  missing colours or the exact linear energy (9.2);
* **outer central depths:** allow the unavoidable high multiplicities and use
  the exact-factor switching ratio (7.2) only to prove the exponential miss
  bound;
* **never require** quadratic collision excess `o(W)` across a band in which
  `mu_q` diverges.

So a switching proof for a uniformly random exact wreath factor is plausible
and sufficient only for `q>=q_*`.  It is not a replacement for the structured
shallow construction; it is the complementary outer stage.
