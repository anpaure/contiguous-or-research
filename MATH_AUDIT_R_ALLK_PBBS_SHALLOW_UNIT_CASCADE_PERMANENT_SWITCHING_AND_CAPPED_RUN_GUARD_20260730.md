# Independent audit: PBBS shallow cascade, permanent switching, and capped run/guard completion

Date: 2026-07-30  
Audited file:
`MATH_THEOREM_R_ALLK_PBBS_SHALLOW_UNIT_CASCADE_PERMANENT_SWITCHING_AND_CAPPED_RUN_GUARD_20260730.md`  
Method: three independent hand derivations followed by a line-by-line
reconciliation.  No finite search, SAT, web access, or remote computation
was used.

## 1. Final verdict

The fixed-chronology shallow-layer counts, weighted switching inequalities,
target-capped alteration theorem, background-aware run/guard polynomial,
and component-cube theorem are **valid with the scopes stated in the final
report**.

They do not prove `nu(k)<=B(k)+O(k)`.  The strongest proved negative
implication, under the displayed fixed-chronology conditioning hypotheses,
is a concrete obstruction to starting a spread matching measure before
recursively conditioning the shallow Pascal layers.  The strongest positive
result is an exact post-closure expansion criterion.  It is proved
on the odd PBBS chronology; an even conclusion remains conditional on a
Pascal lift satisfying that same closure and pressure criterion.

## 2. Chronology and seam scope

The flat envelope identity

\[
                         |P(I)|=r-d+|I|-1
\]

is used only for intervals wholly in a strict flat region.  Every interval
meeting an endpoint ramp is charged to the fail-safe `2d^2` exceptional
budget.  In a linearization with internal nonresident seams, every interval
crossing such a seam must likewise be exceptional.

For a length-`W+d` source, a length-`ell` interval has owner footprint
`[a-d,b]`, so one seam affects at most `d+ell-1` such intervals.  Summing
through length `d-1` gives

\[
 \sum_{\ell=1}^{d-1}(d+\ell-1)={(d-1)(3d-2)\over2}.
\]

columns of length at most `d-1`.  Therefore Proposition 2.3's parameter

\[
 \xi\le2d^2+s{(d-1)(3d-2)\over2}
\]

is valid.  This is important: the one-piece obstruction cannot be silently
applied to a Catalan-many-component PBBS opening.  The actual opening must
supply its own `xi` ledger.

## 3. Rank-`(r-2)` cut

**Verdict: valid.**

For

\[
 \mathcal A={ [2m+1]\choose m-1},qquad
 |\mathcal A|={m\over m+2}W,
\]

the candidate columns are exhausted by the following classes.

1. A flat interval of length at most `d-2` has envelope rank at most
   `r-3` and serves no member of `mathcal A`.
2. A flat length-`(d-1)` interval has envelope rank `r-2` and serves at
   most its one envelope label.  There are `W+2` such columns.
3. After `W` distinct length-`d` facet reservations, one length-`d` column
   remains.
4. At most `2d^2` ramp exceptions remain, each with envelope inside a
   rank-`r` owner and hence at most `binom(r,2)` relevant labels.

Thus

\[
 e(\mathcal A,R)
 \le U_2=W+2+(2d^2+1){r\choose2}.
\]

The capacitated cut with interval-side set empty gives

\[
 u\ge{|\mathcal A|-o_2\over U_2}=1-o(1)
\]

for `o_2=O(k)`.  This is a pre-recursive-closure theorem.

If Hall holds, degree counting gives

\[
 g_2\ge2(|\mathcal A|-o_2)-U_2.
\]

Two degree-one rows cannot share their unique column under Hall.  Hence
almost all of this layer is genuinely forced, unless its targets are
omitted.

## 4. Rank-`(r-3)` staged cut

**Verdict: valid after replacing one equality by an upper bound.**

At most `E_0=2d^2+1` of the forced rank-`(r-2)` columns are exceptional.
The number of unreserved flat length-`(d-1)` columns is therefore at most

\[
 L_1\le {4W\over m+2}+4
       +E_0\left({r\choose2}+1\right)+2o_2.
\]

For rank `r-3`, flat lengths at most `d-3` give no candidate, length
`d-2` gives at most one, and length `d-1` gives at most `r-2`.  Hence

\[
 e(\mathcal B,R)
 \le W+3+(r-2)L_1+E_0{r\choose3}.
\]

The correct asymptotic relation is

\[
                         (r-2)L_1\le(4+o(1))W,
\]

not equality.  It gives `U_3<=(5+o(1))W` and therefore

\[
                         u\ge1/5-o(1).
\]

This applies before recursively conditioning newly created rank-`(r-3)`
units.  It is not a statement about the final fully closed shore.

### Additional audit: deadline-density product collision

**Verdict: valid with the common-fugacity scope stated.**

The initial interval-column count is

\[
 N_0=dW+{d+1\choose2}=\Lambda+\sigma,
 \qquad 0\le\sigma<W+d.
\]

Conditioning a candidate removes one target and one column; omissions only
increase column surplus, and other deletions decrease it.  Hence every
residual face with `L` targets, `N` supporting columns and `h` omissions has
`N<=L+sigma+h`.  Thus any Hall-feasible face with `L` much larger than
`sigma+h` is asymptotically square.

For product row laws, the same-column pair events opposing a positive
candidate `(s,J)` have total unrenormalized common-fugacity pressure

\[
 c^2\sum_{I\ne J}\pi_{s,I}(\ell_I-\pi_{s,I}).
\]

Weighting by `pi_(s,J)` and summing gives

\[
 c^2\sum_{s,I}\pi_{s,I}(1-\pi_{s,I})
              (\ell_I-\pi_{s,I})
 \ge c^2L(1-u)(L/N-u)_+.
\]

The common-fugacity certificate bounds this by `L log c`; maximizing
`log(c)/c^2` gives `1/(2e)`.  Therefore the report's inequality and
`u>=1-1/sqrt(2e)-o(1)` consequence are exact.  For a uniform `M`-list law
the limiting left side is at least `1/4`, so every `M>=2` fails this
particular certificate.  This does not exclude asymmetric event weights or
matching-supported laws.

## 5. Weighted alternating switching

**Verdict: valid.**

For disjoint extendable edges, direct cancellation of their weights gives

\[
 {\Pr(e,f)\over x_e x_f}
 ={Z_HZ_{H\ominus\{e,f\}}\over
   Z_{H\ominus e}Z_{H\ominus f}}.
\]

Thus the switching estimate below is exactly an estimate for the weighted
permanent deletion ratio; it does not use negative association.

For a pair `(M_11,M_00)` in which `e,f` lie in distinct symmetric-
difference components, swapping the component containing `f` produces a
left-saturating pair in `Omega_10 times Omega_01`.  The edge multiset, hence
the product weight, is unchanged.  The inverse switch is canonical on the
image.  Only same-component pairs escape, proving

\[
 Z_{11}Z_{00}\le Z_{10}Z_{01}+\mathfrak B_H(e,f).
\]

If `mathfrak B_H<=beta Z_10Z_01`, elementary expansion of the four status
weights proves

\[
                         \Pr(e,f)\le(1+\beta)\Pr(e)\Pr(f).
\]

When the direct pair inequality holds with factor `1+gamma/d` in every
endpoint-deleted prefix graph, successive conditioning gives

\[
 {\Pr(F)\over\prod x_e}
 \le(1+\gamma/d)^{j(j-1)/2}
 \le e^{\gamma j/2}
\]

for `j<=d+1`.  The exponent and constant `C_0=e^(gamma/2)` are correct.
For zero status products, the direct pair inequality must be assumed; the
ratio certificate is not divided by zero.

The switch-supply corollary is a weighted incidence double count.  Its
preimage bound counts switch incidences with multiplicity.  The displayed
`q eta>=bd/gamma` statement assumes `gamma>0`; `gamma=0` requires zero
same-component exceptional mass.

## 6. PBBS guard links

**Verdict: valid.**

At a target visited by an alternating component, its two matching edges
link their interval columns.  Thus every alternating component projects to
a connected set in the interval-link graph.  Interval-component separation
forces `mathfrak B_H=0` and survives deletion.

Within the subgraph consisting only of one tagged stable bank, every
auxiliary target has one interval column.  This subgraph is a star forest,
not necessarily an induced subgraph of the full residual graph.  Therefore
all usable alternating entropy must enter through an external candidate

\[
 I'\ne J_h,qquad F(I')\subseteq R_h\subseteq P(I'),
\]

or another external guard bridge.  Existing PBBS all-depth support does not
give the required `Omega(d)` bounded-congestion bridge supply.

## 7. Target-capped alteration

**Verdict: valid.**

Randomly orient every occurring conflict to one of its target parts.  The
union of oriented targets hits all occurring minimal conflicts.  For target
`S`, the union bound gives

\[
 \Pr(S\text{ deleted})\le\min\{1,L_S\}.
\]

Linearity of expectation and integrality give an outcome deleting at most

\[
 \left\lfloor\sum_S\min\{1,L_S\}\right\rfloor
\]

distinct targets.  No independence among conflict occurrences is needed.

Consequently a large conflict polynomial is not a lower obstruction.
Exponentially many stable conflicts sharing one target may cost one
deletion.  The genuine deterministic obstruction for a fixed chronology is
a superlinear minimum target hitting number over every saturating matching.

## 8. Background-aware run/guard polynomial

**Verdict: valid after the forced-background correction.**

Let `Theta_0` be the compatible conditioned family and

\[
 D_x^0=E_x\cap
 \bigcup_{(S,I)\in\Theta_0,\ x\notin S}I.
\]

Residual run conflicts need cover only `W_0 minus D_x^0`, and residual
negative choices can kill the positive guard of either a residual or a
forced anchor.  The corrected report includes all three classes:

1. background-reduced central runs `mathfrak R^0`;
2. residual-anchor guards with factor `C_0x_e`; and
3. forced-anchor guards with anchor probability one.

The minimal-cover expansion safely overcounts nonmatching or repeated-
target choices.  Every residual cover has size at most `d+1` for a run and
at most `d` for a guard, so the permanent bound applies.

Contracted forced-anchor events are used in lifted form with their
deterministic anchor adjoined.  Deleting a conditioned anchor target is
safe by downward closure: its negative demands and positive guard vanish,
its reserved column remains unused, and no new incompatibility can be
created.  This makes target capping of the forced guard term legitimate.

Source-empty conflicts are absent because every candidate whose interval
contains `p` contains the nonempty core `F_p` in its label, so it cannot
delete those core coordinates at `p`.

## 9. Component cube

**Verdict: valid with the complete-family convention.**

Either adjoin every forced candidate to both endpoint matchings before
testing physical conflicts, or use the complete contracted conflict family
with lifted forced-target metadata.  Then:

- fixed conflicts have probability one;
- a conflict using both shores of one component is impossible;
- every other conflict is one atomic assignment of component bits; and
- hybrid conflicts spanning several components are included even if they
  occur in neither endpoint matching.

The target-capped alteration theorem therefore proves the component-cube
completion theorem exactly.

## 10. Final implication boundary

A conditional `B(k)+O(k)` theorem is proved if one physical
upper-complete deadline-resident chronology satisfies all of:

1. recursive shallow unit closure with `O(k)` total omissions;
2. a residual saturating matching law whose prefix graphs satisfy the
   alternating guard-switch bound;
3. background-aware run/guard pressure (7.10) of order `O(k)`;

or, alternatively, a complete two-matching component cube with capped
pressure `O(k)`.

No present PBBS theorem proves these hypotheses.  The fixed-chronology
spread obstruction proves that the matching measure cannot be introduced
as a diffuse law before the shallow closure cascade; the deadline-density
collision theorem separately excludes every uniform/common-fugacity
product pruning at that stage.  Neither statement proves that the cascade
fails, excludes asymmetric atomic fugacities, or excludes a concentrated
matching law.  Therefore no unconditional all-`k` upper bound is changed.
