# Audit of the `k=16` even-equivariant quotient CP-SAT master

Date: 2026-07-29  
Scope: `scratch/search_k16_even_equivariant_quotient_cpsat_20260729.py`
against `MATH_THEOREM_K16_EVEN_EQUIVARIANT_CT_NORMAL_FORM_20260729.md`.  No
solver search was run in this audit.

## 1. Verdict

After omitting the physical Johnson edges whose two endpoints belong to the
same owner orbit, the quotient model is an exact finite formulation of the
following restricted existence problem:

1. a voltage-one equivariant Hamilton middle deck on the two rank-eight
   shores of `B_16`;
2. all four first-shadow (`q=1`) orbit covers;
3. cyclic positive residence at least four for both the `z` trace `t` and
   every old-coordinate trace, equivalently for `t` and `c`.

The correct number of directed arc variables is

\[
858\cdot64-56=54856,
\]

not `54912`.  The omitted 56 incidences are genuine physical Johnson edges,
but they are impossible in an owner-transversal quotient period.  They must
not be supplied to CP-SAT as self-loops: in `AddCircuit`, a self-loop denotes
an excluded vertex rather than a physical transition.

The formulation makes no claim about `q>=2`, arbitrary-width upper traces, a
safe opening, `COMP_3`, or a length-12873 literal word.

## 2. Exact directed arc catalogue

Let `U` be the canonical representative of one rank-seven or rank-eight
`C_15` owner orbit.  For every physical directed Johnson neighbor `V'` of
`U`, freeness of the target owner action gives a unique pair

\[
([V],p),\qquad V'=\rho^pV,quad 0\le p<15,
\]

where `V` is canonical.  Thus a quotient arc is the triple
`([U],[V],p)`.  Distinct physical neighbors give distinct triples.  Each of
the 858 source orbits has 64 directed physical neighbors: 56 same-shore
swaps and 8 cross-shore deletions or additions.  Hence the raw catalogue has
exactly `858*64=54912` triples.

### Lemma 2.1 (self-orbit Johnson incidences)

For either source rank `r=7` or `r=8`, the number of quotient triples
`([U],[U],p)` at a fixed nonzero voltage `p` is

\[
\begin{cases}
1,&\gcd(p,15)=1,\\
2,&\gcd(p,15)=3,\\
6,&\gcd(p,15)=5.
\end{cases}
\tag{2.1}
\]

Consequently there are `8*1+4*2+2*6=28` on each shore and 56 in total.

#### Proof

The condition is

\[
|U\mathbin\triangle\rho^pU|=2.
\]

On the `d=gcd(p,15)` coordinate cycles of the permutation `rho^p`, the
number of deleted elements is the total number of cyclic one-runs.  It is
one precisely when one coordinate cycle is nonconstant and has one one-run,
while every other coordinate cycle is constant.

If `d=1`, the unique 15-cycle has one run of length `r`; its 15 starts form
one rotation orbit.  If `d=3`, the cycles have length five.  At rank seven
the nonconstant run has length two and one of the other two cycles is full;
at rank eight its length is three and again one other cycle is full.  There
are `3*2*5=30` physical sets, hence two rotation orbits.  If `d=5`, the
cycles have length three.  The nonconstant run has length one at rank seven
and length two at rank eight, and two of the other four cycles are full.
There are `5*C(4,2)*3=90` physical sets, hence six rotation orbits.  This
proves (2.1).  ∎

### Lemma 2.2 (why all 56 loops are forbidden)

In a Hamilton equivariant quotient period, the 858 quotient positions use
every rank-seven or rank-eight owner orbit exactly once.  Therefore the
owner-orbit labels at two consecutive positions are distinct, including the
twisted closing seam.  No arc `([U],[U],p)` can occur.

Thus the exact usable directed catalogue has 54856 arcs.  The implementation
now asserts the complete voltage-by-shore loop histogram, the raw count
54912, and the usable count 54856.

## 3. Circuit and voltage lift

No self-loop literals are passed to `AddCircuit`.  Hence every one of the
858 declared vertices must lie on its unique selected directed circuit;
there is no literal by which CP-SAT could mark a vertex absent.  Parallel
arcs with different voltages remain separate legitimate choices.

Write the selected circuit as

\[
v_0\xrightarrow{p_0}v_1\xrightarrow{p_1}\cdots
\xrightarrow{p_{857}}v_0.
\]

Set `s_0=0` and `s_{j+1}=s_j+p_j mod 15`.  The selected arc definition says
that the physical edge from `rho^{s_j}U_{v_j}` ends at
`rho^{s_{j+1}}U_{v_{j+1}}`.  The linear row

\[
\sum_ep_ex_e=1+15h
\]

therefore makes the closing endpoint `rho U_{v_0}`.  Repeating the quotient
period through all 15 phases gives one physical cycle of length 12870.  It
is Hamilton because each shore's 429 owner orbits occur once and those
owner actions are free.  Conversely, cutting any voltage-one equivariant
Hamilton deck into one quotient period selects exactly such a circuit.

Restricting to total voltage one is without loss within the equivariant
lane: any unit total voltage is conjugated to one by multiplying old
coordinate labels by its inverse modulo 15.  A nonunit total voltage cannot
give a physical Hamilton lift.

## 4. First-shadow rows

For a selected arc with old endpoint masks `U,V`, the implementation uses
`U intersect V` and `U union V`.  The shore types give exactly:

| seam | lower row | upper row |
|---|---|---|
| `AA` | no-`z`, old rank 7 | no-`z`, old rank 9 |
| `BB` | with `z`, old rank 6 | with `z`, old rank 8 |
| `AB` or `BA` | no-`z`, old rank 7 | with `z`, old rank 8 |

Canonicalizing these colors is exact because a selected quotient seam lifts
through all 15 rotations.  One selected support arc covers the whole target
orbit; for a rank-six or rank-nine short orbit of size five, the 15 lifted
occurrences repeat its five members three times, which is harmless.

The light catalogue audit gives the following exact support histograms after
the 56 unusable loops are removed:

| palette | target orbits | directed support-size histogram |
|---|---:|---|
| lower no-`z` | 429 | `70:14, 72:415` |
| lower with `z` | 335 | `18:2, 68:2, 70:4, 72:327` |
| upper no-`z` | 335 | `18:2, 68:2, 70:4, 72:327` |
| upper with `z` | 429 | `70:14, 72:415` |

In particular no target row loses all support when the quotient loops are
removed.  The four eager `BoolOr` families are therefore exactly the four
`q=1` orbit-cover conditions, with no marginal substitution.

## 5. Exactness of the lazy residence cuts

For a candidate circuit, a cyclic positive run of length `ell<4` is
certified by its left boundary transition, its `ell-1` internal transitions,
and its right boundary transition: `ell+1` selected quotient arcs.

For `t`, retaining this directed chain retains the same shore word
`0,1^ell,0`.  For `c`, the chain fixes the local old masks and relative
voltages up to a common rotation.  Changing the rest of the circuit can
change the entering phase, but this merely changes which old coordinate
has the pattern.  The 15-sheet lift contains every common phase, so some old
coordinate still has the same short run.  Consequently

\[
\bigvee_{e\text{ in the certificate}}\neg x_e
\tag{5.1}
\]

is a necessary, not heuristic, no-good.  Since `ell+1<=4<858`, the quotient
arc residues in one certificate are distinct, including across either
cyclic boundary.  Every returned violating candidate violates its new row,
so the CEGAR loop is fail-closed.  A time limit or round limit proves
nothing; a candidate with no remaining short run is exact for residence.

## 6. Independent audit boundary

The search output reconstructs `c` sheet by sheet with cumulative voltage,
which is the literal identity `c_i=1[0 in T_i]`.  The separate auditor
reconstructs all 858 quotient masks from `c,t`, checks the twisted final
seam, both owner-orbit bijections, all four palette covers, and the cyclic
run minima.  Acceptance for this lane must inspect
`resident_q1_pass=true`; the auditor's process exit code alone certifies only
its weaker `central_carrier_pass` field.

No local CP-SAT solve was used in obtaining this audit.  Only the 54912-edge
catalogue and its orbit/support counts were enumerated directly.

## Addendum: persistent first-shadow CEGAR

The later persistent-`q1` patch is also exact.

There are 23996 usable directed AA arcs and 23996 usable directed BB arcs.
Only an AA seam can realize an upper target without `z`, and one selected AA
seam realizes only one of the 335 rank-nine target orbits.  Therefore

\[
\sum_{e\in AA}x_e\ge335.
\]

Likewise, only a BB seam can realize a lower target containing `z`, one old
rank-six orbit per seam, so

\[
\sum_{e\in BB}x_e\ge335.
\]

These two eager aggregate rows are necessary consequences of full `q1`
coverage.  They neither replace the targetwise rows nor remove a feasible
carrier.  On any Hamilton circuit they also imply the familiar run bound
`R<=94`, since the numbers of AA and BB quotient seams both equal `429-R`.

For a returned circuit the patch forms `covered[name]` by reading both
canonical palette labels from every selected arc.  Section 4 proves that
this is exactly physical orbit coverage, including the two short rank-six
and rank-nine orbits.  For every missing orbit it installs the original
necessary row

\[
\bigvee_{e:\,\operatorname{colour}(e)=C}x_e.
\]

Rows persist across rounds.  Batching hard palettes (`lower_z`, then
`upper_no_z`) before the two 429-orbit palettes changes only propagation and
runtime: every accepted candidate is directly checked against all four
complete target sets, whether or not every possible row was materialized.
Residence no-goods and palette rows may be added in the same round because
both are necessary constraints.

The exit behavior is fail-closed:

- `INFEASIBLE` for the current relaxation proves infeasibility of the full
  restricted problem, since every installed row is necessary;
- `UNKNOWN`, a time limit, or the round limit returns no certificate;
- success requires simultaneously no short `t` run, no short `c` run, and
  zero holes in each of the four palette dictionaries.

The implementation now rejects a nonpositive batch size and explicitly
raises if a solver assignment ever violates an already installed palette or
residence row.  Its search audit records `resident_q1_pass=true` and four
zero hole counts only on the conjunctive success branch.  A separate replay
with `audit_k16_even_equivariant_ct_20260729.py` remains required for an
independent artifact audit.

Checkpoint/resume addendum.  The checkpoint preserves the complete sets of
installed targetwise `q1` rows and residence no-goods, and its SHA-256 of the
ordered arc records prevents arc-id reuse under a different quotient
catalogue.  The stored 858-arc circuit is restored only as a nonbinding
CP-SAT hint (it normally violates the rows just learned, which affects
search but not feasibility).  To prevent a malformed checkpoint from
injecting an unsound exclusion and producing a false UNSAT, resume now also
replays the hinted circuit and validates every imported residence tuple:
its two to four distinct arcs must form one directed chain forcing
`0,1^ell,0`, with `1<=ell<=3`, either in `t` or in an old-coordinate trace
for some common phase.  Invalid schema, catalogue hash, depth, target row,
arc id, hint, or residence proof aborts before solving; hence restart
preserves the exact logical model and remains fail-closed.

## Addendum: eager expanded-state residence

An optional exact eager formulation is now available.  For every expanded
old-coordinate one-state `(v,s)` introduce `a_(v,s) in {1,2,3,4}`.  A
selected voltage-`p` quotient arc sends `(v,s)` to `(w,s+p)`.  Impose
`a_(w,s+p)=1` on a `0->1` transition,
`a_(w,s+p)<=a_(v,s)+1` on `1->1`, and `a_(v,s)=4` on `1->0`.  These enforced
linear rows are equivalent to positive run length at least four: a run starts
at age one and cannot reach exit age four in fewer than four one-vertices;
conversely, capped distance from the preceding zero supplies feasible ages
on every legal run.  The same construction on the 429 `t=1` quotient
vertices is necessary because old-coordinate residence does not constrain
the fixed coordinate `z`.  There are exactly 6435 `c` age variables and 429
`t` age variables.  The expanded old-coordinate rows number
`23996*9+23996*8+6864*8=462844`; the `t` rows number
`23996+6864=30860`, for 6864 variables and 493704 enforced linear rows in
total.  No conditionally enforced `AllowedAssignments` table is used.
