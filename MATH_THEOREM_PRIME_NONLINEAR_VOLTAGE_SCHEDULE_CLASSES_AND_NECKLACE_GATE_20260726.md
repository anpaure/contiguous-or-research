# Nonlinear prime voltage schedules: midpoint inversion, algebraic class obstructions, and the necklace gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
                         p=2m+1\equiv1\pmod4                     \tag{0.1}
\]

be prime.  The local nonlinear voltage problem has an exact positive
solution after changing variables from the voltage word to the omitted
coordinate word.

Write `E f(i)=f(i+1)` on functions `F_p -> F_p`.  If `z` is any
permutation of `F_p`, the cyclic equation

\[
                         (I+E)s=2z                               \tag{0.2}
\]

has a unique solution, because `-1` is not an eigenvalue of a cyclic
shift of odd order.  Put

\[
                         y={Es-s\over2}.                         \tag{0.3}
\]

Then

\[
 s_{i+1}=s_i+2y_i,\qquad z_i=s_i+y_i,\qquad
 \sum_i y_i=0,\qquad\sum_i i y_i=0.                \tag{0.4}
\]

Thus every omitted-coordinate permutation produces an exact zero-voltage
schedule satisfying all midpoint and linear moment equations.  The
remaining condition for a **free** quotient `p`-cycle is precisely that
its `p` middle every-second windows lie in distinct translation necklaces.

This yields a large nonlinear free-cycle family.  For every fixed `A` and
`H<=A sqrt(m)`, all but `exp(-Omega_A(m))` of the `p!` omitted-coordinate
permutations are simultaneously translation-rainbow at every depth
`0<=q<=H`.  Hence there are at least

\[
              (1-e^{-\Omega_A(m)}){p!\over2p^2}                 \tag{0.5}
\]

distinct simple zero-voltage quotient cycles with simultaneous shallow
literal trace injectivity.  Every one has a nonlinear voltage schedule;
an affine voltage cannot produce a free cycle.

The theorem supplies an exponentially large free catalogue, but not a
difference-family partition of all middle necklaces.  Several compact
algebraic subclasses are rigorously excluded.

1. Every nonaffine Möbius permutation of `F_p`, with its pole patched by
   the projective value at infinity, violates `sum i y_i=0`.
2. Every odd voltage function `y(-i)=-y(i)` gives an even midpoint word
   `z(-i)=z(i)` and therefore cannot work.  In particular every monomial
   permutation-polynomial voltage `a i^d` is impossible.
3. An ordinary orthomorphism automatically satisfies the two linear
   moment equations, but it does not imply midpoint permutation.  Every
   odd orthomorphism is excluded by Item 2.  The surviving object is a
   non-odd orthomorphism lying in the additional nonlinear permutation
   constraint `M y in Sym(F_p)`, where `M` is the midpoint transform.
4. A degree-`d` polynomial voltage class contains at most `p^(d+1)`
   schedules.  Since a factor needs `(Cat_m-2)/p` free cycles, any complete
   polynomial catalogue must have

   \[
               d\ge {p\log2\over\log p}-O(1).                  \tag{0.6}
   \]

   Thus bounded-degree permutation polynomials, Möbius families, and any
   fixed-parameter orthomorphism family are too small even before
   disjointness or shadows are imposed.

At shallow ranks, the local family is stronger than needed: one good
cycle has no repeated target necklace through `H`.  The global problem is
opposite.  At depth one the mean load is only `1+2/m`; an integral factor
with `o(T)` holes must therefore be a near-injection across **different**
cycles.  Independent or uncorrelated cycle selection has a linear missing
mass.  The surviving theorem is an integral, highly correlated
difference-family selection from the nonlinear catalogue, simultaneously
at all protected depths.

## 1. Exact midpoint inversion

Consider a labelled quotient walk with voltage labels

\[
                         y=(y_i)_{i\in\mathbb F_p}.               \tag{1.1}
\]

Let `s_i` be the translation phase of its lifted vertex and `z_i` the
coordinate omitted by its `i`-th physical edge.  The exact relations are

\[
 s_{i+1}-s_i=2y_i,
 \qquad
 z_i=s_i+y_i={s_i+s_{i+1}\over2}.                 \tag{1.2}
\]

The usual direction derives `z` from `y`.  For nonlinear construction the
reverse direction is cleaner.

### Theorem 1.1 (midpoint inversion theorem)

For every function `z:F_p -> F_p`, there is a unique cyclic phase word
`s` satisfying

\[
                         s_i+s_{i+1}=2z_i.                         \tag{1.3}
\]

It is given explicitly by

\[
 \boxed{
 s_i=\sum_{r=0}^{p-1}(-1)^r z_{i+r},
 \qquad
 y_i=z_i-s_i.}                                                   \tag{1.4}
\]

The resulting voltage word satisfies

\[
                         \sum_i y_i=0.                            \tag{1.5}
\]

If `z` is a permutation, then also

\[
                         \sum_i i y_i=0.                          \tag{1.6}
\]

Conversely, every zero-voltage schedule whose omitted word is `z` is
given by (1.4).

#### Proof

Iterating `s_(i+1)=2z_i-s_i` for `p` steps gives

\[
 s_{i+p}=-s_i+2\sum_{r=0}^{p-1}(-1)^r z_{i+r}.       \tag{1.7}
\]

Since `s_(i+p)=s_i`, (1.4) follows.  It also directly satisfies (1.3),
and uniqueness follows because a solution of `h_(i+1)=-h_i` on an odd
cycle has `h_i=0`.

Equation (1.2) now holds with `y_i=z_i-s_i`.  Summing
`s_(i+1)-s_i=2y_i` proves (1.5).

If `z` is a permutation, then `sum_i z_i=0`.  Summing (1.3) gives
`sum_i s_i=sum_i z_i=0`.  Cyclic summation by parts gives

\[
 \sum_i i y_i
  ={1\over2}\sum_i i(s_{i+1}-s_i)
  =-{1\over2}\sum_i s_i=0,                         \tag{1.8}
\]

proving (1.6).  The last assertion is forced by (1.2). \(\square\)

Thus the omitted-permutation and zero-voltage equations are not competing
constraints.  They are one invertible change of variables.  Requiring the
voltage `y` itself to be a permutation polynomial is an additional ansatz,
not a physical necessity.

## 2. Free cycles are exactly translation-transversal permutations

For a permutation `z`, define the every-second windows

\[
 J_{i,r}(z)=
 \{z_{i+1},z_{i+3},\ldots,z_{i+2r-1}\},
 \qquad i\in\mathbb F_p.                              \tag{2.1}
\]

At the middle rank put `B_i=J_(i,m)(z)`.  The omitted-coordinate
reconstruction gives a physical wreath with middle vertices `B_i` in
odd-graph order.  Equations (1.2)--(1.5) show that its normalized quotient
walk has voltage zero.

Here is the literal normalization check.  Put

\[
                         b_i=\sum_{x\in B_i}x,
 \qquad                  \widetilde s_i=-2b_i.                   \tag{2.1a}
\]

Since `m^(-1)=-2`, the translate `A_i=B_i-\widetilde s_i` has sum zero.
The consecutive middle sets `B_i,B_(i+1)` are disjoint and together omit
exactly `z_i`; because `sum_x x=0`,

\[
 b_i+b_{i+1}=-z_i,
 \qquad
 \widetilde s_i+\widetilde s_{i+1}=2z_i.                         \tag{2.1b}
\]

Uniqueness in Theorem 1.1 gives `widetilde s=s`.  Thus the phase and
voltage reconstructed from the actual middle sets are exactly those in
(1.4), not merely a formal solution of the midpoint equations.

### Theorem 2.1 (exact freeness criterion)

The quotient walk obtained from `z` is a simple zero-voltage `p`-cycle if
and only if

\[
              [B_i]_\rho\ne[B_j]_\rho
              \qquad(i\ne j),                                  \tag{2.2}
\]

where brackets denote translation necklaces.  More generally its
depth-`q` lower targets are translation-rainbow if and only if

\[
 [J_{i,m-q}(z)]_\rho\ne[J_{j,m-q}(z)]_\rho
              \qquad(i\ne j).                                  \tag{2.3}
\]

#### Proof

The quotient vertex at phase `i` is exactly the translation necklace of
`B_i`; hence quotient simplicity is (2.2).  The same every-second-window
reconstruction gives (2.3).  Voltage zero was proved in Theorem 1.1.
\(\square\)

The AP orders are the opposite extreme: all middle windows belong to one
necklace and the quotient collapses to a loop.  A free schedule must
therefore be globally nonlinear in its phase chronology.

## 3. Abundance of nonlinear shallow-rainbow schedules

The freeness condition is generic in the complete permutation class.

### Lemma 3.1 (exact translate-collision probability)

Let `I,J` be distinct cyclic position intervals of equal size `k<=m`,
let `r=|I intersect J|`, and let `a` be nonzero.  For a uniformly random
permutation `z` of `F_p`,

\[
 \Pr\bigl(z(J)=z(I)+a\bigr)
        ={k-r\over k\binom{p-1}k}.                               \tag{3.1}
\]

#### Proof

Put `b=k-r`.  For a fixed image `X=z(I)`, the equality requires
`|X setminus (X+a)|=b`.  Along the single `a`-cycle on `F_p`, this says
that `X` has exactly `b` one-runs.  The cyclic run count is

\[
 {p\over b}\binom{k-1}{b-1}\binom{p-k-1}{b-1}.       \tag{3.2}
\]

For each such `X`, the four regions cut out by `I,J` can be bijected to
their forced image regions in

\[
                         r!\,b!^2\,(p-2k+r)!                     \tag{3.3}
\]

ways.  Divide the product of (3.2)--(3.3) by `p!` and cancel
factorials. \(\square\)

### Theorem 3.2 (large free nonlinear catalogue)

Let `H<=A sqrt(m)`.  The fraction of permutations `z` which fail (2.3)
for at least one `0<=q<=H` is at most

\[
 \epsilon_{p,H}
 \le { (H+1)p^2(p-1)\over\binom p{m-H}}
 =e^{-\Omega_A(m)}.                                  \tag{3.4}
\]

Consequently there are at least

\[
                (1-\epsilon_{p,H}){p!\over2p^2}                  \tag{3.5}
\]

distinct simple zero-voltage quotient cycles which are
translation-rainbow at every depth through `H`.

#### Proof

Sum (3.1) over two starts, their nonzero target translation, and all
cyclic separations.  For one rank this gives at most

\[
                         {p^2(p-1)\over\binom pk}                 \tag{3.6}
\]

expected ordered collisions.  The smallest binomial coefficient in the
displayed range occurs at `k=m-H`.  Markov's inequality and a union bound
prove (3.4).

One quotient cycle has at most `2p^2` labelled descriptions: `p` cyclic
position cuts, two orientations, and `p` common coordinate translations.
Dividing the good labelled permutations by this upper bound proves
(3.5). \(\square\)

The family in (3.5) is genuinely nonlinear.  An affine voltage schedule
cannot have a permutation midpoint word on a free quotient cycle; hence
the voltage obtained from any good `z` by (1.4) is nonaffine.  Equally,
every `z` has a unique interpolation polynomial of degree at most `p-1`,
and only `p(p-1)` permutation functions are affine.  Removing those leaves
the same asymptotic lower bound in (3.5).

This is an explicit defining family—permutations satisfying (2.3), with
voltage given by (1.4)—and an exponential existence theorem.  It is not
yet a closed-form low-parameter difference family.

## 4. Möbius schedules are completely obstructed

A nonaffine fractional-linear transformation does not itself permute the
finite affine line: it has one pole.  The canonical projective patch is
the most generous Möbius permutation ansatz.  It has the form

\[
 y(x)=
 \begin{cases}
  \alpha+\displaystyle{\beta\over x-r},&x\ne r,\\[2mm]
  \alpha,&x=r,
 \end{cases}
 \qquad \beta\ne0.                                  \tag{4.1}
\]

It is a permutation of `F_p`: the non-pole inputs cover
`F_p setminus {alpha}`, and the pole is sent to `alpha`.

### Theorem 4.1 (Möbius moment obstruction)

No schedule (4.1) has a permutation omitted word.

#### Proof

Theorem 1.1 shows that a permutation omitted word forces
`sum_x x y(x)=0`.  But

\[
\begin{aligned}
 \sum_xxy(x)
 &=\beta\sum_{x\ne r}{x\over x-r}\\
 &=\beta\sum_{t\ne0}\left(1+{r\over t}\right)
 =-\beta\ne0.                                        \tag{4.2}
\end{aligned}
\]

The constant part contributes zero, and `sum_(t ne 0)t^(-1)=0`.
This contradicts the necessary moment equation. \(\square\)

Every true Möbius permutation of the affine line fixes infinity and is
affine; that already belongs to the refuted affine class.  Thus (4.1)
closes the only nonaffine projective patch as well.

## 5. Odd and monomial permutation-polynomial schedules are obstructed

For a zero-sum voltage function `y`, let `z` be any midpoint word obtained
from a cyclic antiderivative.  From (1.2),

\[
                         z_{i+1}-z_i=y_i+y_{i+1}.                 \tag{5.1}
\]

### Theorem 5.1 (odd-voltage symmetry)

If

\[
                         y(-i)=-y(i)                             \tag{5.2}
\]

for all `i`, then

\[
                         z(-i)=z(i)                              \tag{5.3}
\]

for every midpoint word `z`.  Hence `z` is not a permutation for
`p>2`.

#### Proof

Put `w(i)=z(-i)`.  Equation (5.1) and oddness give

\[
\begin{aligned}
 w(i+1)-w(i)
 &=z(-i-1)-z(-i)\\
 &=-\bigl(y(-i-1)+y(-i)\bigr)
   =y(i+1)+y(i)\\
 &=z(i+1)-z(i).                                      \tag{5.4}
\end{aligned}
\]

Thus `w-z` is constant.  At `i=0` it is zero, proving (5.3).
\(\square\)

### Corollary 5.2 (monomial permutation-polynomial no-go)

No voltage schedule

\[
                         y(i)=a i^d,qquad a\ne0,                \tag{5.5}
\]

with `gcd(d,p-1)=1` has a permutation omitted word.

#### Proof

Since `p-1` is even, coprimality forces `d` odd.  Hence (5.2) holds,
and Theorem 5.1 applies. \(\square\)

This includes the patched inverse monomial `i^(p-2)` with `y(0)=0`.
Adding a constant destroys the odd symmetry and is not covered by this
corollary; such shifted high-degree permutation polynomials remain a
genuine subclass of the midpoint-permutation gate.

There is an exact polynomial form of that gate.  If `y` has reduced
degree `d<=p-2` and leading coefficient `a`, then (5.1) determines `z`
up to a constant and gives

\[
 \deg z=d+1,
 \qquad
 [x^{d+1}]z={2a\over d+1}.                         \tag{5.6}
\]

Indeed `z(x+1)-z(x)=y(x)+y(x+1)`; comparison of the degree-`d`
coefficients proves (5.6).  Hence a permutation-polynomial voltage ansatz
of degree at most `p-2` requires a pair of permutation polynomials of
consecutive degrees, linked by this difference equation.  Shifted
monomials and non-odd binomials are not ruled out merely by degree, but
must pass this much stronger paired-permutation test.

## 6. What ordinary orthomorphisms do and do not solve

Call `y:F_p -> F_p` an orthomorphism when both

\[
                         y(i),\qquad y(i)-i                        \tag{6.1}
\]

are permutations.

### Proposition 6.1 (orthomorphisms pass the linear voltage audit)

For `p>=5`, every orthomorphism satisfies

\[
                         \sum_i y(i)=0,qquad
                         \sum_i i y(i)=0.                         \tag{6.2}
\]

#### Proof

The first equality follows because `y` is a permutation.  Since `y` and
`y-id` are permutations and `sum_i i^2=0`,

\[
 0=\sum_i(y(i)-i)^2
   =\sum_i y(i)^2-2\sum_i i y(i)+\sum_i i^2
   =-2\sum_i i y(i).                              \tag{6.3}
\]

This proves the second equality. \(\square\)

Thus orthomorphisms evade the Möbius moment obstruction.  They do not,
however, solve the omitted-coordinate equation.  Define the cyclic
midpoint transform

\[
                         \mathcal M y=s+y,qquad
                         (E-I)s=2y.                                \tag{6.4}
\]

The antiderivative `s` is defined up to one additive constant.  This
translates `M y` by the same constant, so the assertion that `M y` is a
permutation is unambiguous.

The physical condition is the additional global constraint

\[
                         \mathcal M y\in\operatorname{Sym}(\mathbb F_p).
                                                                    \tag{6.5}
\]

Ordinary orthomorphism equations are pointwise Latin equations; (6.5) is
a cyclic antiderivative equation and does not follow from them.  Theorem
5.1 gives an exact subclass obstruction:

\[
 \boxed{
  y\text{ odd and orthomorphic}
  \quad\Longrightarrow\quad
  \mathcal M y\text{ is not a permutation}.}                     \tag{6.6}
\]

The surviving algebraic object is therefore a **non-odd midpoint
orthomorphism** satisfying all three permutation conditions

\[
             y,qquad y-id,qquad\mathcal M y
             \quad\hbox{are permutations}.                       \tag{6.7}
\]

Even (6.7) constructs only one legal voltage packet.  Freeness still
requires (2.2), and a factor requires exponentially many mutually
middle-disjoint packets.

## 7. Bounded-complexity algebraic families have insufficient capacity

Suppose every candidate voltage schedule is represented by a polynomial
of degree at most `d`.  There are at most

\[
                              p^{d+1}                             \tag{7.1}
\]

such functions, hence at most this many quotient cycles.  An invariant
exact factor requires

\[
                              {T-2\over p},
 \qquad T=\operatorname{Cat}_m,                                 \tag{7.2}
\]

free cycles.  Therefore a necessary counting condition is

\[
                         p^{d+1}\ge {T-2\over p}.                 \tag{7.3}
\]

Using

\[
                  \log T=p\log2-O(\log p)                       \tag{7.4}
\]

gives

\[
 \boxed{
                         d\ge {p\log2\over\log p}-O(1).}         \tag{7.5}
\]

More generally, a family described by `k` independent field parameters
has at most `p^k` members and requires

\[
                         k\ge {p\log2\over\log p}-O(1).          \tag{7.6}
\]

This rules out a complete factor supplied by one Möbius orbit, one fixed
orthomorphism orbit, any bounded-degree permutation-polynomial bank, or
any finite menu of such banks.  The obstruction is capacity, not local
voltage feasibility.  High-degree interpolation of the exponentially
large family in Theorem 3.2 is not affected.

## 8. Difference-family and shallow-necklace assessment

Let

\[
                         T=\operatorname{Cat}_m,qquad
             \overline N_q={1\over p}\binom p{m-q}.              \tag{8.1}
\]

An invariant exact factor consists of two AP loops and `(T-2)/p` free
quotient cycles whose middle vertex sets partition all remaining middle
necklaces.  For a selected free cycle `C`, let `a_(C,q)(O)` be the number
of its `p` depth-`q` occurrences with target necklace `O`.

The exact simultaneous selection problem is

\[
\begin{aligned}
 \sum_Cx_Cv_C+v_{L_1}+v_{L_2}&={\bf1}_{\mathcal N_m},\\
 k_q(O)=\sum_Cx_Ca_{C,q}(O)+a_{L_1,q}(O)+a_{L_2,q}(O),\\
 \sum_{q=1}^{H}\#\{O:k_q(O)=0\}&=o(T),
 \qquad x_C\in\{0,1\}.                            \tag{8.2}
\end{aligned}
\]

Theorem 3.2 shows that the catalogue can be restricted to cycles with

\[
                         a_{C,q}(O)\in\{0,1\}                    \tag{8.3}
\]

for every `q<=H`, losing only an exponentially small fraction of
candidates.  Hence within-cycle repeats are not the obstruction.

The first global row is already critical.  At `q=1`,

\[
 \lambda_1={T\over\overline N_1}={m+2\over m},
 \qquad
 T-\overline N_1={2T\over m+2}.                    \tag{8.4}
\]

Since `sum_O k_1(O)=T`, the exact repeat ledger is

\[
 \#\{O:k_1(O)=0\}
   =\sum_O(k_1(O)-1)_+-{2T\over m+2}.               \tag{8.5}
\]

Therefore `o(T)` first-shadow holes require

\[
 \sum_O(k_1(O)-1)_+
       ={2T\over m+2}+o(T)=o(T).                    \tag{8.6}
\]

So the chosen cycles must be almost mutually disjoint in their first
shadow colors, despite being selected primarily to partition their middle
vertices.  A midpoint orthomorphism controls the `p` colors inside one
cycle only; it gives no cross-cycle disjointness.

For comparison, `T` independent uniform placements into
`overline N_1=(1-o(1))T` boxes leave expected missing mass

\[
 \overline N_1\left(1-{1\over\overline N_1}\right)^T
       =(e^{-1}+o(1))T.                              \tag{8.7}
\]

Thus uncorrelated selection is off by a linear amount.  Equation (8.7)
is a benchmark, not a claim that the actual cycle catalogue is
independent.

At every fixed Gaussian depth `q=A sqrt(m)`, the mean tends to
`e^(A^2)`.  Random coverage still has a positive missing fraction for
fixed `A`; the simultaneous theorem must exploit a structured
difference-family correlation.  The two AP loops affect only two target
necklaces per depth and are asymptotically negligible.

## 9. Exact verdict

The prime nonlinear route now has a clean three-level answer.

1. **Individual schedules:** solved abundantly.  Midpoint inversion
   converts every omitted-coordinate permutation into an exact
   zero-voltage schedule, and almost every permutation gives a free,
   simultaneously shallow-rainbow quotient cycle.
2. **Compact algebraic templates:** obstructed in broad classes.
   Nonaffine Möbius voltages, odd voltages, and all monomial permutation
   voltages fail exactly.  Bounded-degree or bounded-parameter families
   are exponentially too small.  Non-odd midpoint orthomorphisms and
   shifted high-degree permutation polynomials remain locally possible.
3. **Difference-family selection:** open.  One must choose
   `(T-2)/p` cycles from the large nonlinear catalogue so that their
   middle supports partition exactly and their shallow target colors are
   globally near-disjoint at `q=1` and appropriately covering at all
   higher depths.

The surviving gate is not another voltage equation.  It is the integral
two-ledger difference-family problem (8.2).  Any positive theorem must use
an algebraic family with at least `exp(Omega(p))` distinct schedules, or an
equally rich recursive construction; no fixed Möbius, monomial, or
ordinary orthomorphism template has enough capacity.
