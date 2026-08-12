# Euler, owner, and transfer normal forms for complement-coherent `c`-space

Date: 2026-07-29

Status: exact structural theorem, explicit `k=15` resident constructions,
complete finite transfer criterion for Hamiltonicity, exact nonlinear
Euler-height objective, a verified 42-orbit candidate, a no-go theorem for
its whole bounded-defect portfolio, and exhaustive tiny `k=7` audit.  No
SAT/CP or heavy search is used here.  No `k=15` Hamilton carrier is claimed.

## 1. Main conclusion

The finite target in
`MATH_THEOREM_COMPLEMENT_COHERENT_CSPACE_NAND_NORMAL_FORM_20260729.md`
has two redundant gates and one sharper remaining gate.

Let `k=2m+1`, `r=m+1`, `W=kC`, and assume throughout that `W` is odd, as
required by plain complement coherence.  Let

\[
 T_i=\{x:c_{i-xC}=1\},\qquad d_j=c_{tj},qquad 2t=1\pmod W.
\]

Assume the cyclic `d`-word has no `00` and no `111` and that all `C` class
sums are `r`.  Then:

* every physical seam is automatically Johnson;
* middle Hamiltonicity is equivalent to exact lower-`q1` intersection
  bijectivity, so lower `q1` is not an additional gate;
* depth-one physical residence is automatic, but depth three at `k=15` is
  not;
* all upper/lower complementary load identities are automatic, but coverage
  on either side is not.

There are two exact constructive forms.

1. Class-balanced NAND words are Euler circuits of a fixed directed
   multigraph on `Z_C`.
2. Equivalently, their class columns obey a rank-`r` owner recursion on a
   finite graph of size

   \[
   r\binom{k}{r};
   \]

   physical residence is a bounded-memory condition on its owner word.

At `k=15`, this gives explicit linear-time constructions satisfying NAND,
all 429 class sums, every Johnson seam, and minimum physical one-run four.
The deterministic baseline recorded here has 30 of the 429 middle necklace
classes.  The independently verified two-defect candidate
`scratch/k15_nand_gap_adj2_best_42.cw` has 42 middle classes, the same 42
lower-`q1` classes, and 42 occupied lower-`q2` quotient classes.

The correct objective is nonlinear.  It is the number of rotation classes
of the seven lifted zero-visit heights at each residue; lower `q2` deletes
the marked height of the unique gap-three departure.  The 42-candidate
creates a 21-residue fan of singleton height classes.  Nevertheless, every
word in its entire bounded two-adjacent-defect portfolio has at most 252
middle classes.  Thus the useful variable is the accumulated lift/carry of
a genuinely nonperiodic long-residue permutation, not a local score on the
multiset of gap lengths.  The exact unresolved local carrier gate is such a
residence-compatible Euler walk whose height profiles form one complete
necklace transversal.  Once that happens, lower `q1` follows for free.

## 2. Set-valued NAND recursion

It is useful to absorb the inverse-two permutation and class fibres at once.
For every integer `j`, put

\[
 D_j=\{y\in\mathbb Z_k:d_{j-yC}=1\}.                 \tag{2.1}
\]

The indexing is helical:

\[
 D_{j+C}=D_j+1.                                      \tag{2.2}
\]

### Lemma 2.1 (class sums survive inverse two)

The `C` original class sums of `c` equal `r` if and only if

\[
 |D_j|=r\qquad(0\le j<C).                            \tag{2.3}
\]

#### Proof

The class sum at residue `a` is

\[
 \sum_{x\in\mathbb Z_k}c_{a-xC}
 =\sum_x d_{2a-(2x)C}.
\]

Multiplication by two permutes both `Z_C` and `Z_k`, because `C,k` are odd.
Thus these are exactly the weights of all fibres (2.1), in a permuted order.
∎

### Theorem 2.2 (automatic Johnson identity)

Under (2.3), the NAND law is equivalent to

\[
 \boxed{D_j\cap D_{j+2}=\overline{D_{j+1}}}          \tag{2.4}
\]

for every integer `j`.  Moreover, with `mu(x)=2x` on `Z_k`,

\[
 T_i=\mu^{-1}D_{2i},
 \qquad
 X_i:=T_i\cap T_{i+1}
       =\mu^{-1}\overline{D_{2i+1}}.                 \tag{2.5}
\]

Consequently every seam has intersection rank `m` and symmetric difference
two.  The coordinate-pattern multiplicities across
`D_j,D_(j+1),D_(j+2)` are exactly

\[
 \#101=m,\qquad \#110=1,\qquad
 \#011=1,\qquad \#010=m-1.                          \tag{2.6}
\]

#### Proof

For a coordinate `y`, NAND says

\[
 d_{j+1-yC}=0
 \quad\Longleftrightarrow\quad
 d_{j-yC}=d_{j+2-yC}=1,
\]

which is (2.4).  The first identity in (2.5) follows from
`c_p=d_(2p)`; intersecting consecutive terms and applying (2.4) gives the
second.

The right side of (2.4) has size `m`.  Since both endpoint sets have size
`m+1`, their symmetric difference has size two.  The common endpoint pattern
is `101` and has size `m`; equal endpoint weights leave one `110` and one
`011`; the remaining `m-1` coordinates have pattern `010`.  ∎

Thus the 429 separate Johnson-seam equations listed in the earlier finite
target are redundant after NAND and the 429 class sums.

### Corollary 2.3 (middle and lower `q1` are the same gate)

The full middle multiplicity profile and lower-`q1` multiplicity profile are
complemented shifts of one another.  In particular,

\[
 \boxed{
 (T_i)\text{ enumerates the rank-}r\text{ layer}
 \Longleftrightarrow
 (X_i)\text{ enumerates the rank-}m\text{ layer}.}   \tag{2.7}
\]

The same equivalence holds at the necklace-orbit level.

#### Proof

Both maps `i -> 2i` and `i -> 2i+1` permute `Z_W`.  Equation (2.5), followed
by complementation and the fixed coordinate multiplier `mu`, is therefore a
bijection between the two multiplicity words.  ∎

Equivalently, the scalar law gives `X_i=overline(T_(i+t))`.  Lower `q1`
still has to be checked if only the scalar run count is known; it becomes
automatic as soon as middle Hamiltonicity is imposed.

## 3. Exact owner recursion

No `00` and the equal row weights imply

\[
 D_j\cup D_{j+1}=\mathbb Z_k,
 \qquad |D_j\cap D_{j+1}|=1.
\]

Let

\[
 u_j\text{ be the unique member of }D_j\cap D_{j+1}. \tag{3.1}
\]

Then

\[
 \boxed{
 D_{j+1}=\overline{D_j}\cup\{u_j\},
 \qquad
 D_{j+2}=D_j\setminus\{u_j\}\cup\{u_{j+1}\},}      \tag{3.2}
\]

where

\[
 u_j\in D_j,qquad u_{j+1}\in\overline{D_j},qquad
 u_{j+1}\ne u_j.                                    \tag{3.3}
\]

Conversely, starting from a rank-`r` set, a helical sequence satisfying
(3.2)--(3.3) and the closure below gives a class-balanced NAND word.  The
twisted closure is

\[
 (D_C,u_C)=(D_0+1,u_0+1).                            \tag{3.4}
\]

This gives the base transfer graph

\[
 \Gamma_k=\{(A,u):A\in\tbinom{\mathbb Z_k}{r},\ u\in A\},             \tag{3.5}
\]

with an arc `(A,u)->(B,v)` precisely when

\[
 B=\overline A\cup\{u\},qquad v\in\overline A.     \tag{3.6}
\]

It has

\[
 |V(\Gamma_k)|=r\binom{k}{r},\qquad
 \deg^+=m.                                           \tag{3.7}
\]

At `k=15`, these are 51,480 states and outdegree seven.  This is an exact
recursive construction, not a relaxation.

In physical order, the seam with row index `2i` deletes
`mu^(-1)u_(2i)` and inserts `mu^(-1)u_(2i+1)`.  Therefore minimum physical
one-run `h` is exactly the owner condition

\[
 \boxed{
 u_j\ne u_{j+2a-1}
 \quad(1\le a<h),}                                   \tag{3.8}
\]

with the helical extension (3.4).  For `k=15`, `h=4`, so the forbidden owner
returns have distances `1,3,5`.  Equivalently, if `a_i,b_i` are the physical
leaver and enterer, then

\[
 T_{i+1}=T_i-a_i+b_i,qquad
 b_i\notin\{a_{i+1},a_{i+2},a_{i+3}\}.              \tag{3.9}
\]

This proves that residence is finite-memory but is not supplied by the NAND
language itself.

## 4. Euler-tour classification of all class-balanced NAND words

Let the cyclic zero positions of `d` be

\[
 z_0,z_1,\ldots,z_{mC-1}.
\]

The forbidden words `00,111` say that every forward zero gap is two or
three.  Each class fibre has `r` ones and hence exactly `m` zeros.  Thus the
residues `z_a mod C` visit every vertex of `Z_C` exactly `m` times.

### Theorem 4.1 (Euler normal form)

Class-balanced NAND words are exactly the lifted Euler circuits of the
directed multigraph

\[
 G_{C,m}:\qquad
 v\longrightarrow v+2\quad\text{with multiplicity }m-1,
 \qquad
 v\longrightarrow v+3\quad\text{once}.              \tag{4.1}
\]

An Euler circuit is lifted from a starting zero by using its edge increments
`2,3` as the successive literal gaps in `d`.

#### Proof

Let `a_v` be the number of gap-three departures from residue `v`.  There are
`m-a_v` gap-two departures.  Flow balance at `v` gives

\[
 m=(m-a_{v-2})+a_{v-3},                              \tag{4.2}
\]

so `a_(v-2)=a_(v-3)` and all `a_v` are equal.  If `A` is the total number of
gap-three steps, summing literal gaps gives

\[
 W=2mC+A,
\]

whence `A=C`; therefore `a_v=1`.  Every arc in (4.1) is used once.

Conversely, an Euler circuit has `m` visits per residue, exactly `C`
gap-three steps, and total lifted length

\[
 2(m-1)C+3C=(2m+1)C=W.
\]

Its zeros are isolated and its one-runs have length one or two, while every
fibre has `m` zeros and `r` ones.  ∎

The graph is Eulerian.  For the live Mersenne cases `C` is odd, so its
`+2` arcs already connect `Z_C`; Hierholzer gives a linear-time construction.

There is also an exact count.  Let `tau(C,m)` be the common directed
in-arborescence cofactor of

\[
 L=mI-(m-1)P^2-P^3,                                  \tag{4.3}
\]

where `P` is cyclic shift on `Z_C`.  With the starting vertex fixed and the
first edge unrestricted, BEST gives

\[
 m\,\tau(C,m)((m-1)!)^C
\]

labelled tours.  Forgetting the labels of the parallel `+2` arcs leaves
`m tau(C,m)` tours.  There are `C` starting residues and `k` lifts, whereas
each indexed binary word is counted at each of its `mC` zeros.  Hence

\[
 \#\{\text{indexed class-balanced NAND words}\}=k\,\tau(C,m),          \tag{4.4}
\]

and

\[
 \tau(C,m)=\frac1C\prod_{j=1}^{C-1}
 \left(m-(m-1)\omega^{2j}-\omega^{3j}\right),        \tag{4.5}
\]

where `omega` is a primitive `C`th root.  Formula (4.4) is not needed for
the construction, but supplies an exact finite census.  Formula (4.5) is
the circulant-laplacian cofactor product.

## 4A. Marked height fibres: the exact nonlinear objective

The Euler circuit has a canonical lift which exposes the missing global
variable.  For every integer `j`, define the zero-height fibre

\[
 H_j=\{h\in\mathbb Z_k:d_{j+hC}=0\}.                 \tag{4.6}
\]

Let `lambda_j` be the height of the unique gap-three departure in residue
`j`.  Thus `lambda_j in H_j`, and the helical rules are

\[
 H_{j+C}=H_j-1,
 \qquad \lambda_{j+C}=\lambda_j-1.                   \tag{4.7}
\]

### Theorem 4.2 (marked odd-graph and shadow identities)

For every class-balanced NAND word,

\[
 H_j\cap H_{j+1}=\varnothing,                        \tag{4.8}
\]

\[
 \mathbb Z_k\setminus(H_j\cup H_{j+1})
   =\{\lambda_{j-1}\},                              \tag{4.9}
\]

and

\[
 H_{j+2}=(H_j\setminus\{\lambda_j\})
          \cup\{\lambda_{j-1}\}.                   \tag{4.10}
\]

Let `rho=2^(-1) mod k` and put

\[
 \phi(h)=-\rho h\pmod k.
\]

Then the physical middle, lower-`q1`, and lower-`q2` rows are exactly

\[
 T_i=\overline{\phi(H_{2i})},                        \tag{4.11}
\]

\[
 T_i\cap T_{i+1}=\phi(H_{2i+1}),                    \tag{4.12}
\]

and

\[
 T_i\cap T_{i+1}\cap T_{i+2}
   =\phi(H_{2i+1}\setminus\{\lambda_{2i+1}\}).     \tag{4.13}
\]

Consequently the exact quotient objectives are

\[
 \Phi(d)=\left|\{[H_v]:v\in\mathbb Z_C\}\right|,   \tag{4.14}
\]

\[
 \Psi(d)=\left|\{[H_v\setminus\{\lambda_v\}]:
                    v\in\mathbb Z_C\}\right|.      \tag{4.15}
\]

The number of middle classes and the number of lower-`q1` classes both
equal `Phi`; the number of occupied lower-`q2` quotient classes equals
`Psi`.  Middle Hamiltonicity is exactly `Phi=C`, since the rotation action
on rank `m` is free.  For lower `q2`, short rotation orbits can occur, so
literal physical coverage is the weighted quantity

\[
 \Psi_{\rm phys}
 =\sum_{\eta:\,n_\eta>0}|\eta|,
 \qquad
 n_\eta=\#\{v:[H_v\setminus\{\lambda_v\}]=\eta\}.  \tag{4.16}
\]

In particular, merely maximizing the unweighted `q2` counter need not
maximize the number of physical rank-`m-1` targets.

The C++ portfolio key

```text
(middle+q1, q2, middle)
```

is therefore exactly the redundant objective `(2 Phi, Psi, Phi)`, before
the physical orbit-size correction (4.16).

#### Proof

Two adjacent zero heights would give `00`, proving (4.8).  Since both fibres
have size `m`, their disjoint union has size `2m=k-1`.  A coordinate absent
from both `H_j` and `H_(j+1)` has consecutive `11` in `d`; the NAND law
forces a zero immediately before and after them, so the preceding zero has
its unique gap three.  It is therefore the unique missing coordinate
`lambda_(j-1)`, proving (4.9).  A zero in residue `j`
continues to residue `j+2` unless it is the unique gap-three departure;
the unique new zero is the gap-three departure from residue `j-1`.  This is
(4.10).

Since `c_p=d_(2p)`, coordinate `x` is absent from `T_i` exactly when
`d_(2i-2xC)=0`, which is (4.11).  The patterns at the three consecutive
`d` positions centered at `2i+1-2xC` show (4.12).  Finally,

\[
 d_j=d_{j+2}=d_{j+4}=1
\]

holds exactly when the zero at `j+1` has outgoing gap two and therefore
continues at `j+3`; this proves (4.13).  The maps `i -> 2i` and
`i -> 2i+1` traverse all residues modulo `C`, with only the helical rotations
in (4.7).  Equations (4.14)--(4.16) follow.  ∎

The owner pivot in Section 3 is `u_j=-lambda_(j-1)`.  Hence the exact
residence condition (3.8) can equivalently be written

\[
 \lambda_j\ne\lambda_{j+2a-1}
 \qquad(1\le a<h).                                  \tag{4.17}
\]

### Theorem 4.3 (long-residue permutation and carry recursion)

Assume `C>1`.

List the `C` special zeros in literal lifted order as

\[
 L_0<L_1<\cdots<L_{C-1}<L_C=L_0+kC
\]

and put

\[
 \pi_a=L_a\pmod C,
 \qquad \Delta_a=L_{a+1}-L_a.                      \tag{4.18}
\]

Then class-balanced NAND words are exactly the following data:

1. `pi` is a cyclic permutation of `Z_C`;
2. if `delta_a in {1,...,C-1}` is the positive representative of
   `pi_(a+1)-pi_a`, then

   \[
   \Delta_a=\delta_a+C\epsilon_a+2Cb_a,
   \quad
   \epsilon_a={\bf1}_{\delta_a\text{ even}},
   \quad b_a\in\mathbb Z_{\ge0},                    \tag{4.19}
   \]

   with `Delta_a>=3`;
3. the exact winding budget is

   \[
   w(\pi)+e(\pi)+2B=k,                               \tag{4.20}
   \]

   where

   \[
   w(\pi)=C^{-1}\sum_a\delta_a,
   \quad e(\pi)=\sum_a\epsilon_a,
   \quad B=\sum_a b_a.
   \]

Given these data, place zeros in block `a` at

\[
 L_a,\ L_a+3,\ L_a+5,\ldots,L_{a+1}-2.              \tag{4.21}
\]

This reconstructs `d` uniquely up to cyclic origin.  If

\[
 \kappa_a=
 \frac{\pi_a+\delta_a-\pi_{a+1}}C\in\{0,1\},
\]

then the marked-height carry is

\[
 \lambda_{\pi_{a+1}}-\lambda_{\pi_a}
   =\kappa_a+\epsilon_a+2b_a\pmod k.                 \tag{4.22}
\]

For a closed formula for all ordinary heights, put

\[
 n_a=(\Delta_a-3)/2.
\]

For each residue `v`, let `alpha_a(v) in {0,...,C-1}` solve

\[
 2\alpha_a(v)\equiv v-\pi_a-3\pmod C
\]

and set the integer

\[
 \beta_a(v)=\frac{L_a+3+2\alpha_a(v)-v}{C}.
\]

Then

\[
 H_v\setminus\{\lambda_v\}
 =\bigsqcup_a
 \left\{
   \beta_a(v)+2q:\ q\in\mathbb Z,
   0\le\alpha_a(v)+qC<n_a
 \right\}\pmod k,                                  \tag{4.23}
\]

and `H_v` is obtained by adjoining `lambda_v`.  Thus (4.14), (4.15),
(4.22), and (4.23) are the exact nonlinear residue-permutation objective.

#### Proof

Oddness of `Delta_a` and oddness of `C` force exactly the parity correction
in (4.19); all further legal lifts add `2C`.  Summing (4.19) and using
`sum Delta_a=kC` gives (4.20).  Conversely, (4.18)--(4.21) give one
gap-three departure in every residue and only gap-two departures otherwise,
so Theorem 4.1 applies.  Writing `L_a=pi_a+q_a C` and comparing consecutive
terms proves (4.22).  The ordinary zeros in block `a` have offsets
`3+2s`, `0<=s<n_a`; solving their residue congruence gives
`s=alpha_a(v)+qC`.  The defining congruence makes `beta_a(v)` integral, and
division by `C` gives (4.23).  ∎

The budget (4.20) is already restrictive.  In fact

\[
 w(\pi)=\sum_a\kappa_a
\]

is the positive integer number of cyclic descents of `pi`, so

\[
 e(\pi)\le k-w(\pi)\le k-1.                         \tag{4.24}
\]

Thus at most `k-1` transitions can have even positive residue difference.
The budget does not, however, bound the number of varying odd differences.
Those odd, low-winding transitions are the available source of
macroscopically many carry phases.

## 5. Exact physical run ledger

The scalar complement law says

\[
 \{p:c_p=0\}
 =\{q-s:c_q=c_{q+1}=1\}.                             \tag{5.1}
\]

Let `R` be the number of physical one-runs.  The adjacent-`11` start set has
size `|c|_1-R`, while (5.1) says that it is a translate of the zero set and
therefore has size `|c|_0`.  Hence

\[
 R=|c|_1-|c|_0=C.                                    \tag{5.2a}
\]

Translation also preserves the number of cyclic components.  The adjacent-
`11` set has `R` components only if every physical one-run has length at
least two.  A one-run of length `ell` then contributes one adjacent-`11`
component of length `ell-1`.  Applying (5.1) componentwise gives

\[
 \boxed{
 \{\text{physical zero-run lengths}\}
 =\{\text{physical one-run lengths}-1\}}             \tag{5.2}
\]

as multisets, up to a cyclic shift of the run indices.  In particular every
physical one-run has length at least two, and

\[
 \#\text{runs}=|c|_1-|c|_0=(m+1)C-mC=C.              \tag{5.3}
\]

Thus depth-one residence and the Catalan run count are automatic.  At
`k=15`, minimum one-run four is equivalent to minimum zero-run three and
remains an extra condition.

## 6. A complete transfer-matrix existence theorem

Fix a desired minimum physical one-run `h>=2`.  Lift `Gamma_k` to the finite
graph `widehat Gamma_(k,h)` whose vertices are compatible directed histories
of `2h-3` consecutive base states.  Here compatible means that all
constituent base arcs and every already testable odd-distance owner exclusion
hold.  A transition shifts the history by one, appends one base state, and
requires the new pivot to differ from the pivots at backward distances

\[
 1,3,\ldots,2h-3.                                    \tag{6.1}
\]

By (3.8), this lift is exact for residence.  Let `Sigma` add one to every
coordinate and pivot in a history.  The physical boundary condition is
`H_C=Sigma H_0`.

Let `\mathcal N_r` be the set of rotation necklaces of rank `r`; it has
exactly `C` elements because `gcd(k,r)=1`, so the central rotation action is
free.  Work in
the square-zero commutative algebra

\[
 \mathcal A=
 \mathbb Z[y_\nu:\nu\in\mathcal N_r]/(y_\nu^2:\nu\in\mathcal N_r).     \tag{6.2}
\]

For a history `H`, let `col(H)` be the necklace of the last row set.  Define
the labelled adjacency matrix

\[
 \mathsf M_{H,H'}=
 \begin{cases}
 y_{\operatorname{col}(H')},&H\longrightarrow H',\\
 0,&\text{otherwise}.
 \end{cases}                                         \tag{6.3}
\]

### Theorem 6.1 (twisted squarefree coefficient criterion)

There exists a complement-coherent unit-voltage `c`-space carrier satisfying

* all class sums;
* NAND;
* minimum physical one-run `h`;
* a Hamilton middle cycle;
* exact lower `q1`;

if and only if

\[
 \boxed{
 \sum_H(\mathsf M^C)_{H,\Sigma H}\ne0
 \quad\text{in }\mathcal A.}                        \tag{6.4}
\]

Equivalently, over ordinary commuting variables, the coefficient of

\[
 \prod_{\nu\in\mathcal N_r}y_\nu
\]

in the same twisted trace is positive.

#### Proof

A length-`C` path from `H` to `Sigma H` extends helically and gives exactly
one class-balanced NAND word satisfying residence, by Sections 3 and 6.
Each transition weights the destination row.  The `C` destinations include
the shifted copy of the initial row, so they represent exactly the `C`
quotient rows.

Square-zero multiplication kills a path precisely when one middle necklace
is repeated.  A surviving product contains `C` distinct colors, and there
are exactly `C` available colors; hence it contains every middle necklace
once.  The helical extension then supplies all `k` rotations of every
selected necklace, which is exactly middle Hamiltonicity.  Conversely any
desired carrier gives a surviving path.  Corollary 2.3 supplies lower `q1`
automatically.  All coefficients are nonnegative, so there is no
cancellation.  ∎

This is a complete existence theorem, not a proposed raw computation of the
large lifted matrix.  It isolates the exact squarefree necklace-transversal
coefficient which remains after every local gate has been compiled.

## 7. An explicit resident `k=15` family

There is a closed-form family satisfying every local condition preceding
the squarefree necklace requirement in Theorem 6.1.  Put

\[
 C=429,\qquad h=4,\qquad \delta=(C+1)/2=215.          \tag{7.1}
\]

Choose any four-set \(A\subseteq\mathbb Z_C\) with

\[
 A\cap(A-\delta)=\varnothing,
\]

and put \(B=A-\delta\).  In physical `c` order, cyclically concatenate the 429
run pairs

\[
 \boxed{
 1^{\,4+C{\bf1}_A(i)}
 0^{\,3+C{\bf1}_B(i)}}
 \qquad(i\in\mathbb Z_C).                            \tag{7.2}
\]

### Theorem 7.1 (four-insertion construction)

Every word (7.2) has length `15C`, all 429 class sums eight, minimum physical
one-run four, the scalar complement law, and hence NAND after inverse two and
all Johnson seams.

#### Proof

The baseline `(1^4 0^3)^C` has length `7C`.  Since `gcd(7,C)=1`, every
residue modulo `C` sees four baseline ones.  Every inserted block `1^C` adds
one one to every residue; the four such blocks raise every class sum to
eight.  Inserted `0^C` blocks do not change them.  Minimum one-run four is
immediate.

Let \(a_i\) be the lifted start of one-run `i`, with
\(a_{i+C}=a_i+15C\), and let
\(\ell_i=4+C{\bf1}_A(i)\).  With the disjoint union
\(E=A\mathbin{\dot\cup}B\), the identity

\[
 |E\cap[i,i+\delta)|=4+{\bf1}_A(i)                  \tag{7.3}
\]

holds for every `i`.  Indeed, its discrete derivative is

\[
 E(i+\delta)-E(i)=A(i+1)-A(i)
\]

because \(B=A-\delta\) and \(2\delta=1\pmod C\); averaging fixes the constant at
four.  Therefore, with `s=(15C-1)/2`,

\[
 a_{i+\delta}-a_i
 =7\delta+C(4+{\bf1}_A(i))
 =s+\ell_i.                                          \tag{7.4}
\]

The zero-run following run `i` has length

\[
 3+C{\bf1}_B(i)=\ell_{i+\delta}-1.
\]

Thus translation by `s` maps each zero run exactly to the adjacent-`11`
interior of one run.  This is (5.1), hence the scalar complement law.  Apply
Theorem 2.2.  ∎

For

\[
 A=\{153,306,337,398\},
 \qquad B=\{91,122,183,367\},                        \tag{7.5}
\]

the retained cyclic origin has bitstring SHA-256

```text
f4132617a93e0a01d5eaa7d73e30b542f542a9d1a47dbad3119c3aae5d19af48
```

It has zero Johnson defects and exactly 12 middle necklaces; its lower-`q1`
profile has the same 12 necklaces, as predicted.

This whole four-insertion family is not Hamilton.  In every residue column,
the seven baseline bits occur as a cyclic subsequence equal, up to rotation,
to

```text
1100110.
```

The rank-eight necklace `000011111110001` (canonical little-endian mask
`18416`) has one one-run of length seven and one singleton one-run.  It cannot
contain two separated `11` blocks with selected zeros between them, so it
cannot contain the displayed cyclic subsequence.  Hence this orbit is absent
from every member of (7.2).  The family proves local compatibility, not the
squarefree coefficient (6.4).

## 8. A stronger deterministic Euler construction

The Euler theorem gives a less closed-form but more dispersed example.  At
each vertex `v in Z_429`, order its seven outgoing increments as six `2`s and
one `3`, placing the `3` in slot

\[
 4v+3\pmod7.                                         \tag{8.1}
\]

Starting at zero, consume these lists from left to right in ordinary
stack-Hierholzer order.  Lift the resulting 3,003-edge Euler circuit by its
literal increments and set `c_p=d_(2p)`.

The exact one-pass audit gives:

* all 429 class sums equal eight;
* no `00` or `111` in `d`;
* minimum physical one-run four;
* zero Johnson defects;
* 30 distinct middle necklaces and exactly the same 30 lower-`q1`
  necklaces.

The frozen bitstring hashes are

```text
d 36b168285fa66ab7f53d311c6fa81505c38757495c7295ccab2a0a4741a112fe
c d72cbfbacb82a1db0e1311a0f77b0d96f2253a11a9c20a464f571f3abb7bcc4d
```

and the comma-decimal Euler vertex path has SHA-256

```text
374f5ccc8ec2dc64702d8a40f9c27cb9e17da1344cadad331691f97327c05c79
```

Thus all requested local gates coexist constructively at `k=15`; this is a
30-class deterministic baseline for the global height-profile problem.

## 8A. The verified 42-class carry fan

The retained candidate

```text
scratch/k15_nand_gap_adj2_best_42.cw
```

is an exact instance of Theorem 4.3.  With `L_0=0`, its long-residue order is

\[
 \pi_a=7a\pmod{429}
\]

except for the two adjacent transpositions

\[
 (\pi_{262},\pi_{263})=(125,118),
 \qquad
 (\pi_{264},\pi_{265})=(139,132).                   \tag{8.2}
\]

The proof-safe source self-test freezes the affine score
`(26,26,23,4)`; (8.2) is the certified residue-order improvement to
`(42,42,42,4)`.  This comparison is between retained constructions, not an
optimality statement for either family.

All long-interval lengths are seven except

\[
\begin{array}{c|rrrrrr}
a&54&261&262&263&264&265\\ \hline
\Delta_a&865&443&851&21&851&443.
\end{array}                                         \tag{8.3}
\]

Equations (4.21)--(4.23) reconstruct its whole binary trace from this table.
Its zero-gap histogram is

\[
 \#\{\text{gap }2\}=2574=6C,
 \qquad
 \#\{\text{gap }3\}=429=C,                          \tag{8.3a}
\]

and every residue supports exactly one gap-three departure.  Hence its
projected zero walk is literally an Euler circuit of `G_(429,7)`, not merely
a word passing class sums.

The independent literal and height-fibre audit proves

\[
 (\text{middle},\text{lower }q1,
   \text{occupied lower }q2,\min\text{ physical run})
 =(42,42,42,4).                                      \tag{8.4}
\]

There are no class-sum, NAND, Johnson, or residence defects.  The physical
one-run histogram is

\[
 4^{423},\ 11^1,\ 222^2,\ 426^2,\ 433^1.            \tag{8.5}
\]

The multiplicities of the 42 height-fibre necklace classes are

\[
 1^{21},\ 12^7,\ 17^6,\ 18^1,\ 29^6,\ 30^1,         \tag{8.6}
\]

and those of the 42 marked-deletion classes are

\[
 1^{21},\ 11^1,\ 12^6,\ 17^5,\ 18^2,\ 29^6,\ 30^1. \tag{8.7}
\]

The 21 singleton `H` classes occur exactly at the consecutive residue band

\[
 120,121,\ldots,140.                                 \tag{8.8}
\]

The singleton marked-deletion classes occur at

\[
 \{118\}\cup\{120,121,\ldots,138\}\cup\{140\}.     \tag{8.9}
\]

Thus the two transpositions create a literal 21-residue carry fan.  This is
a structural gain over the recorded affine lift-relocation baselines, rather
than a change in the forced gap multiset; no optimum over all affine lift
placements is asserted.  All 42 occupied rank-six orbits in this candidate
have full rotation size 15, so (4.16) equals 630 distinct physical lower-
`q2` targets out of 5,005.  The exact physical load histogram is

\[
 1^{315},\ 11^{15},\ 12^{90},\ 17^{75},\ 18^{30},\
 29^{90},\ 30^{15}.                                 \tag{8.9a}
\]

The word is not a middle or shadow transversal.

The frozen hashes are

```text
candidate file  d9439da1e9e6ba347de2f8062e6a2784a2f389137d71146e1dbd4898fccf8e70
normalized c    a31b0769ecf2f8add44a38ac90791b1b113ff23e06e15f88ef9fa9af8938d78f
normalized d    58d060e605ce3f7ee0e5fcf4cd06d9b7936101027422adc343080047f9455859
long order CSV  ff557145f1e72542cb4fbfcc0d123df5dce9223c18cc67bcc65523da6ff89f55
interval CSV    4f0bf8e5a11a59e070f251ba3dfe12b3a7ad11498d9a96408ceae5ec1e828364
```

### Theorem 8.1 (piecewise-periodic fibre bound)

Let `1<=p<C`.  Suppose the cyclic word `d` is partitioned into `J` arcs and,
on each arc, agrees with a `p`-periodic word.  Then

\[
 \boxed{
 \left|\{[H_v]:v\in\mathbb Z_C\}\right|
 \le \gcd(p,C)+pJ-1.}                               \tag{8.10}
\]

#### Proof

Compare `d_(v+hC)` with `d_(v+p+hC)` for all sheets `h`.  Unless one of
these length-`p` comparisons crosses an arc boundary, periodicity gives
`[H_(v+p)]=[H_v]`; crossing `C` only applies the helical rotation (4.7).
Each literal boundary can spoil at most `p` projected residues, so the actual
number `e` of exceptional directed edges of the `+p` graph on `Z_C` is at
most `pJ`.  Put `g=gcd(p,C)`.  If no edge is exceptional, there are at most
`g` classes.  Otherwise, if the exceptional edges meet `d` of the original
`g` cycles, deleting them leaves exactly `g-d+e` path components.  Since
`d>=1`, this is at most `g+pJ-1`, proving (8.10).  ∎

### Corollary 8.2 (the bounded adjacent-defect portfolio cannot close)

In the exact two-adjacent-defect portfolio used to produce (8.2), at most six
blocks have `Delta_a!=7`.  Indeed, one isolated swap in the affine order
replaces three consecutive lengths

\[
 (7,7,7)\longmapsto(443,851,443),                   \tag{8.10a}
\]

and consumes `4C` of the available `8C` winding surplus.  Two separated
swaps therefore create six exceptional blocks and leave no lift unit.  If
the disjoint swaps are two positions apart, their interacting five-block
replacement is

\[
 (7,7,7,7,7)
 \longmapsto(443,851,21,851,443),                   \tag{8.10b}
\]

which consumes `6C`; the one remaining `2C` lift can make at most one
additional block exceptional.  Thus six is uniform over the exact
portfolio.

Every normal block is

```text
0110101
```

and hence is 7-periodic.  Every exceptional block is of the form

```text
011(01)^n
```

and splits into a bounded prefix and a 2-periodic tail.  Therefore the whole
cyclic word has a partition into at most `3*6=18` arcs, each agreeing with a
14-periodic word.  Since `gcd(14,429)=1`, Theorem 8.1 gives

\[
 \boxed{\Phi\le1+14\cdot18-1=252<429.}             \tag{8.11}
\]

This covers every state in the exact two-disjoint-adjacent-swap portfolio,
not only the retained 42-candidate.  For separated swaps the exact budget
has no remaining lift unit; for neighboring disjoint swaps it has one, which
can make at most one additional normal block exceptional.  More generally,
a `p`-phase construction with `Phi=C` must have at least

\[
 J\ge
 \left\lceil\frac{C-\gcd(p,C)+1}p\right\rceil        \tag{8.12}
\]

phase arcs.  For `p=14,C=429`, this is 31.  Therefore longer annealing in the
bounded-defect family cannot produce a transversal.  A scalable constructive
rule must use (4.19)--(4.23) with macroscopically many odd-difference phase
changes, while respecting the winding budget and the marked-height residence
exclusions.

## 9. Residence macro normal form at `k=15`

There is also an exact local compression before the 429 class sums are
imposed.  Put

\[
 P=1010101,\qquad Q=01.
\]

### Theorem 9.1 (unique cyclic `P/Q` parsing)

Up to rotation, a length-`15C` word `d` satisfies NAND, has physical
minimum one-run four after inverse two, and has totals `(8C,7C)` if and only
if it is a cyclic concatenation of exactly `C` copies of `P` and `4C`
copies of `Q`.

#### Proof

The recurrent length-eight histories for NAND plus the step-two residence
forbidden words are

```text
A=01010101  B=10101010  C=10101011
D=01010110  E=10101101  F=01011010
G=10110101  H=01101010  I=11010101.
```

Their complete recurrent transition graph is

```text
A -> B,C     B -> A
C -> D -> E -> F -> G -> H -> I
I -> B,C.
```

Every directed cycle meets `{A,I}`.  Between successive visits, the branch
through `B` emits `Q` and the branch through `C,D,...,I` emits `P`; both
branches are available from either junction.  Hence the cyclic parsing is
complete.  It is unique because neither macro contains an internal `11`,
and every `P` begins at the second bit of a cyclic `11`; these markers
recover all `P` starts.  If `x=#P,y=#Q`, then

\[
 (\#1,\#0)=(4x+y,3x+y)=(8C,7C),
\]

which forces `x=C,y=4C`.  The converse follows from the same transition
graph.  ∎

This reduces the local word from 6,435 bits to a 2,145-symbol macro necklace
with 429 `P` symbols.  Macro counts alone do not give the 429 class sums: the
cumulative binary lengths modulo `C` still matter.

For example, the resident NAND word

\[
 (P Q^4)^C                                             \tag{9.1}
\]

has period 15.  Since \(C=429\equiv9\pmod {15}\), each class fibre visits five period
positions three times, so every fibre weight is divisible by three and
cannot equal eight.  This proves that class sums are independent of the
local NAND/residence language.

## 10. Complete tiny `k=7` census

At `k=7`, `m=3`, `C=5`.  Marking one zero, a NAND word with the correct
global totals is determined by choosing which five of its fifteen zero gaps
have length three.  Rotating and deduplicating gives exactly 7,007 indexed
words.  The exhaustive gap audit gives:

\[
\begin{array}{c|c}
(\min\text{ physical one-run},\ \#\text{ middle/q1 necklaces})
 &\#\text{ words}\\ \hline
(2,4)&140\\
(2,3)&70\\
(4,1)&7.
\end{array}                                           \tag{10.1}
\]

Exactly 217 words pass all five class sums; this agrees with
`tau(5,3)=31` and `k tau=217`.  All 217 have zero Johnson defects, and their
middle and `q1` necklace counts agree exactly.  Thus:

* class sums do not force residence;
* even clean residence does not force Hamiltonicity;
* the automatic Johnson and middle/`q1` equivalence are visible already at
  the first nontrivial Mersenne case.

## 11. Automatic versus independent constraints

The exact implication ledger is:

| Constraint | Status after NAND |
|---|---|
| global totals and `d` run counts | forced only after class sums (or explicit totals) |
| all individual class sums | independent; (9.1) fails them |
| Johnson seam equations | automatic from NAND plus class sums |
| Catalan physical run count | automatic from NAND plus class sums |
| physical one-runs of length at least two | automatic |
| physical one-runs of length at least four | independent; finite owner-memory gate |
| middle necklace Hamiltonicity | independent; exact squarefree coefficient (6.4) |
| lower-`q1` orbit bijection | equivalent to middle Hamiltonicity, not separate |
| upper depth `q` vs lower depth `q+1` loads | automatically paired by complement |
| completeness at either shadow depth | remains independent; the resident 42-candidate covers only 630 of 5,005 physical lower-`q2` targets |
| one-core, Hall, cut, literal compiler | not implied by any identity proved here |

The depth-three independence assertion has a direct `k=15` witness: order
the six `+2` arcs before the unique `+3` arc at every Euler vertex and apply
stack-Hierholzer.  The resulting class-balanced NAND word has zero Johnson
defects but physical one-run histogram

\[
 2^{426},\ 3^2,\ 2574^1,
\]

so its minimum run is two.  Its normalized `c` SHA-256 is
`6ef125f1ffcc38176db8f44bdc65bb25dc533e347688441291329b3fe2b83a10`.

For arbitrary window length `L`, complement coherence gives a literal
upper/lower duality of that same length (with one additional intersected
middle set).  It does **not** justify replacing arbitrary-width upper
coverage by only the minimal-width lower flag row.  One side of the complete
all-width oracle may be removed only when the corresponding all-width audit
is retained on the other side.

## 12. Reproducibility and proved boundary

The lightweight verifier is

```text
scratch/audit_cspace_nand_euler_transfer_20260729.py
```

It exhausts only the 7,007 `k=7` gap words and performs linear one-pass
checks on the two explicit `k=15` constructions and the retained 42-class
candidate.  It uses no optimizer.  For the candidate it independently
reconstructs the Euler tour, marked height fibres, physical rows, both exact
formulas (4.11)--(4.13), multiplicities, and hashes.  It reproduces every
census, histogram, orbit count, and hash displayed above.

The annealer was not rerun.  The original independent literal verifier and
certificate remain

```text
scratch/verify_k15_nand_gap_candidate.py
scratch/k15_nand_gap_adj2_best_42.audit.json
```

The constructive boundary is now exact:

\[
 \boxed{
 \text{NAND + all class sums + residence + Johnson are feasible at }k=15;
 }
\]

Within the complement-coherent unit-voltage subclass, Johnson needs no
separate enforcement, and lower `q1` will need no separate enforcement once
middle Hamiltonicity is achieved.  What remains is the nonvanishing of the
residence-compatible squarefree necklace coefficient (6.4), followed by one
complete lower/upper shadow side and the compiler.  The bounded
two-adjacent-defect family cannot supply that coefficient by Corollary 8.2;
the exact surviving design space is the low-winding nonlinear permutation
recursion (4.19)--(4.23).  No asymptotic family with `Phi` tending to infinity,
and no `Phi=429` construction, is claimed here: the positive advance is the
exact 21-residue carry fan and objective; the negative advance is the
portfolio-wide bound 252.

## 13. Exact collision-floor potential on the complete mixed-step face

The implementation

```text
scratch/k15_nand_euler_mixed_step_search.cpp
```

uses the exact mixed-step normal form

\[
 \Delta_a=7+2y_a,\qquad y_a\ge0,\qquad
 \sum_a y_a=1716,
\]

with the 429 partial sums forming a permutation modulo 429.  This is the
whole class-balanced NAND/Euler face with physical residence at least four,
not the earlier affine or bounded-defect slice.  Its fail-closed eager audit
reconstructs and checks the literal physical trace before writing a
candidate.

There is an exact scalar potential for its two quotient palettes.  Put 429
middle labels into 429 orbit bins and the same 429 occurrences into the 335
lower-q2 orbit bins.  Let `phi,psi` be the occupied-bin counts and let
`P_phi,P_psi` count unordered colliding pairs.  If

\[
 a=429-\phi,\qquad b=335-\psi,
\]

then convexity of `binom(load,2)` gives, throughout the relevant range,

\[
 P_\phi\ge a,
 \qquad
 P_\psi\ge 94+b.
\]

Consequently

\[
 \boxed{\Xi:=P_\phi+P_\psi-94\ge a+b.}             \tag{13.1}
\]

Thus `Xi=0` is a smooth sufficient certificate for simultaneous middle/q1
and lower-q2/dual-upper-q1 perfection, not a heuristic score.  Completeness
does not imply `Xi=0` unless the punctured load profile is floor-balanced:
loads of three or more add collision excess without creating a hole.

The first complete mixed-step portfolio also produced a new one-sided exact
construction.  Its independently replayed metrics are

\[
 (\phi,\psi,\psi_{\rm physical},\min\operatorname{run})
   =(367,335,5005,4),
\]

with zero class-sum, NAND-language, Johnson, or residence defects.  Its raw
c-word SHA-256 is

```text
de3786f9b6b3f3b211e991fbf9f38a2f0a5026b6d63eee07810439c2746d3936
```

This is the first exact complete lower-q2 deck in this complement-coherent
face; by the proved complement identity it simultaneously gives the exact
dual upper-q1 deck.  It is **not** a decorated carrier or OR-word
certificate, because only 367 of the 429 middle/q1 necklace classes are
occupied.  It proves, however, that the deep-shadow side of this face has no
standalone existence obstruction; the remaining question is simultaneous
squarefreeness of the middle deck.
