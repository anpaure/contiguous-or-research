# Thread D: exact arity-three mixed macro--UNIT circulation at `k=15`

Date: 2026-07-28

Status: exact mixed-circulation theorem and a literal target-safe closed
controller/deck circuit for target mask `24610`.  The circuit is not a full
Shadow--Braid certificate: it loses ten lower and four upper first-shadow
masks.

## 0. Verdict

The pure consecutive-triple macro lane is acyclic and therefore cannot
close itself.  Adding ambient isolated UNIT arcs changes the answer: there
is an exact mixed circuit.

Its service block is

\[
 (4308,14,10),\quad(4309,1,10),\quad(4310,13,10),
\tag{0.1}
\]

where each tuple is `(controller position, inserted coordinate, deleted
coordinate)` and all coordinates are zero-based.  It retains the advertised
Hall record

\[
       (\text{target},\text{cell},\text{start},\text{depth})
       =(24610,10747,4309,1).
\tag{0.2}
\]

Eighteen ambient UNIT operations close its three exported deck arcs.  After
contracting operations whose controller positions are less than eight apart,
the auxiliaries consist of one three-state macro, one two-state macro, and
thirteen isolated atoms.  Together with (0.1), these sixteen atoms are
pairwise separated by at least forty controller positions.  Literal global
recomputation gives one deck 19-cycle and one deck 2-cycle.

This target ID must not be conflated with the preceding arity-two result.
The three arity-two survivors are three alternative blocks for **only** mask
`6308`.  The circuit here serves the distinct mask `24610`.

## 1. Corrected arity-three catalogue

Let

\[
 T_0,\ldots,T_{W-1}\in{[15]\choose8},\qquad W=6435,
\]

be the frozen Hall-29 chronology, and let

\[
 P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i
\tag{1.1}
\]

be its maximal erosion controller.  An arity-three candidate chooses three
distinct theoretical UNIT positions `p_0<p_1<p_2`, with each successive gap
at most seven, and performs one insertion/deletion at each.  Notice that the
support diameter may be fourteen; the condition is not `p_2-p_0<=7`.

The original search checked erosion only at the three selected positions.
The corrected source checks maximal erosion at every position in the entire
affected collar

\[
                         [p_0-3,p_2+3].
\tag{1.2}
\]

The correction removes no candidate.  A fresh compilation gives

\[
\begin{array}{c|r}
\text{connected three-position supports}&122{,}224\\
\text{option nodes}&8{,}616{,}545\\
\text{controller-legal leaves}&528{,}785\\
\text{rank-eight middle leaves}&464{,}600\\
\text{target-envelope-safe exports}&1{,}773\\
\text{exact local deck circuits}&0.
\end{array}
\tag{1.3}
\]

Of the 1,773 exports, 1,708 change three middle states and 65 change two.
There are 1,804 advertised safe incidences.  Keeping target masks distinct,
their exact incidence histogram is

\[
\begin{array}{c|rrrrrrrrr}
S&89&311&449&960&1920&2676&4213&6308&7504\\ \hline
\#&172&2&196&183&188&1&1&68&1
\end{array}
\]

and

\[
\begin{array}{c|rrrrrrrr}
S&8217&8218&9524&16422&18272&18970&20516&24610\\ \hline
\#&235&187&1&180&1&2&201&185.
\end{array}
\tag{1.4}
\]

These are target/cell incidences, not distinct blocks: one block may retain
more than one advertised record.  Envelope safety means only

\[
 S\subseteq\bigcup_{p\in I}P'_p.
\tag{1.5}
\]

It is necessary for a physical compiler and is not itself a common-word or
upper-shadow certificate.

The separate pure-macro census asks that the three changed sources and three
destinations each be consecutive deck triples.  It gives 902 distinct macro
edges on 1,452 incident triple-start vertices.  Kahn elimination removes all
1,452 vertices; the graph is a DAG, and its maximum directed path length is
four.  Of the 902 rows, 166 retain at least one advertised Hall record.

The checked-in executable under `scratch/bin` predates the export/macro
source update and must not be used.  All counts above come from a fresh
compilation of the current source.

## 2. Exact mixed macro--isolated model

The right variables are contracted physical atoms, not fictitious unit
flows.  For every fully collar-audited atom `o`, record

\[
 R_o=\text{its changed controller positions},\qquad
 S_o=\text{its changed middle indices},
\]

and its literal destination map `sigma_o:S_o->[W]`.  Put

\[
 \partial o=\sum_{s\in S_o}(e_{\sigma_o(s)}-e_s),
\qquad
 J_o=[\min R_o,\max R_o+7]\cap\mathbb Z.
\tag{2.1}
\]

Close primitive UNIT moves at distance less than eight are first contracted
and re-audited jointly as one atom.  Two distinct contracted atoms obey the
depth-three independent-collar rule exactly when their intervals `J_o` are
disjoint.

### Theorem 2.1 (exact separated mixed circulation)

Fix a target-labelled service atom `B` and a finite catalogue of fully
collar-audited auxiliary macro and isolated atoms.  A separated exact deck
closure exists if and only if binary variables `z_o`, with `z_B=1`, satisfy

\[
 \sum_{o:r\in J_o}z_o\le1
 \qquad\text{for every controller cut }r,
\tag{2.2}
\]

and, for every deck index `v`,

\[
 \sum_o z_o\,\mathbf1_{v\in S_o}
 =
 \sum_o z_o\,|\{s\in S_o:\sigma_o(s)=v\}|
 \le1.
\tag{2.3}
\]

Equivalently,

\[
                         \sum_o z_o\partial o=0
\tag{2.4}
\]

together with the source capacity in (2.3).  Expanding every selected atom's
ganged arcs gives a vertex-disjoint directed cycle system on the deck.

If the advertised occurrence is `alpha=(S,c,I)`, its exact envelope-survival
condition is, for every coordinate `a in S`,

\[
 \sum_{p\in I}q'_{p,a}\ge1,
\qquad
 q'_{p,a}=q_{p,a}+
 \sum_{o:p\in R_o}z_o(q^o_{p,a}-q_{p,a}).
\tag{2.5}
\]

#### Proof

Condition (2.2) says that distinct audited atoms have disjoint depth-three
interaction collars.  Their local controller, rank, middle-adjacency, and
erosion checks therefore compose without cross terms.  The left side of
(2.3) counts how often the original value `T_v` is removed; the middle term
counts how often it is inserted.  Equality is exactly preservation of its
multiplicity, and the upper bound makes the replacement relation a partial
permutation.  Hence all expanded arcs form vertex-disjoint directed cycles.
The converse follows by reading removal and insertion counts from such a
cycle system.  Finally, (2.2) makes the displayed formula for `q'` literal,
and (2.5) is precisely coordinatewise containment of `S` in its advertised
controller cell. \(\square\)

Theorem 2.1 is a controller/deck and target-envelope theorem.  It does not
replace the all-upper-occurrence or one-common-compiler audits.
Its equivalence is only inside the contracted, distance-eight separated
catalogue just defined.  Distance eight is the sufficient independence
convention of this lane, not a no-go for a closer cluster re-audited as one
larger atom.

### 2.1 Why pure triple macros cannot close

For `0<=i<=W-3`, put

\[
                         a_i=e_i+e_{i+1}+e_{i+2}.
\tag{2.6}
\]

A pure macro from triple start `i` to triple start `j` has boundary
`a_j-a_i`.  The linear map

\[
                         A c=\sum_i c_i a_i
\]

is injective: coordinate zero first gives `c_0=0`, coordinate one then gives
`c_1=0`, and induction gives every `c_i=0`.  If `N` is the node--arc
incidence matrix of the 902-edge macro graph, pure-macro deck balance is

\[
                         ANx=0.
\]

Thus `Nx=0`.  A nonzero nonnegative circulation contains a directed cycle,
contradicting the audited DAG.  Therefore

\[
              \boxed{\text{the pure 902-edge macro cone is pointed}.}
\tag{2.7}
\]

The exact integer image of `A` is also useful:

\[
 \operatorname{im}_{\mathbb Z}A=
 \left\{z:\sum_{v\equiv0(3)}z_v
            =\sum_{v\equiv1(3)}z_v
            =\sum_{v\equiv2(3)}z_v\right\}.
\tag{2.8}
\]

Necessity follows because every consecutive triple has one index of each
residue.  For sufficiency, solve recursively

\[
                         h_i=z_i-h_{i-1}-h_{i-2}.
\]

After matching the first `W-2` coordinates, the equal residue sums force the
last two residual coordinates to vanish.  Since a deck boundary has total
sum zero, its three residue sums must each be zero.

Consequently, in a mixed equation

\[
                 \partial B+B_1y+ANx=0,
\tag{2.9}
\]

the ambient singles `y` must first cancel the two-dimensional residue defect
of the service boundary.  Once they do,

\[
                         h=A^{-1}(-\partial B-B_1y)
\]

is unique and the algebraic macro core is the network system `Nx=h`.  Before
source and position side constraints this core is totally unimodular.  The
physical side constraints are not: adjoining a single conflict row to the
acyclic three-edge graph `1->2,2->3,1->3` gives the minor

\[
 \begin{pmatrix}
 -1&0&-1\\
  1&-1&0\\
  1& 1&0
 \end{pmatrix},
 \qquad \det=-2.
\tag{2.10}
\]

Thus the surviving optimization is genuinely a conflict-constrained macro
transshipment.  The DAG alone is not a no-go after singles are admitted.

## 3. A target-`24610` closed circuit

The service block (0.1) has literal deck arcs

\[
             4305\to2160,\qquad
             4306\to2159,\qquad
             4307\to6014.
\tag{3.1}
\]

The following eighteen ambient operations close them:

\[
\begin{array}{r|r|r|r|r}
p&x&y&\text{source}&\text{destination}\\ \hline
2163&12&4&2160&6012\\
6015&1&5&6012&3766\\
3766&13&14&3766&3569\\
3569&3&9&3569&4687\\
4687&10&8&4687&4141\\
4141&4&3&4141&1084\\
1084&14&13&1084&5162\\
5162&5&7&5162&2959\\
2962&9&12&2959&6431\\
6431&8&2&6431&3010\\
3013&7&14&3010&138\\
138&14&4&138&2158\\
2161&2&7&2158&4307\\
2159&10&1&2159&4306\\
6017&3&13&6014&6372\\
6375&4&1&6372&3723\\
3726&10&14&3723&2809\\
2809&7&3&2809&4305.
\end{array}
\tag{3.2}
\]

The position-conflict components of (0.1)--(3.2) are:

* the service macro on `{4308,4309,4310}`;
* an auxiliary three-state macro on `{2159,2161,2163}`;
* an auxiliary two-state macro on `{6015,6017}`; and
* thirteen singleton atoms.

The auxiliary three-state macro has joint literal arcs

\[
 2158\to4307,\qquad2159\to4306,\qquad2160\to6012,
\tag{3.3}
\]

and the two-state macro has

\[
                       6012\to3766,qquad6014\to6372.
\tag{3.4}
\]

The three-state atom (3.3) is not one of the 902 pure consecutive-triple
macros: its destinations are not consecutive.  This is exactly how the
circuit escapes the pointed cone (2.7).  The two-state atom is locally legal
but not itself target-safe.

All sixteen contracted atoms are pairwise separated by at least forty
positions.  Their expanded deck arcs form precisely

\[
\begin{split}
(&138,2158,4307,6014,6372,3723,2809,4305,2160,6012,\\
 &3766,3569,4687,4141,1084,5162,2959,6431,3010)
\end{split}
\tag{3.5}
\]

and

\[
                              (2159,4306).
\tag{3.6}
\]

These are a 19-cycle and a 2-cycle, so (2.3) is exact.

### Theorem 3.1 (literal verification)

Applying the 21 controller swaps in (0.1)--(3.2) gives a controller `P'`
and chronology

\[
                         T'_i=\bigcup_{p=i}^{i+3}P'_p
\]

with all of the following properties.

1. Every `T'_i` has rank eight and every consecutive pair is
   Johnson-adjacent.
2. `P'` is exactly the maximal erosion of `T'` at every controller position.
3. The multiset `{T'_i}` is the original rank-eight deck exactly.
4. Exactly 21 controller states and 21 middle states change, with deck cycles
   (3.5)--(3.6).
5. At the advertised cell,

   \[
    P'_{4309}=16931,\qquad P'_{4310}=8739,
   \]

   and

   \[
    P'_{4309}\cup P'_{4310}=25123\supseteq24610.
   \tag{3.7}
   \]

#### Proof

Start from (1.1), xor the advertised `(x,y)` bits at the 21 listed
positions, reconstruct every four-controller union, and re-intersect every
four-middle window.  The resulting ranks, adjacencies, erosion equality,
deck Counter, changed-label permutation, and target containment are exactly
the assertions checked by
`scratch/verify_threadD_k15_arity3_mixed_circuit_24610.py`.  That verifier
also applies each contracted component separately before composing them.
The component separation makes this a finite literal proof, not an
additivity assumption about overlapping raw arcs. \(\square\)

## 4. Exact remaining obstruction

The circuit closes the controller and middle deck while retaining one
advertised Hall target.  It does not preserve the first-shadow ledgers.  On
the lower side it loses exactly

\[
\{947,1852,1957,12685,12935,16821,17959,18226,21285,25379\},
\tag{4.1}
\]

and on the upper side it loses exactly

\[
                         \{3901,18357,21623,29479\}.
\tag{4.2}
\]

There are no new lower or upper first-shadow **support masks**.  This is not
an occurrence-multiset assertion: multiplicities are redistributed among
masks already in the support.  Hence the four upper support losses already
violate SB2 for this literal circuit.  The ten lower losses could be repaired
only through the same common compiler or a larger circuit; no such repair is
proved here.

The result therefore advances the finite gate exactly one step:

\[
 \boxed{
 \begin{array}{c}
 \text{isolated target service impossible}\\
 \Downarrow\\
 \text{target-safe arity-three macro + mixed auxiliary circulation exists}\\
 \Downarrow\\
 \text{restore upper occurrences and solve the one-common-compiler ledger.}
 \end{array}}
\tag{4.3}
\]

It is a positive controller/deck theorem, not the constant-one theorem and
not a complete 29-address Hall repair.

## 5. Reproduction

Compile the current source, rather than the stale checked-in binary:

```text
clang++ -O3 -DNDEBUG -std=c++20 \
  scratch/search_k15_full_unit_service_circuits.cpp \
  -o /tmp/threadD_k15_service_circuits
```

The catalogue commands are

```text
python3 scratch/export_k15_full_unit_service_instance.py |
  /tmp/threadD_k15_service_circuits 3 export

python3 scratch/export_k15_full_unit_service_instance.py |
  /tmp/threadD_k15_service_circuits 3 macro

python3 scratch/export_k15_full_unit_service_instance.py |
  /tmp/threadD_k15_service_circuits 3
```

The final default-mode command, not export mode, independently checks the
zero exact-local-deck-circuit count.

The positive circuit is frozen in
`scratch/threadD_k15_arity3_mixed_circuit_24610.json`.  Verify it with

```text
python3 scratch/verify_threadD_k15_arity3_mixed_circuit_24610.py
```

The generic separated binary model is
`scratch/threadD_k15_mixed_macro_isolated_circulation.py`; it uses OR-Tools
for the deck, position, and labelled-incidence system, then verifies target
survival and the complete controller/deck reconstruction literally.
