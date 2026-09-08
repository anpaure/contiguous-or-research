# Flag contraction exposes small codegrees, but preselection destroys the packet degree

## Status

This note gives a proof-safe answer to the flag-contraction question for
the one-step pull-ring packets.  Contracting an occurrence

\[
                 Q\subset O\subset U
\]

to one flag really does remove the visible `2/r` owner--root codegree: in
the shortest upper-rich packet, two consecutive full flags have normalized
codegree exactly `1/((r-1)(r-2))`.

That gain cannot be obtained by first choosing the incidence bijections.
After an owner--root incidence bijection is fixed, a compatible ring is
determined by its initial ordered hole queue.  A period `D+a` packet has at
most `(r-1)_a` continuations through a fixed owner.  If the full
`Q subset O subset U` flag is fixed at every owner, at most
`(r-2)_(a-1)` continuations remain.  For the current `D+2` packets these
bounds are only `(r-1)(r-2)` and `r-2`, respectively, instead of degree
`exp(Theta(D log r))`.

Thus preselecting the incidence factor moves the codegree obstruction into
an exponential loss of degree.  Keeping all flags instead merely moves it
into the owner/root partition-conflict system.  The theorem does not rule
out an incidence factor chosen *jointly* with an exact packet factor; it
rules out the proposed two-stage route "choose flags, then apply a
growing-uniformity nibble".

No computation or search is used.

## 1. Common flag geometry of every pure pull ring

Work on `[2r-1]`.  Put

\[
                 D=d+1,\qquad L=D+a,\qquad a\ge2.          \tag{1.1}
\]

Assume `D<=r` and `a<=r-1`, which are exactly the conditions needed for
the core and the `a` outside holes to fit.  They hold for every packet type
used in the present pull-ring master.

The all-high ring and every pure pull ring in the symmetric fractional
packet factor have the same owner row.  For a core `K` of size `r-D` and a
cyclically ordered private set

\[
                 F=(f_0,\ldots,f_{L-1}),
\]

that row and its two immediate palettes are

\[
 \begin{aligned}
 O_t&=K\cup\{f_t,\ldots,f_{t+D-1}\},\\
 Q_t&=O_t\cap O_{t+1}=O_t-\{f_t\},\\
 U_t&=O_t\cup O_{t+1}=O_t+\{f_{t+D}\}.
 \end{aligned}                                             \tag{1.2}
\]

All indices are modulo `L`.  A direction on the source ring gives the
oriented flag

\[
                         \phi_t=(Q_t,O_t,U_t).              \tag{1.3}
\]

The `a` elements of `F-O_t` are the **hole queue** at time `t`, in the
order

\[
                    (f_{t+D},f_{t+D+1},\ldots,f_{t+L-1}).   \tag{1.4}
\]

At the next step the first hole is inserted, the phase label `f_t` is
deleted, and that deleted label is appended to the queue.

The shortest upper-rich packet of the current ledger is `a=2`, so

\[
                             L=D+2.                          \tag{1.5}
\]

## 2. Exact unsplit and flag degrees

Write `(x)_j=x(x-1)\cdots(x-j+1)`.  Count directions of a ring separately.
The degree of a fixed owner in the oriented period-`D+a` packet orbit is

\[
                   \widehat D_a=(r-1)_a(r)_D.               \tag{2.1}
\]

Indeed, choose and order the `a` holes outside the owner, and choose and
order the `D` private labels inside it.  Reversal identifies the two
directions in the unoriented convention, giving
`D_a=\widehat D_a/2`, in agreement with the existing packet ledger.

Ground-set symmetry and incidence counting now give exact contracted
degrees.

### Proposition 2.1 (contracted one-flag degrees)

For a fixed incident owner--root flag `(Q,O)`,

\[
 \boxed{
 D_{QO}={\widehat D_a\over r}
       =(r-1)_a(r-1)_{D-1}.}                               \tag{2.2}
\]

For a fixed full flag `Q subset O subset U`,

\[
 \boxed{
 D_{QOU}={\widehat D_a\over r(r-1)}
       =(r-2)_{a-1}(r-1)_{D-1}.}                           \tag{2.3}
\]

#### Proof

Every owner has `r` facets and `r-1` cofacets.  An oriented packet uses
exactly one outgoing facet flag and one outgoing full flag at that owner.
The stabilizer of the owner is transitive on its facets and on its ordered
facet--cofacet pairs.  Divide (2.1) by `r` and by `r(r-1)`, respectively.
The falling-factorial forms follow by cancellation.  \(\square\)

For `a=2`, (2.1)--(2.3) become

\[
 \begin{aligned}
 \widehat D_2&=(r-1)(r-2)(r)_D,\\
 D_{QO}&=(r-1)(r-2)(r-1)_{D-1},\\
 D_{QOU}&=(r-2)(r-1)_{D-1}.
 \end{aligned}                                             \tag{2.4}
\]

This agrees with the unoriented degree

\[
 D_0={1\over2}(r-1)(r-2)(r)_D
\]

in the `D+2` ledger.

### Proposition 2.2 (the visible consecutive full-flag codegree)

Let `a=2`, and fix two compatible full flags which occur at consecutive
phases of an oriented packet.  Their common packet degree is

\[
                         (r-2)_{D-2}.                       \tag{2.5}
\]

Consequently their codegree relative to one full-flag degree is exactly

\[
 \boxed{
 { (r-2)_{D-2}\over D_{QOU}}
       ={1\over(r-1)(r-2)}.}                               \tag{2.6}
\]

#### Proof

The first full flag identifies

\[
                   f_0,\qquad f_D,qquad O_0.
\]

The next one identifies `f_1` and the second hole `f_(D+1)`.  The remaining
ordered private labels are `f_2,...,f_(D-1)`, chosen without repetition
from the remaining `r-2` elements of `O_0`; this gives (2.5).  Since

\[
 D_{QOU}=(r-2)(r-1)(r-2)_{D-2},
\]

division gives (2.6).  \(\square\)

Thus full-flag contraction genuinely changes the visible local scale from
`Theta(1/r)` to `Theta(1/r^2)` for the consecutive obstruction.  The next
sections show why that improvement is unavailable after the required
capacity constraints are restored.

### Proposition 2.3 (all full-flag pair codegrees)

For `a=2`, the maximum codegree of two distinct full flags satisfies

\[
 \boxed{
 {\Delta_2^{\rm flag}\over D_{QOU}}
 \le {L-1\over(r-1)(r-2)}
 =O\left({D\over r^2}\right).}                            \tag{2.7}
\]

Consequently the crude aggregate collision mass of one `L`-flag packet is

\[
 {1\over D_{QOU}}
 \sum_{\{\phi,\psi\}\in\binom e2}d(\phi,\psi)
       =O\left({L^3\over r^2}\right)
       =O(r^{-1/2}).                                       \tag{2.8}
\]

#### Proof

Fix a first flag at phase zero.  Its candidates are parameterized by

* the second hole `f_(D+1)` outside `U_0`; and
* the ordered internal tuple `f_1,...,f_(D-1)` inside `Q_0`.

Fix a nonzero phase offset `s`.  A second full flag at phase `s` determines
`f_s=O_s-Q_s` and `f_(s-2)=U_s-O_s`.  It also determines the second hole:
because

\[
 H=U_0\cup\{f_{D+1}\},\qquad U_s=H-\{f_{s-1}\},           \tag{2.9}
\]

and `s` is nonzero, `f_(D+1)` belongs to `U_s-U_0`.  Once this hole is
known, `H` is known and `f_(s-1)=H-U_s` is known as well.  Among the three
consecutive labels `f_(s-2),f_(s-1),f_s`, at least one is an internal
label `f_i` with `1<=i<=D-1`; the only initially known phase labels are
`f_0` and `f_D` (besides the just recovered second hole).  Thus, for this
fixed offset, at most

\[
                            (r-2)_{D-2}                    \tag{2.10}
\]

candidates remain.  Sum over the at most `L-1` nonzero offsets and divide
by

\[
                   D_{QOU}=(r-2)(r-1)(r-2)_{D-2}.
\]

This proves (2.7).  Summing (2.7) over the `binom(L,2)` pairs of a packet
gives (2.8).  \(\square\)

So the fully contracted host really does satisfy a much stronger *internal*
pair-spread ledger.  The obstruction below is not a failure of that count;
it is the cost of selecting one flag from each owner/root capacity class.

## 3. Queue rigidity after an owner--root factor is selected

Let

\[
 \vartheta:{[2r-1]\choose r-1}\longrightarrow
            {[2r-1]\choose r}                              \tag{3.1}
\]

be any incidence bijection: `Q subset vartheta(Q)`.  Write its inverse as

\[
 \sigma:{[2r-1]\choose r}\longrightarrow
        {[2r-1]\choose r-1},\qquad \sigma(O)\subset O,      \tag{3.2}
\]

and define the uniquely prescribed deletion

\[
                         x(O)=O-\sigma(O).                  \tag{3.3}
\]

An oriented ring is `vartheta`-compatible when

\[
                         Q_t=\sigma(O_t)                    \tag{3.4}
\]

at every phase.

### Theorem 3.1 (owner--root queue rigidity)

For every incidence bijection `vartheta` and every starting owner `O`, the
number of `vartheta`-compatible oriented period-`D+a` pull rings through
`O` is at most

\[
 \boxed{(r-1)_a.}                                          \tag{3.5}
\]

If either cyclic direction is admitted in an unoriented packet model, the
bound is at most `2(r-1)_a`.

#### Proof

Choose an ordered `a`-tuple

\[
                         (y_0,\ldots,y_{a-1})               \tag{3.6}
\]

of distinct elements outside `O`.  There are `(r-1)_a` choices.  Starting
with `O_0=O`, recursively put

\[
 \begin{aligned}
 x_t&=x(O_t),\\
 O_{t+1}&=O_t-\{x_t\}\cup\{y_t\},\\
 y_{t+a}&=x_t.
 \end{aligned}                                             \tag{3.7}
\]

The set

\[
                 O_t\cup\{y_t,\ldots,y_{t+a-1}\}           \tag{3.8}
\]

is invariant under (3.7).  Hence (3.7) is exactly the shift of the ordered
hole queue in (1.4).  Every compatible ring starting from `O` must obey
this recursion, because (3.4) forces its leaving label to be `x(O_t)`.
Thus the initial ordered queue determines at most one ring.  Some queues
fail distinctness or cyclic closure, so this is an upper bound.  Reversing
the direction gives at most the factor two stated.  \(\square\)

Comparing (3.5) with (2.2), preselecting the incidence bijection loses the
exact multiplicative factor

\[
 \boxed{(r-1)_{D-1}.}                                      \tag{3.9}
\]

This loss is independent of `a`: the factor being removed is the ordered
interior of the owner window.

## 4. Full-flag preselection is still more rigid

Suppose in addition that every owner is assigned one cofacet

\[
                         \upsilon(O)\supset O,              \tag{4.1}
\]

with no assumption about the multiplicities of the upper targets.  A ring
is full-flag-compatible if (3.4) holds and

\[
                         U_t=\upsilon(O_t)                  \tag{4.2}
\]

at every phase.  This contains as a special case any preselected feasible
`Q subset O subset U` flag table, including one with upper capacities and
marks already priced.

### Theorem 4.1 (full-flag queue rigidity)

For every such full-flag table and every starting owner `O`, the number of
compatible oriented period-`D+a` rings through `O` is at most

\[
 \boxed{(r-2)_{a-1}.}                                      \tag{4.3}
\]

For `D+2` packets this is only

\[
                             r-2.                           \tag{4.4}
\]

#### Proof

Equation (4.2) fixes the first inserted hole:

\[
                    y_0=\upsilon(O)-O.                     \tag{4.5}
\]

Choose and order only the remaining `a-1` holes outside
`O union {y_0}`.  There are `(r-2)_(a-1)` choices.  The recurrence (3.7)
then determines the entire candidate, and later upper flags merely reject
candidates.  \(\square\)

Again the ratio between the full-flag degree (2.3) and (4.3) is exactly
the factor `(r-1)_(D-1)`.

## 5. Quantitative failure of preselect-then-nibble for `D+2`

Specialize to `a=2`, `L=D+2`, with `D=Theta(sqrt r)`.  After an owner--root
factor is fixed, every owner has compatible packet degree at most

\[
                         \Delta_\vartheta\le(r-1)(r-2).     \tag{5.1}
\]

After a full flag table is fixed,

\[
                         \Delta_\phi\le r-2.               \tag{5.2}
\]

Retain every other selected flag independently with density `u`.  For any
fixed starting flag, the expected number of surviving compatible packets
through it is at most

\[
                 \Delta_\vartheta u^{L-1}
       \quad\hbox{or}\quad
                 \Delta_\phi u^{L-1}.                     \tag{5.3}
\]

For every fixed `u<1`, both quantities tend to zero, because
`L=Theta(sqrt r)` while the two degrees are polynomial in `r`.  At the
critical uncontracted cover-down density `u=r^(-1/2)`, they are bounded by

\[
 r^{2-(D+1)/2}
       \quad\hbox{and}\quad
 r^{1-(D+1)/2},                                            \tag{5.4}
\]

respectively, and hence vanish superpolynomially.

Equivalently, their unit-degree thresholds satisfy

\[
 \begin{aligned}
 u_\vartheta^*&\ge((r-1)(r-2))^{-1/(D+1)},\\
 u_\phi^*&\ge(r-2)^{-1/(D+1)}.
 \end{aligned}                                             \tag{5.5}
\]

Both are

\[
                         1-O\left({\log r\over\sqrt r}\right),\tag{5.6}
\]

not `Theta(r^(-1/2))`.  Therefore a standard random-like cover-down cannot
even remove a fixed positive proportion after the incidence factor is
preselected.  This is a degree obstruction, before codegrees or absorption
are considered.

The conclusion is scoped.  A specially correlated incidence factor and
packet factor can exist even when every compatible degree equals one.
What (5.3)--(5.6) rule out is obtaining that object by first freezing the
flags and then invoking a growing-degree nibble or universal sparse
reservoir theorem.

## 6. If flags are not preselected, the old conflict returns exactly

One may instead keep every contracted flag as a vertex and postpone the
choice of one flag per owner and root.  The visible hypergraph then has the
small degree/codegree ledger of Section 2, but a packet matching in that
hypergraph is not enough: two different flags over the same owner or root
still cannot both be used.

This hidden partition conflict has exact multiplicity.  By (2.1)--(2.3),

\[
 {\widehat D_a\over D_{QO}}=r,
 \qquad
 {\widehat D_a\over D_{QOU}}=r(r-1).                       \tag{6.1}
\]

Thus, relative to one exact flag, its owner class contains `r` times as
many packet incidences in the owner--root contraction, and `r(r-1)` times
as many in the full-flag contraction.  For any chosen packet and any one
of its flags, all alternative packets through the same owner are capacity
conflicts even when they are disjoint in the contracted flag hypergraph.

In particular, the raw owner-capacity conflict relation applied after
full-flag contraction has degree at least

\[
                   \widehat D_a-D_{QOU}
       =\bigl(r(r-1)-1\bigr)D_{QOU}                        \tag{6.2}
\]

from just one owner class (some of these conflicts may already be visible
as flag intersections, so this is a ledger for the capacity relation, not
a claim that every term is an additional irredundant conflict).  The
analogous owner--root value is

\[
                   \widehat D_a-D_{QO}=(r-1)D_{QO}.        \tag{6.3}
\]

Hence the apparent `1/r^2` local codegree in (2.6) is not a free
small-codegree host: restoring owner/root capacities produces a
`Theta(r^2)`-normalized conflict neighbourhood.  Adding the owner and root
classes back as ordinary hypergraph vertices gives exactly the original
packet formulation and its `2/r` incident-pair row.

This is a conservation law for the attempted contraction:

\[
 \boxed{
 \text{small visible flag codegree}
 \quad\Longleftrightarrow\quad
 \text{large unresolved partition conflict}.}
                                                               \tag{6.4}
\]

## 7. Consequence for the integral programme

The `D+2` packet cannot be rounded by either of the two flag-first routes:

1. **preselect the incidence factor:** queue rigidity leaves only
   polynomial degree, which dies before a cover-down begins;
2. **retain all flags and use an ordinary matching theorem:** the owner,
   root, and upper partition conflicts have normalized degrees `r` and
   `r(r-1)`.

The viable quantifier must be joint.  A positive theorem has to choose the
incidence flags and the packet rings in the same absorption/design step,
or use a theorem which natively handles the partition capacities rather
than hiding them by contraction.

For a longer period `D+a`, Theorems 3.1 and 4.1 give the exact diagnostic
degrees `(r-1)_a` and `(r-2)_(a-1)`.  Thus only packets with a macroscopic
hole queue `a=Theta(D)` retain exponential degree after owner--root
preselection.  Full-flag preselection remains one power of the queue
shorter.  This points to a possible mixed-length route, but it does not
rescue the shortest `D+2` atom or prove an integral packet factor.

At the precise critical density `u=r^(-1/2)`, these diagnostics sharpen to

\[
 \begin{aligned}
 (r-1)_a u^{D+a-1}
     &\le r^{(a-D+1)/2},\\
 (r-2)_{a-1}u^{D+a-1}
     &\le r^{(a-D-1)/2}.                                  \tag{7.1}
 \end{aligned}
\]

Hence owner--root preselection can retain growing critical-scale degree
only when `a>=D`, up to the endpoint convention.  Full-flag preselection
requires `a>=D+2`.  But every pure packet in the current master has

\[
                         L\le2D+1,\qquad a=L-D\le D+1.      \tag{7.2}
\]

Therefore **no current pure packet type has divergent residual degree at
the critical scale after full-flag preselection**.  This is the sharpest
form of the obstruction: longer mixed packets may leave owner--root
contraction open, but a complete `Q subset O subset U` table still has to
be selected jointly with the packet factor.
