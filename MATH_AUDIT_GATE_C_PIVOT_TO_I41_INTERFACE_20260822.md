# Gate C: the pivot tail controls schedule entropy, not the holes in (I.41)

**Status (2026-08-22).** Every assertion below is proved.  Combining the
equal-block bad-cut theorem with the pivot miss-set tail gives the exact
upper bound (2.2) on the number of equal-block macro schedules having
small central loss.  At the live scale this is only
`exp(O(b/log b))` schedules.

This is the strongest direct consequence for Appendix I.  It neither
implies the product lift `C_P` nor the independent fragment gate `C_F`.
The pivot miss set is a set of failed **block cuts** of one schedule;
the holes in (I.41) are missing **labelled subset targets** in every rank.
The latter depend on outer pairings, states, relabellings, intersections,
and literal off-middle windows, none of which occurs in the pivot
statistic.  In particular the identity schedule has no pivot misses at
all, but one copy still covers only polynomially many middle targets.

## 1. The two different miss sets

Let

\[
 b=K\ell,\qquad K=2e+1,\qquad K,\ell\ge3\text{ odd},
 \qquad q=b(b-1).                                      \tag{1.1}
\]

For a cyclic order `tau` of the `K` equal blocks, let `G(tau)` be its
number of two-sided-ballot cuts and put

\[
                       R(\tau)=K-G(\tau).              \tag{1.2}
\]

Thus `R(tau)` counts locations in the macro schedule.  By contrast, for
a family `F` of physical fragments as in Appendix I, the rank-`s` hole
set is

\[
 \mathcal H_s(\mathscr F)=
 {\Omega\choose s}\setminus\mathcal I_s(\mathscr F),  \tag{1.3}
\]

and (I.41) asks for

\[
             \sum_{s=b-H}^{b+H}|\mathcal H_s(\mathscr F)|=o(W),
 \qquad W={2b\choose b}.                               \tag{1.4}
\]

There is no identification between (1.2) and (1.3): their ground sets
are respectively the `K` block cuts and the labelled rank layers of the
`2b`-cube.

## 2. The exact valid bridge

Let `E_(b,K)(L)` be the set of equal-block orders for which one coherent
phase meets the fixed central factor in at least `q-L` internal flags.
Set

\[
 r_L=\left\lfloor
 {L\over(\ell-2)(b-1)}
 \right\rfloor,                                        \tag{2.1}
\]

and assume `r_L<K`.  Then

\[
\boxed{
 |\mathcal E_{b,K}(L)|
 \le {K\choose e+1}2^{K-r_L}
       e_{r_L}(n_0,\ldots,n_{K-1})
 \le
 4^K{((e+1)^2/2)^{r_L}\over r_L!},}                   \tag{2.2}
\]

where

\[
 n_{2j}=e+1-j\quad(0\le j\le e),\qquad
 n_{2j+1}=e-j\quad(0\le j<e).                         \tag{2.3}
\]

### Proof

The equal-block bad-cut theorem gives

\[
 q-M(\tau)\ge R(\tau)(\ell-2)(b-1).                   \tag{2.4}
\]

If `M(tau)>=q-L`, then (2.1)--(2.4) imply
`R(tau)<=r_L`, or equivalently `G(tau)>=K-r_L`.  The first inequality in
(2.2) is exactly the pivot miss-set bound with `R=r_L`; its closed
elementary-symmetric-polynomial estimate gives the second inequality.
\(\square\)

Suppose now that

\[
 K=\Theta(b/\log b),\qquad L=O(bK).                    \tag{2.5}
\]

Since `ell=b/K`, equation (2.1) gives

\[
                      r_L=O(K^2/b)=O(b/\log^2 b).      \tag{2.6}
\]

Using `r!>=(r/\mathrm e)^r` in (2.2), with the case `r=0`
read separately, yields

\[
 \log|\mathcal E_{b,K}(L)|
 \le K\log4+r_L\log{\mathrm e(e+1)^2\over2r_L}
 =O(b/\log b).                                         \tag{2.7}
\]

Thus the pivot theorem rigorously removes equal-block macro-order
multiplicity as a source of `exp(Theta(b))` independent schedules.

There is one useful uniformization consequence.  Let `Xi_b` be any random
outer construction, and for each
`tau in E_(b,K)(L)` let `B_tau` be an event depending on `Xi_b`.  No
independence is required.  Equation (2.2) and the union bound give

\[
 \Pr\left(\bigcup_{\tau\in\mathcal E_{b,K}(L)}\mathsf B_\tau\right)
 \le 4^K{((e+1)^2/2)^{r_L}\over r_L!}
       \max_\tau\Pr(\mathsf B_\tau).                  \tag{2.8}
\]

At the scale (2.5), any pointwise outer-lift failure estimate

\[
              \max_\tau\Pr(\mathsf B_\tau)
              =\exp\{-\omega(b/\log b)\}              \tag{2.9}
\]

therefore holds simultaneously for every viable equal-block schedule with
probability `1-o(1)`.  This is a genuine bridge from the pivot theorem to
a future repair argument, but only after that argument supplies the
pointwise tail (2.9).  The pivot theorem supplies no such tail.

There is also a deterministic pigeonhole consequence.  Suppose every
retained core start of a proposed equal-block construction is tagged by
one schedule in `E_(b,K)(L)`, and let `M_tau` be the total number of starts
carrying tag `tau`.  If `M=sum_tau M_tau`, then (2.2) gives

\[
 \max_\tau M_\tau
 \ge {M\over|\mathcal E_{b,K}(L)|}.                    \tag{2.10}
\]

Hence, under (2.5) and `M=W-o(W)`, some single macro schedule must carry

\[
                    M_\tau\ge W\exp\{-O(b/\log b)\}.   \tag{2.11}
\]

If every unsplit coherent tour contributes at most `q` starts, this means
at least

\[
              {W\over q}\exp\{-O(b/\log b)\}          \tag{2.12}
\]

tour pieces with that same schedule.  Thus essentially all exponential
target diversity must come from the outer pairing/state/relabeling layer,
not from the equal-block order.

## 3. Why (2.2) does not control (I.41)

The compiler does not require distinct macro schedules.  It requires
distinct labelled middle targets and near-surjectivity of the union of
literal windows.  The same schedule may be reused on many different
pairings, states, or coordinate relabellings.

This failure is already visible at the best possible value of the pivot
statistic.  Take `sigma(a)=a`.  For every `v!=a`,

\[
 (-1)^{((v-a)\bmod K)+((\sigma(v)-\sigma(a))\bmod K)}=+1. \tag{3.1}
\]

Every ballot word is therefore all plus, so

\[
                            G(\mathrm{id})=K.           \tag{3.2}
\]

At the live scale `ell>3`, the equal-block sufficiency theorem even gives
this phase at least

\[
 K(\ell-3)(b-2)=q-O(bK)                               \tag{3.2a}
\]

factor flags, so it is a genuinely viable high-overlap example.
Nevertheless one coherent phase has at most `q` distinct internal middle
targets.  Since `q=o(W)`, a family consisting of this one schedule and one
labelling has

\[
                  |\mathcal H_b|\ge W-q=(1-o(1))W,     \tag{3.3}
\]

and is nowhere near (I.41).  Repeating the same labelled copy changes
nothing.  On the other hand, relabelling the ground set preserves the
macro order and (3.2) while moving its target support.  Indeed, if
`A` is any nonempty proper middle support, transitivity of
`Sym(Omega)` on `binom(Omega,b)` gives

\[
                  \bigcup_{\gamma\in\operatorname{Sym}(\Omega)}
                  \gamma A={\Omega\choose b}.          \tag{3.4}
\]

Thus identical pivot data are compatible both with total repetition and
with a relabelling orbit whose union covers the middle layer.  The pivot
statistic contains no information about the intersections needed to
extract a disjoint subfamily from that orbit.  It also contains no
information at all about the rank-`b\pm j` windows in (1.4).

Equations (3.2)--(3.4) are the minimal obstruction to a direct inference:
even zero pivot misses neither proves nor disproves the literal target
coverage demanded by (I.41).

## 4. What an actual bridge would still have to prove

For a positive use in `C_P`, one needs an additional deterministic or
probabilistic lift which, from the same Gate-B row bank and chosen
schedules, constructs singleton fragments and proves simultaneously:

1. clean windows at every offset `b-H<=s<=b+H`;
2. global injectivity of the retained middle targets;
3. `o(W)` aggregate holes in those `2H+1` labelled layers; and
4. `gt=o(W)` after every required split or repair.

The pivot bound proves none of these four statements.  For a negative
route, (2.2) would have to be supplemented by a target-atlas or matching
capacity bound uniform over all allowed pairings, states, and relabellings.
The fixed-pairing atlas cap in Appendix I is not such a uniform bound,
because (I.41) explicitly allows exponentially many different pairings.

Therefore the pivot result is a completed entropy obstruction for the
equal-block schedule subroute, not progress on the product lift or the
all-band repair itself.
