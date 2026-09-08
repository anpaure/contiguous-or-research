# Phase-dependent C8 halos: exact common-Q rows and the minimum circuit gate

Date: 2026-08-01  
Lane: Thread D, codimension-two folded-C8 rail physicalization  
Status: exact mixed common/private maximal-word theorem; exact occurrence
export criterion; a unique minimum six-edge palette circuit in the natural
six-label alphabet; and a sharp source/residence no-go for that bounded
circuit.  A nonlocal equal-length resident rethread remains open.

## 0. Verdict

The common codimension-two rail has a genuine algebraic two-colour boundary
current.  It can be canceled at owner/palette level by the phase-dependent
halos

\[
\begin{array}{c|c|c}
 &0&1\\ \hline
L&ah-ax-bx-hx&bh-bx-ax-hx,\\
R&yt-ay-by-bt&yt-by-ay-at,
\end{array}                                             \tag{0.1}
\]

where `a=a_1`, `b=a_3`, `h=f_(d+1)`, `x=f_2`,
`y=f_(d-1)`, `t=f_0`, and a two-letter symbol is the omitted pair of a
rank-`r` owner in an `(r+2)`-set `D`.  The lower counters agree separately
on each shore.  The two upper mismatches cancel jointly.

This circuit is not physical.  Its left coordinate `h` and right coordinate
`t` have internal positive owner runs of length two.  Equivalently, the
maximal depth-`d` erosions are nonempty but fail to reconstruct exactly four
owners: zero-based rows `1,2` lose `h`, and zero-based rows `d+4,d+5` lose
`t`.  Since maximal
erosion is the largest possible inverse, no choice of smaller source letters
or common caps can repair it.

More generally, under the literal separated left/right profiles, a
phase-neutral resident halo has at least `d+2` edges on each shore, hence at
least `2d+4` total.  Replacing the two direct edges therefore costs at least
`2d+2` owner/source positions unless an equal-length segment of that size is
prospectively allocated or contracted elsewhere.  Equal phase lengths are
not zero replacement charge.

The aligned-birail telescope does not change this verdict.  It needs the
same literal base and profiles at every step.  The prospective `q(q-1)`
atlas varies base roles and is not an active chain in a frozen chronology.
Even a valid signed telescope says nothing about occurrence addresses; the
exact export row is the Hall condition in Section 3.

## 1. Exact mixed common/private maximal-word theorem

The two phase halos may differ while the central rail source is required to
be literal-common.  The following formulation cleanly separates those
quantifiers.

Let `epsilon in {0,1}`.  Let `C` be live source addresses whose letters must
be common in both phases, and let `H` be equal indexed halo addresses whose
letters may be phase-dependent.  Every address `p` has one phase-common cap
`P_p`.  For every required row `R` and phase `epsilon`, prescribe:

* a target set `S_R^epsilon`;
* a frozen exterior contribution `F_R^epsilon` contained in
  `S_R^epsilon`; and
* live incidence sets `J_(R,epsilon)^C subseteq C` and
  `J_(R,epsilon)^H subseteq H`.

Owner rows, crossing upper rows, lower pins, and protected compiler rows may
all be included in this one family.  Define the maximal common and private
letters

\[
\begin{aligned}
 K_p^C&=P_p\cap
   \bigcap_{\epsilon,R:\ p\in J_{R,\epsilon}^C}S_R^\epsilon,
                                      &&p\in C,\\
 K_p^\epsilon&=P_p\cap
   \bigcap_{R:\ p\in J_{R,\epsilon}^H}S_R^\epsilon,
                                      &&p\in H.         \tag{1.1}
\end{aligned}
\]

An address unused by every declared row may be omitted; equivalently, its
empty target intersection is interpreted as the ambient coordinate universe,
so its maximal letter is just `P_p`.

### Theorem 1.1 (mixed two-phase maximal-word criterion)

There are nonempty source letters

\[
 Q_p^0=Q_p^1\subseteq P_p\quad(p\in C),\qquad
 Q_p^\epsilon\subseteq P_p\quad(p\in H)                \tag{1.2}
\]

which realize every row iff all sets in (1.1) are nonempty and

\[
 S_R^\epsilon=F_R^\epsilon
   \cup\bigcup_{p\in J_{R,\epsilon}^C}K_p^C
   \cup\bigcup_{p\in J_{R,\epsilon}^H}K_p^\epsilon    \tag{1.3}
\]

for every `R,epsilon`.  When feasible, the `K` rows themselves are the
componentwise maximal solution.

#### Proof

Every feasible live letter is contained in its cap and in every incident
target, so it is contained in the appropriate `K`.  Taking unions proves
necessity of (1.3).  Conversely (1.3) says directly that the nonempty `K`
letters realize all rows.  Enlarging to `K` is safe because each `K` is
contained in every incident target. \(\square\)

For owner rows alone, (1.1) is screened maximal erosion.  The theorem is
strictly stronger than checking the two endpoint differences: baseline
interior reconstruction remains load-bearing.  If only a common cap, not a
literal common source, is required on the rail, move those positions from
`C` to `H`; the two phase reconstructions then decouple except for cap
containment.

The row family, interval witnesses, incidence addresses, `C/H` partition,
and caps are fixed inputs to Theorem 1.1.  The theorem does not choose an
existential upper/compiler witness, enforce injectivity between rows, or
forbid an unwanted extra row.  Those nonmonotone choices must be resolved
before applying (1.1), or retained in the separate occurrence problem of
Section 3.

For the literal six-edge circuit (0.1), including the complete common rail,
the two phase maximal erosions have length `2d+7` and agree at exactly
`2d+1` addresses.  Their six phase-private addresses are

\[
                  0,1,d+2,d+4,2d+5,2d+6.              \tag{1.4}
\]

Their directed differences are

\[
\begin{array}{c|c|c}
p&E_p^0\setminus E_p^1&E_p^1\setminus E_p^0\\ \hline
0,1&\{b\}&\{a\}\\
d+2&\{a\}&\{b\}\\
d+4&\{b\}&\{a\}\\
2d+5,2d+6&\{a\}&\{b\}.
\end{array}                                             \tag{1.5}
\]

Thus every private address differs only by exchanging `a,b`, and (1.4) is
the exact candidate common/private source partition:
the phase disagreement is localized rather than diffuse.  This does not
prove that prescribed caps `P_p` admit those letters; their containment,
rank/state, and nonemptiness rows remain.  Even with free caps, (1.3) fails
at the four owner rows listed in Section 5 because the short `h,t` runs do
not reconstruct.

Indeed a maximal erosion letter is `D` minus the union of the omitted pairs
in its incident owner window.  Taking those consecutive unions in (0.1)
gives exactly the six indices (1.4); every other incident union is
`a<->b`-invariant.

## 2. Scalar equal length versus addressed replacement

Suppose a declared replacement segment has `W` consecutive owner rows.  The
span of source addresses incident to those rows has `W+d` positions; its two
`d`-position halos overlap the exterior and are not separately appendable
blocks.  **Scalar equal length** means only that the old and new complete
source words have the same number of letters.  A **proof-safe addressed
equal-length replacement** additionally uses the same addressed incident
span, or supplies an address bijection, and verifies every crossing-row
equality.  Merely giving phase zero and phase one the same new length proves
phase balance, not transparency or zero charge relative to the old word.

The direct C8 scaffold has one edge on each boundary.  Circuit (0.1) has
three on each, adding four owner rows and therefore four source positions.
It is zero-charge only if two three-edge halo slots were allocated in the old
chronology prospectively.  A later four-cell contraction is another possible
payment, but it needs its own protected-occurrence Hall certificate.

For a resident separated halo, Section 5 strengthens the charge to at least
`2d+2`.  Thus no bounded halo repeated along a serial construction can be
called regenerative without a full reset/contraction theorem.

## 3. Occurrence-address export is exactly Hall

Let `U` be the multiset of protected old target occurrences which lose their
old cells under an equal-length replacement.  An element of `U` remembers
its target value, rank/type, phase, old interval address, and any trace guard.
Let `V` be the available new physical interval-address cells under one fixed
maximal word and cap state.  Join `u in U` to `v in V` exactly when:

1. `v` has the same literal target value and required type as `u`;
2. its source interval is legal under the relevant phase word and cap;
3. every crossing-context and trace guard attached to `u` is respected; and
4. `v` is not a frozen or already allocated occurrence.

### Theorem 3.1 (addressed export criterion)

For one fixed phase, the replacement exports all protected occurrences
injectively iff

\[
                         |N(X)|\ge |X|\qquad(X\subseteq U). \tag{3.1}
\]

For one common physical allocation in two phases, do **not** retain two
phase-labelled copies of the same logical requirement as separate left
nodes.  Fix the phase pairing and form:

* one left node `hat u=(u^0,u^1)` for each paired logical requirement; and
* one right node `hat v=(v^0,v^1)` for each aligned physical address pair.

Join `hat u` to `hat v` iff both phase incidences are legal.  Then (3.1),
with `hat U,hat V`, is again necessary and sufficient.  This avoids the
false double count in which one logical target in two phases is matched
twice to its one common address.

If either the logical requirement pairing or the phase address pairing is
variable, selecting compatible disjoint pairs is an additional
matching/hypergraph layer; the single bipartite Hall row is then not
sufficient.

This is ordinary bipartite matching, hence (3.1) is necessary and
sufficient.  A signed value-counter identity records only degrees after
forgetting `V`; it cannot imply (3.1).  In particular, equal lower/upper
counters in (0.1) are not an occurrence-address export.

## 4. Literal boundary current and aligned telescope

For the two direct edges, phase zero minus phase one is

\[
\begin{aligned}
 \delta={}&[D\setminus\{a,h,x\}]
           +[D\setminus\{b,t,y\}]\\
          &-[D\setminus\{b,h,x\}]
           -[D\setminus\{a,t,y\}].                    \tag{4.1}
\end{aligned}
\]

Put

\[
 P=D\setminus\{a,b,h,x\},\qquad
 S=D\setminus\{a,b,t,y\}.                             \tag{4.2}
\]

Then

\[
 \delta=[P\cup\{b\}]+[S\cup\{a\}]
       -[P\cup\{a\}]-[S\cup\{b\}],                 \tag{4.3}
\]

which is exactly one aligned-birail boundary current.  A reverse packet
cancels it only when its literal `P,S` and every fixed base label equal those
in (4.2).  Equal ranks, isomorphic flags, or separately relabelled fillers do
not cancel literal targets.

The canonical `q(q-1)` atlas varies the roles which occur in the fixed base;
its members are different prospective old words.  It is therefore not a
chain of reverse `a<->b` currents at one frozen `(P,S)` pair.  A usable
serial circuit must first prospectively plant an actual active chain with
literal profile alignment, then still pass Theorems 1.1 and 3.1.

## 5. Minimum algebraic circuit and the residence/source no-go

In omitted-pair notation the unique minimum owner-disjoint solution in the
natural six-label alphabet is (0.1).  Its lower triples are

\[
\begin{array}{c|c}
L&ahx,abx,bhx,\\
R&aty,aby,bty,
\end{array}                                             \tag{5.1}
\]

which are reversed by `a<->b`.  The phase-zero upper shared-label list is

\[
                         a,x,x,y,y,b,                   \tag{5.2}
\]

and phase one has `b,x,x,y,y,a`, the same multiset.

The exact 15-vertex pair-graph census gives:

* without cross-halo owner disjointness, the minimum has four total edges
  and repeats omitted pair `ht` in both halos;
* after owner disjointness, the minimum is six, and (0.1) is the unique
  minimum;
* replacing the direct pair of seams therefore adds four rows.

This algebraic minimum fails source reconstruction.  In the complete owner
sequence (left halo, common rail, right halo), `h` has owner-presence trace
`0,1,1,0` across the left halo and `t` has the same trace on the right.  At
depth `d>=4`, no depth-`d` source letter can generate an internal positive
owner run of length two.  Maximal erosion is nonempty but loses `h` from
zero-based owner rows `1,2` and `t` from zero-based rows `d+4,d+5`.  Hence
Theorem 1.1 fails even
with free caps.

There is a dimension-uniform lower bound.  Consider a phase-zero left path

\[
                  ah=E_0,E_1,\ldots,E_\ell=hx          \tag{5.3}
\]

whose phase-one path is its `a<->b` image, and suppose the literal left
lower profile is phase-neutral.  If every `E_i` contains `h`, write
`E_i={h,u_i}`.  The lower triples are then `h` plus the edge multiset of the
label walk `u_0=a,...,u_ell=x`.  Phase neutrality makes that edge multiset
`a<->b` invariant, but its odd-degree endpoints are `{a,x}`, not an invariant
set.  Contradiction.  Some internal `E_i` omits `h`, creating an internal
positive `h`-run.  Residence forces at least `d+1` consecutive such owners,
so

\[
                              \ell\ge d+2.              \tag{5.4}
\]

The right `t` argument is identical.  In the separated class the left path
uses only `{a,b,h,x}` and the right only `{a,b,t,y}`, with `h,x,t,y`
distinct.  Every lower omitted triple therefore belongs to disjoint
three-subset alphabets (their intersection has only `{a,b}`), so the two
target counters cannot cancel crosswise.  Both inequalities apply, and every
separated resident circuit has at least `2d+4` edges.

This is the sharp current conclusion: a bounded palette circuit exists, but
no bounded circuit in this direct class is simultaneously resident and
maximal-erodable.  A positive construction must be a nonlocal equal-length
rethread with preallocated growing halos, or use a different owner/facet
compiler in which the two short runs are not flat source runs.

## 6. Audit

Run

```text
python3 scratch/audit_threadD_c8_phase_halo_circuit_20260801.py --write
```

The solver-free replay enumerates all simple paths of at most five edges per
shore in the 15-vertex missing-pair graph.  This contains every possible
solution of total size below six.  It proves the raw four-edge repeated-owner
minimum and the unique owner-disjoint six-edge minimum, checks every lower
and upper counter, and replays the complete central chronology for
`4<=d<=64`.  At every depth and in both phases maximal erosion is nonempty
but has exactly the four mismatches stated above.

The general residence lower bound is the parity proof in Section 5, not an
extrapolation from the finite census.  Its literal-profile hypothesis is
load-bearing.  The prospective quadratic atlas is not asserted to satisfy
that hypothesis.
