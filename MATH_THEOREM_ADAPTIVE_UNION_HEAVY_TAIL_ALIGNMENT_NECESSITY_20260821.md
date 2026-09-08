# Adaptive union freshness forces a heavy all-rank palette tail

**Status (2026-08-21).**  Every statement below is proved.  This note does
not construct the coefficient-one word.  It gives a necessary condition for
the exact adaptive union target: on a logarithmic inner band, a successful
block selection must repeatedly choose candidates lying in a very heavy
upper tail of simultaneous cross-time, cross-rank freshness.  In particular,
under the fixed-residual uniform candidate law defined below, negative
association, a product Chernoff law, or any comparable subgaussian model for
those freshness indicators is impossible at most middle-stage residuals
reached by a successful selection.  The actual nested decks may instead have
the required positive alignment.  Exact one-point marginals and small pair
kernels therefore cannot be promoted to the required union theorem through a
diffuse-tail argument.

## 1. Block model and the inner band

All asymptotics are as odd `n` tends to infinity.  Fix a constant `C>=1`
and let the integer block length `a=a(n)` satisfy

\[
                         n\le a\le n^C.              \tag{1.0}
\]

Put

\[
 n=2m+1,\qquad W={n\choose m},\qquad
 H=\lceil\sqrt{n\log n}\rceil,
 \qquad K=\{m-H,\ldots,m+1+H\}.
\]

Put also

\[
 b=\left\lfloor {W\over a}\right\rfloor,
 \qquad W-a<A=ab\le W,                               \tag{1.1}
\]

and select one bare legal block in each of the `b` slots.  Assume that every
selected block has `a` distinct retained observations at every rank in `K`.
Write its rank-`q` deck as `U_(i,q)`, and put

\[
 M_q={n\choose q},\qquad R_q=\min(A,M_q),\qquad
 V_q=\left|\bigcup_{i=1}^bU_{i,q}\right|.             \tag{1.2}
\]

Suppose the exact adaptive union target holds:

\[
                  \sum_{q\in K}(R_q-V_q)=o(W).        \tag{1.3}
\]

Take

\[
 r=\lceil(\log n)^2\rceil,\qquad
 J=\{m-r,\ldots,m+1+r\},\qquad s=|J|=2r+2.            \tag{1.4}
\]

For all sufficiently large `n`, `J subset K`.

Order the selected blocks arbitrarily.  Before block `i`, let

\[
 Z_{i,q}={ [n]\choose q}\setminus\bigcup_{j<i}U_{j,q} \tag{1.5}
\]

be the residual family at rank `q`.  Define

\[
 u_{i,q}=|U_{i,q}\cap Z_{i,q}|,
 \qquad x_{i,q}=a-u_{i,q},
 \qquad X_i=\sum_{q\in J}x_{i,q}.                     \tag{1.6}
\]

Thus `X_i` is the number of old-target incidences in block `i`, summed over
the inner band.  It is not an internal-repeat count; the decks themselves
are simple.

## 2. The inner band has only `o(W)` old-hit mass

### Lemma 2.1 (inner binomial baseline)

Uniformly for `q in J`,

\[
 0\le W-M_q=O\left({Wr^2\over n}\right),
 \qquad
 \sum_{q\in J}(W-M_q)=O\left({Wr^3\over n}\right)=o(W). \tag{2.1}
\]

#### Proof

By complement symmetry it is enough to write `q=m-t`, `0<=t<=r`.  Then

\[
 {M_{m-t}\over W}
   =\prod_{j=0}^{t-1}{m-j\over m+2+j}.                \tag{2.2}
\]

Every factor is `1-O((j+1)/n)`.  The inequality
`1-prod_j(1-z_j)<=sum_j z_j` gives
`1-M_(m-t)/W=O(t^2/n)`.  Sum this over the two ranks at every depth
`0<=t<=r`.  Since `r^3/n=o(1)`, (2.1) follows.  \(\square\)

### Proposition 2.2 (zero first-order slack on the logarithmic band)

Under (1.1)--(1.3),

\[
                         \sum_{i=1}^bX_i=o(W).        \tag{2.3}
\]

Consequently there is a sequence `eta_n->0` such that all but `o(b)` blocks
satisfy

\[
                              X_i\le\eta_n a.         \tag{2.4}
\]

#### Proof

For every rank, telescoping first occurrences gives

\[
 \sum_i x_{i,q}=A-V_q=(A-R_q)+(R_q-V_q).              \tag{2.5}
\]

Because `A<=W`,

\[
 0\le A-R_q=(A-M_q)_+\le W-M_q.                      \tag{2.6}
\]

Sum (2.5) over `J`, use (1.3), Lemma 2.1, and the nonnegativity of every
summand in (1.3).  This proves (2.3).

Put `epsilon_n=(sum_i X_i)/A=o(1)`.  If `epsilon_n>0`, take
`eta_n=sqrt(epsilon_n)`; if it is zero, take any positive sequence tending
to zero.  Markov's inequality shows that at most
`epsilon_n b/eta_n=o(b)` indices violate (2.4).  \(\square\)

The strength of (2.3) is worth emphasizing.  There are `as` retained
inner-band incidences per block, but a typical selected block is allowed
only `o(a)`, rather than merely `o(as)`, old hits.

## 3. A successful selector forces a heavy palette tail

Before making the selection, fix for every slot `i` a nonempty finite
relabeling-invariant family `Omega_i` of candidate bare blocks, and require
the selected block to lie in `Omega_i`.  Thus the palette is not defined
after seeing the selected block or its reached residual.  A candidate records
an ordered starting history of a prescribed length `k_0=k_0(i,n)` and an
`a`-letter legal continuation; candidates are physical records, even if two
records happen to induce the same retained observations.  Assume
every candidate is simple at the ranks in `J`.  This includes the narrowed
free-history palette used in the central matching program.  Independently of
any lower bound on its size,

\[
 |\Omega_i|\le (n)_{k_0}n^a\le n^{n+a},              \tag{3.1}
\]

where `k_0<=n` is the retained-history length.  The sharper factor `d^a`
may replace `n^a`, but is unnecessary here.

For a candidate `omega in Omega_i`, denote its observation at internal time
`t` and rank `q` by `S_(omega,t,q)`, and define its freshness score against
the residual (1.5) by

\[
 Y_i(\omega)=
 \sum_{q\in J}\sum_{t=1}^a
 1_{\{S_{\omega,t,q}\in Z_{i,q}\}}.                  \tag{3.2}
\]

Let `omega` be uniform on `Omega_i`.  Relabeling invariance makes every fixed
`S_(omega,t,q)` uniform on `binom([n],q)`.  Therefore

\[
 \mathbb E_{\Omega_i}Y_i
   =a\sum_{q\in J}{|Z_{i,q}|\over M_q}.               \tag{3.3}
\]

### Theorem 3.1 (heavy all-rank alignment is necessary)

For all but `o(b)` indices

\[
                         {b\over3}\le i\le {2b\over3}, \tag{3.4}
\]

the uniform candidate law on `Omega_i` satisfies

\[
 \mathbb E Y_i\le\left({2\over3}+o(1)\right)as,       \tag{3.5}
\]

but also

\[
 \Pr\bigl(Y_i\ge as-\eta_n a\bigr)
   \ge {1\over|\Omega_i|}
   \ge \exp\{-(a+n)\log n\}.                         \tag{3.6}
\]

In particular, for all sufficiently large `n`,

\[
 \Pr\left(Y_i-\mathbb EY_i\ge {as\over5}\right)
   \ge \exp\{-(a+n)\log n\}.                         \tag{3.7}
\]

#### Proof

Let `V_(i-1,q)` be the number of rank-`q` targets seen in the first `i-1`
selected blocks.  From (1.6),

\[
 V_{i-1,q}=(i-1)a-\sum_{j<i}x_{j,q}
 \ge(i-1)a-\sum_{j=1}^bX_j.                           \tag{3.8}
\]

Thus the global nonnegative old-hit budget controls every prefix and every
rank separately; later blocks cannot cancel an earlier old hit.  For an
index in (3.4), Proposition 2.2 and (1.1) give, uniformly in `q in J`,

\[
 V_{i-1,q}\ge(1/3-o(1))W,
 \qquad {|Z_{i,q}|\over M_q}\le 2/3+o(1),             \tag{3.9}
\]

where Lemma 2.1 was used in the second inequality.  Summing the exact
first-occurrence identity also gives

\[
 \sum_{q\in J}V_{i-1,q}
   =(i-1)as-\sum_{j<i}X_j.                            \tag{3.10}
\]

Since `M_q<=W`, equations (3.3) and (3.10) give

\[
 \begin{aligned}
 {1\over a}\mathbb EY_i
 &=s-\sum_{q\in J}{V_{i-1,q}\over M_q}\\
 &\le s-{(i-1)as-\sum_{j<i}X_j\over W}.
 \end{aligned}                                       \tag{3.11}
\]

For indices in (3.4), `(i-1)a/W>=1/3-o(1)` by (1.1), while
`sum_jX_j/W=o(1)` by Proposition 2.2.  This proves (3.5).

All but `o(b)` indices in (3.4) satisfy (2.4).  For such an index, the
actually selected candidate `omega_i` belongs to `Omega_i` and has

\[
 Y_i(\omega_i)=\sum_{q\in J}u_{i,q}=as-X_i
       \ge as-\eta_n a.                              \tag{3.12}
\]

Thus the event in (3.6) contains at least one element of the finite uniform
palette.  Inequality (3.1) proves (3.6).  Finally `s->infinity` and
`eta_n->0`; combining (3.5) and (3.6) yields (3.7).  \(\square\)

The tail in (3.7) is much heavier than a product tail.  Its negative
logarithm is only `O((a+n)log n)`, although the deviation involves
`as=Theta(a(log n)^2)` Bernoulli incidences.

## 4. Negative association and subgaussian palette laws are impossible

### Corollary 4.1 (diffuse-tail no-go)

Fix any index supplied by Theorem 3.1 and freeze its actually reached
residual families `(Z_(i,q):q in J)`.  Under the uniform law on `Omega_i`,
the `as` resulting freshness indicators in (3.2) cannot satisfy a
subgaussian upper-tail bound

\[
 \Pr(Y_i-\mathbb EY_i\ge z)
       \le\exp\left\{-{z^2\over C as}\right\}         \tag{4.1}
\]

with an absolute constant `C`, uniformly for `z>=0`.  In particular, under
this fixed-residual uniform candidate law they cannot be negatively
associated.

#### Proof

At `z=as/5`, (4.1) is `exp(-Omega(as))`.  On the other hand, (3.7) is at
least `exp(-(a+n)log n)`.  Since `a>=n` and
`s=Theta((log n)^2)`,

\[
                         as\gg(a+n)\log n,            \tag{4.2}
\]

which is a contradiction.

For negatively associated Bernoulli variables, increasing exponential
functions factor in the required direction.  Hoeffding's lemma and the
exponential Markov inequality then give

\[
 \Pr(Y_i-\mathbb EY_i\ge z)
       \le\exp\left\{-{2z^2\over as}\right\},         \tag{4.3}
\]

a special case of (4.1).  \(\square\)

The order of correlation that must fail can also be quantified.  For a
fixed residual and palette, abbreviate the indicator in (3.2) by

\[
 \xi_\alpha(\omega)
   =1_{\{S_{\omega,t,q}\in Z_{i,q}\}},
 \qquad \alpha=(t,q)\in[a]\mathbin\times J,
 \qquad N=as.                                        \tag{4.4}
\]

### Corollary 4.2 (positive alignment is forced at order `Theta(a log n)`)

Put

\[
 d=\left\lceil10(a+n)\log n\right\rceil.             \tag{4.5}
\]

For every index supplied by Theorem 3.1 and all sufficiently large `n`,
there is a set `I subset [a] times J` of exactly `d` coordinates for which

\[
 \Pr\bigl(\xi_\alpha=1\text{ for every }\alpha\in I\bigr)
   >\prod_{\alpha\in I}\Pr(\xi_\alpha=1).            \tag{4.6}
\]

Thus the necessary positive alignment is genuinely high-order but occurs
well below the full dimension: `d=Theta(a log n)` while
`N=Theta(a(log n)^2)`.

#### Proof

Freeze the reached residual as in Corollary 4.1, and write
`p_alpha=E xi_alpha`.  The marginals need not be equal.  Equation (3.5)
nevertheless gives

\[
 \overline p={1\over N}\sum_\alpha p_\alpha
       ={\mathbb EY_i\over N}\le 2/3+o(1).           \tag{4.7}
\]

Suppose, contrary to (4.6), that the reverse weak inequality holds for every
`d`-set `I`.  The factorial-moment identity and Maclaurin's elementary
symmetric-mean inequality give

\[
 \mathbb E{Y_i\choose d}
   =\sum_{|I|=d}\Pr(\xi_\alpha=1\text{ for all }\alpha\in I)
   \le\sum_{|I|=d}\prod_{\alpha\in I}p_\alpha
   \le {N\choose d}\overline p^{\,d}.               \tag{4.8}
\]

For completeness, the last inequality follows by repeatedly replacing two
of the nonnegative numbers `p_alpha` by their average: at fixed pair sum,
the contribution from terms containing neither entry is unchanged, the
contribution from terms containing exactly one depends only on that sum, and
the contribution from terms containing both is proportional to their
product, which cannot decrease.  Iteration and continuity make all entries
equal to `overline p`.

Let `L=ceil(N-eta_n a)`.  Since `a>=n` and
`s=2ceil((log n)^2)+2`,

\[
 {d\over N}\le {10(a+n)\log n+1\over as}
       =O(1/\log n),
 \qquad {N-L\over N}\le {\eta_n\over s}=o(1).       \tag{4.9}
\]

In particular `d<L<N+1` for all sufficiently large `n`.  Moreover,

\[
 { {N\choose d}\over {L\choose d}}
   =\prod_{j=0}^{d-1}{N-j\over L-j}
   \le\left(1+{N-L\over L-d}\right)^d
   =(1+o(1))^d.                                      \tag{4.10}
\]

Markov's inequality applied to the increasing statistic `{Y_i choose d}`
and (4.7)--(4.10) therefore give, for all sufficiently large `n`,

\[
 \Pr(Y_i\ge L)
   \le { {N\choose d}\overline p^{\,d}\over {L\choose d}}
   \le (3/4)^d
   <\exp\{-(a+n)\log n\}.                           \tag{4.11}
\]

This contradicts (3.6), because its event is exactly `Y_i>=L` after the
integer rounding.  \(\square\)

## 5. Exact implication for the coefficient-one program

This theorem is a necessary obstruction, not a coefficient-one proof and
not a no-go for the adaptive union route.  It identifies the kind of
correlation a successful construction must create.

On a dynamically reached middle-stage residual, a uniform legal candidate
has only about a `2/3` mean fresh fraction across the logarithmic inner band,
yet the selected core must be almost perfectly fresh across both time and
rank.  The palette must therefore organize these rare cores into clusters
whose upper-tail exponent is at most `O(a log n)`, rather than the
`Omega(a(log n)^2)` exponent predicted by independent or negatively
associated incidences.  Corollary 4.2 locates a necessary positive
upper-orthant correlation already at order `Theta(a log n)`.  Exact
relabeling marginals, annealed two-point kernels, and one-bite estimates do
not provide this high-order alignment.

A positive proof can still succeed by exhibiting such clustered structure,
for example through a coherent wreath/product factor or a coverage-aware
augmentation.  What Corollary 4.1 rules out is any argument that keeps the
candidate block's cross-time, cross-rank freshness diffuse while hoping that
the entropy of all legal blocks, or a best-of-polynomial-choices step, will
locate an almost wholly fresh core.
