# Mixed-profile continuation of the quantitative seam argument

## 1. Scope and outcome

This note starts from the independently audited three-box framework in
`FABLE_QUANTITATIVE_SEAM_TRACE_AUDIT.md`.  It does not assume any of the
retracted concentration or staircase claims.

There are three results.

1.  The seam repair has an exact fixed-threshold limiting formulation.  Its
    variables are a plateau-length measure, a stationary coupling of
    predecessor and successor lengths, a gap allocation, and a fractional
    matching of absorbing seams to positive coordinate levels.  The exact
    saving integrand is
    \[
      \phi(p,s,z)=
      \min\{p,(4-s-z)_+\}(s-z)_+ .                 \tag{1.1}
    \]
2.  The atomic theorem is stable.  There is one numerical
    `epsilon_0>0` such that an arbitrary, possibly non-atomic profile with
    mass nearly two and all but `epsilon_0` of its mass in an
    `epsilon_0`-band about any
    \(x\in[4/3,3/2]\) is impossible under `D=o(a^2)`.  Thus the audited
    theorem excludes an open mixed-profile neighbourhood of the whole
    atomic segment, not just the atoms themselves.
3.  Atomic exclusion cannot be extended by convexity or by optimizing each
    threshold separately.  The adversarial fixed-threshold functional is
    concave in the plateau measure.  Moreover the broad measure
    \[
                         \mu(dx)=2\mathbf 1_{[1,2]}(x)\,dx       \tag{1.2}
    \]
    has, for every `1<c<=4/3`, a feasible **thresholdwise static seam
    ledger** whose modified cost is strictly above four.  These ledgers are
    not asserted to arise from one ordering, and their couplings for
    different `c` are not asserted to be mutually compatible.

The distinction in the last sentence is essential.  The measure (1.2) is
not a counterexample to the three-box conjecture.  It is an explicit
obstruction to a proof which treats the thresholds independently or simply
integrates the already-proved atomic inequalities.

## 2. Fixed-threshold limiting data

Fix `1<c<2`.  List the `c`-dangerous directed internal peak plateaux in word
order.  Normalize their edge lengths and predecessor gaps by

\[
 p_j={\lambda_{j-1}\over a},\qquad
 s_j={\lambda_j\over a},\qquad
 z_j={g_{j-1}\over a}.
\]

After passing to a subsequence, define

\[
 \mu={1\over a}\sum_j\delta_{s_j},
 \qquad
 \rho={1\over a}\sum_{j\ge2}\delta_{(p_j,s_j,z_j)}             \tag{2.1}
\]

in the weak limiting sense.  Write

\[
 f=\mu((c,2]),\qquad
 \ell=\int x\,d\mu(x),\qquad
 e_c=\int(x-c)\,d\mu(x).                                    \tag{2.2}
\]

Deleting the first and last plateau changes the normalized measures by
`o(1)`, so both the `p`- and `s`-marginals of `rho` are `mu`.  Edge
disjointness and the vertex-union gap convention give

\[
          \ell\le3,
 \qquad  \int z\,d\rho(p,s,z)\le 3-\ell .                    \tag{2.3}
\]

The second inequality remains meaningful if a vanishing number of gaps is
macroscopic: truncate `z`, pass to the limit, and then remove the
truncation.  Such gaps make no favourable contribution to the saving below.

### 2.1 Exact absorption capacity

Call a seam absorbed when the predecessor's rising cross-coordinate becomes
the fixed coordinate of the successor at the seam-local maximum.  The proof
of Lemma 1 in `FABLE_QUANTITATIVE_SEAM_TRACE_AUDIT.md` does not need the two
lengths to be asymptotically equal.  For a seam of normalized lengths
`(p,s)`, absorption at normalized positive level `t` necessarily satisfies

\[
                         p-1\le t\le2-s.                       \tag{2.4}
\]

Indeed the rising coordinate ends at least at `(p-1)a`, while a successor
of length `sa` fits on level `ta` only when `t<=2-s`.  In particular
absorption is impossible when `p+s>3`.

Every dangerous successor has more than `a` edges.  Hence two such
successors cannot use the same geometric coordinate line.  In the limit an
absorbed submeasure is therefore represented by a measure

\[
 \kappa(dp\,ds\,dz\,dt\,dd),\qquad d\in\{1,2,3\},             \tag{2.5}
\]

whose `(p,s,z)` projection `alpha` obeys `0<=alpha<=rho`, whose support
obeys (2.4), and whose level-direction projection satisfies

\[
        \kappa\{d\in\{1,2,3\},t\in B\}\le3|B|                \tag{2.6}
\]

for every Borel `B subset [0,1]`.  Equivalently, one has one Lebesgue unit
of line capacity in each of the three directions.  This is the sharp
measure-level version of the atomic bound `3(3-2x)`.

For a prescribed predecessor-successor coupling, the largest absorbable
mass is thus a fractional interval-matching problem: a pair `(p,s)` asks for
one point of the interval `[p-1,2-s]`, and the available resource is
`3 dt`.  In max-flow/min-cut form,

\[
 A_{\max}(\rho_{ps})
 =f-\sup_{\mathcal U}
       \left(\rho_{ps}(\mathcal U)-3|N(\mathcal U)|\right)_+, \tag{2.7}
\]

where `N(U)` is the union of the requested level intervals.  Formula (2.7)
is only a compact way of writing the fractional Hall theorem; retaining
`kappa` is safer in applications.

### 2.2 Exact nonabsorbing saving

For a nonabsorbing seam, the seam-local maximum lemma gives an internal
threshold run of normalized cost at most `z+o(1)`.  The exact safe service
interval from the audited repair has normalized size at least

\[
                         b(p,s,z)=\min\{p,(4-s-z)_+\}.          \tag{2.8}
\]

The first quantity is the predecessor edge-interior supply.  The second is
the remaining forward-window supply after the successor and its predecessor
gap are inserted.  Different seams use disjoint predecessor interiors.

Reassigning one of these starts saves at least `(s-z)a-o(a)`, when positive.
Consequently the total normalized saving is

\[
 \boxed{
 S(\rho,\alpha)
   =\int \phi(p,s,z)\,d(\rho-\alpha),
 \qquad
 \phi(p,s,z)=\min\{p,(4-s-z)_+\}(s-z)_+.}           \tag{2.9}
\]

This formula includes partial successor plateaux, intermediate seam maxima,
shared endpoints, and word-boundary loss: those were precisely the cases
settled in the atomic audit, and the total boundary loss is `o(a^3)`.

### 2.3 The modified first-dangerous functional

The first-dangerous seam term itself converges to

\[
 H_c(\rho)=
 \int (s-c)\min\{z,4-s\}\,d\rho(p,s,z).                       \tag{2.10}
\]

The audited cyclic secant estimate contributes `2e_c`.  Therefore the
modified assignment has

\[
 {Q_{\rm mod}\over a^3}
 \le
 \boxed{
 \Phi_c(\mu,\rho,\kappa)
 =3c+2e_c+H_c(\rho)-S(\rho,\alpha)}+o(1).            \tag{2.11}
\]

Let `F_c(mu)` denote the feasible ledgers satisfying (2.3)--(2.6), and put

\[
 \mathcal U_c(\mu)=
 3c+2e_c+sup_{(\rho,\kappa)\in\mathcal F_c(\mu)}
       \{H_c(\rho)-S(\rho,\alpha)\}.                         \tag{2.12}
\]

Under `D=o(a^2)`, the run-spectrum lower bound says that a realizable
profile must have `U_c(mu)>=4` at every continuity threshold for which the
limiting ledger is taken.  Thus

\[
                         \mathcal U_c(\mu)<4                   \tag{2.13}
\]

is a valid fixed-threshold exclusion certificate.

Equation (2.12) is sharp for the present seam repair.  It is not claimed to
encode all line-intersection, cross-line-desert, orientation, or multiscale
ordering constraints of a real word.

## 3. Coarse cheap-seam corollary and optimized atomic constant

The exact functional has a useful one-parameter relaxation.  For `r>0`,
the gap budget gives

\[
 \rho\{z>r\}\le {3-\ell\over r}.                             \tag{3.1}
\]

If at most `A` seam mass is absorbed, the nonabsorbed seams with `z<=r`
have mass at least

\[
                 \left[f-A-{3-\ell\over r}\right]_+.          \tag{3.2}
\]

If on the relevant support `p>=p_0` and `s_0<=s<=s_1`, their saving is at
least

\[
 \boxed{
 \left[f-A-{3-\ell\over r}\right]_+
 \min\{p_0,(4-s_1-r)_+\}(s_0-r)_+.}                 \tag{3.3}
\]

This is the measure-level absorption-capacity/long-gap/cheap-seam ledger.
The atomic proof used `r=1`, but that choice is not optimal.

For `mu=2 delta_x`, `4/3<=x<=3/2`, one has

\[
 A\le3(3-2x),\qquad 3-\ell=3-2x.
\]

For the optimizing range the service factor is `x`, and (3.3) becomes

\[
 S_r(x)=x\left[6x-7-{3-2x\over r}\right]_+(x-r)_+.            \tag{3.4}
\]

Its interior maximizer is

\[
 r_*(x)=\sqrt{{x(3-2x)\over6x-7}},                            \tag{3.5}
\]

and hence

\[
 \boxed{
 S_*(x)=x\left(\sqrt{x(6x-7)}-\sqrt{3-2x}\right)^2.}          \tag{3.6}
\]

At the former balanced endpoint this gives

\[
                         S_*(4/3)=4/9,                         \tag{3.7}
\]

improving the sufficient `r=1` coefficient `8/27` in the audited proof.
No theorem status changes—the atom was already excluded—but (3.6) is the
correct optimized scalar benchmark for mixed-profile work.

## 4. A genuine mixed-profile stability theorem

The next theorem is deliberately finite and quantitative, so it does not
hide a convergence assumption.

### Theorem 4.1 (uniform band stability)

There exists an absolute `epsilon_0>0` with the following property.  Fix

\[
                         4/3\le x\le3/2
\]

and `0<epsilon<=epsilon_0`, and set `c=x-2epsilon`.  Suppose that, for all
sufficiently large `a`, the `c`-dangerous list contains

* between `(2-epsilon)a` and `(2+epsilon)a` regular plateaux with normalized
  lengths in `[x-epsilon,x+epsilon]`; and
* at most `epsilon a` other plateaux.

Then no such sequence of middle orders can have `D=o(a^2)`.

In particular the conclusion permits an arbitrary non-atomic distribution
inside the band.  It is a true mixed-profile extension of the atomic
theorem.

#### Proof

Let `R` and `E` be the regular and exceptional counts.  In the dangerous
word, the number of regular-to-regular predecessor-successor seams is at
least

\[
                         R-E-1\ge(2-2\epsilon-o(1))a.           \tag{4.1}
\]

For such a seam, absorption uses a level in

\[
 [x-1-\epsilon,,2-x+\epsilon].                               \tag{4.2}
\]

No line can be reused, so at most

\[
                         3(3-2x+2\epsilon)a+O(1)               \tag{4.3}
\]

regular seams are absorbed.

The regular plateaux alone consume at least

\[
                         (2-\epsilon)(x-\epsilon)a^2           \tag{4.4}
\]

ordering edges.  Hence all complement gaps have total size at most

\[
 \left[3-(2-\epsilon)(x-\epsilon)+o(1)\right]a^2.             \tag{4.5}
\]

At most the coefficient in (4.5), times `a+o(a)`, seams can have gap
greater than `a`.  Consequently the density of regular, nonabsorbed seams
with gap at most `a` is at least

\[
 C_\epsilon(x)
 =8x-10-(10+x)\epsilon+\epsilon^2-o(1).                       \tag{4.6}
\]

For each such seam, (2.8) supplies at least

\[
                         (x-\epsilon)a-O(1)                    \tag{4.7}
\]

disjoint starts: indeed
`4-(x+epsilon)-1 >= x-epsilon` throughout the stated interval.
The saving at every one is at least

\[
                         (x-1-\epsilon)a-O(1).                 \tag{4.8}
\]

Thus

\[
 {S\over a^3}\ge
 C_\epsilon(x)_+(x-\epsilon)(x-1-\epsilon)-o(1).              \tag{4.9}
\]

It remains to bound the unmodified assignment.  Every regular plateau has
excess at most `3epsilon a` above `ca`, and every exceptional plateau has
excess at most `(2-c)a`.  Therefore

\[
 e_c\le3\epsilon(2+\epsilon)+\epsilon(2-c)
       \le7\epsilon+3\epsilon^2.                              \tag{4.10}
\]

The sharpened audited seam bound gives `H_c<=(4-c+o(1))e_c`, and hence

\[
 {Q_{\rm fd}\over a^3}
 \le3c+2e_c+H_c+o(1)
 \le3x+29\epsilon+15\epsilon^2+o(1).                         \tag{4.11}
\]

At `epsilon=0`, the amount subtracted in (4.9) is

\[
                         (8x-10)x(x-1).
\]

The independently audited polynomial inequality is uniform on the compact
interval:

\[
 (8x-10)x(x-1)-(3x-4)\ge8/27.                                \tag{4.12}
\]

All expressions in (4.9)--(4.11) are continuous in `(x,epsilon)`.
Therefore one absolute `epsilon_0>0` makes

\[
                         Q_{\rm mod}\le(4-\eta)a^3             \tag{4.13}
\]

for some `eta>0`, uniformly in `x`.  This contradicts the audited capped-run
lower bound `(4-o(1))a^3`.  QED.

### Measure formulation

The hypotheses are an explicit neighbourhood of the atomic segment in the
tail-count topology: total dangerous count is near two, all but small count
mass lies in a narrow length band, and the outlier count is small.  Hence
Theorem 4.1 excludes many genuinely non-atomic limiting measures, including
every mass-two measure supported in a sufficiently narrow band about one
`x in [4/3,3/2]`.

It does not imply that an arbitrary mixed survivor must be close to one
atom.  Such a stability reduction remains open.

## 5. Concavity: why atoms are not extremizers

The feasible set in Section 2 is convex.  If ledgers for `mu_1` and `mu_2`
are mixed in proportions `theta` and `1-theta`, then

* both marginal equations remain valid;
* the gap budget mixes exactly, since `3-ell` is affine;
* the line resource remains bounded by
  `theta(3dt)+(1-theta)(3dt)=3dt`; and
* the objective in (2.11) mixes linearly.

It follows that

\[
 \mathcal U_c(\theta\mu_1+(1-\theta)\mu_2)
 \ge
 \theta\mathcal U_c(\mu_1)
 +(1-\theta)\mathcal U_c(\mu_2).                            \tag{5.1}
\]

Thus the adversarial value is **concave**, not convex, in the plateau
measure.  Maximizing a concave functional over measures need not put the
maximizer at a Dirac measure; mixing can create new predecessor-successor
couplings and share the level resource more efficiently.  Therefore the
atomic theorem cannot be integrated or extended by an extreme-point
argument.

## 6. An explicit broad thresholdwise obstruction

Take the one fixed broad measure

\[
                         \mu(dx)=2\mathbf 1_{[1,2]}(x)\,dx.    \tag{6.1}
\]

It has count mass two and edge mass three.  At threshold
`1<c<=4/3`, its dangerous tail is

\[
 \mu_c(dx)=2\mathbf1_{[c,2]}(x)\,dx,\qquad
 e_c=(2-c)^2,qquad
 \ell_c=4-c^2,qquad
 G_c=3-\ell_c=c^2-1.                                        \tag{6.2}
\]

We now give a feasible ledger for this one threshold.

### 6.1 Absorbed low block

On `[c,3-c]`, couple predecessor and successor by

\[
                         p=3-s,qquad z=0.                     \tag{6.3}
\]

Absorb the seam at the unique level

\[
                         t=2-s=p-1.                            \tag{6.4}
\]

Reflection preserves the density `2 ds`.  Its level pushforward has density
two on `[c-1,2-c]`, strictly within the available density three.  Thus every
low-block seam satisfies the exact absorption constraint (2.6).

### 6.2 Nonabsorbed high block

On `[3-c,2]`, use the identity coupling `p=s`.  Put

\[
 r_c=\sqrt{2(c^2-3c+4)}.                                     \tag{6.5}
\]

Assign

\[
 z=s\quad(3-c\le s\le r_c),
 \qquad z=0\quad(r_c<s\le2).                                 \tag{6.6}
\]

This uses exactly the available complement gap mass, because

\[
 2\int_{3-c}^{r_c}s\,ds
 =r_c^2-(3-c)^2=c^2-1=G_c.                                   \tag{6.7}
\]

For the first high subblock, `z=s`, so the saving vanishes and the seam term
is `(s-c)s`.  For the second, `z=0`, so the seam term vanishes and the saving
is `s^2`.  The ledger value is therefore

\[
 \begin{aligned}
 \Psi(c)
 &=3c+2(2-c)^2
   +2\int_{3-c}^{r_c}(s-c)s\,ds
   -2\int_{r_c}^{2}s^2\,ds\\
 &=\frac43\,[2(c^2-3c+4)]^{3/2}
   -\frac13c^3-4c^2+14c-\frac{46}{3}.             \tag{6.8}
 \end{aligned}
\]

Elementary differentiation shows that `Psi` is decreasing on
`[1,4/3]`.  At the right endpoint,

\[
 \Psi(4/3)
 ={512\sqrt2-370\over81}
 =4.371\ldots>4.                                                \tag{6.9}
\]

Thus

\[
                         \Psi(c)>4,qquad1<c\le4/3.             \tag{6.10}
\]

This is a concrete broad mixed profile on which the sharp fixed-threshold
seam repair has no contradiction, even though every atom in the critical
interval has been excluded.

### 6.3 What this construction does and does not prove

The construction proves static feasibility only for the variables retained
in (2.3)--(2.6).  In particular:

* the coupling `rho_c` is allowed to depend on `c`;
* deleting the plateaux below two different thresholds need not induce the
  two displayed successor couplings from one common word;
* the level resource is aggregated over directions and does not impose the
  predecessor's actual rising-direction labels;
* line intersections, additive triples, and cross-line-desert placement are
  not encoded; and
* no permutation of `H_a` is constructed.

Accordingly (6.1)--(6.10) are not evidence against the original conjecture.
They identify the next theorem: a successful general proof must couple
different thresholds or add realizable ordering/cross-line constraints.

## 7. The precise next mathematical targets

The atomic step is no longer the bottleneck.  Any of the following would
move the general case genuinely forward.

1. **Multiscale consistency.**  Characterize the family of tail couplings
   `rho_c` which can arise by repeatedly deleting shorter plateaux from one
   cyclic/linear successor order.  The obstruction in Section 6 deliberately
   ignores this nesting.
2. **Direction-labelled absorption.**  Refine (2.6) to a transport law in
   which the resource direction equals the predecessor's rising
   cross-coordinate and the successor's fixed coordinate.  This couples
   absorption to the three-direction line measures rather than only to
   `3 dt`.
3. **Cross-line gap transport.**  Combine the exact saving integrand (1.1)
   with the finite inclusion
   `C subset (C\Lambda) union (Lambda\V)`.  The present functional knows
   the total gap budget but not whether a gap allocation can occupy the
   required predecessor seams outside the selected line union.
4. **Stability reduction.**  Prove that every optimizer of the full
   direction-labelled, multiscale functional lies in the neighbourhood
   excluded by Theorem 4.1.  Concavity (5.1) shows that no naive
   extreme-point argument can provide this reduction.

## 8. Ledger

### Proved in this note, conditional only on the inherited audited framework

* the general absorption interval and fractional line-capacity formulation;
* the exact mixed saving integrand and modified first-dangerous functional;
* the cheap-seam relaxation (3.3);
* the optimized atomic saving (3.6), including `4/9` at `x=4/3`;
* the uniform mixed band-stability exclusion, Theorem 4.1;
* concavity of the adversarial fixed-threshold value; and
* feasibility and value of the thresholdwise broad ledger in Section 6.

### Explicitly not proved

* that the Section 6 ledgers come from one word;
* that they satisfy the full mixed cross-line variational constraints;
* a multiscale relation between `rho_c` at different thresholds;
* exclusion of every non-atomic profile;
* the three-box impossibility theorem; or
* the all-`k` OR-array conjecture.
