# The odd GK/complement factor is the dual centered PBBS factor

**Date:** 2026-08-13  
**Status:** unconditional all-parameter identification and forced-cycle
obstruction to one-per-upper thinning

## 0. Verdict

Put

\[
 m=r-1,\qquad n=2m+1=2r-1.                       \tag{0.1}
\]

For every `m`-set `L`, join its upward successor in the standard
Greene--Kleitman SCD to its upward successor in the complemented SCD.
This gives a Johnson `2`-factor on the rank-`m+1` layer with:

* every rank-`m` intersection colour exactly once;
* every rank-`m+2` union colour between one and three times; and
* at most `Cat_m` cycle components.

However, this is not a new factor.  Edgewise complementation identifies it
exactly with the centered PBBS factor

\[
                         \{f^{-1}(L),f(L)\}.        \tag{0.2}
\]

Consequently the known PBBS single-soliton obstruction transfers
literally.  For every `m>=3`, equivalently `r>=4`, one cycle of length
`2m+1` has globally singleton union colours on every edge.  Every selection
which retains one occurrence of every upper colour is forced to retain
that whole cycle.  Therefore:

> The GK/complement factor cannot be thinned to an upper-exact linear
> forest for any `r>=4`, even though lower colours are already exact,
> upper colours are surjective, and owner degree is two.

An ambient Johnson surgery can still escape; representative changes inside
the fixed factor cannot.

## 1. The two central GK matchings

Use binary words on the cyclic ground `Z_n`.  In the ordinary linear GK
matching, scan from left to right, pair each `1` with the last earlier
unmatched `0`, and let

\[
 g_+(L)=L+z_+(L)                                   \tag{1.1}
\]

be the upward successor, where `z_+(L)` is the first remaining unmatched
zero.  Define the complemented successor by

\[
 g_-(L)=\overline{gk_down(\bar L)}.                \tag{1.2}
\]

Every symmetric chain of `B_n`, with `n=2m+1`, meets both central ranks
`m,m+1` exactly once.  Hence

\[
 g_+,g_-:{[n]\choose m}\longrightarrow{[n]\choose m+1}
\tag{1.3}
\]

are bijections.

Let `r_+(L),r_-(L)` be the unique unmatched zeros under the forward and
reverse cyclic parenthesis matchings used for PBBS.  Linear cancellation
leaves the normal form

\[
                         1^a0^{a+1}.                \tag{1.4}
\]

The cyclic cancellations pair the `a` boundary pairs and leave the first
or last zero of the displayed zero block according to orientation.
Therefore, up to the harmless naming of the two cyclic orientations,

\[
 \boxed{
 \{z_+(L),z_-(L)\}=\{r_+(L),r_-(L)\},}
\tag{1.5}
\]

and in particular

\[
 \{g_+(L),g_-(L)\}
 =\{L+r_+(L),L+r_-(L)\}.                           \tag{1.6}
\]

The two coordinates are distinct for `m>=2`: equality would give a PBBS
two-cycle, whereas every PBBS orbit length is divisible by the odd number
`n>=5`.

## 2. Literal duality with PBBS

The PBBS permutation on rank-`m` sets is

\[
 f(L)=\bar L-r_+(L),\qquad
 f^{-1}(L)=\bar L-r_-(L).                          \tag{2.1}
\]

Complementing the two endpoints in `(1.6)` gives

\[
 \boxed{
 \overline{\{g_+(L),g_-(L)\}}
   =\{f(L),f^{-1}(L)\}.}                           \tag{2.2}
\]

The right side is exactly the centered PBBS edge indexed by `L`.
Therefore the entire GK/complement Johnson factor is the edgewise
complement of the centered PBBS factor.

This proves the owner-degree statement without computation.  Since `g_+`
and `g_-` are bijections, their union is a bipartite `2`-factor; after
suppressing the rank-`m` shore it is a Johnson `2`-factor on every
rank-`m+1` owner.

Its lower colour is

\[
 g_+(L)\cap g_-(L)=L,                              \tag{2.3}
\]

so lower colours are exact.  Its upper colour is

\[
 Q(L)=L+\{r_+(L),r_-(L)\}.                         \tag{2.4}
\]

On the PBBS side,

\[
 \overline{Q(L)}=f(L)\cap f^{-1}(L),               \tag{2.5}
\]

the q1 angle colour of the centered edge.  Thus upper-colour fibres of the
GK factor are precisely complementary PBBS q1 occurrence fibres.

## 3. Exact inherited ledgers

The audited PBBS first-shadow theorem says that every rank-`m-1` colour
has multiplicity between one and three.  Complementation and `(2.5)` give:

### Theorem 3.1 (GK/complement central ledgers)

For every `m>=2`:

1. the GK/complement edges form a spanning `2`-factor on
   `binom([2m+1],m+1)`;
2. every rank-`m` lower colour occurs exactly once; and
3. every rank-`m+2` upper colour `U` satisfies

   \[
                         1\le\mu(U)\le3.            \tag{3.1}
   \]

If a PBBS orbit has length `h`, its centered step-two graph has
`gcd(2,h)` components, each of length `h/gcd(2,h)`.  Hence the same is true
of the GK/complement factor.  PBBS orbit homomesy implies that every `h` is
divisible by `n`, and the standard action-angle census gives at most

\[
                         \operatorname{Cat}_m       \tag{3.2}
\]

components in total.

These conclusions are exactly the already-proved PBBS ledgers in dual
rank notation; no new asymptotic inference is required.

## 4. Why upper-exact thinning would otherwise be ideal

The factor has

\[
 V={2m+1\choose m}
\tag{4.1}
\]

edges, whereas the upper palette has

\[
 F={2m+1\choose m-1}.                              \tag{4.2}
\]

Selecting one representative edge from each upper fibre would retain
exactly `F` edges.  It would automatically preserve:

* one occurrence of every upper colour;
* injectivity of lower colours, since they were exact before thinning; and
* maximum owner degree at most two, since it is a subgraph of a `2`-factor.

Such a subgraph is a linear forest if and only if the deleted occurrences
meet every factor cycle.  Thus the only remaining condition inside this
fixed factor is an omission transversal of its cycles.

## 5. The single-soliton cycle is forced

The PBBS single-soliton theorem applies for every `m>=3`.  In GK rank
notation, its dual cycle has the `n=2m+1` vertices given by the rotations
of

\[
                         0^m1^{m+1}.                \tag{5.1}
\]

Its upper colours are the rotations of

\[
                         0^{m-1}1^{m+2}.            \tag{5.2}
\]

The complementary PBBS q1 colour is

\[
                         1^{m-1}0^{m+2}.            \tag{5.3}
\]

The exact occurrence/fixed-point calculation for `(5.3)` gives

\[
                         \mu=1                     \tag{5.4}
\]

when `m>=3`.  Rotation equivariance gives the same multiplicity for every
edge colour around the cycle, and the `n` rotations are distinct.

### Theorem 5.1 (forced GK cycle)

For every `r>=4`, every subgraph of the GK/complement factor containing at
least one occurrence of every rank-`r+1` upper colour contains the entire
cycle of rotations of

\[
                         0^{r-1}1^r.                \tag{5.5}
\]

In particular, no one-per-upper selection inside this factor is acyclic.

#### Proof

Put `m=r-1`.  Each of the `2r-1` colours on the displayed cycle has global
multiplicity one by `(5.2)--(5.4)`.  Upper coverage therefore forces every
one of its edges.  They form the full cycle `(5.5)`. \(\square\)

Equivalently, the cycle-hit Hall system has the support-minimal cut
consisting of this single component: every incident colour has omission
capacity `mu-1=0`.

## 6. Exact scope

The obstruction is decisive only for **thinning the fixed factor**.  It
does not refute a pathization which replaces one of the forced edges by an
ambient Johnson diamond of the same upper colour, or which performs a
multi-colour palette-preserving exchange.  Such a repair must create an
external occurrence for at least one colour in `(5.2)` and simultaneously
preserve lower-colour injectivity and owner degree two.

So the GK/complement discovery contributes a clean reidentification and a
sharp repair interface, not a new proof of Catalan pathization.

## 7. Dependencies

The only imported PBBS results are already proved and independently
audited in this workspace:

* `MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md`;
* `MATH_AUDIT_PBBS_FIRST_SHADOW_AND_CENTERED_JOHNSON_FACTOR_20260726.md`;
  and
* `MATH_THEOREM_PBBS_SINGLE_SOLITON_FORCED_CYCLE_OBSTRUCTION_20260805.md`.

The new content here is the literal edgewise identity `(2.2)` and its
translation to the odd GK/complement rank convention.
