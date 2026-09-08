# Self-audit: cross-ray envelope factorization and q1 multiplicity

**Date:** 2026-08-04  
**Method:** independent symbolic replay from the displayed bridge and
interval definitions; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_CROSS_RAY_ENVELOPE_DIAMOND_FACTORIZATION_AND_Q1_MULTIPLICITY_NOGO_20260804.md`

## 0. Verdict

**PASS, with the stated scope.**

The exact positive statement is an occurrence-labelled **factorization
record** for each single cut.  A complete cap state must still accept its
within-ticket two-coordinate coinstantiation and must price every occurrence
used by the two monotone envelope chains.  The negative statement grants
those favorable premises and remains valid because all cuts on one rail
still meet the same unit q1 terminal.

The theorem does not claim that no remote copy of the same envelope value
occurs elsewhere in a completed word.  It proves uniqueness in the selected
q1-exact turn bank, uniqueness in each explicit chord span, and an
`Omega(d)` charge for manufacturing all required copies as repeated seams
of the same flat diagonal band.

## 1. Owner-index and address replay

The owner word

\[
 G_1,\ldots,G_d,B,A,H_1,\ldots,H_d,D,E
\]

has indices

\[
 B:d,\quad A:d+1,\quad H_s:d+1+s,\quad
 D:2d+2,\quad E:2d+3.
\]

For a depth-`d` diagonal, the lower-turn address at seam `i` is
`[i+1,i+d]`.  Hence

\[
 p_d=[d+1,2d],qquad p_{2d+2}=[2d+3,3d+2],
\]

which are exactly the two source rails in the bridge construction.  The
corresponding upper-turn addresses are

\[
 q_d=[d,2d+1],qquad
 q_{2d+2}=[2d+2,3d+3].
\]

They are distinct and disjoint for every `d>=2`.

## 2. Boolean-value replay

With

\[
 U=K\cup\{z,a_1,a_3\}\cup F^\circ,
 \quad M_+=U\cup\{f_{d+1}\},
 \quad M_-=U\cup\{f_0\},
\]

the chord endpoints are

\[
 B=M_+-a_3,quad A=M_--a_3,quad
 D=M_--a_1,quad E=M_+-a_1.
\]

Therefore

\[
\begin{aligned}
 B\cap A&=K\cup\{z,a_1\}\cup F^\circ=C_1,\\
 B\cup A&=K\cup\{z,a_1\}\cup F=R_1,\\
 D\cap E&=K\cup\{z,a_3\}\cup F^\circ=C_3,\\
 D\cup E&=K\cup\{z,a_3\}\cup F=R_3.
\end{aligned}
\]

Since `|K|=r-d-3`, the ranks are

\[
 |C_1|=|C_3|=r-1,qquad |B|=|A|=|D|=|E|=r,qquad
 |R_1|=|R_3|=r+1.
\]

Thus both chord squares are Boolean Hasse diamonds of exactly the required
q1 type.

## 3. Ray partition and monotone-chain replay

On the left rail, cut `j` gives

\[
 [d+1,d+j]\ \dot\cup\ [d+j+1,2d]=[d+1,2d].
\]

Its two values are

\[
 K\cup\{z,a_1\}\cup F[1,j],qquad
 K\cup\{z,a_1\}\cup F[j+1,d],
\]

whose union is `C_1`.  The right rail is identical with `a_1` replaced by
`a_3` and the translated address origin `2d+3`.

For the prefix, extending the right endpoint once changes `F[1,t]` to
`F[1,t+1]`; for the suffix, extending the left endpoint once changes
`F[t+1,d]` to `F[t,d]`.  Every step adds one interval position and exactly
one new filler value.  The final step adds `f_d` or `f_1`, respectively,
and reaches the full rail.  Hence the two chains displayed in the theorem
are literal interval and Boolean Hasse chains.

This also exposes an additional collision which the theorem does not need:
different cut bundles reuse other cuts' ray cells as intermediate chain
occurrences.  Pricing these cells can only decrease simultaneous rank; it
cannot invalidate the terminal rank-one upper bound.

## 4. Capacity replay

For fixed rail `epsilon`, every deterministic record ends at the one address

\[
 q_{i_\epsilon},\qquad i_1=d,quad i_3=2d+2.
\]

Under ordinary per-ticket unit-capacity semantics this is a cut of capacity
one.  Granting diagonal dual-role coinstantiation inside one ticket does not
permit two different logical ticket labels to consume that occurrence.
Therefore the rail rank is at most one.  The two rails have two distinct
terminal addresses, so the total rank is at most two and the deficiency of
`2(d-1)` separate tickets is at least `2d-4`.

If the envelope lower turn is finite, it gives the same cut earlier.  If it
is contracted as declarative, the terminal cut remains.  If within-ticket
diagonal coinstantiation is not accepted, feasibility is weaker still.
Thus the theorem deliberately uses the strongest favorable convention.

## 5. Q1-exact multiplicity replay

On a cyclic q1-exact diagonal, `i -> P_i` is a bijection from `W` seams to
the `W` rank-`(r-1)` values.  Since `OR(p_i)=P_i`, a fixed envelope value
has exactly one selected lower-turn occurrence.  The q1 diamond above that
value is therefore unique in the selected diagonal.

This does not bound remote intervals of the same value which are not
selected q1 turns.  Such an interval helps only after an additional typed
upper attachment and complete-state capacity proof are supplied.

## 6. Explicit-source uniqueness replay

Within one explicit rail, source position `s` contains the private filler
`f_s`, so every rail position is necessary to obtain all of `F^circ`.
Outside the left rail, every unchanged source letter which could connect to
it contains `f_0`, `f_(d+1)`, or `a_3`; a strict interior interval of the
other rail consists only of fillers and lacks `K union {z,a_1}`.  Thus the
full left rail is the unique interval of value `C_1` in the complete bridge
source.  The symmetric blocker list for `C_3` is `f_0`, `f_(d+1)`, or
`a_1`, and the full right rail is likewise unique.

No statement about a remote part of a later ambient word is inferred.

## 7. Replication-charge replay

A word of length `W+d+c` has `W+c` width-`d+1` intervals and therefore at
most `W+c-1` internal seams.  If `b` base q1 colours are supplied outside
those seams, realizing the remaining `W-b` distinct colours plus `t`
repeated seam occurrences forces

\[
 W-b+t\le W+c-1,
\]

or `c>=t-b+1`.  Raising each of two envelope multiplicities from one to
`d-1` adds `t=2(d-2)`, yielding `c>=2d-b-3`.

This is exact for the stated consecutive flat-band model.  Off-band sockets
are outside the conclusion.

## 8. Scope checks

The deterministic product criterion is a direct capacity equivalence, not
an appeal to two marginal matchings.  When two phase coordinates are
distinct, all of their terminal occurrences must be distinct.  When the
fixed state explicitly accepts a diagonal pair `(q_j,q_j)`, that occurrence
is charged once inside ticket `j`, but different ticket labels still need
different `q_j`.  The existing bridge supplies a constant `q_j` on each
rail, so it fails the latter injection.

The audit confirms that the theorem does **not** assume or claim:

1. a many-ticket fan coinstantiation rule;
2. that a polarity bit duplicates capacity;
3. that the existing q1-exact diagonal contains remote duplicate envelope
   diamonds;
4. that product/phase acceptance for even one bundle is automatic;
5. that intermediate ray-chain cells avoid the background; or
6. that an off-band replicated socket is impossible.

The exact remaining positive premise is an occurrence-distinct accepted
terminal bank of size `d-1` per rail, or a different injective typed
factorization.  The selected q1-exact palette and the explicit bridge's two
native chord diamonds do not provide it.
