# Audit: near-cyclic invariance and the exact quotient gate

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Orbit mass is indeed invariant under rowwise powers of one coordinate
cycle, and a genuinely invariant factor attains its orbit-mass hole floor.
Two stronger conclusions do not follow.

1. Physical energy `O(W)` does not imply that a factor invariant under the
   **same** cycle has `o(W)` holes.  The `1/n` projection gain comes from
   choosing a cycle by conjugacy-class averaging; it disappears for a cycle
   under which the load is already invariant.
2. A near-invariant exact factor is not a full-orbit core plus an arbitrary
   small patch.  Its exceptional rows must themselves have an invariant
   middle support.  Thus the quotient construction contains an invariant
   deck problem, exactly the kind of structure exhibited by the genuine
   `Q_7` circuit.

The quotient route remains valid, but it is an alternative formulation of
the deck gate, not a proof that deck circuits are unnecessary.

## 1. Orbit-mass conservation and exact attainment

Fix a coordinate cycle `sigma` and one target rank.  For a row family `F`
write

\[
 M_F(O)=\sum_{S\in O}\mu_F(S)
\]

on every target orbit `O`.  Replacing any row `C` by any power
`sigma^a C` permutes that row's occurrences inside each `O`; hence

\[
 \boxed{M_{F'}(O)=M_F(O)}.                                      \tag{1.1}
\]

If `sigma F=F`, then `mu_F` is constant on every target orbit.  For an
orbit of length `n`, its mass is therefore `n k_O` for an integer `k_O`,
and its hole count is `n` precisely when `k_O=0`.  Consequently

\[
 \boxed{
 H(F)=\sum_O(n-M_F(O))_+ }
                                                               \tag{1.2}
\]

for an invariant factor.  This proves exact attainment of the orbit floor.

## 2. Why physical energy cannot be combined with same-cycle invariance

Put `lambda=W/N` and `f=mu-lambda 1`.  If `mu` is invariant under
`sigma`, then

\[
                         \Pi_\sigma f=f,                         \tag{2.1}
\]

not `||Pi_sigma f||^2=||f||^2/n`.  The latter identity holds only after
averaging `sigma` over its conjugacy class and then selecting a favorable
cycle.

Already at the load-vector level, take free `n`-orbits and put load zero
on half of them and load two on half of them.  The vector is invariant, has
mean one, and satisfies

\[
                         \|f\|_2^2=N=O(W),                       \tag{2.2}
\]

while it has `N/2=Theta(W)` holes.  Floor/ceiling adjustments accommodate
any mean `1+o(1)` without changing the conclusion.  Thus an implication

\[
 \text{same-cycle invariance}+\|f\|_2^2=O(W)
 \Longrightarrow H=o(W)                                       \tag{2.3}
\]

requires substantial extra wreath structure and is not a consequence of
the two displayed hypotheses.

The correct alternatives are different.

* Start with a physical low-energy factor, choose a favorable cycle by
  class averaging, and **lift** the resulting within-orbit transports.
* Construct an invariant or near-invariant factor whose quotient orbit
  loads are directly nonzero on all but `o(N/n)` target orbits.

The first is the prime-cycle row-lift gate.  The second is the quotient
covering gate.

## 3. Exact shared-necklace quadratic identity

For a row `C` and target orbit `O`, put

\[
 a_C(O)=\#\{\text{rank-}r\text{ intervals of }C\text{ lying in }O\},
\]

and

\[
 X(C,D)=\sum_Oa_C(O)a_D(O).
\]

For `M_F(O)=sum_(C in F)a_C(O)`, the orbit energy is

\[
 \begin{aligned}
 \mathcal E_\sigma(F)
  &:=\sum_O(M_F(O)-n\lambda)^2\\
  &=\boxed{\sum_{C,D\in F}X(C,D)-n\lambda W}.                   \tag{3.1}
 \end{aligned}
\]

Here there are `N/n` target orbits and `sum_O M_F(O)=W`.

The diagonal term is not automatically `W`.  One has

\[
 X(C,C)=\sum_Oa_C(O)^2\ge\sum_Oa_C(O)=n,                        \tag{3.2}
\]

with equality exactly when the `n` row intervals lie in distinct target
orbits.  An affine/AP row has all `n` intervals in one target orbit and
therefore has

\[
                         X(C,C)=n^2.                             \tag{3.3}
\]

Uniform one-row marginals under a random relabeling do not imply equality
in (3.2), nor do they determine the off-diagonal term.  The correct exact
averaging statement for a fixed physical factor is

\[
 \boxed{
 \mathbb E_\sigma\mathcal E_\sigma(F)
 =\|\mu_F-\lambda\mathbf1\|_2^2,}                               \tag{3.4}
\]

where `sigma` is a uniform prime coordinate cycle.  Combining this with
(3.1) gives the exact bilinear average

\[
 \boxed{
 \mathbb E_\sigma\sum_{C,D\in F}X_\sigma(C,D)
 =n\lambda W+\|\mu_F-\lambda\mathbf1\|_2^2.}                   \tag{3.5}
\]

If `P=sum_S binom(mu_F(S),2)` is the physical factorial pair moment, then
`||mu_F-lambda 1||_2^2=W+2P-lambda W`, so equivalently

\[
 \boxed{
 \mathbb E_\sigma\sum_{C,D}X_\sigma(C,D)
 =(n-1)\lambda W+W+2P.}                                       \tag{3.6}
\]

Thus separate diagonal and off-diagonal averages cannot be substituted
for (3.5) without controlling their covariance.  Uniform one-row
marginals determine neither term; only their complete sum has this exact
conjugacy average.  Equation (3.4), rather
than a diagonal=`W` assertion, is what transfers the newly proved canonical
MSW first-shadow energy to an `o(W)` orbit floor.

## 4. The exceptional rows of a near-invariant factor form an invariant deck

### Exact congruence obstruction to full invariance

Assume now that `n=2m+1=p` is prime and let

\[
                         T={1\over p}\binom p m=\operatorname{Cat}_m.
\]

The Catalan row count has the exact residue

\[
 \boxed{
 T\equiv
 \begin{cases}
  2       &\pmod p,\qquad m\text{ even},\\
  p-2     &\pmod p,\qquad m\text{ odd}.
 \end{cases}}                                                   \tag{4.0}
\]

Indeed,

\[
 T={1\over m}\binom{p-1}{m-1}
   \equiv {(-1)^{m-1}\over m}\pmod p,
\]

and `m^{-1}=-2 mod p` because `2m=-1 mod p`.

There are exactly `(p-1)/2=m` geometric wreaths fixed by the coordinate
cycle `sigma`.  To see this, a fixed wreath must carry the order-`p`
action of `sigma` to an order-`p` automorphism of its supporting
`p`-cycle.  It is therefore an affine cyclic order

\[
                         a,a+d,a+2d,\ldots,a+(p-1)d,
\]

and the differences `d` and `-d` define the same geometric wreath.  This
gives `(p-1)/2` possibilities.

If a whole exact factor were `sigma`-invariant, all its nonfixed row
orbits would have size `p`.  If `f` is the number of fixed rows it uses,
then

\[
                         f\equiv T\pmod p,
 \qquad                         0\le f\le m.                    \tag{4.0a}
\]

Consequently:

\[
 \boxed{
 \begin{array}{ll}
  m\text{ odd}: & \text{no fully }\langle\sigma\rangle
                    \text{-invariant exact factor exists};\\
  m\text{ even}:& \text{any such factor must contain exactly two
                    fixed affine wreaths.}
 \end{array}}                                                   \tag{4.0b}
\]

The second line is only a necessary condition, not an existence theorem.
For the sample `m=11,p=23`, the residue `T mod p=21` is therefore not a
minor bookkeeping defect: full invariance is impossible, and a
near-invariant construction really must supply a nontrivial invariant-
support `21`-row deck.

### Lemma 4.1

Let `F=C dotcup R` be an exact middle factor, with both subfamilies middle
packings, and suppose `sigma C=C`.  Then the middle support of `R` is
`sigma`-invariant.

#### Proof

Exact ownership gives

\[
 B_m\mathbf1_R=\mathbf1-B_m\mathbf1_C.                          \tag{4.1}
\]

The all-one vector and `B_m 1_C` are `sigma`-invariant, so the right side
and hence the support of `R` are invariant.  \(\square\)

If `sigma` is a prime `n`-cycle and `|R|=r`, the packing `R` covers `rn`
middle targets.  Every nontrivial middle target orbit has size `n`.
Lemma 4.1 therefore says that `R` partitions exactly `r` complete target
necklaces.  It is an `r`-row deck with invariant **middle support**.  The
lemma does not by itself say that the row set `R` is permuted by `sigma`;
that stronger property needs a separate deck circuit.  What is forced,
and what already rules out an arbitrary patch, is the invariant union of
the `r` middle necklaces.

Thus writing

\[
                         |F|=an+r,qquad0\le r<n                \tag{4.2}
\]

does not leave `r` arbitrary rows.  The quotient construction requires

1. `a` complete row orbits whose quotient middle packets are disjoint; and
2. one invariant `r`-row deck covering the remaining `r` middle necklaces.

The second item is a genuine finite deck-design condition.  Fixed AP rows
may provide some singleton decks, but they need not supply the required
residue.  For example, when `n=23`, `Cat_11 mod 23=21`, whereas there are
only `(n-1)/2=11` AP packets up to reversal.

The `Q_7` factor is the model rather than an irrelevance: its AP row and
its nontrivial invariant four-row deck together resolve the row-count
residue.  The associated three-phase circuit demonstrates legal
within-necklace transport inside that deck.

It does not by itself prove that orbit mass is the only exact-fibre
invariant.  Coordinate copies of its first-shadow direction span the full
rational point-balanced rank-two module, but converting that signed span
into a positive, support-feasible family of simultaneous factor moves is a
separate theorem.  The circuit certifies nontrivial transport, not complete
reachability.

## 5. Correct quotient formulation

For a nonfixed row orbit `hat C`, its `n` rows contribute invariant middle
load.  It may occur in an exact factor core only if its middle packet is
transversal to target necklaces:

\[
                         a_C(O)\in\{0,1\}\quad\text{for every }O. \tag{5.1}
\]

Indeed the full row orbit contributes load `a_C(O)` to every target in
`O`, while the desired total load is one.  Such a row orbit becomes an
`n`-edge on the quotient set of `W/n=Cat_m` middle necklaces.  The
near-invariant middle problem is therefore an exact matching problem in
this **transversal row-orbit hypergraph**, together with the invariant
remainder deck of Section 4.

At depth `q`, a selected quotient edge carries the integer vector
`a_C^(q)(O)` on lower target necklaces.  The required quotient shadow
condition is

\[
 \#\left\{O:\sum_{\hat C\text{ selected}}a_C^{(q)}(O)=0\right\}
 =o(W/n)                                                        \tag{5.2}
\]

through the needed band, up to the polynomially small contribution of the
remainder deck.

Condition (5.2) is a legitimate smaller design problem.  It has not been
proved, and control only through `q=O(m^(1/4))` does not by itself control
the rest of a fixed Gaussian window: a further orbit-energy or surplus
theorem is needed there.

### The quotient overload is exactly self-similar

There is an exact way to see that quotienting reduces the finite instance
size but does not relax its asymptotic balancing parameter.  Suppose that
the depth-`q` load of a fully invariant family is constant with value
`k_O` on each target necklace `O`.  Put

\[
 \bar N_q=N_q/n,\qquad \sum_O k_O=W/n=T.
\]

Then

\[
 {T\over\bar N_q}={W\over N_q}=\lambda_q,
 \qquad
 \bar r_q:=T-c_q\bar N_q={r_q\over n}.                         \tag{5.3}
\]

In particular `r_q` is divisible by `n` whenever such an invariant load
exists.  Define the quotient lower and upper defects

\[
 \bar L_q=\sum_O(c_q-k_O)_+,
 \qquad
 \bar U_q=\sum_O(k_O-c_q-1)_+.
\]

Because every necklace has `n` phases, the physical defects are exactly

\[
                         L_q=n\bar L_q,
 \qquad                 U_q=n\bar U_q.
\]

The exact overload ledger therefore gives

\[
 \boxed{
 O_q(F)=n\,\bar O_q,
 \qquad
 \bar O_q:=\max\{\bar L_q,\bar U_q\}.}                         \tag{5.4}
\]

Consequently

\[
 \boxed{
 \sum_{q\le H}{O_q(F)\over c_q}=o(W)
 \quad\Longleftrightarrow\quad
 \sum_{q\le H}{\bar O_q\over c_q}=o(T).}                      \tag{5.5}
\]

Thus the invariant quotient problem is not merely reminiscent of MWB: at
the level of load arithmetic it is the same balanced-overload problem,
with `W,N_q` divided by `n` and the mean occupancy unchanged.  Any gain
must come from additional algebraic structure of the transversal
row-orbit catalogue, not from quotienting itself.

In fact the familiar `m^(1/4)` crossover belongs to the **noninvariant**
prime-smoothing argument.  There it comes from summing `n` approximately
decorrelated phase loads, whose fluctuation scale is `sqrt(n)`.  For an
invariant core the `n` phase loads on one necklace are identical, so the
quotient load itself has mean `lambda_q=1+O(q^2/m)` and receives no
`sqrt(n)` averaging gain.  An iid-like quotient would retain a constant
zero fraction throughout `q=o(sqrt(m))`.  Thus invariance does not make the
tail beyond `m^(1/4)` automatic; it removes exactly the fluctuation mechanism
which created that crossover.

## 6. Current consequence

### Lemma 6.1 (orbit mass is not phase balance)

Let `O={S,sigma S,...,sigma^(n-1)S}` be a nontrivial target necklace and
let `mu` be the load vector of an arbitrary, not necessarily
`sigma`-invariant, factor.  Knowledge of the single orbit mass

\[
                         M_O=\sum_{T\in O}\mu(T)                 \tag{6.2}
\]

does not bound the number of holes in `O`.  This remains true even at the
perfect mean: the two nonnegative integral vectors

\[
 (1,1,\ldots,1),\qquad(n,0,\ldots,0)                            \tag{6.3}
\]

both have orbit mass `n`, while their hole counts are respectively zero
and `n-1`.

If the factor itself is `sigma`-invariant, then its load vector is
constant on every target necklace, and (6.2) does determine all phase
loads.  Without that invariance, small orbit-mass discrepancy controls
only the orthogonal projection

\[
 \Pi_\sigma\mu={1\over n}\sum_{j=0}^{n-1}\sigma^j\mu,           \tag{6.4}
\]

not the within-necklace component `(I-Pi_sigma)mu`.

Consequently, a favorable prime cycle obtained from the canonical MSW
pair energy is not by itself a balanced single factor.  It certifies that
the **average of the `n` phase copies** has good orbit masses.  Passing
from those `n` copies to one integral factor still requires a positive
phase-lift/deck circuit which transports load inside target necklaces
while preserving exact middle ownership.  Randomized MSW pair-energy
control cannot silently replace that step.

#### Proof

The example (6.3) proves the first assertion.  Equation (6.4) is constant
on `O` with value `M_O/n`, while its orthogonal complement records all
phase fluctuations.  Invariance is exactly the vanishing of that
orthogonal complement. \(\square\)

The near-invariant quotient route and the low-energy row-lift route are
two distinct live strategies.

* Quotient route: solve the transversal quotient matching, the invariant
  residue deck, and the lower-orbit covering condition (5.2).
* Lift route: use the canonical MSW physical energy (now proved at depth
  one), select a favorable prime cycle, and realize its orbit-mass
  transports through legal row circuits.

Invariant factors attain the best load allowed by their own orbit masses,
but this fact does not manufacture the right orbit masses or the required
middle factor.  It therefore does not subsume the genuine deck-circuit
program.

There is a useful relaxation.  Because the final OR construction may
literalize an `o(W)` middle leave, one may select only complete row orbits
and stop with `o(W/n)` uncovered middle necklaces.  This avoids the residue
deck of Lemma 4.1.  It does **not** avoid the shadow-design gate: on the
quotient there are `N_q/n` depth-`q` target classes, each selected row orbit
supplies total quotient mass `n`, and the mean load is again

\[
                         {W\over N_q}=\lambda_q.                  \tag{6.1}
\]

Thus an iid-like quotient matching has the same constant zero fraction for
every `q=o(sqrt(m))`.  Dividing the ambient instance by `n` improves its
finite size but does not change the near-rainbow occupancy parameters or
the growing-band obstruction.
