# Clustered product banks admit a coherent integral phase-origin transport

**Status (2026-08-21).**  Every assertion below is proved.  Conditional on
the complementary-rank tight-cycle factors used by the two-block product
route, the order pairs can be placed in nested cross-rank columns and given
one counter-origin shift per column so that every upper profile and every
phase diagonal has capacity within `b^2` of its uniform fractional value,
simultaneously for all offsets in the DCC band.  Consequently the aggregate
deficit in the equal-phase-bin relaxation is still
`O(W_b b^(-1/4))=o(W_b)`.

This is an integral theorem about **phase origins and profile counts**.  It
does not make the cyclic orders in one column equal or otherwise compatible,
and it does not assign labelled targets.  The remaining theorem must create
that cross-rank order compatibility; no phase-origin rounding obstruction
remains after it does.

## 1. Conditional order-pair counts and Ferrers columns

Let `b` tend to infinity through odd primes and let

\[
 W_b={2b\choose b},\qquad
 H/\sqrt b\longrightarrow\infty,\qquad H=o(b^{2/3}).       \tag{1.1}
\]

Put

\[
 I=\{H+2,\ldots,b-H-2\}.
\]

Conditionally assume, for every `r in I`, a tight-cycle factor of the
rank-`r` subsets of `A` and a tight-cycle factor of the rank-`(b-r)` subsets
of `B`, where `|A|=|B|=b`.  Each factor contains

\[
 F_r={1\over b}{b\choose r}
\]

cyclic orders, so the product construction has

\[
 N_r=F_r^2=\left({1\over b}{b\choose r}\right)^2          \tag{1.2}
\]

order pairs at payload rank `r`.  These are integers because `b` is prime
and `0<r<b`.

Enumerate the order pairs at rank `r` arbitrarily by
`j=0,...,N_r-1`.  Pair entries with the same index `j` across ranks, allowing
a column to be absent at ranks where `j>=N_r`.  Since `binom(b,r)` is
symmetric and unimodal in `r`, the rank support

\[
 I_j=\{r\in I:j<N_r\}                                  \tag{1.3}
\]

of every column is an interval (possibly empty).  This is the Ferrers
columnization of the rank-wise order-pair counts.  It asserts no compatibility
between the actual cyclic orders occupying a column.

Give every atom in column `j` the common relative counter-origin shift

\[
 \theta_j=j\pmod b.                                    \tag{1.4}
\]

Changing this relative origin only translates every counter-sum phase
diagonal of the atom.  It changes neither its middle target set, legality,
nor internal band simplicity.

For `theta in Z_b`, let

\[
 x_{r,\theta}=|\{0\le j<N_r:j\equiv\theta\pmod b\}|.  \tag{1.5}
\]

Then, simultaneously for every `r` and `theta`,

\[
 \left|x_{r,\theta}-{N_r\over b}\right|<1.             \tag{1.6}
\]

Thus one common shift per cross-rank interval column gives the optimal
floor/ceiling rounding of every rank marginal at once.

## 2. Uniform phase-diagonal discrepancy

For the clustered schedule `tau_r=A^rB^(b-r)`, put

\[
 P_r=\{0,\ldots,r-1\}\subseteq\mathbb Z_b,
 \qquad J_p(q)=\{p+1,\ldots,p+q\}\pmod b,
\]

\[
 \phi_p^{(q)}(r)=r+|P_r\cap J_p(q)|.                   \tag{2.1}
\]

Fix `1<=q<=H` and a central split rank `s in [b/4,3b/4]`.  For all
sufficiently large `b`, every relevant payload `r=s-z`, `0<=z<=q`, lies in
`I`.  Define its contributing base phases by

\[
 S_{r;q,s}=\{p\in\mathbb Z_b:\phi_p^{(q)}(r)=s\}.      \tag{2.2}
\]

The clustered interval count gives

\[
 \sum_{r\in I}|S_{r;q,s}|=b-q.                        \tag{2.3}
\]

Indeed, the terms `z=0,q` contribute respectively
`b-s-q+1` and `s-2q+1` phases, while each `1<=z<=q-1`
contributes two.

After an atom in column `j` receives shift `theta_j`, a base phase `p`
at upper offset `q` occupies counter-sum diagonal
`d=p+q+theta_j`.  Each such diagonal contains `b` counter pairs.  Hence the
integer occurrence capacity placed in diagonal `d in Z_b` at profile
`(q,s)` is

\[
 C_{q,s,d}
 =b\sum_{r\in I}\sum_{p\in S_{r;q,s}}
       x_{r,d-q-p}.                                    \tag{2.4}
\]

The total profile capacity is

\[
 T_{q,s}=b\sum_{r\in I}N_r|S_{r;q,s}|,                \tag{2.5}
\]

which is exactly

\[
 {1\over b}\left[(b-s-q+1){b\choose s}^2
 +(s-2q+1){b\choose s-q}^2
 +2\sum_{z=1}^{q-1}{b\choose s-z}^2\right].          \tag{2.6}
\]

### Theorem 2.1 (simultaneous integral origin balancing)

For every admissible `q,s,d`, the single column assignment (1.4) satisfies

\[
 \boxed{\left|C_{q,s,d}-{T_{q,s}\over b}\right|<b^2.} \tag{2.7}
\]

The same assignment works simultaneously for every upper offset, split
profile, and phase diagonal.

#### Proof

Substitute (1.6) into (2.4) and compare with (2.5) divided by `b`.  The
absolute discrepancy is less than

\[
 b\sum_{r\in I}|S_{r;q,s}|=b(b-q)<b^2
\]

by (2.3).  No constraint is rounded separately: all of them use the one
column shift `theta_j` fixed in (1.4).  \(\square\)

## 3. The equal-phase-bin flow relaxation has sublinear deficit

The rank-`(b+q)` split profile with `s` letters in `A` has demand

\[
 P_{q,s}={b\choose s}{b\choose s-q}.                  \tag{3.1}
\]

On the central interval both binomial factors are divisible by the prime
`b`, so the equal phase-bin demand `P_(q,s)/b` is an integer.  Define the
phase-only transport deficit by

\[
 D_{\rm ph}
 =\sum_{q=1}^H\sum_{s=b/4}^{3b/4}\sum_{d\in\mathbb Z_b}
   \left[{P_{q,s}\over b}-C_{q,s,d}\right]_+
 +\sum_{q=1}^H\sum_{s\notin[b/4,3b/4]}P_{q,s}.        \tag{3.2}
\]

Integer endpoints in (3.2) may be rounded inward; this changes only the
already charged tail convention.

### Theorem 3.1 (phase-origin transport has no linear obstruction)

With the shifts (1.4),

\[
 \boxed{D_{\rm ph}=O(W_b b^{-1/4})=o(W_b).}            \tag{3.3}
\]

#### Proof

For each central `(q,s,d)`, Theorem 2.1 and
`[a-(y+e)]_+<=[a-y]_++|e|` give

\[
 \left[{P_{q,s}\over b}-C_{q,s,d}\right]_+
 \le {1\over b}[P_{q,s}-T_{q,s}]_+ +b^2.              \tag{3.4}
\]

Sum over the `b` diagonals.  The pooled profile-capacity theorem gives

\[
 \sum_{q=1}^H\sum_s[P_{q,s}-T_{q,s}]_+
   =O(W_b b^{-1/4}),                                  \tag{3.5}
\]

where profiles outside the central interval are charged in full.  There are
`O(Hb)` central profile pairs, so the rounding term from (3.4) is at most
`O(Hb^4)`.  This is polynomial in `b` and hence
`o(W_b b^{-1/4})`.  Equations (3.4)--(3.5) prove (3.3).  \(\square\)

## 4. Exact remaining order-bank gate

The Ferrers columns solve the smallest count-level coupling problem:

- every payload order pair is used once;
- a single origin is assigned to a column across all ranks in its interval;
- every rank marginal is floor/ceiling balanced over the `b` shifts; and
- every `q,s,d` phase-bin constraint is met up to polynomial discrepancy,
  whose aggregate cost is `o(W_b)`.

What the arbitrary enumeration in Section 1 does not provide is a common
labelled order coordinate.  To turn (3.3) into target coverage, one must
enumerate or modify the complementary tight-cycle factors so that, for all
but `o(W_b)` relevant column mass, the cyclic orders occupying one Ferrers
column have compatible interval-set coordinates at neighboring payload
ranks on both `A` and `B`.  The same labelled target must then be assigned at
most once across those coordinated occurrences.  Ordinary rank-by-rank
Baranyai--Katona factors do not supply such an enumeration, and independent
relabeling leaves the known one-quarter adjacent-rank miss.

Thus neither scalar profile volume nor integral phase-origin transport is the
remaining gate.  The gate is a simultaneous cross-rank factor coupling in
the labelled interval geometry.

