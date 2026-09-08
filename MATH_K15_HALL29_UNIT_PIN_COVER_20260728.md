# The exact unit-controller-pin cover of the `k=15` Hall-29 core

Date: 2026-07-28

Status: exact finite theorem for the authoritative frozen Hall-29 carrier.
The sharp count is 24 in the positive-defect UNIT model, and an explicit
24-pin witness is complementary to the six surviving old cells.  This is
not a legal controller rethreading and therefore does not solve `k=15`.
A subsequent simultaneous-collar audit proves that this particular witness
cannot be physical; a different collar-safe equality witness is recorded in
`THREAD_H_K15_COMPENSATED_CONTROLLER_CIRCUIT_GATE_20260728.md`.

## 1. Controller-port formulation

Let

\[
 T_0,\ldots,T_{W-1}\in {[15]\choose 8},\qquad W=6435,
\]

be the frozen depth-three resident Johnson carrier, and put

\[
 P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i.
 \tag{1.1}
\]

By erosion--Johnson duality, the flat interior of `P` is a rank-five
Johnson path.  Both singleton transition identities

\[
 P_p\setminus P_{p+1}=\{\alpha_p\},\qquad
 P_p\setminus P_{p-1}=\{\beta_{p-4}\}                 \tag{1.1a}
\]

hold simultaneously for `4<=p<=W-2`.  Outside that range the defined
one-sided difference is retained and an undefined port is omitted.  If `A`
is a physical factor with `D^3A=T`, then, for `1<=p<=W+1`,

\[
 (P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1})
 \subseteq A_p\subseteq P_p,                         \tag{1.2}
\]

and on every internal coordinate run of `P`, the positions selected into
`A` include both run endpoints and have consecutive gaps at most four.
Thus `A` is exactly a pinning of the controller `P`.
At the two source endpoints the nonexistent port is omitted:

\[
 P_0\setminus P_1\subseteq A_0\subseteq P_0,
 \qquad
 P_{W+2}\setminus P_{W+1}\subseteq A_{W+2}\subseteq P_{W+2}.
 \tag{1.2a}
\]

The audited compact Hall-29 atlas has 4,045 defect-one records.  Of these,
3,807 are **positive-defect** records

\[
             (S,c,J,x),\qquad x\in S,qquad
             x\notin\bigcup_{p\in J}P_p,              \tag{1.3}
\]

with no bad mandatory coordinate and no empty source position.  The other
238 records have one bad mandatory coordinate and are not part of the
present model.

A **UNIT controller pin** is a pair `u=(p,x)` occurring in a record (1.3),
with `p in J`, such that exactly one carrier state in the defining window
for `P_p` omits `x`:

\[
 \left|\{i:\max(0,p-3)\le i\le\min(p,W-1),\ x\notin T_i\}\right|=1.
 \tag{1.4}
\]

At the envelope level, the operation asks for the new controller incidence
`x in P'_p`.  A physical lift must additionally select the pin
`x in A'_p`; otherwise the assigned target cell still does not contain `x`.
Condition (1.4) makes the demand a one-carrier-boundary defect, but does not
make it a legal one-vertex edit.

For a pin `u`, let `I(u)` be its set of target/cell pairs `(S,c)` from
(1.3).  Its service multiplicity is the two-coordinate matching number

\[
 \mu(u)=\max\{|M|:M\subseteq I(u),\ 
       \pi_{\rm target}|_M\text{ and }\pi_{\rm cell}|_M
       \text{ are injective}\}.                       \tag{1.5}
\]

Raw target degree is not the right statistic.  For example, `(3025,4)`
touches three targets, but all three occurrences use physical cell 9462,
so its service multiplicity is one.

## 2. Exact service census and the 24-pin lower bound

There are 1,602 UNIT pin types.  Their service multiplicities are

\[
          \#\{u:\mu(u)=1\}=1594,
          \qquad \#\{u:\mu(u)=2\}=8,                 \tag{2.1}
\]

and no pin has service multiplicity at least three.  The eight double
services are

\[
\begin{array}{c|c}
(301,5)&(16422,301),(20516,6738)\\
(2453,5)&(16422,8890),(20516,15326)\\
(4467,9)&(960,17340),(1920,10904)\\
(4708,2)&(6308,11146),(20516,4708)\\
(5862,10)&(9524,5862),(13620,12300)\\
(5863,10)&(13616,5863),(13620,12300)\\
(6200,3)&(89,6200),(1103,19073)\\
(6429,4)&(8217,12866),(8218,19302).
\end{array}                                             \tag{2.2}
\]

The first, second, and fourth rows of (2.2) form a conflict triangle: any
two repeat target 20516 or both targets.  The fifth and sixth rows conflict
at target 13620 and cell 12300.  The remaining three rows are mutually
compatible and disjoint from those two conflict classes.  Consequently at
most

\[
                         1+1+3=5                       \tag{2.3}
\]

double services can coexist with distinct targets and cells.

### Theorem 2.1 (sharp UNIT exposure count)

Any positive-defect UNIT-pin repair exposing 29 distinct residual targets
at 29 distinct physical cell addresses uses at least 24 pins.  This remains
true after requiring that the six omitted targets be one selectable target
from each of the six surviving old cells.  The bound 24 is attained in that
retained architecture.

#### Proof

If `t` pins are used, give each used pin one of its served addresses.  Every
further address makes that pin a double service.  By (2.1) no pin supplies
two further addresses, and by (2.3) at most five pins can supply even one.
Thus at most `t+5` distinct target/cell addresses are exposed.  Hence
`29<=t+5`, or `t>=24`.

The 24 rows in Section 3 expose 29 distinct new targets at 29 distinct new
cells.  The six remaining targets use the six old cells, one from each old
pair.  This proves sharpness under the retained target-choice constraint.
\(\square\)

The earlier count 14 belongs to a strictly weaker relaxation in which an
arbitrary erosion incidence may be inserted regardless of how many of its
four defining carrier states omit the coordinate.  It is not the UNIT
controller-pin bound and is not used here.

## 3. An old-pair-complementary 24-pin certificate

The table gives `pin`, its unique missing carrier index, and the served
`target -> cell [physical length]` assignments.

\[
\begin{array}{c|c|l}
(p,x)&q&\text{assignments}\\ \hline
(6429,4)&6426&8217\to12866[2],\ 8218\to19302[3]\\
(5863,10)&5861&13616\to5863[1],\ 13620\to12300[2]\\
(6200,3)&6198&1103\to19073[3],\ 89\to6200[1]\\
(301,5)&298&16422\to301[1],\ 20516\to6738[2]\\
(4467,9)&4464&1920\to10904[2],\ 960\to17340[3]\\
(4772,13)&4772&24610\to11210[2]\\
(4520,6)&4517&4213\to10957[2]\\
(3809,5)&3809&18272\to16684[3]\\
(5919,0)&5916&449\to12356[2]\\
(2787,0)&2785&2575\to2787[1]\\
(5205,4)&5205&17683\to11643[2]\\
(1918,10)&1915&7504\to8355[2]\\
(6360,8)&6357&311\to12797[2]\\
(2237,2)&2237&6308\to2237[1]\\
(3025,5)&3025&2420\to9463[2]\\
(3528,10)&3525&17738\to16401[3]\\
(5214,4)&5211&10868\to11651[2]\\
(5805,9)&5805&4909\to18680[3]\\
(5216,5)&5216&9524\to11654[2]\\
(5682,3)&5682&18970\to12120[2]\\
(6398,12)&6396&29776\to6398[1]\\
(3226,0)&3225&21641\to3226[1]\\
(6110,4)&6108&27760\to12548[2]\\
(711,12)&709&5801\to13584[3].
\end{array}                                             \tag{3.1}
\]

The six old assignments are

\[
\begin{array}{c|c}
2932\to15899&4877\to16597\\
21779\to18079&2676\to18088\\
9588\to18090&19568\to18985.
\end{array}                                             \tag{3.2}
\]

Direct comparison with the authoritative atlas proves:

1. all 24 pins, 29 new targets, and 29 new cells in (3.1) are distinct in
   the required senses;
2. every assignment is a positive-defect UNIT incidence;
3. the new cells avoid all 1,489 reserved cells and the six old cells;
4. (3.1) and (3.2) cover all 35 residual targets exactly once; and
5. the new-cell physical-length histogram is

\[
                (n_1,n_2,n_3)=(7,15,7).                \tag{3.3}
\]

Thus 22 of the 29 new addresses are nonsingletons.  The independent
run-boundary/rank argument requires at least 13 length-two or length-three
addresses in any retained exactly-29-address repair.  Certificate (3.1)
meets that condition.  Therefore the 13-cell mixed-row tax and the sharp
24-UNIT-pin count are simultaneously feasible in the incidence relaxation;
their conjunction is not the remaining obstruction.

All 24 missing carrier indices `q` in (3.1) are distinct.  Hence any
same-position lift that realizes every designated incidence `x in P'_p`
must change at least 24 indexed carrier states: the unique old state `T_q`
omits `x`, whereas every carrier state defining `P'_p` must contain it.

## 4. Exact controller-port lift still required

Let `D` be the 24 demanded pins in (3.1).  A physical realization is not a
choice of 24 independent bits.  It requires one controller `P'`, with the
usual boundary ranks and rank-five flat interior, and one physical pinning
`A'` with all of the following properties.

For the displayed `D`, this system is now known infeasible already at the
fixed-cell containment layer: demands `(5919,0)` and `(6110,4)` contradict
retained collars.  The conditions below remain the exact generic lift gate
and apply to the replacement collar-safe witness.

1. Every four-window union

   \[
          T'_i=\bigcup_{p=i}^{i+3}P'_p                 \tag{4.1}
   \]

   has rank eight, consecutive `T'_i` are Johnson-adjacent, and these
   windows exhaust the middle layer without repetition.

   Relative to the frozen controller, define the incidence changes

   \[
   \delta^+_{p,x}=1_{\{x\in P'_p\setminus P_p\}},\qquad
   \delta^-_{p,x}=1_{\{x\in P_p\setminus P'_p\}}.       \tag{4.1a}
   \]

   The state ranks and controller-incidence congruence force

   \[
   \sum_x\delta^+_{p,x}=\sum_x\delta^-_{p,x}
       \quad\text{for every }p,                        \tag{4.1b}
   \]

   and, for every coordinate `x`,

   \[
   \sum_p(\delta^+_{p,x}-\delta^-_{p,x})
      =3(i_x-i'_x)\equiv0\pmod3,                       \tag{4.1c}
   \]

   where `i_x,i'_x` are the internal `x`-run counts in `T,T'`.  Indeed both
   controller counts equal `3432` minus three times the appropriate run
   count.  Every demanded `(p,x) in D` imposes
   `delta^+_{p,x}=1`.  Thus each desired exposure comes with statewise
   deletions and coordinatewise mod-three compensation; neither can be
   chosen independently.

   For the displayed 24-pin certificate the demanded insertion counts by
   coordinate are

   \[
   (a_0,a_2,a_3,a_4,a_5,a_6,a_8,a_9,a_{10},a_{12},a_{13})
      =(3,1,2,4,4,1,1,2,3,2,1),                       \tag{4.1d}
   \]

   with all unlisted counts zero.  Any exact-demanded-only replacement
   would therefore need 24 deletions, one at each of the 24 distinct states,
   whose coordinate counts `d_x` satisfy `d_x congruent a_x (mod 3)`.
   Allowing additional insertions or changed states preserves (4.1b)--(4.1c)
   but changes that restricted census.
2. Every required upper occurrence of physical length at least four is
   retained.  Such a window may be checked in `P'`, since items 3--5 imply
   `D^3A'=D^3P'`.  Every short protected, owner, old, reserved, and target
   window is checked in the physical word `A'`, not merely in `P'`.
3. Every demanded `(p,x) in D` satisfies

   \[
                         x\in A'_p\subseteq P'_p.       \tag{4.2}
   \]
4. On every internal coordinate run `[u,v]` of `P'`, the selected pin set

   \[
                   Q_x=\{p\in[u,v]:x\in A'_p\}
   \]

   contains `u,v` and has consecutive gaps at most four.  The exact boundary
   rules are as follows.  A left-boundary run `[0,v]` selects `v`, has first
   selected position at most 3, and has gaps at most four.  A right-boundary
   run `[u,W+2]` selects `u`, has last selected position at least `W-1`, and
   has gaps at most four.  A full run `[0,W+2]` has first selected position
   at most 3, last selected position at least `W-1`, and gaps at most four.
5. At every source position, including one crossed by no active target,
   the exact global port cut is

   \[
   (P'_p\setminus P'_{p-1})\cup(P'_p\setminus P'_{p+1})
      \subseteq A'_p\subseteq P'_p.                   \tag{4.3}
   \]

   If the active target cells through `p` have labels `S_1,...,S_s`, this
   sharpens to

   \[
   (P'_p\setminus P'_{p-1})\cup(P'_p\setminus P'_{p+1})
      \subseteq A'_p
      \subseteq P'_p\cap S_1\cap\cdots\cap S_s.        \tag{4.3a}
   \]

   Here and throughout, a nonexistent endpoint port is omitted; equivalently
   set `P'_{-1}=P'_0` and `P'_{W+3}=P'_{W+2}` in (4.3)--(4.3a).

   Every selected target cell `J_S` must also satisfy

   \[
                       \bigcup_{p\in J_S}A'_p=S.       \tag{4.4}
   \]
6. The same word retains the 1,489 reserved cells, the six old cells,
   base eligibility, owner compatibility, trace two, the common reserve,
   and every deadline condition.

Items 1--6 are the controller-port form of the surviving
simultaneous labelled-routing theorem.  In particular, the old defect-one
atlas cannot simply be carried across a rethreading: changing `P` can lose
other envelope coordinates, create new forced ports, and change overlaps
with reserved or protected cells.  Every candidate must be recomputed on
the final common `P',A'`.

There is also no isolated one-vertex shortcut.  Suppose the unique missing
carrier state for `(p,x)` is `T_q` and all other carrier states are frozen.
For a rank-preserving trial

\[
                         T'_q=T_q-\{y\}+\{x\},          \tag{4.5}
\]

adjacency to a frozen neighbour `T_h` is preserved exactly when `x` and
`y` have the same membership indicator in `T_h`.  This follows by comparing
the new intersection size with seven, and is necessary and sufficient for
each of `h=q-1,q+1` that exists.  Even when both local tests pass, `T'_q` is
another rank-eight set already appearing elsewhere in the exact middle
deck.  A lone edit therefore duplicates `T'_q` and omits `T_q`.  Any legal
repair must close into a globally coupled rethreading.

The smallest positive UNIT-lane lemma is now exact: construct a controller
`P'` and pinning `A'` satisfying items 1--6 for some old-pair-complementary
24-pin cover.  This is sufficient, but minimal incidence size need not be
preserved by physical compatibility: a lift might require a cover using
25, 26, 27, 28, or 29 serving pins.  Therefore a negative UNIT theorem must
exclude every admissible old-pair-complementary cover of sizes 24 through
29, or first prove a reduction from a physical cover to one of size 24.
Every positive or negative argument must also retain the state-balance and
coordinate-congruence equations (4.1b)--(4.1c).
The 24-pin theorem is not a lower bound for repairs using mandatory-defect
records, non-UNIT incidences, or a globally coupled move that creates
addresses outside this atlas.

Reproduce the finite census and certificate with

```text
python3 scratch/audit_k15_hall29_unit_pin_cover.py
```
