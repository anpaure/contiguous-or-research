# The frozen top-shadow gate regenerates from a rainbow-factor sidecar

Date: 2026-08-01  
Lane: same-parity Pascal regeneration of the immediate lower shadow  
Status: exact q1 theorem and exact finite state-insufficiency witness.  The
result isolates a sufficient regenerative sidecar.  It does not prove that
the four-sector child has the required rainbow cyclic braid, residence,
upper support, or a common-cap compiler.

## 0. Outcome

For an odd middle layer, a q1-rainbow two-factor has exactly one occurrence
of every immediate lower colour.  Opening its components and joining the
resulting paths has a completely transparent q1 ledger:

\[
 \boxed{\text{holes}=\{\text{cut colours}\}
                   \setminus\operatorname{supp}\{\text{seam colours}\}.}
 \tag{0.1}
\]

Consequently, if all but at most `eta` of the **interior** cut colours are
recycled by seams, then the frozen boundary-bank deficiency of the final
path is at most `eta` as soon as `d>=eta+2`.  The two unrecycled outer cut
colours cost nothing: each is contained in its own global endpoint.

This gives an exact same-parity reset rule.  A one-hole path whose hole lies
in both endpoints closes to a q1-rainbow Hamilton cycle.  If the cyclic
four-sector Pascal braid has injective q1 colours, opening one child edge
again gives precisely the state

\[
                 (z,\ell,\rho,b)=(0,0,0,1),
                 \qquad \delta_{\rm top}=0.             \tag{0.2}
\]

Thus the q1 frozen Hall gate can regenerate **exactly**; it need not
accumulate under `k -> k+2`.  The missing input is not another scalar
inequality.  It is a cyclic rainbow-factor/opening sidecar, or more
generally a cut-colour recycling certificate.

The four counts `(z,ell,rho,b)` alone do not encode that sidecar.  Two
explicit Hamilton paths in `J(5,3)` have the identical state
`(0,1,1,0)` and `delta_top=0`; one is obtained by splicing two q1-rainbow
cycles and the other admits no inverse of this one-seam form.  Hence no
regeneration theorem may silently infer factor recoverability from the
frozen Hall state.

## 1. Rainbow factor openings

Let

\[
 k=2r-1,\qquad W={k\choose r}={k\choose r-1},
\]

and let `F` be a spanning simple two-factor in `J(k,r)`.  Give an edge
`XY` its immediate lower colour

\[
                         \chi(XY)=X\cap Y.             \tag{1.1}
\]

Assume that `chi` is a bijection from `E(F)` to
`binom([k],r-1)`.  Call such an `F` **q1-rainbow**.

Write the components in an order `C_1,...,C_c`.  In component `C_i`, cut
one edge of colour `q_i`, orient the resulting path as `P_i`, and write its
first and last vertices as `a_i,b_i`.  Thus

\[
                         q_i\subset a_i\cap b_i.       \tag{1.2}
\]

For `1<=i<c`, join `b_i` to `a_(i+1)` by a Johnson seam of colour

\[
                         s_i=b_i\cap a_{i+1}.          \tag{1.3}
\]

The concatenation is a spanning Johnson path `T`.

### Theorem 1.1 (exact cut/seam palette ledger)

The natural q1-hole set of `T` is

\[
 \boxed{
  \mathcal H_1(T)=
  \{q_1,\ldots,q_c\}\setminus
  \operatorname{supp}\{s_1,\ldots,s_{c-1}\}.}
 \tag{1.4}
\]

#### Proof

The factor contains every colour exactly once.  Cutting removes exactly the
distinct colours `q_i`; no other old occurrence changes.  The only new
q1 occurrences are the seam colours `s_i`.  Therefore a cut colour remains
missing exactly when no seam reinstalls it.  Every non-cut colour retains
its old occurrence, whether or not a seam duplicates it.  This is (1.4).
\(\square\)

Define the **interior cut-colour recycling defect** of this ordered splice by

\[
 \eta(T;F)=
 \left|\{q_2,\ldots,q_{c-1}\}
       \setminus\operatorname{supp}\{s_1,\ldots,s_{c-1}\}\right|.
 \tag{1.5}
\]

The set in (1.5) is empty when `c<=2`.

### Theorem 1.2 (frozen Hall deficiency is paid only by interior debt)

If `d>=eta(T;F)+2`, then

\[
                         \boxed{\delta_{\rm top}(T)
                                  \le \eta(T;F).}       \tag{1.6}
\]

In particular, recycling every interior cut colour gives
`delta_top(T)=0`, independently of the number of factor components.

#### Proof

By (1.2), an unrecycled `q_1` lies in the global left endpoint `a_1`, and
an unrecycled `q_c` lies in the global right endpoint `b_c`.  Hence every
hole in class `Z` is one of the unrecycled interior cut colours, so

\[
                              z\le\eta.                \tag{1.7}
\]

Equation (1.4) also gives

\[
                         z+\ell+\rho+b\le\eta+2\le d.  \tag{1.8}
\]

Thus neither endpoint bank overflows: in the notation of the frozen
boundary theorem, `u_L=ell`, `u_R=rho`, and

\[
                    2d-u_L-u_R\ge d\ge b.
\]

Substitution in the exact formula

\[
 \delta_{\rm top}
 =z+\ell+\rho+b-u_L-u_R
     -\min\{b,2d-u_L-u_R\}
\]

gives `delta_top=z<=eta`.  \(\square\)

This theorem is stronger than a component-count bound.  A factor may have
many components; what matters is whether its seams transport their deleted
colours.  Conversely, merely joining all components is insufficient if the
seams duplicate unrelated retained colours.

## 1A. The raw two-tag lift is not regenerative

The factor sidecar is necessary even at the level of endpoint classes.
Consider the raw fixed-tag part of an odd-to-odd lift, with new coordinates
`x,y`, whose inherited tagged q1 occurrences are exactly

\[
 x+\mathcal J_1(T),\qquad y+\mathcal J_1(T),           \tag{1A.1}
\]

and whose global endpoints are `x+T_0` on the left and
`y+T_(W-1)` on the right.  Assume no cross-sector seam has yet supplied an
inherited tagged hole.

### Theorem 1A.1 (exact raw endpoint-state recurrence)

The two tagged copies of the parent holes contribute the child endpoint
state

\[
 \boxed{
 (z^+,\ell^+,\rho^+,b^+)
   =(2z+\ell+\rho,\ \ell+b,\ \rho+b,\ 0).}
 \tag{1A.2}
\]

In particular

\[
                         \delta_{\rm top}^{+}
                         \ge 2z+\ell+\rho.             \tag{1A.3}
\]

#### Proof

If `Q` is in parent class Z, neither `x+Q` nor `y+Q` lies in its
same-tag child endpoint, and a set with tag `x` cannot lie in the endpoint
with tag `y`, or conversely.  It gives two Z holes.  A parent L hole gives
`x+Q` in class L and `y+Q` in class Z.  A parent R hole gives one Z and one
R.  A parent B hole gives one L and one R.  Summing gives (1A.2).  Every Z
hole contributes one unit to the exact frozen boundary deficiency, proving
(1A.3).  \(\square\)

Starting from B1, repeated raw transport gives

\[
 (0,0,0,1)\longmapsto(0,1,1,0)
 \longmapsto(2,1,1,0)\longmapsto(6,1,1,0)\longmapsto\cdots,
 \tag{1A.4}
\]

with `z_n=2^n-2` after `n>=1` raw lifts.  Thus endpoint containment by
itself is not stable under Pascal tagging.  A regenerative lift must either
close the parent to its rainbow factor before lifting, or install at least
the companion tagged holes represented by the `2z+ell+rho` term.  The
cyclic reset below does the former; cross-sector q1 sockets may do the
latter.

## 2. The exact `B1 -> B1` Pascal reset

Call a Hamilton path `T=(T_0,...,T_(W-1))` a **B1 path** when

\[
                   (z,\ell,\rho,b)=(0,0,0,1).         \tag{2.1}
\]

### Lemma 2.1 (B1 closure equivalence)

Every B1 path closes, by adding its endpoint edge, to a q1-rainbow
Hamilton cycle.  Conversely, opening one edge of a q1-rainbow Hamilton
cycle gives a B1 path.

#### Proof

A Hamilton path has `W-1` q1 occurrences.  A B1 path has support size
`W-1`, because it misses exactly one of the `W` target colours.  Therefore
its path-edge colours are all distinct.  Let `Q` be the missing colour.
The B condition says `Q subset T_0 intersection T_(W-1)`.  The endpoints
are distinct rank-`r` sets, so their intersection has rank at most `r-1`;
containing the rank-`r-1` set `Q` forces equality.  Hence the endpoint edge
is Johnson and has colour `Q`.  Adding it completes the palette exactly.

The converse deletes one uniquely coloured edge.  Its two endpoint owners
both contain that colour, so the sole hole belongs to class B.  \(\square\)

Now use the cyclic form of the component-neutral four-sector Pascal braid.
Its four q1-signature banks have sizes

\[
 {2r-1\choose r-2},\quad
 {2r-1\choose r-1},\quad
 {2r-1\choose r-1},\quad
 {2r-1\choose r},                                  \tag{2.2}
\]

and the cyclic slot ledger has exactly these same sizes.  The conditional
gate is that the occurrence-labelled colours in all four banks are
injective.  Under that gate the cyclic child is q1-rainbow.

### Theorem 2.2 (same-parity top-shadow reset)

Let a B1 parent path close as in Lemma 2.1.  Assume this q1-rainbow parent
cycle satisfies the owner-level hypotheses of the cyclic four-sector Pascal
braid, and assume the child braid has injective q1 colours.  Open any one
child edge.  Then the child path is again B1 and

\[
                         \delta_{\rm top}^{+}=0.       \tag{2.3}
\]

In particular the parent's missing colour does not branch into two child
holes.  If its colour is `Q`, closing the parent supplies the edge whose two
fixed-tag images carry `x+Q` and `y+Q`; the cyclic child palette contains
both.  The only child hole is the newly opened child-edge colour.

#### Proof

Lemma 2.1 supplies the q1-rainbow cyclic parent required by the Pascal
factor construction.  Injectivity plus the cyclic slot count makes the
child a q1-rainbow Hamilton cycle.  Applying the converse direction of
Lemma 2.1 to any opened child edge proves (2.3).  The fixed-tag statement is
the `x`- and `y`-signature part of the four-sector edge ledger.  \(\square\)

Thus, at q1, the same-parity induction has a genuinely closed one-state
automaton:

\[
                              B1\longmapsto B1.        \tag{2.4}
\]

The hard condition is the cyclic occurrence-labelled injectivity, not the
frozen endpoint Hall arithmetic.

### Corollary 2.3 (q1 alone has an unconditional all-dimensional reset)

For every odd `k=2r-1`, there exists a B1 Hamilton path in `J(k,r)`.

#### Proof

Apply the Middle Levels Theorem to the bipartite graph induced by ranks
`r-1` and `r` of the Boolean lattice on `[2r-1]`.  Write its Hamilton cycle
alternately as

\[
 T_0,X_0,T_1,X_1,\ldots,T_{W-1},X_{W-1},T_0,
 \]

where the `T_i` have rank `r` and the `X_i` rank `r-1`.  Necessarily
`X_i=T_i intersection T_(i+1)`.  Projecting onto the `T_i` therefore gives
a q1-rainbow Hamilton cycle in `J(k,r)`.  Open any edge and invoke
Lemma 2.1.  \(\square\)

So the q1 frozen Hall condition is not an abstract existence obstruction.
The remaining correlated question is whether a B1 cycle/path can be chosen
inside the same Pascal, residence, upper-witness and common-cap fibre needed
by the rest of the construction.

## 3. Bounded recurrence with a factor-opening sidecar

For a q1-rainbow factor `F`, let

\[
 \eta_*(F)=\min \eta(T;F),                            \tag{3.1}
\]

where the minimum runs over all choices of cuts, component orderings,
orientations, and legal Johnson seams.  This is an occurrence-labelled
quantity; it is not determined by the number of components.

### Corollary 3.1 (bounded q1 regenerative sidecar)

Suppose a same-parity Pascal construction maps a q1-rainbow factor sidecar
`F_k` to a q1-rainbow factor sidecar `F_(k+2)` and, for one absolute `C`,

\[
                          \eta_*(F_{k+2})\le C          \tag{3.2}
\]

at every sufficiently large step.  Then the opened child can be chosen with

\[
                          \delta_{\rm top}(T_{k+2})\le C.
 \tag{3.3}
\]

If `eta_*=0`, the frozen q1 gate regenerates with zero deficiency.

#### Proof

For large enough `k`, `d(k+2)>=C+2`.  Apply Theorem 1.2 to a minimizing
splice.  The finitely many smaller dimensions are absorbed into the base
family.  \(\square\)

This is the desired bounded recurrence, but on the correct state:

\[
       \text{rainbow factor} + \text{opening/splice certificate},
 \tag{3.4}
\]

not on `(z,ell,rho,b)` alone.

### Corollary 3.2 (the fresh-q1 transporter realizes the two free ends)

Assume the splice recycles every interior cut colour, so its only possible
holes are `q_1` and `q_c`.  Prepare at the two global endpoint collars two
disjoint relabelled copies of the fresh-q1 endpoint transporter from
`MATH_THEOREM_REBASED_SERIAL_EXTERIOR_EAR_CONTRACTION_20260801.md`,
Corollary 2.6.  If the selected alternatives in their length-`d` cells are
`q_1` and `q_c`, respectively, then both outer holes have a simultaneous
physical q1 assignment while the declared q>=2 nested endpoint chains are
transported exactly.

#### Proof

In one transporter the two antecedents have the same depth-`d` carrier and
agree again at prefix length `d+1`.  Their prefixes of lengths below `d`
are the prescribed paired deeper chain, while their length-`d` values are a
fresh pair of endpoint-contained q1 facets.  Coordinate relabelling selects
the desired endpoint facet.  Use the construction itself at the left end
and its reversal at the right end.  The two physical banks are disjoint, so
the two q1 assignments do not compete.  The explicit prefix identities give
the simultaneous q>=2 transport.  \(\square\)

This closes the **local endpoint part** of the rainbow-sidecar reset: the
two colours which Theorem 1.2 declares free can be carried by actual
antecedents without duplicating the packet's native q1 palette.  It does not
construct the factor splice, recycle an interior cut colour, or prove the
remaining common-cap matching.

## 4. The four endpoint counts are not regenerative data

The insufficiency already occurs in `J(5,3)`, where `W=10` and `d=2`.
Use coordinates `1,...,5` and consider the two Hamilton paths

\[
\begin{aligned}
T_{\rm good}={}&
123,125,145,124,234,345,134,135,235,245,\\
T_{\rm bad}={}&
145,134,345,135,125,245,235,234,124,123.
\end{aligned}                                           \tag{4.1}
\]

Both have endpoint state

\[
                         (z,\ell,\rho,b)=(0,1,1,0),
                         \qquad\delta_{\rm top}=0.     \tag{4.2}
\]

For `T_good`, the holes are `23` and `45`, and the repeated colour is
`34`.  Delete the edge

\[
                         234-345                       \tag{4.3}
\]

of colour `34`.  Closing the left piece by `123-234` installs `23`, and
closing the right piece by `345-245` installs `45`.  The result is two
five-cycles whose ten edge colours are the ten pairs exactly once.

For `T_bad`, the holes are `45` and `13`, and the repeated colour is `25`.
Its two occurrences are

\[
                         125-245,qquad245-235.         \tag{4.4}
\]

Deleting the first does not permit the required two Johnson closures.
Deleting the second closes the left piece with colour `45`, but the right
closure has colour `23`, not the missing `13`.  Deleting any uniquely
coloured edge necessarily creates another hole.  Therefore no deletion of
one path edge followed by closure of the two pieces gives a q1-rainbow
two-factor.

### Proposition 4.1 (state-insufficiency no-go)

The state `(z,ell,rho,b)`, even together with `delta_top`, does not determine
whether a path carries the one-seam inverse needed to recover a q1-rainbow
factor.  Therefore a Pascal recurrence based only on those scalars cannot
invoke the rainbow-factor reset of Theorem 2.2 without an additional
occurrence-labelled sidecar.

This is not a no-go for a more global repair of `T_bad`, and it is not a
no-go for same-parity Pascal induction.  It is an exact warning about the
minimum sufficient state.

## 5. Consequence for the current programme

The frozen boundary theorem and the present result fit together as follows.

1. Current coatom packets cannot alter `delta_top` inside one safe fibre.
2. A cyclic q1-rainbow Pascal braid resets the gate before those packets are
   used: open one edge and obtain B1 with `delta_top=0`.
3. More generally, a q1-rainbow child factor with bounded interior
   cut-colour recycling defect gives bounded `delta_top`.
4. The correct exported q1 sidecar is therefore a cyclic factor plus an
   opening/splice certificate.  The four endpoint counts are a terminal
   audit of that certificate, not a regenerative state by themselves.

The exact remaining q1 theorem is now sharply stated:

> **Cyclic palette regeneration.**  Produce the cyclic four-sector child
> with injective occurrence-labelled q1 colours, or produce a q1-rainbow
> child factor whose interior cut-colour recycling defect is `O(1)`.

This target is strictly weaker than the full Shadow--Braid theorem.  It says
nothing about residence, arbitrary-width upper witnesses, or common-cap
compilation, but it removes the frozen top-shadow gate from the induction.

## 6. Replay

Run

```text
python3 scratch/audit_top_shadow_pascal_rainbow_sidecar_20260801.py
```

which writes

```text
scratch/top_shadow_pascal_rainbow_sidecar_20260801.audit.json
```

with expected status

```text
PASS_TOP_SHADOW_PASCAL_RAINBOW_SIDECAR
```

The replay verifies both `J(5,3)` Hamilton paths, their identical state and
zero frozen deficiency, the unique two-cycle recovery of `T_good`, and the
exhaustive absence of a one-cut/two-closure recovery for `T_bad`.
