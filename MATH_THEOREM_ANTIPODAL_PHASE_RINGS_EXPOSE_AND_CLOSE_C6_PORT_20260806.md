# Three antipodal phase rings expose and close the Boolean C6 port

## Status

The abstract three-way splice in
`MATH_THEOREM_BOOLEAN_C6_THREE_WAY_ZERO_CHARGE_SPLICE_20260806.md`
has an explicit realization inside the phase-adaptive antipodal vortex
packet family.  Three period-`2h` common-core rings are made identical on
their `h-1` left and right cumulative profiles except for the cyclic active
labels.  Two remote labels private to each ring distinguish every owner,
immediate-lower root, and immediate-upper colour outside the port.

The Boolean `C6` splice fuses the three rings into one period-`6h` literal
component.  It remains flat in the required owner or root phase, preserves
the immediate-lower palette and the displayed OR tensor, and is
automatically biresident.  No source position is added.  All but six
immediate-upper occurrences are also transported; the two extreme
length-`h+1` crossings at each cut lie one letter beyond the displayed
collars and require retained backup witnesses or a longer tensor.

This closes the **literal local planting** of one phase-adaptive C6 port.
It does not decompose the full balanced slice into such rings.  The tagged
thinning below makes all compiler-width source values distinct except
three explicitly forced active-singleton repeats; those three cells must be
left unassigned, reassigned by the global compiler, or paid from available
scalar slack.

## 1. Three ported antipodal rings

Let `h>=3`, let the moving ground set `R` have size `2q-1`, and assume

\[
                              h\le q-1.                   \tag{1.1}
\]

Choose a common core `K` of size `q-h`, three active labels

\[
                              a_0,a_1,a_2,                \tag{1.2}
\]

common collar labels

\[
 \lambda_1,\ldots,\lambda_{h-2},\qquad
 \rho_1,\ldots,\rho_{h-2},                              \tag{1.3}
\]

and, for each `t in Z/3Z`, two ring-private remote labels `x_t,y_t`.
Require all displayed labels and `K` to be pairwise disjoint.  Their total
size is

\[
 (q-h)+3+2(h-2)+6=q+h+5.                                \tag{1.4}
\]

Thus this literal private-label version fits whenever

\[
                              h\le q-6.                   \tag{1.5}
\]

which holds eventually for the critical-vortex deadline
`h=Theta(sqrt(q))`.  (For smaller margins some remote labels may be reused
after a separate collision audit; no such reuse is needed here.)

First define the cyclic marker order in ring `t` by

\[
                              (f_s^{(t)})_{s\in\mathbb Z/(2h)},         \tag{1.6}
\]

where the cyclic private-label order is

\[
 \begin{array}{c|cccccc}
 s&0&1,\ldots,h-2&h-1&h&h+1,\ldots,2h-2&2h-1\\ \hline
f_s^{(t)}
   &a_{t+1}&\rho_1,\ldots,\rho_{h-2}&x_t&y_t&
    \lambda_{h-2},\ldots,\lambda_1&a_t.
 \end{array}                                             \tag{1.7}
\]

For the basic ring one may take `C_s^(t)=K+f_s^(t)`.  We will use the
sharper tagged thinning below.  Let

\[
 \mathcal F=\{2h-1,0,h-1,h\}                            \tag{1.8}
\]

be the two active and two remote phases.  For every `t` and every
`s notin mathcal F`, choose a distinct tag `g_(t,s) in K`, with all these
tags distinct, and put

\[
 C_s^{(t)}=
 \begin{cases}
 K\cup\{f_s^{(t)}\},&s\in\mathcal F,\\
 \{g_{t,s},f_s^{(t)}\},&s\notin\mathcal F.
 \end{cases}                                             \tag{1.9}
\]

This requires only

\[
                        |K|=q-h\ge 3(2h-4)=6h-12,        \tag{1.10}
\]

which again holds eventually.  Every length-`h` cyclic interval meets
either the active full-core pair or the remote full-core pair.  Therefore
the tags do not change any owner: its union is still `K` plus the `h`
markers in that interval.

Open every ring immediately before phase zero.  Its cumulative right and
left collars are

\[
 \begin{aligned}
 R_j^{(t)}&=K\cup\{a_{t+1},\rho_1,\ldots,\rho_{j-1}\},\\
 L_i^{(t)}&=K\cup\{a_t,\lambda_1,\ldots,\lambda_{i-1}\},
 \end{aligned}
 \qquad 1\le i,j\le h-1.                                \tag{1.11}
\]

Hence (1.8) is exactly the cyclic three-label tensor, with

\[
 \Lambda_i=K\cup\{\lambda_1,\ldots,\lambda_{i-1}\},
 \qquad
 P_j=K\cup\{\rho_1,\ldots,\rho_{j-1}\}.                \tag{1.12}
\]

Each ring separately has the same owner row as the common-core antipodal
ring: every length-`h` window is a rank-`q` owner, and every noncore marker
coordinate has owner run and gap exactly `h`.  Core coordinates are present
in every owner because every owner window meets a full-core phase.

## 2. Cross-ring resource disjointness

### Theorem 2.1 (three disjoint immediate-palette packets)

Across the three rings, all length-`h` owner values are pairwise distinct.
The same is true of all length-`h-1` immediate-lower values and all
length-`h+1` immediate-upper values.

#### Proof

Call phases `2h-1,0` the adjacent **active pair**, and phases `h-1,h` the
adjacent **remote pair**.

A cyclic interval of length `h` which meets the remote pair contains a
ring-private label `x_t` or `y_t`, so it cannot equal an interval value in
another ring.  If it avoids the remote pair, it lies in the complementary
arc of length `2h-2`; every length-`h` subinterval of that arc contains
both active phases.  Its active-label set is therefore
`{a_t,a_(t+1)}`, and these three pairs are distinct.  This proves the owner
claim.

The same argument applies at width `h+1`: an interval avoiding the remote
pair necessarily contains both active phases.  At width `h-1`, an interval
avoiding the remote pair either contains both active phases, or is one of
the two extreme subintervals containing exactly one active phase.  In the
first case the active pair distinguishes the ring.  The two extreme cases
are respectively

\[
 K\cup\{\lambda_1,\ldots,\lambda_{h-2},a_t\},
 \qquad
 K\cup\{a_{t+1},\rho_1,\ldots,\rho_{h-2}\}.             \tag{2.1}
\]

Within one side the active label distinguishes `t`, while opposite sides
are distinct because the lambda and rho banks are disjoint.  Thus the
lower row is also cross-ring disjoint.  \(\square\)

Within each individual ring, simplicity of all three rows follows from
the distinct-private-label cyclic-interval argument.  Theorem 2.1 therefore
gives `6h` distinct resources in each immediate row before splicing.

## 3. Literal C6 closure

Reconnect the left side of ring `t` to the right side of ring `t+1`.

### Theorem 3.1 (one zero-charge phase component)

The reconnected word is one cyclic source component of length `6h`.  For
every crossing address `1<=i,j<=h-1`, its new value is an old value with
the exact ticket transport `t->t+1`.  Consequently:

1. all length-`h` owners remain the same `6h` distinct rank-`q` values;
2. all length-`h-1` roots remain the same distinct values;
3. every displayed shorter or longer local ticket is transported by the
   same cyclic occurrence bijection; and
4. among the length-`h+1` immediate-upper occurrences, every crossing
   split with `2<=i,j<=h-1` is transported; only the extreme splits
   `(i,j)=(1,h)` and `(h,1)` at each of the three cuts are outside the
   tensor, for a total of six unprotected occurrences; and
5. no source position is inserted or deleted.

If the intrinsic child deadline is `e` and

\[
                        h=e+\epsilon+1,qquad
                        \epsilon\in\{0,1\},              \tag{3.1}
\]

then the fused word is phase-correct:

* for `epsilon=0`, its depth-`e` row is the owner row;
* for `epsilon=1`, its depth-`e` row is the rank-`(q-1)` root row and one
  further derivative is the owner row.

#### Proof

Equations (1.8)--(1.9) satisfy the hypotheses of the Boolean-C6
three-way tensor theorem, so every crossing occurrence and ticket is
cyclically transported.  Noncrossing intervals stay in an old ring and
are unchanged.  The reconnection acts on the three old components by the
three-cycle `t->t+1`, hence produces one component.  The resource claims
follow from Theorem 2.1 and tensor preservation.

Every source interval of width `h` has rank `q` after the splice: this is
old away from a seam and follows from the crossing rank formula at a seam.
Likewise every width-`h-1` interval has rank `q-1`.  Since a depth-`e` row
uses width `e+1`, (3.1) gives the two phase assertions.  \(\square\)

### Theorem 3.2 (automatic biresidence after fusion)

The fused owner component is biresident at ambient deadline `h-1`.

#### Proof

Core coordinates are constantly present.  A remote label occurs once and
every common lambda or rho label occurs once in each of the three old
rings.  In the fused cyclic order, successive source occurrences of such a
repeated label are exactly `2h` positions apart.  Each therefore creates
an owner run of length `h` followed by a zero gap of length `h`.

Each active label occurs at one active phase in each of two old rings and
nowhere else.  Under the component order `t->t+1`, its two occurrences are
separated in both cyclic directions by at least `2h`.  Its owner runs and
gaps therefore also have length at least `h`.  Unused coordinates are
constantly absent.  This is precisely biresidence at deadline `h-1`.
\(\square\)

## 4. The tagged thinning leaves exactly three proper-width repeats

### Theorem 4.1 (near-one-copy proper source deck)

Across all three tagged rings, every cyclic source-interval value of width
`1<=ell<2h` is unique except

\[
                              K\cup\{a_0\},
                              K\cup\{a_1\},
                              K\cup\{a_2\}.              \tag{4.1}
\]

Each value in (4.1) occurs exactly twice, once at a left active phase and
once at a right active phase.  Thus the complete proper-width source deck
has exactly three excess occurrences beyond one-copy simplicity.

#### Proof

Consider first an interval containing no full-core phase.  Every one of its
source positions carries a tag `g_(t,s)` unique in the entire three-ring
bank.  The set of tags in its union therefore recovers the ring and the
exact cyclic interval.  Since the interval has width below `2h`, it omits
many coordinates of `K` under (1.10), so its value cannot equal a value
from an interval containing a full-core phase.

An interval containing a remote phase contains the ring-private marker
`x_t` or `y_t`, and its remaining distinct cyclic markers recover its
interval.  It cannot collide with another ring.

It remains to consider intervals containing an active full-core phase but
no remote phase.  Their value is `K` plus their marker set.  Within one
ring the markers are distinct, so a proper cyclic marker interval is
recovered from its set.  Across rings, an interval containing both active
phases has the ring-distinguishing active pair `{a_t,a_(t+1)}`.  An
interval containing exactly one active phase extends only into the lambda
side or only into the rho side; these banks are disjoint and their prefix
records the side and length.  The sole case with no lambda or rho marker is
the active singleton itself.  Label `a_s` occurs at the left active phase
of ring `s` and the right active phase of ring `s-1`, giving exactly the two
copies of `K+{a_s}` in (4.1).  No other occurrence uses an active marker.
\(\square\)

For the compiler-relevant widths `1<=ell<=h-1`, every crossing split lies
inside the displayed collars.  The C6 splice therefore only permutes those
values, and Theorem 4.1 continues to describe their multiplicities after
fusion.  Longer proper intervals with an extreme split can leave the
displayed tensor; no post-fusion one-copy claim is made for them.

## 5. Named lower cells and exact scope

The construction is exact on owners, the immediate-lower palette, literal
phase, state balance, the displayed local OR tickets, topology, and
residence.  Its immediate-upper row has an explicit six-occurrence seam
exposure which must be backed up or extended.  It is also not an exact
one-copy factor for all proper source widths: Theorem 4.1 leaves the three
forced active-singleton repeats.  Thus one port has constant, not
`O(h^2)`, source-deck excess.  A loose tree with `O(W/h)` ports has only
`O(W/h)` such excess occurrences, below the full `Theta(W)` scalar block
created by one extra physical position.  This makes the port compatible at
the counting level with a `B(k)+1` programme, but it does not by counting
alone prove the required incidence-level compiler matching or exact
`B(k)`.

The remaining all-dimensional theorem is now global:

> plant a compatible family of the three-ring C6 components inside the
> phase-appropriate integral balanced-vortex/exterior cover-down; route or
> quarantine their three repeated lower cells per port; retain backups for the
> six extreme q1-upper seam occurrences; and retain arbitrary-width upper
> witnesses away from the three cuts.

No local owner, root, phase, topology, residence, or source-state
obstruction remains for that planting problem.  Upper-q1 has been reduced
to six explicitly located boundary occurrences rather than silently
claimed closed.

## 6. A fixed port bank is unconditionally plantable at owner/q1 level

One antipodal ring has `2h` owner transitions and therefore `4h`
incidence edges in the adjacent-rank middle-levels graph.  One three-ring
port has `12h` incidence edges before its zero-charge fusion.

### Corollary 6.1 (fixed-number protected planting)

For every fixed `H`, all sufficiently large `q` admit `H` pairwise
resource-disjoint copies of the three-ring port inside one spanning simple
owner/lower-q1 two-factor, provided

\[
                              12Hh\le q-2.                \tag{6.1}
\]

After the factor is chosen, applying each port's C6 splice turns its three
protected cycles into one without changing any owner or lower-q1 resource.

#### Proof

For fixed `H`, take independent uniform coordinate images of the `H`
abstract ports.  Each port has `O(h)` owner/root resources, and any fixed
central resource in one image is uniform on its shore.  A union bound over
the `O(H^2h^2)` cross-port role pairs has collision probability

\[
                  O(H^2h^2/W_q)=o(1).
\]

Hence images with pairwise disjoint owner/root resources exist.  Their
incidence cycles have
maximum degree two, and together use `12Hh` edges.  The small protected
middle-levels factor theorem extends every maximum-degree-two protected
subgraph with at most `q-2` incidence edges to a spanning simple
two-factor.  Apply it using (6.1), then invoke Theorem 3.1 independently on
the disjoint ports.  \(\square\)

This corollary is deliberately only an owner/lower-q1 statement.  The six
upper seam backups, repeated proper-width cells, terminal compiler, and a
growing loose connector tree remain outside its scope.  In particular it
does not supply the `Theta(number of factor cycles)` ports needed for the
global loose-tree compression theorem.

## 7. Why the two extreme upper cells do not extend in this ring class

One may try to add one more lambda and rho phase, extending the common C6
profiles from `i,j<=h-1` to `i,j<=h`.  On a period-`2h` antipodal ring this
uses the entire left and right halves and removes the two remote private
phases.  If all far labels are common and the active labels occur only at
the main cut, an opposite-cut owner window avoids the active pair and is
identical in all three rings.  Thus resource disjointness fails.

The natural repair is to put a ring-private token `x_t` in the last right
phase (and similarly a private left token).  The following exact calculation
shows why that repair destroys the extreme upper tensor.

### Proposition 7.1 (private-tail obstruction)

Suppose the old extreme right upper occurrence in ring `t` has, after a
common background is suppressed, the label set

\[
                         \{a_t,a_{t+1},x_t\},             \tag{7.1}
\]

where `x_0,x_1,x_2` are pairwise distinct and occur in no other displayed
role.  Under the C6 reconnection `left(t)->right(t+1)`, the corresponding
new set is

\[
                         \{a_t,a_{t+2},x_{t+1}\}.         \tag{7.2}
\]

The three old sets (7.1) and three new sets (7.2) do not have the same
multiset.  The analogous statement holds at the extreme left upper cell.

#### Proof

If the multisets were equal, the unique token `x_(t+1)` in (7.2) would
force that set to equal the old set with index `t+1`.  Removing the common
token would then give

\[
              \{a_t,a_{t+2}\}=\{a_{t+1},a_{t+2}\},
\]

contrary to distinctness of the three active labels.  \(\square\)

Therefore a full `h`-collar extension is invalid in the natural
common-profile antipodal class: without private far tokens it repeats
opposite-cut central resources, while private far tokens violate the two
extreme width-`h+1` tensor identities.  A more elaborate multi-label trade
could evade Proposition 7.1, but is not supplied by the phase-adaptive ring.
Within the present exact construction, six named upper backups (two per
cut, across three cuts) are the sharp honest interface.
