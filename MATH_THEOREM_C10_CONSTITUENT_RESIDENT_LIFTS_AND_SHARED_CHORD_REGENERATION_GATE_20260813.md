# Both constituent `C6`s of the rigid `C10` have resident witness-rematerializing lifts, but the lifts do not compose automatically

**Date:** 2026-08-13  
**Status:** unconditional identification with the existing resident
three-port theorem, followed by an exact non-composition audit  
**Input:** the `C10` of
`MATH_THEOREM_GK_RIGID_PALETTE_NEUTRAL_C10_FUSION_20260813.md`

## 1. Outcome

Put `n=2m+1`.  The palette-neutral decagon factors as

\[
 \{e_1,e_2,e_3\}\to\{n_2,n_3,c\},\qquad
 \{e_0,e_4,c\}\to\{n_0,n_1,n_4\},                \tag{1.1}
\]

where `c=A_3B_1`.

Each arrow in `(1.1)` is not merely a simple alternating `C6`: after a
cyclic relabelling it is exactly the clean three-port normal form to which
the existing resident q-port and hybrid common-history theorems apply.
Consequently, **each phase separately** has a zero-length-charge
`6d+6`-owner prospective lift which

* is positively resident through depth `d`;
* transports every strict-lower occurrence and its compiler address;
* preserves both immediate palettes; and
* rematerializes every old internal cyclic upper-deck target in the fused
  state.

This includes the second phase through the globally singleton rigid edge
`e_0`.

However, the two resident lifts cannot simply be applied serially.  In the
first fused lift the new chord `A_3->B_1` continues along the old port-`e_1`
return rail `B_1 leadsto A_1`; the second lift requires it to close along a
different return rail `B_1 leadsto A_3`.  Moreover the first phase already
puts `c` and `e_4` in one fused component.  Thus its output is not the
three-port input state required by the second resident theorem.

The missing statement is a **compound resident decagon converter** (or a
regeneration move between the phases), not coordinate supply or immediate
palette algebra.

## 2. First clean phase

Let

\[
 K^{(1)}=L_1\cap L_2\cap L_3
 =\{0\}\cup\{m,m+1,\ldots,2m-3\}.                 \tag{2.1}
\]

It has rank `m-1`.  Put

\[
 z=m-1,qquad
 (a_0,a_1,a_2)=(2m-2,2m-1,1).                    \tag{2.2}
\]

Use the cyclic port order

\[
                         (e_1,e_3,e_2).            \tag{2.3}
\]

Then, writing `Q_i` for the corresponding `A` endpoint and `P_i` for its
`B` endpoint,

\[
 Q_i=K^{(1)}+z+a_i,qquad
 P_i=K^{(1)}+a_i+a_{i+1}.                         \tag{2.4}
\]

The old direct shore is `Q_iP_i`.  The fused direct shore
`Q_iP_(i-1)` is respectively

\[
                         n_2,quad c,quad n_3.     \tag{2.5}
\]

Thus the first arrow in `(1.1)` is literally the `q=3` resident-port
fusion, with only the standard cyclic index reversal.

## 3. Second clean phase

Similarly,

\[
 K^{(2)}=L_0\cap L_4\cap L_3
 =\{m,m+1,\ldots,2m-3\}\cup\{2m-1\}.             \tag{3.1}
\]

Put

\[
 z=m-1,qquad
 (b_0,b_1,b_2)=(2m-2,2m,0),                       \tag{3.2}
\]

and use port order

\[
                         (e_0,e_4,c).              \tag{3.3}
\]

The `A` endpoints and the other endpoints obey

\[
 Q_i=K^{(2)}+z+b_i,qquad
 P_i=K^{(2)}+b_i+b_{i+1}.                         \tag{3.4}
\]

Now `Q_iP_(i-1)` is respectively

\[
                         n_1,quad n_0,quad n_4.   \tag{3.5}
\]

This is exactly the second arrow in `(1.1)`.

## 4. What the existing resident theorem gives

The owner rank in the resident theorem is `r=m+1`, and both cores above
have rank `r-2=m-1`.  Its coordinate condition is

\[
                         r\ge d+3,
 \quad\text{equivalently}\quad d\le m-2.          \tag{4.1}
\]

Under `(4.1)`, choose `d` deleted coordinates in the appropriate core,
retain one anchor, and choose `d` fresh rail coordinates.  The theorem
attaches one return rail `P_i leadsto Q_i` at every port.  It gives three
old resident cycles `H_2`, one fused resident cycle `H_3`, and

\[
             \operatorname {Deck}_{\rm cyc}(H_2)
             \subseteq
             \operatorname {Deck}_{\rm cyc}(H_3).             \tag{4.2}
\]

The hybrid-source theorem supplies the same packet with a literal
depth-`d` source and an occurrence-bijective strict-lower transport.  Thus
`(4.2)` and lower/compiler transport concern one physical packet, not two
incompatible existential lifts.

For the target OR-word depth on odd ground, `(4.1)` holds from the first
nontrivial decagon range onward; asymptotically it has linear room because
`d=Theta(sqrt(m))`.

The support conclusion is deliberately internal: it rematerializes an old
target whose chosen cyclic interval lies wholly inside the displayed
resident port cycles.  It does not preserve an arbitrary PBBS fan interval
which enters an uncontrolled exterior or crosses the final linear cut.

## 5. Exact serial non-composition

Denote a resident return rail only by its endpoints.  Phase one begins with

\[
 B_1\leadsto A_1,qquad
 B_3\leadsto A_3,qquad
 B_2\leadsto A_2.                                  \tag{5.1}
\]

After its direct fusion, the chord is oriented

\[
                         A_3\longrightarrow B_1.   \tag{5.2}
\]

It is followed in the fused cycle by the already installed rail

\[
                         B_1\leadsto A_1.           \tag{5.3}
\]

Phase two, by contrast, requires its three **old resident port cycles** to
contain

\[
 B_0\leadsto A_0,qquad
 B_4\leadsto A_4,qquad
 B_1\leadsto A_3.                                  \tag{5.4}
\]

In particular the chord in `(5.2)` must be followed by the last rail in
`(5.4)`, closing back at `A_3`.  Since `A_1!=A_3`, `(5.3)` and `(5.4)`
are distinct successor requirements at the same occurrence `B_1`.
They cannot coexist in a degree-two occurrence factor.

There is a second view of the same obstruction.  The first C6 fuses the
three old components carrying `e_1,e_2,e_3`; the component carrying `e_1`
also contains `e_4`.  Therefore, after phase one, `c` and `e_4` already lie
in one component, while `e_0` lies in another.  The second native C6 is
topologically neutral on those two components; it is not a three-to-one
resident-port fusion state.

This is exactly the regeneration qualification in the resident hybrid
theorem: a fused `H_3` output is not automatically a fresh `H_2` bank for
the next move.

## 6. Coordinate supply is not the obstruction

The two cores overlap in

\[
 I=\{m,m+1,\ldots,2m-3\},\qquad |I|=m-2.          \tag{6.1}
\]

Their combined active/core support leaves the common fresh interval

\[
                         \{2,3,\ldots,m-2\},       \tag{6.2}
\]

of size `m-3`.  Hence, under the slightly stronger `d<=m-3`, both phases
can use common deleted coordinates inside `I` and a common fresh bank in
`(6.2)`.  This aligns their histories as far as scalar coordinate supply
permits.  It does not change the conflicting successor requirements
`(5.3)`--`(5.4)`.

Thus the sharp next local theorem is:

> **Compound resident `C10` converter.**  On one common occurrence bank,
> realize the two palette/q2-exact hexagonal phases and their cancelling
> chord while transporting the first fused continuation into the second
> three-port input, with final internal cyclic-deck support containing the
> initial deck.

An equivalent escape is a bounded resident regeneration gadget inserted
between the two phases.  Neither statement is supplied by the current
q-port theorem.

## 7. Consequence for the gap-nine obstruction

The individual phase-two lift proves that a forced singleton upper colour
is not intrinsically incompatible with residence: after prospectively
replacing its local exterior by resident rails, the rigid direct edge can
be moved without losing the internal cyclic deck.

It does **not** yet repair the six-edge gap-nine collar obstruction.  That
obstruction concerns six particular unique PBBS fibres and the complete
old flagged bank; the present decagon touches one rigid singleton edge and
protects only its displayed internal resident packet.  A successful global
PBBS rethread must still plant replacement-enabled packets on a transversal
of all short forced collars and then solve their joint host/regeneration
problem.

