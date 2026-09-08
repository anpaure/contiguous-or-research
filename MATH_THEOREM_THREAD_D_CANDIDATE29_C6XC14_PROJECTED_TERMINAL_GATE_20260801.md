# Candidate29 `C6 x C14`: projected terminal gate and a scope-safe depth-three SCD diagnostic interface

Date: 2026-08-01  
Status: **proved prefilters and exact schemas; no Cartesian run or finite shell conclusion**

## 1. Frozen shell and raw banks

Let $d,h:O\to E$ be the selected literal D/H incidence matchings, let
$\bar D,\bar H:O\to F$ be their endpoint matchings, and put

\[
                         \pi=\bar H^{-1}\bar D.             \tag{1.1}
\]

The candidate29 input has $|O|=|F|=1430$, one quotient cycle, voltage $3$
modulo $17$, upper rank-ten hole $u=0x0355f$, and lower rank-seven hole
$\ell=0x0062f$.

This note treats only

\[
                 (p_H,p_D)=(3,7)\quad\hbox{or}\quad(7,3),  \tag{1.2}
\]

namely `H-C6 x D-C14` and `H-C14 x D-C6`.  The exact raw terminal-map
banks are

| bank | maps | isolated-base-valid | obligation histogram |
|---|---:|---:|---|
| $H3$ | 621 | 387 | $0^{387}1^{229}2^5$ |
| $D3$ | 626 | 394 | $0^{394}1^{227}2^5$ |
| $H7$ | 303,975 | 118,864 | $0^{118864}1^{119776}2^{51355}3^{12076}4^{1766}5^{132}6^6$ |
| $D7$ | 304,444 | 119,120 | $0^{119120}1^{119844}2^{51523}3^{12064}4^{1757}5^{129}6^7$ |

The raw Cartesian products contain 189,059,724 and 190,288,350 pairs.
Opposite-base atoms remain in the raw banks because simultaneous movement
can rescue them.

The goal here is to state every exact or proved necessary filter available
from the terminal algebra before evaluating those products.  No result below
is a finite no-go.

## 2. Bank records and exact pair rescue

Let $A=\operatorname{supp}(\alpha)$ be the D support and
$B=\operatorname{supp}(\beta)$ the H support.  Thus $(|A|,|B|)$ is $(7,3)$
or $(3,7)$.  For terminal literal incidences $d',h'$, define

\[
 C_D=\{x\in A:d'_x=h_x\},\qquad
 C_H=\{x\in B:h'_x=d_x\}.                                 \tag{2.1}
\]

### Theorem 2.1 (pair-rescue iff)

The two terminal matchings are mutually incidence-disjoint if and only if

\[
 C_D\cup C_H\subseteq A\cap B                              \tag{2.2}
\]

and

\[
                         d'_x\ne h'_x\quad(x\in A\cap B). \tag{2.3}
\]

#### Proof

Outside $A\cap B$, exactly one selected incidence can change, so an equality
with the unchanged opposite incidence is fatal.  On the overlap, both
incidences change and (2.3) is precisely terminal validity. $\square$

### Corollary 2.2 (obligation pins)

Every valid pair satisfies

\[
                |C_D\cup C_H|\le |A\cap B|\le3.            \tag{2.4}
\]

Consequently:

1. a C14 atom with at least four opposite-base obligations is impossible
   against every C6 atom;
2. the C6 support must contain every conflict owner of the C14 atom;
3. the C14 support must contain every conflict owner of the C6 atom; and
4. if $|C_D\cup C_H|=3$, the C6 support is forced and equals
   $A\cap B=C_D\cup C_H$.

The first row removes exactly 1,175,553 raw pairs in `H3 x D7` and
1,191,904 in `H7 x D3`, leaving 187,884,171 and 189,096,446 before the
other rows.  These are atom-capacity counts, not terminal-valid counts.

For implementation, every atom may safely cache

```text
support bitset; terminal endpoint permutation; terminal literal edge per
support owner; opposite-base conflict bitset/count; literal voltage delta.
```

Pairs can be indexed by C14 conflict bitset and enumerated only against C6
support bitsets containing it.  The union containment (2.2) and all final
equalities (2.3) must still be checked.

## 3. Owner/facet overlaps and support-time correlations

The nonlinear lower and upper overlaps are different:

\[
 O_\times=A\cap B,
 \qquad
 F_\times=\bar D(A)\cap\bar H(B).                          \tag{3.1}
\]

Under $\bar H^{-1}$,

\[
             r_-:=|O_\times|=|A\cap B|,
 \qquad
             r_+:=|F_\times|=|\pi(A)\cap B|.               \tag{3.2}
\]

Thus $0\le r_-,r_+\le3$, and the changed-row counts are

\[
                         n_-=10-r_-,\qquad n_+=10-r_+.      \tag{3.3}
\]

The two popcounts in (3.2) are exact constant-time filters from atom support
bitsets and the cached base successor.  Owner overlap controls pair rescue
and lower squares; the one-step overlap controls upper squares.  Replacing
$r_+$ by $r_-$ is unsound.

## 4. Projected isolated current and overlap squares

For each atom, form its isolated formal delta against the unchanged opposite
matching in the free abelian group on **all set traces**.  Only after adding
the formal columns apply

\[
 \operatorname{pr}_-([T])=
 \begin{cases}[\operatorname{can}(T)]&|T|=7,\\0&|T|\ne7,
 \end{cases}
 \qquad
 \operatorname{pr}_+([T])=
 \begin{cases}[\operatorname{can}(T)]&|T|=10,\\0&|T|\ne10.
 \end{cases}                                                \tag{4.1}
\]

This drops off-rank isolated opposite-base traces rather than diagnosing
them as errors.  Let

\[
 \nu_\varepsilon=\mu_\varepsilon+
 \operatorname{pr}_\varepsilon
 (\Delta_D^{\rm iso}+\Delta_H^{\rm iso})                  \tag{4.2}
\]

be the provisional required-palette load.

At a lower owner overlap, denote the base, D-only, H-only, and true final
turns by $B_x,P_x,Q_x,R_x$.  The exact correction is

\[
 \kappa_x^-=operatorname{pr}_-
 ([R_x]-[P_x]-[Q_x]+[B_x]).                                \tag{4.3}
\]

At an upper facet overlap the same identity gives $\kappa_f^+$.  Therefore

\[
 \mu'_- =\nu_-+\sum_{x\in O_\times}\kappa_x^-,
 \qquad
 \mu'_+ =\nu_++\sum_{f\in F_\times}\kappa_f^+.           \tag{4.4}
\]

Equations (4.3)--(4.4), with projection after the formal square, are the
only proof-safe way to combine isolated atom columns at overlaps.

Define

\[
                     \operatorname{Def}(\nu)=
                     \sum_T(1-\nu(T))_+.                   \tag{4.5}
\]

### Theorem 4.1 (scalar and targetwise overlap cuts)

Every palette-exact pair satisfies

\[
 \operatorname{Def}(\nu_-)\le2r_-,\qquad
 \operatorname{Def}(\nu_+)\le2r_+,                        \tag{4.6}
\]

and hence

\[
             \operatorname{Def}(\nu_-)+\operatorname{Def}(\nu_+)
             \le2(r_-+r_+)\le12.                          \tag{4.7}
\]

More strongly, for every target $T$,

\[
 (1-\nu_\varepsilon(T))_+
 \le
 \sum_{z\in Z_\varepsilon}(\kappa_z^\varepsilon(T))_+,
                                                                    \tag{4.8}
\]

where $Z_-=O_\times$ and $Z_+=F_\times$.

#### Proof

The positive part of one projected square is contained in its two positive
terms $[B]+[R]$, so it has mass at most two.  This gives (4.6)--(4.7).
If the final load of $T$ is at least one, the required increment over
$\nu(T)$ cannot exceed the sum of the positive parts of its square
coefficients, proving (4.8). $\square$

If the named hole is absent from $\nu_\varepsilon$, then the corresponding
overlap is nonempty and a final mixed turn $R$ must equal that hole: the base
turn is not a base-missing colour and off-rank isolated turns vanish under
(4.1).

An exact implementation may cache every sparse isolated column and every
literal square signature keyed by the two terminal incidences.  The scalar
and targetwise tests precede summing the signed squares; the exact sum in
(4.4) is then the final current test.

## 5. Exact current, exposure, and repeat-release rows

For shore $\varepsilon$, let $d_T^\varepsilon$ count changed old rows of
colour $T$ and $g_T^\varepsilon$ count terminal new rows.  Put

\[
                         a_T^\varepsilon=d_T^\varepsilon-g_T^\varepsilon.
                                                                    \tag{5.1}
\]

The terminal shore is complete if and only if

\[
 a_{h_\varepsilon}^\varepsilon\le-1,
 \qquad
 a_T^\varepsilon\le\mu_\varepsilon(T)-1
 \quad(T\ne h_\varepsilon),                               \tag{5.2}
\]

where $h_+=u$ and $h_-=\ell$.

There is an equivalent bitset form useful before a full replay.  Cache, for
each base target $T$, the bitset $\operatorname{Occ}_\varepsilon(T)$ of its
old row occurrences.  For the changed-row bitset $R_\varepsilon$, define

\[
 {\cal E}_\varepsilon=
 \{T:\mu_\varepsilon(T)>0\ \hbox{ and }\ 
       \operatorname{Occ}_\varepsilon(T)\subseteq R_\varepsilon\}.      \tag{5.3}
\]

These are exactly the old colours fully exposed by the packet.  If
$G_\varepsilon$ is the multiset of exact terminal new turns, then

\[
 \boxed{
 \text{terminal shore complete}
 \iff
 {\cal E}_\varepsilon\cup\{h_\varepsilon\}
 \subseteq\operatorname{supp}G_\varepsilon.}              \tag{5.4}
\]

Indeed, every colour outside ${\cal E}_\varepsilon$ retains an unchanged
old occurrence, while every colour in it and the old hole requires a new
one.  Thus (5.4) is exact, not merely a heuristic.

Let

\[
 \chi_\varepsilon=n_\varepsilon-
 |\operatorname{supp}G_\varepsilon|.                       \tag{5.5}
\]

Taking sizes in (5.4) gives the strong release row

\[
                 |{\cal E}_\varepsilon|+1
                 \le n_\varepsilon-\chi_\varepsilon.       \tag{5.6}
\]

If $s_\varepsilon$ is only the number of changed old singleton rows and
$\rho_\varepsilon=n_\varepsilon-s_\varepsilon$, then

\[
                         \rho_\varepsilon\ge1+\chi_\varepsilon           \tag{5.7}
\]

is the cheaper repeat-release consequence requested in this lane.  It is
weaker than the fully exposed-target test (5.4)--(5.6).

## 6. Exact provider classes and gap filters

For each shore, a terminal witness of its named hole lies in exactly one row
class:

1. D-unmixed, on the D-only changed rows;
2. H-unmixed, on the H-only changed rows; or
3. mixed, on the relevant owner/facet overlap.

The disjunction over these three row classes is necessary and sufficient to
create the named hole.  Multiple witnesses may coexist.  A safe cache has:

```text
one-side provider bits on each atom;
lower mixed table keyed by (owner,d_terminal_edge,h_terminal_edge);
upper mixed table keyed by (facet,d_terminal_edge,h_terminal_edge).
```

The provider tables are evaluated after the exact overlap is known.
Requiring either raw atom alone to supply a hole is unsound.

The audited cross head/tail exclusions imply that two unmixed upper/lower
provider arcs on one directed $p$-cycle have positive directed gaps
$g_1,g_2$ with $g_1+g_2=p-2$.  Therefore:

* a C6 atom cannot contain both unmixed provider types;
* a C14 atom can contain them only at gaps
  $(1,4),(2,3),(3,2),(4,1)$.

Hence in `H3 x D7`, the two holes cannot both be H-unmixed; if both are
D-unmixed on the C14 atom, its gap must be one of those four.  In
`H7 x D3`, interchange H and D.  If the holes use different circuits, or if
either witness is mixed, there is no same-cycle gap rejection.

For duplicate-free provider-first enumeration, assign each named hole its
least witness in the ordered classes `D-unmixed`, `H-unmixed`, `mixed`, and
then the least literal row inside that class.
The resulting nine witness-type pairs partition terminal repairs; they do
not remove mixed providers.

## 7. Endpoint order, exact topology, and additive voltage

Extend $\alpha,\beta$ by the identity outside their supports.  The full
terminal successor is

\[
                              P'=\beta^{-1}\pi\alpha.        \tag{7.1}
\]

Its changed tails are contained in, and after deleting vacuous coincidences
are exactly the active part of,

\[
                  S=A\cup\alpha^{-1}\pi^{-1}(B),
                  \qquad |S|\le10.                          \tag{7.2}
\]

The naive set $A\cup B$ is not typed: the H support acts after $\pi\alpha$,
not at the original tail coordinate.

For $z\in O$, let $\operatorname{next}_S(z)$ be the first vertex of $S$
encountered by iterating the base successor $\pi$, allowing zero iterations.
Cut the base arcs $x\to\pi(x)$ for $x\in S$, insert the literal terminal
heads $P'(x)$, and define the contracted map

\[
                  \Psi(x)=\operatorname{next}_S(P'(x))
                  \qquad(x\in S).                          \tag{7.3}
\]

Equivalently, contract every maximal unchanged base-$\pi$ path after
reconnecting the terminal heads.  The full quotient factor is connected if
and only if $\Psi$ is one cycle.  This is an $O(10)$ exact order test once
the base next-port table is cached.  Since both assignment cycles are even
permutations, every
terminal factor has an odd number of quotient components.  Odd component
parity is only a cheap rejection check; (7.1)--(7.3) are exact.

Indeed, if $x\notin S$, then $\alpha(x)=x$ and
$\pi\alpha(x)\notin B$, so $P'(x)=\pi(x)$.  Hence every arc outside $S$
is the unchanged base arc.  Cutting at $S$ therefore decomposes the base
cycle into disjoint unchanged paths, and reconnecting their starts by the
literal heads $P'(x)$ gives exactly (7.3).  Contracting those paths preserves
the component partition.

Voltage also has an exact bank-local decomposition.  Define

\[
 \delta_D=\sum_{e\in D_{\rm new}}\!\operatorname{shift}(e)
          -\sum_{e\in D_{\rm old}}\!\operatorname{shift}(e),
 \qquad
 \delta_H=\sum_{e\in H_{\rm new}}\!\operatorname{shift}(e)
          -\sum_{e\in H_{\rm old}}\!\operatorname{shift}(e).           \tag{7.4}
\]

For a connected terminal quotient cycle its physical voltage is

\[
                              V'=3+\delta_D-\delta_H\pmod {17}.          \tag{7.5}
\]

Thus pairs with zero value in (7.5) are safely rejected, and atoms may be
bucketed by voltage residue.  Formula (7.5) uses literal labels; endpoint
permutations alone do not determine it.  If topology is disconnected, the
total residue does not replace the componentwise voltage ledger, but such a
row already fails the one-cycle target.

No further endpoint-order cut is asserted.  Any order heuristic not implied
by the full identity (7.1) and typed contraction (7.2)--(7.3) must not be
used as a proof filter.

## 8. Proof-safe evaluation order

The following order uses only sound filters:

1. discard C14 atoms with obligation count at least four;
2. support-index by the obligation containments of Corollary 2.2;
3. test (2.2), then every final collision in (2.3);
4. compute $r_-,r_+$ from (3.2);
5. apply the exact provider disjunctions and only the scoped gap rows;
6. apply (4.6)--(4.8) with off-rank isolated traces dropped;
7. apply (5.6) or the cheaper (5.7);
8. test the typed contracted topology (7.1)--(7.3) and voltage (7.5);
9. sum the exact overlap squares (4.4) and apply (5.2), equivalently (5.4).

Steps may be reordered for speed when their inputs are available.  A pair
surviving all necessary rows is not a repair until the exact conditions in
steps 3, 8, and 9 all pass.

## 9. Strictly diagnostic cyclic-SCD depth-three interface

The relevant independent formulation is

```text
MATH_THEOREM_SCD_FLAG_RAIL_BALANCE_STATEWISE_HALL_AND_OWNER_GATE_20260801.md
MATH_THEOREM_CYCLIC_QUOTIENT_SCD_EQUIVARIANT_SELECTOR_AND_D3_RAIL_BALANCE_20260801.md
MATH_AUDIT_K17_CYCLIC_SCD_D3_FIRST_FACTOR_STATE_HALL_20260801.md
```

At $k=17,d=3$, that gate requires a **literal equivariant deletion-flag
table**

\[
                         f(q)=(q;z_1(q),z_2(q))             \tag{9.1}
\]

at every rank-eight root, exact marked rank-seven and rank-six target
coverage, and a rainbow perfect matching in one representative state graph
$G_0$.  Rail balance alone is not enough.  The audited first table has
`3836` edges, `246/124` isolated tail/head flags, ordinary matching
`1010/1430`, and only `818` distinct colours in that matching; this is a
failure of that one table only.

A candidate29 `C6 x C14` terminal row supplies only the two immediate q1
palettes, quotient topology, and literal voltage.  It does **not** supply
(9.1), a rank-six marking, or the state graph.  Therefore its default
diagnostic status is

```text
NOT_STATE_HALL_EVALUABLE_NO_LITERAL_EQUIVARIANT_FLAG_TABLE
```

and this status is not a rejection.

### Owner-cycle export interface

For a connected terminal factor, traverse its alternating quotient cycle.
Write $q_i$ for its rank-eight facet roots and $o_{i+1}$ for the rank-nine
owner joining $q_i$ to $q_{i+1}$.  Export

```text
(tail_root_orbit, head_root_orbit, rank9_owner_colour_orbit,
 literal_shift_increment)
```

for all 1430 steps, together with the cyclic order and total voltage.  The
facet roots and rank-nine owner colours are each distinct because the two
terminal incidence matchings are perfect.  This is an **input interface**
for a later flag-table construction, not a state-Hall certificate.

If an external literal equivariant flag table is supplied, a diagnostic
adapter may:

1. verify its rank-seven/rank-six marked-target equations and rail balance;
2. build $G_0$ from the exact deletion-word shift law;
3. compute its intrinsic rank-nine edge colours and compare/expose them
   against the exported owner-cycle interface;
4. compute ordinary Hall and then rainbow perfect matching; and
5. report whether the exported terminal cycle itself embeds in those legal
   flag transitions.

Failure of the exported cycle to embed does not prove that $G_0$ has no
other rainbow matching.  Failure of one supplied flag table is scoped only
to that table.  None of these diagnostics is a sound prefilter for the
immediate `C6 x C14` Cartesian shell, because depth-three target coverage and
residence are outside that shell's claim.

## 10. Exact surviving gate

The prefilter stack is complete as an algebraic specification: pair rescue,
projected overlap current, exact exposure/current, connectedness, and voltage
together are an iff test for an immediate physical repair.  The raw products
have not been enumerated under these rows.  No finite pass/no-go, no
depth-three SCD result, and no deeper-shadow or compiler result is claimed.
