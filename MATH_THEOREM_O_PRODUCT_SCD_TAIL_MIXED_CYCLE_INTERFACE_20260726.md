# Factor-blind product-SCD tails for mixed-frame middle cycles

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict and the tensor plug-in

The product-SCD exterior word is completely independent of the middle
factor.  It may be concatenated after arbitrary mixed-frame recoupling,
cycle splitting, exact replacement, or deletion.  It requires no common
frame, owner, endpoint, chronology, phase, or separator.

Define

\[
 A_m(a)=\binom ma-\binom m{a-1},
 \qquad
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0,
 \end{cases}                                             \tag{0.1}
\]

and

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\[1mm]
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0.
 \end{cases}                                             \tag{0.2}
\]

Put

\[
 \boxed{
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
 A_m(a)w_m(a)C_m(r-a).}                                 \tag{0.3}
\]

There is an absolute constant `C_0` such that, for every `m>=1` and
`0<=H<=m-1`,

\[
 \boxed{
 \frac{L_m(m-H-1)}{\binom{2m}m}
 \le C_0\exp\!\left(-\frac{H^2}{8m}\right).}           \tag{0.4}
\]

The word counted by (0.3) covers **both** tails in even dimension.  Its
trimmed one-coordinate lift has length `2L_m(m-H-1)` and covers both tails
in odd dimension.  Consequently

\[
                         \frac H{\sqrt m}\longrightarrow\infty
 \quad\Longrightarrow\quad
 \text{exterior cost}=o(W),                             \tag{0.5}
\]

with no moderate-deviation upper restriction on `H`.

The central tensor interface is as follows.

* In `Q_(2m)`, a retained `H`-safe middle cycle costs its number of middle
  owners plus exactly `2H` collar letters.
* In `Q_(2m+1)`, an `H`-safe alternating `X/Y` cycle, encoded by its
  cyclic `m`-set shore, costs its number of `X` owners plus exactly
  `2H+1` collar letters.
* A legal residual cycle may simply remain as a separate component.  It
  incurs only this collar charge, independently of its owner mass.
* If residual cycles belong to a fully `H`-safe pre-deletion factor,
  balanced multiplicity floors charge total deleted owner mass `r` by
  `O(r sqrt(m))`, uniformly in `H`.
* A mixed-frame junction has zero extra cost if its actual state sequence
  remains `H`-safe.  A junction which is not certified safe must be cut or
  included in the actual central-deficit ledger.  A bare unsafe cut can
  cost `H(H+1)` two-sided shadow occurrences in even dimension and
  `(H+1)^2` in odd dimension.

Thus the tail, component collars, deleted residual cycles, and physical
recoupling seams are four separate ledgers.  Exact middle ownership alone
does not control the remaining central shadow deficit.

## 1. The exact product-SCD exterior word

Split a `2m`-element ground set as `X disjoint-union Y`, with
`|X|=|Y|=m`, and choose arbitrary symmetric-chain decompositions of the two
half-cubes.

A symmetric chain with minimum rank `a` has the form

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a}.
                                                               \tag{1.1}
\]

Writing `C_j setminus C_(j-1)={e_j}`, define its forward increment word

\[
 R(C)=
 \begin{cases}
 \{e_1\},\ldots,\{e_m\},&a=0,\\
 C_a,\{e_{a+1}\},\ldots,\{e_{m-a}\},&a>0,
 \end{cases}                                             \tag{1.2}
\]

and let `L(C)` be its reversal.  Both have length `w_m(a)`.  Every nonempty
member of `C` is the union of a prefix of `R(C)` and also the union of a
suffix of `L(C)`.

The number of half-cube chains of minimum rank `a` is

\[
                         A_m(a)=\binom ma-\binom m{a-1}. \tag{1.3}
\]

For each ordered pair of chains `(C,D)` with minimum ranks `a,b` satisfying

\[
                              a+b\le r,                 \tag{1.4}
\]

emit the literal gadget

\[
                              L(C)\mathbin\Vert R(D).   \tag{1.5}
\]

Concatenate the gadgets in an arbitrary order.

### Theorem 1.1 (simultaneous two-tail coverage)

The word (1.5), over all pairs satisfying (1.4), covers every nonempty set
`S subseteq X union Y` such that

\[
                         |S|\le r
 \quad\hbox{or}\quad
                         |S|\ge2m-r.                   \tag{1.6}
\]

Its exact constructed length is `L_m(r)` from (0.3).

#### Proof

Write `S=S_X disjoint-union S_Y`, and let `C,D` be the unique half-chains
containing `S_X,S_Y`, with minimum ranks `a,b`.

If `|S|<=r`, then `a+b<=|S|<=r`.  If `|S|>=2m-r`, symmetry of the chains
gives

\[
 a\le m-|S_X|,
 \qquad b\le m-|S_Y|,
 \qquad a+b\le2m-|S|\le r.                              \tag{1.7}
\]

Thus the relevant gadget is present.  A suffix of `L(C)` has union `S_X`
and a prefix of `R(D)` has union `S_Y`; their concatenation is one literal
contiguous interval.  If one part is empty, use only the other side.

The total gadget length is

\[
 \sum_{a+b\le r}A_m(a)A_m(b)(w_m(a)+w_m(b)).             \tag{1.8}
\]

The two summands are equal after interchanging the half-cubes, while

\[
 \sum_{b=0}^{\min(t,\lfloor m/2\rfloor)}A_m(b)
 =\binom m{\min(t,\lfloor m/2\rfloor)}.                 \tag{1.9}
\]

Equations (1.8)--(1.9) give (0.3).  \(\square\)

The same gadgets cover both tails.  The leading factor `2` in (0.3) comes
from the two sides of the chain-pair length in (1.8); it is not a second
copy for the upper tail.

### Lemma 1.2 (trimmed odd lift)

If `Q=(Q_1,...,Q_N)` covers a family of nonempty targets on `V`, then, for
a new coordinate `z`,

\[
 Q_1,\ldots,Q_N,\{z\},
 Q_1\cup\{z\},\ldots,Q_{N-1}\cup\{z\}                 \tag{1.10}
\]

has exactly `2N` entries and covers the old family, `{z}`, and every old
target with `z` adjoined.

#### Proof

Old witnesses stay in the first copy.  If an old witness ends before
`Q_N`, use its translated copy in the last block.  If it ends at `Q_N`, use
the corresponding suffix in the first copy followed by `{z}`.  \(\square\)

At `r=m-H-1`, Theorem 1.1 covers every even-dimensional rank outside

\[
                              [m-H,m+H],                \tag{1.11}
\]

and Lemma 1.2 covers every odd-dimensional rank outside

\[
                              [m-H,m+H+1].              \tag{1.12}
\]

### Theorem 1.3 (uniform exponential tail)

Equation (0.4) holds uniformly for every `0<=H<=m-1`.  Consequently the
even exterior word has length `o(binomial(2m,m))`, and the odd exterior word
has length `o(binomial(2m+1,m))`, whenever `H/sqrt(m)->infinity`.

#### Proof

Put

\[
 h=\lfloor m/2\rfloor,
 \qquad \epsilon=m-2h,
 \qquad x=h-a,
 \qquad d=H+1-\epsilon.                                 \tag{1.13}
\]

For `0<=x<h`, direct subtraction in (1.3) gives

\[
 B_{m,x}:=A_m(h-x)w_m(h-x)
 =\binom m{h-x}
 \frac{(2x+\epsilon+1)^2}{h+x+\epsilon+1},             \tag{1.14}
\]

while `B_(m,h)=m`.  The exact parity-uniform form of (0.3) is

\[
 L_m(m-H-1)
 =2\sum_{x=0}^{h}B_{m,x}
 \binom m{h-(d-x)_+},                                   \tag{1.15}
\]

and

\[
                              \sum_{x=0}^{h}B_{m,x}=2^m-1. \tag{1.16}
\]

The elementary central-ratio estimate is

\[
 \frac{\binom m{h-y}}{\binom mh}\le e^{-y^2/m}
 \qquad(0\le y\le h).                                  \tag{1.17}
\]

It follows by writing the ratio as a product of successive binomial ratios
and using `log(1-u)<=-u`.  Equations (1.14) and (1.17) imply

\[
 \frac{B_{m,x}}{\binom mh}
 \le\frac{8(x+1)^2}{m}e^{-x^2/m}
 \qquad(x<h).                                           \tag{1.18}
\]

Split (1.15) at `t=floor(d/2)`.  For `x<=t`, the second binomial in (1.15)
is at most

\[
                         \binom mh e^{-H^2/(4m)}.       \tag{1.19}
\]

Using (1.16), this part divided by `binomial(2m,m)` is

\[
 O\!\left(
  \frac{2^m\binom mh}{\binom{2m}m}e^{-H^2/(4m)}
 \right).                                               \tag{1.20}
\]

For `x>t`, use

\[
 e^{-x^2/m}\le e^{-H^2/(8m)}e^{-x^2/(2m)}.             \tag{1.21}
\]

Equations (1.15) and (1.18) bound this part, after normalization, by

\[
 O\!\left(
 \frac{\binom mh^2}{\binom{2m}m}
 e^{-H^2/(8m)}
 \left[\frac1m\sum_{x\ge0}(x+1)^2e^{-x^2/(2m)}\right]
 \right).                                               \tag{1.22}
\]

The bracket is `O(sqrt(m))`.  Wallis' inequalities give

\[
 \frac{2^m\binom mh}{\binom{2m}m}=O(1),
 \qquad
 \frac{\binom mh^2\sqrt m}{\binom{2m}m}=O(1).          \tag{1.23}
\]

The exceptional `x=h` term is exponentially smaller.  Equations
(1.20)--(1.23) prove (0.4).  Finally

\[
 \binom{2m+1}m=\frac{2m+1}{m+1}\binom{2m}m             \tag{1.24}
\]

proves the normalized odd assertion.  \(\square\)

No hypothesis `H<=m/2` or `H=o(m^(2/3))` was used.  If `H>=m`, the exterior
family is empty and its charge may be taken to be zero.

For comparison with the older truncated-ideal shorthand, put
`W=binomial(2m,m)` and

\[
 \rho_H=\frac{\binom{2m}{m-H}}{\binom{2m}m}.
\]

The exact product formula gives

\[
 \rho_H
 =\prod_{j=0}^{H-1}\frac{m-j}{m+j+1}
 \le\exp\!\left(-\frac{H^2}{m+H}\right)
 \le\exp\!\left(-\frac{H^2}{2m}\right).               \tag{1.25}
\]

Hence

\[
 \left(1+\frac{H^2}{m}\right)\binom{2m}{m-H}=o(W)     \tag{1.26}
\]

whenever `H/sqrt(m)->infinity`.  Conversely, if `H/sqrt(m)` has a bounded
subsequence, pass to one on which it tends to `c<infinity`; then
`rho_H->e^(-c^2)`, and the normalized right side of (1.26) tends to
`(1+c^2)e^(-c^2)>0`.  Thus `H/sqrt(m)->infinity` is exactly the threshold
for that familiar envelope.  Only the forward implication is needed below.

## 2. Concatenation is the whole product-tail interface

For a literal word `U`, let `Cov(U)` be its family of contiguous interval
unions.  For arbitrary words `U,V`,

\[
                    \operatorname{Cov}(U)\cup
                    \operatorname{Cov}(V)
 \subseteq          \operatorname{Cov}(U\Vert V).      \tag{2.1}
\]

Indeed, an interval internal to either word stays contiguous after
concatenation.  Cross-interface intervals may create additional targets but
cannot destroy an old witness.

### Theorem 2.1 (parity-neutral black-box composition)

Let `A_(m,H)` be any literal central word and `R_(m,H)` any literal repair
word for its residual central targets.  Then

\[
 \boxed{
 \nu(2m)\le |A_{m,H}|+|R_{m,H}|+L_m(m-H-1)}             \tag{2.2}
\]

provided the first two words cover ranks `[m-H,m+H]`, and

\[
 \boxed{
 \nu(2m+1)\le |A_{m,H}|+|R_{m,H}|+2L_m(m-H-1)}         \tag{2.3}
\]

provided they cover ranks `[m-H,m+H+1]`.

There is exactly zero additional `A`--tail seam charge.

#### Proof

Concatenate `A_(m,H)`, `R_(m,H)`, and the appropriate exterior word from
Section 1, and apply (2.1).  \(\square\)

This proves factor-blindness in its strongest form: the product tail does
not even require Stage A to arise from a factor.

## 3. Finite factorization of arbitrary geodesic middle components

The next lemma is the only literal-word input needed from a middle cycle.
It depends on the actual state sequence, not on the frame which produced
it.

Let

\[
                         T=(T_1,\ldots,T_v)             \tag{3.1}
\]

be a linear sequence of subsets of one ground set.  Say that `T` is
**delay-`H` safe** if no coordinate changes twice in any block of at most
`H+1` consecutive transitions.  Equivalently, every internal positive
coordinate run has at least `H+1` states.  Boundary runs may be shorter.
The “at most” clause is needed for path remnants having fewer than `H+1`
transitions; the condition is not intended to be vacuous there.

Define

\[
 A_j=\bigcap_{i=\max(1,j-H)}^{\min(v,j)}T_i,
 \qquad 1\le j\le v+H.                                  \tag{3.2}
\]

### Lemma 3.1 (finite delay factor)

For every `1<=i<=v`,

\[
                         T_i=\bigcup_{j=i}^{i+H}A_j.    \tag{3.3}
\]

For every `1<=a<=b<=v` with `b-a<=H`,

\[
 \bigcap_{i=a}^{b}T_i=\bigcup_{j=b}^{a+H}A_j.           \tag{3.4}
\]

For every `1<=a<=b<=v`, with **no restriction on `b-a`**,

\[
 \bigcup_{i=a}^{b}T_i=\bigcup_{j=a}^{b+H}A_j.           \tag{3.5}
\]

Hence every displayed intersection or union is a literal contiguous OR in
the factor word `(A_1,...,A_(v+H))`.

#### Proof

Fix one coordinate and examine its binary state row.  If it is one at
position `i`, the positive run containing `i` either reaches a boundary or
has at least `H+1` states.  It therefore contains one defining window for
some `A_j` with `i<=j<=i+H`.  This proves the nontrivial direction of
(3.3); the reverse direction is immediate because every such defining
window contains `i`.

If the coordinate is one throughout `[a,b]` and `b-a<=H`, the same run
contains a defining window whose right endpoint `j` lies in
`[b,a+H]`.  Conversely every defining window with such an endpoint contains
`[a,b]`.  This proves (3.4).

Finally, take the union of (3.3) over `a<=i<=b`.  The union of the index
intervals `[i,i+H]` is exactly `[a,b+H]`, proving (3.5) without any
restriction on the length of `[a,b]`.  \(\square\)

The unrestricted range in (3.5) is important for the odd `X/Y` compiler:
an upper depth-`H` target uses `H+2` consecutive `X`-states, although the
factor delay remains `H`.

Empty factor entries may be deleted after all witnesses are fixed.  The
remaining entries of every old witness stay consecutive and retain their
union.

### Corollary 3.2 (path and cycle costs)

A delay-`H` safe path of `v` middle states has a literal factor word of
length `v+H` covering all its internal lower intersections through depth
`H` and all its internal upper unions.

If `(X_i)_(i mod v)` is cyclically delay-`H` safe, cut it once and copy its
first `H` states.  Lemma 3.1 gives a word of length

\[
                              v+2H                       \tag{3.6}
\]

which covers every cyclic intersection and union of at most `H+1`
states.  More generally, copying only `0<=sigma<=H` prefix states gives
length

\[
                              v+H+\sigma.               \tag{3.7}
\]

At signed depth `q`, exactly `(q-sigma)_+` cyclic starts are unavailable.

#### Proof

The path statement is Lemma 3.1.  In the cyclic case, copying `H` prefix
states makes every cyclic window of at most `H` transitions an ordinary
linear interval.  With only `sigma` copied states, the `q` wraparound
windows require respectively `1,...,q` copied states, so precisely the last
`(q-sigma)_+` remain unavailable.  \(\square\)

## 4. Even-dimensional exact cycle theorem

Put

\[
 W=\binom{2m}m,
 \qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.                  \tag{4.1}
\]

Let `F` be any exact middle cycle factor: its pairwise vertex-disjoint
oriented cycles

\[
 C=(X_0,\ldots,X_{\lambda_C-1}),
 \qquad X_i\in\binom{[2m]}m,                            \tag{4.2}
\]

partition all `W` middle sets.  Delete an arbitrary union of complete
cycles of total middle-owner mass `r`, and assume every **retained** cycle
is cyclically delay-`H` safe.  In particular, every retained cyclic segment
of `q<=H` transitions is a Johnson geodesic.  Define its lower and upper
flags by

\[
 L_{i,q}=\bigcap_{j=0}^{q}X_{i+j},
 \qquad
 U_{i,q}=\bigcup_{j=0}^{q}X_{i+j}.                     \tag{4.3}
\]

They have ranks `m-q` and `m+q`.

For each retained cycle choose a copied-prefix length

\[
                              0\le\sigma_C\le H.        \tag{4.4}
\]

Let `M_q^-` and `M_q^+` be the actual numbers of lower and upper targets
not represented by the surviving certified windows, and put

\[
                        D_H^{\rm ret}
                        =\sum_{q=1}^H(M_q^-+M_q^+).     \tag{4.5}
\]

### Theorem 4.1 (direct-support cycle/tail interface)

For every such factor, deletion, and collar choice,

\[
 \boxed{
 \nu(2m)\le
 W+\sum_{C\ \mathrm{retained}}(H+\sigma_C)
 +D_H^{\rm ret}+L_m(m-H-1).}                           \tag{4.6}
\]

In particular, full collars give

\[
 \boxed{
 \nu(2m)\le W+2H K+D_H^{\rm ret}+L_m(m-H-1)}           \tag{4.7}
\]

where `K` is the number of retained cycles.

#### Proof

By Corollary 3.2, a retained cycle `C` contributes
`lambda_C+H+sigma_C` factor letters.  The total retained middle mass is
`W-r`, so all retained cycle words have total length

\[
                    (W-r)+\sum_C(H+\sigma_C).           \tag{4.8}
\]

Append the `r` deleted middle sets once each.  This restores the baseline
to exactly

\[
                         W+\sum_C(H+\sigma_C).          \tag{4.9}
\]

Thus the middle leave cancels exactly; it has no multiplicative `H` charge.
Append every missing certified central shadow once, at cost
`D_H^(ret)`, and append the independent exterior word.  Theorem 2.1 proves
(4.6).  \(\square\)

The direct-support form is the logically sharp factor-blind theorem.  It
does not assume any quota or balance property.

## 5. Floor-buffer leave theorem

For the stronger floor-buffer certificate in this section, assume in
addition that **every** cycle of the full pre-deletion factor `F`, including
the cycles later deleted, is cyclically delay-`H` safe.  Thus its two signed
depth-`q` histograms are rank-correct and have total mass exactly `W`.

For `1<=q<=H`, put

\[
                         c_q=\left\lfloor\frac W{N_q}\right\rfloor. \tag{5.1}
\]

A balanced quota on either signed rank takes values in `{c_q,c_q+1}` and
has total mass `W`.  Let `mu_q^+` and `mu_q^-` be the two occurrence
histograms of the full, pre-deletion exact factor.  Both have total mass
`W`.  Define

\[
 O_q^\pm(F)=
 \min_{b_q}\sum_S(\mu_q^\pm(S)-b_q(S))_+,              \tag{5.2}
\]

where the minimum is over balanced quotas, and put

\[
 J_H(F)=\sum_{q=1}^H\frac{O_q^-(F)+O_q^+(F)}{c_q},
 \qquad
 S_H=\sum_{q=1}^H\frac1{c_q}.                          \tag{5.3}
\]

### Lemma 5.1 (floor-buffer deletion)

Let `mu` be a nonnegative integral vector of total mass `W`, let
`b in {c,c+1}^X` have total mass `W`, and let `0<=delta<=mu`.  Then

\[
 \boxed{
 c\,|\{S:(\mu-\delta)(S)=0\}|
 \le\sum_S(b(S)-\mu(S))_++\|\delta\|_1.}              \tag{5.4}
\]

#### Proof

At a new hole, `mu(S)=delta(S)` and

\[
 c\le b(S)\le(b(S)-\mu(S))_++\delta(S).                \tag{5.5}
\]

Sum over the holes and enlarge the first sum to all coordinates.  \(\square\)

Since `mu` and `b` have equal total mass, overload equals underload for a
minimizing quota.

### Lemma 5.2 (uniform reciprocal floors)

Uniformly for every `H<=m`,

\[
 \boxed{
 S_H\le\frac{4^m}{W}-1
       =(\sqrt\pi+o(1))\sqrt m.}                       \tag{5.6}
\]

#### Proof

For every `x>=1`, `1/floor(x)<=2/x`; hence `1/c_q<=2N_q/W`.  Also

\[
 \sum_{q=1}^{m}N_q=\frac{4^m-W}{2}.                    \tag{5.7}
\]

Sum and use the central-binomial asymptotic.  \(\square\)

### Theorem 5.3 (exact partial-collar leave certificate)

Under the hypotheses of Theorem 4.1,

\[
 \boxed{\begin{aligned}
 \nu(2m)\le{}&
 W+\sum_{C\ \mathrm{retained}}(H+\sigma_C)
 +J_H(F)+2rS_H\\
 &+2\sum_{C\ \mathrm{retained}}\sum_{q=1}^H
       \frac{(q-\sigma_C)_+}{c_q}
 +L_m(m-H-1).
 \end{aligned}}                                        \tag{5.8}
\]

Full collars give the clean form

\[
 \boxed{
 \nu(2m)\le
 W+2HK+J_H(F)+2rS_H+L_m(m-H-1).}                       \tag{5.9}
\]

#### Proof

Deleting complete cycles of total mass `r` removes exactly `r` occurrences
at every depth and sign.  At depth `q`, a partial collar on `C` removes
exactly `(q-sigma_C)_+` further cyclic starts.  Apply Lemma 5.1 separately
to the two signed histograms.  It gives

\[
 M_q^-+M_q^+
 \le\frac{O_q^-(F)+O_q^+(F)+2r
 +2\sum_C(q-\sigma_C)_+}{c_q}.                         \tag{5.10}
\]

Sum (5.10) and substitute it for the actual deficit in (4.6).  \(\square\)

Thus the uniform balanced size-only deletion rate is

\[
                              r=o(W/\sqrt m).           \tag{5.11}
\]

Without the balanced-overload hypothesis and with full collars, deletion of
owner mass `r` can create at most one new hole per deleted occurrence, at
every sign and depth.  Therefore the direct support inequality is

\[
 D_H^{\rm ret}\le D_H^{\rm full}+2Hr,                  \tag{5.12}
\]

and `r=o(W/H)` is the corresponding crude size-only sufficient rate.  A
structured larger leave is allowed whenever its actual deficit in (4.5) is
`o(W)`.

## 6. Mixed-frame recoupling and unsafe seams

The phrase “mixed frame” carries no cost by itself.  Only the resulting
successor word matters.

Let `F` and `F'` be two exact cyclic factors on the same middle owners, and
suppose their directed successor maps differ at `s` owner positions.  At
signed depth `q`, a window changes only if one of its `q` transitions uses
one of those positions.  Hence at most `sq` occurrence slots change.
Therefore

\[
 \frac12\|\mu_q^\pm(F')-\mu_q^\pm(F)\|_1\le sq.        \tag{6.1}
\]

For equal-mass histograms,

\[
 O_q^\pm(\mu)=\frac12\min_{b_q}\|\mu-b_q\|_1.          \tag{6.2}
\]

Distance to a fixed set is one-Lipschitz, so

\[
 J_H(F')\le J_H(F)+2sQ_H,
 \qquad
 Q_H:=\sum_{q=1}^H\frac q{c_q}.                        \tag{6.3}
\]

The weighted seam moment has an exact uniform bound.

### Lemma 6.1 (even recoupling moment)

For every `H<=m`,

\[
 \boxed{2Q_H\le2m.}                                    \tag{6.4}
\]

#### Proof

Again `1/c_q<=2N_q/W`.  The exact binomial moment identity is

\[
 \sum_{q=1}^{m}q\binom{2m}{m-q}
 =\frac m2\binom{2m}m.                                 \tag{6.5}
\]

It follows, for example, by writing `q=m-k`, using
`(m-k)binomial(2m,k)=m[binomial(2m-1,k)-binomial(2m-1,k-1)]`, and
telescoping over `0<=k<m`.  Equations (6.4)--(6.5) follow.  \(\square\)

Consequently

\[
                         J_H(F')\le J_H(F)+2ms.         \tag{6.6}
\]

This term is needed only when one transfers a pre-recoupling estimate.  If
`J_H(F')` or the actual post-recoupling deficit is measured directly, the
history and `s` disappear completely.

### Unsafe-junction caveat

The recoupled factor must still be delay-`H` safe for Theorem 4.1.  A new
Johnson edge is not automatically safe with the preceding and following
`H` transitions.  If a junction cannot be certified, cut there.  A bare
cut has factor overhead `H`, but at depth `q` it removes `q` cyclic starts
on each side.  Thus its raw two-sided shadow charge is at most

\[
                        2\sum_{q=1}^Hq=H(H+1).          \tag{6.7}
\]

With `b` such cuts, the completely unweighted support estimate is

\[
             D_H^{\rm cut}\le D_H^{\rm cyclic}+H(H+1)b. \tag{6.8}
\]

The balanced-floor version replaces (6.7) by `2Q_H<=2m`, so its total
collateral is at most `2mb`.  Therefore

\[
 b=o(W/H^2)                                             \tag{6.9}
\]

is the crude support-blind rate, while

\[
 b=o(W/m)                                               \tag{6.10}
\]

is the weighted-floor rate.  Merely asserting `b=o(W/H)` is insufficient
unless the crossing shadows are certified or already included in the
actual deficit.

## 7. Residual cycles should normally be retained

Suppose the post-recoupling exact factor consists of `K` main cycles and
`z` additional legal residual cycles `R_1,...,R_z`, with owner masses
`r_1,...,r_z`.  There are two factor-blind choices.

1. Retain residual cycle `R_i`; its exact full-collar charge is `2H`.
2. Delete it; its middle leave cancels from the baseline, and its
   floor-buffer shadow charge is at most `2r_iS_H`.

Choosing independently gives

\[
 \boxed{\begin{aligned}
 \nu(2m)\le{}&W+2HK+J_H(F)
 +2\sum_{i=1}^z\min\{H,r_iS_H\}\\
 &+L_m(m-H-1).
 \end{aligned}}                                        \tag{7.1}
\]

In the direct-support ledger, replace `J_H` and every deletion certificate
by the actual resulting deficit.

If every main and residual cycle has length at least `2ell`, retaining all
cycles gives

\[
 2H(K+z)\le\frac H\ell W.                              \tag{7.2}
\]

Thus `H/ell->0` makes even a linear residual owner mass harmless.  More
generally the exact residual-cycle requirement is

\[
                              Hz=o(W).                  \tag{7.3}
\]

If deletion is forced, total residual owner mass `r=sum_i r_i` is harmless
under `r=o(W/sqrt(m))` with floor balance, or under `r=o(W/H)` using only
raw support.

In particular, suppose an Ordered-Hall or successor-cover theorem supplies
a defect number `Delta` for which the residual cycles have total owner mass
at most `Delta` and count `z`.  The exact factor-blind residual term may be
taken to be

\[
                         2\min\{Hz,\ \Delta S_H\}.      \tag{7.3a}
\]

This is the only way the routing defect enters the exterior interface; no
shape or frame information about the residual cycles is used.

If a tensor construction instead outputs `p` delay-`H` safe open path
remnants and `z` safe closed cycles covering `W-u` owners, Lemma 3.1 gives
the exact direct-support bound

\[
 \boxed{
 \nu(2m)\le
 W+Hp+2Hz+D_H^{\rm actual}+L_m(m-H-1).}                \tag{7.4}
\]

Here `D_H^(actual)` is computed only from the surviving internal path
windows and the cyclic windows of the retained cycles.  Equation (7.4)
does not silently assume that a broken boundary remains certified.

## 8. Odd alternating `X/Y` cycle interface

This is the form directly compatible with an exact middle-level tensor
factor on `n=2m+1` coordinates.  Put

\[
 W=\binom{2m+1}m,
 \qquad
 N_q=\binom{2m+1}{m-q}
     =\binom{2m+1}{m+1+q},
 \qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor.           \tag{8.1}
\]

Encode an alternating middle-level cycle by a cyclic `m`-set sequence
`(X_i)` such that

\[
                              Y_i=X_i\cup X_{i+1}.      \tag{8.2}
\]

An exact `X/Y` cycle factor means that the `X_i` occurrences partition rank
`m` and the `Y_i` occurrences partition rank `m+1`.

At depth `q`, define

\[
 L_{i,q}=\bigcap_{j=0}^qX_{i+j},
 \qquad
 U_{i,q}=\bigcup_{j=0}^{q+1}X_{i+j}.                  \tag{8.3}
\]

The lower target has rank `m-q`, while the upper target has rank
`m+1+q`.  Assume every `H+1` consecutive cyclic transitions form a Johnson
geodesic.  Lemma 3.1 with delay `H` represents all lower intersections.
Its union identity (3.5) is unrestricted in interval length, so it also
represents the `H+2`-state upper window at `q=H`.

After cutting a cycle, copy `H+1` prefix states to preserve every upper
wraparound window.  The resulting linear row has `lambda+H+1` states, and
the delay factor adds `H` more letters.  Hence the exact full-collar cycle
cost is

\[
                              \lambda+2H+1.             \tag{8.4}
\]

This `2H+1` constant is not an off-by-one: the extra copied state is needed
on the upper side, whereas the factor delay remains `H`.

For the two signed histograms at `1<=q<=H`, define `O_q^pm`, `J_H`, and
`S_H` exactly as in (5.2)--(5.3).

### Theorem 8.1 (full-collar odd tensor interface)

After arbitrary exact, `H`-safe mixed-frame recoupling, delete complete
alternating cycles of total `X`-owner mass `r` and retain `K` cycles.  Then

\[
 \boxed{
 \nu(2m+1)\le
 W+(2H+1)K+r+J_H(F)+2rS_H
 +2L_m(m-H-1).}                                        \tag{8.5}
\]

The exact direct-support version replaces `J_H+2rS_H` by the actual total
lower and upper holes at depths `1,...,H`.

#### Proof

The retained factor words have length

\[
                         (W-r)+(2H+1)K.                 \tag{8.6}
\]

Deleting whole alternating cycles removes `r` distinct rank-`m` owners and
`r` distinct rank-`m+1` owners.  Appending both middle shores costs `2r`,
so the baseline becomes

\[
                         W+(2H+1)K+r.                  \tag{8.7}
\]

At each positive depth and sign, deletion removes exactly `r` occurrences.
Lemma 5.1 bounds all remaining holes by

\[
 \sum_{q=1}^H(M_q^-+M_q^+)
 \le J_H(F)+2rS_H.                                     \tag{8.8}
\]

Append those holes and the odd product-SCD word.  \(\square\)

The extra `+r`, absent in even dimension, is necessary in this literal
ledger because both middle shores must be repaired.

For odd ranks,

\[
 \boxed{
 S_H\le\frac{2\cdot4^m}{W}-2
       =(\sqrt\pi+o(1))\sqrt m.}                      \tag{8.9}
\]

Indeed `1/c_q<=2N_q/W` and
`sum_(q=1)^m N_q=4^m-W`.

### Theorem 8.2 (exact odd partial collars)

Choose `0<=sigma_C<=H+1` copied prefix states on each retained cycle.  Its
factor seam is `H+sigma_C`.  At depth `q`, the exact unavailable counts are

\[
 (q-\sigma_C)_+
 \quad\hbox{on the lower side},
 \qquad
 (q+1-\sigma_C)_+
 \quad\hbox{on the upper side}.                         \tag{8.10}
\]

Let `z_0` be the number of cycles with `sigma_C=0`; each such bare cut also
loses its wraparound `Y` owner.  Then

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&
 W+\sum_C(H+\sigma_C)+r+z_0+J_H(F)\\
 &+\sum_{q=1}^H\frac{
 2r+\sum_C\bigl((q-\sigma_C)_+
                 +(q+1-\sigma_C)_+\bigr)}{c_q}\\
 &+2L_m(m-H-1).
 \end{aligned}}                                        \tag{8.11}
\]

Full collars `sigma_C=H+1` reduce (8.11) to (8.5).  A bare odd cut loses
exactly

\[
 1+\sum_{q=1}^H(2q+1)=(H+1)^2                         \tag{8.12}
\]

raw occurrences over the two shores, including the lost middle `Y` owner.

### Corollary 8.3 (standard odd cyclic rows)

Let `n=2m+1`, `B=W/n`, and suppose every cycle row has `X`-length `n`.
Deleting `R` complete rows means `r=nR`, and Theorem 8.1 is equivalently

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&
 (B-R)(n+2H+1)+J_H(F)\\
 &+2nR(1+S_H)+2L_m(m-H-1).
 \end{aligned}}                                        \tag{8.13}
\]

For a complement-symmetric wreath factor the two signed overloads are
equal, so `J_H(F)` here is twice the usual one-sided weighted overload.
Thus (8.13) is exactly the standard arbitrary-row deletion interface, now
seen as a specialization of the mixed-cycle theorem.

### Corollary 8.4 (odd cycle/path remnants, actual-deficit form)

Let `p` delay-`H` safe open `X`-paths and `z` cyclically safe closed
`X/Y` cycles be pairwise owner-disjoint and cover `W-u` rank-`m` owners.
Let `M_0^+` be the actual number of rank-`m+1` targets not represented by
the internal path edges or cyclic edges, and for `q>=1` let `M_q^pm` be the
actual signed deficits of the surviving windows.  Then

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&W+Hp+(2H+1)z+M_0^+\\
 &+\sum_{q=1}^H(M_q^-+M_q^+)
 +2L_m(m-H-1).
 \end{aligned}}                                        \tag{8.14}
\]

#### Proof

Lemma 3.1 gives `v+H` factor letters for an open path, while (8.4) gives
`v+2H+1` for a closed cycle.  Their total base is

\[
                         (W-u)+Hp+(2H+1)z.             \tag{8.15}
\]

Append the `u` omitted rank-`m` owners, the actual missing upper-middle
targets, the positive-depth holes, and the odd exterior word.  \(\square\)

If the paths arise by making `p` bare cuts in a pre-cut exact cycle factor
without deleting `X` owners, then `M_0^+<=p`.  Hence their baseline seam is
at most `(H+1)p`; their full raw cut ledger through depth `H` is
`(H+1)^2p`.  Transferring a balanced pre-cut estimate instead costs
`O(mp)`.  Thus path remnants must use (8.14) or these explicit cut charges;
they are not covered silently by the complete-cycle deletion theorem.

## 9. Odd recoupling moment and residual cycles

Suppose two exact odd `X/Y` factors have successor maps differing at `s`
directed `X` positions.  A lower depth-`q` window uses `q` transitions and
an upper depth-`q` window uses `q+1`.  The same `L^1` argument as in
Section 6 gives

\[
 J_H(F')\le J_H(F)
 +s\sum_{q=1}^H\frac{2q+1}{c_q}.                       \tag{9.1}
\]

The exact odd binomial moment is

\[
 \sum_{q=1}^{m}(2q+1)\binom{2m+1}{m-q}
 =m\binom{2m+1}m.                                      \tag{9.2}
\]

Indeed, with `k=m-q` and `n=2m+1`,

\[
 (2q+1)\binom nk=(n-2k)\binom nk
 =n\left(\binom{n-1}k-\binom{n-1}{k-1}\right).        \tag{9.2a}
\]

Summing over `0<=k<m` telescopes to
`n binomial(2m,m-1)=m binomial(2m+1,m)`.

Using `1/c_q<=2N_q/W`,

\[
 \boxed{
 \sum_{q=1}^H\frac{2q+1}{c_q}\le2m}
 \qquad
 J_H(F')\le J_H(F)+2ms.                                \tag{9.3}
\]

Thus `s=o(W/m)` transfers an `o(W)` overload bound across arbitrary choices
of recoupled junctions, provided the resulting cycles are physically
`H`-safe.  Direct measurement of the post-recoupling `J_H` removes this
term.

If an odd recoupling junction is not `H`-safe and is cut bare, it adds `H`
factor letters and loses one middle `Y` owner together with `2q+1` signed
positive-depth occurrences at depth `q`.  Its exact raw repair ceiling is
therefore `(H+1)^2`, as in (8.12).  With balanced floors, the q-zero loss
plus (9.3) is at most `(2m+1)` per cut.  Hence `b=o(W/m)` is again the
uniform weighted sufficient rate for `b` uncertified odd cuts.

If there are `z` additional legal residual `X/Y` cycles with `X`-masses
`r_i`, retaining residual cycle `i` costs `2H+1`; deleting it costs the
factor-blind ledger

\[
                         r_i+2r_iS_H.                   \tag{9.4}
\]

Thus the sharp componentwise upper choice is

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&W+(2H+1)K+J_H(F)\\
 &+\sum_{i=1}^z
   \min\{2H+1,\ r_i(1+2S_H)\}\\
 &+2L_m(m-H-1),
 \end{aligned}}                                        \tag{9.5}
\]

where `K` counts the nonresidual retained cycles.

If every alternating cycle has total middle-level length `2ell`, hence
`X`-shore length `ell`, retaining all main and residual cycles gives

\[
                  (2H+1)(K+z)\le\frac{2H+1}{\ell}W.   \tag{9.6}
\]

Accordingly `H/ell->0` kills the whole cycle collar even if residual cycles
carry a linear proportion of the owners.  If only the residual-cycle count
is controlled, the exact condition is `Hz=o(W)`.  If deletion is forced,
`sum_i r_i=o(W/sqrt(m))` is sufficient.

If a successor-cover defect `Delta` bounds the total residual `X`-owner
mass and `z` bounds the residual-cycle count, the odd residual term is

\[
 \min\{(2H+1)z,\ \Delta(1+2S_H)\}.                     \tag{9.7}
\]

Again this depends only on the two scalar defect ledgers, not on the
recoupling frames.

## 10. Constant-one corollaries

### Corollary 10.1 (even tensor architecture)

Let `H=H_m` and `ell=ell_m`.  Suppose a mixed-frame construction, after all
recoupling and before deletion, produces an exact cyclic factor in
`Q_(2m)` such that:

1. every cycle of this pre-deletion factor, including every cycle later
   deleted, is cyclically delay-`H` safe;
2. every main cycle has length at least `2ell`;
3. its post-recoupling, pre-deletion weighted overload satisfies
   `J_H=o(W)`;
4. an arbitrary union of complete residual cycles, of total owner mass
   `r=o(W/sqrt(m))`, is deleted; and
5. retained short residual cycles have count `z=o(W/H)`.

If

\[
 \frac H{\sqrt m}\longrightarrow\infty,
 \qquad
 \frac H\ell\longrightarrow0,                          \tag{10.1}
\]

then

\[
                         \nu(2m)\le W+o(W).             \tag{10.2}
\]

If `J_H` is known only before changing `s` successor positions, add the
sufficient condition `s=o(W/m)`.

#### Proof

The main collars are at most `(H/ell)W=o(W)` by (7.2); short residual
collars are `o(W)` by hypothesis.  Lemma 5.2 makes the deletion term
`O(r sqrt(m))=o(W)`, while `J_H=o(W)`.  Theorem 1.3 makes the exterior word
`o(W)`.  Substitute in Theorem 5.3 or (7.1).  \(\square\)

### Corollary 10.2 (odd `X/Y` tensor architecture)

Under the odd analogues of the preceding hypotheses—exactness and `J_H`
measured after recoupling and before deletion, every cycle in that factor
`H`-safe, and deletion restricted to complete alternating cycles—with cycle
`X`-length at least `ell`, one has

\[
 \frac H{\sqrt m}\to\infty,qquad
 \frac H\ell\to0,qquad
 J_H=o(W),qquad
 r=o(W/\sqrt m),qquad
 Hz=o(W)
 \quad\Longrightarrow\quad
 \nu(2m+1)\le W+o(W).                                  \tag{10.3}
\]

Again `s=o(W/m)` suffices if the overload estimate is transferred from a
pre-recoupling factor.

#### Proof

Use (8.5), (8.9), (9.3), (9.6), and the odd half of Theorem 1.3.  The
additional odd middle-leave term `r` is already `o(W)` under
`r=o(W/sqrt(m))`.  \(\square\)

### Corollary 10.3 (actual-deficit form)

The overload hypotheses in Corollaries 10.1--10.2 may be replaced by the
strictly more direct condition that the actual post-deletion central repair
family is `o(W)` and that the compiled central word has length `W+o(W)`.
For the odd theorem this repair family includes both missing middle shores,
so it automatically detects the extra `+r` in (8.5).  In that black-box
form, no pre-deletion balance, recoupling count, or separate deletion-rate
hypothesis is logically required.  Those quantities are only uniform
sufficient certificates for the two actual conditions.

## 11. Fixed-window diagonalization

At a fixed Gaussian window `H_A=ceil(A sqrt(m))`, (0.4) gives only a
constant depending on `A`; the exterior word is not yet `o(W)` when `A` is
fixed.  Suppose the central tensor estimates hold for every fixed integer
`A`, with normalized error `epsilon_A(m)->0` as `m->infinity`.  Choose
thresholds `M_A` so that `epsilon_A(m)<=1/A` for `m>=M_A`, and then choose a
slow integer function `A=A(m)->infinity` with `m>=M_(A(m))` and all seam,
leave, and local-geodesicity scale restrictions still valid.  Put

\[
                         H_m=\lceil A(m)\sqrt m\rceil.  \tag{11.1}
\]

Then the central error is `o(W)` and Theorem 1.3 gives

\[
 \frac{\text{tail}}W
 \le C_0e^{-A(m)^2/8}=o(1).                            \tag{11.2}
\]

Thus the theorem plugs directly into a fixed-window tensor construction;
no uniform-in-growing-`A` central theorem is needed.

## 12. Exact implication boundary and independent audit

The following statements are proved.

1. The product-SCD word literally covers both exterior tails at the exact
   charges `L_m(m-H-1)` in even dimension and `2L_m(m-H-1)` in odd
   dimension.
2. Its normalized charge is at most `C_0 exp(-H^2/(8m))` for every
   `0<=H<=m-1`; `H/sqrt(m)->infinity` is sufficient without an upper
   moderate-deviation hypothesis.
3. The product-tail concatenation seam costs exactly zero.
4. Mixed frames themselves cost nothing.  The post-recoupling state
   sequences need only satisfy the stated local geodesicity condition.
5. Full cycle collars cost exactly `2H` in even dimension and `2H+1` for
   odd alternating `X/Y` cycles.
6. A legal residual cycle can be retained independently; no global fusion
   is needed.
7. The literal middle leave cancels in even dimension.  In odd dimension,
   deleting `r` alternating-cycle owners leaves the necessary extra `+r`
   because both middle shores are lost.
8. For a fully `H`-safe pre-deletion factor, balanced floors reduce an
   arbitrary whole-cycle deletion from the crude `O(Hr)` shadow charge to
   `O(r sqrt(m))`.
9. A recoupling estimate transferred across `s` changed successors incurs
   at most `2ms`; direct post-recoupling measurement incurs none.

The following statements are not proved and must not be inferred.

1. Exact middle ownership does not imply `D_H=o(W)` or `J_H=o(W)`.
2. A frame-changing Johnson edge is not automatically delay-`H` safe.
3. An `o(W/H)` number of uncertified cuts is not enough in the raw ledger;
   their factor-blind cost is quadratic in `H` per cut.
4. The product tail repairs no target inside the mesoscopic core and proves
   no MWB, owner synchronization, or cycle-rounding theorem.
5. The deletion rates above are sufficient, not necessary.  Larger
   structured leaves are permitted whenever their actual central deficit is
   `o(W)`.

The decisive constants and off-by-one points were independently audited:

* the factor `2` in (0.3) already covers both even tails;
* the odd lift is the only second doubling;
* the even full collar is `2H`;
* the odd full collar is `2H+1`, because (3.5) is unrestricted for unions;
* a bare even cut loses `H(H+1)` signed occurrences;
* a bare odd cut loses `(H+1)^2`, including its wraparound `Y` owner;
* `S_H=O(sqrt(m))` and both recoupling moments are `O(m)` uniformly in
  `H`.

Therefore the product-SCD tail/leave gate is closed in a form ready for the
tensor architecture.  The sole nonexternal input still required is a
post-recoupling simultaneous central-shadow estimate.
