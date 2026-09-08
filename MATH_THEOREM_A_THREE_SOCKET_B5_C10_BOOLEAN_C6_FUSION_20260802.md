# Three-socket `B_5` `C10`--Boolean-`C6` fusion

**Date:** 2026-08-02  
**Status:** exact local four-resource theorem.  It fuses fifteen closed
`C4` components to one `C60`.  It does not by itself open the final cycle,
plant the module in a complete central table, or prove history, residence,
upper-shadow, source, or compiler compatibility.

## 1. Data and the three sockets

Fix

\[
 [2m]=H\mathbin{\dot\cup}K,\qquad |K|=5,qquad m\ge5.
\]

Choose `C_0 subset H`, `|C_0|=m-4`, and distinct
`alpha,beta,gamma,delta in H-C_0`.  Identify `K` with `Z_5`, and put

\[
 p_i=\{i,i+1\},\quad d_i=\{i,i+2\},\quad
 U_i=\{i,i+1,i+2\}.                                \tag{1.1}
\]

Use the following three adjacent-core sockets:

\[
\begin{array}{c|c|c|c}
j&\text{intersection core}&A_j&B_j\\ \hline
1&C_0+\alpha&C_0+\alpha+\gamma&C_0+\alpha+\delta\\
2&C_0+\gamma&C_0+\beta+\gamma&C_0+\gamma+\delta\\
3&C_0+\beta &C_0+\alpha+\beta &C_0+\beta+\delta.
\end{array}                                         \tag{1.2}
\]

Their six endpoint cores, three intersection cores, and three union cores
are respectively

\[
\begin{aligned}
&\alpha\gamma,\alpha\delta,
  \beta\gamma,\gamma\delta,
  \alpha\beta,\beta\delta,\\
&\alpha,\gamma,\beta,\\
&\alpha\gamma\delta,\beta\gamma\delta,
  \alpha\beta\delta,
\end{aligned}                                       \tag{1.3}
\]

with `C_0` suppressed.  Every entry in each row is distinct.  By the exact
socket-conflict criterion, the three sockets are pairwise disjoint in all
named resources.

In every endpoint fibre use the palette-equivalent `B_5` phases

\[
 E^+=\{p_i d_i:i\in Z_5\},\qquad
 E^-=\{p_i d_{i-1}:i\in Z_5\}.                     \tag{1.4}
\]

Orient the `A_j` phase from its `p` shore to its `d` shore and the `B_j`
phase oppositely.  The vertical bank of socket `j` consists of all ten
diamonds joining `A_j+Y` to `B_j+Y`, `Y in {K choose 2}`; orient `p`-type
verticals from `B_j` to `A_j` and `d`-type verticals from `A_j` to `B_j`.
Thus same horizontal phases plus the vertical bank form five directed
`C4` cycles, while switching only `A_j` forms one directed `C20`.

The displayed support uses `(m-4)+4+5=m+5<=2m` coordinates, exactly the
stated range `m>=5`.

## 2. The old verticals are ten parallel Boolean hexes

Fix `X in {K choose 2}` and write `S=C_0+X`.  The selected vertical edges
of the three sockets are

\[
\begin{array}{lll}
o_1:&S+\alpha+\gamma&\longrightarrow S+\alpha+\delta,\\
o_2:&S+\beta+\gamma &\longrightarrow S+\gamma+\delta,\\
o_3:&S+\alpha+\beta  &\longrightarrow S+\beta+\delta.
\end{array}                                         \tag{2.1}
\]

Their lower palette is `S+{alpha,gamma,beta}`, their upper palette is

\[
 S+\{\alpha\gamma\delta,
      \beta\gamma\delta,
      \alpha\beta\delta\},                         \tag{2.2}
\]

and their tail/head palettes are the two columns in (2.1).  Replace them by

\[
\begin{array}{lll}
n_1:&S+\alpha+\beta &\longrightarrow S+\alpha+\delta,\\
n_2:&S+\alpha+\gamma&\longrightarrow S+\gamma+\delta,\\
n_3:&S+\beta+\gamma &\longrightarrow S+\beta+\delta.
\end{array}                                         \tag{2.3}
\]

Direct intersection and union give

\[
 \operatorname{res}\{o_1,o_2,o_3\}
 =\operatorname{res}\{n_1,n_2,n_3\}               \tag{2.4}
\]

in the lower, upper, tail, and head rows separately.  Both triples are
matchings on the same six middle vertices.  Hence (2.1)--(2.3) are one
literal directed Boolean `C6`.  This holds independently for all ten
choices of `X`.

## 3. Exact fusion theorem

### Theorem 3.1 (`15C4 -> C60`)

Let `Q_old` use phase `E+` in all six endpoint fibres, and let `R_old` be
the union of the three vertical banks.  Let `Q_new` switch the three
`A_j` fibres to `E-`, leaving the `B_j` fibres fixed.  Finally, at one
chosen `X`, replace (2.1) by (2.3), obtaining `R_new`.

Then:

1. `Q_old,Q_new` are 30-diamond matchings with identical lower, upper,
   tail, and head palettes;
2. `R_old,R_new` are 30-diamond matchings with identical four palettes;
3. every one of the four rows of the complete 60-diamond table is literal
   and injective; and
4. the physical topology changes as

\[
 Q_{old}\cup R_{old}=15C_4,qquad
 Q_{new}\cup R_{old}=3C_{20},qquad
 Q_{new}\cup R_{new}=C_{60}.                       \tag{3.1}
\]

Thus three primitive fibre `C10` moves followed by one Boolean `C6` reduce
the graphic cycle nullity from `15` to `1`, preserving all four resource
rows and both bank labels exactly.

#### Proof

Resource disjointness follows from (1.3); horizontal and vertical resources
cannot cross-collide because their `H`-intersection sizes differ.  The
single-socket `C10` theorem gives `5C4 -> C20` and exact directed palettes
in each socket.  Applying it independently gives the first two topology
states in (3.1).

Delete the three old edges (2.1).  This opens the three `C20` cycles into
three directed paths.  The new matching (2.3) joins their endpoints by a
3-cycle: path 1 flows into path 2, path 2 into path 3, and path 3 into path
1.  It therefore makes one directed cycle using all sixty middle vertices.
Equation (2.4) proves exact four-row preservation, and its six middle
vertices are distinct, so the vertical bank remains a matching.  QED.

### Corollary 3.2 (sharp residual opening debt)

No internal equal-size move can make this closed 60-vertex table a forest:
both banks are perfect matchings, so their union is 2-regular.  The final
`C60` attains the minimum possible cycle count, one.  Deleting any one
untouched vertical edge gives a spanning `P60` but loses that edge's lower
and upper colours.  Hence the exact residual is one named opening ticket.

## 4. Exact count and load ledger

Put `h=2m-5`.  For fixed `K`, the number of directed modules is

\[
 N_m=8\binom{h}{m-4}\binom{m-1}{4}.                \tag{4.1}
\]

Indeed choose `C_0`, an unordered four-marker set, one of four common
markers `delta`, and one of the two directions of the Boolean hex.  Each
module contains ten possible fusion tickets `X`; distinguishing the ticket
multiplies (4.1) by ten.

Across the directed modules, the exact loads on one fixed `H` core are

\[
\begin{array}{c|c}
\text{resource-core type}&\text{load}\\ \hline
|P|=m-2\quad\text{horizontal}&
 8\binom{m-2}{2}\binom{m-3}{2}\\[1mm]
|L|=m-3\quad\text{vertical lower}&
 6(m-3)\binom{m-2}{3}\\[1mm]
|D|=m-1\quad\text{vertical upper}&
 6(m-4)\binom{m-1}{3}.
\end{array}                                         \tag{4.2}
\]

All are `O(m^4)`.  They count directed module choices, not a disjoint
packing and not global host acceptance.

## 5. Scope

The theorem supplies a literal, palette-exact, topology-improving local
module and ten internal fusion choices.  It does **not** prove:

* that a complete central table contains a compatible module;
* that many modules can be planted with histories or reset addresses;
* that the final opening ticket is repaired;
* residence, deep upper support, source chronology, or compiler transport.

The lightweight verifier is

```text
scratch/a_three_socket_c10_c6_fusion_20260802/
  audit_a_three_socket_c10_c6_fusion_20260802.py
```

and replays the literal construction for `5 <= m <= 20`.
