# Independent audit of `FOUR_BOX_FACTOR_ESCAPE_RESEARCH.md`

## Verdict

The main theorem is correct.  The padded row satisfies the global
delay-`D` run condition, its maximal factor is one ordinary max-word, and
every point in the stated central rank band is represented.  The block count
and length bound

\[
 M_m+D(11m^2+13m+3)
\]

are also correct.  Taking `D=2m-1` and appending the full point gives the
stated all-nonzero equal-box bound with the displayed polynomial exactly.

Two local statements need correction or qualification.

1. In Section 4, the lower truncated block does not literally contain
   **every** lower-fan witness of depth at most `D`.  When `D<r`, it omits the
   canonical witness with
   \[
       x=r,\qquad t=r-D,
   \]
   whose depth is exactly `D`.  This is not a gap in Theorem 5: residual
   tail targets always have `x<r`; the omitted `x=r` point has second hook
   radius `K=r` and belongs to the central square, where a diagonal already
   covers it.  The sentence should say “every **residual** lower-fan witness
   of depth at most `D`.”
2. Section 10.3 says that at a right-boundary run the choice `j=l+D` has a
   truncated factor window ending at `L`.  Its actual endpoint is
   `min(L,l+D)`, which need not equal `L`.  It is nevertheless contained in
   the right-boundary run, so Lemma 1 remains valid.

The peak-atom lower bound is valid for the full canonical fans of radius at
least two.  Applied to the truncated blocks, its direct proof requires
`D>=2`, so that both canonical peak neighbours remain present.  This is
enough for the claimed `Omega(Dm^2)` order when `D>=2`.  For `D=1`, the
overall literal architecture already has `Theta(m^2)` raw fan mass, but
Proposition 6 alone does not prove that the **padding portion** must have
that order.

No constant-one Boolean conclusion follows.  The theorem is for equal boxes
`[0,m]^4`, covers only a band at near-width cost, and does not supply the
complete generally unequal-box surface estimate required by the aggregation
theorem.

## 1. Central coefficient and prefix encoding

Inclusion-exclusion gives

\[
 [z^{2m}](1+z+\cdots+z^m)^4
 =\binom{2m+3}{3}-4\binom{m+2}{3}
 =\frac{2m^3+6m^2+7m+3}{3}.
\]

Thus the formula for `M_m` is exact.

The prefix encoding

\[
 x_c\longmapsto\{(c,s):1\le s\le x_c\}
\]

is injective, and coordinatewise maximum/minimum become set union/
intersection.  Every factor entry obtained as a coordinatewise minimum of
box points remains in `[0,m]^4`.  Hence proving the set-union identities is
enough to produce an ordinary coordinatewise-max word.

## 2. Audit of Lemma 1

For a row `T_1,...,T_L`, define

\[
 A_j=\bigcap_{i=\max(1,j-D)}^{\min(L,j)}T_i,
 \qquad1\le j\le L+D.
\]

Fix one atom and let `[a,c]` be a maximal run of ones in its incidence word.
The standard erosion/dilation criterion is exact:

\[
 T_i=\bigvee_{j=i}^{i+D}A_j\quad(1\le i\le L)
\]

if and only if every internal run has length at least `D+1`; boundary runs
may be shorter because factor windows truncate at positions `1` and `L`.

Now let `l<=r` and `r-l<=D`.  For every `j in [r,l+D]`, the defining
`T`-interval of `A_j` contains `[l,r]`.  Indeed,

\[
 j-D\le l,\qquad j\ge r,
\]

and truncating at the two global boundaries does not remove a member of
`[l,r]`.  Therefore an atom absent anywhere on `[l,r]` is absent from every
such `A_j`.

Conversely, suppose the atom is present throughout `[l,r]`.

* If `[a,c]` is internal, candidate full erosion windows have endpoints
  `j in [a+D,c]`.  The intervals `[r,l+D]` and `[a+D,c]` intersect because
  \[
  r\le l+D,\quad r\le c,\quad a+D\le l+D,
  \quad a+D\le c.
  \]
  Any endpoint in their intersection supplies an `A_j` containing the atom.
* If `a=1`, take `j=r`; then
  \[
     [\max(1,r-D),r]\subseteq[1,c].
  \]
* If `c=L`, take `j=l+D`; then
  \[
     [l,\min(L,l+D)]\subseteq[a,L].
  \]

This proves, including both boundaries,

\[
 \bigvee_{j=r}^{l+D}A_j=\bigcap_{i=l}^{r}T_i.
\]

The right-boundary interval does not necessarily end at `L`; the corrected
endpoint above is all the proof needs.

Taking `l=r=i` yields the factor equation.  Uniting those overlapping
factor windows for `i=l,...,r` yields exactly the integer interval
`[l,r+D]`, and therefore

\[
 \bigvee_{i=l}^{r}T_i=\bigvee_{j=l}^{r+D}A_j.
\]

No cyclic convention, sentinel point, or implicit zero term is present.

## 3. Hook parametrization

For `-H<=p<=H`,

\[
 \gamma_H(p)=
 \begin{cases}
   (H+p,m-H),&p\le0,\\
   (H,m-H+p),&p\ge0.
 \end{cases}
\]

It is coordinatewise nondecreasing in `p` and has coordinate sum `m+p`.
Given `(x,y) in [0,m]^2`, set

\[
 H=\max(x,m-y),\qquad p=x+y-m.
\]

If `x<=m-y`, this gives the negative arm; if `x>=m-y`, it gives the positive
arm.  Thus every square point has exactly one hook coordinate `(H,p)`, and
every four-box point has exactly one representation

\[
 X(H,p;K,q)=(\gamma_H(p),\gamma_K(q)).
\]

Its rank is `2m+p+q`.

For `H>=K`, the diagonal

\[
 T_{H,K}(s)=(\gamma_H(s),\gamma_K(-s)),
 \qquad-K\le s\le K,
\]

is well-defined.  For `s<=t`, monotonicity gives

\[
 \bigvee_{u=s}^{t}T_{H,K}(u)
   =(\gamma_H(t),\gamma_K(-s)),
\]

and

\[
 \bigwedge_{u=s}^{t}T_{H,K}(u)
   =(\gamma_H(s),\gamma_K(-t)).
\]

Hence all targets with `|p|<=K` have the diagonal witnesses used in Theorem
5.  This remains true when `H=K`; only the residual fan discussion requires
strict `H>K`.

## 4. Audit of Lemma 2

### Upper fan

The order is

\[
 U_{r-1},\ldots,U_0,V_1,\ldots,V_r.
\]

The interval beginning at `U_x` and ending at `V_t` consists of

\[
 U_x,U_{x-1},\ldots,U_0,V_1,\ldots,V_t,
\]

so it has exactly

\[
 (x+1)+t=x+t+1
\]

terms.  Its first-pair maximum is attained at `U_0` and its second-pair
maximum is `(x,m-r+t)`, proving (3.6).  The latter pair has hook deviation

\[
 q=x-r+t.
\]

With `p=r`, the rank depth is

\[
 p+q=x+t,
\]

exactly one less than the witness length.

### Lower fan

For `t<r`, the canonical interval is

\[
 A_x,A_{x+1},\ldots,A_r,B_{r-1},\ldots,B_t;
\]

for `t=r` it ends at `A_r`.  It has

\[
 (r-x+1)+(r-t)=2r-x-t+1
\]

terms.  The coordinatewise minimum is (3.9), whose deviation is

\[
 -r+(x-r+t)=-(2r-x-t).
\]

Thus its lower depth is `2r-x-t`, again exactly one less than the witness
length.  Lemma 2 is correct for its full displayed parameter ranges.

### Exact truncation range

For an upper residual target, `x+t<=D` implies

\[
 x\le D-1,\qquad t\le D,
\]

so (4.1)--(4.2) retain its whole witness.

For a lower **residual** target one has `x<r`.  Put

\[
 \alpha=r-x\ge1,\qquad\beta=r-t\ge0.
\]

Depth at most `D` says `alpha+beta<=D`.  Therefore

\[
 \alpha\le\min(D,r),
\]

and, when `beta>0`,

\[
 \beta\le D-1.
\]

These are exactly the retained `A` and `B` ranges in (4.3)--(4.4).

The unrestricted sentence in Section 4 has the one exception described in
the verdict: if `D<r`, then `x=r,t=r-D` has depth `D` but needs the omitted
term `B_(r-D)`.  Its second square point is

\[
 (r,m-D)=\gamma_r(r-D),
\]

so its hook radius is `K=r` and `|p|=K`; it is a central-square point rather
than a residual target.  Theorem 5 loses nothing.

Both truncated block lengths are at most `2D`:

\[
 |\mathcal U|=a+1+b\le2D,
 \qquad
 |\mathcal L|=c+1+e\le2D.
\]

## 5. Exhaustive run-shape audit of Lemma 3

An atom in coordinate `c` and at height `s` is present exactly when that
coordinate is at least `s`.  It therefore suffices to audit the scalar
coordinate sequences in each block.

### Diagonal blocks

Along a diagonal, the two coordinates of `gamma_H(s)` are nondecreasing and
the two coordinates of `gamma_K(-s)` are nonincreasing.  A threshold word of
a nondecreasing sequence is a suffix; that of a nonincreasing sequence is a
prefix.  Constants give all ones or all zeros.  Item 1 is exact.

### Lower fan blocks

Across the retained `A` arm and then the retained `B` arm, the first hook
parameter decreases to `-r` and then increases.  Since `gamma_H` is
coordinatewise nondecreasing, each first-pair coordinate has a valley.  Its
superlevel word is a prefix union a suffix.

For the second pair:

* its first coordinate increases along the `A` arm and then remains `r` on
  the `B` arm, so its atom words are suffixes (or all ones/zeros);
* its second coordinate is `m` on the `A` arm and decreases on the `B` arm,
  so its atom words are prefixes (or all ones/zeros).

Thus every lower-block atom word is a union of a prefix and a suffix; there
is no hidden internal one-run.

### Upper fan blocks

The first hook parameter increases to `r` at `U_0` and then decreases.
Every first-pair coordinate is therefore unimodal with its maximum at the
peak.  A threshold word is either boundary-touching or one internal interval
containing `U_0`.

In the second pair, the first coordinate decreases on the `U` arm and is
zero on the `V` arm, giving a prefix word; the second coordinate is constant
on the `U` arm and increases on the `V` arm, giving a suffix word.  Hence an
upper block has at most one internal run for any atom, and every such run
contains the peak.  This covers all four coordinate types and proves item 3.

Transposing the two coordinate pairs merely permutes the four atom families,
so all three conclusions survive in the transposed blocks.

## 6. Global padding and seams

Replacing a distinguished point by `D+1` identical copies adds `D`
positions and gives every atom in that point a plateau of length `D+1`.
If endpoint and peak designations coincide, processing both designations may
add redundant copies but never exceeds the separate `D`-per-designation
upper count used later.

Inside one padded block:

* every diagonal one-run touches an endpoint;
* every lower-fan one-run touches an endpoint;
* every upper-fan one-run either touches an endpoint or contains the padded
  peak.

Thus any one-run that becomes globally internal while remaining in one block
already has a `D+1` plateau.  A run crossing a seam contains the padded last
point of the left block whenever it is one there, the padded first point of
the right block whenever it is one there, or both.  If a zero on one side
cuts the run at the seam, the run on the other side still contains its own
endpoint plateau.  Therefore every global internal one-run has length at
least `D+1`, independently of the order of the blocks.

Repeating terms does not change any selected meet or join.  A selected lower
witness has canonical length at most `D+1`.  If a selected endpoint is
padded, choose the copy adjacent to the block interior; the physical witness
then contains only one copy of that endpoint and retains its canonical
length.  No selected lower witness traverses an upper-fan peak plateau,
because upper fan blocks are used only for upper joins.  Diagonal and lower
fan witnesses therefore remain eligible for Lemma 1.

The corresponding factor interval is allowed to extend across a raw block
boundary.  This causes no contamination: Lemma 1 and the factor equation are
global statements about the fully padded concatenation, so any terms across
the seam are already included in the exact erosion identity.

## 7. Exhaustive coverage audit of Theorem 5

Let `X(H,p;K,q)` be arbitrary and first assume `H>=K`.

### Central square: `|p|<=K`

Both `p` and `-q` lie in `[-K,K]`.

* If `p+q>=0`, then `-q<=p`, and the join of
  \[
       T_{H,K}(-q),\ldots,T_{H,K}(p)
  \]
  is the target.
* If `p+q<=0`, then `p<=-q`, and the meet of
  \[
       T_{H,K}(p),\ldots,T_{H,K}(-q)
  \]
  is the target.

In both cases the number of terms is `|p+q|+1`.  At equality zero either
description degenerates to the same singleton.  Hence every central-square
target in the band has the required witness.

### Upper residual tail: `p>K`

Put `r=p`.  Then `K<r`.  If the second square point is `(x,y)`, the hook
formula `K=max(x,m-y)` gives

\[
 0\le x<r,qquad y>m-r.
\]

There is a unique `t in {1,...,r}` with `y=m-r+t`.  Thus the target has the
upper-fan form (3.6).  Moreover

\[
 p+q=x+t\ge1.
\]

If it lies in the band, `x+t<=D`, so its retained upper witness exists.

### Lower residual tail: `p<-K`

Put `r=-p`; again `K<r`, and the same unique parametrization gives
`0<=x<r` and `1<=t<=r`.  Its lower depth is

\[
 -(p+q)=2r-x-t.
\]

Band membership makes this at most `D`; the residual truncation calculation
in Section 4 shows that the retained lower witness exists and has at most
`D+1` terms.

These cases are mutually exhaustive when `H>=K`.  If `K>H`, transposition of
the coordinate pairs puts the target into exactly the same three cases.
When `H=K`, every `p` already satisfies `|p|<=K`, so no fan case is missing.

Upper witnesses become factor maxima by the unrestricted union identity.
Lower witnesses become factor maxima by the short-intersection identity.
Middle targets follow from the factor equation itself.  This covers every
rank from `2m-D` through `2m+D`, including zero and the full point when
`D=2m`.

If only nonzero targets are required, deleting every zero factor entry
preserves all chosen nonzero witnesses: after global deletion, the nonzero
entries formerly lying in one interval remain consecutive and have the same
maximum.  If the zero target is required, at least one zero entry must of
course be retained or prepended.

## 8. Exact block and length count

There are `(m+1)^2` diagonal blocks, one for each `(H,K)`.  Their total
length is exactly `M_m`, because their points are precisely the rank-`2m`
box points, once each.

The number of pairs

\[
 1\le r\le H\le m
\]

is

\[
 N=\sum_{H=1}^{m}H=\frac{m(m+1)}2.
\]

For every pair there are an upper and lower block in each of two coordinate
orientations, hence `4N` fan blocks.  Each has raw length at most `2D`, so
their aggregate raw length is at most

\[
 8DN=4Dm(m+1).
\]

The total block count is

\[
 (m+1)^2+4N=(m+1)(3m+1).
\]

Endpoint padding adds at most `2D` positions per block.  There are `2N`
upper blocks, and peak padding adds at most `D` positions to each.  Therefore

\[
\begin{aligned}
 L
 &\le M_m+4Dm(m+1)
       +2D(m+1)(3m+1)+Dm(m+1)\\
 &=M_m+D(11m^2+13m+2).
\end{aligned}
\]

The maximal factor has positions `1,...,L+D`, so its length is at most

\[
 M_m+D(11m^2+13m+3).
\]

No hidden factor of `m` occurs: the construction repeats whole points, and
one repeated point pads every atom it contains simultaneously.

Since `M_m=(2/3)m^3+O(m^2)`, every `D=o(m)` makes the additive term
`o(M_m)`.  This is uniform in such `D`; it is not a full-box estimate.

## 9. The `D=2m-1` all-nonzero specialization

At `D=2m-1`, Theorem 5 covers exactly every rank from `1` through `4m-1`.
Appending the full point `(m,m,m,m)` covers the only remaining nonzero rank.
Existing witnesses remain internal to the preceding factor word.

The resulting length bound is

\[
\begin{aligned}
 M_m+(2m-1)(11m^2+13m+3)+1
 &=M_m+22m^3+15m^2-7m-2,
\end{aligned}
\]

which agrees with (1.4).  This is a valid bound for the nonzero local
quantity `g_4(m,m,m,m)`.  For a version demanding the all-zero target, one
must retain or prepend a zero as one additional position unless the factor
already retains one.

## 10. Scope of the peak-atom obstruction

For `r>=2`, the atom

\[
 b_{H,r}=(2,m-H+r)
\]

is legal because `1<=m-H+r<=m`.  Along the canonical upper fan, the second
coordinate of the first hook pair attains this threshold only when the hook
parameter equals `r`, namely at `U_0`.  Its canonical neighbours `U_1` and
`V_1` omit it.

If those neighbours remain on opposite sides of a contiguous peak region,
the maximal one-run containing `U_0` is globally internal and must have at
least `h+1` occurrences in any delay-`h` factorable row.  At least `h`
additional atom-containing terms in that region are therefore necessary.
Peak regions of distinct literal fan blocks are disjoint.

Over two orientations, the number of radius-at-least-two upper blocks is

\[
 2\sum_{H=2}^{m}(H-1)=m(m-1)=\Theta(m^2).
\]

Thus full literal fans with common delay `h` require `Omega(hm^2)` extra
peak-region occurrences.  The longest required residual lower witness is
obtained at `r=m,x=0,t=1`; it has depth `2m-1` and `2m` terms.  Translating
all canonical lower-fan witnesses with one fixed erosion delay therefore
requires `h>=2m-1`, yielding `Omega(m^3)` extra length.

For the depth-truncated block, both `U_1` and `V_1` are retained whenever
`D>=2` and `r>=2`; Proposition 6 then directly yields the same
`Omega(Dm^2)` order as the peak-padding term.  When `D=1`, `U_0` is a block
endpoint and this particular internal-run argument does not apply.  The
overall architecture still emits `Theta(m^2)` raw fan terms, so its total
surface-order excess remains, but optimality of the endpoint/peak padding
alone is not established by Proposition 6.

The proposition is architectural, not universal.  It does not rule out
interleaving terms from different fans, sharing peak-containing points,
using alternate witnesses, or abandoning one common fixed delay.

## 11. Aggregation and asymptotic scope

The theorem is an equal-box statement for `P_m=[0,m]^4`.  It provides a
near-width word only for the central band when `D=o(m)`.  Appending all
outside points literally does not repair this at near-width cost:

\[
 R_m(D)\ge(m+1)^4-(2D+1)M_m=\Theta(m^4)
\]

for `D=o(m)`, using symmetry and unimodality of the rank coefficients.

If `D=2m-h` with `h<=m`, one lower extreme tail has exactly

\[
 \sum_{r=0}^{h-1}[z^r](1+z+\cdots+z^m)^4
 =\binom{h+3}{4}
\]

points, because the coordinate upper bounds are inactive in these ranks.
Making literal tails `o(M_m)` therefore requires

\[
 h=o(m^{3/4}),
\]

which forces `D=(2-o(1))m`; then the proved `Theta(Dm^2)` padding/fan error
is itself `Theta(M_m)`.

The fixed-dimension grid reduction requires a complete estimate for every,
generally unequal, four-box:

\[
 g_4(\ell_1,\ldots,\ell_4)
 \le w(\ell_1,\ldots,\ell_4)
      +O((1+\ell_1+\cdots+\ell_4)^2).
\]

Theorem 5 proves neither completeness nor the unequal-box extension.
Consequently it gives no `1+o(1)` Boolean result and no exact formula for the
original problem.  Its proved contribution is narrower but genuine: in the
equal four-box geometry, the depth-truncated fan shadows admit one explicit
max-factor word at every prescribed delay, and that word is near width for
every sublinear band.

## 12. Claim ledger

| Claim | Audit status | Exact qualification |
|---|---|---|
| Lemma 1 erosion identities | proved | Section 10.3 has one incorrect endpoint description, not an identity error. |
| Hook parametrization and rank formula | proved exactly | Includes `H=K`; fans are needed only for strict imbalance. |
| Lemma 2 depth equals witness length minus one | proved exactly | Both upper and lower ranges. |
| Upper truncated block retains all shallow witnesses | proved | For residual upper targets. |
| Lower truncated block retains every shallow fan witness | false literally | True for every residual target `x<r`; omitted `x=r` boundary case is central and already covered. |
| Lemma 3 run shapes | proved | All four coordinates and transposed blocks checked. |
| Lemma 4 arbitrary-order seam padding | proved | Repetitions are physical points, not atomwise padding. |
| Theorem 5 band coverage | proved | No missing `H=K`, sign-zero, transposed, or boundary cases. |
| Padded row and factor length | proved | Exact upper accounting; redundant coincident plateaus remain within it. |
| `D=2m-1` all-nonzero corollary | proved | Append the full point; zero requires retaining/prepending zero if demanded. |
| Peak-atom lower bound | proved | Full fans `r>=2`; truncated application directly covers `D>=2`. |
| Literal full fixed-delay architecture costs `Omega(m^3)` | proved in stated architecture | Uses canonical lower witnesses and disjoint peak regions. |
| Equal-box band theorem implies full equal-box surface bound | not proved | Literal tails are too large. |
| Equal-box theorem implies fixed-grid aggregation | not proved | Aggregation needs complete generally unequal boxes. |
| Constant-one Boolean upper bound follows | false | Explicitly outside the theorem's scope. |

