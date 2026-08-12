# Low targets reduce to one-cell mandatory-core Hall on native PBBS hook components

**Date:** 2026-08-06  
**Method:** maximal-envelope necessity, mandatory-core localization, exact
hook-sector enumeration, and binomial counting; no search  
**Status:** unconditional reduction and sharp few-component obstruction.
It proves the exact source-level ticket criterion for every rank and shows
that one or any fixed number of physical PBBS components cannot carry the
complete ranks `2,...,d` atlas.  The hook sector has an enormous average
ticket surplus, but the required worst-orbit/Hall statement remains open.

## 1. Exact one-cell ticket criterion

Let

\[
                         T=(T_i)_{i\in\mathbb Z_L}
\]

be a cyclic simple rank-`m` Johnson component whose positive coordinate
runs have length at least `d+1`.  Put

\[
 P_t=\bigcap_{a=0}^{d}T_{t-a},
 \qquad
 F_t=(P_t\setminus P_{t-1})\cup(P_t\setminus P_{t+1}).
\tag{1.1}
\]

Then `P` is the maximal depth-`d` antecedent and every antecedent `A`
with `D^dA=T` satisfies

\[
                         F_t\subseteq A_t\subseteq P_t.
\tag{1.2}
\]

For a simple Johnson trace,

\[
                         F_t=\{\iota_t,\delta_t\},
\tag{1.3}
\]

where the two labels may coincide.  Thus `|F_t|` is one or two.

### Theorem 1.1 (one-cell ticket iff mandatory core fits)

Fix a nonempty target `S`.  There is an antecedent which equals `P` away
from one position `t`, has `A_t=S`, and still satisfies `D^dA=T` if and
only if

\[
                         \boxed{F_t\subseteq S\subseteq P_t.}
\tag{1.4}
\]

#### Proof

Necessity is (1.2).  Conversely, take the free bank to be the singleton
interval `{t}`.  It has length one, at most `d`, and the proposed letter
retains `F_t`.  The mandatory-core short-gap theorem then gives
`D^dA=T`.  `square`

At an exact length-`d+1` coordinate run, the two labels in (1.3)
coincide.  If its coordinate is `x`, (1.4) becomes simply

\[
                         x\in S\subseteq P_t.
\tag{1.5}
\]

Thus one native singleton ticket is automatically a ticket for every
larger target contained in its envelope.

## 2. Simultaneous thinning

The one-cell operations also compose under an exact local condition.

### Theorem 2.1 (short-block atlas)

Let `Z` be a set of source positions such that every maximal cyclic block
of consecutive positions in `Z` has length at most `d`.  Assign a nonempty
target `S_t` to every `t in Z` and suppose

\[
                         F_t\subseteq S_t\subseteq P_t.
\tag{2.1}
\]

Define

\[
 A_t=\begin{cases}
 S_t,&t\in Z,\\
 P_t,&t\notin Z.
 \end{cases}
\tag{2.2}
\]

Then

\[
                         D^dA=T.
\tag{2.3}

If the positions in `Z` are distinct, (2.2) gives occurrence-disjoint
literal width-one tickets for all assigned targets.

#### Proof

The set `Z` is a union of free gaps of length at most `d`.  Equation (2.1)
retains every mandatory core and never exceeds the maximal envelope.
Apply short-gap localization.  `square`

In particular, choosing at most one ticket on each PBBS component makes
the operations completely independent and automatically satisfies the
theorem.

## 3. Endpoint graphs and the exact PBBS reduction

For each envelope value `U` of rank

\[
                         R=m-d,
\tag{3.1}
\]

record the loop or edge `F_t` carried by its occurrence.  Call the
resulting occurrence-labelled multigraph the **depth-`d` endpoint graph**.
A rank-`s` target has a one-cell ticket precisely when it contains one
recorded loop/edge and is contained in that edge's envelope.

Equivalently, define the bipartite graph

\[
 \mathcal H_s=(\binom{[n]}s,\mathcal Z_d;E),
\tag{3.2}
\]

where `mathcal Z_d` is any chosen bank of resident PBBS source positions
and

\[
                         S\sim t
 \quad\Longleftrightarrow\quad
                         F_t\subseteq S\subseteq P_t.
\tag{3.3}

Then a matching saturating the left shore gives a simultaneous literal
rank-`s` atlas, provided its chosen positions obey the short-block
condition of Theorem 2.1.  If the right shore is first quotiented to
physical PBBS components and `S` is joined to a component when that
component has at least one occurrence satisfying (3.3), ordinary Hall

\[
                         |N(\mathcal X)|\ge|\mathcal X|
 \quad
 (\mathcal X\subseteq\binom{[n]}s)
\tag{3.4}

is already sufficient: choose one ticket per matched component.

This is the exact next gate after the native singleton theorem.  It is an
ordinary occurrence-labelled Hall problem, not a common-cap or upper-deck
problem.  Once the cells are selected, owner chronology and every inherited
owner-interval upper witness remain unchanged because `D^dA=T`.

## 4. A sharp obstruction to one or a few components

One physical component cannot possibly contain the complete low atlas.
There are two independent reasons.

### 4.1 Simultaneous occurrence count

A gamma-one hook component of height `h=d+1` has

\[
                         L=n(2d+1)
\tag{4.1}

source positions.  Since a physical cell has one literal value, `H`
such components can simultaneously realize at most `HL` distinct
width-one targets.  Hence a complete rank-`s` atlas requires

\[
                         \boxed{
 H\ge {\binom ns\over n(2d+1)}.}
\tag{4.2}

For `s=d=Theta(sqrt(m))`, the right side is
`exp(Theta(sqrt(m) log m))`.  Thus "one/few physical components" is
impossible even before PBBS geometry is considered.

This conclusion is not an artefact of insisting on width one.  A cyclic
word of length `L` has at most `L^2` nonempty cyclic intervals, hence at
most `L^2` target values with occurrence labels.  Even an unrestricted
interval atlas on `H` such components requires

\[
                         H\ge {\binom ns\over L^2}.
\tag{4.2a}
\]

For `s=d`, a fixed number of components is still exponentially
insufficient.

### 4.2 Candidate-support count

At a position with `|F_t|=f`, the number of rank-`s` targets satisfying
(3.3) is exactly

\[
                         \binom{R-f}{s-f}.
\tag{4.3}

This is maximized at `f=1`, so one length-`L` component can offer a
candidate to at most

\[
                         L\binom{R-1}{s-1}
\tag{4.4}

rank-`s` targets.  Relative to all rank-`s` targets, this is at most

\[
 {L\binom{R-1}{s-1}\over\binom ns}
 ={Ls\over n}
   {\binom{R-1}{s-1}\over\binom{n-1}{s-1}}
 \le
 (2d+1)s
 \left({R\over n-s+1}\right)^{s-1}.
\tag{4.5}

For `s=d=o(m)`, the last expression is

\[
                         \exp(-\Theta(d)).
\tag{4.6}

Thus a fixed number of hook components does not merely lack enough cells:
it fails to offer any candidate at all to almost every rank-`d` target.
Any native proof must use a large action-angle bank.

## 5. Exact scalar supply in the complete hook sector

The necessary large bank is present numerically.  Continue with

\[
 h=d+1,
 \quad p=2d+1,
 \quad b=m-d-1,
 \quad R=m-d.
\tag{5.1}

Hook rooted shapes are weak compositions of `b` into `p` slots.  Their
number is

\[
                         \Omega=\binom{b+p-1}{p-1}.
\tag{5.2}

The number whose terminal slot is zero is

\[
                         \Omega_0=\binom{b+p-2}{p-2}
                         =\binom{m+d-2}{2d-1}.
\tag{5.3}

Every such rooted phase starts an exact length-`d+1` run.  After the `n`
physical root placements, the hook sector therefore contains exactly

\[
                         n\Omega_0
\tag{5.4}

native loop positions `F_t={x}`.  Counting every target which each loop
could carry, the exact number of rank-`s` candidate incidences is

\[
                         I_s
 =n\Omega_0\binom{R-1}{s-1}.
\tag{5.5}

The average number of candidate loop positions per rank-`s` target is

\[
                         \overline\mu_s
 ={n\Omega_0\binom{R-1}{s-1}\over\binom ns}.
\tag{5.6}

At the hardest displayed rank `s=d`, with `d=Theta(sqrt(m))`, Stirling's
formula gives

\[
 \log\overline\mu_d
 =2d\log(m/d)+O(d),
\tag{5.7}

so the average multiplicity tends to infinity superpolynomially.  There
is no scalar shortage whatsoever.

## 6. Exact survivor classification and the corrected remaining theorem

Only cyclic coordinate symmetry acts on the hook sector.  It makes ticket
multiplicity constant on rotation orbits of targets, not on all targets.
Therefore the large average (5.6) does not imply that every target has a
ticket, much less Hall (3.4).

For a zero-terminal hook phase `D`, let `x(D)` be its omitted coordinate
and define its survivor envelope

\[
 E_d(D)=\bigcap_{j=1}^{d+1}g^jD.
\tag{6.1}

In rooted-update notation this is exactly

\[
 E_d(D)
 =\bigl(D\cup\{r(D)\}\bigr)
   \setminus
   \{p_+(D),p_+(gD),\ldots,p_+(g^dD)\},
\tag{6.2}

with the common cyclic-coordinate convention; the deletion labels are
distinct by depth residence.  The distinguished coordinate `x(D)=r(D)`
has the exact run, and hence

\[
                         F(D)=\{x(D)\}.
\tag{6.3}

The survivor set (6.2) is now evaluated exactly in
`MATH_THEOREM_PBBS_HOOK_SURVIVOR_ENVELOPE_AND_COMPLETE_PAIR_ATLAS_20260806.md`.
After rooting at zero it is

\[
 \{0\}\cup J,
 \qquad
 J\subseteq\{3,4,\ldots,n-3\},
 \qquad
 J\text{ nonconsecutive},
 \qquad |J|=m-d-1.
\tag{6.4}
\]

Therefore the naive loop-only Hall lemma above would be false: adjacent
and distance-two pairs have zero loop degree.  The same theorem repairs
those structural zeros with, respectively, two consecutive loop cells and
one terminal-occupancy-one cell, and proves a simultaneous native atlas
for **every rank-two target**.

The corrected remaining statement concerns ranks `3,...,d`: form the
bipartite graph whose right vertices are short hook source intervals and
whose edge condition says that the union of their mandatory cores lies in
`S` while the union of their maximal envelopes contains `S`.  A
component-level Hall theorem for that graph would install the remaining
targets without changing any owner or q1 edge.  Aggregate hook-sector
counts still cannot decide this interval-Hall question.

## 7. Consequence for the programme

The native singleton and pair theorems close ranks one and two.  The
present reduction shows:

1. higher low ranks require a large bank of physical components, not one
   distinguished component;
2. the complete height-`d+1` hook sector has far more than enough scalar
   loop supply;
3. one-cell thinning eliminates every owner/q1/upper interaction after a
   ticket is chosen; and
4. the exact PBBS-specific gap is the short-interval hook Hall theorem for
   ranks `3,...,d`.

Thus the next proof should study unions of the explicit cores
`{r,r-2z}` along short hook intervals, preferably by an explicit
target-to-composition injection.  No general common-cap theorem is needed
for these low tickets.
