# The relabelled four-block C8 has a common source basis, but zero exterior-ear gain and no simple-owner lift

Date: 2026-08-01  
Status: exact source-language, lower identity-cap, matching-action, and
physical-scope theorem.  It gives a common source-level compiler basis and
an exact `ell=alpha` calculation.  It also proves that the literal four-block
word is not an occurrence-simple owner/q1 carrier and that its four guard
spares are not protected exterior-ear sinks.  No quotient weave or
`B(k)+O(1)` theorem is claimed.

## 0. Verdict

Let `Q^0,Q^1` be the **unexpanded sharp source inverses** of the resident
quaternary octagon.  Thus

\[
                         |Q^\epsilon|=9d+23.                 \tag{0.1}
\]

On the four active labels put

\[
 \alpha=(a_0\ a_2),\qquad \beta=(a_1\ a_3),\qquad
 V=\{1,\beta,\alpha,\alpha\beta\}.                         \tag{0.2}
\]

For `pi in V`, define the guarded source block

\[
 G_{\pi,\epsilon}=L_\pi\,(\pi Q^\epsilon)\,R_\pi,
 \quad
 L_\pi=\{\pi a_0,\pi a_1\},\quad
 R_\pi=\{\pi a_1,\pi a_2\}.                               \tag{0.3}
\]

In the order `(1,beta,alpha,alpha beta)`, put

\[
 \begin{aligned}
 W^-&=G_{1,0}G_{\beta,1}G_{\alpha,1}G_{\alpha\beta,0},\\
 W^+&=G_{1,1}G_{\beta,0}G_{\alpha,0}G_{\alpha\beta,1}.
 \end{aligned}                                               \tag{0.4}
\]

The positive source fact is stronger than support equality:

\[
                   \Sigma(W^-)=\Sigma(W^+),                 \tag{0.5}
\]

where `Sigma` records pointwise prefixes, pointwise suffixes, and the
complete interval-OR multiset separately at every width.

However, the exact lower compiler calculation is **rank neutral**.  On the
complete strict-lower exact-value bank of source intervals of widths at most
`d`, there is one physical cell basis valid in both phases.  For a
minimum-damage such basis,

\[
 \boxed{
   \ell=\alpha_{\rm restore}=2d^2+26d-24,
   \qquad \alpha_{\rm restore}-\ell=0.}                      \tag{0.6}
\]

Every repair is a closed alternating `C8`; none ends at a cell unused by the
initial matching.  The eight guard letters leave four parallel unused
addresses after their four literal target values are matched, but full
signature protection gives each such cell only its already-saturated guard
target.  Their protected exterior-ear rank for a distinct task is zero.

There is a more basic physical obstruction.  The four central owner words
have

\[
 \begin{array}{c|cc|c}
 &\text{occurrences}&\text{distinct values}&\text{overload}\\ \hline
 \text{owners}&32d+92&8d+24&24d+68\\
 \text{lower q1}&32d+88&8d+24&24d+64.
 \end{array}                                                 \tag{0.7}
\]

Almost every owner occurs four times.  Hence the literal four-block macro
cannot coexist with an occurrence-labelled simple owner embedding.  The
common source basis is real, but it is source-level only.

At the smallest depth `d=2`, this already reads

\[
 |W^\pm|=172,\quad |\mathcal T_2|=85,\quad
 \ell=\alpha=36,
\quad 156\text{ owner occurrences on }40\text{ owners}.       \tag{0.8}
\]

Thus `d=2` is a literal finite counterexample to the inference

```text
full graded source equality + parallel guard cells
    => positive exterior-ear rank or a physical simple-owner C8 lift.
```

## 1. Exact graded identity

Let

\[
                         \rho=(a_0\ a_1\ a_2\ a_3).          \tag{1.1}
\]

The two octagon phases have identical internal OR decks.  Their only
prefix discrepancy is screened by `{a0,a1}` and their only suffix
discrepancy is screened by `{a1,a2}`.  Relabelling gives the same statement
for every `pi` in (0.2).  Thus the two versions of every guarded block have
pointwise-equal prefix and suffix profiles.

For an interval contained in one block, the four Klein relabellings and the
phase character

\[
        (0,1,1,0)\longleftrightarrow(1,0,0,1)                 \tag{1.2}
\]

pair every phase-only OR occurrence.  An interval crossing one or more
block joins is determined by a suffix profile, zero or more complete block
totals, and a prefix profile.  All of those data agree pointwise.  The
graded block-transposition lemma therefore gives (0.5), including
multiplicity and arbitrary fixed exterior context.

This argument uses the unsplit guards in (0.3).  It is distinct from the
earlier two-host expansion of one octagon phase.

## 2. The strict-lower transition graph

Suppress a common fixed core, so the owner rank is `r=d+3`.  Let

\[
 \mathcal C_d=\{[i,j]:1\le j-i+1\le d,
                    |\bigvee_{t=i}^jW^-_t|<r\},              \tag{2.1}
\]

and put

\[
             v^\epsilon(c)=\bigvee_{t\in c}W^\epsilon_t.
                                                                    \tag{2.2}
\]

The active-trace formulas of the sharp inverse give the following exact
cellwise statement.

### Lemma 2.1 (quarter-turn dichotomy)

For every `c in C_d`,

\[
                  v^+(c)=v^-(c)
                 \quad\hbox{or}\quad
                  v^+(c)=\rho v^-(c).                         \tag{2.3}
\]

In the second case the active part of the value has a four-element
`rho`-orbit.  No changed value has orbit two.

#### Proof

A cell of width at most `d` meets at most one guarded block join.  Substitute
the eight phase-changing sharp-source addresses

\[
 \begin{split}
 d+4,&\ 2d+5,\ 3d+5,\ 3d+8,\\
 5d+16,&\ 6d+17,\ 7d+17,\ 7d+20
 \end{split}                                                  \tag{2.4}
\]

inside each block.  The phase vector (1.2) changes every met active trace by
the same quarter-turn `rho`; the unsplit guards make the same statement at a
join.  If the interval already contains a `rho`-invariant active set, the
value is unchanged.  Otherwise the met active trace is one of the one- or
three-label cyclic traces, whose orbit has size four.  Fillers and the core
are fixed.  This proves (2.3).  \(\square\)

Make a directed multigraph `D_d` on the distinct target values by giving
each physical cell the arc

\[
                         v^-(c)\longrightarrow v^+(c).        \tag{2.5}
\]

Graded deck equality says that indegree equals outdegree at every target.
By Lemma 2.1, a nonloop component is therefore one full directed
`rho`-cycle.  The complete interval-shape census is:

\[
\begin{array}{c|c|c|c}
\text{component type}&\text{number}&
 \text{multiplicity of each cycle arc}&\text{loop support}\\ \hline
\text{isolated loop target}&4d^2+11d+11&0&\text{nonempty}\\
\text{pure }C_8\text{, internal}&\binom{d+1}{2}&4&0\\
\text{pure }C_8\text{, boundary}&4d-2&2&0\\
\text{mixed }C_8&2(d-2)&2&\text{two opposite loops, mult. }2.
\end{array}                                                   \tag{2.6}
\]

Here `C8` refers to the bipartite target--cell support: after identifying
the two target copies, (2.5) is a directed four-cycle.  The count follows by
sorting intervals according to whether they meet two internal active-trace
fronts, one guarded boundary front, or one of the two overlap rays.  The
respective shape counts are

\[
             \sum_{h=1}^dh=\binom{d+1}{2},\qquad
             4d-2,\qquad 2(d-2).                            \tag{2.7}
\]

All other distinct values are fixed loops; direct deduplication of the
phase-common interval shapes gives the first row.  Equivalently, summing
the rows gives

\[
             |\mathcal T_d|=6d^2+37d-13.                    \tag{2.8}
\]

The dependency-free replay performs this same classification on literal
sets and physical addresses.

## 3. One common physical basis and the exact `ell/alpha` calculation

For every isolated target in (2.6), choose one loop cell.  In every
nontrivial component, choose one physical representative of each of its
four directed `rho` arcs.  Call the selected cell set `B_d`.

In phase minus, assign each selected arc cell to its tail.  In phase plus,
assign it to its head.  The tails and heads both enumerate the four targets
of that component, so `B_d` is a target-saturating physical cell basis in
both phases.  In a mixed component the two opposite loop cells cannot occur
in any such common basis: choosing either loop blocks the unique incoming
cycle cell needed by its predecessor.  Thus every common basis of minimum
damage uses all four cycle arcs.

The number of nontrivial components is

\[
 c_d=\binom{d+1}{2}+(4d-2)+2(d-2)
     ={d^2+13d-12\over2}.                                    \tag{3.1}
\]

All four selected assignments in each component change target at their
physical address.  Consequently

\[
                         \ell=4c_d=2d^2+26d-24.              \tag{3.2}
\]

Delete those old edges.  Every selected cycle cell and every cycle target
is now unmatched.  The four phase-plus edges in that component are four
pairwise-disjoint length-one augmenting paths.  Components are disjoint, so

\[
                         \alpha_{\rm restore}=\ell.           \tag{3.3}
\]

No restoring path ends at a cell unused by the initial matching: its cell
belongs to `B_d` and was used by the old cycle matching.  The symmetric
difference of the two complete assignments is exactly `c_d` closed
alternating `C8`s.  Hence

\[
                  \alpha_{\rm restore}-\ell=0.               \tag{3.4}
\]

This is the exact compiler meaning of the coefficientwise `4g_8`
relation.  Its multiplicity supplies parallel occurrence choices, not new
literal target rank.  Counting coefficient mass as additional compiler
tasks would be a quantifier error: the OR problem has one vertex per target
mask.

For the restoration task set itself, the all-cut rank is perfect:

\[
                  r_{\rm restore}(P_X)=|X|\qquad(X\subseteq U).
                                                                    \tag{3.5}
\]

Equation (3.5) restores the deleted basis.  It is not an exterior-ear
inequality because its sinks were initially used.

## 4. The guard cells are parallel spares, not exterior ears

The eight literal guards in the four blocks take exactly four values:

\[
 H_i=\{a_i,a_{i+1}\},\qquad i\pmod4,                         \tag{4.1}
\]

and each value occurs in exactly two singleton cells, once as a left guard
and once as a right guard.  No other strict-lower exact-value cell has value
`H_i`.  Matching the four targets therefore leaves exactly four unused
guard cells.

These are genuine **basis-exchange** spares.  They are not exterior-ear
sinks.  Proposition 3.2 of the octagon tensor says that a left guard screens
the prefix discrepancy only if it contains both of its displayed labels,
and likewise on the right.  Since the guard is itself the two-label source
letter, any protected cap must equal `H_i`.  Thus a guard cell has no legal
protected incidence to a distinct target.

In the exact protected identity-cap graph, the two copies of `H_i` form an
isolated parallel class.  The empty copy can move the matching of `H_i`, but
the target is already saturated.  For one distinct exterior task `u`,

\[
                     r_{\rm ext}(P_{\{u\}})=0,
              \qquad |\{u\}|-r_{\rm ext}(P_{\{u\}})=1.       \tag{4.2}

This is the smallest Rado cut.  Four address spares do not imply even one
unit of exterior target rank.

A richer ambient cap may supply nonlocal incidences to other cells.  Such
edges are precisely the still-unproved exterior-ear bank; they are not a
consequence of (0.5) or of the guards.

## 5. Incompatibility with a simple owner embedding

The central owner rows are obtained before choosing any lower compiler
matching.  Their exact multiplicity histogram is

\[
                 2^2\,4^{,8d+22},                            \tag{5.1}
\]

and the lower-q1 histogram is

\[
                 2^4\,4^{,8d+20}.                            \tag{5.2}
\]

Hence (0.7).  A simple owner factor has capacity one at every central owner,
so the literal four-block demand already violates that partition capacity
by `24d+68`.  Choosing a compiler basis cannot change (5.1).

Overlapping consecutive source blocks in `d` common letters does not repair
the issue.  Such an overlap creates neither a new nor an identified
length-`d+1` owner window, so owner occurrence counts still add exactly.
The largest phase-common literal overlap in fact misses six required owners
and creates fourteen nonrequired ones in each state.

Therefore the positive source basis of Section 3 cannot coexist with an
occurrence-labelled simple owner embedding in the literal four-block
geometry.  A surviving route must construct a new quotient weave which
identifies/rethreads the repeated owner occurrences while retaining the
source `C8` action and an actual exterior compiler edge.

## 6. Scope and replay

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_c8_fourblock_source_common_basis_and_ear_nogo_20260801.py --write
```

The replay checks `2<=d<=24`:

1. the literal words (0.4), full width-graded decks, and pointwise boundary
   profiles;
2. every strict-lower physical cell and the quarter-turn dichotomy;
3. all component counts and physical multiplicities in (2.6);
4. an explicit common basis, (3.2)--(3.4), and the absence of an initially
   unused restoration endpoint;
5. the exact eight-cell/four-target guard bank and singleton Rado cut; and
6. the owner and lower-q1 overloads.

It reports

```text
PASS_C8_FOURBLOCK_SOURCE_COMMON_BASIS_AND_EAR_NOGO
```

The finite replay audits the displayed literal formulas.  The proofs above
use the all-`d` sharp-source addresses and interval-shape classification;
they do not extrapolate the theorem merely from the checked range.

