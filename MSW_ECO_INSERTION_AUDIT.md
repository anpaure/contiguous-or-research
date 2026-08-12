# Peak insertion in the MSW flip order: exact locality and the fixed-coordinate obstruction

## 1. Outcome

The MSW flip order has a stronger locality property than the usual Dyck
suffix identity.  Insert a peak `10` in **any** gap of a Dyck word.  In the
new MSW flip permutation, the two inserted coordinates are consecutive, and
deleting them recovers the old flip permutation exactly.

This gives a canonical two-seam description of every ECO child path.  It
does **not**, however, give a two-coordinate lift of an entire MSW factor:
the inserted gap, and hence the two coordinate labels being deleted, depends
on the Dyck root and on its ECO site.  Identifying these varying labels with
one fixed new pair requires a different coordinate permutation on every
path.  That destroys targetwise shadow provenance.

There is a sharp support witness for this obstruction.  If the same fixed
pair `p,q` were the consecutive inserted flips on every child path, then
each child would have all but at most one of its lower-middle vertices in
the one-tag sector.  Such paths cannot cover the entire zero-tag and two-tag
rectangles of the new middle layer.  The full MSW factor succeeds precisely
because the locally inserted pair varies.

Consequently the peak-insertion theorem is useful local algebra, but it does
not bypass the fixed-coordinate punctured-prism completion problem and does
not by itself prove a defect recurrence with coefficient two.

## 2. Definitions

Let `D_m` be the Dyck words of length `2m`.  The MSW flip permutation is
defined recursively by

\[
 \rho(\epsilon)=(),
 \qquad
 \rho(1u0v)=
 (|u|+2,\ |u|+2-\rho(\mu(u)),\ 1,\ |u|+2+\rho(v)),       \tag{2.1}
\]

where `mu` is reverse-complement and scalar addition/subtraction is applied
entrywise to a sequence.  Thus `rho(w)` is a permutation of the coordinate
positions of `w`.

Number the gaps of a word `w=w_1...w_N` by `g=0,...,N`, where gap `g` is
after the first `g` letters.  Let

\[
                         I_g(w)=w_1\cdots w_g\,10\,
                                  w_{g+1}\cdots w_N.      \tag{2.2}
\]

The inserted `1` and `0` are denoted by `p` and `q`, respectively.  Let
`iota_g` be the increasing injection from the old positions `[N]` to the
positions of `I_g(w)` that skips `p,q`.

Every gap insertion (2.2) is Dyck.  The standard ECO children are the
subfamily in which `g` lies along the final descent; restricting to those
gaps makes deletion of the rightmost peak a unique parent map.

## 3. Exact peak-insertion theorem

### Theorem 3.1

For every Dyck word `w` and every gap `g`, the sequence
`rho(I_g(w))` is obtained from `iota_g(rho(w))` by inserting one adjacent
two-letter block.  More precisely,

\[
 \rho(I_g(w))=
   (\iota_g(r_1),\ldots,\iota_g(r_a),\ \sigma_g(p,q),
     \iota_g(r_{a+1}),\ldots,\iota_g(r_N))             \tag{3.1}
\]

for some cut `a`, where

\[
 \sigma_g(p,q)=
 \begin{cases}
   (p,q),& h_w(g)\text{ is odd},\\
   (q,p),& h_w(g)\text{ is even}.
 \end{cases}                                           \tag{3.2}
\]

Here `h_w(g)` is the height of the Dyck path at gap `g`.

In particular, deleting `p,q` and order-preservingly relabelling the old
coordinates gives exactly

\[
                       \operatorname{del}_{p,q}
                         \rho(I_g(w))=\rho(w).          \tag{3.3}
\]

### Proof

Induct on the semilength.  Write the first-return decomposition

\[
                              w=1u0v.                  \tag{3.4}
\]

If the insertion gap lies in `v`, (2.1) leaves the first three blocks of
the flip order unchanged and applies the induction hypothesis inside the
last block `|u|+2+rho(v)`.  The global height at the gap equals its height
inside `v`, so both (3.1) and (3.2) are preserved.

Suppose instead that the insertion gap lies in `u`.  Then

\[
                         I_g(w)=1I_{g-1}(u)0v.          \tag{3.5}
\]

Reverse-complement maps the inserted peak to a peak at the reflected gap
of `mu(u)`, but it exchanges the identities of the two inserted letters:
the new `1` in `mu(I_{g-1}(u))` is the old letter `q`, and its new `0` is
the old letter `p`.  The standard path-reversal identity

\[
 \rho(\mu(x))=(N+1-r_N,\ldots,N+1-r_1)
 \quad\text{when }\rho(x)=(r_1,\ldots,r_N)             \tag{3.6}
\]

shows that adjacency and deletion survive the mirrored block in (2.1).
The exchange of `p,q` reverses the order in (3.2).  At the same time the
outer initial `1` raises the gap height by one, so its parity also reverses.
Thus (3.2) again has exactly the stated global parity.

The boundary gap immediately after the first primitive component is the
initial gap of `v` and is covered by the first case.  The gap before the
first letter gives

\[
                       \rho(10w)=\rho(10)\Vert
                                  (2+\rho(w)),          \tag{3.7}
\]

where `rho(10)=(q,p)` and the gap height is zero.  The gap after the final
letter similarly appends the block `(q,p)`.  These boundary identities
complete the induction.  Equation (3.3) is immediate from (3.1).  \(\square\)

### Corollary 3.2 (ECO path locality)

Let `c` be an ECO child of `w`.  After deleting the locally inserted
coordinates, the MSW path `P(c)` projects to `P(w)` without changing the
order of any old coordinate flip.  Before, between, and after the two new
flips there are at most three fixed-tag sections; hence the projected path
has at most two seams.

This statement is in the **omitted-label/flip-order path representation**.
The standard wreath order is obtained from the odd cycle by the step-two
reindexing.  Under that reindexing two adjacent flip positions become
nearly antipodal positions of the standard cyclic order.  Corollary 3.2
therefore does not, by itself, put every affected OR window in an
`O(H)`-neighbourhood of one standard-order seam.  A separate provenance
argument is required before the cut-halo lemma can be invoked.

For a parent whose final descent has length `ell`, the ECO child obtained
after `h` final zeros has inserted-flip order `(p,q)` exactly when
`ell-h` is odd, and `(q,p)` otherwise.

## 4. Why this is not a fixed two-coordinate lift

The ECO identity is path-local.  In `I_g(w)`, the labels `p,q` mean the
two **positions at gap `g`**.  Across the child family

\[
 \{I_g(w):w\in D_m,\ g\text{ an ECO site of }w\},      \tag{4.1}
\]

the value of `g` varies.  The order-preserving old-coordinate injection
`iota_g` therefore varies as well.  There is no common decomposition

\[
                   [2m+2]=X\mathbin{\dot\cup}\{p,q\}   \tag{4.2}
\]

for which Theorem 3.1 deletes the same two labels on every path.

One can force (4.2) separately on each path by conjugating it with a
coordinate permutation that sends its local insertion positions to the
chosen `p,q`.  But those conjugating permutations depend on `(w,g)`.  A
fixed old target `S subseteq X` is then sent to different subsets on
different child paths, so old shadow holes no longer have two fixed tagged
descendants.  This is exactly the targetwise information needed in a
contractive repair recurrence.

### Proposition 4.1 (sector-support obstruction)

There is no exact new middle-level factor in which every path is obtained
from an old path by inserting consecutive flips of one common fixed pair
`p,q`, with the old flip order otherwise unchanged.

### Proof

Start an extended path with tag state `{p}`.  The two consecutive flips
have one of two orders.

* In order `(p,q)`, the tag states are

  \[
                            \{p\}\longrightarrow
                            \varnothing\longrightarrow\{q\}.
  \]

  The middle state is one lower-middle vertex in the zero-tag sector.

* In order `(q,p)`, the tag states are

  \[
                            \{p\}\longrightarrow
                            \{p,q\}\longrightarrow\{q\}.
  \]

  The middle state is an upper-middle vertex.  Every lower-middle vertex
  on this path still has exactly one tag.

Thus every such path has all lower-middle vertices in the one-tag sector,
apart from at most one zero-tag vertex, and it has no two-tag lower-middle
vertex at all.  The rank-`m+1` layer on `X union {p,q}` contains the
nonempty rectangle

\[
                   \{K\cup\{p,q\}: |K|=m-1\}.        \tag{4.3}
\]

It cannot be covered by these paths, contradicting exact middle support.
\(\square\)

Proposition 4.1 pinpoints how the complete MSW factor evades the
contradiction: a path's locally inserted pair is not the same global pair
as the locally inserted pair of another path.

## 5. Relation to the Catalan count and the MNW alpha tuple

If `ell(w)` is the final-descent length, the ECO children of `w` are its
`ell(w)+1` peak insertions along that descent, and

\[
 \sum_{w\in D_m}(\ell(w)+1)=\operatorname{Cat}_{m+1}. \tag{5.1}
\]

The two endpoint sites contribute `2 Cat_m` children.  The internal sites
contribute

\[
 \sum_w(\ell(w)-1)
   =\operatorname{Cat}_{m+1}-2\operatorname{Cat}_m
   =D_m.                                               \tag{5.2}
\]

The parameterized MNW tuple

\[
 \alpha(w)=\{1w11000,\ 1w10100,\ 1w10010\}            \tag{5.3}
\]

is exactly the three ECO children of the parent `1w100`: it moves one peak
through the three sites of a final descent of length two.

No claim is made here that every three consecutive sites of an arbitrary
parent are one alpha context.  That stronger statement is not a formal
consequence of (5.3), and a context changes the surrounding owner paths as
well as the visible peak position.

It does not supply the required rank-transfer absorber by itself.  A
flipping tuple replaces alternating edges of one middle-level cycle and
therefore preserves the set of upper vertices used by that switch.  The
punctured-prism correction must instead replace excess zero-tag and two-tag
upper occurrences by missing one-tag upper occurrences.  Its local ledger
is

\[
                             (-1,+2,-1),              \tag{5.4}
\]

so an additional four-boundary rank-transfer identity is still required.

There is nevertheless no *counting* obstruction to a bounded Catalan
schedule.  The number of Dyck words of semilength `m` with final descent
exactly `ell` is the ballot number

\[
 N_{m,\ell}={\ell\over 2m-\ell}
               {2m-\ell\choose m},\qquad1\le\ell\le m.            \tag{5.5}
\]

Since

\[
 {N_{m,\ell}\over\operatorname{Cat}_m}
 = {\ell(m+1)\over2m-\ell}
   \prod_{j=0}^{\ell-1}{m-j\over2m-j}
 \le {2\ell\over2^\ell},                              \tag{5.6}
\]

we obtain the uniform second-moment bound

\[
 \sum_{w\in D_m}\ell(w)^2
 \le 2\operatorname{Cat}_m
       \sum_{\ell\ge1}{\ell^3\over2^\ell}
 =52\operatorname{Cat}_m.                              \tag{5.7}
\]

Thus even a hypothetical `O(ell(w)^2)` endpoint-safe globalization per
parent would have only `O(Cat_m)` total complexity.  What is missing is not
the Catalan mass estimate but the local **paired antipodal braid** which
moves between coordinate roles while retaining complementary endpoint
pairs and the targetwise upper colours.

## 6. Consequence for the global programme

There are two genuinely coordinate-consistent subfamilies inside the ECO
family.  For every `w in D_m`, concatenation locality gives

\[
                   \rho(w10)=\rho(w)\Vert(2m+2,2m+1),              \tag{6.1}
\]

while path reversal gives

\[
                   \rho(1w0)=(2m+2,\ 1+\operatorname{rev}\rho(w),\ 1).
                                                                    \tag{6.2}
\]

The terminal-peak roots `w10` and the primitive roots `1w0` are disjoint
for `m>=1`, and each family has `Cat_m` members.  The other roots therefore
number

\[
                   \operatorname{Cat}_{m+1}-2\operatorname{Cat}_m=D_m.
                                                                    \tag{6.3}
\]

These are exactly the two outer copies plus the residual Catalan mass in
the punctured-prism ledger.  Equations (6.1)--(6.2) are promising sources
for the two inherited repair sections.  Notice, however, that they delete
different global coordinate pairs (the final two positions in (6.1), and
the first and final positions in (6.2)).  A targetwise shadow table is still
needed before they can be counted as two fixed descendants of one old
hole.

Theorem 3.1 proves that the MSW recursion has exactly the desired
`O(1)`-seam locality **after a path-dependent coordinate deletion**.  A
contractive lift needs this locality after one common coordinate split.
The distinction is decisive:

* path-dependent deletion gives about four child embeddings per parent on
  average and no fixed target map;
* fixed deletion gives the desired two tagged sections, but Proposition
  4.1 shows that it cannot complete middle support without cross-sector
  braiding.

Therefore the remaining all-dimensional lemma is still the fixed-coordinate
punctured-prism braid (or an equivalent global coordinate-consistent
absorber).  The ECO theorem narrows what such a lemma must do: it must
globalize the locally varying peak coordinates while changing only
`O(Cat_m)` seams, rather than discover an unrelated new factor from
scratch.
