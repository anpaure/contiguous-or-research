# Variable-base endpoint annuli and the sharp one-reset pull hinge

**Date:** 2026-08-07  
**Method:** arbitrary-base overlap, endpoint-interval deadlines, and an
explicit periodic core-restoration ring  
**Status:** theorem, independently audited.  This gives a literal
positive-density endpoint interface compatible with fixed additive length,
and identifies its rank profile with the owner-once lift of the corrected
fractional pull-clock packet types.  It does not round the fractional packet
factor to one global owner-once chronology.

## 1. Setup

Let the selected owner rank be `m`, let the lower deadline be `d`, and let a
word have length

\[
                         N=W+d+C,
\]

where `C` is fixed.  Put

\[
                         L=d+C+1.
\]

The architecture-free endpoint-interval lemma says that every `L`-letter
interval contains a selected rank-`m` witness interval.  In particular, its
union has rank at least `m`.

For integers `s,h` with `1<=h<=d`, call `i` an **`(s,h)` endpoint** when

\[
 \left|A_{i-q+1}\cup\cdots\cup A_i\right|=s+q-1
 \qquad(1\le q\le h).                                  \tag{1.1}
\]

Write `E_(s,h)` for the set of these endpoints.  Unlike the earlier full
endpoint theorem, the base rank `s` is arbitrary.

## 2. The arbitrary-base forbidden annulus

### Lemma 2.1 (overlap)

If `i,i+g in E_(s,h)` and `1<=g<=h-1`, then the complete `(h+g)`-letter
span of their two depth-`h` suffixes has rank at most

\[
                         s+h+g-1.                         \tag{2.1}
\]

#### Proof

Let `X,Y` be the two depth-`h` suffix unions.  Their common source segment is
the depth-`(h-g)` suffix at `i`, so (1.1) gives

\[
 |X|=|Y|=s+h-1,
 \qquad |X\cap Y|\ge s+h-g-1.
\]

Hence

\[
 |X\cup Y|\le 2(s+h-1)-(s+h-g-1)=s+h+g-1.
\]

This is the union of the complete source span. \(\square\)

Put

\[
 a=L-h=d+C+1-h,
 \qquad
 b=\min\{h-1,m-s-h\}.                                  \tag{2.2}
\]

### Theorem 2.2 (arbitrary-base annulus and density)

If `b>=a`, then:

1. no two members of `E_(s,h)` have separation `g` with

   \[
                              a\le g\le b;               \tag{2.3}
   \]

2. their total number satisfies

   \[
   \boxed{
   |E_{s,h}|\le
   a\left(1+\left\lfloor{N-1\over b+1}\right\rfloor\right).}
                                                                  \tag{2.4}
   \]

#### Proof

For (2.3), the two-suffix span has length `h+g>=h+a=L`, so it
contains an `L`-letter interval.  Lemma 2.1 bounds the rank of even the
whole span by

\[
                         s+h+g-1\le s+h+b-1<m,
\]

contradicting the endpoint-interval lemma.

For (2.4), greedily take the least remaining endpoint `x` and put every
endpoint in `[x,x+a-1]` into its cluster.  A cluster has at most `a`
positions.  The next cluster anchor `y` obeys `y-x>=a`; (2.3) therefore
forces `y-x>=b+1`.  There are at most
`1+floor((N-1)/(b+1))` anchors. \(\square\)

### Corollary 2.3 (scale-free form)

Suppose `C=O(1)`, `d->infinity`, and along a subsequence

\[
 {h\over d}\longrightarrow\alpha,
 \qquad
 {m-s\over d}\longrightarrow\beta.
\]

If `alpha>1/2`, `beta>=1`, and the limiting annulus is nonempty, then

\[
 \limsup {|E_{s,h}|\over W}
 \le
 {1-\alpha\over\min\{\alpha,\beta-\alpha\}}.           \tag{2.5}
\]

Indeed, `a/d -> 1-alpha`, `b/d -> min(alpha,beta-alpha)`, and
`N/W -> 1`.  Two boundaries are especially informative.

* For the old base `s=m-2d`, so `beta=2`, equation (2.5) is

  \[
  \limsup {|E_{s,h}|\over W}\le {1-\alpha\over\alpha}.
                                                                  \tag{2.6}
  \]

* For the high base `s=m-d+O(1)`, so `beta=1`, the right side is `1`.
  The overlap theorem gives no density loss.  Thus moving the continuation
  to the high base is exactly the first scale at which the annulus becomes
  harmless.

## 3. Every low endpoint exports a rank-restoration debt

### Lemma 3.1 (guard budget)

Let `i` be an `(s,h)` endpoint and let `J` be any containing `L`-letter
interval.  If `G` is the union of the letters of `J` outside the depth-`h`
suffix, then

\[
 \boxed{
 |G\setminus Z_{i,h}|\ge m-(s+h-1).}                    \tag{3.1}
\]

#### Proof

The endpoint-interval lemma gives `|union J|>=m`, while
`|Z_(i,h)|=s+h-1`.  The difference can only be supplied by coordinates in
`G\setminus Z_(i,h)`. \(\square\)

For `s=m-d-delta`, the debt in (3.1) is

\[
                         d+\delta-h.                     \tag{3.2}
\]

Thus a positive-density low-base interface cannot be repaired by a bounded
tag.  It needs a growing, but potentially reusable, rank-restoring guard.

### Lemma 3.2 (age-excess conservation)

Let a rank-`m`, depth-`D=d+1` owner have age composition
`(c_0,...,c_d)`.  Suppose its first `h` proper suffixes form a saturated
base-`s` rail, and suppose every remaining suffix extension is also strict.
Write

\[
                         \delta=m-d-s.                  \tag{3.3}
\]

Then

\[
 c_0=s,
 \qquad c_1=\cdots=c_{h-1}=1,
 \qquad
 \boxed{\sum_{q=h}^{d}(c_q-1)=\delta.}                 \tag{3.4}
\]

In particular, the continuation must carry total rank-jump excess
`delta`.  The unique continuation with one jump at the earliest possible
age is

\[
                         c_h=\delta+1,
 \qquad                  c_q=1\quad(q>h).              \tag{3.5}
\]

#### Proof

Suffix ranks are the partial sums of the age composition.  Saturation
through depth `h` gives the first two assertions in (3.4).  Strictness of
every later extension gives `c_q>=1`.  Subtracting the mandatory one from
each of the `d` nonzero-age classes and using
`sum_(q=0)^d c_q=m` gives

\[
 \sum_{q=h}^{d}(c_q-1)=m-s-d=\delta.
\]

Concentrating this entire excess at age `h` is the unique one-jump
continuation with the earliest reset. \(\square\)

Thus the growing guard in Lemma 3.1 is not an artefact of the overlap
proof.  It is the conserved excess mass in every strict literal age
continuation.  The construction below realizes the extremal composition
(3.5) and then recycles it.

## 4. A sharp one-reset hinge ring

The guard debt above can be paid with equality and recycled periodically.

Put

\[
                         D=d+1,
 \qquad                  c=m-D=m-d-1.
\]

Choose integers

\[
 1\le\delta\le c,
 \qquad 1\le j\le d-1.                                 \tag{4.1}
\]

Let `C_0` be a core of size `c`, let `H subset C_0` have size `delta`, and
choose a cyclic private-label set

\[
 F=(f_0,\ldots,f_{ell-1})
\]

where `ell` is a multiple of `j+1` and `ell>=D+2`.  On the cyclic phase
set, repeat the pattern

\[
 \underbrace{\mathsf L,\ldots,\mathsf L}_{j\text{ times}},
 \mathsf H.                                             \tag{4.2}
\]

At phase `t`, use the source letter

\[
 A_t=
 \begin{cases}
 (C_0\setminus H)\cup\{f_t\},&\mathsf L,\\
 C_0\cup\{f_t\},&\mathsf H.
 \end{cases}                                            \tag{4.3}
\]

One may take

\[
 \ell=(j+1)\left\lceil{D+2\over j+1}\right\rceil.
                                                                  \tag{4.4}
\]

For the middle-layer applications, the required labels fit for all
sufficiently large parameters because `ell<=D+j+2<=2D+1=o(m)`.

### Theorem 4.1 (sharp pull hinge)

The ring (4.2)--(4.3) has all of the following properties.

1. Every `D`-letter union is a rank-`m` owner:

   \[
   O_t=C_0\cup\{f_{t-D+1},\ldots,f_t\}.                 \tag{4.5}
   \]

   The owners are distinct and form a simple Johnson cycle.  Their
   immediate lower and upper colours are also separately distinct.

2. Let `a_t` be the number of consecutive low phases ending at `t`, with
   `a_t=0` at a high phase.  For every `1<=q<=d`,

   \[
   |Z_{t,q}|=
   \begin{cases}
   c-\delta+q,&q\le a_t,\\
   c+q,&q>a_t.
   \end{cases}                                          \tag{4.6}
   \]

   Thus every endpoint has a low saturated rail followed by one
   rank-restoring jump and then a high saturated rail.  All `d` proper
   suffix unions are strict and have rank below `m`.

3. With

   \[
                            s_\delta=c-\delta+1=m-d-\delta,
                                                                  \tag{4.7}
   \]

   the density of `(s_delta,h)` endpoints is exactly

   \[
   \boxed{
   {j-h+1\over j+1}}
   \qquad(1\le h\le j).                                \tag{4.8}
   \]

4. The rank-restoration debt is paid with equality.  Extending an
   `(s_delta,h)` low suffix backwards to its containing `D`-window adds

   \[
                   (D-h)+\delta=m-(s_\delta+h-1)         \tag{4.9}
   \]

   fresh coordinates: `D-h` new private labels and the `delta` restored
   core coordinates.

#### Proof

Since `j<=d-1=D-2`, every `d`-letter, and hence every `D`-letter, interval
contains a high phase.  Every `D`-interval therefore contains all of
`C_0` and exactly `D` consecutive private labels, proving (4.5).  Because
`D+1<ell`, cyclic private intervals of lengths `D-1,D,D+1` recover their
start phase.  This proves owner simplicity and both immediate palettes.

If `q<=a_t`, the suffix lies wholly in the current low run, so its union is
`C_0\setminus H` plus `q` private labels.  If `q>a_t`, it crosses the
preceding high phase, restoring all of `C_0`.  This proves (4.6).  A newly
extended suffix always acquires a fresh private label, so all inclusions are
strict.

In each period of length `j+1`, precisely the low positions of ages
`h,h+1,...,j` satisfy (1.1) with base (4.7), giving (4.8).  Finally, the
containing `D`-window has the `D-h` private labels outside the suffix and
restores exactly `H`, proving (4.9). \(\square\)

Every interval of length `D+C` contains a rank-`m` `D`-window, so this
literal ring satisfies the deadline condition for every fixed `C>=0`.

### Corollary 4.2 (single-bulge age normal form)

At a low endpoint of age `a`, the literal age composition of its rank-`m`
owner is

\[
 \boxed{
 (c-\delta+1,
   \underbrace{1,\ldots,1}_{a-1},
   \delta+1,
   \underbrace{1,\ldots,1}_{d-a}).}                    \tag{4.10}
\]

At a high endpoint it is the all-high composition

\[
                         (c+1,1,\ldots,1).              \tag{4.11}
\]

Thus the one-reset hinge is exactly a single age bulge of mass `delta`
moving from age `1` through age `j` and then returning to age zero.  In
particular, it is a literal directed cycle in the age-composition graph,
not merely a rank-vector realization.

#### Proof

The current private label has age zero, and the other `d` private labels in
the owner have ages `1,...,d`.  Every coordinate of `C_0\setminus H` occurs
in the current letter and has age zero.  During a low run of current age
`a`, the coordinates of `H` last occurred in the high letter `a` phases
earlier, so they augment age class `a` by `delta`.  This gives (4.10).
At a high phase all of `C_0` returns to age zero, giving (4.11).  Consecutive
compositions are realized by the literal source letters (4.3), so they form
the claimed directed age cycle. \(\square\)

## 5. Sharp density inside the one-reset class

The density in (4.8) is optimal among fixed-core low/high reset words that
retain the exact immediate-lower row.

### Proposition 5.1

Consider any cyclic binary low/high schedule with the letters (4.3), and
assume every `d`-letter interval contains a high phase.  Then, for every
`h<=d-1`, the density of positions whose last `h` phases are all low is at
most

\[
                         \boxed{{d-h\over d}}.            \tag{5.1}
\]

Equality is attained by the periodic schedule
`low^(d-1) high`.

#### Proof

Every low run has length `ell_r<=d-1`.  Assign to it the following high
phase.  The run contributes `(ell_r-h+1)_+` qualifying endpoints in
`ell_r+1` assigned phases.  The ratio

\[
 {\ell_r-h+1\over\ell_r+1}=1-{h\over\ell_r+1}
\]

is increasing in `ell_r` and is at most `(d-h)/d`.  Extra consecutive high
phases contribute no qualifying endpoint and can only lower the global
ratio.  The displayed periodic schedule attains equality. \(\square\)

In particular, given a desired constant endpoint density `eta in (0,1)`,
take

\[
 \delta=d,
 \qquad j=d-1,
 \qquad h=d-\lceil\eta d\rceil.                         \tag{5.2}
\]

For all sufficiently large `m`, this is legal and gives base
`s_delta=m-2d` and density

\[
                         \eta+O(1/d).                    \tag{5.3}
\]

The earlier partial-endpoint theorem requires a puncture of order
`eta d`; (5.2) shows that such a linear puncture is sufficient, up to the
sharp rounding term, once the omitted top depths are continued on the high
rail rather than discarded.  For small `eta`, its density differs from the
unrestricted annulus upper bound `eta/(1-eta)` only by the factor
`1-eta`.

## 6. Exact relation to the corrected pull clock

At the stationary rank-profile level, a corrected pull-clock atom of type
`(delta,j)` has exactly the low/high profile of the ring in Section 4.  The
stationary atom itself uses `d+1` cyclic labels and repeats one owner; it is
therefore not literally the same owner chronology.  The separate symmetric
fractional **pull-ring** factor lifts that atom to the owner-once ring of
Section 4 by taking `ell>=D+2`.  Thus the rank profile and mixture weights
below agree exactly, while one-copy global owner chronology remains a
separate rounding gate.  If `x_(delta,j)` are the nonnegative corrected
pull-clock coefficients, the lifted ring's convex packet weight is

\[
                         p_{\delta,j}=(j+1)x_{\delta,j}.
                                                                  \tag{6.1}
\]

Consequently, the aggregate density of `(s_delta,h)` low endpoints in the
fractional packet factor is exactly

\[
 \boxed{
 \mu_{\delta,h}
   =\sum_{j\ge h}p_{\delta,j}{j-h+1\over j+1}
   =\sum_{j\ge h}(j-h+1)x_{\delta,j}.}                  \tag{6.2}
\]

For odd middle-layer parameters the corrected packet factor has
`x_(delta,d)=0`, so every term in (6.2) also retains the exact
immediate-lower row used in Proposition 5.1.

Equation (4.6) explains why the fractional age/pull-clock marginals evade
the fixed-additive density no-go.  They do not place a positive density of
full depth-`d`, base-`m-2d` endpoints.  They decompose each source endpoint
into:

* a variable-length low-base rail;
* one reusable core-restoration jump; and
* a high-base continuation carrying all remaining proper suffix depths.

No short-window capacity is thrown away.  The pull-clock staircase identity
is exactly the rank-marginal ledger of this mixture of sharp hinge profiles.

### Proposition 6.1 (the actual pull-clock factor has linear-depth hinge mass)

For odd middle-layer parameters, put

\[
 p_*:=2\Phi\!\left(-\sqrt{\pi/2}\right)>0,              \tag{6.3}
\]

where `Phi` is the standard normal distribution function.  In the symmetric
fractional pull-ring packet factor, for every fixed `0<alpha<p_*`, a fraction
at least

\[
                         {p_*-\alpha\over1-\alpha}-o(1) \tag{6.4}
\]

of all owner endpoints are `(s_delta,floor(alpha d))` endpoints for some
`delta>=alpha d`.  Thus the correct pull-clock marginals themselves, not
merely an arbitrarily chosen pure packet, contain a positive density of
linear-depth variable-base hinges.

#### Proof

Let

\[
 P=\sum_{s=1}^{c}q_s.
\]

The Ferrers boundary changes this sum by only `O(d^2/W)=o(1)`.  For
`k=2m-1`, the de Moivre--Laplace theorem and the central-binomial estimate
give

\[
 \sum_{s\le m-d-1}{\binom{k}{s}\over2^k}
   \longrightarrow \Phi\!\left(-\sqrt{\pi/2}\right),
 \qquad
 Wd\sim {2^k\over2}.
\]

Here we used `d~sqrt(pi k/8)`.  Consequently

\[
                         {P\over d}\longrightarrow p_* . \tag{6.5}
\]

Choose a random owner endpoint according to the normalized fractional
packet factor, and let `Y` be the number of its proper suffixes whose rank is
at most `c`.  The pull-clock staircase rows supply the low-rank demand, so

\[
                         \mathbb E Y\ge P.              \tag{6.6}
\]

(In the unthinned low rows there is equality; the weaker inequality is all
that is needed.)  Always `0<=Y<=d`.  Hence

\[
 {\mathbb E Y\over d}
 \le \alpha+(1-\alpha)
       \Pr\{Y\ge\alpha d\}.                            \tag{6.7}
\]

Equations (6.5)--(6.7) imply (6.4).

For a pure `(delta,j)` hinge endpoint of low age `a`, equation (4.6) shows
exactly

\[
                         Y=\min\{a,\delta\}.            \tag{6.8}
\]

Thus `Y>=alpha d` forces both `a>=alpha d` and `delta>=alpha d`, which is
precisely the asserted variable-base endpoint property. \(\square\)

For example, taking `alpha=p_*/2` gives a limiting endpoint density at
least

\[
                         {p_*\over2-p_*}>0.              \tag{6.9}
\]

This statement deliberately allows the base rank to vary with `delta`.
Requiring one fixed base rank would select one lattice slice of the
pull-clock mixture and need not retain positive mass.

## 7. Proof-safe consequence and remaining gate

The weakest currently explicit positive-density endpoint interface is
therefore a **one-reset hinge**, not a truncated low rail by itself.  It is
literal, deadline-safe, owner-simple inside each packet, doubly rainbow at
the immediate level, and realizes the already-proved fractional lower-rank
marginals.

This does not prove `nu(k)<=B(k)+O(1)`.  The surviving integral problem is
now sharply separated:

1. select one hinge packet occurrence for each named owner/target without
   collisions;
2. fuse the selected packet cycles into one chronology; and
3. preserve the complete upper deck and terminal compiler while doing so.

The fixed-additive obstruction no longer applies to the local hinge
profiles themselves; it applies only to any attempted rounding that turns a
positive density of them back into unreset full deep endpoints.
