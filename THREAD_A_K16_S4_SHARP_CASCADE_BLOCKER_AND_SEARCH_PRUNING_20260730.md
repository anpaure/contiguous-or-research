# S4 sharp anchors: blocker-cover cascade, exact five-fibre no-go, and search propagation

Date: 2026-07-30

Status: independent audit PASS.  The lower bound five is solver-free; the
strict five-rehost no-go is an exact finite maximal-core audit.  Both results
apply only to the nine sharp S4 hole-provider anchors.  They do not decide
the other 5,683 compatible anchors or any repeat-free parent layout.

## 1. Frozen objects and terminology

The two uncovered masks in the frozen S4 collar are

\[
S=0x31ce\subset L=0x7bce.
\]

The nine sharp compatible provider pairs are

\[
\{36,68,69\}\times\{2,3,133\},                         \tag{1.1}
\]

where the first coordinate is the shape for \(S\) and the second is the
shape for \(L\).  Their large-provider data are

\[
\begin{array}{c|c|c}
\text{shape}&Q_L&L\setminus F_L\\
\hline
2&\{0,1,2\}&0x7bce\\
3&\{0,1,2,3\}&0x7bce\\
133&\{0,1,2,3\}&0x18c6 .
\end{array}                                             \tag{1.2}
\]

Here \(0,1,2,3\) are the first four collar cells.  Every row in (1.2)
demands the coordinate

\[
b=0x0002.                                               \tag{1.3}
\]

Each sharp pair immediately displaces exactly three protected incumbent
targets.  Write this set as \(D(a)\) for anchor \(a\).  It is

\[
\begin{aligned}
D(a)&=\{0x73cc,0xb0cc,0xb0ce\},
  &&\text{for small shape }36,\\
D(a)&=\{0x3cc8,0x3ce8,0x73cc\},
  &&\text{for small shape }68\text{ or }69.
\end{aligned}                                           \tag{1.4}
\]

A protected target is called rehosted if it selects no incumbent-realized
provider.  Let \(R\) be the set of rehosted protected targets.  Every
completion through anchor \(a\) has \(D(a)\subseteq R\).

## 2. Unavoidable incumbent blockers

For a first-window cell \(p\), define

\[
C_p=\{T:\ b\notin T
 \text{ and every incumbent provider of }T\text{ contains }p\}.          \tag{2.1}
\]

After the three targets in (1.4) are removed optimistically, direct
reconstruction from the complete incumbent-host table gives

\[
\begin{array}{c|l|c}
p&C_p&|C_p|\\
\hline
0&\{0x31cc,0x33cc\}&2\\
1&\{0x338c,0x33cc,0x738c,0x77bc\}&4\\
2&\{0x130c,0x730c,0x731c,0x738c,0x77bc\}&5\\
3&\{0x030c,0x630c,0x631c,0x633c,0x673c,
      0x730c,0x731c,0x738c,0x77bc\}&9.
\end{array}                                             \tag{2.2}
\]

The table already quantifies over every incumbent interval of the six
multi-incumbent targets: membership in \(C_p\) means that all such choices
contain \(p\).  None of the two displaced triples in (1.4) meets (2.2).

### Lemma 2.1 (carrier-cell blocker implication)

If \(b\) survives in the maximal core \(K_p\) of a completion, then

\[
C_p\subseteq R.                                         \tag{2.3}
\]

#### Proof

If \(T\in C_p\) is not rehosted, its selected incumbent provider contains
\(p\).  Since \(b\notin T\), the maximal-intersection formula gives
\(K_p\subseteq T\), hence \(b\notin K_p\), a contradiction. \(\square\)

Since the large provider must reproduce \(b\), Lemma 2.1 gives the exact
necessary disjunction

\[
\bigvee_{p\in Q_L}\bigl(C_p\subseteq R\bigr).            \tag{2.4}
\]

This is stronger for search than the scalar lower bound: choosing the
carrier cell \(p\) forces every member of \(C_p\) away from all incumbent
providers containing \(p\).

## 3. Solver-free five-row lower bound

### Theorem 3.1 (sharp-anchor cascade floor)

Every completion through a sharp anchor rehosts at least five protected
targets.  If exactly five are rehosted, then the rehost set is necessarily

\[
R=D(a)\cup\{0x31cc,0x33cc\}.                            \tag{3.1}
\]

#### Proof

By (1.4), \(D(a)\subseteq R\) and \(|D(a)|=3\).  The blocker sets in (2.2)
are disjoint from \(D(a)\).  Equations (2.2)--(2.4) imply

\[
|R\setminus D(a)|
 \ge \min_{p\in Q_L}|C_p|=2.                            \tag{3.2}
\]

The unique size-two blocker set is \(C_0\), proving (3.1). \(\square\)

Thus the three-compensator budget is solver-free UNSAT.  The phrase
“\(0x31cc\) and \(0x33cc\) are necessary” is exact at equality in (3.2), or
while all other protected targets remain incumbent.  It is not an
unconditional clause for larger cascades: a larger rehost set may instead
contain all four, five, or nine blockers at another carrier cell.

The frozen v2 audit independently checks all demanded bits, all nine raw
anchors, and all 216 choices of incumbent intervals for the multi-incumbent
targets.  Its global minimum is two and its unique size-two minimizer is
\(\{0x31cc,0x33cc\}\) in every sharp anchor, agreeing with the one-bit proof.

## 4. Exact five-rehost fibre is empty

### Theorem 4.1 (strict sharp-root lower bound six)

No sharp-anchor completion has exactly five rehosted protected targets.
Consequently every sharp anchor has

\[
|R|\ge6.                                                \tag{4.1}
\]

#### Proof

By Theorem 3.1, a five-rehost completion must use precisely the set (3.1).
Pin every other protected target to an arbitrary incumbent-realized
provider.  The v2 audit enumerates every resulting valid maximal-core base.

For small shape \(36\), there are 24 valid bases for each large shape, and
in every one the individually unhostable relaxed rows are exactly

\[
\{0x33cc,0x73cc,0xb0cc,0xb0ce\}.                       \tag{4.2}
\]

For small shape \(68\) or \(69\), there are 36 valid bases for each large
shape, and all five relaxed rows are individually unhostable:

\[
\{0x31cc,0x33cc,0x3cc8,0x3ce8,0x73cc\}.                \tag{4.3}
\]

If a row is not feasible when added alone to a valid base, adding the other
relaxed rows can only shrink maximal cores and cannot restore it.  Therefore
no simultaneous choice for the five relaxed rows exists. \(\square\)

The finite step in this proof is not generic SAT.  It enumerates the
incumbent-\(Q\) product, computes the canonical maximal cores, and tests all
same-\(Q\) fixed-OR-dominant provider choices.  Invalid bases may be discarded
soundly: adding rows only shrinks cores, so it cannot repair a missing
provider bit or a zero cell.

## 5. Exact propagation theorem for the full provider search

Let \({\cal P}_t\) be the complete semantic-provider domain of protected
target \(t\), let \({\cal I}_t\subseteq{\cal P}_t\) be the providers
realized by an incumbent interval, and put
\({\cal N}_t={\cal P}_t\setminus{\cal I}_t\).  Choose exactly one provider
\(e_t\in{\cal P}_t\).  A proof-safe search should separate the rehost
decision from that choice:

\[
z_t=0\Rightarrow e_t\in{\cal I}_t,\qquad
z_t=1\Rightarrow e_t\in{\cal N}_t.                      \tag{5.1}
\]

In this frozen atlas, same-\((T,Q)\) fixed-OR dominance also preserves this
provenance split: 30 raw classes contain both incumbent and nonincumbent
rows, and the unique greatest-fixed-OR representative is incumbent-realized
in all 30.  This is an audited property of the present table, not an
automatic fact for another atlas.

### Theorem 5.1 (carrier branching and budget closure)

Fix a sharp anchor and a protected-rehost budget \(B\).

1. Force \(z_t=1\) for every \(t\in D(a)\).
2. Branch on a carrier \(p\in Q_L\) for the demanded bit \(b\).
3. In branch \(p\), delete from every target \(T\) with \(b\notin T\) every
   provider whose support contains \(p\).
4. If this deletes all incumbent providers of \(T\), force \(z_T=1\); if it
   deletes all providers, reject the branch.
5. Iterate tentative maximal-core option deletion, forced rehosts and
   singleton provider choices to a fixed point.  Here a candidate provider
   is tentatively adjoined: cap every cell of its support by its target, and
   delete it only if the resulting system has a zero core, fails one of its
   demanded bits, or invalidates an already selected row.

Every operation is logically sound, and the carrier branches are complete.

#### Proof

The large row needs \(b\) in at least one \(K_p\), so some branch in step 2
is taken.  In that branch, any selected provider for a mask omitting \(b\)
and containing \(p\) would force \(b\notin K_p\); step 3 is therefore exact.
Steps 4--5 follow from monotonicity after the candidate itself has been
adjoined.  This qualification is essential: comparison with the unmodified
current core is not sound, because a later selected row may shrink a current
core to the candidate target.  Once the candidate has been imposed, however,
later selections only intersect the resulting cores further, so a zero core
or missing demanded bit can never recover. \(\square\)

At the root, the incumbent liberation costs of the branches are

\[
2,\ 4,\ 5,\ 9                                           \tag{5.2}
\]

for \(p=0,1,2,3\), omitting \(p=3\) for large shape 2.  Search should try
\(p=0\) first.  This ordering is heuristic; the domain deletions inside each
branch are exact.

Theorems 3.1 and 4.1 give certified budget propagation:

* prune every sharp root when \(B\le5\);
* when \(B=6\), only the \(p=0\) carrier branch fits, so
  \(0x31cc\) and \(0x33cc\) are forced to providers avoiding cell 0, and at
  least one further protected target outside (3.1) must be rehosted;
* for larger budgets, retain exactly those carrier branches whose root cost
  fits: \(p=1\) first fits at \(B=7\), \(p=2\) at \(B=8\), and \(p=3\) at
  \(B=12\); the last branch is absent for large shape 2.  Once a branch
  other than \(p=0\) fits, the named pair is an ordering preference, not an
  unconditional implication.

More generally, with already forced rehost set \(R_0\) satisfying
\(D(a)\subseteq R_0\), the blocker lower bound is

\[
\operatorname{LB}(R_0)
=|R_0|+\min_{p\in Q_L}|C_p\setminus R_0|.               \tag{5.3}
\]

Prune when \(\operatorname{LB}(R_0)>B\).  Do not add overlapping blocker
costs independently; use set union or an exact hitting-set lower bound.
This scalar bound does not subsume Theorem 4.1: at \(R_0=D(a)\) it returns
five, whereas the exact equality-fibre audit raises the bound to six.  A
standalone version for an arbitrary tentative set \(R_0\) replaces it by
\(R^*=R_0\cup D(a)\) on both occurrences in (5.3).

## 6. Ordering all 5,692 roots

The complete compatible-pair census has nine sharp roots with three directly
displaced targets; every other root directly displaces at least four.
Therefore the protected-rehost budget-three face is solver-free UNSAT across
all 5,692 roots:

* the nine sharp roots need at least six by Theorem 4.1;
* the other 5,683 roots need at least four before any cascade propagation.

This does not close the global budget-four or budget-five faces, because
nonsharp roots lie outside the v2 audit.

For the nine sharp roots, bounded-budget proof search may order roots by
increasing slack \(B-\operatorname{LB}\), then use carrier cost (5.2), forced
targets, and minimum surviving provider-domain size.  The fixed table (2.2)
and costs (5.2) must not be transplanted to a nonsharp root: its support,
fixed OR and demanded bits may differ.  For each such root one must recompute
the demanded-bit carrier blockers, using direct displacement only as the
generic precomputed lower bound.  For witness search, roots with the smallest
certified lower bound may be tried first.  These are traversal policies only;
an UNSAT conclusion must come from completed exact branches.

The nine raw sharp anchors reduce to six distinct \(Q\)-roots because the
shape-133 fixed OR dominates shape 3 on their common support.  This
dominance is one-way: UNSAT for the dominant shape-133 root also excludes
shape 3, so six roots suffice for a complete UNSAT or existential-search
portfolio.  A SAT witness for shape 133 does not by itself certify the
dominated raw shape-3 presentation; per-presentation SAT classification must
retain that distinction.

## 7. Independent audit and exact scope

The v2 artifact and reproducer are:

    scratch/k16_s4_sharp_pair_five_rehost_floor_20260730.audit.json
      SHA 85deda18dbd83f6be1662e75181152504c99a689952535ae24d3fe84f879255c

    scratch/audit_k16_s4_sharp_pair_five_rehost_floor_20260730.py
      SHA 8fbfcd751b2ab4a1ebd1a1d75f4c7638bca173f67e9c6b746336603adfb6c6b0

    MATH_AUDIT_K16_S4_SHARP_PAIR_FIVE_REHOST_FLOOR_20260730.md
      author-reported frozen SHA
      3b2a2e9f8a56740ce0aef2248699544e09906108140c4458639157320714e646;
      current workspace-path SHA at this audit
      91f5778bfbb1f9e1303eaf08649fb613e2c98f8a18e46ba330f3328e2dd3c701

The reproducer pins the complete semantic-incidence table at

    5df821abdd06e74a7aa1f8206aa0bc483d55afb0afaaf8c7cd042fd52def8cd5.

The audit checked the option collapse, all 216 incumbent-\(Q\) assignments,
the blocker minimization, all valid five-fibre bases, and monotonicity of the
individual-dead-row certificate.  The lower bound five also has the direct
solver-free proof in Sections 2--3.

The note pathname has therefore drifted from the author-reported frozen note
hash.  This is a lineage caveat, not a mathematical failure: the JSON and
reproducer match their stated v2 hashes, and the current note contains the
same strict five-fibre conclusion.  Any archival claim should preserve the
frozen note bytes or cite the current hash explicitly.

This is a residual-provider theorem for the frozen seed-4 S4 calibration.
The full S4 fibre is independently impossible already by its fixed repeated
middle-delivery ghost.  The blocker theorem remains valuable as a portable
search rule for a future equality-valid parent atlas, but it changes no K16
bound.
