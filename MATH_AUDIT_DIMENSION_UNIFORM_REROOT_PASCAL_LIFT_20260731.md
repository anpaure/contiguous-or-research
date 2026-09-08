# Referee audit: what endpoint rerooting proves uniformly, and what Pascal does not supply

Date: 2026-07-31  
Audited notes:

- `MATH_THEOREM_A_TWO_ENDPOINT_REROOT_RETIMING_AND_COMMONQ_SLACK_20260731.md`;
- `MATH_THEOREM_ENDPOINT_REROOT_INTERVAL_JOIN_PRESERVATION_20260731.md`;
- `MATH_THEOREM_AD_ENDPOINT_REROOT_SINGLETON_RETIMING_AND_ALO_COMMON_CAP_COMPILER_20260731.md`.

Verdict: the endpoint-join algebra, singleton contraction, maximal-cap
criterion, and ALO compiler are valid dimension-free **conditional**
theorems.  They turn a proposed construction into a short exact certificate.
They do not imply that the required cuts, schedule, pins, or common-cap cover
exist in every dimension.  The one-defect Pascal lift supplies exact middle
ownership and a sharply localized defect, but it does not supply the four
remaining existence assertions.

## 1. Statements that are genuinely dimension-free

The following implications use no special property of `k=16`.

1. Reversing independently oriented consecutive blocks preserves every
   interval join internal to a block.  Formula (2.3) of the semilattice note
   is the complete cross-block spectrum, in any join-semilattice.
2. A two-ended reroot changes exactly two *adjacency occurrences*, with the
   signed multiplicity ledger in Theorem A.1.1.  This does not mean that it
   changes exactly two distinct colours.
3. A reroot is a Johnson path iff its new seams are Johnson edges.  It is
   upper-complete iff the invariant internal banks plus its new seam ladders
   cover the desired upper family.  This is an exact verifier, not an
   existence theorem.
4. Once an uncapped maximal envelope is exact, a positional singleton cap is
   legal exactly when every affected row retains all its bits.  Moving one
   omitted deadline by `tau` costs exactly `tau` units of selected-prefix
   area, subject to order and schedule legality.
5. For a fixed schedule, Theorems AD.1.1 and AD.4.1 give the exact individual
   provider and simultaneous maximal-cap criteria.
6. The ALO-only formulation AD.5.1 is exact.  Cell capacity and target AMO
   are consequences of exact interval semantics, not extra constraints, when
   the target masks are distinct.
7. Exact middle rows transfer a consecutive-row upper witness to the physical
   word when the corresponding row intervals have connected union.  The
   convenient sufficient condition is

   ```text
   s_(i+1) <= d_i + 1
   ```

   for every adjacent pair used by the witness.

Thus the K16 proof is valid after its finite data are supplied.  What is not
dimension-free is the supply of those data.

## 2. Exact algebra of a one-defect Pascal source

Let `Omega` have size `2r-1`, let `z` be new, and write

\[
 P_i=D^{h-1}w_i\quad(0\le i\le N),\qquad
 Q_i=D^hw_i\quad(0\le i<N),
 \qquad N={2r-1\choose r}.
\]

There is an identity stronger than the ownership count:

\[
                     \boxed{Q_i=P_i\cup P_{i+1}.}       \tag{2.1}
\]

Assume the `Q_i` are all rank-`r` sets once, and deleting the indexed
occurrence `P_c` leaves all rank-`r-1` sets once.  Form the natural child

\[
 T=\operatorname{rev}(z\cup P_{[0,c)})\Vert Q
   \Vert\operatorname{rev}(z\cup P_{(c,N]}).            \tag{2.2}
\]

Then the following are exact.

### Proposition 2.1 (localized Pascal defect)

1. `T` is the complete child middle layer, once.
2. Every adjacency of `T` is automatically Johnson except possibly
   `Q_(c-1),Q_c` (when `c` is internal).  That last edge is Johnson exactly
   when

   \[
   |Q_{c-1}\cap Q_c|=r-1.                               \tag{2.3}
   \]

3. Away from the two end-degenerate cases, the marked internal wing colours
   are

   \[
   z\cup Q_i\quad(i\ne c-1,c),                          \tag{2.4}
   \]

   while the two phase seams repeat `z union Q_0` and
   `z union Q_(N-1)`.  Hence the natural child has precisely the two forced
   marked q1 holes

   \[
   z\cup Q_{c-1},\qquad z\cup Q_c,                      \tag{2.5}
   \]

   with the obvious one-hole truncation when `c` is within one place of an
   endpoint.
4. The unmarked adjacent colours are exactly

   \[
                     Q_i\cup Q_{i+1}.                   \tag{2.6}
   \]

Proof.  Identity (2.1) gives the layer count.  If `i+1 != c`, the two
distinct rank-`r` sets `Q_i,Q_(i+1)` share the rank-`r-1` set `P_(i+1)`, so
they are Johnson adjacent.  Consecutive marked wing entries `z union P_i`
and `z union P_(i+1)` have union `z union Q_i`; listing which adjacent
`P`-pairs survive deletion gives (2.4)--(2.5).  The two phase seams use
`P_0 subset Q_0` and `P_N subset Q_(N-1)`.  Equation (2.6) is immediate.

This proposition is the strongest automatic output of the one-defect
Pascal lift.  In particular, Pascal gives a *two-colour defect normal form*;
it does not itself repair those colours.

## 3. Why the two-endpoint repair is an additional theorem

There is a canonical way to install the two colours in (2.5): reroot so that
the new left seam is

\[
 (z\cup P_{c-1},Q_{c-1})
\]

and the new right seam is

\[
 (Q_c,z\cup P_{c+1}).
\]

But these two cuts delete the old unmarked seams

\[
 Q_{c-2}\cup Q_{c-1},\qquad Q_c\cup Q_{c+1}.            \tag{3.1}
\]

Unless the colours in (3.1) have other witnesses, this merely transports the
q1 debt.  The K16 cuts succeed for a more special reason: their endpoint
values install the two missing colours while the two deleted colours already
have multiplicity two.  Neither endpoint coincidence nor multiplicity is a
consequence of Proposition 2.1.

For arbitrary depth, the exact extra condition is the bank-and-ladder test:
every old crossing target must have an internal or new-ladder witness, and
every old deficit must lie in a new ladder.  The one-defect hypotheses
control only the two adjacent marked colours; they impose no corresponding
condition on the deeper rays.

Likewise, an unmarked upper target can be supplied inside the natural child
only through the `Q` block.  A useful sufficient parent condition is:

> every old upper target has a parent-word occurrence of length at least
> `h+1`, equivalently a consecutive-`Q` witness.

Universality of the parent word alone does not force this derivative-graded
condition; a target might have only a short occurrence.

## 4. Exact hypotheses needed after Pascal ownership

A Pascal-to-optimal-word induction needs all of the following, not merely
the layer identity.

### Carrier hypotheses

`C1.` The two derivative shores are exact after an explicitly specified
indexed deletion/replacement.

`C2.` The exceptional `Q` adjacency satisfies (2.3), or is repaired by the
rethread.

`C3.` The signed q1 seam ledger leaves positive multiplicity on every
required colour.
It is sufficient, but not necessary, that deleted colours have multiplicity
at least two and inserted colours are exactly the holes.

`C4.` The complete internal-bank/new-ladder spectrum covers every upper
target.  q1 completeness is not a proxy for this condition.

### Schedule hypotheses

`S1.` A length-`W+d(k)` monotone schedule exists and its uncapped maximal
envelope is nonempty and exact on every middle row.

`S2.` The schedule is chain-aligned for every chosen consecutive-row upper
witness.

`S3.` Every positional pin is legal after retiming, and all non-singleton
pins remain protected under subsequent caps.  A one-cell singleton is the
special case whose equality becomes automatic after contraction.

`S4.` The physical lower catalogue is complete for the claimed compiler, or
a sound subcatalogue is used only for a positive construction.

### Joint compiler hypothesis

`J1.` The ALO/common-cap system has one simultaneous solution.  Equivalent
forms are an exact maximal-cap assignment, a Cartesian provider bank with
Hall, or avoidance of the complete conflict clutter.  Marginal Hall, scalar
area, or targetwise individual providers do not imply `J1`.

These are sufficient by AD.7.1.  They are also the exact interfaces exposed
by the current architecture: deleting any one of `C3`, `C4`, `S1--S3`, or
`J1` is refuted by a finite audit or by the abstract robust-Hall example.

## 5. Can Pascal guarantee the hypotheses?

No—not from the presently proved Pascal assumptions.

Pascal guarantees `C1`, and Proposition 2.1 reduces most of `C2` and the
marked part of `C3` to one local defect.  It does not guarantee:

- redundancy of the seams deleted by a repair;
- the all-depth ladder identities in `C4`;
- an optimal chain-aligned schedule or a legal singleton port;
- sufficient provider domains after pinning; or
- a simultaneous common-cap cover.

The failure is not merely formal.  The authenticated natural K16 Pascal
child already has exact ownership and a Johnson chronology, yet its entire
fixed-order three-hole P/Q schedule class is scalar compiler-infeasible.
Only a special reroot changes that conclusion.  Conversely, the robust
`K_(2,5)` common-cap example shows that even large marginal Hall expansion
cannot manufacture `J1`.

Therefore the correct uniform target is a **Pascal source plus an absorber
invariant**, not Pascal ownership by itself.  One possible inductive
invariant is precisely `C1--C4, S1--S4, J1`; proving it is essentially the
remaining upper-bound theorem rather than a routine lift.

## 6. Multi-cell prepin correction (now incorporated)

During this audit, Lemma 4.1 of
`MATH_THEOREM_K_ALLK_PASCAL_REROOT_OWNER_CONFLICT_COMPILER_20260731.md`
needed correction: distinct residual cells can overlap a multi-cell prepin
and erase its last occurrence of a bit, even when the residual assignment
does not reuse the prepin's cell identity.  The synthesis note now correctly
retains every multi-cell prepin equality as a protected row and fully
contracts only an immune case such as a one-cell singleton.

For example, take envelopes

\[
 E_0=\{a,b,c\},\quad E_1=\{a,b,d\},\quad E_2=\{b,e\},
\]

one protected middle row `[0,2]` with target `{a,b,c,d,e}`, and prepin
`{a,b,c,d}` on `[0,1]`.  The prepin and middle row are initially exact.
Choose distinct residual singleton cells `[0,0]` and `[1,1]` for targets
`{a,c}` and `{a,d}`.  The final cap is

\[
 \{a,c\},\quad\{a,d\},\quad\{b,e\}.
\]

Both residual targets and the middle row remain exact, but the frozen prepin
has fallen to `{a,c,d}`.  The repair is exactly the one in the abstract audit:
retain every multi-cell prepin equality in the residual maximal-cap/ALO
system.  Full contraction is valid for a one-cell singleton, or under a
separately proved immunity condition.

## 7. Final assessment

The three audited notes contain a sound and valuable dimension-free
**verification and compilation framework**.  K16 is a certified instance.
The framework is not yet a dimension-uniform construction.  The Pascal lift
explains why the successful even child begins only two q1 colours and a local
upper tower away from completion, but the existence of an upper-safe reroot,
an optimal pinned schedule, and a simultaneous common-cap provider cover are
independent uniform gates.
