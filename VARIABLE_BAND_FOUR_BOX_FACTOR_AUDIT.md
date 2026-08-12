# Independent audit of `VARIABLE_BAND_FOUR_BOX_FACTOR.md`

## 1. Verdict

The coordinatewise interval theory in Sections 2--6 is correct.  In
particular, the internal-run inequality, the core-window formula, the
distinction between maximal-factor core pinning and arbitrary non-core
pinning, and the automatic upper-join translation under linked intervals all
survive a direct endpoint audit.

The cubic calculation in Theorem 6 is also correct **for the intended
literal concatenation architecture**:

\[
 d\ge 2\sum_{H=1}^m\sum_{r=2}^H(2r-1)
   ={m(2m^2+3m-5)\over3}.
\]

There is no double-counting in that sum when every oriented fan is a
separate, position-disjoint contiguous block.  Each summand is charged to a
different subinterval of the monotone `beta` sequence.

One hypothesis should be made explicit in the source theorem statement.
The phrase "a row contain[s] the literal full combined fan blocks" must mean
that the oriented fan occurrences occupy pairwise position-disjoint
contiguous blocks, with no terms inserted between their canonical terms and
no sharing/fusion of physical positions between blocks.  The proof invokes
this assumption when it says the intervals
`[p_(H,r)-1,u_(H,r)]` are pairwise disjoint.  Under a broader subsequence or
overlapping-superstring interpretation, Theorem 6 as written is not proved,
and insertions containing the peak atom can also destroy the singleton-run
hypothesis.  This is a scope clarification, not a defect in the intended
literal-concatenation result.

Proposition 7 is correct under its stated canonical-endpoint hypothesis, but
the phrase "run of consecutive `(2,c)`-containing peaks" should mean a
maximal positive run of the atom `(2,c)` in the **whole row**, possibly
containing nonpeak terms.  It counts distinct canonical peak radii lying in
that atom run.  The proposition yields only an atom-run-incidence count, as
the source correctly emphasizes; it does not yield a physical-length lower
bound without a further disjointness hypothesis.

Subject to those wording corrections, the note's theorem ledger and stated
limitations are mathematically sound.

## 2. Endpoint audit for the monotone interval system

Write

\[
 I_i=[\ell_i,r_i]=[i+\alpha_i,i+\beta_i],
 \qquad 0\le \alpha_i\le\beta_i\le d,
\]

with both offset sequences nondecreasing.  Then

\[
 \ell_{i+1}-\ell_i=1+\alpha_{i+1}-\alpha_i\ge1,
 \qquad
 r_{i+1}-r_i=1+\beta_{i+1}-\beta_i\ge1.
\]

Thus both physical endpoint sequences are strictly increasing, every
interval is nonempty, and `I_i subseteq [1,L+d]`.  These basic index claims
are correct.

### Theorem 1: correct

For an atom `b`, every position outside

\[
 Z_b=[N]\setminus\bigcup_{i:b\notin T_i}I_i
\]

is forbidden by at least one negative equation.  Conversely, a positive
equation needs exactly one occurrence in `I_i cap Z_b`.  Since coordinates
are independent, choosing a hitting set `H_b subseteq Z_b` for every atom is
both necessary and sufficient.  Taking `H_b=Z_b` proves the maximal-factor
claim.  Positions lying in no prescribed interval are genuinely free, so
the final observation in Section 2 is also correct.

No hidden compatibility condition between different atoms is needed: set
union equations decompose coordinatewise.

## 3. Exact audit of the run inequality

Let `[u,v]` be an internal maximal positive run for one atom.  For any
`i in [u,v]` and `p in I_i`:

* if `p<=r_(u-1)`, then `p>=ell_i>ell_(u-1)`, so
  `p in I_(u-1)` and is illegal;
* if `p>=ell_(v+1)`, then `p<=r_i<r_(v+1)`, so
  `p in I_(v+1)` and is illegal.

Earlier negative intervals end before `r_(u-1)`, and later negative
intervals begin after `ell_(v+1)`.  Hence the legal trace in any positive
interval is exactly

\[
 I_i\cap[r_{u-1}+1,\ell_{v+1}-1].
\]

All positive intervals are hit if and only if this integer gap is nonempty:

\[
 r_{u-1}+1\le\ell_{v+1}-1.
\]

Substitution is off-by-one safe:

\[
 (u-1+\beta_{u-1})+1
 \le (v+1+\alpha_{v+1})-1
 \iff
 \beta_{u-1}-\alpha_{v+1}\le v-u.
\]

Therefore Lemma 2 and (3.2) are exact.  For a singleton run `u=v=p`, this
specializes to

\[
 \beta_{p-1}\le\alpha_{p+1},
\]

as claimed.

The boundary statement is also correct.  For a run `[1,v]`, every positive
`I_i` contains its left endpoint `ell_i<ell_(v+1)`, which avoids all later
negative intervals.  A run `[u,L]` is dual, using `r_i>r_(u-1)`.  An all-one
row has no negative barrier.  Thus no additional boundary-run inequality is
missing.

As a consistency check, for fixed delay `alpha_i=0`, `beta_i=D`, the
internal inequality becomes `D<=v-u`, i.e. run length at least `D+1`, the
usual erosion criterion.

## 4. Lower cores and non-core windows

### Theorem 3: correct

Strict endpoint monotonicity gives

\[
 J_{u,v}=\bigcap_{i=u}^v I_i=[\ell_v,r_u]
          =[v+\alpha_v,u+\beta_u].
\]

It is nonempty precisely when

\[
 v+\alpha_v\le u+\beta_u
 \iff \beta_u-\alpha_v\ge v-u.
\]

If `b` is absent from the meet `S_(u,v)`, some central label in the range
excludes it.  Since `J_(u,v)` is contained in that label's interval, every
central factor excludes `b` throughout the core.  Thus contamination by
atoms outside the meet is automatically impossible.  For an atom in the
meet, equality is exactly the positive pin condition
`J_(u,v) cap H_b != empty`; setting `H_b=Z_b` gives the maximal-factor
version.  This proves both directions of Theorem 3, including simultaneous
use of arbitrarily many core targets by the one maximal factor.

### Corollary 4: correct, including boundaries

If `[a,c]` is the maximal support run containing `[u,v]`, the immediate
negative intervals dominate all farther negative intervals.  Consequently
the legal region inside any positive interval in this run is its trace on

\[
 [L_b,R_b]
 =
 \begin{cases}
 [r_{a-1}+1,\ell_{c+1}-1],&1<a,\ c<L,\\
 [1,\ell_{c+1}-1],&a=1,\ c<L,\\
 [r_{a-1}+1,N],&1<a,\ c=L,\\
 [1,N],&a=1,\ c=L.
 \end{cases}
\]

Intersecting this with `[ell_v,r_u]` yields exactly

\[
 \max(\ell_v,L_b)\le\min(r_u,R_b).
\]

There is no missing left- or right-boundary correction.

### Theorem 5: correct and genuinely more general

For arbitrary assigned lower windows, the source correctly recomputes the
legal set

\[
 Z_b^*=[N]\setminus
 \left(\bigcup_{i:b\notin T_i}I_i
       \cup\bigcup_{s:b\notin S_s}Q_s\right).
\]

The two families of positive hitting conditions in (5.2) are then necessary
and sufficient coordinatewise.  This is the correct distinction:

* a natural core is automatically clean because it lies inside a central
  negative interval for every atom absent from its meet;
* a non-core window is not automatically clean and introduces additional
  negative barriers which can remove pins needed by central or other lower
  equations.

The note does not conflate mere core nonemptiness (4.3), maximal-factor bit
survival (4.5)/(4.8), and arbitrary-factor chosen-pin survival (4.6)/(5.2).

## 5. Upper joins

### Section 6: correct

The link inequality is exactly

\[
 \ell_{i+1}\le r_i+1
 \iff i+1+\alpha_{i+1}\le i+\beta_i+1
 \iff \alpha_{i+1}\le\beta_i.
\]

Under this condition, the union of the increasing intervals indexed by
`[u,v]` is the full physical interval `[ell_u,r_v]`.  Reordering the two
finite unions gives

\[
 \bigvee_{p=\ell_u}^{r_v}A_p
 =\bigvee_{i=u}^v\bigvee_{p\in I_i}A_p
 =\bigvee_{i=u}^vT_i.
\]

Without linking, an interval hull can contain positions constrained by none
of the selected central equations, so the warning about nonautomatic upper
translation is justified.

## 6. Literal-fan index audit

For radius `r`, the combined word has

\[
 r+r+r+(r-1)=4r-1
\]

physical positions: `r` upper `U` terms, `r` upper `V` terms with `V_r=A_0`
shared, `r` further `A` terms, and `r-1` `B` terms.  Thus (7.1) has the
claimed length.

For `r>=2`, the immediate neighbours of `U_0` are exactly `U_1` and `V_1`.
The atom

\[
 b_{H,r}=(2,m-H+r)
\]

is present in `U_0`, while both neighbours have second first-pair coordinate
`m-H+r-1`; hence this is an internal singleton run independently of labels
outside the block.  Lemma 2 therefore gives

\[
 \beta_{p_{H,r}-1}\le\alpha_{p_{H,r}+1}.
\]

The lower core starts at `u=V_r=A_0` and ends at `v=B_1`.  It contains
`r+1` terms `A_0,...,A_r` and `r-1` terms
`B_(r-1),...,B_1`, hence `2r` terms and

\[
 v-u=2r-1.
\]

Core nonemptiness consequently requires

\[
 \beta_u-\alpha_v\ge2r-1.
\]

Because `p+1<=u<=v`, monotonicity gives the exact charge

\[
 \beta_u-\beta_{p-1}
 \ge \alpha_v+(2r-1)-\beta_{p-1}
 \ge 2r-1.
\]

All direction signs and all endpoint offsets in (7.3)--(7.5) are correct.

## 7. Theorem 6 and the cubic sum

### Verdict: correct under explicit disjoint-literal-block scope

For each oriented fan, charge the quantity

\[
 \beta_{u_{H,r}}-\beta_{p_{H,r}-1}\ge2r-1
\]

to the physical index interval

\[
 K_{H,r}=[p_{H,r}-1,u_{H,r}].
\]

If the fan occurrences are concatenated as separate literal blocks, these
`K_(H,r)` are pairwise disjoint.  Put them in physical order,
`[a_1,b_1],...,[a_s,b_s]`, so `b_j<a_(j+1)`.  Since `beta` is nondecreasing,

\[
 \sum_{j=1}^s(\beta_{b_j}-\beta_{a_j})
 \le \beta_{b_s}-\beta_{a_1}
 \le \beta_L-\beta_1
 \le d.
\]

Thus no increment of `beta` is counted twice.  There are two disjoint
oriented copies of every fan, and

\[
 \sum_{r=2}^H(2r-1)=H^2-1.
\]

Therefore

\[
\begin{aligned}
 d
 &\ge2\sum_{H=1}^m(H^2-1)\\
 &=2\left({m(m+1)(2m+1)\over6}-m\right)\\
 &={m(2m^2+3m-5)\over3}.
\end{aligned}
\]

The expression is integral: it is twice a sum of odd integers.  At `m=1`
it is zero, consistently with the absence of radii `r>=2`; at `m=2` it is
six, corresponding to one radius-two charge of three in each orientation.

The proof uses only core nonemptiness, not pin survival, so failed bit pins
could only strengthen the obstruction.

### Exact wording correction required

Replace the first sentence of Theorem 6 by an explicit hypothesis such as:

> Let the row be a concatenation, in arbitrary order, of pairwise
> position-disjoint literal copies of (7.1), one for every
> `1<=r<=H<=m` and both orientations (with arbitrary additional blocks only
> between, not inside, these copies).

Without that interpretation, the sentence "a row contain[s] the ...
blocks" is too weak for the summation.  If two prescribed block occurrences
are allowed to share physical positions, their charge intervals need not be
disjoint.  If extra peak-atom-positive terms may be inserted between `U_1`,
`U_0`, and `V_1`, the support at `U_0` need not be a singleton at all.  The
proof then supplies neither (7.3) nor a separate `2r-1` charge for each fan.
The source's introductory and closing descriptions clearly intend the
literal concatenation interpretation, so this correction narrows the formal
statement to the architecture actually proved rather than changing its
mathematical conclusion.

## 8. Peak grouping

### Coordinate calculation: correct

At fixed `c=m-H+r`, put `delta=m-c`; then `H=delta+r` and the admissible
radii are exactly `1<=r<=c`.  The peak and depth-one target are

\[
 P_{c,r}=(\delta+r,c,0,m-r),
 \qquad
 Y_{c,r}=(\delta+r,c,0,m-r+1).
\]

For another peak,

\[
 P_{c,s}\le Y_{c,r}
 \iff s\le r\ \text{and}\ s\ge r-1.
\]

Thus only radii `r` and `r-1` are allowed in any union witness for
`Y_(c,r)`.

### Proposition 7: correct under its stated canonical-witness scope

The corresponding `V_1` omits `(2,c)`.  Starting at the retained canonical
peak and moving along its contiguous witness toward `V_1`, one must leave
the maximal positive atom run through one of its two boundaries.  Every
peak encountered before that exit lies in the witness and hence must be at
most `Y_(c,r)`.  There can therefore be at most two distinct peak radii on
that side: `r` and possibly `r-1`.  Only the first two and last two distinct
peak radii in one atom run can support their own canonical witnesses, so one
run services at most four radii.  The fixed-`c` lower bound

\[
 \left\lceil{c\over4}\right\rceil
\]

follows, and summing over `c=1,...,m` and both orientations gives
`Omega(m^2)` atom-run incidences.

For precision, "run of consecutive `(2,c)`-containing peaks" should be
rephrased as "a maximal `(2,c)`-positive run in the whole incidence word,
and the distinct canonical peak radii lying in it."  Positive nonpeak terms
do not invalidate the proof, but a list obtained by deleting them is not
itself the run to which the argument applies.

The source correctly refuses to multiply this incidence count by a run
length: runs for different atoms can occupy the same physical positions.
Only when the physical runs are additionally disjoint does a fixed delay of
order `m` imply cubic length from Proposition 7.  No overclaim occurs in the
stated conclusion.

## 9. Final theorem ledger

| Item | Verdict | Qualification |
|---|---|---|
| Theorem 1, variable-band factorization | proved | Exact coordinatewise characterization. |
| Lemma 2, internal-run inequality | proved | All integer endpoint and boundary cases check. |
| Theorem 3, core pinning | proved | Core nonemptiness alone is not enough; the note correctly retains the bit-pin condition. |
| Corollary 4, local pin form | proved | Immediate negative barriers are sufficient and exact. |
| Theorem 5, arbitrary lower windows | proved | Correctly includes new negative barriers from all assigned lower equations. |
| Section 6, upper joins | proved | Requires the explicitly stated link condition. |
| Theorem 6, cubic slack | proved in intended architecture | State pairwise position-disjoint literal block copies explicitly. |
| Proposition 7, peak grouping | proved in stated canonical-witness architecture | Clarify that "run" is a full atom-incidence run; conclusion is incidence count only. |

The audited work therefore establishes an exact and useful obstruction to
the **literal concatenated full-fan architecture**.  It does not obstruct
global overlap, physical sharing, reordering of terms inside fans,
replacement of canonical upper witnesses, or arbitrary non-core lower
assignments.  The source's final list of escape routes accurately preserves
those possibilities.
