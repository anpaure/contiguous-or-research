# Erased-parity census and Gaussian capacity cuts for affine parity-complete lifts

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The affine parity-complete family in
`MATH_THEOREM_DOUBLE_FACTOR_AFFINE_PARITY_COMPLETE_MAPPING_20260726.md`
does not make its completed-pair support encode the erased parity context.
It has the opposite exact law: the support and erased parity are
independent.

Let `p` be uniform on the even shore of `Q_r`, let `x` be uniform on
`Q_r`, and put

\[
                         y=Sp\oplus x.                \tag{0.1}
\]

For the affine family

\[
 d_p(x)=\delta_0(Sp\oplus x),
 \qquad
 F_p(x)=x\oplus e_{d_p(x)},                           \tag{0.2}
\]

the completed support at coarse depth `d` is

\[
 \boxed{
 J_{p,d}(x)=J_d^{G_0}(y).}                            \tag{0.3}
\]

The variables `p` and `y` are independent and uniform on their respective
spaces.  Consequently, if `A\subsetneq[r]`, `|A|=d`, and

\[
 \nu_d(A)=2^{-r}|\{y:J_d^{G_0}(y)=A\}|,              \tag{0.4}
\]

then for every `u\in Q_A`,

\[
 \boxed{
 \Pr(J=A,\ p_A=u)=\nu_d(A)2^{-d}.}                   \tag{0.5}
\]

Thus, for `d<r`,

\[
                         H(p_J\mid J)=d.              \tag{0.6}
\]

The support `J` carries exactly zero information about the `d` erased
parity bits.

The outside code can recover some of those bits only when `S` moves them
across the boundary of `J`.  Put

\[
                         K_S(J)=J\cap S^{-1}J.        \tag{0.7}
\]

Every code fibre of

\[
 \mathcal C_d(p,x)=
 \bigl(J_{p,d}(x),x|_{J^c},p|_{J^c}\bigr)            \tag{0.8}
\]

has multiplicity at least

\[
 \boxed{
 2^{\max(|K_S(J)|-1,0)}.}                            \tag{0.9}
\]

For the actual finite seed, `S=(2\ 4)`.  Every `d`-set satisfies

\[
                         |K_S(J)|\ge d-1,             \tag{0.10}
\]

so every aligned trace at `d\ge2` has multiplicity at least

\[
 \boxed{2^{d-2}.}                                    \tag{0.11}
\]

At Gaussian completed depth `d=\Theta(\sqrt m)`, this is exponential in
`\sqrt m`.  The affine `Q_4` seed and every recursion retaining a
near-identity context permutation therefore fail the trace-code gate
before any outer Hall problem is reached.

There is also a construction-independent output-capacity cut.  Any
aligned code of the form (0.8), for arbitrary context-dependent factors,
has at most

\[
                         \binom rd2^{2(r-d)}          \tag{0.12}
\]

possible values, while the even-time start set has size `2^{2r-1}`.
Hence its cap-one collision excess is at least

\[
 \boxed{
 \left[
  1-{2\binom rd\over4^d}
 \right]_+2^{2r-1}.}                                 \tag{0.13}
\]

In particular, at the natural half-depth `d=r/2`,

\[
 {2\binom r{r/2}\over2^r}=O(r^{-1/2}),              \tag{0.14}
\]

so a `1-O(r^{-1/2})` fraction of all starts is unavoidable collision
excess.  More generally the obstruction is exponentially strong whenever
`d/r` tends to a constant larger than `1/2`.

Therefore no near-injective choice exists for the current affine family,
and no parity-complete construction can be near-injective through aligned
half-depth.  Below half-depth, an affine construction could evade the
displayed kernel only if almost every completed support is essentially
`S`-transversal:

\[
 \Pr\bigl(|J_d\cap S^{-1}J_d|\ge2\bigr)=o(1).         \tag{0.15}
\]

The bounded-support affine seed does not have this property.  A growing
affine successor must either have it or fail already at the kernel level.

The finite-field syndrome bank gives the complementary obstruction.  It
can make `J\cap S^{-1}J` empty, but at depth `d` it has only `r-1`
long-sector supports.  If `r=2^s` and `d\ge s`, then every nonempty
long-sector code fibre has the exact size

\[
                         2^{2d-s-1}={4^d\over2r}.     \tag{0.16}
\]

More generally, if a construction quarantines `\varepsilon N` starts,
chooses among `L` algebraic orders on the remainder, and the union of
their depth-`d` support catalogues has size at most `L(r-1)`, its
collision excess is at least

\[
 \boxed{
 \left[1-\varepsilon-{2L(r-1)\over4^d}\right]_+
 2^{2r-1}.}                                          \tag{0.17}
\]

Consequently, at `d=A\sqrt m` with `r,L\le m^{O(1)}`, a polynomial
algebraic catalogue with `\varepsilon=o(1)` has collision fraction at
least `1-o(1)-\exp\{-2A(\log2)\sqrt m+O(\log m)\}`.  For one fixed
syndrome order, `\varepsilon=1/r`, and conditional on its long sector the
fraction is `1-\exp(-\Theta(\sqrt m))`.  Eliminating the overlap kernel is
therefore not enough: a Gaussian-depth construction needs exponentially
many physically distinct completed-support labels.

## 1. Exact affine evolution

Let `G_0` be a neighbor permutation of `Q_r` with direction function
`\delta_0`.  In the double-factor construction, for every even context
`p`,

\[
                         Sp\oplus F_p(x)=G_0(Sp\oplus x).           \tag{1.1}
\]

Iterating gives

\[
                         Sp\oplus F_p^t(x)=G_0^t(y),                \tag{1.2}
\]

where `y=Sp\oplus x`.  Therefore

\[
 d_p(F_p^t x)=\delta_0(G_0^t y).                     \tag{1.3}
\]

Taking the first `d` distinct coarse directions proves (0.3).

The map

\[
                         (p,x)\longmapsto(p,y)        \tag{1.4}
\]

is a bijection from `Q_r^{\rm even}\times Q_r` to itself.  Hence `p` is
uniform even, `y` is uniform, and the two are independent.

### Theorem 1.1 (joint support/parity law)

For `d<r`, conditional on `J=A`, the erased word `p_A` is uniform on all
`2^d` words and independent of every statistic of `y`.  Equivalently,
(0.5) holds.

For `d=r`, the support is `[r]` and `p_J` is uniform on the even words,
with mass `2^{-(r-1)}` each.

#### Proof

The event `J=A` is a function of `y` alone.  For `d<r`, every prescribed
word `u\in Q_A` has exactly

\[
                         2^{r-d-1}                    \tag{1.5}
\]

even completions on `A^c`.  Division by `|Q_r^{\rm even}|=2^{r-1}`
gives probability `2^{-d}`.  Independence of `p` and `y` completes the
proof.  The full-support case is immediate from the definition of the
even shore.  \(\square\)

This theorem applies unchanged when `G_0` is algebraic, recursive, or a
nonlinear cycle factor.  Only the affine context form (0.2) is used.

## 1.5 Exact census for the finite-field syndrome bank

Let `r=2^s`, index the coordinates by
`\mathbb F=\mathbb F_{2^s}`, and use the construction

\[
 \Sigma(y)=\sum_{z\in\mathbb F}y_z z,
 \qquad
 G_c(y)=y\oplus e_{c\Sigma(y)},                      \tag{1.6}
\]

where `g=1+c` is primitive.  For a fixed admissible multiplier `a`, put

\[
                         y=P_ap\oplus x.             \tag{1.7}
\]

The change `(p,x)\mapsto(p,y)` is again a bijection.  In particular,
`p` is uniform even, `y` is uniform, and `u=\Sigma(y)` is uniform on
`\mathbb F` and independent of `p`.

For `u\ne0` and `1\le d<r-1`, the completed support is

\[
 J_d(u)=cu\{1,g,\ldots,g^{d-1}\}.                   \tag{1.8}
\]

These `r-1` supports are distinct.  If `A=J_d(u)` and `v\in Q_A`, then
Theorem 1.1 specializes to the exact law

\[
 \boxed{
 \Pr(J=A,\ p_A=v)={1\over r\,2^d}.}                 \tag{1.9}
\]

Conditioned on the nonzero-syndrome sector, the right side is
`1/((r-1)2^d)`.  The remaining `1/r` of the starts have `u=0`; there the
direction `0` repeats and the component is a `C_2`, so it is not an
isometric depth-`d` packet when `d\ge2` and must be quarantined.

The joint law (1.9) says that the algebraic support is a perfect label for
the syndrome `u`, but contains no bit of the erased parity word.

### Theorem 1.2 (exact outside-code fibres in the long sector)

Assume `s\le d<r-1`.  For every long-sector support `J=J_d(u)` and every
pair of outside words

\[
                         v\in Q_{J^c},\qquad w\in Q_{J^c},          \tag{1.10}
\]

the code `(J,p|_{J^c},x|_{J^c})=(J,v,w)` has exactly

\[
                         2^{2d-s-1}                 \tag{1.11}
\]

preimages `(p,x)`.

Equivalently, under a uniform even-time start the full joint law is

\[
 \boxed{
 \Pr\bigl(J=A,\ p|_{A^c}=v,\ x|_{A^c}=w\bigr)
 ={1\over r\,4^{r-d}}}                               \tag{1.12}
\]

for every one of the `r-1` long supports and every pair of outside
words.  Conditional on the long sector, replace `r` by `r-1`.

#### Proof

Fix `J`, hence fix its unique nonzero syndrome `u`.  Choose the erased
word `p_J` subject only to the global even-parity equation.  There are
`2^{d-1}` choices.  Once `p` and `x|_{J^c}=w` are fixed, equation (1.7)
fixes `y|_{J^c}`.  It remains to choose `y_J` so that
`\Sigma(y)=u`.

The `d` labels in (1.8) contain the `s` consecutive powers
`cu, cug,\ldots,cug^{s-1}`.  Since the minimal polynomial of the primitive
element `g` has degree `s`, these form an `\mathbb F_2`-basis of
`\mathbb F`.  Therefore the map

\[
 Q_J\longrightarrow\mathbb F,
 \qquad z\longmapsto\sum_{j\in J}z_jj                \tag{1.13}
\]

has rank `s`, and every required syndrome has exactly `2^{d-s}`
preimages.  Multiplying the independent counts gives
`2^{d-1}2^{d-s}=2^{2d-s-1}`.  Conversely every such choice reconstructs
one `y`, hence one `x=y\oplus P_ap`, with exactly the prescribed code.
\(\square\)

This theorem is independent of the multiplier `a`.  In particular, the
overlap-free choices from the syndrome bank remove the subgroup in
Theorem 2.1 but do not change the exact information deficit (1.11).
Indeed all choices of `a` use the same `r-1` supports in (1.8); mixing
only these multipliers does not enlarge the support catalogue at all.

## 2. The exact invisible-parity kernel

Fix a start `(p,x)` and put `y=Sp\oplus x` and `J=J_d^{G_0}(y)`.  Define

\[
 \mathcal H_S(J)=
 \{h\in Q_r:
   \operatorname {supp}(h)\subseteq J\cap S^{-1}J,
   \ |h|\equiv0\pmod2\}.                             \tag{2.1}
\]

For `h\in\mathcal H_S(J)`, put

\[
                         p'=p\oplus h,
 \qquad
                         x'=x\oplus Sh.              \tag{2.2}
\]

Then `p'` is even and

\[
 Sp'\oplus x'
 =Sp\oplus Sh\oplus x\oplus Sh
 =y.                                                  \tag{2.3}
\]

Thus the completed support remains `J`.  Since `h` is supported in `J`,

\[
                         p'|_{J^c}=p|_{J^c}.          \tag{2.4}
\]

Since `h` is also supported in `S^{-1}J`, the vector `Sh` is supported in
`J`, and hence

\[
                         x'|_{J^c}=x|_{J^c}.          \tag{2.5}
\]

Every member of `\mathcal H_S(J)` therefore gives the same code (0.8).
For an aligned window this is also the same raw physical trace: every
coordinate in a completed pair takes both binary values, so the lower
trace is empty and the upper trace is full on `J`; every coordinate in
`J^c` is constant and is reconstructed bijectively from
`(x|_{J^c},p|_{J^c})`.  Thus code fibres and aligned physical-trace fibres
are identical, rather than one merely projecting onto the other.

### Theorem 2.1 (affine fibre lower bound)

Let `k=|J\cap S^{-1}J|`.  Then

\[
 |\mathcal H_S(J)|=
 \begin{cases}
 1,&k=0,\\
 2^{k-1},&k\ge1.
 \end{cases}                                         \tag{2.6}
\]

Consequently every code fibre over support `J` has at least the
multiplicity in (0.9).

#### Proof

On a `k`-element coordinate set, the even-weight vectors form a subspace
of dimension `k-1` when `k\ge1`.  The case `k=0` contains only the zero
vector.  Equations (2.2)--(2.5) inject this subspace into one code fibre.
\(\square\)

### Corollary 2.2 (the current transposition seed fails)

For `S=(2\ 4)`, if `J` contains exactly one of `2,4`, then

\[
                         |J\cap S^{-1}J|=d-1.         \tag{2.7}
\]

If it contains both or neither, the intersection has size `d`.  Hence
(0.10)--(0.11) hold for every support, not merely on average.

If `N=2^{2r-1}` is the number of even-time starts, the number of distinct
codes is at most `N/2^{d-2}`.  Therefore the cap-one collision excess is
at least

\[
                         (1-2^{2-d})N.                \tag{2.8}
\]

The same conclusion applies to any context permutation `S` which moves
at most `t` coordinates: then

\[
 |J\cap S^{-1}J|\ge d-t,                             \tag{2.9}
\]

and every fibre has size at least `2^{d-t-1}` when `d>t`.

## 3. The universal output-capacity cut

Now allow arbitrary parity-complete factors `F_p`; no affine form is
assumed.  If every coarse cycle is isometric, an aligned completed depth
`d\le r` has a `d`-element support `J`.  The code records:

1. one of at most `\binom rd` supports;
2. an outside phase word of length `r-d`; and
3. an outside parity word of length `r-d`.

Thus the code range has size at most (0.12).  Since the domain has size
`N=2^{2r-1}`, the number of collisions beyond the first representative of
each code is at least

\[
 N-\binom rd2^{2(r-d)}
 =\left(1-{2\binom rd\over4^d}\right)N,              \tag{3.1}
\]

whenever the right side is positive.  This proves (0.13).

At `d=r/2`, the central-binomial estimate gives

\[
 \binom r{r/2}
 =\left(\sqrt{2\over\pi r}+o(r^{-1/2})\right)2^r.    \tag{3.2}
\]

Substitution proves (0.14).  If `d/r\to\alpha>1/2`, Stirling gives

\[
 \log_2{2\binom rd\over4^d}
 =r\bigl(H_2(\alpha)-2\alpha\bigr)+o(r),             \tag{3.3}
\]

and `H_2(\alpha)<2\alpha`, proving exponential decay.

For `\alpha<1/2`, the raw output alphabet is large enough and this
particular capacity cut disappears.  That does not prove injectivity; it
only leaves room for a support-erasure construction.

### Theorem 3.1 (support-catalogue cut)

Let `\Omega_d` be a set of starts on which depth `d` completes `d`
distinct pairs, let `Q=N-|\Omega_d|`, let `\mathscr J_d` be the collection
of supports realized there, and put `R_d=|\mathscr J_d|`.  Even if the
rule selecting an order is allowed to depend arbitrarily on the start,
the aligned trace-code range on `\Omega_d` has size at most

\[
                         R_d\,2^{2(r-d)}.             \tag{3.4}
\]

Consequently, with `N=2^{2r-1}`, its collision excess is at least

\[
 \boxed{
 \left[1-{Q\over N}-{2R_d\over4^d}\right]_+N.}      \tag{3.5}
\]

#### Proof

For each realized support, the two outside words have `r-d` bits each,
so (3.4) is an exhaustive count of the output alphabet on `\Omega_d`.
Keeping at most one start per output leaves at most (3.4) starts.  Its
collision excess is therefore at least
`|\Omega_d|-R_d\,2^{2(r-d)}`, which is (3.5).
\(\square\)

If the construction selects among `L` finite-field syndrome catalogues,
then `R_d\le L(r-1)`.  For one fixed order the zero-syndrome quarantine
has `Q=N/r`; in general put `\varepsilon=Q/N`.  Equation (3.5) then gives
(0.17).  In particular, for
`d=A\sqrt m` and `r,L\le m^C`,

\[
 {2R_d\over4^d}
 \le
 \exp\{-2A(\log 2)\sqrt m+O(\log m)\}.              \tag{3.6}
\]

Thus the collision fraction is at least
`1-\varepsilon-\exp\{-2A(\log2)\sqrt m+O(\log m)\}`.  For one syndrome
order and `d\ge s`, Theorem 1.2 attains the catalogue count exactly on the
long sector: every used code has degree `4^d/(2r)`.

## 4. Exact escape conditions below half-depth

For an affine double factor, Theorem 2.1 shows that cap-one collision
excess can be `o(2^{2r})` only if

\[
 \Pr_y\bigl(|J_d^{G_0}(y)\cap S^{-1}J_d^{G_0}(y)|\ge2\bigr)=o(1).  \tag{4.1}
\]

Indeed every start over such a support belongs to a fibre of size at least
two, so a positive probability of these supports gives linear collision
excess.

Condition (4.1) says that the direction supports must be almost
transversals of the context permutation.  A near-identity `S` cannot do
this by (2.9).  For a uniformly distributed `d`-set and a fixed
fixed-point-free permutation, linearity of expectation gives the exact
overlap mean

\[
 \mathbb E|J\cap S^{-1}J|
 ={d(d-1)\over r-1}.                                 \tag{4.2}
\]

Thus uniform-looking supports do not even have vanishing expected overlap
unless `r\gg d^2`.  At Gaussian `d=\Theta(\sqrt m)` with `r\le m`, this
scale is not little-oh.  This expectation alone is not a probability
obstruction to (4.1), but it explains why a positive construction needs
deliberately `S`-transversal supports rather than mere marginal
uniformity.  The syndrome intervals do achieve transversality, and
Theorem 1.2 shows that the independent support-entropy obstruction then
survives exactly.

Even if (4.1) is achieved, it is only a necessary condition.  The support
alphabet must also satisfy

\[
 |\operatorname {range}(J_d)|
 \ge(1-o(1))2^{2d-1},                                \tag{4.3}
\]

which follows by dividing the required code range by the
`2^{2(r-d)}` outside words.  Finally, the remaining outside equations must
actually recover both `y` and the boundary-crossing parity bits.

The current `Q_4` affine seed fails (4.1) maximally.  A recursive successor
must therefore change the context permutation at growing scale and prove,
simultaneously:

1. the same-vertex direction relation needed for parity completeness;
2. almost `S`-transversal completed supports at every protected depth;
3. the support entropy bound (4.3); and
4. two-sided recovery from `(J,x_{J^c},p_{J^c})`.

No recursion audited here meets these four conditions.  The exact proved
conclusion is stronger than the bounded-seed kernel obstruction:

* every globally affine recursion has the independent joint law (0.5);
* bounded-motion context permutations have the Gaussian fibre lower bound
  (0.9)--(0.11);
* the overlap-free finite-field bank has the exact uniform fibre law
  (1.11)--(1.12); and
* every polynomial support catalogue has the Gaussian collision cut
  (0.17) and (3.6).

A genuinely nonaffine recursive direction array is not ruled out.  It
must, however, create at least `(1-o(1))2^{2d-1}` physically distinct
depth-`d` supports while still satisfying the pointwise parity-complete
matching equations and whole-cycle constraints.  That exponential
support-hash theorem is the remaining construction target.
