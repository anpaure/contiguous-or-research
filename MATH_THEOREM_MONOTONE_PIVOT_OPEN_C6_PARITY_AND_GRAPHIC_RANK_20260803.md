# Monotone-pivot opening and the exact C6 parity/graphic-rank boundary

**Date:** 2026-08-03  
**Status:** unconditional abstract factor topology.  This note determines
exactly what opening one factor component changes.  It does not assert that
the required Boolean `C6`, `C4`, `C8`, or open ear is present with the
literal upper, residence, and compiler guards.

## 1. Opening does not change component parity

Let a bipartite spanning two-factor be written as the union of perfect
matchings

\[
                              F=A\cup B.
\]

Let `omega` be one edge of `F`.  The opened factor

\[
                              F^\circ=F-\omega
\]

has one path component in place of the cycle containing `omega`, and all
other components remain cycles.  In particular

\[
                              c(F^\circ)=c(F).            \tag{1.1}
\]

An alternating `C_(2t)` exchange replaces `t` edges of one matching by the
opposite alternating phase.  On the shore identified through `A`, this
composes the factor permutation `A^(-1)B` with a `t`-cycle.  Therefore

\[
                   c(F')-c(F)\equiv t-1\pmod 2.           \tag{1.2}
\]

Indeed, for a permutation `pi` on `W` letters,

\[
                   \operatorname {sgn}(\pi)=(-1)^{W-c(\pi)},
\]

and a `t`-cycle has sign `(-1)^(t-1)`.

### Theorem 1.1 (opened-factor parity criterion)

Suppose an alternating `C_(2t)` is performed and one edge of the terminal
factor is then opened (possibly moving the opening from `omega` to a new
edge).  The number of components of the resulting path-plus-cycles factor
changes by parity `t-1`.

In particular, a `C6` has `t=3` and preserves component parity.  It can
reduce three components to one, but it cannot reduce two components to one.
A `C4` or `C8` has even `t` and has the required odd endpoint parity, if a
literal guarded realization exists.

#### Proof

Virtually restore the old opening before the exchange and virtually restore
the chosen terminal opening after it.  This compares the two closed
two-factors by the same alternating exchange.  Removing one edge from a
cycle turns it into a path without changing the number of connected
components.  Equation (1.2) therefore applies unchanged.  \(\square\)

This includes the apparently special punctured implementation.  If the old
opening `omega` is one of the three old `C6` edges, then deleting the other
two old edges and inserting all three new edges simply constructs the full
closed `C6` switch.  Deleting a new terminal opening afterward is still

\[
                         (F-D+D')-\omega'.                \tag{1.3}
\]

Thus a punctured closed `C6` does not acquire odd endpoint action merely
because one old edge was absent physically.

## 2. Exact graphic-rank accounting after an opening

The parity statement has a finer graphic form.  Let `J` be any spanning
maximum-degree-two graph having one distinguished path component and all
other components cycles.  Perform an equal-size exchange

\[
                         J'=J-D+A,
                         \qquad |D|=|A|=t,               \tag{2.1}
\]

with disjoint old and new edge sets.  Let `q` be the number of cyclic
components of `J` which meet `D`.  Contract every component of `J-D`, and
let

\[
                  \rho= r_{\rm gr/(J-D)}(A)              \tag{2.2}
\]

be the graphic rank of the new edges on this fragment quotient.

### Theorem 2.1 (opening-exchange rank identity)

One has

\[
       r_{\rm gr}(J')-r_{\rm gr}(J)=\rho-(t-q),           \tag{2.3}
\]

and equivalently

\[
       c(J)-c(J')=\rho-(t-q).                             \tag{2.4}
\]

#### Proof

Deleting `d_i>=1` edges from a cycle loses graphic rank `d_i-1`; the first
deletion merely destroys its unique cycle.  Deleting `d_i` edges from the
path loses rank `d_i`.  Summing over the `t` deletions gives rank loss
`t-q`.  By definition, adding `A` restores rank `rho`.  Since both graphs
are spanning, component reduction equals graphic-rank increase.  \(\square\)

Consequently, to absorb every one of the `q` hit cyclic components into the
anchor path in one exchange, it is necessary and sufficient that

\[
                              \rho=t.                    \tag{2.5}
\]

Thus the new edges must be a forest on the contracted path fragments.  This
is the exact test; component labels alone are insufficient.

## 3. What a C6 does after opening

There is one important positive face.  Suppose a `C6` deletes one edge from
the anchor path and one edge from each of two distinct cycle components.
After deletion there are four relevant fragments: the two halves of the
anchor path and one path from each broken cycle.  If the deleted edges are

\[
                    p_0q_0,\quad p_1q_1,\quad p_2q_2,
\]

with `p_0,q_0` on the two anchor halves and `p_i,q_i` on cycle fragment `i`,
the new cyclic phase may be written

\[
                    p_0q_2,\quad p_2q_1,\quad p_1q_0.     \tag{3.1}
\]

On the fragment quotient these are the three edges of the path

\[
        \text{anchor-left}-C_2-C_1-\text{anchor-right}.   \tag{3.2}
\]

Hence `rho=3`, `q=2`, and (2.4) gives

\[
                              c(J)-c(J')=2.               \tag{3.3}
\]

So an available `C6` is an exact **anchor path plus two cycles to one path**
merge.  Repeating such moves can absorb cyclic components two at a time.

It is not an anchor path plus one cycle merger.  In that case `q=1`; a
one-component result would require `rho=3` by (2.4), but Theorem 1.1 forbids
the resulting odd component change for a closed-phase `C6`.  Equivalently,
the physical `C6` stub rematching has rank at most two on that fragment
pattern.

Thus, if the opened factor initially has `c` total components, `C6` moves
alone can reach one component only when `c` is odd.  For even `c` they can
at best leave one anchor path and one cycle.  This includes the familiar
two-component final obstruction.

## 4. Exact stub-permutation test

For a completely general support, delete the switched edges and the virtual
anchor edge and contract all retained path interiors.  Let `alpha` be the
matching of stubs joined by those retained fragments, `rho` the old closure
matching, `beta` the new `C6` closure matching, and
`omega=(a^-a^+)` the virtual anchor closure.  On the touched support,

\[
 \begin{aligned}
   c_{\rm old}^{\rm closed}
     &=\tfrac12 c\bigl(\alpha(\rho\cup\{\omega\})\bigr),\\
   c_{\rm new}^{\rm closed}
     &=\tfrac12 c\bigl(\alpha(\beta\cup\{\omega\})\bigr).
                                                               \tag{4.1}
 \end{aligned}
\]

The terminal opened support is one path exactly when the second number in
(4.1) is one and the terminal opening lies on that cycle.  Formula (4.1) is
the proof-safe test when several cuts lie on the same old component; simply
counting which component ids are touched is not enough.

## 5. Consequence for the `B+1` monotone pivot

The monotone-pivot theorem supplies an extra literal cell, two compiler
rays, and (under its hypotheses) a safe flat owner aperture.  Those facts do
not by themselves change (1.2).  Even granting that the carrier is opened
at the pivot, a closed or punctured `C6` remains an even endpoint actuator.

Therefore the `+1` pivot eliminates the old parity gate only under one of
the following additional statements.

1. The starting opened factor has odd component count, and a sequence of
   literal guarded `C6` supports realizes the rank-three merge (3.2) until
   one path remains.
2. The pivot aperture supports a **genuinely open ear** whose virtual
   closure is not a closed `C6` `3`-cycle and whose endpoint action is odd.
3. A guarded odd actuator, for example an available `C4` or `C8` rectangle,
   performs the final parity change.

The first is a catalogue/packing theorem.  The second is a new local
geometry theorem.  The third still requires literal rectangle existence;
no clean physical rectangle may be assumed from the abstract parity count.

Hence the exact verdict is

\[
 \boxed{\text{opening turns a C6 into a two-cycles-at-a-time path merger,}
        \text{ but does not remove the final even-to-odd obstruction.}}
\]

