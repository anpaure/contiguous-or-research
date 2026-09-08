# Even equivariant multi-component `(c,t)` and compact routing

Date: 2026-07-29  
Status: exact solver-free normal form and encoding-size theorem.  No carrier
existence claim and no solver run.

## 0. Verdict

Let `K=2r`, `n=K-1=2r-1`, let `rho(x)=x+1` on the old coordinates
`Z_n`, and let `z` be fixed.  Put

\[
 W=\binom K r,\qquad N=W/n.
\]

There is an exact arbitrary-component extension of the unit-voltage
`(c,t)` chart.  It has two equivalent forms.

1. **Slot-voltage form.**  Choose one representative of every middle-owner
   orbit, a successor permutation of the `N` representatives, and one
   residue in `Z_n` on each successor dart.  One local Johnson test and one
   local no-backtracking test are necessary and sufficient.
2. **Componentwise track form.**  A quotient component of length `ell` and
   voltage `v` needs `g=gcd(n,v)` binary tracks, each of length
   `(n/g)ell`, and one top word of length `ell`.  The total number of track
   bits over all components is still exactly `W`, including at zero and
   nonunit voltage.

On one quotient component, the familiar one-word `(c,t)` chart is exactly
the special case `g=1`.  With several unit-voltage components there is one
track per component, not one global chronology word, and their relative
voltages survive.  Replacing every component voltage by one is not without
loss: section gauges preserve voltage, and only one global coordinate
multiplier is available.

For a fixed finite window catalogue, the compact orbit-coverage/Waksman
projection extends to this normal form without any occurrence-by-target
selector product.  If the component decomposition is variable, one extra
width-`N` Waksman successor network and `N` phase residues suffice.  This is
an encoding theorem, not a claim that the current one-cycle implementation
already performs the extension.

## 1. Free owner action

Write a middle state uniquely as

\[
 U=M\cup (t\{z\}),\qquad t\in\{0,1\},\qquad |M|=r-t.
\tag{1.1}
\]

The `C_n` action is free on both shores.  Indeed, a set fixed by a
nonidentity translation is a union of equal translation orbits of some
length `d>1` dividing `n`; hence `d` divides its old rank.  But

\[
 \gcd(n,r)=\gcd(n,r-1)=1.
\tag{1.2}
\]

Consequently there are exactly `N` middle-owner orbits, and a spanning
equivariant factor has exactly one quotient vertex over each of them.

## 2. Exact slot-voltage normal form

### Theorem 2.1 (arbitrary-component quotient normal form)

A `rho`-invariant spanning simple degree-two factor of `J(K,r)` is
equivalent, up to choosing an orientation on every quotient component, to
the following data:

* representatives `U_i`, `1<=i<=N`, of all middle-owner orbits, each used
  exactly once;
* a permutation `sigma` of `{1,...,N}`;
* phases `p_i in Z_n` such that

  \[
       U_i\sim \rho^{p_i}U_{\sigma(i)};
  \tag{2.1}
  \]

* for `h=sigma^{-1}(i)`, the two physical neighbours at `U_i` are distinct:

  \[
   \rho^{-p_h}U_h\ne \rho^{p_i}U_{\sigma(i)}.
  \tag{2.2}
  \]

The reconstructed physical edge set is

\[
 E=\bigl\{\{\rho^aU_i,\rho^{a+p_i}U_{\sigma(i)}\}:
        i\in[N],\ a\in Z_n\bigr\}.
\tag{2.3}
\]

If `C=(i_0,...,i_(ell-1))` is a cycle of `sigma`, define

\[
 v_C=\sum_{j=0}^{\ell-1}p_{i_j}\pmod n.
\tag{2.4}
\]

Then `C` lifts to exactly

\[
 g_C=\gcd(n,v_C)
\tag{2.5}
\]

physical cycles, each of length `n ell/g_C`; here `gcd(n,0)=n`.  Hence the
whole factor has

\[
 \sum_C\gcd(n,v_C)
\tag{2.6}
\]

physical components.

#### Proof

Given the data, every physical vertex `rho^a U_i` has the outgoing edge
indexed by `(i,a)` and the incoming edge indexed by
`(sigma^{-1}(i),a-p_(sigma^{-1}(i)))`.  Equation (2.1) makes both Johnson
edges, and (2.2) makes them distinct.  Freeness of the owner action and
oddness of `n` exclude any other duplicate of an undirected lifted edge.
Thus (2.3) is a spanning simple degree-two factor.

Conversely, quotient a `rho`-invariant factor.  Its quotient is a weighted
degree-two multigraph, with a loop counted twice.  Orient each circuit.  At
every quotient owner there is then one outgoing circuit dart; relative to
the chosen owner representatives it has a unique phase `p_i`.  Simplicity
of the physical factor is exactly (2.2), and the outgoing darts define
`sigma`.

After one lap around `C`, a physical phase `a` becomes `a+v_C`.
Translation by `v_C` on `Z_n` has `g_C` orbits, each of size `n/g_C`.
Following one such phase orbit traverses `C` `n/g_C` times, proving
(2.5)--(2.6).  QED.

For quotient cycles of length at least three, (2.2) follows from the owner
transversal.  It is essential for a length-two quotient cycle: the two
oppositely directed darts must not be the same undirected edge orbit.  In a
closing-voltage gauge this exceptional failure is precisely `v_C=0`.

### Proposition 2.2 (what the section gauge does)

Changing representatives by `U_i'=rho^{a_i}U_i` changes

\[
 p_i'=p_i+a_i-a_{\sigma(i)}.
\tag{2.7}
\]

Thus every `v_C` is gauge invariant.  On each `sigma`-cycle, one may choose
the `a_i` so that every dart except the closing dart has phase zero and the
closing dart has phase exactly `v_C`.

#### Proof

Equation (2.7) follows by rotating the physical dart by `a_i`.  Its extra
terms telescope around a cycle.  Starting at one vertex and recursively
setting `a_(sigma(i))=a_i+p_i` kills all nonclosing phases; the remaining
closing phase is their sum.  QED.

This componentwise flattening is genuinely without loss: it changes the
section, not the physical factor.  It must not be confused with changing
the voltage.

## 3. Exact componentwise multi-track `(c,t)` chart

Fix one oriented quotient component `C` of length `ell` and voltage `v`, in
the closing-voltage gauge of Proposition 2.2.  Write its representatives as

\[
 U_j=M_j\cup(t_j\{z\}),\qquad 0\le j<\ell,
\tag{3.1}
\]

so the internal seams are `U_j~U_(j+1)` and the closing seam is
`U_(ell-1)~rho^v U_0`.  Put

\[
 g=\gcd(n,v),\qquad m=n/g.
\tag{3.2}
\]

For `0<=h<g` and `q in Z_m`, set

\[
 x_{h,q}=h+qv\pmod n.
\tag{3.3}
\]

These are the `g` orbits of translation by `v` on the old coordinates.

### Theorem 3.1 (multi-track reconstruction)

The masks `M_0,...,M_(ell-1)` are equivalent uniquely to `g` cyclic binary
tracks

\[
 c_h\in\{0,1\}^{m\ell}\qquad(0\le h<g)
\tag{3.4}
\]

through

\[
 x_{h,q}\in M_j
 \quad\Longleftrightarrow\quad
 c_h(j-q\ell)=1,
\tag{3.5}
\]

where track indices are reduced modulo `m ell`.  Extending (3.5) to the
integer `j=ell` gives automatically

\[
 M_\ell=\rho^vM_0.
\tag{3.6}
\]

Define, using the integer `j+1` before reducing track indices,

\[
 S_j=\sum_{h,q}(1-c_h(j-q\ell))c_h(j+1-q\ell),
\tag{3.7}
\]

\[
 E_j=\sum_{h,q}c_h(j-q\ell)(1-c_h(j+1-q\ell)).
\tag{3.8}
\]

The displayed sequence is a rank-`r` twisted closed Johnson **walk** with
closing voltage `v` if and only if, for every `j in Z_ell`,

\[
 \sum_{h,q}c_h(j-q\ell)=r-t_j,
\tag{3.9}
\]

and

\[
 \boxed{
 S_j=1-(1-t_j)t_{j+1},\qquad
 E_j=1-t_j(1-t_{j+1}).}
\tag{3.10}
\]

Across all quotient components the chart reconstructs a spanning factor if
and only if the pairs `([M_j],t_j)` form the complete middle-owner orbit
transversal and the simplicity condition (2.2) holds.

#### Proof

The map `(j,q) -> j-q ell` is a bijection from
`Z_ell x Z_m` to `Z_(m ell)`, so (3.5) is a unique encoding.  At `j=ell`,

\[
 c_h(\ell-q\ell)=c_h(-(q-1)\ell),
\]

which says that `x_(h,q)` belongs to `M_ell` exactly when
`x_(h,q-1)=x_(h,q)-v` belongs to `M_0`.  This is (3.6).

Equations (3.7)--(3.8) therefore count exactly the old coordinates inserted
and deleted at the `j`-th seam, including the twisted closing seam.  The top
coordinate is inserted on a `01` top seam and deleted on a `10` seam.  A
rank-preserving distinct Johnson step has exactly one total insertion and
one total deletion, which is precisely (3.10).  Equations (3.9) are exactly
the rank laws.  The global orbit-transversal and simplicity conditions in
the preceding paragraph are what upgrade these local walk equations to
factor circuits; Theorem 2.1 then applies.  QED.

### Corollary 3.2 (bit census and the unit case)

Component `C` uses

\[
 g(m\ell)=n\ell
\tag{3.11}
\]

track bits.  Since the quotient component lengths sum to `N`, the complete
arbitrary-voltage chart uses exactly

\[
 \sum_C n\ell_C=nN=W
\tag{3.12}
\]

`c` bits and `N` top bits, exactly the census of the one-cycle `(c,t)`
chart.

If `v` is a unit, then `g=1`, and (3.5) is one scalar word of length
`n ell`.  Writing `q=v^{-1}x` recovers

\[
 M_j=\{x:c(j-v^{-1}x\ell)=1\}.
\tag{3.13}
\]

After a legitimate global normalization `v=1`, this is the familiar
formula `M_j={x:c(j-x ell)=1}`.  A nonunit voltage intrinsically has `g`
translation tracks in this uniform helical-shift normal form.  Their bits
can of course be concatenated into one storage array, but no one-orbit
scalar closure formula replaces them; doing so silently discards `g-1`
translation orbits.

Using the component's own order `0,v,2v,...` in (3.5) is only an indexing
of the actual common coordinate set.  It is therefore legal independently
on different components and does **not** assert an independent physical
coordinate relabelling; all cross-component owner and palette identities
remain expressed in the original labels through (3.3).

### Corollary 3.3 (literal traces and residence)

One physical lift over a phase orbit has length `m ell`.  For any old
coordinate, its trace on that lift is a cyclic shift of exactly one `c_h`.
The top trace is the `m`-fold repetition `t^m`.  Hence componentwise
positive (respectively dual) `D`-residence is equivalent to all cyclic
one-runs (respectively both one- and zero-runs) of every `c_h` and of `t^m`
having length at least `D`.

Here cyclic runs use the finite physical-cycle convention.  A constant-one
trace on a component of length `L=m ell` is one positive run of length `L`,
and a constant-zero trace is one zero run of length `L`.  Thus a constant
positive trace on a component shorter than `D` fails positive residence;
periodically traversing the component again does not turn it into an
infinite run.  The absent run type is vacuous for one-sided residence but
the present constant run still governs dual residence.

#### Proof

Start the lift in phase `a` and write `x-a=x_(h,q_0)`.  At physical time
`q ell+j`,

\[
 x\in\rho^{a+qv}M_j
 \Longleftrightarrow
 x_{h,q_0-q}\in M_j
 \Longleftrightarrow
 c_h(q\ell+j-q_0\ell)=1.
\]

This is a cyclic shift of `c_h`; the top coordinate is fixed by rotation.
QED.

### Corollary 3.4 (the monochromatic-cycle residence correction)

For a coordinate trace `b` on a physical component of length `L`, positive
`D`-residence is equivalent to the disjunction

\[
 \begin{cases}
 b\not\equiv1\text{ and no cyclic motif }0\,1^s\,0
                         \text{ has }1\le s<D,\quad\text{or}\\
 b\equiv1\text{ and }L\ge D.
 \end{cases}
\tag{3.14}
\]

The dual statement adds the analogous all-zero/`1 0^s 1` test.  Therefore
the usual boundary-motif clauses alone are incomplete on a monochromatic
physical component: an all-one cycle of length `<D` has no `0 1^s 0`
boundary witness but still violates residence.  In the fixed componentwise
track chart this is just the constant-word length test; in a variable
successor model it must be audited from the exact physical return length or
represented by a guarded constant-cycle row.

When compiling the nonconstant boundary motifs, the two displayed boundary
zeros are allowed to be the same physical state after one exact wrap.  A
short nonconstant physical cycle may realize `0 1^s 0` with its last zero
equal to its first.  Requiring the motif certificate itself to be a simple
path would therefore be an unsound weakening.

#### Proof

If `b` is nonconstant, every maximal positive run has both a zero predecessor
and a zero successor, so the motifs enumerate its positive runs exactly.  If
`b` is constant one, its unique cyclic run has length `L` and has no zero
boundary.  The zero statement is complementary.  QED.

In the compiler notation used elsewhere in this project, depth `d`
positive residence means minimum positive-run length `D=d+1`.  A separate
zero-run requirement, if imposed, must use its own declared threshold.

## 4. Exactly which voltage normalizations are WLOG

There are three different operations.

1. A section gauge (2.7) preserves every component voltage.
2. A single global coordinate automorphism `x -> ux`, `u in Z_n^times`,
   sends every voltage simultaneously to `uv_C`.
3. Reversing an undirected component sends its voltage to `-v_C`.  This sign
   is available independently only when the admitted chronology/catalogue
   is closed under that reversal.

It follows that:

* one unit-voltage component can be normalized to voltage one by one global
  multiplier, provided the construction class is closed under that global
  coordinate relabelling;
* with fixed orientations, all unit component voltages can be made one if
  and only if they were all equal;
* with independently reversible components, they can all be made one if
  and only if all lie in one sign class `{v,-v}`;
* `gcd(n,v_C)`, in particular zero or nonunit status, is invariant under
  every global multiplier.

Thus a one-component physical Hamilton lift forces a unit voltage and may
be put in the original voltage-one chart.  Requiring each component of an
arbitrary factor to have voltage one is only a sufficient subclass.

This failure is realized already at `K=6`: the exact four-loop equivariant
middle factor in Section 5 of the cited audit has unit voltage vector
`(1,2,1,2)` modulo five.  The sign classes `{1,4}` and `{2,3}` are disjoint,
so no common multiplier, even with independent loop reversals, makes all
four voltages one.

The exact simultaneous normalization criterion for nonunits is the common
unit-multiplier/prime-power criterion proved independently in
`MATH_AUDIT_AD_EVEN_MULTICOMPONENT_COMMON_VOLTAGE_GAUGE_20260729.md`.

## 5. Compact and Waksman encoding size

Let `S(M)` be the number of switches in the unequal recursive Waksman
network on `M` wires:

\[
 S(1)=0,\qquad
 S(M)=2\lfloor M/2\rfloor
      +S(\lceil M/2\rceil)+S(\lfloor M/2\rfloor).
\tag{5.1}
\]

This is the exact recurrence of the current two-sided recursive
implementation (including its two switches at size two), not the
occasionally quoted minimal-switch recurrence `M-1+...`, which differs at
even sizes.  Thus `S(M)=O(M log M)`; exactly

\[
                 S(858)=8078,
 \qquad S(5148)=61680.
\tag{5.1a}
\]

### Theorem 5.1 (arbitrary topology without edge selectors)

Conditional on the existing exact middle owner-transversal layer, the
slot-voltage data of Theorem 2.1 have an exact Boolean routing encoding
with:

* `W=nN` old-membership bits and `N` top bits;
* one **additional** width-`N` Waksman network, using `S(N)` switch
  controls, to encode `sigma`;
* `N ceil(log_2 n)` phase bits, with residues `n,...,2^b-1` forbidden;
* `O((n+log n)S(N)+Nn log n)` multiplexer-size local circuitry for the
  forward predecessor payload, the backward successor payload, the two
  phase rotations, the Johnson test, and (2.2).

Together with one exact width-`N` middle-orbit partial-permutation network,
which enforces that the `U_i` are the complete owner-orbit transversal,
this projection is necessary and sufficient for all rotation-equivariant
spanning simple factors.  The successor/phase block by itself enforces the
local factor law but does not prevent two slots from choosing the same owner
orbit.  The complete model contains every component decomposition and every
component voltage; voltages are recovered as the cycle sums (2.4), so no
component-by-voltage or edge-by-component selector is required.

#### Proof

A Waksman setting realizes an arbitrary permutation `sigma`.  Route the
source state and its phase forward; at output `i` this supplies the unique
predecessor `h` and constructs `rho^(-p_h)U_h`.  Route the output-labelled
state payload backward through the same switch settings; at input `i` this
supplies `U_(sigma(i))` and constructs `rho^(p_i)U_(sigma(i))`.  Enforce
(2.1) and inequality (2.2) slotwise.  The separate middle cover network is
exactly the orbit-transversal condition in Theorem 2.1, so that theorem
proves exactness.

Each switch routes only `O(n+log n)` payload bits.  A binary barrel rotator
uses `O(n log n)` multiplexers per phase-controlled state, giving the stated
size.  No catalogue edge is selected from a Cartesian source-target table.
QED.

If the component lengths and voltages are fixed in advance, arrange their
quotient slots componentwise and use the track chart of Theorem 3.1.  Then
the successor network is unnecessary: only the component boundary formulas
change, and the base variable census remains exactly `W+N`.

### Corollary 5.2 (voltage information is linear, not constant)

If a labelled component decomposition is fixed but its voltages are not,
retain one residue `V_C in Z_n` per component and impose the modular sum of
its dart phases.  This needs `c ceil(log_2 n)` voltage bits and
`O(N log n)` modular-addition circuitry, not a one-hot enumeration of
`n^c` voltage vectors.

Conversely, for `c` oriented all-unit components, diagonal global
multiplication has exactly

\[
                     \varphi(n)^{c-1}
\tag{5.2}
\]

labelled voltage classes.  Any exact encoding modulo that WLOG symmetry
therefore needs at least

\[
                (c-1)\log_2\varphi(n)
\tag{5.2a}
\]

bits of relative-voltage information.  The relative residues
`V_C V_(C_0)^(-1)` attain this linear information scale.  Thus one global
unit-voltage flag is insufficient, while an exponential selector product is
also unnecessary.

#### Proof

The upper bound is ordinary modular summation.  The diagonal action of
`Z_n^times` on `(Z_n^times)^c` is free; normalize one distinguished entry,
leaving `c-1` arbitrary unit ratios.  This proves the count and its
information lower bound.  QED.

### Theorem 5.3 (coverage routing remains selector-free)

Fix a finite set `H` of permitted window widths and let `Hmax=max H`.
From the slot-voltage datum, form all **one-pass** successor windows within
its physical lift components.  A quotient component `C` contributes its
`ell_C` quotient-start words at width `w` exactly when

\[
                 w\le n\ell_C/\gcd(n,v_C).
\tag{5.3}
\]

Thus the actual input count is

\[
 M_w=\sum_{C:\,w\le n\ell_C/\gcd(n,v_C)}\ell_C\le N.
\tag{5.4}
\]

If every physical component has length at least `Hmax`, then `M_w=N` for
every admitted width.  Otherwise one may use the smaller network of width
`M_w`, or pad to width `N` with fixed inactive words that cannot equal a
required nonempty target.  Repeated traversal of a shorter physical cycle
is not called a literal one-pass interval here.

For variable topology this padding has the following exact intrinsic form.
For a start slot `i`, let

\[
 \sigma^q(i),\qquad
 P_{i,q}=\sum_{a=0}^{q-1}p_{\sigma^a(i)}\pmod n
\tag{5.5}
\]

be its slot and accumulated phase after `q` successor steps.  Define

\[
 a_{i,w}=1
 \quad\Longleftrightarrow\quad
 \forall\,1\le q<w:\
 (\sigma^q(i),P_{i,q})\ne(i,0).
\tag{5.6}
\]

The first return of the lifted successor to `(i,0)` is exactly the physical
component length.  Hence `a_(i,w)=1` if and only if the requested width is a
valid one-pass interval.  Carry the pair `(a_(i,w),word_(i,w))` through the
coverage Waksman network and require validity bit one at every required
target output.  Inactive inputs may be padded arbitrarily and cannot serve a
target.  Formula (5.6) costs only
`O(Hmax N(log N+log n))` equality/comparison circuitry after the successor
payloads have been generated; it introduces no target selectors.

This is an exact catalogue of cyclic one-pass windows of the factor.  It
does **not** choose one simultaneous cut in every physical cycle.  A given
cyclic window is present in some opening of its cycle, but a single fixed
opening loses the windows crossing its cut.  Cut selection, the resulting
boundary losses, and cross-component seams belong to the separate opening /
compiler layer; no claim about them is hidden in this theorem.

For a fixed component decomposition one may use the exact active count
`M=M_w`.  For variable topology, retain `M=N` wires and use the validity
bit above.  In either case, for `D<=M` required rotation orbits, exact
coverage is expressible by:

* `M ceil(log_2 n)` phase bits and `M` barrel rotators;
* one width-`M` Waksman network with `S(M)` controls and
  `O(KS(M))` word multiplexers;
* `D` fixed representative equalities.

There are no `M D` occurrence-target selectors.  For variable `sigma`, all
windows through width `Hmax` can be generated by `Hmax-1` further payload
passes through the same successor switch settings, for total size

\[
 O\!\left(
 H_{\max}(n+\log n)S(N)
 +H_{\max}Nn\log n
 +\sum_f K M_f\log M_f
 \right),
\tag{5.7}
\]

where `f` ranges over the middle/shadow/upper catalogue families.  For a
fixed catalogue this is polynomial and has the same absence of selector
products as the current compact model.

#### Proof

The partial-permutation lemma is component-blind: every required orbit is
covered if and only if one may independently phase one distinct actual
occurrence per required orbit and permute those phased words to fixed
required outputs.  A Waksman network realizes that permutation.  Component
voltage changes which words occur and, through the one-pass condition
(5.3), can reduce their number; it does not change the lemma or create a
target-by-occurrence product.

The independent phases in this coverage network are only witnesses that an
actual word belongs to a required rotation orbit.  They do not replace or
modify the physical dart phases `p_i`, and they cannot normalize component
voltages independently.

Successive applications of the same `sigma` switch settings propagate the
state and accumulated phase along a quotient component, producing the
candidate windows.  Equation (5.6) removes precisely those that have already
wrapped around their physical component.  The number of payload copies is
linear in the largest admitted width, and the routing controls are shared.
The displayed bound follows from (5.1).  QED.

For the present `K=16` padded family widths, the coverage-network switch
controls can therefore retain the audited census

\[
 3S(858)+S(6\cdot858)=85{,}914.
\tag{5.8}
\]

The arbitrary-topology extension adds one successor network, hence `8078`
controls, for `93,992` controls at this network level.  Validity tags and
successor payload passes add multiplexed bits and clauses but no further
permutation controls and no occurrence-by-target selectors.  This is not an
exact CNF-variable census for a patched implementation; such a census must
also fix its mux and modular-adder encodings.

### Corollary 5.4 (conservative `K=16` successor-layer census)

Let `b=ceil(log_2 n)` and build aligned states through width `L`.  Excluding
the `W+N` quotient-state bits already present, rank/Johnson comparators,
cover networks, and the validity equalities (5.6), the shared-successor
construction needs at most

\[
 S(N)+2K(L-1)S(N)+Nb+nbN(L-1)
\tag{5.9}
\]

Boolean variables: one set of switch controls, two `K`-bit mux outputs per
switch and successor layer, the phase fields, and the old-coordinate barrel
rotators.  At `K=16`, `n=15`, `N=858`, `b=4`, and `L=13`, this is

\[
 8078+3{,}101{,}952+3{,}432+617{,}760
 =3{,}731{,}222.
\tag{5.10}
\]

This is an auxiliary-layer upper bound, not the variable count of an
implemented widened CNF.  It must not be added blindly to the current
fixed-successor total: some fixed-column/window circuitry is being replaced,
while the orbit-cover networks are reused.

### Proposition 5.5 (optional exact voltage annotation)

If arbitrary voltages are merely allowed, the edge phases already encode
them and no component annotation is needed.  If the master must constrain or
report each component voltage while `sigma` is variable, this can still be
done without enumerating voltage tuples.

Give slot `i` a root label `a_i in [N]`, an integer order
`h_i in {0,...,N-1}`, a potential `q_i in Z_n`, and a root bit `R_i`.  Route
their successor values through the same `sigma` controls and impose

\[
 a_{\sigma(i)}=a_i,\qquad a_i\le i,\qquad
 R_i\Longleftrightarrow a_i=i,
\tag{5.11}
\]

\[
 R_i\Longrightarrow h_i=0,qquad
 \neg R_i\Longrightarrow h_i>0,qquad
 \neg R_{\sigma(i)}\Longrightarrow
 h_{\sigma(i)}=h_i+1.
\tag{5.12}
\]

Set `q_i=0` at roots.  On an edge not entering a root require

\[
 q_{\sigma(i)}=q_i+p_i\pmod n,
\tag{5.13}
\]

and on the unique edge entering root `j` record

\[
 V_j=q_i+p_i\pmod n.
\tag{5.14}
\]

These rows give exactly one root, the minimum-index slot, on every
`sigma`-cycle: a rootless cycle would make `h` increase strictly around a
closed loop, while the propagated root label permits at most one root.
Equations (5.13)--(5.14) then telescope to the exact cycle voltage.  Any
desired residue predicate may be imposed at the root; omitting it permits
all voltages.

Writing `a=ceil(log_2 N)` and `b=ceil(log_2 n)`, the four routed fields have
`2a+b+1` bits.  They require at most

\[
 2(2a+b+1)S(N)
\tag{5.15}
\]

multiplexer variables, `N(2a+b+1)` stored bits, and
`O(N(a+b))` local comparison/addition gates.  At `N=858`, `a=10`, `b=4`,
the mux bound is `403900`.  This is polynomial shared-control annotation,
not an `n^c` selector over the `c` component voltages.  The complexity of an
extra allowed-voltage predicate depends only on how that predicate itself is
represented.

## 6. Scope boundary

The following are exact WLOG statements:

* the slot-voltage normal form for rotation-equivariant spanning simple
  factors;
* componentwise closing-voltage gauge;
* the multi-track chart, including zero and nonunit voltage;
* one global normalization of one unit voltage, when the admitted class is
  closed under that coordinate multiplier;
* Waksman partial-permutation coverage for the actual fixed catalogue.

The following are only sufficient subclasses or still require separate
work:

* one quotient component and unit voltage, unless a physical Hamilton
  carrier is itself required;
* voltage one on every component;
* any fixed upper-width catalogue, absent a width-completeness theorem;
* the present `search_even_eager_benes_cnf_20260729.cpp`, which hardcodes
  the one-cycle `(c,t)` successor rather than Theorem 5.1;
* componentwise reversal inside a directed or asymmetric catalogue unless
  reverse closure is proved;
* opening/joining the cyclic components, cross-component literal intervals,
  and the exact common compiler.

For `Hmax=O(1)` and a fixed number of catalogue families, (5.7) is
near-linear in `N` up to logarithms.  If every width `2,...,N` is explicitly
materialized, there are already

\[
 \sum_{w=2}^{N}N=\Theta(N^2)
\]

start--width objects before target matching, and the shared routing bound is
`O(KN^2 log N)`.  This all-width growth is a chronology-catalogue issue, not
a component-voltage selector blowup; no all-width near-linear encoding is
proved here.

If componentwise voltage predicates (rather than arbitrary voltages) must
be enforced inside the master while the cycle decomposition is itself
unknown, Proposition 5.5 supplies one exact rooted-cycle arithmetic layer of
polynomial size.  The representation cost of an additional nonlinear
predicate on the recovered voltages remains separate.  Theorem 5.1 proves
that merely allowing arbitrary voltages causes no selector blowup; it does
not make every possible predicate on their multiset free.
