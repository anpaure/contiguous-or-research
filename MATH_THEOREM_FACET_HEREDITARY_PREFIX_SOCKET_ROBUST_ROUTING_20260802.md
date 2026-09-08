# Hereditary prefix-socket routing through exponentially many core layers

Date: 2026-08-02  
Status: unconditional robust-routing theorem under an explicit hereditary
prefix-load hypothesis.  The hypothesis is quantitatively compatible with
the `O(h^(-1/2))` anchor density at the target q1 packing scale, but it is
not implied by the current clustered-pruning expectation.  This file does
not claim a complete reservoir packing unconditionally.

## 0. Outcome

The fixed-support fusion problem has a layered socket-state graph with

\[
                         D_h=(h-1)!^2                    \tag{0.1}
\]

successors per state.  A mere `O(h^(-1/2))` density of dead states in each
layer does not control how those states meet individual socket
neighbourhoods.

The theorem below gives the correct nonaccumulating condition.  Expose the
two free successor orders one tag at a time.  If, after **every** surviving
partial exposure, at most a `rho` fraction of the next choices is fatal,
then every state has at least

\[
              (1-\rho)^{2(h-1)}(h-1)!^2                 \tag{0.2}
\]

safe successors.  For

\[
                         \rho=O(h^{-1/2}),               \tag{0.3}
\]

the quantity (0.2) tends to infinity extremely quickly.  Therefore one may
route through an arbitrary number of core layers with no accumulated loss.

This turns the open path-preservation row into one precise strengthening of
clustered pruning: prove a hereditary conditional cylinder-load bound, not
only an average collision count.

## 1. Socket states and successor coordinates

Use the state notation

\[
 \omega=(\mathbf A,\mathbf B,\epsilon),                 \tag{1.1}
\]

with ordered complementary halves

\[
 \mathbf A=(a_0,\ldots,a_{h-1}),\qquad
 \mathbf B=(b_0,\ldots,b_{h-1}).                        \tag{1.2}
\]

For a compatible successor `omega'`, the unordered halves are forced:

\[
\begin{aligned}
 A'&=\{a_{h-1}\}\cup(B-\{b_0\}),\\
 B'&=\{b_0\}\cup(A-\{a_{h-1}\}),                      \tag{1.3}
\end{aligned}
\]

with

\[
 a'_0=a_{h-1},\qquad b'_{h-1}=b_0,qquad
 \epsilon'=\epsilon+h\pmod2.                           \tag{1.4}
\]

Thus a successor is encoded by two independent permutations:

* the order of the remaining `h-1` elements of `A'`, exposed from left to
  right;
* the order of the remaining `h-1` elements of `B'`, exposed from right to
  left.

The opposite exposure directions match the two zipper seams: local tag
sets are a fixed old suffix plus a newly exposed prefix on the `A` seam,
and a newly exposed suffix plus a fixed old prefix on the `B` seam.

## 2. Hereditary prefix load

Fix a core layer `i`, a live state `omega`, a forbidden named-resource bank
`mathcal B_i`, and a prescribed live-state set `K_(i+1)` in the next layer.

Expose the `2(h-1)` free successor entries in any fixed interleaving which
respects the two directions above.  A partial exposure is called surviving
when:

1. no owner/lower-q1/upper-q1 resource already determined by that exposure
   lies in `mathcal B_i`;
2. it has not yet forced the completed successor outside `K_(i+1)`.

Whenever a new entry is chosen, inspect every local resource which becomes
fully determined for the first time.  A choice is fatal if the enlarged
partial exposure is not surviving.

### Definition 2.1 (HPS(`rho`))

The transition `i -> i+1` satisfies hereditary prefix-socket load
`HPS(rho)` on `K_i,K_(i+1)` when, for every `omega in K_i`, every surviving
partial exposure with `m` choices remaining in the currently exposed
permutation has at most `rho m` fatal next choices.

The quantifier over every surviving prefix is essential.  A root-average
bound does not prevent all residual choices from concentrating behind one
apparently safe first tag.

There is a more static sufficient condition tailored to the zipper.  For
the `A` shore, let

\[
 W_A=A'-\{a'_0\}                                       \tag{2.1}
\]

be the free successor set.  For each `0<=p<=h-1`, let
`mathcal F^A_p(omega)` be the family of `p`-subsets `Q subset W_A` for
which exposing exactly `Q` as the first `p` entries determines a forbidden
local resource for the first time.  Put all order-independent endpoint
anchors into the live-state test.  Define `mathcal F^B_p` analogously while
exposing `B'` from right to left.  For this static formulation, require in
addition that exclusion from `K_(i+1)` is either order-independent or is a
union of such one-shore prefix conditions.  A genuinely joint terminal
condition on the two complete permutations must instead be handled by HPS
directly.

### Definition 2.2 (HPL(`rho`))

The layer satisfies hereditary prefix-link load `HPL(rho)` when every
safe prefix `Q in binom(W_A,p)`, `p<h-1`, obeys

\[
 \left|\{x\in W_A-Q:Q\cup\{x\}\in
                    \mathcal F^A_{p+1}(\omega)\}\right|
 \le \rho(h-1-p),                                      \tag{2.2}
\]

and the identical inequality holds on the `B` shore.  If several resource
rows become determined at the same prefix length, their forbidden-prefix
families are unioned before (2.2) is tested.

Every non-anchor zipper resource is a fixed old suffix union a new prefix,
so it appears in exactly one of these families.  Under the stated
prefix-separability of the next kernel, HPL implies HPS: at each exposure
step, the newly fatal symbols are precisely the link in (2.2).  This
formulation contains no look-ahead or circular reference to a completed
path; it is a finite family of conditional Boolean-cylinder degree
inequalities.

## 3. Robust routing theorem

### Theorem 3.1 (hereditary prefix-socket routing)

Let

\[
 K_0,K_1,\ldots,K_T                              \tag{3.1}
\]

be nonempty live-state sets in an arbitrary number of consecutive core
layers.  Suppose every transition `i -> i+1` satisfies `HPS(rho)` for one
`0<=rho<1`.

Then every state in `K_i` has at least

\[
                         D_{\rm safe}
 =(1-\rho)^{2(h-1)}(h-1)!^2                             \tag{3.2}
\]

safe compatible successors in `K_(i+1)`.  In particular, if

\[
                         D_{\rm safe}\ge1,               \tag{3.3}
\]

there is a safe directed state path through all `T+1` layers.  The number
of layers does not enter (3.2) or (3.3).

### Proof

Consider one live state.  At a step with `m` remaining symbols, HPS leaves
at least `(1-rho)m` choices.  Multiplying over the `h-1` choices in each of
the two successor permutations gives

\[
 \prod_{m=1}^{h-1}(1-\rho)m
 \prod_{m=1}^{h-1}(1-\rho)m
 =(1-\rho)^{2(h-1)}(h-1)!^2.                            \tag{3.4}
\]

Every completed nonfatal exposure is a distinct compatible successor in
`K_(i+1)` and has a completely safe local zipper deck.  This proves (3.2).
Under (3.3), choose one such successor at every layer.  Because the bound
is hereditary and independent of the preceding choices, this greedy
construction continues through all `T` transitions. \(\square\)

### Corollary 3.2 (the `h^(-1/2)` regime)

If

\[
                         \rho\le {C\over\sqrt h}         \tag{3.5}
\]

for an absolute `C`, then for all sufficiently large `h`,

\[
 D_{\rm safe}
 \ge (h-1)!^2\exp(-4C\sqrt h)>1.                        \tag{3.6}
\]

Hence a safe path exists through an arbitrary number of core layers.

### Proof

For large `h`, `rho<=1/2` and `log(1-rho)>=-2rho`.  Substitute this in
(3.2).  The logarithm of the factorial term is

\[
                         2h\log h-O(h),                  \tag{3.7}
\]

which dominates `4C sqrt(h)`. \(\square\)

The important feature is that the safe **fraction** may be as small as
`exp(-O(sqrt(h)))`; the factorial socket menu is still vastly larger.
A constant safe fraction is unnecessary.

## 4. A statewise weighted-load certificate

The HPS hypothesis can be checked by a prefix cylinder ledger.

For a local occurrence `o` and a fixed state `omega`, let `p_o` be the
number of freely ordered successor entries in the prefix which determines
that occurrence.  A prescribed compatible target at that occurrence is
realized by at most the fraction

\[
                         {1\over\binom{h-1}{p_o}}         \tag{4.1}
\]

of the successor orders on that shore.  Indeed, the target fixes the set of
the first `p_o` entries; the compatible orders are

\[
                         p_o!(h-1-p_o)!                   \tag{4.2}
\]

out of `(h-1)!`.

The endpoint cases `p_o=0` or `h-1` have weight one.  For example, the
first mixed owner on the `A` seam is

\[
 R_i\cup\{\beta\}\cup(A-\{a_0\}),                      \tag{4.3}
\]

independent of all successor ordering choices.

For a surviving partial prefix `xi`, define its conditional load

\[
 \mathcal L_i(\omega,\xi)
 = {\#\{\text{fatal next symbols after }\xi\}
       \over\#\{\text{remaining next symbols after }\xi\}}. \tag{4.4}
\]

Then the exact sufficient certificate is

\[
 \boxed{
   \sup_{i,\omega\in K_i,\xi\ {m surviving}}
      \mathcal L_i(\omega,\xi)\le\rho.}                 \tag{4.5}
\]

Equations (4.1)--(4.2) turn (4.5) into a finite collection of weighted
Boolean-cylinder inequalities.  Unlike an unweighted target count, this
ledger prices endpoint anchors at one and central prefixes by their exact
binomial dilution.

Equivalently, one may verify the static HPL inequalities (2.2).  HPL is
stronger than a root weighted sum but weaker than enumerating complete
successor permutations: it asks only for maximum one-symbol links of the
forbidden prefix families.

## 5. Packing consequence under hereditary cylinder spread

### Theorem 5.1 (conditional complete q1-reservoir packing)

Let

\[
                         t\le \alpha {4^h\over h^2}      \tag{5.1}
\]

for fixed `alpha>0`.  Suppose that after any `j<t` already selected
owner/q1-disjoint fused reservoirs, the resulting forbidden bank admits
nonempty kernels `K_i^(j)` on one rainbow core path and satisfies

\[
                         \operatorname{HPS}
                  \left({C_\alpha\over\sqrt h}\right)   \tag{5.2}
\]

at every layer, with `C_alpha` independent of `h,i,j`.

Then, for all sufficiently large even `k`, one can select `t` complete
fixed-support fused reservoirs whose owner, lower-q1, and upper-q1 decks
are pairwise disjoint.

### Proof

Induct on `j`.  At stage `j`, Corollary 3.2 gives a full safe decoration
path through the core layers, hence one more reservoir disjoint from the
current bank.  Add its deck to the bank.  Hypothesis (5.2) regenerates for
the next stage. \(\square\)

This theorem is deliberately q1-scoped.  The same-support source-cap
theorem forbids more than two reservoirs if the literal `P/H` source decks
must also be pairwise distinct.

## 6. Relation to clustered pruning

The existing clustered-pruning estimate has the form

\[
 \mathbb E_{\text{supports, modules}}
       [\text{number of named collisions}]
       =O(q^2/2^Q)                                      \tag{6.1}
\]

at the normalized module scale.  It averages over the support, core, and
complete module.  HPS instead requires the conditional maximum

\[
 \sup_{i,\omega,\xi}
 \Pr(\text{next tag is fatal}\mid i,\omega,\xi)          \tag{6.2}
\]

after every previous reservoir has been exposed.

The anchor-shadow theorem proves that at the target count (5.1), only
`O(h^(-1/2))` of the unordered halves are completely killed by endpoint
owner anchors at any one outside edge.  This matches (5.2) at the marginal
level.  What is still missing is conditional spread inside every socket
fiber and after every partial ordering.

Thus the exact upgrade needed from clustered pruning is:

> **Hereditary socket-cylinder spread.**  Select the support/core banks so
> that every conditional prefix cylinder has fatal next-symbol density
> `O(h^(-1/2))`, uniformly after all earlier selected reservoirs.

In the static zipper language this is exactly HPL with
`rho=O(h^(-1/2))`: every forbidden prefix family must have all its
one-symbol links bounded at that density.  This is substantially more
concrete than the earlier full-path condition and is the natural maximum-
codegree strengthening of clustered pruning.

Ordinary Markov cleanup cannot establish this: there are exponentially
many core layers and factorially many partial socket states, and a single
weight-one anchor can kill one complete successor fiber.

## 7. Strict scope

Theorem 3.1 is a complete robust-routing proof once HPS is supplied.  It
does not prove HPS for the actual clustered bank.  In particular this file
does not establish:

* unconditional packing of `Theta(4^h/h^2)` fused reservoirs;
* literal source-row disjointness (which is impossible on one support past
  two reservoirs);
* arbitrary-width upper coverage;
* occurrence-labelled compiler/common-cap feasibility;
* an OR word or a bound on `nu(k)`.

The remaining mathematical task is no longer vague path preservation.  It
is the uniform conditional inequality (4.5), or a correlated resampling
construction which enforces it.
