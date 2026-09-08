# Audit of the ordered pair-column tower and the proposed beta tail

Date: 2026-07-27

Scope: Sections 1--3 of
`MATH_THEOREM_AGGREGATE_FIRST_MOMENT_TOP_STRIP_QUARANTINE_20260727.md`,
including the proposed repair which uses an \(\alpha\)-initializer up to
\(B=C\log ^2m\) and a maximum-codegree tail thereafter.

## 0. Verdict

The backward exponential-potential identity is algebraically correct
**if** its infinite ordered tower and its one-step generator inequality
hold.  Neither premise is currently valid.

There are two decisive failures.

1. Lemma 1.1 applies the static mixed-diagram theorem at arbitrarily
   large excess \(s+j\).  The proved theorem explicitly applies only
   while twice the excess is within the certified local path-mesh order.
   Fixing the row set does not remove this restriction.
2. The generator discards events meeting a previously adjoined protected
   column as “nonpositive.”  They are nonpositive for the raw count, but
   not after division by the full moving product base.  One event can
   kill two protected columns once while the base charges two marginal
   deaths.  This produces a positive normalized common-event defect not
   represented by a pair column on two fixed row arms.

The second point directly refutes the displayed inequality

\[
                     \mathcal G\widetilde F_{\tau,j}
                     \le\kappa\widetilde F_{\tau,j+1}
\tag{0.1}
\]

for the tower as defined.  Consequently (3.3), although a correct
formal cancellation, cannot be applied to the physical process.

The suggested \(\beta=O(1/m)\) tail is arithmetically strong enough for
selected-edge columns between two genuinely resource-disjoint fixed
arms.  It does not yet repair the proof: it omits protected-column
interactions and has no analogue for unresolved common compensation
resources.  A larger state space might use this idea, but that state
space and its initializer have not been proved.

## 1. Lemma 1.1 exceeds the proved static range

Let the base type have excess \(s\).  Each ordered pair column has two
incidences and one column, hence increases excess by one.  Therefore

\[
                         \omega(\mathcal E_j(\tau))=s+j.
\tag{1.1}
\]

The exact scope statement in
`MATH_THEOREM_STATIC_MIXED_DIAGRAM_EXCESS_AND_DYNAMIC_OMEGA_BUFFER_20260727.md`
is

\[
                  2\omega\le L_{\rm pm},
\tag{1.2}
\]

where \(L_{\rm pm}\) is the certified total order of the one-row
disjoint path-mesh maximum and internal census.  Thus that theorem gives
Lemma 1.1 only for

\[
                         2(s+j)\le L_{\rm pm},
\tag{1.3}
\]

not for every \(j\ge0\).

The sentence “the formal row set is fixed” does not change (1.3).  In
the row-exploration proof, one physical row may eventually meet \(j\)
old columns.  The relevant path-mesh composition then has total witness
order growing with \(j\).  No theorem supplies a uniform endpoint factor
after that order leaves the certified range.

Dropping disjointness between the ordered columns makes the claimed
iteration still less justified.  Reusing an already exposed physical
column or an already forced endpoint does not impose a fresh endpoint
constraint, so it cannot automatically pay a fresh factor \(\alpha\).
The equality credit from a rare row pattern is finite; it cannot be
spent once per column for an arbitrarily long ordered list.

This is not a harmless formal tail.  The backward parameter is

\[
                         A(t_0)=\Theta(m\log m)
\tag{1.4}
\]

over the whole trajectory.  Without a per-column decay beyond
\(L_{\rm pm}\), the factorial weights \(A^j/j!\) do not by themselves
make the unproved part negligible.  The estimate
\(\exp(A\alpha)=1+o(1)\) is a consequence of the missing
\(\alpha^j\) initializer, not an independent bound on the tail.

## 2. The full-base drift has protected-column correlations

For clarity, consider a current displayed configuration containing two
protected edge/resource columns \(c_1,c_2\).  Suppose a future selected
edge \(g\) meets both columns, but meets none of the fixed row-arm
witnesses used to define the tower.  Let its clock rate be \(\lambda\).

For the raw configuration indicator, the event contributes

\[
                         \mathcal L Z=-\lambda Z.
\tag{2.1}
\]

The complete product base counts the marginal survival of both protected
columns.  Its contribution is

\[
                    {\dot B\over B}=-2\lambda.
\tag{2.2}
\]

Consequently the normalized count has positive drift

\[
 \mathcal L(Z/B)=(-\lambda+2\lambda)Z/B
                 =\lambda Z/B.
\tag{2.3}
\]

The event is therefore not favorable after transport by the full base.
It is exactly another joint-hazard/multiplicity-excess term.

Section 2 of the tower proof says instead to discard every event meeting
a previously adjoined protected column.  That is the raw-sign argument
which the earlier top-strip audit already ruled out for prefix rows.  It
does not become valid for protected columns.

The union-deficit inequality

\[
                         (t-1)_+\le\binom t2
\tag{2.4}
\]

is useful, but its pairs must range over **all marginally counted live
objects**: physical row arms, the marked incidence, and every protected
column.  In the tower as defined, pair columns join only two fixed row
arms.  After \(j\) extensions there are \(j\) additional protected
objects, so the number of possible pairs and the possible multiplicity
of one event both grow with \(j\).  A coefficient \(\kappa\) independent
of \(j\) is not justified.

There is a further closure issue.  If a new edge column \(g\) meets a
previous protected edge column, the enlarged tuple is no longer in the
pairwise resource-disjoint column class used by the static mixed-diagram
theorem.  Calling the event terminal avoids constructing the child, but
also loses the positive correction (2.3).  Keeping it requires a new
column-intersection-forest state and a proved bound for that state.

Hence (0.1) is false for the stated tower even if one grants its static
initializer.

## 3. Physical equality-block normalization

Let \(a\) be the number of formal row copies and \(b\) the number of
physical blocks after the equality partition.

* A physical first-moment reference must have one row hazard per
  physical block, hence a factor \(d_t(X)^b\), not
  \(d_t(X)^a\).
* The static theorem deliberately retained the looser factor
  \(d(X)^a\) as equality credit.  It did not state the dynamic
  equality-block initializer used in the tower.

The marked-incidence lift also has equality cases: the marked edge may
coincide with one of the displayed physical rows.  Then it is not a new
physical arm and does not have an independent row hazard.  To interpret
\(d_t(X)Z_{\tau,j,X}\) literally, one must partition the mark equality
patterns and give each its physical-block base.  The current proof calls
the mark one additional arm without carrying out this partition.

This issue is plausibly repairable by quotient-row exploration, but it
is not bookkeeping-free and it does not repair Sections 1--2.

## 4. Edge and compensation columns have different free factors

For a selected-edge column, one free incidence has scale \(K\Delta_t\)
and its clock has rate

\[
                         \nu_t={1\over r\Delta_t}.
\tag{4.1}
\]

Thus the free factor cancels because
\(\nu_tK\Delta_t=K/r=1+o(1)\).

For a compensation-resource column, one free incidence has only \(K\)
choices and its clock rate is at most \(1/r\).  The corresponding
cancellation is

\[
                         K/r=1+o(1).
\tag{4.2}
\]

Therefore a color-correct base must distinguish \(K\Delta_t\) from
\(K\).  The arbitrary static mixed-diagram theorem used the common loose
factor \(K D\) for private columns; that statement alone does not give
the coin cancellation in (4.2).

More importantly, the latest exact status in
`MATH_THEOREM_STARRED_C4_COIN_ENDPOINT_AND_EDGE_ONLY_WEIGHTED_GATE_20260727.md`
lists the dynamic resource-coin endpoint (2.13) after endogenous
restriction as **not proved**.  The tower's declaration that
\(\alpha_\circ\) is already a proved current endpoint therefore imports
an open input.

Resolving a displayed shared resource does not solve this for an
arbitrarily long tower.  Two distinct repaired rows can share many
unexposed resources.  To make every future common coin disappear, one
would have to resolve the complete row intersection, potentially adding
\(\Theta(m)\) resource columns.  The finite \(O(\log ^2m)\) equality/
witness core does not certify the absence of all such resources.

## 5. Slabs do not create heredity

If an infinite tower satisfying Lemma 1.1 and (0.1) were initialized at
time zero, then a single whole-trajectory backward potential with

\[
                         A(t)=\int_t^T\kappa(v)\,dv
\tag{5.1}
\]

would indeed propagate it without reapplying a static theorem to an
endogenous residual.  This is a genuine virtue of the proposed method.

The subdivision into \(O(m\log m)\) reference slabs does not supply the
missing infinite initializer or the missing generator closure.  At a
new slab start one may use what the preceding supermartingale actually
propagated; one may not invoke row exploration afresh on the current
residual.  Moreover, fixed-factor changes of a base cannot be multiplied
once per slab.  Only an error whose integral is globally \(o(1)\) may be
carried through all slabs without exponential accumulation.

Thus a single whole-trajectory potential would avoid the nonheredity
problem **conditional on** the correct tower.  It cannot cure the two
failures above.

## 6. Audit of the proposed \(\beta\)-tail repair

There is a valid and potentially useful calculation.  Let \(A,B\) be
two resource-disjoint repaired-edge arms, each of size at most \(K\).
If \(\Delta_2\) is the maximum current pair codegree and \(\Delta\) the
free edge-column degree scale, then

\[
 \left|\{g:g\cap A\ne\varnothing,\ g\cap B\ne\varnothing\}\right|
 \le \sum_{a\in A,b\in B}d(a,b)
 \le K^2\Delta_2.
\tag{6.1}
\]

Relative to the free edge-column mass \(K\Delta\), this is

\[
                         \beta_E\le{K\Delta_2\over\Delta}.
\tag{6.2}
\]

At time zero in the repaired catalogue,
\(\Delta_2/\Delta=O(m^{-2})\), so

\[
                         \beta_E=O(1/m).
\tag{6.3}
\]

Suppose, hypothetically, that the initializer satisfied

\[
 {F_j(t_0)\over F_{\rm base}(t_0)}
 \le
 \begin{cases}
  C\alpha^{s+j},&j\le B,\\
  C\alpha^{s+B}\beta_E^{,j-B},&j>B.
 \end{cases}
\tag{6.4}
\]

Then the backward tail would be at most

\[
 C\alpha^s\left({\alpha\over\beta_E}\right)^B
       \exp(A\beta_E).
\tag{6.5}
\]

For \(B=C_0\log ^2m\),
\(\alpha=m^{-19/10+o(1)}\),
\(\beta_E=O(m^{-1})\), and \(A=O(m\log m)\),

\[
 \log\left[
  (\alpha/\beta_E)^B e^{A\beta_E}
 \right]
 =-\Omega((\log m)^3).
\tag{6.6}
\]

So the numerical tail is excellent.

However, (6.4) is not yet a theorem for the required tower.

1. Formula (6.1) applies to two genuinely resource-disjoint arms.  A
   finite witness-equality type does not certify that two displayed rows
   have no other shared owner.
2. Once protected columns are included among the marginally counted
   objects, a new edge meeting two old columns creates a non-disjoint
   column-intersection state outside the present static theorem.
3. For compensation columns, the analogous fraction is

   \[
              \beta_\circ(A,B)={|A\cap B|\over K},
   \tag{6.7}
   \]

   which can be \(1-o(1)\) for distinct near-coincident repaired rows.
   There is no universal \(O(1/m)\) coin tail.  Completely resolving
   all shared resources can require \(\Theta(m)\) columns, beyond the
   local initializer.
4. In an endogenous residual, \(\Delta_{2,t}/\Delta_t\) need not retain
   its time-zero value.  The beta calculation is safe as a time-zero
   initializer for a globally propagated tower, but not as a fresh
   current-time static estimate.

The beta tail therefore supplies a credible selected-edge ingredient
for a redesigned global tower.  A complete repair still needs:

* states which include row--column and column--column joint-deletion
  pairs;
* a time-zero initializer for those states with an \(\alpha\)-to-beta
  transition;
* a separate treatment of long common-resource/coin fibres; and
* physical equality-block references, including the marked incidence.

## 7. Surviving conclusion

The static arbitrary-diagram theorem and the graded finite moment core
remain valid in their certified range.  The proposed infinite ordered
pair-column tower does not close the first-moment top strip.  The exact
open problem is now narrower: construct and initialize a globally
propagated joint-deletion tower (or another affine top barrier) which
includes protected-column interactions and controls the coin fibre.

