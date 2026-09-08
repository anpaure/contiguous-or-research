# Audit of the Catalan global-sharing theorem

## Verdict

The Catalan accounting theorem is correct.  For every fixed `p`, the
`p`-th moment of `1+ell(w)` over Dyck words of semilength `m` is
`O_p(Cat_m)`, and the displayed quadratic constant `52` is valid.

This moment theorem is already present in the project in
`MSW_ECO_INSERTION_AUDIT.md`, equations (5.5)--(5.7).  The new useful
packaging is the observation that an `O(ell(w)^2)` endpoint correction per
parent is still only Catalan-many corrections globally.

The proposed permutation-routing lemma is also correct as an abstract group
statement.  It does **not** prove the constant-one construction, because the
available OR-array switches have not been shown to form a dynamically closed
connected graph of ledger-neutral transpositions.  Static connectivity at
the initial chart is insufficient: earlier switches may destroy later local
moves or their colour/root witnesses.

The claimed `O(H)` halo cost is valid for actual length-`O(H)` neighbourhoods
of cuts in an already factorable word, by the cut-halo lemma in
`CONTRACTIVE_DEFECT_LIFT.md`.  It is not automatic for an abstract middle-row
portal switch.  One must first prove that the switch is realized by such an
actual factor-word patch and that compositions preserve all earlier upper
colours, lower roots, and pins.

Thus the rigorous new conclusion is a no-counting-obstruction theorem, not a
completed sharing construction.

## 1. Catalan moments

The number of Dyck words of semilength `m` with final descent exactly `j` is

\[
 a_{m,j}={j\over 2m-j}{2m-j\choose m},\qquad 1\le j\le m.
\]

Since

\[
 {a_{m,j}\over \operatorname{Cat}_m}
 ={j(m+1)\over 2m-j}
   \prod_{i=0}^{j-1}{m-i\over2m-i}
 \le 2j,2^{-j},
\]

we obtain, for fixed `p`,

\[
 \sum_{w\in\mathcal D_m}(1+\ell(w))^p
 \le 2\operatorname{Cat}_m
       \sum_{j\ge1}j(1+j)^p2^{-j}
 =O_p(\operatorname{Cat}_m).
\]

For `p=2`, using `(1+j)^2` gives another finite constant.  For the stated
unshifted quadratic moment,

\[
 \sum_w\ell(w)^2
 \le 2\operatorname{Cat}_m\sum_{j\ge1}j^3 2^{-j}
=52\operatorname{Cat}_m.
\]

In fact the quadratic moment has the sharper exact value

\[
 {1\over\operatorname{Cat}_m}\sum_w\ell(w)^2
 ={m(13m-1)\over(m+2)(m+3)}<13.
\]

To see this, the bivariate final-descent generating function is

\[
 A(z,u)=\sum_{m,j}a_{m,j}z^m u^j
 ={uzC(z)\over1-uzC(z)},
 \qquad C(z)=1+zC(z)^2.
\]

Applying `(u partial_u)^2` at `u=1`, and using
`zC(z)=1-1/C(z)`, gives

\[
 \sum_m\left(\sum_jj^2a_{m,j}\right)z^m
 =2C(z)^3-3C(z)^2+C(z).
\]

The standard coefficient formula
`[z^m]C(z)^q=q/(2m+q) binom(2m+q,m)` simplifies to the displayed rational
moment.  Thus `52` is valid but quite loose.

Similarly,

\[
 {1\over\operatorname{Cat}_m}\sum_w\ell(w)={3m\over m+2}.
\]

Consequently the moment that directly appears in the proposed routing cost
obeys the uniform sharp-enough estimate

\[
 \sum_w(1+\ell(w))^2<20\operatorname{Cat}_m.
\]

All inequalities, including the endpoint cases `j=m`, are valid.

Because

\[
 W(2m+1)={2m+1\choose m}=(2m+1)\operatorname{Cat}_m,
\]

`O(H Cat_m)=o(W(2m+1))` whenever `H=o(m)`.

## 2. Tail estimate correction

The choice `H=ceil(sqrt(m log m))` is sufficient for an `o(W)` binomial
tail.  Hoeffding gives, up to harmless endpoint shifts,

\[
 \sum_{s\le m-H-1}{2m+1\choose s}
 \le 2^{2m+1}\exp\left(-{2H^2\over2m+1}\right)
 =O(2^{2m+1}/m).
\]

Since `W(2m+1)=Theta(2^(2m+1)/sqrt(m))`, this is `o(W)`.

The stronger displayed claim `O(2^(2m+1)/m^2)` does not follow with the
unit coefficient in `H=sqrt(m log m)`.  It becomes valid after choosing a
sufficiently larger fixed coefficient, for example
`H=ceil(2 sqrt(m log m))`.  This correction does not affect the desired
asymptotic conclusion.

## 3. Abstract permutation neutralization

Let `G` be a connected graph on `r` strand labels and suppose every edge
transposition is available.  If `u=v_0,...,v_d=v` is a tree path, then

\[
 (v_0v_1)\cdots(v_{d-2}v_{d-1})(v_{d-1}v_d)
 (v_{d-2}v_{d-1})\cdots(v_0v_1)
\]

implements `(uv)` using `2d-1<2r` edge transpositions.  Every permutation is
a product of at most `r-1` arbitrary transpositions.  Hence any endpoint
permutation can be corrected with fewer than `2r(r-1)<2r^2` edge moves.

Together with the Catalan moment theorem, this proves the following
conditional accounting statement:

> If a parent of final-descent length `ell` has a state-stable connected
> transposition system on `O(1+ell)` strands, and every move costs an actual
> `O(H)` factor-word halo, then all endpoint corrections in generation `m`
> cost `O(H Cat_m)=o(W)`.

The qualifier **state-stable** is essential.  It means that after every
prefix of the correction word, all later required edge moves remain
realizable (or have certified conjugate replacements), and that their
witness/pin preservation is relative to the current word rather than only
to the original chart.

## 4. What remains unproved

The current project supplies local atomic rank-transfer squares and exact
cut-halo compression, but not the following combined theorem:

1. the usable neutral switches generate a connected transposition graph on
   the actual root-owned strands;
2. the graph remains dynamically usable after preceding switches;
3. every move preserves the one-tag colour bijection and the selected lower
   merge-forest roots;
4. every move is an actual factorable patch, so the `O(H)` halo and clean
   coordinate pins really exist; and
5. the final monodromy is the required antipodal endpoint ownership
   permutation.

Existing alpha switches are alternating circuits and generate only formal
even monodromy inside a component; they do not perform the endpoint-moving
boundary repair.  Thus connectedness of an abstract graph of desired
transpositions cannot be substituted for construction of the moves.

If the five properties above are proved, the moment theorem and routing
lemma immediately give

\[
 \nu(2m+1)\le W(2m+1)+o(W(2m+1)).
\]

The standard trimmed lift and
`W(2m+2)=2W(2m+1)` then give the same conclusion in even dimensions.

Until that local dynamic switch theorem is supplied, the correct status is:

\[
 \boxed{\text{quadratic local switch counts are asymptotically affordable,
 but compatible switches are not yet constructed.}}
\]

## 5. The atomic square is not the claimed neutral transposition

The canonical prism square in `PRISM_SEGMENT_COMPLETION.md`, Lemma 3,
replaces the opposite edges

\[
U_0U_1,\quad (xp)(xq)
\]

by the two cross edges

\[
U_0(xp),\quad U_1(xq).
\]

It preserves the degree of all four lower vertices, but its upper-colour
sector ledger is

\[
(-1,+2,-1).
\]

Therefore it is an atomic **rank-transfer** switch, not a ledger-neutral
endpoint transposition.  It also has zero endpoint boundary, so it cannot
perform the endpoint replacements forced by the MW sector imbalance

\[
(n_{00},n_{10},n_{01},n_{11})=(2D+C,2C,C,0).
\]

When the two removed edges belong to distinct paths, one switch may exchange
their tails.  This does not make it a universally available pure
transposition: if they occur on the same component it can split or close a
component, and after overlapping switches a later square need no longer be
alternating in the current factor.  Pairing several squares to cancel their
colour ledgers is an additional global construction, not a consequence of
the local four-cycle.

The alpha six-cycle switches have the same endpoint-boundary limitation.
They can generate a formal alternating permutation group on a connected
support, but every such switch preserves every vertex degree.  Hence they
can only correct pairing monodromy **after** a separate endpoint-moving
signed `T`-join has supplied a complement-invariant endpoint set.

## 6. Topological sections do not yet give factor halos

The existing MW/MSW comparison has an `O(C_m)` alternating-piece or
topological-section ledger.  That is not the same as a literal cut and
reconnect of old factor words.  In fact the bulk-transition no-go in
`MW_MSW_CATALAN_BRAID.md` proves that any transformation retaining old MW
segments requires at least

\[
(2m-3)C_m
\]

cuts, because that many old edges disappear.

Thus an `O(C_m)` abstract piece decomposition does not imply an
`O(HC_m)` factor-word halo.  The latter follows only after one supplies one
of the following:

1. literal old-segment provenance away from `O(C_m)` physical seams; or
2. a coordinate-consistent map carrying every length-`H` window of each
   long new section to a certified old window.

The path-dependent ECO deletion is a possible local map, but it has not
been globalized across the fixed-coordinate sectors.

Even genuine localization of the changed positions to `O(H)` around one
cut is only a support statement.  One still needs an explicit actual-factor
patch showing that the halo jointly realizes all changed upper targets,
lower roots and coordinate pins.  An `O(H)` set of affected positions can
support `Theta(H^2)` interval targets, so cardinality alone neither proves
nor disproves the required sharing.

Consequently the recurrence

\[
R_{m+1,H}\le2R_{m,H}+O(H\operatorname{Cat}_m)
\]

is a valid accounting theorem under a physical seam/halo hypothesis.  It is
not yet a theorem about the published MW/MSW or prism-switch construction.
