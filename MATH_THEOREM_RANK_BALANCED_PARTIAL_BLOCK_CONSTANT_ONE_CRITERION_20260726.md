# Rank-balanced partial blocks: a sharp sufficient criterion for constant one

Date: 2026-07-26

Method: pure mathematics only.

## 0. Scope and verdict

This note gives a self-contained implication theorem.  It does **not** prove
the remaining block-selection statement.

The theorem separates four exact quantities:

1. the middle leave `u`;
2. the block-boundary/seam overhead `S`;
3. the simultaneous weighted two-sided shadow deficit `D`; and
4. the independent outer-tail length `T`.

The exact construction below has length at most

\[
                 W+S+D+T.                                      \tag{0.1}
\]

In particular, a middle mask left out of the block packing is appended once
as a literal entry.  It does not have to be inserted into the delayed middle
row and therefore does not cost `H` copies.  This is sharper than the older
sufficient condition `Hu=o(W)`.

The unresolved Stage B is pure union coverage.  Prescribed rank-balanced
quotas and their max-flow inequalities give a useful stronger certificate,
but they are not physical constraints of the OR word.

## 1. Parameters and locally geodesic blocks

For `m>=1`, put

\[
 W=W_m=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},\qquad
 \rho_q=\frac{N_q}{W}.                                  \tag{1.1}
\]

Let `H=H(m)` and `ell=ell(m)` be positive integers, and put

\[
                         R=2\ell.                         \tag{1.2}
\]

An oriented cyclic middle block is a cyclic list

\[
 B=(X^B_0,X^B_1,\ldots,X^B_{R-1}),
 \qquad X^B_i\in\binom{[2m]}m,                            \tag{1.3}
\]

of `R` distinct middle sets.  It is **cyclically delay-`H` geodesic** if, for
every cyclic start `i` and every `0<=q<=H+1`, the segment

\[
 X^B_i,X^B_{i+1},\ldots,X^B_{i+q}                        \tag{1.4}
\]

is a Johnson geodesic.  Equivalently, no coordinate is changed twice among
any `H+1` consecutive transitions.  The extra one transition is essential:
it is exactly what forces every internal positive coordinate run to contain
at least `H+1` states.  Shadows are required only through depth `H`.  For
such a shadow segment define

\[
 L^B_{i,q}=\bigcap_{j=0}^qX^B_{i+j},\qquad
 U^B_{i,q}=\bigcup_{j=0}^qX^B_{i+j}.                     \tag{1.5}
\]

Then

\[
 |L^B_{i,q}|=m-q,\qquad |U^B_{i,q}|=m+q.                 \tag{1.6}
\]

Every partial pair-flip block of length `2ell` is cyclically delay-`H`
geodesic whenever `H<ell`; in that case its depth-`q` lower colours are distinct
within the block, and so are its upper colours.  The implication theorem
does not need the within-block distinctness separately: all repetitions are
already charged by the global deficit below.

Let `F=F_m` be a family of blocks whose middle sets are pairwise disjoint,
including between different blocks.  Write

\[
 t=|F|,\qquad u=W-Rt.                                    \tag{1.7}
\]

Thus `u` is the exact middle leave.

## 2. Cuts, copied collars, and the exact shadow deficit

For every block choose an integer copied-prefix length

\[
                         0\le \sigma_B\le H              \tag{2.1}
\]

and form the ordinary linear middle row

\[
 T_B=(X^B_0,\ldots,X^B_{R-1},X^B_0,\ldots,
                    X^B_{\sigma_B-1}).                    \tag{2.2}
\]

Its length is `R+sigma_B`.  A cyclic block window is called **available**
if all of its states occur consecutively in (2.2).  Let

\[
 \begin{aligned}
 C^-_q(B)&=\{L^B_{i,q}:\text{the depth-}q\text{ window at }i
                         \text{ is available}\},\\
 C^+_q(B)&=\{U^B_{i,q}:\text{the depth-}q\text{ window at }i
                         \text{ is available}\}.
 \end{aligned}                                           \tag{2.3}
\]

Thus `sigma_B=0` is a bare cut and `sigma_B=H` retains every cyclic window
through depth `H`.  Define the covered and missing sets by

\[
 \mathcal C_q^\pm=\bigcup_{B\in F}C_q^\pm(B),\qquad
 M_q^\pm=N_q-|\mathcal C_q^\pm|.                         \tag{2.4}
\]

The exact **one-copy repair ledger** for the certified central-band shadows is

\[
\boxed{D=D_m=\sum_{q=1}^H(M_q^-+M_q^+).}                \tag{2.5}
\]

Appending each listed missing mask once costs exactly `D`.  This is the
repair used in the theorem; it need not be the minimum possible repair,
because an uncertified or incidental interval elsewhere in the word may
already realize some listed mask.

If

\[
 \eta_q^\pm=\frac{M_q^\pm}{N_q}                         \tag{2.6}
\]

is the relative deficit in one shadow layer, then (2.5) is equivalently the
**weighted shadow-deficit identity**

\[
 \boxed{\frac DW=
   \sum_{q=1}^H\rho_q(\eta_q^-+\eta_q^+).}               \tag{2.7}
\]

Consequently the exact Stage-B target is not a separate unspecified `o(1)`
fraction in every rank.  It is the single simultaneous condition

\[
 \sum_{q=1}^H\rho_q(\eta_q^-+\eta_q^+)=o(1),             \tag{2.8}
\]

equivalently `D=o(W)`.  Since
`sum_(q<=H)rho_q=Theta(sqrt(m))` once `H/sqrt(m)->infinity`, a uniform
per-layer error `o(1)` is not by itself enough.

The exact block boundary overhead used below is

\[
 \boxed{S=S_m=\sum_{B\in F}(H+\sigma_B).}                \tag{2.9}
\]

In the safe all-cyclic-window choice `sigma_B=H`,

\[
 S=2Ht=\frac H\ell(W-u)\le\frac H\ell W.                \tag{2.10}
\]

For a bare cut, provided Stage B is measured only on the surviving windows,

\[
 S=Ht=\frac H{2\ell}(W-u).                               \tag{2.11}
\]

No cross-seam shadow is counted in (2.4).  Thus there is no hidden seam
repair assumption.

## 3. The sufficient theorem

### Theorem 3.1 (rank-balanced partial-block criterion)

Suppose that for every sufficiently large `m` there are integers `H,ell`, a
pairwise middle-disjoint family `F_m` of length-`2ell` cyclically
delay-`H` geodesic blocks, and copied-prefix lengths `sigma_B` as above, satisfying

\[
 \frac H{\sqrt m}\longrightarrow\infty,\qquad
 H=o(m^{2/3}),\qquad
 H<\ell\le m,\qquad
 \frac H\ell\longrightarrow0,                           \tag{3.1}
\]

and

\[
       \sum_{q=1}^H(M_q^-+M_q^+)=o(W).                   \tag{3.2}
\]

Then

\[
                         \nu(2m)\le W+o(W).              \tag{3.3}
\]

More precisely, let `T_m` be the length of any literal OR word covering all
ranks outside the band `[m-H,m+H]`.  The construction in the proof gives

\[
 \boxed{\nu(2m)\le W+S_m+D_m+T_m.}                       \tag{3.4}
\]

The established truncated-ideal tail theorem supplies

\[
 T_m=O\!\left(\left(1+\frac{H^2}{m}\right)
                     \binom{2m}{m-H}\right)=o(W)         \tag{3.5}
\]

under (3.1).  Moreover `S_m=o(W)` follows from (2.9),
`sigma_B<=H`, and `H/ell->0`.

If these hypotheses hold for all large `m`, then the standard one-coordinate
lift `nu(k+1)<=2nu(k)` and the width lower bound imply

\[
             \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}
             \qquad(k\longrightarrow\infty).             \tag{3.6}
\]

#### Proof

Fix one linear row

\[
                    T=(T_1,\ldots,T_v)=T_B,
             \qquad v=R+\sigma_B.                         \tag{3.7}
\]

Define its finite delay-`H` factor by

\[
 A_j=\bigcap_{i=\max(1,j-H)}^{\min(v,j)}T_i,
                 \qquad 1\le j\le v+H.                   \tag{3.8}
\]

Because the original block is cyclically delay-`H` geodesic, no coordinate
changes twice in `H+1` consecutive transitions of (3.7).  Hence every internal
positive coordinate run in (3.7) has at least `H+1` states.  A direct
coordinatewise check gives, for every `1<=a<=b<=v` with `b-a<=H`,

\[
 \begin{aligned}
 T_i&=\bigcup_{j=i}^{i+H}A_j,                              &&\tag{3.9}\\
 \bigcap_{i=a}^bT_i
     &=\bigcup_{j=b}^{a+H}A_j,                             &&\tag{3.10}\\
 \bigcup_{i=a}^bT_i
     &=\bigcup_{j=a}^{b+H}A_j.                             &&\tag{3.11}
 \end{aligned}
\]

All indices in (3.9)--(3.11) lie in `[1,v+H]`, including at the two finite
boundaries.  For completeness, (3.9) follows because a `1` at position `i`
lies in a defining all-one window for some `A_j`: this window has `H+1`
states in the interior and is truncated only at a boundary.  An internal
positive run is long enough, while a boundary run uses the truncation in
(3.8).  In (3.10), the factor windows indexed by
`b<=j<=a+H` all contain `[a,b]`; conversely the same run argument supplies
one such all-one window for every coordinate present throughout `[a,b]`.
Finally (3.11) is the union of (3.9) over `a<=i<=b`.

Thus every middle state in the block and every available lower or upper
shadow in (2.3) is a literal contiguous OR of entries of the single factor
word

\[
                       A_1,A_2,\ldots,A_{v+H}.             \tag{3.12}
\]

This word has exactly

\[
                         R+\sigma_B+H                     \tag{3.13}
\]

entries.  Concatenate (3.12) over the blocks.  Every certified witness stays
inside its own factor word, so concatenation cannot destroy it and no
cross-block interval is being assumed.  The total block-factor length is

\[
 \sum_{B\in F}(R+\sigma_B+H)
   =Rt+S=(W-u)+S.                                        \tag{3.14}
\]

Append each of the `u` uncovered middle masks once as a literal entry.  This
changes (3.14) to exactly `W+S`, which proves why no condition `Hu=o(W)` is
needed.  Next append once each mask missing from (2.4); this costs exactly
`D`.  At this point every rank from `m-H` through `m+H` is covered.  Append
the independent outer-tail word, at cost `T_m`.  This proves (3.4).

Some sets in the factors (3.8) may be empty.  After all witnesses have been
fixed, delete every empty entry.  The nonempty members of each old witness
become consecutive and have the same union, so this can only shorten the
word.  The construction is therefore a literal nonempty contiguous-OR word.

To verify (3.5), the quoted tail theorem gives its first bound.  Also

\[
 \rho_H=\prod_{j=0}^{H-1}\frac{m-j}{m+j+1}
 \le \exp\!\left(-\frac{H^2}{m+H}\right).                \tag{3.15}
\]

Thus `(1+H^2/m)rho_H=o(1)` when `H/sqrt(m)->infinity` and `H=o(m)`, proving
the second equality in (3.5).

The safe choice `sigma_B=H` gives (2.10), hence `S=o(W)`.  Equations
(3.2), (3.4), and (3.5) now prove (3.3).

Finally,

\[
 \binom{2m+1}{m}=\frac{2m+1}{m+1}\binom{2m}{m}
                 =(2-o(1))W.                              \tag{3.16}
\]

Therefore the lift from even to odd dimensions preserves the leading
constant, and the middle-layer width bound supplies the reverse inequality.
QED.

### Corollary 3.2 (an explicit admissible scale)

Let `omega(m)->infinity` with `omega=o(m^{1/3})`, set

\[
 H=\left\lceil\sqrt{m\omega(m)}\right\rceil,
 \qquad
 \ell=\left\lceil\sqrt{mH}\right\rceil.                  \tag{3.17}
\]

Then (3.1) holds.  Hence it is enough to prove (3.2) for disjoint
length-`2ell` partial pair-flip blocks at these scales.  Taking the full
copied collar `sigma_B=H` gives

\[
                 S\le \frac H\ell W
                    =\sqrt{\frac Hm}\,W=o(W).              \tag{3.18}
\]

## 4. The exact deterministic flow certificate for Stage B

Pure coverage (3.2) is the sharp physical hypothesis.  The following
rank-balanced statement is a stronger deterministic certificate for it.

Fix a depth `q`, a sign `epsilon`, and nonnegative integer block quotas
`b_{B,q}^epsilon` satisfying

\[
 b_{B,q}^\epsilon\le |C_q^\epsilon(B)|,
 \qquad
 \sum_{B\in F}b_{B,q}^\epsilon=N_q-r_q^\epsilon
 \le N_q.                                                \tag{4.1}
\]

Define the block-side Hall deficiency

\[
 \delta_q^\epsilon=
 \max_{\mathcal A\subseteq F}
 \left(
  \sum_{B\in\mathcal A}b_{B,q}^\epsilon-
  \left|\bigcup_{B\in\mathcal A}C_q^\epsilon(B)\right|
 \right)_+.                                              \tag{4.2}
\]

### Lemma 4.1 (integral max-flow certificate)

For every `q,epsilon`,

\[
                    M_q^\epsilon
                    \le r_q^\epsilon+\delta_q^\epsilon.  \tag{4.3}
\]

Consequently the deterministic rank-balanced condition

\[
 \boxed{
 \sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
       (r_q^\epsilon+\delta_q^\epsilon)=o(W)}             \tag{4.4}
\]

implies Stage B, and hence Theorem 3.1.

#### Proof

Replace a block `B` by `b_{B,q}^epsilon` left clones, each adjacent to all
targets in `C_q^epsilon(B)`.  The deficiency form of Hall's theorem says
that a maximum matching leaves exactly `delta_q^epsilon` clones unmatched.
It therefore chooses

\[
 N_q-r_q^\epsilon-\delta_q^\epsilon                     \tag{4.5}
\]

distinct occurring targets.  At most `r_q^epsilon+delta_q^epsilon` targets
remain, proving (4.3).  Summing proves (4.4).  QED.

When all quotas are saturated (`r_q^epsilon=0`), the exact feasibility
criterion is

\[
 \left|\bigcup_{B\in\mathcal A}C_q^\epsilon(B)\right|
 \ge\sum_{B\in\mathcal A}b_{B,q}^\epsilon
 \quad\hbox{for every }\mathcal A\subseteq F.             \tag{4.6}
\]

This is a lossless-expansion condition, not ordinary positive expansion.
At depth one its allowed collision budget is only `O(1)` per block.  Exact
fractional rank balance, average degrees, or averaging over coordinate
permutations does not imply (4.6): translating a fixed integral factor
preserves every union size in (4.6) and therefore preserves its deficiency.

Conversely, if no quotas are imposed, there is no matching problem at all.
One occurrence of each covered target may be chosen independently.  The
sole physical condition is the union deficit (2.5).

## 5. Leave, seam, and collision ledgers

The theorem has the following exact audit consequences.

### 5.1 The shadow condition itself forces a near-factor

Because a block has at most `R` depth-one lower colours,

\[
 N_1-M_1^-\le Rt=W-u.                                   \tag{5.1}
\]

Since `W-N_1=W/(m+1)`, Stage B with `M_1^-=o(W)` forces

\[
 u\le\frac{W}{m+1}+M_1^-=o(W).                           \tag{5.2}
\]

Thus a separate near-factor assumption on the leave is harmless but
logically redundant once the full Stage-B deficit is known.  Its exact
literal repair cost is already included in the baseline `W` of (3.4).

### 5.1A The sharp aggregate capacity rate of the middle leave

There are at most `W-u` available window starts at every fixed depth and
sign, even with a full copied collar.  Consequently

\[
 M_q^\epsilon\ge
 \bigl(N_q-(W-u)\bigr)_+
 =\bigl(u-W(1-\rho_q)\bigr)_+ .                         \tag{5.2a}
\]

Thus every block family obeys the exact aggregate capacity lower bound

\[
 \boxed{
 D\ge \Lambda_H(u):=
 2\sum_{q=1}^H\bigl(u-W(1-\rho_q)\bigr)_+.}             \tag{5.2b}
\]

This is sharp if one forgets block geometry and retains only the number of
available starts: use distinct targets until the smaller of `W-u` and
`N_q` is exhausted.

Write `delta=u/W`.  If `delta->0`, `m delta->infinity`, and
`H/sqrt(m delta)->infinity`, then

\[
 \boxed{
 \Lambda_H(u)=\left(\frac43+o(1)\right)
 W\sqrt m\,\delta^{3/2}.}                               \tag{5.2c}
\]

Indeed

\[
 \rho_q=\prod_{j=0}^{q-1}\frac{m-j}{m+j+1},
 \qquad
 1-\rho_q=\frac{q^2}{m}+o(\delta)                       \tag{5.2d}
\]

uniformly for `q=O(sqrt(m delta))`; the second relation follows by expanding
`-log rho_q`, whose error there is
`O(q/m+q^3/m^2)=o(delta)`.  Outside that range the summand in (5.2b) is
zero.  With `Q=(1+o(1))sqrt(m delta)`, summation gives

\[
 2W\sum_{q=1}^{Q}\left(\delta-\frac{q^2}{m}+o(\delta)\right)
 =\left(\frac43+o(1)\right)W\sqrt m\,\delta^{3/2}.
\]

The same product estimate also gives, uniformly in `H`,

\[
 \Lambda_H(u)
 =O\!\left(W\delta+W\sqrt m\,\delta^{3/2}\right).       \tag{5.2e}
\]

Therefore `u=o(Wm^{-1/3})` makes the *forced* shadow loss `o(W)`; this
does not control collisions.  Conversely, under the window scale in
Theorem 3.1, the hypothesis `D=o(W)` necessarily forces

\[
                         u=o(Wm^{-1/3}).                 \tag{5.2f}
\]

To see this, (5.2) first gives `delta=o(1)`.  If `m delta=O(1)`, (5.2f)
is immediate.  On every subsequence with `m delta->infinity`, one has
`H/sqrt(m delta)->infinity` because `H/sqrt m->infinity` and
`delta<=1`; then (5.2b)--(5.2c) and `D=o(W)` imply
`sqrt(m) delta^(3/2)->0`, which is equivalent to (5.2f).

### 5.2 Collision form of the physical deficit

Let `A_q^epsilon` be the total number of available depth-`q`, sign-`epsilon`
window occurrences and let `n_q^epsilon(S)` be the multiplicity of target
`S`.  Put

\[
 C_q^\epsilon=\sum_S(n_q^\epsilon(S)-1)_+ .              \tag{5.3}
\]

Then exactly

\[
 M_q^\epsilon=N_q-A_q^\epsilon+C_q^\epsilon.             \tag{5.4}
\]

Thus Stage B may equivalently be stated as control of collision excess above
the unavoidable slot surplus:

\[
 \sum_{q,\epsilon}
  \bigl(C_q^\epsilon-(A_q^\epsilon-N_q)\bigr)=o(W).       \tag{5.5}
\]

The summands in (5.5) are the nonnegative missing counts, even when the raw
duplicate count `C_q^epsilon` is large in the outer central band.  Quadratic
collision energy or the uncorrected sum of duplicates is not the relevant
objective.

### 5.3 What remains unproved

Neither exact fractional rank balance nor the known middle-block packing
theorems prove (2.8) or (4.4).  The missing theorem is:

> Select the pairwise middle-disjoint, cyclically delay-`H` geodesic
> length-`2ell` blocks so that their simultaneous weighted two-sided shadow
> deficit (2.7), measured after the chosen cuts/collars, is `o(1)`.

This is Stage B in its sharp physical form.  A deterministic flow proves the
representative assignment once the Hall inequalities (4.6) are known, but
flow does not create a target absent from every selected block.  Any proposed
deterministic averaging proof must therefore establish the union inequality
(2.8), or the stronger family of cut inequalities (4.6), for one integral
block packing; symmetric fractional marginals alone are insufficient.

## 6. Proved/conditional boundary

Proved in this note:

* the exact implication and length bound (3.4);
* the finite-boundary contiguous-OR identities (3.9)--(3.11);
* the weighted deficit identity (2.7);
* the exact seam/collar constants (2.9)--(2.11);
* literal middle-leave repair with no `H` multiplier;
* the exact forced-capacity sum (5.2b), its Gaussian constant `4/3`, and
  the necessary `u=o(Wm^(-1/3))` rate under the theorem's window scale;
* the deterministic max-flow certificate (4.3)--(4.4); and
* the deduction from the even-dimensional theorem to all dimensions.

Used as an established external input:

* the truncated-ideal tail bound (3.5).

Still unproved:

* Stage B, namely (2.8), or its stronger quota-flow certificate (4.4), at
  any prescribed `H/sqrt(m)->infinity` scale.

Accordingly this report is a sufficient theorem, not a proof of constant
one.
