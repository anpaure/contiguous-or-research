# Three balanced SCD accumulators give the upper coefficient pi^2/8

Date: 2026-09-06. New supplemental research; Master is not modified.

## 1. Result

Let `W(k)=binom(k,floor(k/2))`, and let `nu(k)` be the shortest word of
nonempty subsets whose nonempty interval unions cover every nonempty subset
of `[k]`. Then

\[
 \boxed{\nu(k)\le\left({\pi^2\over8}+o(1)\right)W(k),\qquad
        {\pi^2\over8}=1.233700550136\ldots.}                 \tag{1}
\]

This is an unconditional constructive upper bound, not the terminal-rank
relaxation. In the notation of the two preceding coalescence notes,

\[
 \boxed{{2\over\sqrt e}\le R_*\le{\pi^2\over8}<1.24.}       \tag{2}
\]

The upper endpoint is proved analytically, without numerical quadrature.
It improves the previous diagnostic coefficient `c4 = 1.2673446...` by
approximately `0.03364`, rather than `0.00001`. The centered floor and the
coefficient-one problem are not attained.

There is also an explicit, if very large, fixed-block certificate. With
`m=2^30` equal blocks, the policy below has limiting coefficient

\[
                         Q_{2^{30}}<1.239825.             \tag{3}
\]

Thus even the strict improvement below `1.24` does not depend on an
unspecified favorable finite value of `m`.

Inputs: `GENERAL_D_BLOCK_AND_RECURSIVE_SCD_LIMITS_20260905_f6b82.md`,
`MULTIBLOCK_PARTITION_BARRIER_20260906_8b47c.md`, and Master A.5--A.6.
The pivot partition, product-SCD kernel, and global Euler compiler are
existing ingredients. The three-accumulator policy, its Brownian-clock
analysis, and the upper bounds (1)--(3) are the new contribution here.

## 2. The literal policy

Fix `m>=3` first. Split `mh` coordinates into `m` pivoted blocks, and take
a Boolean SCD on each block minus its pivot. For every initial chain tuple
and every signed complementary product pair, do the following.

1. Keep the first three factors in three labeled accumulator slots.
2. Read the remaining factors in the fixed order `4,5,...,m`. Merge the
   next factor into a currently shortest accumulator, using a complete
   hook product SCD. Retain the slot label. At each child, continue the
   same rule with the child's actual length. Break ties by slot label.
3. When no unread factor remains, merge the two shortest accumulators by
   one complete product SCD. Its children paired with the remaining
   accumulator are the terminal rectangles.
4. Globally Euler-assemble all terminal paired rectangles as in Section 8.

The next accumulator is chosen without consulting the unread factor's
length. This is not needed for the finite construction, but is important
for the independent-increment proof below. The rule uses chain lengths
only, not vector directions, sampled angles, or unobserved future data.

For integer lengths `a<=b<=c`, the final three-factor step has exact charge

\[
 \sum_{r=b-a+1,\,\mathrm{step}\,2}^{a+b-1}(r+c)
                         =ab+ac=a(b+c).                 \tag{4}
\]

After division by `abc`, its cost is exactly `1/b+1/c`. In particular,
the length of the smallest accumulator does not appear in this final
normalized cost. This removes the small-radius singularity that would
otherwise complicate a two-accumulator proof.

No factors are discarded or frozen permanently. Every unread factor is
consumed, every complete SCD child is kept, and every target has an owner.

## 3. Correct limiting normalization

The volume-biased initial length divided by `sqrt(h)` converges to

\[
 Z\sim\chi_3,\qquad
 g_Z(z)=\sqrt{2/\pi}\,z^2e^{-z^2/2},\quad z>0.
\]

At an integer merge the volume probabilities of the child lengths are
`r/(ab)`. Their mesh-two limit is

\[
                 K(a,b;dr)={r\over2ab}
                     {\bf1}_{|a-b|<r<a+b}\,dr.          \tag{5}
\]

Let `B_m<=A_m` be the two largest final accumulator radii when the rule in
Section 2 consumes `m` independent inputs `Z/sqrt(m)` with kernel (5).
Define the coefficient of this particular policy by `Q_m`, keeping it
distinct from the earlier notes' one-step partition constant `C_m`:

\[
       Q_m=\sqrt{\pi/8}\,\mathbb E(1/B_m+1/A_m).        \tag{6}
\]

For fixed `m`, the literal full-cube main charge has limiting ratio `Q_m`.
Here is a normalization check. If `P` is the finite principal charge and
the initial lengths are `a_1,...,a_m`, the signed products give

\[
 M=2^{mh-1}\,\mathbb E_{\rm volume}
                       {P(a_1,\ldots,a_m)\over\prod_i a_i}.
\]

The factor `2^{mh-1}/(sqrt(h) W(mh))` tends to `sqrt(pi*m/8)`.
Scaling the inputs additionally by `1/sqrt(m)` gives (6).

The usual fixed-`m` Riemann justification applies to this policy directly.
Its active state is a sorted triple; at a tie the two slot choices give
the same length multiset. Its continuum value is therefore continuous.
The bound

\[
       P(\mathbf a)\le\left(\prod_i a_i\right)\sum_i a_i^{-1}
                                                               \tag{7}
\]

gives polynomial domination under the unweighted SCD law. At a child
radius near zero, multiply the normalized integrand by its kernel factor
`r`, truncate `r<epsilon`, and use (7); the truncated contribution tends
to zero. On compact positive-radius sets the remaining sums are ordinary
Riemann sums. This proves the fixed-`m` limit, without assuming any rate
uniform in `m`. Section 8 pays the word's nonprincipal positions.

In particular `R_m<=Q_m`. It remains to prove the substantive upper-limit
claim

\[
                         Q_m\longrightarrow\pi^2/8.    \tag{8}
\]

## 4. Three independent Brownian clocks

Let `W_1,W_2,W_3` be independent standard three-dimensional Brownian
motions, each started at zero. Give each its own clock on the mesh
`{j/m:j>=0}`. Start all clocks at zero. At each of `m` updates, advance
the clock of a currently shortest-radius path by `1/m`. Ties are broken
by label. Only that path is observed at its new clock time.

The first three updates seed the three different paths, almost surely.
Afterward this is exactly the law in (6). Indeed each next unrevealed
vector increment is an independent `N(0,I_3/m)`. Its norm is `Z/sqrt(m)`;
conditionally on that norm and the current vector norm, its relative
cosine is uniform on `[-1,1]`. The resulting radius has kernel (5).
Adaptive choices of the clock do not expose any unobserved increment.

This coupling is an analysis of a volume-biased branch, not a randomized
word construction. The actual word construction retains all children.

For `a>=0`, put

\[
 \tau_i(a)=\inf\{t:|W_i(t)|=a\},\quad
 \sigma(a)=\sum_{i=1}^3\tau_i(a),\quad
 A=\sup\{a:\sigma(a)\le1\}.                            \tag{9}
\]

All hitting times are finite almost surely, and `sigma` is strictly
increasing and left-continuous, although it need not be right-continuous.
Left-continuity follows by taking increasing levels in a continuous path:
the limiting first-hit times must themselves hit the limiting level.
The generalized inverse in (9) is intentional. The following pathwise
argument, rather than an informal reflected-diffusion identification,
controls the limit.

Define

\[
 \omega_m=\max_{i\le3,\,0\le j<m}
  \sup_{j/m\le t\le(j+1)/m}|W_i(t)-W_i(j/m)|.
\]

Let `H_i` be the largest radius sampled on path `i` up to its allocated
clock time, and let `A_m,B_m` be the current largest and second largest
radii after all updates. There are three deterministic invariants:

\[
 \begin{split}
 &A_m\text{ is the global maximum of all sampled radii},\\
 &0\le A_m-B_m\le\omega_m,\\
 &A_m-\omega_m\le H_i\le A_m\quad(i=1,2,3).            \tag{10}
 \end{split}
\]

For the first invariant, updating a minimum cannot destroy the current
maximum. For the second, the new radius is at most the old minimum plus
`omega_m`, so it cannot create a larger top-two gap. For the last, consider
the update that first attained the final global maximum: its old minimum,
and hence every other current radius at that time, was at least
`A_m-omega_m`. Those historical maxima cannot be lost.

Every path has reached `(A_m-omega_m)_+` by its allocated clock time.
Before that time its continuous radius is at most `A_m+omega_m`, so it
has not reached `A_m+2omega_m`. Since the three allocated times sum to one,

\[
 \sigma((A_m-\omega_m)_+)\le1
                    <\sigma(A_m+2\omega_m).
\]

Consequently

\[
       A_m-\omega_m\le A\le A_m+2\omega_m,
       \qquad B_m,A_m\longrightarrow A\quad\hbox{a.s.} \tag{11}
\]

Uniform continuity of the three Brownian paths on `[0,1]` gives
`omega_m -> 0`. No interchange of an unbounded reciprocal with a weak
limit is made at this point.

## 5. Reciprocal tails and an explicit finite-m bound

Let `tau` be the first exit time from the unit ball by standard
three-dimensional Brownian motion started at zero, and let
`S=tau_1+tau_2+tau_3` for independent copies. Brownian scaling and (9) give

\[
                  1/A\ \overset{d}=\ \sqrt S,
             \qquad \mathbb E S=1.                    \tag{12}
\]

For example, left-continuity gives
`Pr(A<a)=Pr(sigma(a)>1)=Pr(S>1/a^2)`. The hitting time of a fixed positive
level has no time atoms: hitting exactly at time `t` entails a Gaussian
vector lying on the sphere at time `t`. Thus `S` and `A` have no atoms.

The elementary exit-time mean from a point `x` in the unit ball is
`(1-|x|^2)/3`, by stopping the martingale `|W_t|^2-3t`.
Markov's inequality and the Markov property, in time steps `2/3`, imply

\[
       \Pr(\tau\ge u)\le2^{-\lfloor3u/2\rfloor},\qquad
       \Pr(A\le r)\le3\,2^{-\lfloor1/(2r^2)\rfloor}.  \tag{13}
\]

Finiteness needed in the stopping argument also follows by first stopping
at `tau wedge t`: its squared radius is at most one, so
`3 E(tau wedge t)<=1`, and monotone convergence applies.

The reflection bound for one-dimensional Brownian motion, a union bound
over the nine coordinates and `m` mesh intervals, gives

\[
                  \Pr(\omega_m>\epsilon)
                     \le36m e^{-m\epsilon^2/6}.        \tag{14}
\]

The second largest current radius never decreases under minimum updates.
After the first three steps, the three radii are independent
`chi_3/sqrt(m)`. Since `E Z^{-2}=1`, this gives

\[
                         \mathbb E B_m^{-2}\le3m.      \tag{15}
\]

On `G={omega_m<=epsilon, A>6epsilon}`, (10)--(11) imply

\[
 \begin{split}
 {1\over B_m}+{1\over A_m}
 &\le {1\over A-3\epsilon}+{1\over A-2\epsilon}\\
 &\le {2\over A}+{10\epsilon\over A^2}.
 \end{split}
\]

On its complement use `1/B_m+1/A_m<=2/B_m` and Cauchy--Schwarz with
(13)--(15). Define

\[
 D_m(\epsilon)=36m e^{-m\epsilon^2/6}
                      +3\,2^{-\lfloor1/(72\epsilon^2)\rfloor}.
\]

We obtain the explicit estimate, valid for every `m>=3` and `epsilon>0`,

\[
 \boxed{Q_m\le\sqrt{\pi/8}
   \left(2\mathbb E\sqrt S+10\epsilon
                      +2\sqrt{3mD_m(\epsilon)}\right).} \tag{16}
\]

Taking `epsilon=m^(-1/4)` sends the last two terms to zero. Fatou's lemma
applied to the nonnegative reciprocals in (11) gives the reverse liminf.
Thus the expectations really converge, and

\[
          \lim_m Q_m=\sqrt{\pi/2}\,\mathbb E\sqrt S.   \tag{17}
\]

This proves the required uniform-integrability conclusion explicitly;
small-radius exceptional events have not been discarded without charge.

## 6. Exact evaluation

The exit-time Laplace transform is

\[
       \mathbb E e^{-s\tau}={\sqrt{2s}\over\sinh\sqrt{2s}}.
                                                               \tag{18}
\]

For completeness, the regular radial solution of
`u''/2+u'/r=s u`, with `u(1)=1`, is
`u(r)=sinh(r sqrt(2s))/(r sinh(sqrt(2s)))`. Its value at zero is (18).
Applying Ito's formula to the stopped bounded solution and then letting
the stopping time increase proves the transform identity. Its derivative
at zero also gives `E tau=1/3`.

For a nonnegative random variable `X`, Tonelli's theorem and integration
by parts give

\[
 \mathbb E\sqrt X={1\over2\sqrt\pi}
                   \int_0^\infty(1-\mathbb E e^{-sX})s^{-3/2}\,ds.
\]

Substitute (18) cubed, and set `x=sqrt(2s)`. The right side of (17) becomes

\[
 I=\int_0^\infty\left({1\over x^2}-{x\over\sinh^3x}\right)dx.
                                                               \tag{19}
\]

This integral has a short exact evaluation. Let

\[
 F(x)=-{1\over x}+{x\over2}\coth x\,\operatorname{csch}x
                          +{1\over2}\operatorname{csch}x.
\]

Direct differentiation gives

\[
 {1\over x^2}-{x\over\sinh^3x}
                         =F'(x)+{x\over2\sinh x}.
\]

Both endpoint limits of `F` are zero. Therefore

\[
 I={1\over2}\int_0^\infty{x\over\sinh x}\,dx
   =\sum_{j=0}^\infty{1\over(2j+1)^2}
   ={\pi^2\over8}.                                     \tag{20}
\]

The series expansion of `1/sinh x` has nonnegative terms, so its integral
interchange uses Tonelli. Equations (17)--(20) prove (8). Nothing in this
upper evaluation uses the threshold-dual lower bound.

## 7. A fixed-m certificate below 1.24

Choose `m=2^30`, `epsilon=2^-10` in (16). Since `e>2`,

\[
 36m e^{-m\epsilon^2/6}<2^{-134},\qquad
 3\,2^{-\lfloor1/(72\epsilon^2)\rfloor}
                         =3\,2^{-14563},
\]

so `D_m(epsilon)<2^-133` and
`2 sqrt(3mD_m(epsilon))<2^-49`. Exact Machin-series bounds for `pi`,
checked in the accompanying script, give

\[
 {\pi^2\over8}<{1233701\over10^6},\qquad
 \sqrt{\pi/8}<{627\over1000}.
\]

Consequently

\[
 Q_{2^{30}}< {1233701\over10^6}+{627\over102400}+2^{-49}
                        <1.239825.                     \tag{21}
\]

This is an analytic finite-policy bound; it is not a simulation with
`2^30` factors, and no numerical computation of a billion-dimensional
integral is required. Its block count is not asserted to be efficient.

## 8. Literal compiler and all dimensions

Here is the full accounting, including the parts for which a separate
linearization of each terminal rectangle would lose a leading constant.

Fix a pivot in every block. In each tuple take `2^(m-1)` sign patterns,
with the first sign positive, and pair each signed product with its full
complement. The first pivot determines global complementation, the other
pivots determine the signs, and the nonpivot SCDs determine ownership.
The pairs partition the cube. Complete product SCDs preserve the partition
at every adaptive child, including all decisions in Section 2.

For an ascending chain `C=(C_0,...,C_{a-1})` on `U`, let

\[
 \beta_U(C)=(C_0,C_1\setminus C_0,\ldots,
                    C_{a-1}\setminus C_{a-2},U\setminus C_{a-1}),
\]

deleting empty letters. Prefixes realize `C`, and suffixes realize its
complements; an empty part of a witness is omitted. The bridge has at
most `a+1` letters. Because every accumulated chain retains a fixed pivot,
it cannot contain both the empty set and its full support, so the bridge
also has at least `a` letters.

For each terminal desired pair `(C,D)` on complementary supports `U,V`,
put both directed arcs between vertices `(U,C)` and `(V,D^c)`, where
`D^c` is ordered increasingly. A suffix of the second bridge followed by
a prefix of the first gives `C x D`; the reverse boundary gives its full
complement. Each nonempty designated target therefore has an ordinary
nonempty interval witness at the asserted boundary.

In every connected component take a directed Euler circuit. Output the
bridge of each arc tail, followed by one extra copy of the starting
bridge. Concatenate these component words; no witness is required to
cross a component join. If `E` is the number of terminal paired rectangles,
`M=sum_terminal(a+b)`, and `V_cat` bounds all bridge vertices, then

\[
                       M\le N\le M+2E+(mh+1)V_{\rm cat}. \tag{22}
\]

For fixed `m`, each tuple has at most `(sum_i a_i)^(m-2)` leaves. The
initial chain count and its fixed polynomial moments therefore give

\[
                 E=O_m(2^{mh}/h)=o(W(mh)).
\]

Any accumulated chain belongs to a fixed ordered binary-tree hook SCD on
its support. Include all such trees, all proper supports, all signs, and
their ascending complements in a catalogue. The existing coarse bound

\[
              V_{\rm cat}\le 2m!8^m\,2^{(m-1)h}
\]

is sufficient. External length-dependent decisions select from this
catalogue; they do not create new chains outside it. Thus the closing
bridges in (22) also cost `o(W(mh))` for every fixed `m`. Together with
Section 3 this proves

\[
                  \nu(mh)\le(Q_m+o_h(1))W(mh).          \tag{23}
\]

For arbitrary `k`, take `h=floor(k/m)` and `r=k-mh<m`. A top-bit splice
replaces a covering word `w` by `w, {z}, mark_z(w)`, at length `2|w|+1`.
After `r` splices the length is `2^r(|w|+1)-1`, and for fixed `m`,

\[
                 {2^rW(mh)\over W(k)}=1+O_m(1/h).
\]

An explicit all-dimension selection avoids any hidden uniform-in-`m`
claim. For `k>=9`, construct the preceding word for every integer
`3<=m<=floor(sqrt(k))`, splice each to dimension `k`, and output a shortest
candidate. Use the word listing all nonempty subsets for the finitely
many smaller dimensions. This is a finite deterministic algorithm; no
efficiency claim is needed. Every fixed `m` is eventually a candidate.
Equation (23) consequently gives limsup at most `inf_m Q_m`, and (8)
makes this at most `pi^2/8`. This proves (1) for all dimensions, with all
endpoint and component costs paid. The inequality `R_m<=Q_m` gives
the upper half of (2).

## 9. Verification and remaining gap

Run the dependency-free exact checker:

```text
python3 -B scratch/three_accumulator_verify_20260906_a31d9.py
```

It checks rational pi enclosures and (21), integer product-SCD identities,
the exact volume-weighted policy recurrence, deterministic minimum-update
invariants, terminal full-cube partitions, every asserted local boundary,
every actual interval union in the compiled words, and the complete
primary/endpoint/closing ledger. Its assertions use exact arithmetic.
Small-word checks are corroboration, not a substitute for the limit proof.

The checker passed 11,935 exact volume-weighted recurrences, 140,000
seeded integer minimum-update checks, and these six full-cube words:

| Block sizes | Dimension | Word length | Main charge | Endpoint letters | Closing letters |
|---|---:|---:|---:|---:|---:|
| `(2,2,2)` | 6 | 41 | 32 | 6 | 3 |
| `(2,2,2,2)` | 8 | 146 | 112 | 28 | 6 |
| `(2,3,2,3,2)` | 12 | 1721 | 1392 | 312 | 17 |
| `(2,2,2,2,2,2)` | 12 | 1983 | 1536 | 428 | 19 |
| `(3,3,3,3,3)` | 15 | 12309 | 10080 | 2156 | 73 |
| `(2,2,2,2,2,2,2,2)` | 16 | 27453 | 21504 | 5896 | 53 |

All 11,424 directed local boundary checks passed, as did full interval-union
enumeration for each word. The old recursive checker was also rerun with
`-B`: its six words, 1,600 merge identities, and 1,344 completed-rank
inventories passed unchanged.

As a separate comparison check, the existing exact-rational
`certify_four_block(384)` returned the enclosure
`1.252215366813... < c4 < 1.282471384641...`, in particular `c4>1.25`.
Also `Delta_8<1/10000` follows immediately from its printed exact formula,
`e>2`, and `pi>3`. Hence the new coefficient is strictly below the prior
`c4-Delta_8` even without using the finer diagnostic decimal for `c4`.
This comparison is not needed in the proof of (1).

Two separate exploratory files are retained for reproducibility:
`coalescent_policy_probe_20260906_a31d9.cpp` and
`bessel_balance_probe_20260906_a31d9.py`. They explicitly label their output
as Monte Carlo or noncertified quadrature. None of their values is used
in (1)--(3). The C++ probe's mode `4` implements exactly the three-slot
policy; other modes were exploratory. Four and five equalized active
slots with the tested terminal continuations were worse, not improvements.

The remaining centered gap is

\[
 {\pi^2\over8}-{2\over\sqrt e}=0.020639230710\ldots.
\]

The policy does not force the terminal intervals to straddle one almost
surely. Its exact limiting charge has the displayed positive gap. No
claim that the sharp rank-law relaxation is realizable is made, and no
coefficient-one construction is supplied. What is closed here is an
actual, substantially improved upper bound below `1.24`, together with
its realizable finite policies and literal set-word compiler.
