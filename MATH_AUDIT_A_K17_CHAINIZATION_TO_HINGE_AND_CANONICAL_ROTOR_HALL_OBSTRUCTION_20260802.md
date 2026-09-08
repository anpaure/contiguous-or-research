# K17 three-level chainization: proof audit, hinge interface, and the canonical-rotor Hall obstruction

**Date:** 2026-08-02  
**Lane:** A, integral rotor fusion  
**Status:** independently audited static theorem; unconditional obstruction on
the canonical disjoint-increment functional-rotor face; exact conditional
Hoffman/rooted-Euler interface.  Enriched or coupled literal states are not
excluded.  No upper-shadow or common-cap/compiler claim is made.

## 0. Outcome

The proof of
`MATH_THEOREM_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md` is correct:
the 65,535 nonempty subsets of `[17]` of rank at most eight partition into
24,310 inclusion chains of length at most three, one per rank-eight root.
The copied explicit static table

```text
scratch/k17_exact_depth3_owner_payload_table_20260802/
  k17_depth3_owner_payload.tsv
```

also replays exactly: all roots, owners, and lower targets occur once, every
chain is nested, and every root is a facet of its assigned owner.

This static table cannot, however, be inserted unchanged into the strict
canonical functional-rotor normal form.  The exact copied table has a
predecessor Hall shore of deficiency at least

\[
                              12\,999.                 \tag{0.1}
\]

More generally, every three-level Dilworth partition produced on these
compressed levels has canonical predecessor deficiency at least `9,503`.
The obstruction is only to the face on which every three-member chain is
realized by its three disjoint difference blocks.  Overlapping/enriched
source letters, occurrence-labelled filler values, two-sided realizations,
or factor-critical bridge packets may change the complete states and escape
the cut.

Consequently the correct use of the new table is the general fixed-table
Hoffman/hinge theorem: its owner and named-target resources are frozen and
private, while its accepted literal tail/head states still have to be
constructed and balanced.  The table removes target selection, not state
selection.

## 1. Independent audit of the chainization theorem

Let

\[
 P_0=\bigcup_{s=1}^{6}{[17]\choose s},\qquad
 P_1={[17]\choose7},\qquad P_2={[17]\choose8},
\]

with containment retained only between different displayed levels.  Their
sizes are

\[
       n_0=21\,777,\qquad n_1=19\,448,\qquad n_2=24\,310.       \tag{1.1}
\]

For `S in P_0` of rank `s` and `T in P_1`, the source theorem uses

\[
 \mu_{01}(S,T)=
 {\mathbf1_{S\subset T}\over n_0{17-s\choose7-s}}.             \tag{1.2}
\]

The `S`-marginal is `1/n_0`.  For fixed `T`,

\[
 \sum_{S\subset T}\mu_{01}(S,T)
 ={1\over n_0}\sum_{s=1}^{6}
 {{7\choose s}\over{17-s\choose7-s}}
 ={1\over n_0}\sum_{s=1}^{6}
 {{17\choose s}\over{17\choose7}}
 ={1\over n_1}.                                            \tag{1.3}
\]

Likewise the uniform weight `1/(10n_1)` on each containment
`T subset U`, `T in P_1`, `U in P_2`, has marginals `1/n_1` and `1/n_2`
because `10n_1=8n_2`.  Conditional composition through `P_1` gives a random
chain `S subset T subset U` uniform on each level.  An antichain meets this
chain at most once, hence

\[
 {|A_0|\over n_0}+{|A_1|\over n_1}+{|A_2|\over n_2}\le1.       \tag{1.4}
\]

Since every `n_i<=n_2`, this implies `|A|<=n_2`; equality is attained by
`P_2`.  Dilworth therefore gives `n_2` chains.  There are exactly `n_2`
rank-eight elements and a chain contains at most one, so every resulting
chain contains exactly one.  This proves the static theorem.

The owner attachment is also exact once a rank8--rank9 perfect incidence
matching is fixed.  Every earlier chain member lies in its rank-eight root,
and hence in the matched rank-nine owner.  On the complete middle incidence
graph, existence is automatic because both shores are 9-regular.  For a
selected physical phase it remains conditional on that phase containing the
claimed perfect matching; the copied table itself directly certifies a
bijective facet assignment.

### 1.1 Chain-shape identities

Let

* `x` be the number of `P_0-P_1-P_2` chains;
* `y` the number of `P_0-P_2` chains;
* `z` the number of `P_1-P_2` chains; and
* `w` the number of singleton `P_2` chains.

Then

\[
 x+y=n_0,\qquad x+z=n_1,\qquad x+y+z+w=n_2.            \tag{1.5}
\]

Thus

\[
 16\,915=n_0+n_1-n_2\le x\le n_1=19\,448,              \tag{1.6}
\]

and the number of chains of length at most two is

\[
                              n_2-x.                    \tag{1.7}
\]

For the copied table,

\[
 (w,y+z,x)=(1\,748,3\,899,18\,663).                    \tag{1.8}
\]

The bottom-rank histogram among its length-three chains is

\[
\begin{array}{c|rrrrrr}
s&1&2&3&4&5&6\\ \hline
\#&17&136&680&2\,320&5\,485&10\,025.
\end{array}                                             \tag{1.9}
\]

## 2. The ordered canonical-state obstruction

Consider a three-member compressed chain

\[
                    L_i\subset M_i\subset U_i,
 \qquad |L_i|=s_i,\quad |M_i|=7,\quad |U_i|=8.          \tag{2.1}
\]

Its canonical strict suffix-increment state is

\[
 h_i=(a_i,b_i,c_i)
     =(U_i\setminus M_i,\ M_i\setminus L_i,\ L_i),      \tag{2.2}
\]

with size signature

\[
                         \sigma(i)=(1,7-s_i,s_i).        \tag{2.3}
\]

The direction convention is important.  In the functional rotor, an arc
**from tail state `h_j` to head state `h_i`** requires

\[
                         (b_j,c_j)=(a_i,b_i),            \tag{2.4}
\]

and its owner is

\[
                         \kappa(j,i)=U_i\cup a_j.        \tag{2.5}
\]

### Lemma 2.1 (signature rotation)

For any legal canonical rank8-to-rank9 arc `j -> i`,

\[
            \sigma(j)=(|c_i|,|a_i|,|b_i|).             \tag{2.6}
\]

#### Proof

Equation (2.4) fixes the last two coordinates.  Both state unions have
rank eight, so

\[
 |a_j|=8-|b_j|-|c_j|
      =8-|a_i|-|b_i|=|c_i|.
\]

This proves (2.6).  Notice that (2.5), a fixed owner phase, residence, and
all other guards can only delete arcs from this necessary relation.  \(\square\)

### Corollary 2.2 (rigid three-chain incompatibility)

If both `i` and `j` are three-member compressed chains, with bottom ranks
`s` and `t`, respectively, then `j -> i` is possible only if

\[
                              s=1,\qquad t=6.           \tag{2.7}
\]

Indeed, equating the predecessor signature
`(1,7-t,t)` with the required rotation `(s,1,7-s)` first gives `s=1`, then
`t=6`.

### Theorem 2.3 (universal canonical Hall deficit)

On every such three-level chain partition, the strict canonical
predecessor graph has Hall deficiency at least

\[
                              9\,503.                  \tag{2.8}
\]

For the copied table its deficiency is at least `12,999`.

#### Proof

Let `H` be the head roles whose chain has length three and bottom rank
greater than one.  By Corollary 2.2, no length-three role can be a
predecessor of a member of `H`.  Therefore

\[
                         N^-(H)\subseteq
     \{\hbox{roles on chains of length at most two}\}.           \tag{2.9}
\]

There are at most 17 length-three chains with bottom rank one.  Hence, for
the general chain-shape parameter `x`,

\[
 |H|-|N^-(H)|
 \ge (x-17)-(n_2-x)=2x-24\,327\ge9\,503,              \tag{2.10}
\]

using (1.6).  In the copied table, (1.8)--(1.9) give

\[
 |H|=18\,663-17=18\,646,qquad |N^-(H)|\le5\,647,
\]

and hence deficiency at least `18,646-5,647=12,999`.  \(\square\)

This is already a zero-boundary predecessor Hall obstruction.  A fixed
owner phase or any literal guard only shrinks `N^-(H)`.  Adding `q` unit
predecessor capacities can reduce this certified deficit by at most `q`;
in particular, a bounded bank of such unit tokens cannot close it.

## 3. Exact mask form of a forced predecessor

The size argument has a useful occurrence-level form.  Let the owner phase
attach root `U` to

\[
                              \phi(U)=U\cup\{z_U\}.     \tag{3.1}
\]

Let `L_U subset M_U subset U` be the suffix flag inducing `h_U`.  If a
canonical state on root `V` is a legal predecessor of `U`, then for some
`x in L_U`,

\[
\boxed{
 \begin{aligned}
  L_V&=M_U\setminus L_U,\\
  M_V&=U\setminus L_U,\\
  V&=(U\setminus\{x\})\cup\{z_U\}.
 \end{aligned}}                                             \tag{3.2}
\]

Conversely, these identities give the required two-block overlap and owner
union.

To see this, (2.4) gives

\[
 L_V=c_V=b_U=M_U\setminus L_U,qquad
 M_V=b_V\cup c_V=a_U\cup b_U=U\setminus L_U.          \tag{3.3}
\]

The remaining block has size `|L_U|`, is disjoint from `U-L_U`, and must
add exactly the new owner coordinate `z_U`; it is therefore

\[
                   a_V=(L_U\setminus\{x\})\cup\{z_U\} \tag{3.4}
\]

for a unique omitted `x in L_U`, which proves (3.2).

This formula is a necessary literal-state relation, not a claim that the
assigned chain on `V` contains `L_V` and `M_V`.  That extra alignment is
exactly what fails massively on the canonical compressed table.

## 4. The proof-safe fixed-table Hoffman/rooted-Euler gate

Freeze the copied rows.  Row `i` now has:

* one rank-eight root `U_i`;
* one assigned rank-nine owner `T_i`; and
* one disjoint named payload chain `C_i`.

Let `E_i` be the catalogue of **complete occurrence-labelled literal
arcs** which carry this same owner and every named target of `C_i`.
Any incidental filler outputs, residence histories, protected source
addresses, and lower-palette resources must be part of the catalogue
semantics.  The static theorem supplies none of these arcs.

Let `P` be a protected root/path bank, with boundary

\[
                              \eta=\partial P.          \tag{4.1}
\]

If certified submenus factor as Cartesian rectangles

\[
                              A_i\times H_i\subseteq E_i,         \tag{4.2}
\]

put

\[
 \ell_A(X)=|\{i:A_i\subseteq X\}|,qquad
 r_H(X)=|\{i:H_i\cap X\ne\varnothing\}|.             \tag{4.3}
\]

### Theorem 4.1 (exact conditional balanced selector)

On the certified rectangle face, one can select one arc from every frozen
row with total boundary `-eta` if and only if

\[
 \boxed{\ell_A(X)-r_H(X)\le\eta(X)\qquad(X\subseteq V).}         \tag{4.4}
\]

The selector is integral and automatically retains every fixed owner and
every named lower target exactly once.

For a connected rooted Euler realization, it is additionally necessary and
sufficient that one can reserve arcs from distinct rows whose union with
`P` contains a spanning tree of the used state set, and that (4.4) holds
for the residual rectangles with the reserved boundary added to `eta`.

#### Proof

The possible tail-count vectors and head-count vectors are the integral
transversal-polymatroid bases generated by the lists `A_i` and `H_i`.
Their shifted intersection is nonempty exactly under (4.4), by the standard
polymatroid-intersection/Hoffman cut calculation.  Integrality gives one
tail and one head per row; Cartesianity pairs them into a legal arc.
Reserving a spanning tree reduces connected completion to the same theorem
on the residual rows.  Conversely, any connected selector contains such a
distinct-row spanning tree and witnesses all residual cuts.  This is the
fixed-table specialization of the already frozen protected hinge theorem.
\(\square\)

If the literal menus are not Cartesian, (4.4) is not sufficient.  The exact
gate is then the occurrence-labelled integer system

\[
 \sum_{e\in E_i}x_{i,e}=1,qquad
 \sum_{i,e}x_{i,e}\partial e=-\eta,qquad x_{i,e}\in\{0,1\},    \tag{4.5}
\]

together with a connected-support certificate.  Projecting a correlated
menu to separate tail and head lists can create false completions.

## 5. Cross-depth factor-critical use of the table

Partition the frozen rows into modules `K_q`.  Their owner and named-target
resources are automatically disjoint, which removes one major hypothesis
from the abstract factor-critical conveyor.  What remains genuinely open is
to construct complete-state realizations

* `F_q(r,c)`, using every row of `K_q` except one root row and leaving one
  tail socket; and
* bridges from one module socket to the next module root, realizing exactly
  the omitted row with compatible residence histories.

If these realizations form port-complete, jointly matching-compatible
atlases, their quotient digraph `Gamma` has an exact balanced completion if
and only if

\[
                              |N^+(S)|\ge|S|\quad(S\subseteq Q). \tag{5.1}
\]

A directed module path forest with `c` paths reduces the complete remaining
bank to the `2^c` Hall rows between its `c` sinks and `c` roots; a Hamilton
path leaves one endpoint pair and a Hamilton cycle gives a balanced Euler
component.  This is the weakest currently proved mechanism by which many
local deficit-one copies can telescope instead of accumulating.

The `12,999` cut proves that a bridge atlas which merely permutes the
canonical difference states cannot suffice.  Successful cross-depth fusion
must change complete literal states (or use another noncanonical realization),
not merely reassign the already fixed owner/payload rows.

## 6. Scope

Proved here:

1. the three-level LYM/Dilworth proof is valid;
2. the copied K17 table is an exact owner/root/named-target table;
3. the canonical disjoint-increment functional rotor on that table has an
   explicit Hall shore of deficiency at least `12,999`;
4. every such compressed partition has the universal lower bound `9,503`;
5. (3.2) is the exact forced canonical predecessor identity; and
6. (4.4)--(4.5) are the correct fixed-table balanced/rooted-Euler gates.

Not proved:

* any accepted enriched-state catalogue `E_i`;
* Cartesianity, residence, or a protected spanning skeleton;
* a factor-critical Boolean module/bridge atlas;
* arbitrary-width upper witnesses; or
* common-cap/source/compiler compatibility.

The lightweight verifier

```text
scratch/a_k17_chain_hinge_20260802/
  audit_a_k17_chain_hinge_20260802.py
```

replays the copied table and every numerical identity used in the explicit
and universal Hall bounds.
