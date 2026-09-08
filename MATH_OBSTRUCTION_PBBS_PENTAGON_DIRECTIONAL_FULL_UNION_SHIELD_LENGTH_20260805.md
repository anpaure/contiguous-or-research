# Directional full-union shields for the PBBS pentagon require linear support

**Date:** 2026-08-05  
**Method:** exact missing-bank count, Johnson union-rank growth, and the
sharp cyclic-window rotor; no computation or search  
**Status:** unconditional obstruction to an `O(d)` context-free shielded
pentagon.  The rank-three common-history core closes the strict-lower deck
but does not shorten a full-union exterior shield.  Even after using both
depth-`d` collars, every shielded cut needs `Omega(k)` owner support.  A
linear shield is sharp and can be biresident, but a height ladder with
`Theta(d)` cuts then has `Omega(kd)` marked shield support.

## 0. Outcome

Use the three-screen pentagon notation

\[
 n=2r+1,
 \qquad R=r+1,
 \qquad |G_h|=R-3=r-2.
\]

At a changed role, the old owner edge is

\[
                         P_iQ_i,
\]

and its two owners have rank `R` and one common rank-`R-1` facet.  Hence

\[
                         |P_i\cup Q_i|=R+1=r+2.             \tag{0.1}
\]

The exact missing coordinate bank is therefore

\[
 \boxed{
  M_i=[n]\setminus(P_i\cup Q_i),
  \qquad |M_i|=(2r+1)-(r+2)=r-1.}                         \tag{0.2}
\]

Thus the common rank-`R-3` core and the two rank-three screens still leave a
linear-size bank outside one hinge union.

The sharp conclusions are:

1. a full-union block of rank-`R` Johnson owners has at least

   \[
                            n-R+1=r+1                     \tag{0.3}
   \]

   owners;
2. even crediting both hinge owners, a one-sided directional penetration
   must contain at least `r` owners on that side before full union is
   possible;
3. crediting depth-`d` collars on both sides leaves at least

   \[
                            r-2d-1                         \tag{0.4}
   \]

   additional owner positions in any full-union block; and
4. for the word deadline `d=Theta(sqrt r)`, all three bounds are
   `Theta(r)=Theta(k)`, not `O(d)`.

The cyclic-window rotor attains (0.3) and has a literal depth-`d`
antecedent, so the obstruction is the correct scale rather than an artifact
of the proof.

## 1. Why the small screen bank is not enough

The head permutation changes only a rank-three screen at the immediate
hinge, and the union of all five head-screen differences is contained in
the five-label survivor bank.  It is tempting to saturate only those five
labels.

That would preserve the **internal** hinge value, but not an arbitrary
exterior interval.  In the old reassembly a crossing interval couples one
incoming context with one outgoing context.  The rethread couples the same
incoming context with a different outgoing context.  Coordinates occurring
farther down those outgoing arcs are not confined to the five-label bank.

### Proposition 1.1 (two unsaturated coordinates are not context-free)

Let `S` omit two coordinates `p,q`.  A theorem which assumes only that every
directional shield has union containing `S` cannot preserve the complete
upper support for all owner-legal two-sided exteriors.

#### Proof

Place a private `p` occurrence in the old outgoing context of role zero and
nowhere else.  Under the cyclic head shift that complete right context moves
to role `-1`.  Put a private `q` occurrence in the incoming context of role
`-1`, and omit `q` from role zero.  The standard Johnson-legal marker collar
realizes either marker by replacing one nonprotected coordinate in the
adjacent owner.

The old role-zero crossing interval has target `S+p`.  After the shift, the
only right context containing `p` is paired with the left context containing
`q`, and therefore gives `S+p+q`; no other new role contains `p`.  The target
`S+p` is proper because `q` is absent, so the full-ground target does not
rescue it.  Thus `S+p` is lost.  \(\square\)

Consequently a **context-free support** theorem based on one common
saturation set needs

\[
                         |S|\ge n-1.                        \tag{1.1}
\]

This is sharp at the level of set support: if `S` is co-singleton, every
interval containing it has value either `S` or the full ground set, and
both values have the obvious shield witnesses.  The full-union theorem uses
`S=[n]`; even the optimal co-singleton relaxation below remains linear in
owner length.  A much smaller bank can be useful only after proving a
PBBS-specific restriction on all exterior coordinate differences; no such
restriction follows from the rank-three screen algebra.

## 2. Sharp owner-length lower bounds

### Lemma 2.1 (Johnson union growth)

Let

\[
                         T_0,T_1,\ldots,T_{\ell-1}
\]

be a path of rank-`R` Johnson owners.  Then

\[
 \left|\bigcup_{j=0}^{\ell-1}T_j\right|
                         \le R+\ell-1.                    \tag{2.1}
\]

#### Proof

The first owner contributes `R` coordinates.  Every Johnson transition
deletes one coordinate and inserts one, so it introduces at most one
coordinate not seen previously.  Sum over the `ell-1` transitions.
\(\square\)

### Theorem 2.2 (full-union shield aperture)

Every full-ground block of rank-`R` Johnson owners has at least

\[
                         n-R+1=r+1                         \tag{2.2}
\]

owners.

If a crossing interval is credited with both hinge owners `P_i,Q_i`, and
uses `s` outgoing owners including `Q_i`, then it has at most

\[
                         R+s                               \tag{2.3}

\]

coordinates.  Hence a one-sided directional rule of the form

\[
   \text{outgoing penetration at least `s`}
   \Longrightarrow \text{full union}
\]

requires

\[
                         s\ge n-R=r.                       \tag{2.4}
\]

#### Proof

Equation (2.2) is Lemma 2.1 with union rank `n`.  For (2.3), the interval
contains `s+1` owners after counting `P_i` and the `s`-owner outgoing
segment; Lemma 2.1 gives `R+s`.  Full union forces `R+s>=n`, which is
(2.4).  \(\square\)

### Corollary 2.3 (even co-singleton saturation is linear)

Any common saturation block strong enough for Proposition 1.1 in arbitrary
two-sided exteriors has union rank at least `n-1` and therefore contains at
least

\[
                         (n-1)-R+1=n-R=r                    \tag{2.5}
\]

rank-`R` Johnson owners.  Thus weakening full union to the sharp
co-singleton support condition saves only one owner.

The missing-bank count (0.2) gives the same result directly: after the
two-owner hinge has supplied rank `R+1`, at least `r-1` additional fresh
coordinates must enter, one per later Johnson transition.

## 3. A depth-`d` collar cannot hide the linear aperture

Suppose one installs a left collar of at most `d` owners and a right collar
of at most `d` owners around the hinge.  The resulting protected local block
has at most

\[
                         2d+2                              \tag{3.1}

\]

owners.  Even if it is a geodesic which introduces one fresh coordinate at
every step, its union has rank at most

\[
                         R+2d+1.                           \tag{3.2}

\]

### Corollary 3.1 (residual shield length)

Any extension of this collared block to a full-union Johnson block requires
at least

\[
                         r-2d-1                            \tag{3.3}

\]

additional owners.  In particular, when `d=o(r)`, the additional support
is `Omega(r)`.

#### Proof

A full-union block needs at least `r+1` owners by Theorem 2.2.  Subtract the
`2d+2` owners already credited in (3.1); if the difference is negative,
replace it by zero.  This gives (3.3).  Equivalently, subtract (3.2) from
`n=2r+1`.  \(\square\)

There is also an unavoidable transition band.  Put a full-union shield
immediately outside the depth-`d` collar.  An interval with penetration

\[
                         d+1,d+2,\ldots,r-1               \tag{3.4}

\]

is too long for a theorem transporting only the local depth-`d` deck and
too short to contain the complete directional shield guaranteed by
Theorem 2.2.  The band has `r-d-1=Theta(r)` possible penetrations.  Moving
the shield farther away only enlarges it.

Thus “local transport through depth `d`, then full union” cannot be a
gapless proof when `d=Theta(sqrt r)`.

## 4. Sharpness and residence

The lower bound is attained.  Since

\[
                         n=2R-1,
\]

the cyclic-window rotor on `n` coordinates consists of the owners

\[
 T_j=\{z_j,z_{j+1},\ldots,z_{j+R-1}\}.                    \tag{4.1}

Every `R=r+1` consecutive owners have union `[n]`.  No shorter block can do
so by Theorem 2.2.

The same rotor has positive runs of length `R` and zero gaps of length
`R-1`; hence it is biresident for every

\[
                         d\le R-2.                          \tag{4.2}

\]

It also has the explicit nonempty depth-`d` source antecedent from the
cyclic-window rotor theorem.

Opening the rotor is not free: every opening clips a positive and a zero
run to length one.  The sharp opening theorem requires a `d`-owner residence
collar on each exposed side and exports one nested seam state.  Therefore a
literal opened directional shield has support

\[
                         (r+1)+O(d)=Theta(r),              \tag{4.3}

\]

with the `Theta(r)` term unavoidable and the residence overhead lower
order at the word deadline.

This shows that residence is compatible with the linear shield; it does not
compress it to `O(d)`.

## 5. Many pentagon cuts

The height-ladder return changes

\[
                         q=5(H-2)                           \tag{5.1}

\]

old factor edges.  The full-union arc theorem requires every directed
intercut arc to contain its prescribed shield and, in particular, to have
length at least `r+1` under the standalone-shield convention.

### Proposition 5.1 (aggregate marked support)

If the `q` cut sides are protected by resource-disjoint full-union arc
blocks, their total marked owner support is at least

\[
                         q(r+1)=5(H-2)(r+1).                \tag{5.2}

\]

Allowing the terminal block of one cut to serve as the initial block of the
next can change only the constant convention: every intercut arc still
needs `Theta(r)` owners.  Hence the aggregate scale is

\[
                         \Omega(Hr).                        \tag{5.3}

\]

For `H=Theta(d)` and `d=Theta(sqrt r)`, this is

\[
                         \Omega(r^{3/2})=\Omega(kd).        \tag{5.4}

\]

#### Proof

Apply Theorem 2.2 to each disjoint marked block.  Under sharing, partition
the cyclic factor components into intercut arcs.  An arc shorter than the
shield aperture cannot furnish a full-union prefix and suffix.  Summing the
arc-length lower bounds gives (5.3).  \(\square\)

The component-load-seven theorem limits the number of cuts on one PBBS
component but does not change this aperture.  Even one pentagon has five
cut sides and needs `Omega(r)` shield support; a fixed number of pentagons
is still not an `O(d)` local packet.

## 6. Typed-cap consequence

A linear rotor shield introduces `Theta(r)` owner/facet occurrences and an
opened shield exports `Theta(d)` residence state.  A typed-cap theorem must
therefore route a linear occurrence bank, or prove that those shield
occurrences are cap-inert.  The rank-three common-history cell bijection
does not supply either conclusion.

The linear shield scale does **not** by itself contradict an additive word
bound: these are internal carrier occurrences rather than appended word
positions.  It does show that the existing `O(d)` protected-packet and
bounded typed-interface theorems cannot absorb the shield for free.

## 7. Exact surviving alternatives

The directional full-union route has the following proof-safe status.

* `O(d)` support is impossible for a context-free shielded pentagon.
* `Theta(r)` support per fixed cut is necessary and sufficient before
  rooted factor/cap planting.
* `Theta(Hr)` marked support is the natural scale for the full height
  ladder.
* A shield placed outside a depth-`d` collar leaves the transition band
  (3.4), so it does not combine with the present short-deck theorem without
  another witness construction.

Therefore one must choose between:

1. a genuinely global `Theta(Hr)` protected shield-and-cap theorem,
   together with transport across the transition bands;
2. a PBBS-specific alternate-corridor theorem for the complete exterior
   current; or
3. a non-bijective upper absorber which avoids context-free full-union
   saturation.

No `B(k)+O(1)` conclusion is claimed.

## 8. Dependencies

The abstract full-union localization and sharp Johnson shield are in

`MATH_THEOREM_FULL_UNION_SHIELDS_LOCALIZE_ALL_EXTERIOR_SPLICE_DAMAGE_20260805.md`.

The sharp resident rotor and its source antecedent are in

`MATH_THEOREM_CYCLIC_WINDOW_FULL_UNION_SHIELD_ROTORS_20260805.md`.

The sharp opening collar is in

`MATH_THEOREM_ROOTED_ROTOR_OPENING_RESIDENCE_COLLAR_AND_C8_GRAFT_GATE_20260805.md`.

The rank-three pentagon screen decomposition is in

`MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`.
