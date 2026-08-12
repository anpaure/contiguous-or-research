# Thread D: K16 any-unit-voltage subgroup orbit audit

**Date:** 2026-07-30  
**Scope:** source-independent one-block K16 two-rail quotient model.  This is
an algebraic audit of the unit-multiplier reduction and of the four
strengthened AAAB collars.  It uses no solver outcome, source carrier, edit
radius, or seam assumption.

## 1. Exact symmetry and its necessary hypothesis

Put $n=15$, let the distinguished top coordinate be fixed, and let


\[
 U=\mathbb Z_{15}^{\times}=\{1,2,4,7,8,11,13,14\}.
\]

For $u\in U$, multiplication of old coordinates,

\[
 \mu_u:x\longmapsto ux\pmod {15},
\]

conjugates translation by one to translation by $u$.  It therefore induces
a permutation of every necklace layer and of the complete transition-option
catalogue.  It preserves shores, Johnson adjacency, the one-A-block/one-B-
block condition, binary rail positions, and insertion-history residence.
It also fixes both installed subgroup targets

\[
 H=\{0,3,6,9,12\},\qquad H\cup\{\mathrm{top}\},
\]

because $uH=H$.

There is a small but important gauge term in the option increments.  Write
$\phi_u$ for the induced permutation of quotient-node indices.  If
\(\mu_u(R_v)=\rho^{a_v}R_{\phi_u(v)}\) for the chosen canonical
representative at node $v$, then an option $v\to w$ of increment $\delta$
is sent to an
option of increment

\[
 \delta'=u\delta+a_w-a_v\pmod {15}.
\]

On a selected directed 2-factor the $a$-terms telescope, so total quotient
voltage transforms as

\[
 V\longmapsto uV\pmod {15}.
\]

Consequently the class $V\in U$ is invariant, while the normalized slice
$V=1$ is not.  The reduction below is therefore valid precisely with the
new `--any-unit-voltage` acceptance set (or before choosing a voltage gauge).
It is **not** valid by simply deleting cases from the old fixed-voltage-one
portfolio.

Canonical integer labels must likewise be transformed as

\[
 L\longmapsto \operatorname{can}(uL),
\]

not by ordinary integer multiplication.  Raw node indices and raw option IDs
are gauge-dependent.

## 2. The nine q2 middles have three unit orbits

The nine exceptional A nodes and their canonical old-coordinate masks are

\[
\begin{array}{c|c}
378&H\cup\{1,2\}\\
380&H\cup\{1,4\}\\
381&H\cup\{2,4\}\\
383&H\cup\{1,5\}\\
384&H\cup\{2,5\}\\
395&H\cup\{1,7\}\\
396&H\cup\{2,7\}\\
405&H\cup\{1,8\}\\
406&H\cup\{2,8\}.
\end{array}
\]

Their exact $U$-orbits are

\[
\begin{aligned}
 \mathcal O_{120}^{(1)}&=\{378,381,383,405\},\\
 \mathcal O_{80}&=\{380,384,395,406\},\\
 \mathcal O_{120}^{(2)}&=\{396\}.
\end{aligned}
\]

The subscripts record the q2-prefix count at each middle.  One convenient
choice of gauges to the displayed representatives is

\[
\begin{array}{c|cccc}
\text{target representative }378&m=378&m=381&m=383&m=405\\
u_m&1&7&4&2\\ \hline
\text{target representative }380&m=380&m=384&m=395&m=406\\
u_m&1&11&7&2\\ \hline
\text{target representative }396&m=396\\
u_m&1.
\end{array}
\]

The seven q3 shore patterns are unchanged by every multiplier.  Hence the
old (9\times7=63) existential cover reduces, in the any-unit-voltage class,
to exactly

\[
 \{\mathcal O_{120}^{(1)},\mathcal O_{80},
   \mathcal O_{120}^{(2)}\}\times
 \{AAAB,ABBB,BBAA,AABB,BAAA,BBBA,BBBB\},
\]

namely 21 orbit cases.

For an exact disjoint portfolio, the old first-*node* exclusions must be
replaced by first-*orbit* exclusions.  In an AAAB case the terminal-position
theorem already gives a unique AAAB middle, hence a unique middle orbit.  In
a non-AAAB case one may choose the first q3 pattern and first q2 middle orbit.
The existing individual-node tie-break is not itself multiplier invariant.

## 3. Exact map of the four strengthened AAAB branches

The four smallest branches are precisely the orbit $\mathcal O_{80}$.  Under
the gauges (u_m) above, all four become `AAAB_A380`; their shifted q2 collar
label becomes 4683:

\[
\begin{array}{c|c|c|c}
\text{old branch}&u_m&\text{old shifted q2 label}&
 \operatorname{can}(u_m L)\\ \hline
AAAB_{380}&1&4683&4683\\
AAAB_{384}&11&4685&4683\\
AAAB_{395}&7&4683&4683\\
AAAB_{406}&2&4685&4683.
\end{array}
\]

The exact five next-collar alternatives transform as follows:

\[
\begin{array}{c|c|ccccc}
\text{middle}&u_m&\multicolumn{5}{c}{\text{old label}\mapsto
\text{label at middle }380}\\ \hline
380&1&587\mapsto587&601\mapsto601&713\mapsto713&
1609\mapsto1609&2341\mapsto2341\\
384&11&589\mapsto713&617\mapsto1609&841\mapsto2341&
1171\mapsto601&2633\mapsto587\\
395&7&587\mapsto1609&601\mapsto587&713\mapsto713&
1609\mapsto2341&2341\mapsto601\\
406&2&589\mapsto713&617\mapsto2341&841\mapsto601&
1171\mapsto587&2633\mapsto1609.
\end{array}
\]

After fixing middle 380, its stabilizer is ({1,4}).  Multiplication by four
acts on the five labels by

\[
 587\leftrightarrow2341,qquad
 601\leftrightarrow1609,qquad
 713\longmapsto713.
\]

Thus the twenty branch--collar pairs form exactly three $U$-orbits:

\[
\begin{aligned}
\mathcal C_1=\{&
(380,587),(406,617),(380,2341),(395,1609),\\
& (406,1171),(384,2633),(395,601),(384,841)\},\\
\mathcal C_2=\{&
(380,601),(406,2633),(380,1609),(395,587),\\
& (406,841),(384,1171),(395,2341),(384,617)\},\\
\mathcal C_3=\{&
(380,713),(406,589),(395,713),(384,589)\}.
\end{aligned}
\]

Therefore an orbit-normalized AAAB-$\mathcal O_{80}$ next-collar portfolio
needs only the representatives 587, 601, and 713, provided no additional
constraint breaks the multiplier symmetry.  Running five labels at the
fixed representative is correct but has two redundant isomorphic pairs.

## 4. Clauses preserved at option level

Under the semantic option permutation induced by $\mu_u$, the following
families are isomorphic, with exactly the same cardinalities:

1. incoming/outgoing degree-one rows and the one-AB/one-BA rows;
2. binary rail-successor and position clauses, including
   `position_A(middle)=427`;
3. the three-step history clauses, after applying the node-relative affine
   relabelling $x\mapsto ux-a_v$ to stored old-coordinate values;
4. all complete q1 palette rows and the exact at-most-two/repeat-token rows;
5. the 80 q2-prefix AND equivalences and their positive OR;
6. the ten local excess-two three-option no-goods;
7. each 640-clause next-collar family, with its label replaced by
   $\operatorname{can}(uL)$; and
8. the two marginal Hall graphs and all reported matching/degree statistics.

In particular, a conditional row

\[
 \neg p_{ef}\vee\neg x_s\vee\bigvee_{g\in G_{ef,s,L}}x_g
\]

is carried bijectively to the corresponding row for the transformed prefix,
seam, and label.  The option-ID SHA values in the four existing audits need
not agree, because option IDs are not invariant; an orbit audit must compare
the transformed semantic tuples.

The following objects are **not** automatically preserved:

* the terminal equation $V=1$ (replace it by $V\in U$);
* the individual-node canonical first-witness exclusions (replace them by
  orbit-level exclusions);
* a raw option-ID clause or raw semantic-row digest without applying the
  option permutation; and
* any source-relative hint, edit-radius restriction, fixed seam, or other
  coordinate-labelled symmetry breaker.

No such extra restriction is present in the stated source-independent
subgroup problem.  The 63-to-21 reduction and the further 20-to-3 collar
reduction are therefore exact for that class.  They are symmetry reductions,
not feasibility or UNSAT results.

## 5. Inputs cross-audited

The reduction is aligned with the exact catalogues and collar ledgers in

```text
THREAD_D_K16_PERIOD_THREE_SUBGROUP_BRANCH_AUDIT_20260730.md
THREAD_D_K16_AAAB_TERMINAL_POSITION_AND_Q1_HALL_AUDIT_20260730.md
THREAD_D_K16_AAAB_NEXT_COLLAR_AND_MARGINAL_HALL_20260730.md
scratch/k16_subgroup_shadow_geometry_20260730.audit.json
scratch/threadD_k16_aaab_branch_hall_structure_20260730.audit.json
scratch/threadD_k16_aaab_next_collar_hall_20260730.audit.json
```

The current executable's `--any-unit-voltage` terminal set is exactly
$\{1,2,4,7,8,11,13,14\}$ at $n=15$, matching the hypothesis above.

## 6. Executable orbit interface

`scratch/solve_even_two_rail_joint_history_kissat_20260730.py` now accepts
`--preinstall-q23-orbit-branch PATTERN_A<m>`, with
\(m\in\{380,378,396\}\).  It rejects the flag unless the voltage domain is
all of \(U(15)\), or the exact stabilizer-orbit residue set is supplied:

\[
 380:(1,2,7,11),\qquad 378:(1,2,4,7),\qquad 396:(1).
\]

The orbit formulas are an overlapping exact cover, not the old nodewise
disjoint partition.  They therefore add no individual-node first-witness
exclusions.  Exact q1 repeat-token clauses and the AAAB one-step
colour/order/history rows are generated from semantic options after the
representative is chosen.  The lightweight regression exercises all three
AAAB representatives: 22,400 successor rows at 380 and 33,600 at each of
378 and 396, with zero local tight-colour repeats.  No timed branch solve was
used to infer this interface.
