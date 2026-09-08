# The first compensated-controller lift forces a closed interacting deck circuit

Date: 2026-07-28

Status: exact finite theorems for the authoritative frozen `k=15` carrier.
The demand-only one-state lift is ruled out for **every** 24-pin cover.  The
previously displayed 24-pin witness is also ruled out by two physical collar
conflicts.  A second old-pair-complementary 24-pin witness passes every
fixed collar test.  No exact controller `P'` or physical word `A'` is
constructed; the smallest surviving interacting circuit CSP is stated
exactly in Sections 4--5.

## 1. Frozen notation

Let

\[
 T_0,\ldots,T_{W-1}\in{[15]\choose8},\qquad W=6435,
\]

be `scratch/k15_doubletrans_05_213_hall29.json`, and put

\[
 P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i,
 \qquad 0\le p\le W+2.                                \tag{1.1}
\]

The controller rank profile is

\[
 8,7,6,\underbrace{5,\ldots,5}_{6432},6,7,8.          \tag{1.2}
\]

A UNIT demand `(p,x)` asks for

\[
                         x\in A'_p\subseteq P'_p.      \tag{1.3}
\]

The 24-pin theorem shows that a 29-address UNIT cover needs at least 24
serving pins.  Equality uses five double-serving pins.  Their conflict
graph is

\[
                         K_3\sqcup K_2\sqcup3K_1.      \tag{1.4}
\]

## 2. Every 24-pin lift needs a nondemanded interacting change

Call a lift **demand-only** if `P'_p=P_p` at every position not named by a
selected UNIT pin.  At a named position one may choose any new controller
state of the prescribed rank containing every demanded coordinate; this is
more general than one insertion and one deletion.

### Theorem 2.1 (all-cover demand-only no-go)

No 24-pin UNIT cover of 29 distinct target/cell addresses has an exact
demand-only controller lift whose consecutive controller states are
Johnson-adjacent and whose four-window unions all have rank eight.

#### Proof

A 24-pin cover of 29 addresses must use exactly five double services.  A
five-vertex independent set in (1.4) contains all three isolated vertices.
In particular, every such cover uses the double pin

\[
                             (6429,4).                 \tag{2.1}
\]

The exact UNIT atlas has no pin at any other position in the full affected
controller collar

\[
                         \{6426,\ldots,6432\}.         \tag{2.2}
\]

Thus a demand-only lift freezes that collar except at 6429.  Write

\[
 C=\{0,2,8,9\}.
\]

The two frozen neighbours are

\[
 P_{6428}=C\cup\{13\},
 \qquad P_{6430}=C\cup\{4\}.                          \tag{2.3}
\]

Every rank-five state `Q` which contains 4 and is Johnson-adjacent to both
sets in (2.3) has the form

\[
                 Q=(C\setminus\{c\})\cup\{4,13\},
                 \qquad c\in C.                       \tag{2.4}
\]

For each of these four possibilities, direct union with the frozen states
at positions 6426 through 6432 gives the four affected middle ranks

\[
                         (8,7,7,8).                   \tag{2.5}
\]

Hence two middle windows have the wrong rank.  No exact controller exists
in the demand-only model. \(\square\)

### Corollary 2.2 (necessary generalization)

Every exact lift of every 24-pin cover changes at least one nondemanded
controller state in the collar (2.2).  In particular, the requested
one-deletion-at-each-demanded-position model is impossible for all 24-pin
covers, not merely for one witness.

There is a complementary global no-go.  The independently audited file
`MATH_K15_UNIT_PIN_ISOLATED_CONTROLLER_CYCLE_NOGO_20260728.md` exhausts all
1,602 UNIT pins.  Exactly 1,318 admit a locally admissible isolated
rank-preserving one-state
edit, every such edit replaces one middle state `T_q` by one other state
`T_(q')`, and the resulting 1,318-arc digraph on 2,295 indices is acyclic.
Therefore no nonempty pairwise distance-at-least-eight family of isolated
UNIT edits preserves the exact deck.  Only 14 of the formerly displayed 24
pins are even isolated-admissible.  The surviving mechanism must be an
overlapping multi-state circuit.

## 3. Exact changed-window closure

Let `P'` be any exact controller and `T'` its four-window middle chronology.
Define

\[
 \mathcal C=\{p:P'_p\ne P_p\},
 \qquad
 \mathcal D=\{i:T'_i\ne T_i\}.                        \tag{3.1}
\]

### Theorem 3.1 (deck-cycle closure)

The changed sets satisfy

\[
 \mathcal D\subseteq
   \bigcup_{p\in\mathcal C}([p-3,p]\cap[0,W-1]),      \tag{3.2}
\]

\[
 \mathcal C\subseteq
   \bigcup_{i\in\mathcal D}([i,i+3]\cap[0,W+2]).      \tag{3.3}
\]

Moreover,

\[
              \{T'_i:i\in\mathcal D\}
              =\{T_i:i\in\mathcal D\}               \tag{3.4}
\]

as multisets.  Consequently there is a unique derangement
`sigma` of `mathcal D` such that

\[
                         T'_i=T_{\sigma(i)}.           \tag{3.5}
\]

#### Proof

A changed controller state can affect only the four middle unions that
contain it, giving (3.2).  Conversely, both controllers are their maximal
erosions.  If all middle windows defining `P_p` are unchanged, their
intersection is unchanged, giving (3.3).  Both `T` and `T'` enumerate every
rank-eight set exactly once and agree off `mathcal D`; deleting the common
unchanged values proves (3.4).  Distinctness of the deck values gives the
unique permutation, and no changed position is fixed. \(\square\)

For demands `mathcal P`, put

\[
 R_i=\{x:(p,x)\in\mathcal P,\ i\in[p-3,p]\}.          \tag{3.6}
\]

Every exact lift has `R_i subseteq T'_i`.  If a proposed exact changed set
`mathcal D` is fixed, one must first have

\[
                         R_i\subseteq T_i
                         \quad(i\notin\mathcal D).      \tag{3.7}
\]

For a UNIT family this forces every unique missing index into `mathcal D`.
On `mathcal D`, deck feasibility before chronology is then the literal Hall
problem in the off-diagonal graph

\[
 i\sim j
 \quad\Longleftrightarrow\quad
 i\ne j\text{ and }R_i\subseteq T_j,
 \qquad i,j\in\mathcal D.                              \tag{3.8}
\]

Chronology then requires adjacent assigned deck values to be Johnson-
adjacent, including the unchanged exterior neighbours of each changed
interval.  Finally, controller recovery imposes (1.1) and the rank profile
(1.2).  Thus (3.7)--(3.8) are only the first exact circuit screen, not the
lift.

### Proposition 3.2 (the 24 missing indices are not a closed circuit)

For the formerly displayed 24-pin witness, let `D_0` be its 24 distinct
unique missing middle indices.  The deck-only graph (3.8) has a perfect
matching of size 24.  If `D_0` is required to be the entire changed set,
then its positions are pairwise nonadjacent and their exterior neighbours
remain frozen.  After adding those two Johnson-neighbour tests to (3.8),
21 left positions have degree zero and the maximum matching has size 3.

For the collar-safe witness of Section 4, deck-only Hall again has size 24,
but the frozen-neighbour graph has 23 zero-degree positions and maximum
matching size 1.  Therefore either witness needs additional changed middle
indices before controller recovery is even considered.

#### Proof

This is a direct evaluation of the 24 by 24 graphs (3.8).  The verifier
reconstructs every `R_i`, deck domain, and neighbour intersection from the
frozen carrier; no optimization over an unlisted state is used. \(\square\)

## 4. The physical collar kills the old witness but not the lane

For a selected family `mathcal F` of target/cell pairs `(S,J)`, define

\[
 C_p(\mathcal F)=
 \bigcap_{(S,J)\in\mathcal F:\ p\in J}S.              \tag{4.1}
\]

### Lemma 4.1 (physical collar cut)

Every physical word realizing all cells in `mathcal F` satisfies

\[
                         A'_p\subseteq C_p(\mathcal F).
 \tag{4.2}
\]

Hence a demanded pin `(p,x)` is impossible if `x notin C_p(mathcal F)`.

#### Proof

If the union of the letters on `J` is exactly `S`, every individual letter
on `J` is contained in `S`.  Intersect over all selected intervals crossing
`p`. \(\square\)

The formerly displayed witness fails exactly twice against the retained
architecture.

* At `p=5919`, new `449 -> 12356=[5918,5919]` overlaps retained
  `19400 -> 18792=[5917,5919]` and one further retained interval.  Their
  complete collar is `{6,7,8}`, excluding demanded coordinate 0.
* At `p=6110`, new `27760 -> 12548=[6110,6111]` overlaps reserved
  `26464 -> 18983=[6108,6110]` and old
  `19568 -> 18985=[6110,6112]`.  Their collar is `{5,6,10,14}`, excluding
  demanded coordinate 4.

Thus the old displayed certificate cannot lift to a physical word under
any controller.

The UNIT lane nevertheless has a collar-safe equality certificate.  Its
five double pins are the first five rows below.

\[
\begin{array}{c|c|l}
(p,x)&q&\text{target}\to\text{cell[length]}\\ \hline
(6200,3)&6198&89\to6200[1],\ 1103\to19073[3]\\
(5863,10)&5861&13616\to5863[1],\ 13620\to12300[2]\\
(301,5)&298&16422\to301[1],\ 20516\to6738[2]\\
(4467,9)&4464&960\to17340[3],\ 1920\to10904[2]\\
(6429,4)&6426&8217\to12866[2],\ 8218\to19302[3]\\
(3226,0)&3225&21641\to3226[1]\\
(3528,10)&3525&17738\to16401[3]\\
(2787,0)&2785&2575\to2787[1]\\
(6398,12)&6396&29776\to6398[1]\\
(5205,0)&5202&21779\to11642[2]\\
(6111,4)&6108&27760\to12548[2]\\
(5214,4)&5211&10868\to11651[2]\\
(3025,4)&3022&2932\to9462[2]\\
(5216,5)&5216&9588\to11654[2]\\
(710,10)&707&5801\to13583[3]\\
(467,3)&464&4909\to13340[3]\\
(5756,9)&5753&18970\to12193[2]\\
(6360,8)&6357&311\to12797[2]\\
(3703,8)&3703&18272\to10141[2]\\
(6104,12)&6101&7504\to12541[2]\\
(1507,4)&1507&4213\to14382[3]\\
(2508,11)&2505&6308\to8945[2]\\
(237,13)&234&24610\to6674[2]\\
(6369,8)&6366&449\to12806[2].
\end{array}                                             \tag{4.3}
\]

The six old assignments are

\[
\begin{array}{c|c}
2420\to15899&4877\to16597\\
17683\to18079&2676\to18088\\
9524\to18090&19568\to18985.
\end{array}                                             \tag{4.4}
\]

The 24 pins, 29 new targets, 29 new cells, and 24 missing indices in (4.3)
are distinct in the required senses.  The new cells avoid all 1,489
reservations and the six old cells; (4.3)--(4.4) partition the 35 residual
targets.  The physical-length profile is

\[
                         (n_1,n_2,n_3)=(6,16,7),       \tag{4.5}
\]

so 23 new cells are nonsingletons.  Every one of the 24 demanded
coordinates belongs to the complete fixed-reservation/old/new collar
(4.1).  This is still only a collar-safe incidence certificate, not a
controller or physical word.

## 5. The exact residual controller and physical CSP

The following permutation form is the smallest exact controller/deck
problem.  Let `Sym(W)` act on the frozen rank-eight deck and choose

\[
                         \sigma\in\operatorname{Sym}(W),
 \qquad T'_i=T_{\sigma(i)}.                            \tag{5.1}
\]

Define, rather than independently choose,

\[
 P'_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T'_i.       \tag{5.2}
\]

### Theorem 5.1 (exact compensated-controller circuit equivalence)

There is an exact controller/deck lift of a prescribed UNIT demand family
if and only if a permutation `sigma` satisfies all of:

1. **Johnson chronology:**

   \[
                         |T'_i\triangle T'_{i+1}|=2
                         \quad(0\le i<W-1).            \tag{5.3}
   \]

2. **Controller ranks:** `|P'_p|` has the complete profile (1.2).
3. **Erosion--dilation equality:**

   \[
                         T'_i=\bigcup_{p=i}^{i+3}P'_p
                         \quad(0\le i<W).              \tag{5.4}
   \]

4. **Demand containment:** `x in P'_p` for every prescribed `(p,x)`.

For comparison with the frozen controller, put

\[
 \delta^+_{p,x}=1_{\{x\in P'_p\setminus P_p\}},
 \qquad
 \delta^-_{p,x}=1_{\{x\in P_p\setminus P'_p\}}.       \tag{5.5}
\]

Then every solution automatically satisfies

\[
 \sum_x\delta^+_{p,x}=\sum_x\delta^-_{p,x}
 \quad\text{for every }p,                             \tag{5.6}
\]

\[
 \sum_p(\delta^+_{p,x}-\delta^-_{p,x})\equiv0\pmod3
 \quad\text{for every }x.                             \tag{5.7}
\]

Thus compensation is an exact propagation cut, but not a substitute for
the deck permutation, chronology, or erosion--dilation constraints.

#### Proof

From an exact lift, the `T'_i` exhaust the rank-eight deck, so they define a
unique permutation (5.1).  Maximal erosion gives (5.2), residence gives the
rank profile, and factorability gives (5.4).  This proves necessity.

Conversely, (5.1) exhausts the deck exactly; (5.3) makes it a Johnson
chronology; (5.2)--(5.4) make `P'` its exact resident depth-three
controller; and Condition 4 installs every demanded controller incidence.
This proves sufficiency.  Equation (5.6) is the equality of old and new
positionwise ranks.  Since every exact-deck controller count has the form

\[
                         p'_x=3432-3i'_x,
\]

subtracting the frozen count proves (5.7). \(\square\)

To add the physical word, introduce Boolean pins

\[
                         a_{p,x}=1_{\{x\in A'_p\}}.
\]

### Theorem 5.2 (exact physical extension for fixed cells)

Fix a controller solution of Theorem 5.1 and a selected family
`mathcal F` containing the 1,489 retained pairs, six old pairs, and 29 new
pairs.  A nonempty physical word realizes the middle chronology, every
prescribed pin, and every selected cell union if and only if

\[
 a_{p,x}\le1_{\{x\in P'_p\}},
 \qquad \sum_xa_{p,x}\ge1,                            \tag{5.8}
\]

\[
 1_{\{x\in T'_i\}}=\bigvee_{p=i}^{i+3}a_{p,x},        \tag{5.9}
\]

\[
 a_{p,x}=1\quad\text{for every demanded }(p,x),       \tag{5.10}
\]

and, for every selected `(S,J) in mathcal F`,

\[
 a_{p,x}=0\quad(p\in J,\ x\notin S),                 \tag{5.11}
\]

\[
 \bigvee_{p\in J}a_{p,x}=1
       \quad\Longleftrightarrow\quad x\in S.          \tag{5.12}
\]

#### Proof

These equations are the literal statements `A'_p subseteq P'_p`,
nonemptiness, `D^3A'=T'`, pin selection, and
`union_(p in J) A'_p=S`.  Hence they are necessary and sufficient. \(\square\)

Equation (5.9), together with (5.8), is equivalent to the complete forced-
port and controller-run pinning theorem: internal run endpoints are selected,
all pin gaps are at most four, and the exact one-sided boundary rules hold.
No separate abstract incidence or rankwise Hall argument can replace it.

For the residual selector, let `u_(S,c)` be binary and zero outside the
audited old/new candidate graph.  In addition to activating
(5.11)--(5.12) when `u_(S,c)=1`, exact retained matching requires

\[
 \sum_c u_{S,c}=1\quad(S\text{ residual}),
 \qquad
 \sum_Su_{S,c}\le1\quad(c\text{ physical}),           \tag{5.13}
\]

and sum one at each of the six old cells.  These equations couple the old
choices to the 29 new choices; six independent old-cell bits alone are not
enough.  The collar-safe certificate fixes one exact solution of this
selector layer via (4.3)--(4.4).

For the trace-two/common-owner architecture, let `mathcal L_p` be the
actually active owner family through `p`.  Every `L in mathcal L_p` must
contain `A'_p`, and one must choose

\[
 \Gamma_p\subseteq\mathcal L_p,
 \qquad |\Gamma_p|\le2,
\]

with the literal meet equation

\[
 A'_p=P'_p\cap\bigcap_{L\in\Gamma_p}L.                \tag{5.14}
\]

together with every protected and deadline window.  These are subsequent
constraints on the same physical word, not a new matching layer.

## 6. Proved/open boundary

Proved:

1. no 24-pin cover lifts by changing only its demanded controller positions;
2. no nonempty separated family of isolated UNIT edits closes the exact
   deck;
3. the old displayed 24-pin witness is physically impossible;
4. a different 24-pin cover passes every fixed collar test;
5. the 24 unique missing indices of either witness are not a closed
   chronological deck circuit; and
6. Theorems 5.1--5.2 are exact necessary-and-sufficient formulations of the
   remaining controller/deck and fixed-cell physical problems.

Not proved:

1. a permutation `sigma` satisfying Theorem 5.1 for the collar-safe witness;
2. a physical extension satisfying Theorem 5.2;
3. the trace-two/common-owner meet, protected upper windows, or deadlines;
4. impossibility for all interacting 24-pin circuits; or
5. a Hall-zero `k=15` word.

The collar-safe assertion concerns exactly the listed 1,489 retained, six
old, and 29 new intervals; any additional owner or protected interval can
add a new collar cut and must be included in `mathcal L_p`.

The smallest positive finite target is now unambiguous: solve Theorem 5.1
for the collar-safe witness (4.3), necessarily with a changed deck set
strictly larger than its 24 missing indices and with a nondemanded change in
the collar (2.2); then solve the single physical system (5.8)--(5.14).

Reproduce every finite count, collar, matching, and certificate assertion
with

```text
python3 scratch/audit_k15_compensated_controller_circuit_gate.py
```
