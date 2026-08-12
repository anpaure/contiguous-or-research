# Candidate29 parity-legal support-ten two-circuit shells

Date: 2026-08-01  
Status: **exact algebra and exact lightweight raw-bank census; no Cartesian terminal pass/no-go claim**

## 1. Scope and the two tied shells

Let $d,h:O\to E$ be the two selected literal incidence matchings of the
candidate29 factor, let $\bar D,\bar H:O\to F$ be their endpoint matchings,
and put

\[
                         \pi=\bar H^{-1}\bar D.             \tag{1.1}
\]

The frozen factor has one quotient cycle on $|O|=1430$, voltage $3$ modulo
$17$, upper hole $u=0x0355f$, and lower hole $\ell=0x0062f$.  This note
concerns only two simultaneous simple assignment circuits with total owner
support ten.

There are two tied parity-legal families, each in both H/D orientations:

\[
 (p_H,p_D)\in\{(4,6),(6,4),(3,7),(7,3)\}.                 \tag{1.2}
\]

Assignment support $p$ is the bipartite circuit `C(2p)`.  Thus (1.2)
comprises `C8 x C12` and `C6 x C14`.  The balanced `C10 x C10` shell is
already closed, but neither family in (1.2) is called the uniquely next
shell here.

Residence, deeper shadows, opening, and the compiler are outside scope.

## 2. Complete raw terminal-map domain

For one side $M\in\{D,H\}$, the raw assignment graph contains every
nonselected nonloop literal incidence from an owner $x$ to a facet occupied
by $M(y)$.  It retains parallel labels and incidences equal to the opposite
base matching.  A simple directed $p$-cycle changes exactly its $p$ owner
rows and is a perfect matching on that side.

Two histories are identified only when their complete literal terminal
matching vectors agree.  Equivalently, since all other rows are fixed, their
sorted `(owner,new-incidence)` patches agree.

### Theorem 2.1 (raw Cartesian completeness)

For each pair $(p_H,p_D)$ in (1.2), every simultaneous literal terminal state
of that type occurs exactly once in

\[
                     {\cal B}_{H,p_H}\times{\cal B}_{D,p_D},              \tag{2.1}
\]

where ${\cal B}_{M,p}$ is the deduplicated bank of all raw simple directed
$p$-cycles.  No raw atom may first be discarded merely because it collides
with the unchanged opposite matching.

#### Proof

A terminal side state is exactly a raw simple assignment cycle together with
its literal choices.  Deduplication by the complete terminal vector removes
histories and nothing else.  Before mutual D/H disjointness, the two sides
are chosen independently, giving (2.1).  An isolated opposite-base
incidence can be rescued when the other circuit changes the same owner, so
isolated base validity is not a sound bank restriction. $\square$

### Exact candidate29 bank census

The lightweight source audit gives:

| bank | terminal maps | isolated-base-valid |
|---|---:|---:|
| $H3$ | 621 | 387 |
| $D3$ | 626 | 394 |
| $H4$ | 1,386 | 802 |
| $D4$ | 1,377 | 797 |
| $H6$ | 46,287 | 20,504 |
| $D6$ | 46,171 | 20,425 |
| $H7$ | 303,975 | 118,864 |
| $D7$ | 304,444 | 119,120 |

There are zero duplicate terminal maps in every row.  Hence the four raw
Cartesian sizes are

| orientation | raw pairs |
|---|---:|
| `H4 x D6` | 63,993,006 |
| `H6 x D4` | 63,737,199 |
| `H3 x D7` | 189,059,724 |
| `H7 x D3` | 190,288,350 |

Thus `C8 x C12` has 127,730,205 raw pairs, `C6 x C14` has 379,348,074,
and the tied support-ten union has 507,078,279.  These are domain counts,
not a terminal search.

## 3. Exact pair rescue and an atom-level capacity cut

Let $A=\operatorname{supp}(\alpha)$ be the D support and
$B=\operatorname{supp}(\beta)$ the H support.  Write $d',h'$ for the
literal terminal incidences and define

\[
 C_D=\{x\in A:d'_x=h_x\},\qquad
 C_H=\{x\in B:h'_x=d_x\}.                                 \tag{3.1}
\]

Put $s=\min(p_D,p_H)$, so $s=4$ for `C8 x C12` and $s=3$ for
`C6 x C14`.

### Theorem 3.1 (pair rescue)

The simultaneous terminal matchings are incidence-disjoint if and only if

\[
 C_D\cup C_H\subseteq A\cap B                              \tag{3.2}
\]

and

\[
                         d'_x\ne h'_x\quad(x\in A\cap B). \tag{3.3}
\]

Consequently

\[
                    |C_D\cup C_H|\le |A\cap B|\le s.       \tag{3.4}
\]

#### Proof

Outside $A\cap B$, at most one incidence changes, so equality with the
unchanged opposite incidence is fatal.  On $A\cap B$, both change and (3.3)
is the exact final condition.  These owner classes partition $O$. $\square$

The raw census records $|C_M|$ as the opposite-base-obligation count.  Thus
any long-side atom with more than $s$ obligations is impossible against
every short atom.  This atom-level cut removes exactly:

| orientation | raw pairs removed | pairs surviving only this cut |
|---|---:|---:|
| `H4 x D6` | 11,088 | 63,981,918 |
| `H6 x D4` | 11,016 | 63,726,183 |
| `H3 x D7` | 1,175,553 | 187,884,171 |
| `H7 x D3` | 1,191,904 | 189,096,446 |

This remains only a necessary prefilter.  If $|C_D\cup C_H|=s$, then the
short support itself must equal $A\cap B=C_D\cup C_H$; this is a stronger
exact support pin before (3.3).

## 4. The two overlaps and exact terminal currents

Define the owner and facet overlaps

\[
 O_\times=A\cap B,\qquad
 F_\times=\bar D(A)\cap\bar H(B).                          \tag{4.1}
\]

Under $\bar H^{-1}$, the second identity becomes

\[
                  |F_\times|=|\pi(A)\cap B|.               \tag{4.2}
\]

Thus the lower and upper nonlinearities are the time-zero and one-step
correlations of the two support sets.  Put

\[
 r_-=|O_\times|,\qquad r_+=|F_\times|,\qquad
 n_-=10-r_-,\qquad n_+=10-r_+.                            \tag{4.3}
\]

For shore $\varepsilon\in\{-,+\}$ and target $T$, let
$d_T^\varepsilon$ count changed old rows carrying $T$, let
$g_T^\varepsilon$ count terminal new rows carrying $T$, and define

\[
                  a_T^\varepsilon=d_T^\varepsilon-g_T^\varepsilon.
                                                                    \tag{4.4}
\]

Then $\sum_Ta_T^\varepsilon=0$.

### Theorem 4.1 (exact current criterion)

A terminal shore is complete if and only if

\[
 a_{h_\varepsilon}^\varepsilon\le-1,
 \qquad
 a_T^\varepsilon\le\mu_\varepsilon(T)-1
 \quad(T\ne h_\varepsilon),                              \tag{4.5}
\]

where $h_+=u$ and $h_-=\ell$.

#### Proof

The terminal load is $\mu'_\varepsilon(T)=
\mu_\varepsilon(T)-a_T^\varepsilon$.  Requiring every load to be positive
gives exactly (4.5). $\square$

## 5. Projected cross-square obstruction

Evaluate the D and H atoms separately against the base matching in the free
abelian group on **all** traces, add them, and then project to the required
rank-seven or rank-ten palette.  Call the provisional load
$\nu_\varepsilon$.

At an overlap, with base, D-only, H-only, and final mixed turns denoted by
$B,P,Q,R$, the correction is

\[
                 \kappa=\operatorname{pr}_\varepsilon
                 \bigl([R]-[P]-[Q]+[B]\bigr).              \tag{5.1}
\]

Projection is essential: an isolated opposite-base trace can be off-rank.
The positive mass of (5.1) is at most two, because its positive part is
contained in $[R]+[B]$.

Define

\[
                    \operatorname{Def}(\nu)=
                    \sum_T(1-\nu(T))_+.                    \tag{5.2}
\]

### Theorem 5.1 (overlap-rank cut)

Every terminal palette-exact pair satisfies

\[
 \operatorname{Def}(\nu_-)\le2r_-,\qquad
 \operatorname{Def}(\nu_+)\le2r_+.                        \tag{5.3}
\]

Consequently

\[
 \operatorname{Def}(\nu_-)+\operatorname{Def}(\nu_+)
 \le2(r_-+r_+)\le4s.                                      \tag{5.4}
\]

If a named hole is absent from the isolated provisional load, the relevant
overlap is nonempty and some final mixed turn $R$ must create that hole.

#### Proof

Each missing unit of provisional load needs one positive correction unit;
one cross-square supplies at most two.  A base turn cannot equal a
base-missing hole, and off-rank isolated turns disappear under projection,
so a hole absent provisionally can only be supplied by $R$. $\square$

The inequalities are necessary, not sufficient: the two negative terms can
eject other singleton targets, and positive units can hit the wrong colours.

## 6. Exact hole-provider clauses and corrected gap rows

Each named hole must be witnessed by at least one of three provider classes:

1. a D-unmixed changed row;
2. an H-unmixed changed row; or
3. an exact mixed D/H incidence pair on the appropriate overlap.

At the lower shore these classes lie in $A\setminus B$, $B\setminus A$,
and $A\cap B$.  At the upper shore they lie in
$\bar D(A)\setminus\bar H(B)$,
$\bar H(B)\setminus\bar D(A)$, and $F_\times$.  The disjunction is both
necessary and sufficient for creating the named hole, but full current
(4.5) is still required.

For two **unmixed** upper/lower provider arcs on one directed assignment
$p$-cycle, let $(g_1,g_2)$ be the numbers of intervening nonprovider arcs in
the two directions.  The audited cross head/tail exclusions force

\[
                       g_1,g_2\ge1,qquad g_1+g_2=p-2.       \tag{6.1}
\]

Hence the sound compound-shell gap rows are:

| support $p$ | permitted gap patterns from (6.1) |
|---:|---|
| 3 (`C6`) | none |
| 4 (`C8`) | $(1,1)$ |
| 6 (`C12`) | $(1,3),(2,2),(3,1)$ |
| 7 (`C14`) | $(1,4),(2,3),(3,2),(4,1)$ |

These patterns are necessary, not assertions that the corresponding literal
cycles exist.  The earlier statement that `C10` is the first one-side
Hamilton-compatible possibility also used one-side parity; provider
incidence alone permits the even support-four pattern $(1,1)$ inside an
even-even compound.  If either hole witness is mixed, no gap rejection is
sound and the exact incidence-pair table must be retained.

## 7. Repeat release

Let $s_\varepsilon$ be the number of changed old rows whose base target has
load one, let $G_\varepsilon$ be the multiset of $n_\varepsilon$ terminal
turns, and put

\[
 \chi_\varepsilon=n_\varepsilon-|\operatorname{supp}G_\varepsilon|,
 \qquad
 \rho_\varepsilon=n_\varepsilon-s_\varepsilon.            \tag{7.1}
\]

Every terminal exact shore satisfies

\[
                         \rho_\varepsilon\ge1+\chi_\varepsilon.          \tag{7.2}
\]

Indeed, all $s_\varepsilon$ deleted singleton colours and the distinct old
hole must occur in $G_\varepsilon$, so
$s_\varepsilon+1\le n_\varepsilon-\chi_\varepsilon$.

## 8. Topology parity, connectedness, and voltage

A $p$-cycle has sign $(-1)^{p-1}$.  From

\[
                         \pi'=\beta^{-1}\pi\alpha           \tag{8.1}
\]

and the fact that the base 1430-cycle is odd, a terminal Hamilton cycle can
exist only when

\[
                         p_D+p_H\equiv0\pmod2.              \tag{8.2}
\]

Both tied shells satisfy (8.2): the two even-support cycles are both odd
permutations, while the two odd-support cycles are both even permutations.
Thus parity does not obstruct connectedness.

More precisely, every terminal factor in either shell has an odd number of
quotient components.  The full successor is

\[
                              P'=\beta^{-1}\pi\alpha.        \tag{8.3}
\]

Its typed changed-tail set is

\[
                  S=A\cup\alpha^{-1}\pi^{-1}(B),
                  \qquad |S|\le10.                          \tag{8.4}
\]

Cut the base arcs at $S$, reconnect each tail $x$ to its literal terminal
head $P'(x)$, and contract every maximal unchanged base-$\pi$ path.  If
$\operatorname{next}_S(z)$ is the first port met by iterating $\pi$ from
$z$, the contracted successor is

\[
                  \Psi(x)=\operatorname{next}_S(P'(x)).     \tag{8.5}
\]

Connectedness is exactly the statement that $\Psi$ is one cycle.  The
naive set $A\cup B$ is not generally typed and must not be used.  The
physical lift is one cycle exactly when direct literal traversal has nonzero
voltage modulo $17$.  Parallel incidence labels prevent voltage from being
deduced from endpoint permutations or currents.

## 9. Exact terminal theorem and surviving finite gate

### Theorem 9.1

A raw pair in either support-ten family is an immediate physical repair if
and only if:

1. its two side terminal maps are perfect and satisfy (3.2)--(3.3);
2. both exact current systems (4.5) hold;
3. $\beta^{-1}\pi\alpha$ is one quotient cycle; and
4. its literal voltage is nonzero modulo $17$.

The atom-capacity cut, (5.3)--(5.4), the provider disjunction/gap rows, and
(7.2) are sound necessary prefilters.  None replaces the exact conditions.

The frozen census proves only raw-domain completeness and sizes.  It does not
evaluate the 507,078,279 Cartesian states and therefore proves neither a
repair nor a no-go for `C8 x C12` or `C6 x C14`.  Triple circuits, `C30`, and
all deeper-shadow conditions are explicitly excluded.

## 10. Reproducible lightweight audit

```text
scratch/threadD_k17_candidate29_compound_repair_20260801/
  census_candidate29_support10_two_circuit_shells_light.cpp
  support10_two_circuit_raw_census.audit.json
```

The local source audit enumerated only the eight raw banks, not a Cartesian
terminal product.  It completed in 2.31 seconds.  Resource exhaustion would
be `UNKNOWN`; the recorded run exited normally.
