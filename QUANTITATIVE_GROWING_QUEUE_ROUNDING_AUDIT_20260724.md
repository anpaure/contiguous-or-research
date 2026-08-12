# Audit of quantitative growing-depth queue rounding

## Verdict

The growing-depth queue theorem is valid.  Its parameters give

\[
h=\left\lfloor\sqrt{\frac{\log m}
 {\log\log m\,\omega(m)}}\right\rfloor,
\qquad
H=\left\lfloor\frac14\sqrt{\frac{\log m\,\omega(m)}
 {\log\log m}}\right\rfloor,
\]

with `omega->infinity` and
`omega=o(log m/log log m)`.  A zero-collision atom matching leaves
`W(log m)^(-1/2+o(1))=o(W)` real band masks uncovered, and the literal queue
word has length

\[
W+(8+o(1))W/\omega+W(\log m)^{-1/2+o(1)}.
\]

The original presentation left one issue to resolve: Poisson sampling
creates parallel indexed edge occurrences, whereas the cited theorem is
stated for an ordinary hypergraph family.  There are now two complete
repairs.  Section 4 gives a direct Bernoulli sampling of distinct supports.
Section 5 records the independently supplied label-lift and
collision-cleaning argument, which also produces an ordinary no-parallel-edge
hypergraph and does not need the support-probability bound from Section 4.

This result is quantitatively new for the **queue matching** route, but it
does not improve the largest unconditional OR-covered depth: the independent
cyclic-strip cover already reaches any `J=o(sqrt(log m))`, which is much
larger than the displayed queue depth.

The later full proof with the random-label lift is now certified as a
complete proof of this partial theorem.  In particular, it no longer relies
on interpreting the ABKV theorem for a Poisson multihypergraph: Section 5
below produces an ordinary no-parallel-edge hypergraph before Theorem 3.9 is
applied.
Two harmless prose clarifications remain important when the proof is quoted:

1. two dummy vertices in one signed row are sampled without replacement, so
   their conditional joint probability is
   `b_q(b_q-1)/(R_q(R_q-1))`;
2. the uniform Poisson pair tail at threshold `2*mu_*` is obtained by
   stochastic domination from the actual mean `lambda<=mu_*`.

Neither clarification changes a bound or conclusion.

## 1. Atom, dummy, and fractional-cover audit

The exact queue invariant remains valid while `h,H` grow because
`H+h<=m`.  Every atom exposes the distinct masks

\[
B_{t,s}=\{z_{t-s},\ldots,z_{t+m-1}\},
\qquad |s|\le d_t,\quad 0\le t<H,
\]

and has literal word length at most `H+2h+1`.

With

\[
a_q=\lfloor HN_q/W+U\rfloor,
\]

the dummy-completed augmented edge has fixed size

\[
K=H(2h+1)
\]

on `(2h+1)W` vertices.  Every real or dummy augmented vertex has inclusion
probability exactly `H/W`; hence

\[
x_e=(W/H)\Pr(E=e)
\]

is an exact fractional perfect matching of total mass `W/H`.

The dummy injections are mutually independent between all signed rank rows
and uniform without replacement within each row.  The middle row `q=0` has
no dummy class.  These conventions are needed for the dummy--dummy codegree
bound.  In particular, two distinct dummy vertices in the same signed row
have conditional joint-use probability

\[
\frac{b_q(b_q-1)}{R_q(R_q-1)},
\]

not a product of independent probabilities; this is still bounded by the
displayed `H^2/[R_1(R_1-1)]` estimate.  Capacity is exact: if `R_q=W-N_q`, then

\[
H-a_q\le \lceil HR_q/W\rceil\le R_q.
\]

The growing-parameter weighted codegree calculation is uniform:

\[
\alpha(x)=\max_{u\ne v}\sum_{e\supseteq\{u,v\}}x_e
 \le \frac{H}{m-h}.
\tag{1.1}
\]

For two real masks, conditional permutation counting gives the reciprocal
of a product of two binomial coefficients.  A denominator-one complement
case would require complementary active position intervals, impossible
because every active interval omits the final queue position.  Real-dummy
and dummy-dummy codegrees are exponentially smaller, using
`R_1=W/(m+1)`.

## 2. Parameter audit

Write

\[
L=\log m,\qquad \ell=\log L.
\]

Then

\[
hH=(1/4+o(1))L/\ell,
\qquad H/h=(1/4+o(1))\omega,
\]

and

\[
K=H(2h+1)=(1/2+o(1))L/\ell.
\tag{2.1}
\]

Thus reset cost is `(2h+1)/H=(8+o(1))/omega=o(1)`, while the matching
uniformity is small enough for the quantitative ABKV exponent.

The phrase “uniform over all functions omega satisfying the limits” should
be read pointwise, or uniformly on a quantitative window
`omega_min(m)<=omega<=omega_max(m)` with
`omega_min->infinity` and `omega_max=o(L/ell)`.  A literal uniform threshold
over every arbitrarily slowly converging function is not meaningful.

## 3. Near-regular sparsification and ABKV matching

Take `Lambda=m^8`.  A sparsification with expected edge multiplicity
`Lambda x_e` has expected vertex degree `Lambda` and expected pair degree at
most

\[
\mu_*\le \Lambda H/(m-h).
\]

Chernoff bounds and union bounds over at most `exp(2m)` vertices and
`exp(4m)` pairs give a realization with

\[
\Lambda-4\sqrt{\Lambda m}\le d(v)\le
\Lambda+4\sqrt{\Lambda m},
\]

and maximum codegree `C<=2mu_*+1`.

For clarity, a fixed pair may have Poisson mean `lambda<mu_*`.  The uniform
tail estimate at threshold `2mu_*` uses stochastic domination
`Pois(lambda) <=_st Pois(mu_*)`, followed by the usual upper-tail bound for
`Pois(mu_*)`.  One should not apply a displayed `2lambda` Chernoff inequality
directly and then silently replace its exponent by `mu_*`.

Put `D=Lambda+O(sqrt(Lambda m))`.  The degree spread is
`o((D^2 C log D)^(1/3))`.  Moreover

\[
\log\frac{e^{2K}C\log D}{D}
=-L+O(L/\ell)+O(\ell)\to-\infty.
\]

The auxiliary size condition used in the ABKV setup also holds explicitly:

\[
\frac{f(D)}D
=20\left(\frac{C\log D}{D}\right)^{1/3}
=O\!\left(\left(\frac{H\log m}{m}\right)^{1/3}\right)
=o(1),
\]

so in particular `f(D)<=D/10` for all sufficiently large `m`.

The near-regular form of
[Alon--Bollobas--Kim--Vu, *Economical covers with geometric applications*]
(https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf), Theorem 3.9, gives a
matching whose uncovered augmented-vertex fraction is

\[
O\!\left(
K(C\log(1+C)/D)^{1/(K-1)}
\right)
=(\log m)^{-1+o(1)}.
\]

Since the augmented universe has
`(2h+1)W<=W(log m)^(1/2+o(1))` vertices,
the absolute uncovered count is

\[
W(\log m)^{-1/2+o(1)}=o(W).
\tag{3.1}
\]

This is the crucial quantitative gain over a fixed-uniformity nibble.

## 4. A simple-hypergraph Bernoulli repair

The Poisson multihypergraph can be replaced by a simple random subhypergraph.
An augmented edge determines its unordered family of `H` middle queue
windows.  Conditional on the first middle set, there are

\[
(m)_{H-1}^2
\]

ordered geodesic queue paths: choose the ordered leaving and entering
coordinates.  One unordered path has at most two orientations.  Therefore

\[
\Pr(E=e)\le \frac{2}{W(m)_{H-1}^2},
\qquad
x_e\le \frac{2}{H(m)_{H-1}^2}.
\tag{4.1}
\]

As `H->infinity` and `H=o(m)`, (4.1) gives

\[
\max_e \Lambda x_e=o(1).
\]

Select each distinct augmented support edge independently with probability
`Lambda x_e` instead of using a Poisson number of copies.  Vertex degrees
and pair codegrees are now sums of independent Bernoulli variables with the
same means as above, so the same Chernoff and union bounds apply.  The
resulting hypergraph is simple, and ABKV applies exactly as stated.  This
removes any convention about labelled parallel edges.

## 5. Alternative exact conversion to a simple hypergraph by a random label lift

The full Poisson occurrence proof can also be converted to a simple
hypergraph without changing its degree scale.  Let

\[
s=\frac{(2h+1)W}{H(2h+1)}=\frac WH,
\qquad J=\lfloor s\rfloor,
\]

introduce `J` new label vertices, assign every Poisson edge occurrence an
independent uniform label, and lift the occurrence `e` to
`e union {lambda}`.  The lifted uniformity is `r=K+1`.

Conditional on a Poisson realization with all old degrees in
`[Lambda-t,Lambda+t]`, the mean label degree is

\[
\frac{s}{J}\,\overline d=\Lambda+O(t),
\]

not literally `Lambda`; the exponentially small floor imbalance is absorbed
by `t`.  Chernoff bounds give all label degrees in
`[Lambda-3t,Lambda+3t]` with probability `1-o(1)`.

For an old vertex `v` and a label `lambda`, let `Y_(v,lambda)` count lifted
occurrences containing both, and put

\[
Z=\sum_{v,\lambda}\binom{Y_{v,\lambda}}2.
\]

Then

\[
\mathbb E Z
 \le \frac1J\sum_v\binom{d(v)}2
 =O(K\Lambda^2).
\]

Intersecting the high-probability label-degree event with the Markov event
`Z=O(K Lambda^2)` gives one assignment satisfying both.  Delete one edge
whenever an old-vertex/label pair has multiplicity at least two.  Each
deletion lowers `Z` by at least one, so only `O(K Lambda^2)` edges and
`O(K^2 Lambda^2)=poly(m)=o(W)` incident vertices are affected.

The remaining lifted hypergraph has no parallel edges: equal lifted edges would share
the same label and every old vertex, contradicting the cleaned
old-vertex/label codegree one.  Its pair codegrees are at most `C`: old--old
pairs inherit the Poisson bound, old--label pairs have codegree at most one,
and label--label pairs have codegree zero.  Outside the polynomial exceptional
set, all degrees are at least `D-(6t+1)`, and
`6t+1=o(20(D^2 C log D)^(1/3))`.

This avoids confusing “no parallel edges” with the stronger convention
“simple means maximum pair-codegree one”; old--old codegrees may still be as
large as `C`, which is allowed by the theorem.  Thus the exceptional-set form
of ABKV Theorem 3.9 applies directly and gives
the same residual (3.1).  This validates the complete label-lift proof as an
alternative to Section 4.

## 6. Projection and exact OR accounting

Disjoint augmented edges have disjoint real masks, so every duplicate count
is zero.  If `Q` is the number of uncovered real vertices, (3.1) gives
`Q=o(W)`.  Every selected edge contains exactly `H` middle masks, whence

\[
pH=W-M_0,
\qquad p=(1+o(1))W/H.
\]

Concatenating the genuine reset words and appending all missing real masks
gives

\[
L_{\rm band}
 \le W+\frac{2h+1}{H}W+Q
 \le W+(8+o(1))W/\omega
       +W(\log m)^{-1/2+o(1)}.
\]

## 7. Scope and architecture ceiling

The theorem proves an explicit queue band

\[
h=(1+o(1))
\sqrt{\frac{\log m}{\log\log m\,\omega(m)}}.
\]

Within this ABKV matching architecture, negligible reset requires
`H/h->infinity`, while an `o(W)` leftover among `(2h+1)W` augmented vertices
forces `K=2hH+o(hH)` to be at most on the order of
`log m/log log m`.  Thus

\[
h=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right)
\]

is the natural ceiling of this mechanism.

More precisely, the matching ledger is

\[
hK\exp\!\left(-(1+o(1))\frac{\log m}{K}\right)=o(1).
\tag{6.1}
\]

In general, (6.1) and `H/h->infinity` imply only the order bounds

\[
K=O\!\left(\frac{\log m}{\log\log m}\right),
\qquad
h=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).
\]

The sharper constant

\[
K\le(2/3+o(1))\frac{\log m}{\log\log m}
\]

holds in the depth-maximizing regime
`log(H/h)=o(log K)` (equivalently
`log h=(1/2+o(1))log K`).  Without that extra rate hypothesis, `h` may grow
much more slowly than `sqrt(K)`, and constants for `K` arbitrarily close to
one are compatible with the same ledger.  This qualification does not
affect the proved choice `K~(1/2)log(m)/log log(m)`.

For this sparsification, the logarithmic exponent cannot improve through a
hidden much smaller codegree.  The total fractional incidence between
rank-`m+1` active masks and their same-start middle subsets is `N_1`:
each atom contributes `a_1`, and total atom mass is `W/H` with
`E a_1=HN_1/W`.  There are `N_1(m+1)` nested adjacent pairs, so some fixed
pair has fractional codegree at least `1/(m+1)`.  Its Bernoulli-sparsified
codegree is at least `(1-o(1))Lambda/(m+1)` with overwhelming probability.
Thus `C/D=Omega(1/m)` in a realization satisfying the other concentration
events, justifying the `-log m+o(log m)` exponent used in the ceiling ledger.

Within the depth-maximizing regime, this constant is approachable by taking
`H/h` to infinity subpolynomially slowly and

\[
K=\frac{\log m}{(3/2)\log\log m+g(m)}
\]

with a sufficiently large `g(m)->infinity`.  The submitted choice
`K~(1/2)log m/log log m` is conservative by only a constant and can improve
`h` by a factor `sqrt(4/3)`, not by a new exponent.

The cyclic-strip economical **cover** is stronger for raw OR coverage: it
already gives zero holes through any `J=o(sqrt(log m))`.  The queue theorem
remains valuable because it supplies a genuine zero-collision MTF packing
with prescribed profiles, a structure the strip cover does not provide.
