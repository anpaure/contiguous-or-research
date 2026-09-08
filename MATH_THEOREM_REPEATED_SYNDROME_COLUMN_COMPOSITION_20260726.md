# Repeated-syndrome-column composition: an exact conditional compiler

Date: 2026-07-26

## 0. Outcome

There is a clean local-to-global composition theorem behind the proposed
repeated-column compiler.  It gives perfectly balanced fibres of size
`r/b` without requiring a balanced Hamilton Gray code: an isometric
`C_(2b)` phase factor on the quotient already schedules every fibre twice
per quotient cycle.

The theorem requires a **full** local Latin direction array, defined on
both parity shores of its local context cube.  A parity-complete array
defined only on the global even shore does not automatically compose,
because the restriction of a global even context to one fibre may be odd.
This is the exact interface which a four-shore/full-predecessor primitive
must supply.

The augmented support code composes recursively.  Literal physical trace
decoding additionally requires a split-rail/status-cell embedding in which
the varied support is visible from the target; otherwise the old invisible
`J` error remains.

## 1. Full local arrays

Call `D:Q_n x Q_n -> [n]` a full Latin cycle array if

\[
 R_q(u)=u+e_{D(q,u)},\qquad C_u(q)=q+e_{D(q,u)}                 \tag{1.1}
\]

are neighbour permutations for every `q,u`, and every component of every
`R_q` is an isometric `C_(2n)` with a doubled-permutation direction word.

Assume also that its forward and reverse augmented codes

\[
 (q,u)\mapsto(J_k^\pm(q,u),q|_{J^c},u|_{J^c})                 \tag{1.2}
\]

are injective through depth `k<=K`.

## 2. Balanced phase composition

Let `r=bn`, with `b,n` even.  Partition the `r` coordinates into equal
fibres `C_1,...,C_b`, each of size `n`.  For `u in Q_r`, put

\[
 z_j(u)=|u\cap C_j|\pmod2.                                    \tag{2.1}
\]

Let `H` be any exact isometric `C_(2b)`-factor permutation of `Q_b`, with
direction function `lambda(z)`.  In each fibre install a full Latin cycle
array `D_j`.  Define

\[
 j=\lambda(z(u)),\qquad
 D(q,u)=(j,D_j(q|_{C_j},u|_{C_j})).                            \tag{2.2}
\]

### Theorem 2.1 (repeated-column composition)

The global row and column maps associated with (2.2) are neighbour
permutations.  Every global row component is an isometric `C_(2r)` whose
direction word is a permutation of all `r` coordinates followed by the
same permutation.

#### Proof

For fixed `u`, the quotient state `z(u)` fixes `j`.  The global column map
changes only `q|C_j` and is the product of the local bijection `C_{u_j}`
with identities on the other fibres; hence it is bijective.

For a row, toggling any coordinate in `C_j` toggles precisely quotient bit
`j`, so the quotient state advances under `H`.  Given a target row state,
its predecessor quotient state under `H` identifies the unique active
fibre, after which the local row bijection gives the unique predecessor.

One quotient cycle has `2b` steps and selects every fibre twice.  After
`k` quotient cycles, every local row has advanced `2k` steps.  The quotient
has returned, and all local states return for the first time exactly when
`k=n`; hence the global cycle length is `2bn=2r`.  During the first
`bn=r` moves, each local row advances `n` steps and uses every coordinate
of its fibre once.  Its next `n` local directions repeat, as does the
quotient word.  Thus the global word is doubled-permutation and isometric.
\(\square\)

Choosing `b` to be a power of two comparable to `log r` gives perfectly
balanced syndrome-column fibres of size

\[
                              n=Theta(r/log r).                  \tag{2.3}
\]

No balanced Hamilton cycle is needed; the quotient `C_(2b)` factor is the
balanced phase clock.

## 3. Trace composition

During any global `d`-window, the occurrences of one fibre are consecutive
steps in that fibre's local row.  Since the quotient direction word is a
permutation repeated periodically, every fibre occurs either

\[
                         \lfloor d/b\rfloor
 \quad\text{or}\quad    \lceil d/b\rceil                         \tag{3.1}
\]

times, up to one harmless endpoint convention.

### Theorem 3.1 (augmented-code recursion)

If all local augmented codes are injective through depth `K`, then the
global augmented code is injective through every depth `d` with

\[
                              \lceil d/b\rceil\le K.             \tag{3.2}
\]

The statement holds in both traversal orientations.

#### Proof

The global support `J` splits canonically as `J_j=J cap C_j`.  The exterior
context and row state restrict to the exterior data in each fibre.  The
directions in `J_j` are consecutive in local time, so the local decoder
recovers `(q|C_j,u|C_j)` independently in every touched fibre; untouched
fibres are already visible.  This recovers the full start.  Reverse
decoding uses the reverse local codes identically. \(\square\)

Iterating with `b(size)=Theta(log size)` reduces the protected local depth
by the product of the phase arities and reaches a constant-size primitive
rapidly.

## 4. Two non-negotiable interfaces

### 4.1 Parity-only arrays do not compose automatically

A global context `q` may be even while `q|C_j` is odd.  Therefore a local
array indexed only by even local contexts is undefined on a positive
fraction of the states in (2.2).  Normalizing each local parity by toggling
a distinguished bit introduces an unknown shore bit into trace recovery.
One needs either a full two-shore array as in Section 1 or a four-shore
predecessor theorem proving that the odd-row completion is again a row
permutation.

### 4.2 Literal support visibility

Theorem 3.1 decodes the augmented code containing `J`.  It becomes a
literal physical trace theorem in a pair-status cell where every active
rail is split: a lower target is empty exactly on varied rails and singleton
on untouched rails, while an upper target is full exactly on varied rails.
Thus `J` is intrinsic to either sign.

Without this split-cell hypothesis, an untouched empty/full rail is
indistinguishable from a completed rail of the corresponding sign, and
Theorem 3.1 must not be cited as literal shadow injectivity.

