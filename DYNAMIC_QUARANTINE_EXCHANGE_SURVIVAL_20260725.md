# Dynamic quarantine preserves local geodesic exchange cubes

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The independent isolated pruning used in the first protected-strip
construction destroys essentially every prescribed adjacent-swap exchange.
Dynamic quarantine behaves differently.  Its deterministic fibre ledger can
be run with a much smaller depletion threshold than was used previously.
Consequently, outside an `o(W)` physical exceptional ledger, almost every
candidate retains every exchange in a fixed-radius ball of the commuting
adjacent-switch cube.

This is the first proved mechanism which preserves the structural feature
that separates the actual catalogue from the abstract linear matching
counterexamples.  It does **not** yet prove the weighted augmentation
theorem: an arbitrary dual weighting may concentrate on the exceptional
candidates, and no bounded-radius augmentation theorem for the geodesic
support system is currently known.

## 1. Abstract cube erosion lemma

Let `Q_d` be the `d`-dimensional cube and let `R` be a deleted vertex set.
For an integer `r >= 0`, write

\[
 N_r(R)=\{x:d_{Q_d}(x,R)\le r\}.
\]

### Lemma 1.1 (exact ball erosion)

If `|R| <= eta 2^d`, then

\[
 \boxed{
 |N_r(R)|
 \le |R|\sum_{j=0}^r\binom dj
 \le \eta 2^d\sum_{j=0}^r\binom dj .}
 \tag{1.1}
\]

In particular, every vertex outside `N_r(R)` retains its entire cube ball
of radius `r`.

#### Proof

Every member of `N_r(R)` lies in the radius-`r` ball of at least one member
of `R`.  A cube ball has exactly `sum_{j<=r} binom(d,j)` vertices.  The union
bound proves (1.1).  The final assertion is the definition of `N_r(R)`.
\(\square\)

For radius one there is a slightly sharper directed-edge form.

### Lemma 1.2 (boundary form)

For every `theta>0`, the number of vertices outside `R` having more than
`theta d` neighbours in `R` is at most

\[
 \boxed{\frac{\eta}{\theta}2^d.}
 \tag{1.2}
\]

#### Proof

The number of directed cube edges from the complement into `R` is at most
`d|R|`.  Each vertex counted on the left contributes more than `theta d`
such edges.  Divide.  \(\square\)

Both lemmas remain valid for a disjoint union of equal-dimensional cubes:
sum the inequalities over the components.  No lower bound on the density
inside each individual cube is required.

## 2. Dynamic protected-antichain ledger at an arbitrary threshold

Let `A` be the full base-grid degree of every calibrated fibre.  Join two
base grids on distinct tags when their protected strips share an
`s`-element antichain.  Write

\[
 \xi_s=\frac{\Delta_s}{A}.
\]

For fixed `s`, the protected membership-atom census gives

\[
 \boxed{
 \xi_s
 \le m^{o(1)}\frac{gQ}{m^{2(s-1)}}
 =m^{3-2s+o(1)}.}
 \tag{2.1}
\]

Let `S` be any already selected target-disjoint chunk family, with
`|S|<=T=(1+o(1))W/g`, and quarantine every candidate adjacent to a member
of `S`.  Proposition 10.1 of
`MATH_ATTACK_GRID_PRIORITY_NIBBLE_PROPAGATION_AUDIT_20260725.md` gives,
for every threshold `eta>0`,

\[
 \boxed{
 \text{bad tag-fibre weight}\le \frac{W\xi_s}{\eta},
 \qquad
 \text{bad target-fibre weight}\le
 \frac{WK\xi_s}{g\eta}.}
 \tag{2.2}
\]

Since `K/g <= 2Q+1`, both ledgers are `o(W)` whenever

\[
 \boxed{\frac{Q\xi_s}{\eta}=o(1).}
 \tag{2.3}

No probability and no assumption on the history `S` occurs in (2.2).

### Corollary 2.1 (fixed-width numerical choices)

For the three-antichain quarantine,

\[
 \xi_3=m^{-3+o(1)}.
\]

Hence one may take, for example,

\[
 \eta_3=m^{-12/5};
 \tag{2.4}

\]

then `Q xi_3/eta_3=m^{-1/10+o(1)}`.  For the four-antichain
quarantine,

\[
 \xi_4=m^{-5+o(1)},
\]

and one may take

\[
 \eta_4=m^{-4};
 \tag{2.5}

\]

then `Q xi_4/eta_4=m^{-1/2+o(1)}`.  In both cases all fibres except an
`o(W)` physical ledger retain a `(1-eta_s)` fraction of their original
exponential candidate family.

## 3. Application to commuting arrival-switch cubes

Corollary 3.2 of
`MATH_ATTACK_H_DETERMINISTIC_CARRIER_ROTOR_TRAJECTORIES_20260725.md`
provides a full commuting adjacent-switch cube of dimension `Theta(m)`.
Only the switches which change the emitted return-free chunk can support
physical augmentations or pair-square cancellation; after quotienting the
dummy outside switches, these active switches give a cube of dimension

\[
 d_{\rm eff}=\Theta(g)=m^{1/2+o(1)}.
 \tag{3.1}
\]

Every cube edge is a literal two-step arrival diamond.  Its endpoints are
legal simultaneous-rainbow geodesic chunks, and the toggle changes one
intermediate owner together with its complete vertical protected flag
string.

Partition a good fibre into these effective cubes, with irrelevant outside
switches absorbed into the cube index.  If quarantine deletes at most an `eta`
fraction of the whole fibre, Lemma 1.1 shows that the fraction of schedules
whose radius-`r` exchange ball is not completely retained is at most

\[
 \boxed{
 \eta\sum_{j=0}^r\binom {d_{\rm eff}}j
 \le \eta\left(\frac{e d_{\rm eff}}{r}\right)^r
 \quad(1\le r\le d_{\rm eff}).}
 \tag{3.2}

For fixed `r`, both choices (2.4)--(2.5) make (3.2) `o(1)`.  More
quantitatively, under four-antichain quarantine with `eta=m^{-4}` and
`d_eff=m^{1/2+o(1)}`, every fixed radius `r<=7` survives on a `1-o(1)`
fraction of schedules.  Under three-antichain quarantine with
`eta=m^{-12/5}`, the same conclusion holds for every fixed `r<=4`.

The radius-one conclusion is stronger: all but

\[
 (d_{\rm eff}+1)\eta=m^{-7/2+o(1)}
 \tag{3.3}

of the four-antichain schedules retain every adjacent switch.

## 4. A growing antichain threshold preserves growing exchange balls

The same protected census permits a slowly growing `s`.  Uniformly in the
range used below,

\[
 \xi_s
 \le m^{1+o(1)}\left(\frac{Cs}{m}\right)^{2(s-1)}.
 \tag{4.1}

\]

Take

\[
 s=o\!\left(\frac{\log m}{\log\log m}\right),
 \qquad
 \eta_s=m^{-s}.
 \tag{4.2}

\]

Then (2.3) holds with superpolynomial room.  Since
`d_eff=m^{1/2+o(1)}`, (3.2) is `o(1)` uniformly, for example, for every
fixed `epsilon>0` and

\[
 r\le (2-\epsilon)s.
 \tag{4.3}

\]

Moreover, an intersection left by `s`-antichain quarantine has width at
most `s-1`.  The width-`s-1` protected shape expansion at exponential
parameter `w<=C log m` has one-link ratio

\[
 \frac gm(Cw)^{s-1}=m^{-1/2+o(1)},
 \tag{4.4}

\]

under (4.2).  Thus slowly growing exchange radius and the raw shape census
are numerically compatible in the **dynamic** architecture.  This avoids
the fixed-pruning entropy ceiling because no exponential fibre is thinned
in advance.

## 5. Exact limitation

Equations (3.2)--(4.4) prove survival of local geodesic exchange geometry;
they do not prove that local exchanges augment an arbitrary weighted
matching.  Two gaps remain.

1. A dual weighting may be supported entirely on the exceptional
   schedules.  To use the weighted Berge cut, those schedules need a
   separate `o(D)` colouring or a direct charging theorem.
2. There is no proved theorem saying that a subcritical matching in the
   protected chunk hypergraph admits a bounded-radius geodesic
   augmentation.  In a general set-packing system this assertion is
   false.  It must be derived from the common departure/arrival schedule.

For an unweighted near-factor, (3.2) is more directly useful: discarding
the eroded schedules changes every good tag fibre by `o(1)`, while the
bad-fibre physical ledger is `o(W)`.  A bounded-radius augmenting theorem
whose radius tends to infinity slower than
`log m/log log m` would therefore finish the integral selection at
relative error `o(1)`.  With literal row repair one needs the stronger
error `o(1/Q)`; the currently unproved horizontal braid reserve would
relax this back to `o(1)`.

## 6. Quarantine itself preserves the pair-square normalization

There is one further exact gain.  Let `d_0(x)` and `d_0(x,y)` be the raw
target degree and pair codegree, and let `d_A` denote the values after
quarantine.  On every good target fibre,

\[
 d_A(x)\ge(1-\eta)d_0(x),
 \qquad
 d_A(x,y)\le d_0(x,y).
 \tag{6.1}
\]

Therefore the symmetrically normalized codegree obeys

\[
 \boxed{
 \frac{d_A(x,y)}{\sqrt{d_A(x)d_A(y)}}
 \le
 \frac1{1-\eta}
 \frac{d_0(x,y)}{\sqrt{d_0(x)d_0(y)}}.}
 \tag{6.2}
\]

Every blockwise pair-square sum consequently inflates by at most
`(1-eta)^{-2}=1+o(1)`.  Dynamic quarantine itself therefore preserves
the proved pair-square and bow-tie bounds.  The remaining source of
hereditary distortion is specifically the later owner-indicator and
priority weighting, which may delete opposite corners of otherwise intact
switch squares.

No coefficient-one conclusion is claimed here.
