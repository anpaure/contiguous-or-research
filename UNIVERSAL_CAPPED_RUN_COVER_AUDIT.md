# Audit of `UNIVERSAL_CAPPED_RUN_COVER.md`

## Verdict

The main results survive independent audit.

* The `4a+2` peak-mesh theorem is correct for a linear ordering of the
  distinct points of `H_a`.
* Its forward assignment leaves exactly `4a+2` middle indices unassigned,
  has `C_alpha<=4a+3`, `C_beta=0`, and has clipped cost at most
  `2a(M_a-4a-2)=(6+o(1))a^3`.
* For intact side-block schedules and `a>=3`, every constant-coordinate
  plateau has at most `a+2` vertices.  The resulting clipped cost is at
  most

  \[
  (a+1)(M_a-4a-2)=3a^3+2a^2-2a-1,
  \]

  with the same congestion and omitted-index bounds.
* Proposition 8, Lemmas 9--10, and the resulting long-corridor reduction
  are correct after restricting the displayed parameter to
  `0<delta<4/3` and interpreting a directed line object as a monotone
  subsequence on a coordinate line, not necessarily a nearest-neighbour
  lattice segment.

The source was patched only for those scope/terminology issues and to state
the exact implication to subcritical product aggregation.

## Detailed checks

### Peak-free words and the mesh constant

After maximal constant blocks are compressed, an internal peak is exactly
a `+`-to-`-` sign change.  Its absence is therefore equivalent to a weak
valley.  This proves Lemma 1 with the stated endpoint convention.

On an interval where all three coordinates are weakly monotone, choose a
proper nonempty set of nondecreasing coordinates (constant coordinates may
be put on either side).  Their sum increases by at least one at every step
between distinct integer points and has range at most `2a`; hence the
interval has at most `2a+1` points.  This verifies Lemma 2.

For a peak-free window, sorting the three valley indices gives four
overlapping intervals.  The two exterior intervals have at most one point
each; the two interior intervals have at most `2a+1` points each.  The
three cut points are counted twice, so

\[
 |W|+3\le1+(2a+1)+(2a+1)+1=4a+4,
\]

and `|W|<=4a+1`.  Thus `4a+2` forces a peak.  Because both smaller
neighbours lie inside the window, the plateau is a maximal component of
the corresponding upper-threshold word in the full linear order.  Its
coordinate level contains exactly `2a+1-|t|` points.  These observations
verify every endpoint and off-by-one in Theorem 3.

### Charge congestion

For assigned index `i`, the run is contained in `[i+1,i+L]`, where
`L=4a+2`.  If the adjacent `alpha` increment at `t` is charged, then

\[
 i<t\le v_i+1\le i+L+1,
\]

so `t-L-1<=i<=t-1`.  There are at most `L+1=4a+3` such integer indices.
No `beta` increment is charged.  The use of `v_i+1` is legitimate because
the peak is internal in the full middle order.  This verifies Corollary 4,
including the perhaps non-obvious `+1` in `4a+3`.

### Intact side blocks

Inside a non-unit block exactly one coordinate is constant and the other
two are strict.  A plateau using at least two vertices of the block must
therefore use its designated coordinate and contains the whole block.
For a fixed nonzero coordinate level there is only one such designated
block, of length at most `a`; blocks immediately adjacent to it can each
contribute at most one endpoint.  If no non-unit block is traversed, at
most two non-unit endpoints can occur, while the radius-one blocks and the
center contribute at most three points at one coordinate level.  This
gives `max(a+2,5)=a+2` for `a>=3` and validates Lemma 6 and Theorem 7.

### Long-corridor constants

There are `M_a-L=3a^2-a-1` forward windows.  With
`q_0=(4/3-delta)a`, `0<delta<4/3`, the estimate

\[
 \sum_iq_i\le q_0(M_a-L)+(2a-q_0)F_delta
\]

and a lower bound `(4-o(1))a^3` give

\[
 F_delta\ge
 \left(\frac{3delta}{2/3+delta}-o(1)\right)a^2.
\]

Each length-`L` window contains a fixed plateau in at most
`L-|P|+1<=L` ways, yielding `Omega_delta(a)` distinct long peaks.  A peak
on level `c` has at most `2a+1-|c|` vertices, giving the stated central
strip.  Along a fixed-coordinate plateau the two cross-coordinate values
are distinct and sum to a constant; any failure of strict monotonicity
creates a singleton peak in one of them.  Finally, plateau edge sets for
different coordinates cannot share an ordering edge, because two fixed
coordinates determine the point.  Hence `sum_P lambda(P)<=M_a-1`.

The restriction `delta<4/3` is required when dividing by
`(4/3-delta)a` in the peak-count bound.  It was missing in the original
wording and has been patched.

## Exact scope of the implications

The fan-capped avoidance theorem applies because the lower targets are
distinct, have chain height `3a-1`, and no witness of one can contain a
complete selected middle witness.  If the open universal cheap-cover
conjecture held with fixed saving `epsilon a^3`, its combination with that
theorem would force `D=Omega(a^2)` for every cubic three-box word.

That would contradict any uniform local bound of the form

\[
 g_3(\boldsymbol\ell)\le w(\boldsymbol\ell)
       +O((1+\sum_i \ell_i)^c),\qquad c<2,
\]

already on `\boldsymbol\ell=(2a,2a,2a)`.  It would therefore close the
three-factor route in `SUBQUADRATIC_PRODUCT_AGGREGATION.md`.

Nothing currently proved in the source has that consequence.  The
universal cost constant is `6`, not less than `4`; the constant `3` is
proved only for intact side-block schedules.  Likewise, an ordering that
escapes the peak assignment is not automatically a universal word: it is
only a candidate middle-order geometry and still needs a factorable band
and all lower/upper targets.

## Remaining open statement

The exact surviving question is whether every linear order of `H_a`
admits some heterogeneous internal-threshold-run assignment, omitting
`o(a^2)` indices, with `O(a)` charge congestion and clipped cost
`(4-epsilon)a^3` for one absolute `epsilon>0`.  The peak mesh reduces a
failure to `Theta(a)` long, directed, central coordinate-line
subsequences, but does not exclude a three-directional rotating braid of
such subsequences.
