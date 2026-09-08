# Capped lower shadows: compression, sharp two-covered profiles, and a partial-colex obstruction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It reformulates the
protected-Ore slack as a capped-multiplicity lower shadow, proves that
ordinary coordinate shifts never increase that functional, gives the exact
Kruskal--Katona bound on the two-covered face, and exhibits a connected
positive-defect family in the localized size range with slack below
`6|A|`.  Thus a universal estimate of the form
`sigma(A)>15|A|+2m` cannot close the residual small-cut problem, even after
the exact principal stars and down-cliques are removed.  For `m>=144` and
families of size at least `2m`, the theorem also shows that every family
violating that estimate has dense Johnson neighbourhoods on more than half
of its members.  These size hypotheses are necessary for that conclusion;
a singleton is an immediate counterexample without them.

No computation, search, or solver is used.

## 0. Setting

Fix `m>=2`, put `n=2m-1`, and write

\[
 \mathcal L={{[n]}\choose {m-1}},\qquad
 \mathcal U={{[n]}\choose m}.
\]

For `A subseteq mathcal L` and `U in mathcal U`, put

\[
 a_U=|\{X\in A:X\subset U\}|,
 \qquad
 \sigma(A)=\sum_{U\in\mathcal U}\min\{2,a_U\}-2|A|.
\tag{0.1}
\]

This is the exact unprotected capacity in the protected Ore--Ryser
criterion.

For an `m`-uniform family `F`, write

\[
 d_F(D)=|\{Y\in F:D\subset Y\}|\qquad
       \left(D\in{{[n]}\choose {m-1}}\right)
\tag{0.2}
\]

and define its capped lower-shadow mass by

\[
 \Psi_2(F)=\sum_D\min\{2,d_F(D)\}.
\tag{0.3}
\]

Let `partial F={D:d_F(D)>0}` be the ordinary lower shadow and let

\[
 q_1(F)=|\{D:d_F(D)=1\}|.
\tag{0.4}
\]

## 1. Exact capped-shadow equivalence

### Theorem 1.1

Let

\[
                         F=\{[n]\setminus X:X\in A\}.
\tag{1.1}
\]

Then `|F|=|A|`, and

\[
 \boxed{a_U=d_F([n]\setminus U)}
\tag{1.2}
\]

for every `U in mathcal U`.  Consequently

\[
 \boxed{\sigma(A)=\Psi_2(F)-2|F|
       =2(|\partial F|-|F|)-q_1(F).}
\tag{1.3}
\]

#### Proof

For `X in mathcal L` and `U in mathcal U`,

\[
 X\subset U
 \quad\Longleftrightarrow\quad
 [n]\setminus X\supset[n]\setminus U.
\]

The two complements have ranks `m` and `m-1`, respectively, proving
(1.2).  A positive lower-shadow degree contributes one to `Psi_2`, and
it contributes a second unit exactly when its degree is at least two.
Thus

\[
 \Psi_2(F)=q_1(F)+2(|\partial F|-q_1(F))
           =2|\partial F|-q_1(F),
\]

which proves (1.3). \(\square\)

This is the requested complement formulation: `sigma` is precisely the
excess, above two units per member, of the lower shadow in which every
facet has capacity two.

## 2. The exact ordinary-shadow lower bound

Let `KK_m(f)` denote the Kruskal--Katona lower-shadow function.  Thus, if

\[
 f={c_m\choose m}+{c_{m-1}\choose m-1}+\cdots+{c_j\choose j}
\tag{2.1}
\]

is the canonical binomial expansion, then

\[
 KK_m(f)={c_m\choose m-1}+{c_{m-1}\choose m-2}
         +\cdots+{c_j\choose j-1}.
\tag{2.2}
\]

### Theorem 2.1 (capped Kruskal--Katona bound)

For every `F subseteq binom([n],m)` of size `f`,

\[
 \boxed{
 \Psi_2(F)-2f
 \ge {m-2\over m-1}\bigl(|\partial F|-f\bigr)
 \ge {m-2\over m-1}\bigl(KK_m(f)-f\bigr).}
\tag{2.3}
\]

If `f=binom(x,m)` for a real `x>=m`, the Lovasz form is

\[
 \boxed{
 \sigma(A)\ge {m-2\over m-1}
 \left({x\choose m-1}-{x\choose m}\right).}
\tag{2.4}
\]

Equality in the first inequality of (2.3) occurs exactly when every
lower-shadow degree lies in `{1,m}`.

If `F` is **two-covered**, meaning `q_1(F)=0`, then the sharper exact bound

\[
 \boxed{
 \Psi_2(F)-2f
 =2(|\partial F|-f)
 \ge2(KK_m(f)-f)}
\tag{2.5}
\]

holds.  It is attained by every two-covered initial colex segment.

#### Proof

Put `S=|partial F|` and `q=q_1(F)`.  Counting incidences between `F` and
its facets gives

\[
 mf=\sum_Dd_F(D)\le q+m(S-q)=mS-(m-1)q.
\]

Hence

\[
 q\le {m(S-f)\over m-1}.
\]

Substitution in (1.3) gives the first inequality of (2.3).  Equality in
the incidence estimate says exactly that every nonunique positive degree
is `m`.  Kruskal--Katona gives the second inequality, and its Lovasz form
gives (2.4).  If `q=0`, identity (1.3) gives (2.5); a colex initial segment
has ordinary shadow `KK_m(f)`. \(\square\)

The coefficient in (2.3) cannot by itself give the desired constant-15
separation.  More importantly, even the stronger two-covered bound (2.5)
admits macroscopic low-slack partial-colex profiles, as Section 4 shows.

## 3. Coordinate compression is valid for the capped functional

Let `S_ij F` be the usual `(i,j)`-shift, with `i<j`: replace a member
containing `j` but not `i` by the set obtained by exchanging `j` for `i`,
provided that replacement is not already present.

### Theorem 3.1 (capped-shadow shifting)

For every coordinate shift,

\[
                         \boxed{\Psi_2(S_{ij}F)\le\Psi_2(F).}
\tag{3.1}
\]

Consequently an extremizer of `Psi_2` at fixed cardinality may be chosen
shifted.

#### Proof

Facets containing neither `i` nor `j` keep the same number of extensions:
the two possible extensions using `i` and `j` merely exchange occupancy.
Facets containing both coordinates are untouched.

It remains to consider the paired facets

\[
                         C\cup\{i\},\qquad C\cup\{j\},
 \qquad |C|=m-2.
\]

Apart from their common possible extension `C union {i,j}`, let `R_i`
and `R_j` be the sets of outside coordinates producing extensions of the
two facets.  After shifting, these become

\[
                         R_i\cup R_j,\qquad R_i\cap R_j.
\]

Thus the new pair of degrees has the same sum as the old pair and
majorizes it.  The function `phi(t)=min(2,t)` is concave on the
nonnegative integers.  Therefore

\[
 \phi(d_i')+\phi(d_j')\le\phi(d_i)+\phi(d_j).
\]

Summing over all paired facets proves (3.1). \(\square\)

This proves that compression is legitimate, but it does **not** say that
every capped-shadow minimizer is an initial colex segment.  Ordinary
Kruskal--Katona alone cannot make that stronger conclusion because the
unique-facet term in (1.3) is independent data.

## 4. A connected partial-colex obstruction

For integers

\[
 m+1\le t\le2m-2,qquad m\le u\le t-1,
\tag{4.1}
\]

put `z=t+1` and define

\[
 \mathcal F_{t,u}=
 {{[t]}\choose m}\ \dot\cup\
 \bigl\{\{z\}\cup H:H\in{{[u]}\choose {m-1}}\bigr\}.
\tag{4.2}
\]

This is an initial colex segment: it consists of the complete first block,
followed by a complete initial block in the `z`-section.

### Theorem 4.1 (exact two-level staircase)

The family `F_(t,u)` is two-covered and Johnson-connected.  Its exact
cardinality and capped slack are

\[
 \boxed{
 f={t\choose m}+{u\choose m-1},}
\tag{4.3}
\]

and

\[
 \boxed{
 \Psi_2(\mathcal F_{t,u})-2f
 =2\left[{t\choose m-1}+{u\choose m-2}
          -{t\choose m}-{u\choose m-1}\right].}
\tag{4.4}
\]

It attains the two-covered lower bound (2.5).

#### Proof

A facet contained in `[t]` has degree `t-m+1`, with one additional
extension through `z` exactly when it lies in `[u]`.  A facet of the form
`{z} union J`, `J in binom([u],m-2)`, has degree `u-m+2`.  These are all
the positive-degree facets.  Under (4.1) every displayed degree is at
least two.  Hence

\[
 \partial\mathcal F_{t,u}
 ={{[t]}\choose {m-1}}\ \dot\cup\
  \bigl\{\{z\}\cup J:J\in{{[u]}\choose {m-2}}\bigr\},
\]

and every member of the shadow contributes two to `Psi_2`.  This proves
(4.3)--(4.4).  Since the family is an initial colex segment, its displayed
shadow is `KK_m(f)`, proving sharpness in (2.5).

The complete first block is Johnson-connected.  Every set `{z} union H`
in the second block is adjacent to `H union {x}` in the first block for
any `x in [t]-H`, which is nonempty.  Hence the full family is connected.
\(\square\)

### Corollary 4.2 (localized macroscopic counterfamily)

Let `m=4q`, `t=5q`, and `u=5q-1`.  Let `A_q` be the complement image of
`F_(t,u)` under (1.1).  Then `A_q` is Johnson-connected, has positive
clique-closure defect, and

\[
 |A_q|={9\over5}{5q\choose4q}<2^{m+1},
\tag{4.5}
\]

while

\[
 \boxed{
 {\sigma(A_q)\over|A_q|}
 ={54m-104\over9m+36}
 =6-{320\over9m+36}<6.}
\tag{4.6}
\]

In particular,

\[
                         \boxed{\sigma(A_q)<15|A_q|+2m.}
\tag{4.7}
\]

These are neither principal up-stars nor zero-defect down-cliques.  They
are also a macroscopic perturbation of both adjacent complete-support
colex profiles: deleting the second block to obtain `binom([5q],4q)`
changes exactly

\[
 {5q-1\choose4q-1}={4\over9}|A_q|
\tag{4.8}
\]

members, while completing the support to `[5q+1]` changes still more.
Thus they are not an `o(|A_q|)` Hamming perturbation of either adjacent
principal-star extremizer.

There is an exact geometric description which should not be hidden.  Put

\[
 C_0=[n]\setminus[t],\qquad
 C_1=[n]\setminus([u]\cup\{z\}).
\tag{4.9}
\]

Then `C_0,C_1` have the same size and differ by one coordinate exchange,
and

\[
 \boxed{A_q=\mathcal A_{C_0}\cup\mathcal A_{C_1}.}
\tag{4.10}
\]

Indeed, the complements of the second colex block are the members of
`mathcal A_(C_1)` which omit `z`; the omitted members of that star contain
`C_0` and already lie in `mathcal A_(C_0)`.  Thus the obstruction is a
**macroscopic two-centre Hamming-one union**, not a mysterious new
geometry.  If an external theorem already closes all such multi-centre
Hamming unions, this example does not contradict that theorem; it still
proves that scalar `sigma`-isoperimetry alone cannot replace it.

#### Proof

Put `f_0=binom(5q,4q)`.  Then

\[
 {5q-1\choose4q-1}={4\over5}f_0,
 \qquad f={9\over5}f_0.
\]

Furthermore

\[
 {\binom{5q}{4q-1}\over f_0}={4q\over q+1},
 \qquad
 {\binom{5q-1}{4q-2}\over\binom{5q-1}{4q-1}}
 ={4q-1\over q+1}.
\]

Substitution in (4.4) gives (4.6).  The standard estimate

\[
 {5q\choose q}\le(5e)^q<16^q=2^m
\]

gives (4.5).  All positive facet degrees are `q+1` or `q+2`, strictly
between one and `m` for large `q`; hence the clique-closure defect is
positive.  The family is not a complete layer on a support because its
`z`-section is proper, and it cannot be a facet-star because its complete
first block has empty total intersection.  Complementation translates
those two statements to the asserted principal-star/down-clique
exclusions.  Equation (4.8) is the exact second-block size. \(\square\)

More generally, taking `t=alpha m+O(1)` and `u=t-1`, with
`1<alpha<2`, gives

\[
 {\sigma(A)\over|A|}
 \longrightarrow {2(2-\alpha)\over\alpha-1}.
\tag{4.11}
\]

Whenever `alpha>19/17`, the limit is below `15`.  Whenever also

\[
 \alpha H_2(1/\alpha)\le1,
\tag{4.12}
\]

the family has size `2^{m+o(m)}` or smaller and lies in the exact
`O(m^2 2^m)` localization window.  Thus (4.7) is a continuum phenomenon,
not an isolated arithmetic example.

## 5. What low capped slack still forces: dense Hamming neighbourhoods

The counterfamily prevents a scalar closure, but low capped slack has a
strong local-density consequence.

### Theorem 5.1 (heavy-facet concentration)

Assume `m>=144`, `f=|F|>=2m`, and

\[
                         \Psi_2(F)-2f<15f+2m.
\tag{5.1}
\]

Put

\[
 L=\left\lceil {m\over72}\right\rceil,
 \qquad
 \mathcal H=\{D:d_F(D)\ge L\}.
\tag{5.2}
\]

Then more than half of the members `Y in F` contain at least `m/2`
facets from `mathcal H`.  Every such member has induced Johnson degree

\[
 \boxed{
 d_{J[F]}(Y)\ge {m\over2}(L-1)\ge {m^2\over288}.}
\tag{5.3}
\]

Thus every residual low-`sigma` family contains a positive-density set of
centres of quadratic-size Hamming-one neighbourhoods.

#### Proof

Equation (5.1) and `f>=2m` imply

\[
                         \Psi_2(F)<18f.
\tag{5.4}
\]

The number of positive-degree facets is at most `Psi_2(F)`.  The total
raw incidence carried by facets outside `H` is therefore less than

\[
 (L-1)\Psi_2(F)<{m\over72}18f={mf\over4}.
\]

Hence more than `3mf/4` member--facet incidences use `H`.  If at most
`f/2` members contained at least `m/2` heavy facets, their total number of
heavy incidences would be at most

\[
 {f\over2}m+{f\over2}{m\over2}={3mf\over4},
\]

a contradiction.

Finally, every Johnson neighbour `Y'` of `Y` shares a unique facet with
`Y`, so

\[
 d_{J[F]}(Y)=\sum_{D\subset Y}(d_F(D)-1).
\]

The first inequality in (5.3) follows.  Since `m>=144`,
`L-1>=m/144`, proving the second. \(\square\)

This is the strongest scalar reduction available from the threshold
`15|A|+2m` for families satisfying `m>=144` and `f>=2m`: after exact stars,
down-cliques, and their certified stability neighbourhoods, the remaining
work in that size range must control families assembled from many
overlapping quadratic Johnson neighbourhoods.  Ordinary Kruskal--Katona
cannot remove them.

## 6. The co-small side is a different functional

Let `C=mathcal L-A`, put `c=|C|`, and define

\[
                         G=\{[n]\setminus X:X\in C\}.
\]

For `j=0,...,m`, write

\[
                         n_j(G)=|\{D:d_G(D)=j\}|.
\]

### Theorem 6.1 (high-multiplicity co-small tail)

One has the exact identity

\[
 \boxed{
 \sigma(\mathcal L\setminus C)
 =2c-n_{m-1}(G)-2n_m(G).}
\tag{6.1}
\]

In particular

\[
                         \sigma(\mathcal L\setminus C)\le2c.
\tag{6.2}
\]

Therefore no estimate of the form

\[
 \sigma(A)>15\min\{|A|,|\mathcal L-A|\}+2m
\]

can hold on the co-small side.  Co-small protected Ore cuts must instead
be handled by the exact degree/rebate criterion: only `(m-1)`-fold and
`m`-fold facet stars can lower the baseline `2c`.

#### Proof

For `U in mathcal U`, let

\[
 d_U=|\{X\in C:X\subset U\}|.
\]

Under complementation, `d_U=d_G([n]-U)`.  Since `a_U=m-d_U`, regularity
gives the baseline

\[
 \sum_U{2d_U\over m}=2c.
\]

For `d_U<=m-2`, the local weighted-boundary term for `a_U` equals this
baseline.  At `d_U=m-1` it is one unit smaller, and at `d_U=m` it is two
units smaller.  Summing proves (6.1). \(\square\)

## 7. Consequence for the protected-reservoir programme

The pure isoperimetric question is now separated exactly.

1. Complementation turns the small-cut slack into a capacity-two lower
   shadow.
2. Shifting is valid, and Kruskal--Katona gives the exact answer on the
   two-covered face.
3. Nevertheless, connected partial-colex staircases of size below
   `2^(m+1)` have `sigma<6|A|`.  Hence the existing universal protected
   estimate `lambda_P(A)<=15|A|+2m` cannot be paired with a stronger
   universal `sigma` estimate to finish Ore extension.
4. Any such low-slack family with `m>=144` and size at least `2m` has dense
   quadratic Johnson neighbourhoods on more than half its members.  A
   successful next theorem in that range must exploit how the protected
   witness paths cross those neighbourhoods, rather than only their number
   of incidences.
5. Co-small cuts are governed by the separate high-multiplicity tail
   (6.1), exactly as in the frozen near-complete-clique criterion.

The remaining useful target is therefore a **protected crossing theorem
for shifted partial-colex staircases and their dense-neighbourhood
stability class**, not a stronger scalar isoperimetric inequality for
`sigma` alone.

## 8. Dependencies and scope

The only standard input is Kruskal--Katona (and its Lovasz real-binomial
form).  The protected interpretation of `sigma` is the one frozen in

* `MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md`;
* `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`.

Every capped-shadow, compression, partial-colex, and heavy-facet argument
above is proved directly.  Nothing here proves protected-factor
extension, residence, component joining, or common-cap feasibility.
