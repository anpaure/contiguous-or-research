# Merging the PBBS payload bank removes the rank-\((t-1)\) shadow obstruction: an exact symmetric-chain endpoint packing

**Date:** 2026-08-06  
**Method:** pure mathematics; truncated interval posets and symmetric-chain
decompositions  
**Status:** unconditional scalar/chain-capacity theorem for architectural
escape (2).  If the formerly separated depth-\(d\) payload positions can be
merged into one, or a fixed number of, long free regions, then the quadratic
rank-\((t-1)\) upset-shadow obstruction disappears at the exact binomial
target counts.  Moreover the entire deep Boolean band has an explicit exact
partition into at most the available number of length-\(d\) endpoint chains.
This does **not** realize one literal interval-join chart: cross-endpoint join
identities and the PBBS cover-free coordinate cuts remain open.

## 1. Parameters and the merged interval poset

Use the odd PBBS parameters

\[
 n=2m+1,qquad r=m,qquad t=m-d,qquad
 W={n\choose m},qquad M={n\choose t},qquad U=W-M.            \tag{1.1}
\]

The separated template had

\[
                    b=\left\lfloor{U\over d+1}\right\rfloor
\]

blocks of \(d\) free positions.  Let

\[
                              g=bd                              \tag{1.2}
\]

be the number of those free positions.  Architectural escape (2) asks that
these positions occur in one long cyclic free region, or in a fixed number
of long regions, rather than behind rank-\(t\) separators.

For one cyclic region of length \(g>d\), let

\[
 \mathcal J^{\rm cyc}_{g,d}
   =\{\text{cyclic intervals of lengths }1,\ldots,d\}.        \tag{1.3}
\]

It has exactly \(g\) intervals at each length and hence \(gd\) addresses.
Every address belongs to the endpoint chain

\[
 \mathcal E_j={[j-\ell+1,j]:1\le\ell\le d\},                \tag{1.4}
\]

and the \(g\) endpoint chains partition the address set.

The deep target band is

\[
 \mathcal B_{m deep}
   =\{S\subseteq[n]:d+1\le|S|\le t-1\}.                     \tag{1.5}
\]

Put

\[
 A={n\choose t-1},qquad
 L_{m deep}=|\mathcal B_{m deep}|.                        \tag{1.6}
\]

## 2. The top antichain has unit shadow in a long region

### Lemma 2.1 (truncated top-layer shadow)

Every family of \(a\le g\) distinct length-\(d\) cyclic intervals is an
antichain in \(\mathcal J^{\rm cyc}_{g,d}\), and its upset in the truncated
interval poset has exactly \(a\) elements.

#### Proof

Two distinct intervals of equal length are incomparable.  An allowed
interval containing a length-\(d\) member has length at least \(d\), and
therefore equals that member.  \(\square\)

This is the exact point at which the separated-block proof breaks.  A
length-\(d\) separated block has only one maximal address, so placing
\(a_j\) equal-rank targets in it forces shorter antichain intervals and the
quadratic shadow \({a_j+1\choose2}\).  A long region has one maximal address
per endpoint.

### Proposition 2.2 (the exact top layer fits)

For all sufficiently large parameters,

\[
                              A\le g-d.                       \tag{2.1}
\]

Consequently every rank-\((t-1)\) target can be assigned a distinct
length-\(d\) address, and reserving those addresses consumes exactly \(A\)
addresses rather than a quadratic upset shadow.

#### Proof

The central local limit estimates used in the PBBS block audit give

\[
 {M\over W}\longrightarrow e^{-\pi/4},qquad
 {A\over W}\longrightarrow e^{-\pi/4}.                       \tag{2.2}
\]

Since \(d\to\infty\), (1.2) gives

\[
 {g\over W}
 ={d\over W}\left\lfloor{U\over d+1}\right\rfloor
 \longrightarrow1-e^{-\pi/4}.                               \tag{2.3}
\]

The strict inequality

\[
                         e^{-\pi/4}<1-e^{-\pi/4}              \tag{2.4}
\]

follows from \(e^{-\pi/4}<1/2\).  Thus \(g-A=\Omega(W)\),
whereas \(d=o(W)\), proving (2.1).  Lemma 2.1 gives the final assertion.
\(\square\)

The total scalar address count also has large slack:

\[
 {L_{m deep}\over gd}longrightarrow
 {2\Phi(-\sqrt{\pi/2})\over1-e^{-\pi/4}}<0.39.               \tag{2.5}
\]

Thus neither total addresses nor the top antichain refutes the merged
architecture.

## 3. Exact symmetric-chain splitting of the deep band

Take any symmetric-chain decomposition of \(B_n\).  A chain beginning at
rank \(j\) contributes to (1.5) the consecutive segment of ranks

\[
                    \max\{j,d+1\},\ldots,t-1,                \tag{3.1}
\]

of length

\[
                    \ell_j=t-\max\{j,d+1\}.                  \tag{3.2}
\]

Split every nonempty segment into consecutive pieces of at most \(d\)
sets.  Let \(P_{n,d}\) be the number of resulting pieces.

### Theorem 3.1 (exact piece census)

The pieces partition every named target in \(\mathcal B_{\rm deep}\)
exactly once, every piece is an inclusion chain of size at most \(d\), and

\[
\boxed{
 P_{n,d}
   =\sum_{\substack{q\ge0\\qd<t-d-1}}
       {n\choose t-qd-1}.}                                  \tag{3.3}
\]

Exactly \(A={n\choose t-1}\) pieces contain a rank-\((t-1)\) target.

#### Proof

An SCD of \(B_n\) has

\[
                     {n\choose j}-{n\choose j-1}             \tag{3.4}
\]

chains beginning at rank \(j\), with the second binomial interpreted as
zero at \(j=0\).  Splitting (3.1) gives
\(\lceil\ell_j/d\rceil\) pieces.

Use

\[
             \left\lceil{\ell\over d}\right\rceil
                =\sum_{q\ge0}{\bf1}_{\{\ell>qd\}}.           \tag{3.5}
\]

For a fixed \(q\) with \(qd<t-d-1\), condition
\(\ell_j>qd\) is exactly

\[
                              j\le t-qd-1.                    \tag{3.6}
\]

Summing (3.4) up to that rank telescopes to
\({n\choose t-qd-1}\).  Summing over \(q\) proves (3.3).

Every rank-\((t-1)\) set lies in one SCD chain and in the top piece of that
chain.  Conversely every piece meeting that rank contains one such set, so
there are exactly \(A\) top pieces.  \(\square\)

The splitting may be aligned globally from the top.  For each admissible
\(q\), let \(\mathcal C_q\) consist of the nonempty chain intersections with
the rank slab

\[
       t-(q+1)d,\ldots,t-qd-1,                              \tag{3.7}
\]

clipped at the lower boundary \(d+1\).  Every member of
\(\mathcal C_q\) has at most \(d\) sets, all of its maxima have the common
rank \(t-qd-1\), and

\[
                         |\mathcal C_q|={n\choose t-qd-1}.    \tag{3.8}
\]

Thus the exact piece census is a disjoint union of antichain-top chain
families.  The repository's antichain-top static owner theorem applies to
each slab separately.  What it does not provide is one common literal
source chronology simultaneously serializing all slabs.

## 4. The available endpoint chains exceed the exact SCD demand

### Theorem 4.1 (merged-region endpoint capacity)

At the optimal PBBS depth,

\[
 {P_{n,d}\over W}longrightarrow
 \sigma:=\sum_{a=1}^{\infty}e^{-\pi a^2/4},                  \tag{4.1}
\]

and

\[
                         \boxed{\sigma<1-e^{-\pi/4}.}        \tag{4.2}
\]

Consequently

\[
                              P_{n,d}\le g                   \tag{4.3}
\]

for every sufficiently large parameter.

#### Proof

The \(q\)-th summand in (3.3) has rank

\[
                      m-(q+1)d-1.                            \tag{4.4}
\]

The same uniform central binomial estimate used for the PBBS pull clock
therefore gives, for every fixed \(q\),

\[
 { {n\choose m-(q+1)d-1} \over W}
       \longrightarrow e^{-\pi(q+1)^2/4}.                   \tag{4.5}
\]

The standard Gaussian upper bound for off-central binomial coefficients
dominates the summands by a summable multiple of
\(e^{-c(q+1)^2}\), uniformly in the parameter.  Dominated convergence
gives (4.1).

Poisson summation for the Jacobi theta function gives

\[
 \sigma={1\over2}+2\sum_{j=1}^{\infty}e^{-4\pi j^2}
        =0.500006\ldots,                                    \tag{4.6}
\]

whereas

\[
                    1-e^{-\pi/4}=0.544061\ldots.             \tag{4.7}
\]

For a purely elementary strict comparison, bound the tail in (4.6) by a
geometric series and use \(e^{-\pi/4}<0.46\); the left side is below
\(0.501\), while the right side is above \(0.54\).  This proves (4.2).

Equations (2.3), (4.1), and the strict gap (4.2) imply (4.3).  \(\square\)

The limiting endpoint utilization of this explicit construction is

\[
 {\sigma\over1-e^{-\pi/4}}=0.9190\ldots.                     \tag{4.8}
\]

The width lower bound alone requires at least

\[
 {e^{-\pi/4}\over1-e^{-\pi/4}}=0.8380\ldots                 \tag{4.9}
\]

of the available merged endpoints if all rank-\((t-1)\) targets stay in
the merged region.  Thus merging only a small fraction of the old blocks
cannot work, but merging essentially all of them has genuine asymptotic
room.

## 5. An explicit endpoint-chain chart skeleton

Assign the \(P_{n,d}\) SCD pieces injectively to distinct endpoint chains
\(\mathcal E_j\) in (1.4).

For a piece

\[
                         S_1\subset S_2\subset\cdots\subset S_h,
                         \qquad h\le d,                       \tag{5.1}
\]

which contains a rank-\((t-1)\) target, assign it to the nested physical
intervals of lengths

\[
                         d-h+1,d-h+2,\ldots,d.                \tag{5.2}
\]

Thus its top target uses the maximal length-\(d\) address.  Assign every
other piece to any \(h\) consecutive lengths in its endpoint chain, in
increasing order.

### Corollary 5.1 (exact chain-consistent interval injection)

For all sufficiently large parameters there is an injection

\[
                 \psi:\mathcal B_{\rm deep}
                       \longrightarrow\mathcal J^{\rm cyc}_{g,d}          \tag{5.3}
\]

such that

1. every named deep target occurs exactly once;
2. the members of each SCD piece map to nested intervals in the same order;
3. every rank-\((t-1)\) target maps to a length-\(d\) interval; and
4. the upset, within the allowed interval poset, of the complete image of
   the rank-\((t-1)\) layer has size exactly \(A\).

#### Proof

Theorem 4.1 supplies a distinct endpoint for every piece.  The assignments
(5.1)--(5.2) use distinct intervals because endpoint chains partition the
address set.  Inclusion is preserved inside each piece.  The top targets
use distinct maximal intervals, and Lemma 2.1 gives their exact upset size.
\(\square\)

This is an exact named-target construction at the level of endpoint-chain
capacity; it is much stronger than a rank histogram or fractional clock.
It is not yet a literal payload word.

## 6. The exact remaining obstruction after merging

The injection (5.3) controls inclusion **inside** every endpoint chain.  A
source word requires more: whenever two assigned physical intervals overlap
or one contains another across different endpoint chains, all their values
must arise from one common family of letters.  Equivalently, for every
coordinate \(x\), the positive assigned intervals must be hit by one support
set \(E_x\), while every negative assigned interval avoids \(E_x\).

Thus Corollary 5.1 does not imply the interval-join identities or the
PBBS-relative cover-free criterion.  It proves precisely that the former
rank-\((t-1)\) scalar no-go cannot be reused against the merged architecture.

There is also a separate owner-side caveat.  The short-gap common-payload-core
theorem was proved for blocks of length at most \(d\).  A long region need
not possess one payload core common to all positions.  A successful merged
construction must therefore use the full varying maximal envelope
\(P_p\), or rethread the owner chronology; it cannot simply declare the
long region owner-invisible by the old block lemma.

The surviving theorem is now sharply stated.

> **Merged PBBS chart theorem.**  Realize a chain-consistent injection of
> the form (5.3) on one/few long regions by one source word satisfying the
> PBBS coordinate cover-free cuts, while retaining all but a bounded number
> of targets and preserving the fixed whole-fan owner section.

The present theorem proves that this target has enough exact addresses,
enough maximal antichain slots, and an explicit exact SCD chainization.  Its
only remaining content is cross-endpoint join coherence and owner-envelope
compatibility.

## 7. Linear or finitely many long regions

For a linear region of length \(g\), the first \(d-1\) endpoint chains lose
\({d\choose2}\) addresses in total.  For any fixed number \(c\) of long
linear regions, the loss is \(c{d\choose2}=o(W)\).  The strict
\(\Omega(W)\) margins in Propositions 2.2 and Theorem 4.1 absorb this loss.

More directly, discard the first \(d-1\) endpoint chains of each linear
region and use only full length-\(d\) endpoint chains.  This removes only
\(c(d-1)=o(W)\) candidate chains, while (4.2) leaves \(\Omega(W)\) unused
endpoints.  The SCD pieces can therefore still be injected without splitting
or dropping a named target.

Hence every conclusion above remains true for one or any fixed number of
long linear regions, after discarding only unused endpoint capacity—not
named targets.  The theorem genuinely distinguishes long merged regions
from \(\Theta(W/d)\) separated depth-sized blocks, whose cumulative
boundary loss and quadratic top shadows are both macroscopic.

## 8. Consequence for the all-dimensional programme

Architectural escape (2) is viable at the complete scalar and endpoint-chain
levels:

\[
 \boxed{
 \text{the separated rank-}(t-1)\text{ shadow obstruction disappears.}}
\]

The next proof should not spend effort strengthening that no-go.  It should
construct the cross-endpoint coordinate supports, most plausibly by an
integral coloured rotor/Euler fusion whose rank marginals are already
provided by the stationary pull clock, or prove a new obstruction involving
those coordinate supports rather than interval-poset capacity.

This theorem does not prove the merged PBBS chart theorem,
\(\nu(k)\le B(k)+O(1)\), or exact equality.
