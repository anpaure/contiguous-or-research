# The terminal MNW q2 cylinder is one carried B8 relay

**Date:** 2026-08-07  
**Method:** exact Dyck-context decomposition and incidence-circulation
transport; no search  
**Status:** unconditional in the Boolean incidence-cycle lattice.  A literal
factor switch follows from the already isolated prepared-prism hypotheses;
those host hypotheses are not proved here.

## 1. Statement

Write

\[
 B_8=11101101,
 \qquad D=1011101101=10\,B_8.
\]

The signed gamma--alpha relay in the MNW hypertree fills the cylinder
`1110101101v` and transports its unique q2 hole to

\[
                         Dv=10\,B_8v.                 \tag{1.1}
\]

Let `Z_B` be the four-hex incidence circulation which, in the canonical
semilength-four MSW factor, repairs `B8` without deleting any previously
represented q2 target.  For every Dyck suffix `v`, the desired second relay
is the copy of `Z_B` in positive prefix context `10` and suffix context
`U(v)`.

The canonical MSW concatenation instead presents the same base packet in
the down-set context `01`.  Since

\[
                         01\longleftrightarrow10       \tag{1.2}
\]

is one Johnson context move, the difference between these two copies is a
sum of at most twenty-four transport hexagons.  Hence the remaining q2
cylinder has a uniform, suffix-compatible, constant-size algebraic relay.

## 2. Why the natural context is `01`

For a Dyck prefix `W`, a base block `X`, and a Dyck suffix `v`, every owner,
colour, and turn in the `X` portion of the canonical MSW path rooted at
`WXv` has common context

\[
                         D(W)\cup U(v),               \tag{2.1}
\]

where `D(W)` is the set of down-step positions of `W` and `U(v)` the set of
up-step positions of `v`.

Take `W=10`.  Its down-set is the second prefix coordinate, so (2.1) is the
bit context `01` together with `U(v)`.  Thus the canonical packet is

\[
                         (Z_B)_{01,U(v)}.              \tag{2.2}
\]

The terminal hole (1.1), however, uses the first prefix coordinate and is
therefore the positive-context target of

\[
                         (Z_B)_{10,U(v)}.              \tag{2.3}
\]

This is a context mismatch, not a new base relay problem.

## 3. Exact incidence-lattice carry

Every alternating incidence hexagon is a signed circulation.  The four-hex
`B8` macro is therefore a circulation

\[
                         Z_B=H_0+H_1+H_2+H_3.          \tag{3.1}
\]

Before cancellation, (3.1) has twenty-four signed incidence occurrences.
Apply the context-transport theorem to the one Johnson move (1.2), with the
suffix up-set `U(v)` held fixed.  It gives

\[
 \boxed{
 (Z_B)_{10,U(v)}-(Z_B)_{01,U(v)}
       =-\sum_{e\in Z_B}\epsilon_e H_e^{01\to10}.}    \tag{3.2}
\]

The right side uses at most twenty-four transport hexagons; exact
cancellation in (3.1) can only reduce this number.  The bound is independent
of the ambient semilength and of `v`.

Because different Dyck suffixes have different fixed up-sets, projection to
the suffix coordinates separates their base packets and their transport
prisms.  Thus (3.2) tensors simultaneously over every
`v in D_(m-5)`.

## 4. q2 consequence under a prepared prism

Assume the transport annulus for (3.2) is planted with the hypotheses of
the alternating-annulus and turn-faithful carry lemmas:

1. **Current-state boundary phase:** after the gamma--alpha relay, the
   `01` copy of every old `B8` incidence is selected and the `10` copy is
   unselected (or the globally reversed phase), exactly as required by the
   alternating-annulus sweep; this is a statement about the current
   rethreaded factor, not only the canonical product;
2. the transport faces can be swept alternately;
3. the untouched second colour at every affected owner is the corresponding
   contextual copy of the base colour;
4. the contextual copies of the two untouched spare-provider turns for the
   base negative targets are present and remain untouched throughout the
   sweep;
5. the auxiliary rails preserve the component interface and avoid the
   protected stem bank.

Then toggling the canonical down-context `B8` relay and sweeping (3.2)
conjugates it to the positive-context copy.  Its positive q2 term is

\[
                         10\,B_8v=Dv.                 \tag{4.1}
\]

The original four-hex relay is support-closed: its two negative targets
have spare providers.  Items 3--4 make those literal spare occurrences,
not merely their target names, survive the carry.  Hence, under the five
host hypotheses, the second relay fills every terminal
`Dv` hole without opening another q2 hole.

Combining it with the proved mirror-gamma plus `alpha(1100)` relay gives a
closed two-stage q2 repair of the entire `1110101101v` cylinder.

There is no hidden collision between the two signed ledgers.  In ordinary
bit notation the positive-context copy of the four-hex current is

\[
 +[1011101101]+[1011010111]
 -[1011100111]-[1010111110].                         \tag{4.2}
\]

The first gamma--alpha relay changes only

\[
1110101101,\ 1011011101,\ 1110011101,\
1011101101,\ 1110011110.                             \tag{4.3}
\]

Thus the only common target of (4.2) and (4.3) is `D`, negative in the
first relay and positive in the second.  In particular the first relay
does not consume either spare provider used by the two negative terms of
the carried four-hex relay.

At the root-support level the two base banks are separated as well.  Every
root of the first relay begins with `11`: this is immediate for
`alpha(1100)`, and a mirror-wrapped Dyck root begins with `11` because the
old root ends in `0`.  Every natural down-context root of the second relay
is `10x`, with `x` one of the six semilength-four roots.  Hence the two base
packet banks are disjoint before the auxiliary transport rails are added.
Possible collisions involving those rails remain part of the prepared-
prism hypothesis.

## 5. Why cyclic rotation alone is not a proof

The word `D` is also a cyclic coordinate rotation of `B8 10`.  This does
not justify importing the four-hex packet directly.  A global coordinate
permutation sends the whole canonical factor to an isomorphic factor; it
does not certify that the rotated old incidences are selected in the
original factor.  Independent per-component rotations are forbidden by
the MSW cut-rigidity theorem.

Equation (3.2) is the valid replacement for that tempting shortcut.  It
identifies the exact alternating faces needed to move between the two
contexts and records the remaining physical premise explicitly.

## 6. Remaining gate

The q2 target algebra and the suffix-compatible constant bound are now
closed.  What is not closed is the literal prepared-prism host.  The exact
remaining statement is:

> **One-prefix prepared-prism lemma.**  The standard relay hypertree can be
> chosen so that, in the factor state *after* the gamma--alpha relay and for
> every suffix fibre, the `01` and `10` copies of the four-hex `B8`
> circulation, the two named spare-provider turns, and their transport rails
> satisfy the five host hypotheses in Section 4, simultaneously and without
> losing the protected pivot bank.

This is strictly smaller than an arbitrary counter-carry theorem: the
context path has length one and the base circulation is one fixed four-hex
macro.
