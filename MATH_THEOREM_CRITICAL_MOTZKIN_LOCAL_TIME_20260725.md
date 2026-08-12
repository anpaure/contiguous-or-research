# Critical directional Motzkin transfer and the sublinear energy target

Date: 2026-07-25

Method: pure mathematics only.

## 1. The depth-two weights are a probability kernel

The completed canonical-MSW depth-two audit produces three iterated
critical shell weights:

\[
                         p(-1)={3\over8},\qquad
                         p(0)={1\over4},\qquad
                         p(1)={3\over8}.                       \tag{1.1}
\]

Their sum is one, so a scalar row-sum test cannot be strictly
subcritical.  But the signs are structural: the two offset shells change
the synchronized corridor counter by `+1` and `-1`, while the
crossing-flat shell leaves it unchanged.  Retaining that direction turns
the critical part into a centered lazy random walk rather than an
uncontrolled scalar mass.

The disjoint-forward chronological insertion has critical weight `1/12`
and therefore belongs to a bounded geometric decoration, not to (1.1).

This target has substantial slack relative to the independent benchmark.
Independent allocation has centered energy `Theta(W)` at every depth,
whereas the transfer may lose a factor `sqrt(q)` and still give the
sufficient bound `E_q=O(sqrt(q)W)`.  Thus the permitted ceiling is
`sqrt(q)` above random second-moment scale; no beyond-random energy
suppression is being requested.

## 2. Exact analytic estimate

Let `P` be convolution by (1.1) on `ell^2(Z)`.

### Lemma 2.1 (critical local time is square-root)

For every `r>=0`,

\[
                         P^r(0,0)\le {C\over\sqrt{r+1}},       \tag{2.1}
\]

and consequently

\[
                         \sum_{r=0}^{q}P^r(0,0)\le C\sqrt{q+1}.
                                                                  \tag{2.2}
\]

The same bounds hold, up to an absolute factor, for the reflected or
killed walk on a half-line.

#### Proof

The Fourier multiplier is

\[
 \widehat p(\theta)={1\over4}+{3\over4}\cos\theta.
\]

For `|theta|<=1`, it is at most `exp(-c theta^2)`; away from zero its
absolute value is at most `1-c`.  Fourier inversion therefore gives

\[
 P^r(0,0)
 \le {1\over2\pi}\int_{-\pi}^{\pi}|\widehat p(\theta)|^r,d\theta
 \le C(r+1)^{-1/2}.
\]

Summation proves (2.2).  Reflection and killing are bounded by the usual
image argument (or by the spectral measure comparison). \(\square\)

For reference, the full-line walk has variance `3/4` and local central
limit constant

\[
 P^r(0,0)\sim {1\over\sqrt{2\pi(3/4)r}}
 ={\sqrt{2/(3\pi)}\over\sqrt r}
 ={0.4607\ldots\over\sqrt r}.                                \tag{2.2a}
\]

Its return Green sum is therefore `(0.9214...+o(1))sqrt(q)`.  The hold
probability `1/4` removes the parity obstruction.

### Corollary 2.2 (localized-source transfer)

Suppose nonnegative directional collision masses `A_q(k)` satisfy a
coefficientwise domination of the form

\[
 A_q\le P A_{q-1}+b_q\delta_0+R_q,                            \tag{2.3}
\]

where `b_q=O(W)`, and the total contribution obtained by inserting all
`R`-decorations is bounded by a fixed geometric factor (for example their
critical norm is at most `1/12`).  If only the return/localized coordinate
contributes to a repeated target collision, then

\[
                         A_q(0)=O(\sqrt q\,W).                 \tag{2.4}
\]

#### Proof

Iterate (2.3).  The localized sources contribute

\[
 O(W)\sum_{r<q}P^r(0,0)=O(\sqrt q\,W)
\]

by Lemma 2.1.  The subcritical decorations multiply this by a bounded
resolvent constant. \(\square\)

The pair-gap need not itself have three-step increments.  The following
one-marginal domination is enough and is insensitive to the `+/-2` moves
seen in the depth-three audit.

### Lemma 2.3 (arbitrary joint state, one killed marginal)

Let `Omega` be any finite or countable state space, let
`h:Omega->Z_(>=0)`, and let `K` be a nonnegative substochastic kernel on
`Omega`.  Suppose that for every `x in Omega` and every `ell>=0`,

\[
 \sum_{y:h(y)=\ell}K(x,y)\le P(h(x),\ell),                   \tag{2.5}
\]

where `P` is the killed half-line version of the lazy Motzkin kernel
(1.1).  If a source measure `nu` is supported on `h=0`, then

\[
 \boxed{
 \|\nu K^t\|_1\le \|\nu\|_1\sum_{\ell\ge0}P^t(0,\ell)
       \le {C\|\nu\|_1\over\sqrt{t+1}}.}                    \tag{2.6}
\]

Consequently its Green mass through time `q` is at most
`C||nu||_1 sqrt(q+1)`.

#### Proof

Project `nu K^t` by `h`, writing

\[
 a_t(k)=\sum_{x:h(x)=k}(\nu K^t)(x).
\]

Equation (2.5) gives coefficientwise `a_(t+1)<=a_tP`.  Since
`a_0=||nu||_1 delta_0`, induction yields
`a_t<=||nu||_1 delta_0P^t`.  Sum over `k` and use the killed-walk survival
bound from Lemma 13.2A of the depth-two note (equivalently the ballot
estimate used in Lemma 2.1). \(\square\)

This lemma removes three analytic requirements which would otherwise be
artificial: the second counter may have arbitrary jumps, the internal
shell alphabet may grow, and the raw pair gap need not be Markov or
non-coboundary.  What remains is a precise combinatorial inequality.  A
reversible joint-shell deletion must be organized so that, after fixing
the first occurrence's minimum-rooted counter, the **total** weight of
all compatible second-occurrence extensions with projected symbol
`-`, `C`, or `+` is at most `3/8`, `1/4`, or `3/8`, respectively.  This
is exactly a one-marginal version of the weighted square estimate (8.1),
and it is not implied by the one-ladder signature table alone.

## 3. Why this strength is sufficient

The prime-cycle aggregate theorem accepts

\[
                         E_q\le C_Aq^\beta W                 \tag{3.1}
\]

through every fixed Gaussian window for any `beta<1`.  Indeed, split at
`Q=m^a`, with `0<a<1/(beta+2)`.  The shallow contribution is

\[
 {W\over\sqrt m}\sum_{q\le Q}q^{\beta/2}
 =O\left({WQ^{1+\beta/2}\over\sqrt m}\right)=o(W),           \tag{3.2}
\]

and the surplus branch is

\[
 W\sum_{q>Q}q^{\beta-2}=O(WQ^{\beta-1})=o(W).                 \tag{3.3}
\]

Thus the square-root output (2.4), corresponding to `beta=1/2`, has ample
room.

Keeping the constant `C` in (3.1), the optimized split is

\[
                         Q=(Cn)^{1/(4-\beta)},                 \tag{3.3a}
\]

and the resulting orbit floor is

\[
 O_\beta\left(
 C^{3/(4-\beta)}n^{-(1-\beta)/(4-\beta)}W
             \right).                                        \tag{3.3b}
\]

The exponent becomes zero exactly at `beta=1`; the deep sum is then
harmonic and may cost `Theta(W log m)`.  Thus `beta<1` is the sharp
power-law threshold for this two-branch argument.

For that natural exponent the optimized split is `Q=m^(2/7)`: the two
terms in (3.2)--(3.3) are both `O(Wm^(-1/7))`.  Hence a rigorous
`E_q=O(sqrt(q)W)` transfer would give the quantitative fixed-window orbit
floor

\[
                         O_A(Wm^{-1/7}).                       \tag{3.4}
\]

## 4. Exact remaining combinatorial theorem

To turn this analytic observation into the all-depth MSW energy theorem,
one must prove a directional deletion/insertion statement:

1. every iterated critical collision shell carries an integer corridor
   offset;
2. crossing-flat, positive nesting, and negative nesting act on that
   offset with the three weights in (1.1);
3. new collision sources are localized in `O(1)` offset states;
4. disjoint-forward and bounded-strip sectors have a uniformly summable
   resolvent (the latter is already covered through `q<=m^(1/4)` by the
   growing-strip theorem).

This is a triangular/directional transfer theorem, not a scalar
subcriticality theorem.  The depth-two proof establishes the complete
one-step alphabet and its exact critical weights; compatibility of the
offset under three or more deletion layers remains unproved.

## 5. Coboundary and confinement audits

Suppose the eventual shell deletion is a finite irreducible Markov
additive process with driving states `x in A` and integer increment
`f(x,y)`.  After centering its stationary drift, its asymptotic variance
vanishes exactly when

\[
                         f(x,y)=g(y)-g(x)                      \tag{5.1}
\]

on every allowed transition.  Equivalently, the increment sum is zero
around every directed cycle of the shell graph.  In this coboundary case
the additive coordinate is bounded by the driving state and the required
anti-concentration may fail.  Otherwise a finite-state aperiodic local
limit theorem gives a one-sided `C/sqrt(q)` return bound, provided its
constants are uniform.

This becomes a finite cycle-sum check once the genuine shell alphabet has
been constructed.  It cannot be inferred from the depth-two weights
alone: finiteness, irreducibility, uniform dispersion, and non-coboundary
all remain part of the combinatorial transfer theorem.

Per-step dispersion alone is not a substitute for the last condition.
For example, let `X_t` be the two-state chain which chooses its next state
uniformly and independently, put `g(0)=0,g(1)=1`, and assign the increment

\[
                         f(X_{t-1},X_t)=g(X_t)-g(X_{t-1}).     \tag{5.1a}
\]

Conditional on either present state this increment has two atoms of mass
`1/2`, but its partial sum is

\[
                         S_t=g(X_t)-g(X_0),                   \tag{5.1b}
\]

and is confined to `{-1,0,1}`.  Thus a bound on the largest conditional
atom does not by itself imply a `q^(-1/2)` concentration estimate; temporal
cancellation has to be excluded by the cycle-sum/non-coboundary test.

A clean uniform sufficient package is the following.  The shell graph has
at most `K` states, is irreducible and aperiodic, every positive transition
probability is at least `eta`, and the additive labels are bounded.  In
addition, some directed cycle of bounded length has nonzero label sum and
is uniformly accessible from every state.  For fixed `K,eta` these
conditions give a uniform positive asymptotic variance.  Fourier
perturbation of the finite transition matrix (or regeneration at one
state followed by a lattice concentration theorem) then gives

\[
                 \sup_z\Pr(S_t=z)\le {C(K,\eta)\over\sqrt{t+1}}. \tag{5.1c}
\]

If the shell alphabet grows with `m`, the bounded-state conclusion cannot
be quoted: one must prove the corresponding uniform accessibility and
variance estimates directly.

If the additive coordinate is confined to a strip of width `L`, the
correct Green estimate is

\[
                         O\left(\sqrt q+{q\over L}\right),     \tag{5.2}
\]

not the minimum of those terms.  Prime smoothing then gives the
`O(Wm^(-1/7))` square-root contribution plus `O(W log(m)/L)`.  More
explicitly, at `Q_0=(Cn)^(2/7)` the shallow confinement correction is

\[
 W\sqrt{C/n}\,{Q_0^{3/2}\over\sqrt L}
 =O_C\left({Wn^{-1/14}\over\sqrt L}\right),                 \tag{5.3}
\]

and the deep correction is `O(CW log(m)/L)`.  Consequently the much
weaker condition

\[
                              L/\log m\longrightarrow\infty  \tag{5.4}
\]

already makes confinement negligible.  The natural Dyck height scale
`Theta(sqrt(m))` has ample room.

There is a second directional caveat.  For a fixed-site Green function,
a stationary drift bounded away from zero makes returns summable.  For a
**killed survival** Green function this is true only when the drift is
toward the killing boundary; drift away from the boundary leaves positive
survival probability and hence linear Green mass.  Thus a future shell
proof may use the familiar trichotomy

* nonzero drift: good for localized returns;
* zero drift and non-coboundary: square-root local time;
* zero-drift coboundary: potentially linear local time;

only after it has proved that collision acceptance is localized at a
fixed additive state.  The one-marginal survival theorem below instead
uses the exact centered killed Motzkin domination and does not treat
arbitrary drift as favorable.

## 6. The exact state carried by one intrinsic ladder

The counter state itself can be made canonical without any shell
assumption.  For consecutive pivot intervals put

\[
\begin{array}{c|c|c}
\text{symbol}&\text{relative order}&k_{t+1}-k_t\\ \hline
F&b_t<a_t<b_{t+1}<a_{t+1}&0\\
+&b_t<b_{t+1}<a_{t+1}<a_t&+1\\
-&b_{t+1}<b_t<a_t<a_{t+1}&-1\\
C&b_{t+1}<b_t<a_{t+1}<a_t&0.
\end{array}                                                    \tag{6.1}
\]

Here `F` is the forward-disjoint type and `C` the crossing-flat type.
Equation (6.1) is Lemma 13.2 of the depth-two note, applied to every
three-state window of a general ladder.

Remove the `F` positions and consider one remaining irreducible block
`a<=t<=b`.  Put

\[
 r=\min_{a\le t\le b}k_t,
 \qquad t_* =\min\{t:k_t=r\},
 \qquad h_t=k_t-r.                                           \tag{6.2}
\]

### Lemma 6.1 (minimum-rooted directional state)

The state `h` is nonnegative, `h_(t_*)=0`, and its increments to the
right of `t_*` lie in `{-1,0,+1}` with symbols `-,C,+`.  Read to the left,
the signs are reversed and again give increments in `{-1,0,+1}`.  In
either direction, a `-1` step from state `0` is impossible.  Thus the two
halves of every critical signature are paths of the killed half-line
Motzkin chain, started at its killing boundary.

#### Proof

The increment assertion is (6.1).  Subtracting the minimum gives
nonnegativity and `h_(t_*)=0`.  If an outward step from `t_*`, or from any
later return to level zero, had increment `-1`, the original counter would
fall below `r`, contradicting its definition.  Reversing the left half
changes every increment's sign, and the same argument applies. \(\square\)

This is the correct state variable at the signature level: height above
the global minimum, rooted at the first minimum.  The unnormalized initial
counter `k_a` is not a boundary state in general, and the raw difference
of the counters of two colliding ladders is not the state in Lemma 6.1.

Assign the three critical letters their depth-two shell values

\[
                         w(-)={3\over8},\qquad
                         w(C)={1\over4},\qquad
                         w(+)={3\over8}.                      \tag{6.3}
\]

For a word `sigma`, write `w(sigma)` for the product of its letter
weights.  Lemma 6.1 shows exactly why, if a global shell factorization is
coefficientwise dominated by these products, its state starts at the
killing boundary required in Lemma 2.1.  It does not itself prove that
factorization.

## 7. Complete directional audit at depth three

A depth-three intrinsic ladder has three pivot pairs and two symbols in
(6.1).  If neither symbol is `F`, its normalized critical signature is one
of the following nine words.  The last column gives the first location of
the minimum of the partial sums `0,delta_0,delta_0+delta_1`.

\[
\begin{array}{c|c|c}
(\delta_0,\delta_1)&w(\delta_0)w(\delta_1)&t_*\\ \hline
(-,-)&9/64&2\\
(-,C)&3/32&1\\
(-,+)&9/64&1\\
(C,-)&3/32&2\\
(C,C)&1/16&0\\
(C,+)&3/32&0\\
(+,-)&9/64&0\\
(+,C)&3/32&0\\
(+,+)&9/64&0.
\end{array}                                                    \tag{7.1}
\]

Their weights sum to one.  The other seven two-letter words contain at
least one `F` and hence split the one-ladder signature at that position.
Thus, for a single occurrence, the extension from depth two to depth
three has exactly the desired critical alphabet and boundary-rooted state;
there is no hidden fifth direction.

There is, however, an important distinction between this statement and a
collision-shell transfer.  For a depth-three occurrence over common core
`S`, write its states as in the exact ladder formula.  The common cores of
its first and last depth-two subladders are respectively

\[
                         S+\{b_2\},\qquad S+\{a_0\}.          \tag{7.2}
\]

For two genuine depth-three bowties these four depth-two parent targets
are distinct.  Consequently neither pair of depth-two subladders is a
depth-two collision to which the shell proofs producing (6.3) can be
applied.  This is the precise reason that the valid one-ladder table
(7.1) does not yet prove the all-depth energy estimate.

The same warning appears if one tries to use a raw pair gap.  If two
ladders have counter increments `delta_t` and `delta'_t`, then

\[
 (k'_{t+1}-k_{t+1})-(k'_t-k_t)=\delta'_t-\delta_t
 \in\{-2,-1,0,1,2\}.                                       \tag{7.3}
\]

Thus the three-step lazy kernel does not act on the unqualified counter
difference.  A genuine shell theorem must either prove coherence that
excludes the `+/-2` moves, or use a larger state whose additive coordinate
reduces to Lemma 6.1 after a canonical shell is selected.

## 8. What remains to prove combinatorially

The depth-two normal forms suggest the following exact target.

### Directional shell factorization target

For every intrinsic collision pair, after the already-controlled
shared-parent and growing-strip cases are removed, construct a reversible
deletion with these properties:

1. each irreducible shell has a canonical first minimum and a state `h`
   as in (6.2);
2. its `-,C,+` cells have disjoint or uniquely shared excursion data whose
   joint generating function is coefficientwise dominated by the product
   of the corresponding local kernels in (6.3);
3. an `F` cell is a regeneration cut.  Its chronological insertion has
   critical weight `1/12`, while its overlap loops are absorbed once at
   the cut and cannot re-enter as another flat transition;
4. collision sources and terminal identifications occur only at `h=0` (or
   in a fixed finite set of boundary states), and the typed shell list
   reconstructs both ladders uniquely.

Under these four clauses, summing signatures is matrix multiplication by
the killed kernel, not a count of `3^q` words.  Lemma 2.1 then gives
`O(sqrt(q))` Green amplification, while `F` decorations contribute only a
bounded resolvent.

Equivalently, if occurrences are first partitioned by irreducible
signature `sigma`, the needed replacement for crude type-counting Cauchy
is a weighted square estimate.  With `w(sigma)` from (6.3), one needs the
within-signature square masses divided by `w(sigma)` to be summable at
each localized source.  The identity

\[
 \left(\sum_\sigma x_\sigma\right)^2
 \le\left(\sum_\sigma w(\sigma)\right)
     \left(\sum_\sigma{x_\sigma^2\over w(\sigma)}\right)     \tag{8.1}
\]

then turns the signature sum into the Motzkin operator.  The first factor
is controlled by the killed walk after minimum-rooting; the second is
exactly the missing reversible shell estimate.

The present depth-three audit therefore has a sharp outcome.  The
boundary state and the critical alphabet are exact for each ladder, and
forward-disjoint cells are correctly identified as cuts.  What is not yet
proved is that a genuine four-parent collision admits a common removable
shell with those local weights.  In particular, multiplying the
depth-two kernels across (7.1) would be circular.
